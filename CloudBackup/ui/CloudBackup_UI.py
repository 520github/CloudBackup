# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CloudBackup.ui'
#
# Created: Sun May 27 00:11:51 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CloudBackupUI(object):
    def setupUi(self, CloudBackupUI):
        CloudBackupUI.setObjectName(_fromUtf8("CloudBackupUI"))
        CloudBackupUI.resize(710, 500)
        self.CloudSelectTabWidget = QtGui.QTabWidget(CloudBackupUI)
        self.CloudSelectTabWidget.setGeometry(QtCore.QRect(20, 20, 671, 461))
        self.CloudSelectTabWidget.setObjectName(_fromUtf8("CloudSelectTabWidget"))
        self.vdisktab = QtGui.QWidget()
        self.vdisktab.setObjectName(_fromUtf8("vdisktab"))
        self.OpTabWidget_under_vdisk = QtGui.QTabWidget(self.vdisktab)
        self.OpTabWidget_under_vdisk.setGeometry(QtCore.QRect(20, 20, 631, 381))
        self.OpTabWidget_under_vdisk.setObjectName(_fromUtf8("OpTabWidget_under_vdisk"))
        self.syntab_under_vdisk = QtGui.QWidget()
        self.syntab_under_vdisk.setObjectName(_fromUtf8("syntab_under_vdisk"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.syntab_under_vdisk)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 531, 51))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.vgridLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.vgridLayout.setMargin(0)
        self.vgridLayout.setHorizontalSpacing(10)
        self.vgridLayout.setVerticalSpacing(0)
        self.vgridLayout.setObjectName(_fromUtf8("vgridLayout"))
        self.lvdirpath = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lvdirpath.setObjectName(_fromUtf8("lvdirpath"))
        self.vgridLayout.addWidget(self.lvdirpath, 0, 0, 1, 1)
        self.tvdirpath = QtGui.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tvdirpath.sizePolicy().hasHeightForWidth())
        self.tvdirpath.setSizePolicy(sizePolicy)
        self.tvdirpath.setObjectName(_fromUtf8("tvdirpath"))
        self.vgridLayout.addWidget(self.tvdirpath, 0, 1, 1, 1)
        self.gridLayoutWidget = QtGui.QWidget(self.syntab_under_vdisk)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 190, 411, 51))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.vgridLayout_button = QtGui.QGridLayout(self.gridLayoutWidget)
        self.vgridLayout_button.setContentsMargins(30, -1, 30, -1)
        self.vgridLayout_button.setHorizontalSpacing(30)
        self.vgridLayout_button.setObjectName(_fromUtf8("vgridLayout_button"))
        self.button_v_reset = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_v_reset.setObjectName(_fromUtf8("button_v_reset"))
        self.vgridLayout_button.addWidget(self.button_v_reset, 0, 2, 1, 1)
        self.button_v_submit = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_v_submit.setObjectName(_fromUtf8("button_v_submit"))
        self.vgridLayout_button.addWidget(self.button_v_submit, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.syntab_under_vdisk)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(560, 120, 61, 51))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.vgridLayout_dir = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.vgridLayout_dir.setMargin(0)
        self.vgridLayout_dir.setObjectName(_fromUtf8("vgridLayout_dir"))
        self.button_v_dir = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.button_v_dir.setObjectName(_fromUtf8("button_v_dir"))
        self.vgridLayout_dir.addWidget(self.button_v_dir, 0, 0, 1, 1)
        self.OpTabWidget_under_vdisk.addTab(self.syntab_under_vdisk, _fromUtf8(""))
        self.sharetab_under_vdisk = QtGui.QWidget()
        self.sharetab_under_vdisk.setObjectName(_fromUtf8("sharetab_under_vdisk"))
        self.VtreeWidget = QtGui.QTreeWidget(self.sharetab_under_vdisk)
        self.VtreeWidget.setGeometry(QtCore.QRect(20, 21, 581, 291))
        self.VtreeWidget.setObjectName(_fromUtf8("VtreeWidget"))
        self.VtreeWidget.headerItem().setText(0, _fromUtf8("同步文件"))
        self.button_v_share = QtGui.QPushButton(self.sharetab_under_vdisk)
        self.button_v_share.setGeometry(QtCore.QRect(480, 320, 121, 28))
        self.button_v_share.setObjectName(_fromUtf8("button_v_share"))
        self.button_v_cloudflush = QtGui.QPushButton(self.sharetab_under_vdisk)
        self.button_v_cloudflush.setGeometry(QtCore.QRect(400, 320, 71, 28))
        self.button_v_cloudflush.setObjectName(_fromUtf8("button_v_cloudflush"))
        self.OpTabWidget_under_vdisk.addTab(self.sharetab_under_vdisk, _fromUtf8(""))
        self.logtab_under_vdisk = QtGui.QWidget()
        self.logtab_under_vdisk.setObjectName(_fromUtf8("logtab_under_vdisk"))
        self.button_v_logflush = QtGui.QPushButton(self.logtab_under_vdisk)
        self.button_v_logflush.setGeometry(QtCore.QRect(510, 320, 93, 28))
        self.button_v_logflush.setObjectName(_fromUtf8("button_v_logflush"))
        self.VlogTreeWidget = QtGui.QTreeWidget(self.logtab_under_vdisk)
        self.VlogTreeWidget.setGeometry(QtCore.QRect(20, 21, 581, 291))
        self.VlogTreeWidget.setColumnCount(2)
        self.VlogTreeWidget.setObjectName(_fromUtf8("VlogTreeWidget"))
        self.OpTabWidget_under_vdisk.addTab(self.logtab_under_vdisk, _fromUtf8(""))
        self.lvuserstate = QtGui.QLabel(self.vdisktab)
        self.lvuserstate.setGeometry(QtCore.QRect(370, 410, 271, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvuserstate.sizePolicy().hasHeightForWidth())
        self.lvuserstate.setSizePolicy(sizePolicy)
        self.lvuserstate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lvuserstate.setObjectName(_fromUtf8("lvuserstate"))
        self.CloudSelectTabWidget.addTab(self.vdisktab, _fromUtf8(""))
        self.s3tab = QtGui.QWidget()
        self.s3tab.setObjectName(_fromUtf8("s3tab"))
        self.OpTabWidget_under_s3 = QtGui.QTabWidget(self.s3tab)
        self.OpTabWidget_under_s3.setGeometry(QtCore.QRect(20, 20, 631, 381))
        self.OpTabWidget_under_s3.setObjectName(_fromUtf8("OpTabWidget_under_s3"))
        self.syntab_under_s3 = QtGui.QWidget()
        self.syntab_under_s3.setObjectName(_fromUtf8("syntab_under_s3"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.syntab_under_s3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 120, 531, 51))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.sgridLayout = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.sgridLayout.setMargin(0)
        self.sgridLayout.setHorizontalSpacing(10)
        self.sgridLayout.setVerticalSpacing(0)
        self.sgridLayout.setObjectName(_fromUtf8("sgridLayout"))
        self.lsdirpath = QtGui.QLabel(self.gridLayoutWidget_4)
        self.lsdirpath.setObjectName(_fromUtf8("lsdirpath"))
        self.sgridLayout.addWidget(self.lsdirpath, 0, 0, 1, 1)
        self.tsdirpath = QtGui.QLineEdit(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tsdirpath.sizePolicy().hasHeightForWidth())
        self.tsdirpath.setSizePolicy(sizePolicy)
        self.tsdirpath.setObjectName(_fromUtf8("tsdirpath"))
        self.sgridLayout.addWidget(self.tsdirpath, 0, 1, 1, 1)
        self.gridLayoutWidget_5 = QtGui.QWidget(self.syntab_under_s3)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(110, 190, 411, 51))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.sgridLayout_button = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.sgridLayout_button.setContentsMargins(30, -1, 30, -1)
        self.sgridLayout_button.setHorizontalSpacing(30)
        self.sgridLayout_button.setObjectName(_fromUtf8("sgridLayout_button"))
        self.button_s_reset = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.button_s_reset.setObjectName(_fromUtf8("button_s_reset"))
        self.sgridLayout_button.addWidget(self.button_s_reset, 0, 2, 1, 1)
        self.button_s_submit = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.button_s_submit.setObjectName(_fromUtf8("button_s_submit"))
        self.sgridLayout_button.addWidget(self.button_s_submit, 0, 1, 1, 1)
        self.gridLayoutWidget_6 = QtGui.QWidget(self.syntab_under_s3)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(560, 120, 61, 51))
        self.gridLayoutWidget_6.setObjectName(_fromUtf8("gridLayoutWidget_6"))
        self.sgridLayout_dir = QtGui.QGridLayout(self.gridLayoutWidget_6)
        self.sgridLayout_dir.setMargin(0)
        self.sgridLayout_dir.setObjectName(_fromUtf8("sgridLayout_dir"))
        self.button_s_dir = QtGui.QPushButton(self.gridLayoutWidget_6)
        self.button_s_dir.setObjectName(_fromUtf8("button_s_dir"))
        self.sgridLayout_dir.addWidget(self.button_s_dir, 0, 0, 1, 1)
        self.OpTabWidget_under_s3.addTab(self.syntab_under_s3, _fromUtf8(""))
        self.sharetab_under_s3 = QtGui.QWidget()
        self.sharetab_under_s3.setObjectName(_fromUtf8("sharetab_under_s3"))
        self.StreeWidget = QtGui.QTreeWidget(self.sharetab_under_s3)
        self.StreeWidget.setGeometry(QtCore.QRect(20, 21, 581, 291))
        self.StreeWidget.setObjectName(_fromUtf8("StreeWidget"))
        self.StreeWidget.headerItem().setText(0, _fromUtf8("同步文件"))
        self.button_s_share = QtGui.QPushButton(self.sharetab_under_s3)
        self.button_s_share.setGeometry(QtCore.QRect(480, 320, 121, 28))
        self.button_s_share.setObjectName(_fromUtf8("button_s_share"))
        self.button_s_cloudflush = QtGui.QPushButton(self.sharetab_under_s3)
        self.button_s_cloudflush.setGeometry(QtCore.QRect(400, 320, 71, 28))
        self.button_s_cloudflush.setObjectName(_fromUtf8("button_s_cloudflush"))
        self.OpTabWidget_under_s3.addTab(self.sharetab_under_s3, _fromUtf8(""))
        self.logtab_under_s3 = QtGui.QWidget()
        self.logtab_under_s3.setObjectName(_fromUtf8("logtab_under_s3"))
        self.SlogTreeWidget = QtGui.QTreeWidget(self.logtab_under_s3)
        self.SlogTreeWidget.setGeometry(QtCore.QRect(20, 21, 581, 291))
        self.SlogTreeWidget.setObjectName(_fromUtf8("SlogTreeWidget"))
        self.button_s_logflush = QtGui.QPushButton(self.logtab_under_s3)
        self.button_s_logflush.setGeometry(QtCore.QRect(510, 320, 93, 28))
        self.button_s_logflush.setObjectName(_fromUtf8("button_s_logflush"))
        self.OpTabWidget_under_s3.addTab(self.logtab_under_s3, _fromUtf8(""))
        self.lsuserstate = QtGui.QLabel(self.s3tab)
        self.lsuserstate.setGeometry(QtCore.QRect(370, 410, 271, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lsuserstate.sizePolicy().hasHeightForWidth())
        self.lsuserstate.setSizePolicy(sizePolicy)
        self.lsuserstate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lsuserstate.setObjectName(_fromUtf8("lsuserstate"))
        self.CloudSelectTabWidget.addTab(self.s3tab, _fromUtf8(""))
        self.gctab = QtGui.QWidget()
        self.gctab.setObjectName(_fromUtf8("gctab"))
        self.OpTabWidget_under_google = QtGui.QTabWidget(self.gctab)
        self.OpTabWidget_under_google.setGeometry(QtCore.QRect(20, 20, 631, 381))
        self.OpTabWidget_under_google.setObjectName(_fromUtf8("OpTabWidget_under_google"))
        self.syntab_under_google = QtGui.QWidget()
        self.syntab_under_google.setObjectName(_fromUtf8("syntab_under_google"))
        self.gridLayoutWidget_7 = QtGui.QWidget(self.syntab_under_google)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(20, 120, 531, 51))
        self.gridLayoutWidget_7.setObjectName(_fromUtf8("gridLayoutWidget_7"))
        self.ggridLayout = QtGui.QGridLayout(self.gridLayoutWidget_7)
        self.ggridLayout.setMargin(0)
        self.ggridLayout.setHorizontalSpacing(10)
        self.ggridLayout.setVerticalSpacing(0)
        self.ggridLayout.setObjectName(_fromUtf8("ggridLayout"))
        self.lgdirpath = QtGui.QLabel(self.gridLayoutWidget_7)
        self.lgdirpath.setObjectName(_fromUtf8("lgdirpath"))
        self.ggridLayout.addWidget(self.lgdirpath, 0, 0, 1, 1)
        self.tgdirpath = QtGui.QLineEdit(self.gridLayoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tgdirpath.sizePolicy().hasHeightForWidth())
        self.tgdirpath.setSizePolicy(sizePolicy)
        self.tgdirpath.setObjectName(_fromUtf8("tgdirpath"))
        self.ggridLayout.addWidget(self.tgdirpath, 0, 1, 1, 1)
        self.gridLayoutWidget_8 = QtGui.QWidget(self.syntab_under_google)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(110, 190, 411, 51))
        self.gridLayoutWidget_8.setObjectName(_fromUtf8("gridLayoutWidget_8"))
        self.ggridLayout_button = QtGui.QGridLayout(self.gridLayoutWidget_8)
        self.ggridLayout_button.setContentsMargins(30, -1, 30, -1)
        self.ggridLayout_button.setHorizontalSpacing(30)
        self.ggridLayout_button.setObjectName(_fromUtf8("ggridLayout_button"))
        self.button_g_reset = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.button_g_reset.setObjectName(_fromUtf8("button_g_reset"))
        self.ggridLayout_button.addWidget(self.button_g_reset, 0, 2, 1, 1)
        self.button_g_submit = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.button_g_submit.setObjectName(_fromUtf8("button_g_submit"))
        self.ggridLayout_button.addWidget(self.button_g_submit, 0, 1, 1, 1)
        self.gridLayoutWidget_9 = QtGui.QWidget(self.syntab_under_google)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(560, 120, 61, 51))
        self.gridLayoutWidget_9.setObjectName(_fromUtf8("gridLayoutWidget_9"))
        self.ggridLayout_dir = QtGui.QGridLayout(self.gridLayoutWidget_9)
        self.ggridLayout_dir.setMargin(0)
        self.ggridLayout_dir.setObjectName(_fromUtf8("ggridLayout_dir"))
        self.button_g_dir = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.button_g_dir.setObjectName(_fromUtf8("button_g_dir"))
        self.ggridLayout_dir.addWidget(self.button_g_dir, 0, 0, 1, 1)
        self.OpTabWidget_under_google.addTab(self.syntab_under_google, _fromUtf8(""))
        self.sharetab_under_google = QtGui.QWidget()
        self.sharetab_under_google.setObjectName(_fromUtf8("sharetab_under_google"))
        self.GtreeWidget = QtGui.QTreeWidget(self.sharetab_under_google)
        self.GtreeWidget.setGeometry(QtCore.QRect(20, 21, 581, 291))
        self.GtreeWidget.setObjectName(_fromUtf8("GtreeWidget"))
        self.GtreeWidget.headerItem().setText(0, _fromUtf8("同步文件"))
        self.button_g_share = QtGui.QPushButton(self.sharetab_under_google)
        self.button_g_share.setGeometry(QtCore.QRect(480, 320, 121, 28))
        self.button_g_share.setObjectName(_fromUtf8("button_g_share"))
        self.button_g_cloudflush = QtGui.QPushButton(self.sharetab_under_google)
        self.button_g_cloudflush.setGeometry(QtCore.QRect(400, 320, 71, 28))
        self.button_g_cloudflush.setObjectName(_fromUtf8("button_g_cloudflush"))
        self.OpTabWidget_under_google.addTab(self.sharetab_under_google, _fromUtf8(""))
        self.logtab_under_google = QtGui.QWidget()
        self.logtab_under_google.setObjectName(_fromUtf8("logtab_under_google"))
        self.GlogTreeWidget = QtGui.QTreeWidget(self.logtab_under_google)
        self.GlogTreeWidget.setGeometry(QtCore.QRect(20, 21, 581, 291))
        self.GlogTreeWidget.setObjectName(_fromUtf8("GlogTreeWidget"))
        self.button_g_logflush = QtGui.QPushButton(self.logtab_under_google)
        self.button_g_logflush.setGeometry(QtCore.QRect(510, 320, 93, 28))
        self.button_g_logflush.setObjectName(_fromUtf8("button_g_logflush"))
        self.OpTabWidget_under_google.addTab(self.logtab_under_google, _fromUtf8(""))
        self.lguserstate = QtGui.QLabel(self.gctab)
        self.lguserstate.setGeometry(QtCore.QRect(370, 410, 271, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lguserstate.sizePolicy().hasHeightForWidth())
        self.lguserstate.setSizePolicy(sizePolicy)
        self.lguserstate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lguserstate.setObjectName(_fromUtf8("lguserstate"))
        self.CloudSelectTabWidget.addTab(self.gctab, _fromUtf8(""))

        self.retranslateUi(CloudBackupUI)
        self.CloudSelectTabWidget.setCurrentIndex(0)
        self.OpTabWidget_under_vdisk.setCurrentIndex(0)
        self.OpTabWidget_under_s3.setCurrentIndex(0)
        self.OpTabWidget_under_google.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CloudBackupUI)

    def retranslateUi(self, CloudBackupUI):
        CloudBackupUI.setWindowTitle(QtGui.QApplication.translate("CloudBackupUI", "云备份", None, QtGui.QApplication.UnicodeUTF8))
        self.lvdirpath.setText(QtGui.QApplication.translate("CloudBackupUI", "同步文件夹", None, QtGui.QApplication.UnicodeUTF8))
        self.button_v_reset.setText(QtGui.QApplication.translate("CloudBackupUI", "停止同步", None, QtGui.QApplication.UnicodeUTF8))
        self.button_v_submit.setText(QtGui.QApplication.translate("CloudBackupUI", "开始同步", None, QtGui.QApplication.UnicodeUTF8))
        self.button_v_dir.setText(QtGui.QApplication.translate("CloudBackupUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_vdisk.setTabText(self.OpTabWidget_under_vdisk.indexOf(self.syntab_under_vdisk), QtGui.QApplication.translate("CloudBackupUI", "同步设定", None, QtGui.QApplication.UnicodeUTF8))
        self.button_v_share.setText(QtGui.QApplication.translate("CloudBackupUI", "用邮件分享", None, QtGui.QApplication.UnicodeUTF8))
        self.button_v_cloudflush.setText(QtGui.QApplication.translate("CloudBackupUI", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_vdisk.setTabText(self.OpTabWidget_under_vdisk.indexOf(self.sharetab_under_vdisk), QtGui.QApplication.translate("CloudBackupUI", "分享设定", None, QtGui.QApplication.UnicodeUTF8))
        self.button_v_logflush.setText(QtGui.QApplication.translate("CloudBackupUI", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.VlogTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("CloudBackupUI", "时间", None, QtGui.QApplication.UnicodeUTF8))
        self.VlogTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("CloudBackupUI", "动作", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_vdisk.setTabText(self.OpTabWidget_under_vdisk.indexOf(self.logtab_under_vdisk), QtGui.QApplication.translate("CloudBackupUI", "用户日志", None, QtGui.QApplication.UnicodeUTF8))
        self.lvuserstate.setText(QtGui.QApplication.translate("CloudBackupUI", "用户登录状态", None, QtGui.QApplication.UnicodeUTF8))
        self.CloudSelectTabWidget.setTabText(self.CloudSelectTabWidget.indexOf(self.vdisktab), QtGui.QApplication.translate("CloudBackupUI", "微盘", None, QtGui.QApplication.UnicodeUTF8))
        self.lsdirpath.setText(QtGui.QApplication.translate("CloudBackupUI", "同步文件夹", None, QtGui.QApplication.UnicodeUTF8))
        self.button_s_reset.setText(QtGui.QApplication.translate("CloudBackupUI", "停止同步", None, QtGui.QApplication.UnicodeUTF8))
        self.button_s_submit.setText(QtGui.QApplication.translate("CloudBackupUI", "开始同步", None, QtGui.QApplication.UnicodeUTF8))
        self.button_s_dir.setText(QtGui.QApplication.translate("CloudBackupUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_s3.setTabText(self.OpTabWidget_under_s3.indexOf(self.syntab_under_s3), QtGui.QApplication.translate("CloudBackupUI", "同步设定", None, QtGui.QApplication.UnicodeUTF8))
        self.button_s_share.setText(QtGui.QApplication.translate("CloudBackupUI", "用邮件分享", None, QtGui.QApplication.UnicodeUTF8))
        self.button_s_cloudflush.setText(QtGui.QApplication.translate("CloudBackupUI", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_s3.setTabText(self.OpTabWidget_under_s3.indexOf(self.sharetab_under_s3), QtGui.QApplication.translate("CloudBackupUI", "分享设定", None, QtGui.QApplication.UnicodeUTF8))
        self.SlogTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("CloudBackupUI", "时间", None, QtGui.QApplication.UnicodeUTF8))
        self.SlogTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("CloudBackupUI", "动作", None, QtGui.QApplication.UnicodeUTF8))
        self.button_s_logflush.setText(QtGui.QApplication.translate("CloudBackupUI", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_s3.setTabText(self.OpTabWidget_under_s3.indexOf(self.logtab_under_s3), QtGui.QApplication.translate("CloudBackupUI", "用户日志", None, QtGui.QApplication.UnicodeUTF8))
        self.lsuserstate.setText(QtGui.QApplication.translate("CloudBackupUI", "用户登录状态", None, QtGui.QApplication.UnicodeUTF8))
        self.CloudSelectTabWidget.setTabText(self.CloudSelectTabWidget.indexOf(self.s3tab), QtGui.QApplication.translate("CloudBackupUI", "亚马逊S3", None, QtGui.QApplication.UnicodeUTF8))
        self.lgdirpath.setText(QtGui.QApplication.translate("CloudBackupUI", "同步文件夹", None, QtGui.QApplication.UnicodeUTF8))
        self.button_g_reset.setText(QtGui.QApplication.translate("CloudBackupUI", "停止同步", None, QtGui.QApplication.UnicodeUTF8))
        self.button_g_submit.setText(QtGui.QApplication.translate("CloudBackupUI", "开始同步", None, QtGui.QApplication.UnicodeUTF8))
        self.button_g_dir.setText(QtGui.QApplication.translate("CloudBackupUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_google.setTabText(self.OpTabWidget_under_google.indexOf(self.syntab_under_google), QtGui.QApplication.translate("CloudBackupUI", "同步设定", None, QtGui.QApplication.UnicodeUTF8))
        self.button_g_share.setText(QtGui.QApplication.translate("CloudBackupUI", "用邮件分享", None, QtGui.QApplication.UnicodeUTF8))
        self.button_g_cloudflush.setText(QtGui.QApplication.translate("CloudBackupUI", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_google.setTabText(self.OpTabWidget_under_google.indexOf(self.sharetab_under_google), QtGui.QApplication.translate("CloudBackupUI", "分享设定", None, QtGui.QApplication.UnicodeUTF8))
        self.GlogTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("CloudBackupUI", "时间", None, QtGui.QApplication.UnicodeUTF8))
        self.GlogTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("CloudBackupUI", "动作", None, QtGui.QApplication.UnicodeUTF8))
        self.button_g_logflush.setText(QtGui.QApplication.translate("CloudBackupUI", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.OpTabWidget_under_google.setTabText(self.OpTabWidget_under_google.indexOf(self.logtab_under_google), QtGui.QApplication.translate("CloudBackupUI", "用户日志", None, QtGui.QApplication.UnicodeUTF8))
        self.lguserstate.setText(QtGui.QApplication.translate("CloudBackupUI", "用户登录状态", None, QtGui.QApplication.UnicodeUTF8))
        self.CloudSelectTabWidget.setTabText(self.CloudSelectTabWidget.indexOf(self.gctab), QtGui.QApplication.translate("CloudBackupUI", "Google云存储", None, QtGui.QApplication.UnicodeUTF8))

