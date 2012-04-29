#!/usr/bin/env python
#coding=utf-8
'''
Created on 2012-4-20

@author: Chine
'''

import datetime
import urllib2
import time
import mimetypes

from errors import S3Error
from utils import XML, hmac_sha1, calc_md5

__author__ = "Chine King"
__description__ = "A client for Amazon S3 api, site: http://aws.amazon.com/documentation/s3/"
__all__ = ['X_AMZ_ACL', 'S3Bucket', 'S3Object', 'AmazonUser', 'S3Client']

ACTION_TYPES = ('PUT', 'GET', 'DELETE')
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
STRING_TO_SIGN = '''%(action)s
%(content_md5)s
%(content_type)s
%(date)s
%(c_amz_headers)s%(c_resource)s'''

end_point = "http://s3.amazonaws.com"
def get_end_point(bucket_name=None, obj_name=None, http=False):
    prefix = 'http://' if http else ''
    url = '%s%ss3.amazonaws.com' % (prefix, 
                                    bucket_name+'.' if bucket_name else '')
    if not obj_name:
        return url
    return url + obj_name if obj_name.startswith('/') else url + '/' + obj_name

class XAmzAcl(object):
    def __init__(self):
        for val in ('private', 'public-read', 'public-read-write', 
                    'authenticated-read', 'bucket-owner-read', 
                    'bucket-owner-full-control'):
            setattr(self, val.replace('-', '_'), val)
X_AMZ_ACL = XAmzAcl()

class S3Base(object):
    def __init__(self, **kwargs):
        if len(kwargs) > 0 and hasattr(self, 'mapping'):
            reversed_mapping = {}
            for k, v in self.mapping.iteritems():
                reversed_mapping[v.lower()] = k
            
            for k, v in kwargs.iteritems():
                if k in reversed_mapping:
                    setattr(self, reversed_mapping[k], v)                    

class S3Bucket(S3Base):
    mapping = {'name': 'Name',
               'create_date': 'CreationDate',
               'prefix': 'Prefix',
               'marker': 'Marker',
               'max_keys': 'MaxKeys',
               'is_truncated': 'IsTruncated'}
    
    @classmethod    
    def from_xml(cls, tree):
        bucket = S3Bucket()
        
        for k, v in cls.mapping.iteritems():
            tag = tree.find(v)
            if hasattr(tag, 'text'):
                setattr(bucket, k, tag.text)
                
        return bucket
        

class S3Object(S3Base):
    mapping = {'key': 'Key',
               'last_modified': 'LastModified',
               'etag': 'ETag',
               'size': 'Size',
               'storage_class': 'StorageClass',
               'is_truncated': 'IsTruncated',
               'date': 'Date',
               'content_length': 'Content-Length',
               'content_type': 'Content-Type'}
    
    def __init__(self, **kwargs):
        if 'data' in kwargs:
            self.data = kwargs.pop('data')
        super(S3Object, self).__init__(**kwargs)
    
    @classmethod    
    def from_xml(cls, tree):
        obj = S3Object()
        
        for k, v in cls.mapping.iteritems():
            tag = tree.find(v)
            if hasattr(tag, 'text'):
                setattr(obj, k, tag.text)
                
        owner = tree.find('Owner')
        if owner is not None:
            obj.owner = AmazonUser.from_xml(owner)
                
        return obj

class AmazonUser(object):
    mapping = {'id_': 'ID',
               'display_name': 'DisplayName'}
    
    def __init__(self, id_=None, display_name=None):
        self.id_ = id_
        self.display_name = display_name
        
    @classmethod
    def from_xml(cls, tree):
        user = AmazonUser()
        
        for k, v in cls.mapping.iteritems():
            tag = tree.find(v)
            if hasattr(tag, 'text'):
                setattr(user, k, tag.text)
                
        return user

class S3Request(object):
    def __init__(self, access_key, secret_access_key, 
                 action, bucket_name=None, obj_name=None,
                 data=None, content_type=None, metadata={}, amz_headers={} ):
        
        assert action in ACTION_TYPES # action must be PUT, GET and DELETE.
        
        self.access_key = access_key
        self.secret_key = secret_access_key
        self.action = action
        
        self.bucket_name = bucket_name
        self.obj_name = obj_name
        self.data = data
        
        self.content_type = content_type
        self._set_content_type()
        
        self.metadata = metadata
        self.amz_headers = amz_headers
        
        self.date_str = self._get_date_str()
        
        self.host = get_end_point(self.bucket_name)
        self.end_point = get_end_point(self.bucket_name, self.obj_name, True)
            
    def _get_date_str(self):
        return datetime.datetime.utcnow().strftime(GMT_FORMAT)
    
    def _set_content_type(self):
        if self.obj_name is not None and not self.content_type:
            self.content_type = mimetypes.guess_type(self.obj_name)[0]
            
    def _get_canonicalized_resource(self):
        path = '/'
        if self.bucket_name:
            path += self.bucket_name
        if self.bucket_name and self.obj_name:
            if not self.obj_name.startswith('/'):
                path += '/'
            path += self.obj_name
        elif self.bucket_name and not path.endswith('/'):
            path += '/'
            
        return path
    
    def _get_canoicalized_amz_headers(self, headers):
        amz_headers = [(k.lower(), v) for k, v in headers.iteritems() 
                       if k.lower().startswith('x-amz-')]
        amz_headers.sort()
        return ''.join(['%s:%s' % (k, v) for k, v in amz_headers])
    
    def _get_authorization(self, headers):
        string_to_sign = STRING_TO_SIGN % {
                            'action': self.action,
                            'content_md5': headers.get('Content-MD5', ''),
                            'content_type': headers.get('Content-Type', ''),
                            'date': self.date_str,
                            'c_amz_headers': self._get_canoicalized_amz_headers(headers),
                            'c_resource': self._get_canonicalized_resource()
                         }
        signature = hmac_sha1(self.secret_key, string_to_sign)
        
        return "AWS %s:%s" % (self.access_key, signature)
    
    def get_headers(self):
        headers = { 
                   'Date': self.date_str
                   }
        if self.data:
            headers['Content-Length'] = len(self.data)
            headers['Content-MD5'] = calc_md5(self.data)
            
        if self.content_type is not None:
            headers['Content-Type'] = self.content_type
            
        if self.bucket_name:
            headers['Host'] = self.host
        
        for k, v in self.metadata.iteritems():
            headers['x-amz-meta-' + k] = v
        for k, v in self.amz_headers.iteritems():
            headers['x-amz-' + k] = v
            
        headers['Authorization'] = self._get_authorization(headers)
        return headers
    
    def submit(self, try_times=3, try_interval=3, callback=None, include_headers=False):
        def _get_data():
            headers = self.get_headers()
            try:
                opener = urllib2.build_opener(urllib2.HTTPHandler)
                req = urllib2.Request(self.end_point, data=self.data, headers=headers)
                req.get_method = lambda: self.action
                resp = opener.open(req)
                
                if include_headers:
                    return resp.read(), resp.headers.dict
                return resp.read()
            except urllib2.HTTPError, e:
                #c = e.read()
                #print c
                #tree = XML.loads(c)
                tree = XML.loads(e.read())
                raise S3Error(tree, e.code)
            
        for i in range(try_times):
            try:
                if include_headers and callback:
                    data, headers = _get_data()
                    return callback(data, headers)
                if callback:
                    return callback(_get_data())
                return _get_data()
            except urllib2.URLError:
                time.sleep(try_interval)
    
class S3Response(object):
    def __init__(self):
        pass

class S3Client(object):
    def __init__(self, access_key, secret_access_key):
        self.access_key = access_key
        self.secret_key = secret_access_key
        
    def _parse_list_buckets(self, data):
        tree = XML.loads(data)
        owner = AmazonUser.from_xml(tree.find('Owner'))
        
        buckets = []
        for ele in tree.find('Buckets').getchildren():
            buckets.append(S3Bucket.from_xml(ele))
            
        return owner, buckets
        
    def list_buckets(self):
        req = S3Request(self.access_key, self.secret_key, 'GET')
        return req.submit(callback=self._parse_list_buckets)
    
    def put_bucket(self, bucket_name, x_amz_acl=X_AMZ_ACL.private):
        amz_headers = {}
        if x_amz_acl != X_AMZ_ACL.private:
            amz_headers['acl'] = x_amz_acl
        
        req = S3Request(self.access_key, self.secret_key, 'PUT', 
                        bucket_name=bucket_name, amz_headers=amz_headers)
        
        return req.submit()
    
    def _parse_get_bucket(self, data):
        tree = XML.loads(data)
        bucket = S3Bucket.from_xml(tree)
        
        objs = []
        for ele in tree.findall('Contents'):
            obj = S3Object.from_xml(ele)
            obj.bucket = bucket
            objs.append(obj)
            
        return objs
    
    def get_bucket(self, bucket_name):
        req = S3Request(self.access_key, self.secret_key, 'GET',
                        bucket_name=bucket_name)
        return req.submit(callback=self._parse_get_bucket)
    
    def delete_bucket(self, bucket_name):
        req = S3Request(self.access_key, self.secret_key, 'DELETE',
                        bucket_name=bucket_name)
        return req.submit()
    
    def put_object(self, bucket_name, obj_name, data, content_type=None, 
                   metadata={}, amz_headers={}):
        req = S3Request(self.access_key, self.secret_key, 'PUT',
                        bucket_name=bucket_name, obj_name=obj_name, data=data,
                        content_type=content_type, metadata=metadata, amz_headers=amz_headers)
        return req.submit()
    
    def get_object(self, bucket_name, obj_name):
        req = S3Request(self.access_key, self.secret_key, 'GET',
                        bucket_name=bucket_name, obj_name=obj_name)
        return req.submit(include_headers=True, callback=lambda data, headers: S3Object(data=data, **headers))
    
    def delete_object(self, bucket_name, obj_name):
        req = S3Request(self.access_key, self.secret_key, 'DELETE',
                        bucket_name=bucket_name, obj_name=obj_name)
        return req.submit()
    
    def upload_file(self, filename, bucket_name, obj_name, x_amz_acl=X_AMZ_ACL.private,
                    encrypt=False, encrypt_func=None):
        fp = open(filename, 'rb')
        try:
            amz_headers = {}
            if x_amz_acl != X_AMZ_ACL.private:
                amz_headers['acl'] = x_amz_acl
                
            data = fp.read()
            if encrypt and encrypt_func is not None:
                data = encrypt_func(data)
                
            self.put_object(bucket_name, obj_name, data, amz_headers=amz_headers)
        finally:
            fp.close()
            
    def download_file(self, filename, bucket_name, obj_name, 
                      decrypt=False, decrypt_func=None):
        fp = open(filename, 'wb')
        try:
            data = self.get_object(bucket_name, obj_name).data
            
            if decrypt and decrypt_func is not None:
                data = decrypt_func(data)
            
            fp.write(data)
        finally:
            fp.close()
        
        
if __name__ == "__main__":
    from CloudBackup.test.settings import *
    
    client = S3Client(S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY)