# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wvs.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(638, 445)
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setLineWidth(1)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_8.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout_8.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout_8.addWidget(self.label_20, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_8.addWidget(self.label_22, 4, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_8.addWidget(self.label_21, 5, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_8.addWidget(self.label_23, 6, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setObjectName("label_24")
        self.gridLayout_8.addWidget(self.label_24, 7, 2, 1, 1)
        TabWidget.addTab(self.tab_4, "")
        self.tabs = QtWidgets.QWidget()
        self.tabs.setObjectName("tabs")
        self.gridLayout = QtWidgets.QGridLayout(self.tabs)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tabs)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tabs)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 6, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tabs)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tabs)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tabs)
        self.spinBox.setMinimum(5)
        self.spinBox.setMaximum(100)
        self.spinBox.setSingleStep(5)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tabs)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tabs)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tabs)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(4)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tabs)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 5, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tabs)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout.addWidget(self.textBrowser_5, 2, 0, 1, 8)
        self.progressBar = QtWidgets.QProgressBar(self.tabs)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tabs)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 5)
        TabWidget.addTab(self.tabs, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 2, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 3, 0, 1, 4)
        TabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(109, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 1, 3, 1, 1)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout_3.addWidget(self.textBrowser_6, 2, 0, 1, 5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 3)
        TabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 1, 1, 1, 1)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.gridLayout_4.addWidget(self.textBrowser_7, 2, 0, 1, 3)
        TabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_5.addWidget(self.pushButton_8, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 1, 1, 1, 2)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_5.addWidget(self.textBrowser_2, 2, 0, 1, 3)
        TabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_13 = QtWidgets.QLabel(self.tab_6)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_6.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_6.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 1, 1, 1, 2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_6)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_6.addWidget(self.textBrowser_3, 2, 0, 1, 3)
        TabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_15 = QtWidgets.QLabel(self.tab_7)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_7.addWidget(self.lineEdit_8, 0, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_7.addWidget(self.pushButton_10, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_7)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 1, 1, 1, 2)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_7)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_7.addWidget(self.textBrowser_4, 2, 0, 1, 3)
        TabWidget.addTab(self.tab_7, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "GAWVS         by hmoytx"))
        TabWidget.setWhatsThis(_translate("TabWidget", "<html><head/><body><p>C段</p></body></html>"))
        self.label_17.setText(_translate("TabWidget", "<h3>简单集成了一些常用的工具接口</h3>"))
        self.label_18.setText(_translate("TabWidget", "<h3>用python开发，ui是pyqt</h3>"))
        self.label_19.setText(_translate("TabWidget", "<h3>漏洞poc来自网上公开，共300余个，在此表示感谢</h3>"))
        self.label_20.setText(_translate("TabWidget", "<h3>本工具仅限于进行漏洞验证，如若因此引起相关法律问题，作者概不负责</h3>"))
        self.label_22.setText(_translate("TabWidget", "<h3>对于后续可继续开发，也可添加漏洞到目录下</h3>"))
        self.label_23.setText(_translate("TabWidget", "<h2><font color=red>gakki的老公</font></h2>"))
        self.label_24.setText(_translate("TabWidget", "<h3>         2018.7</h3>"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "简介"))
        self.label.setText(_translate("TabWidget", "网站："))
        self.pushButton_2.setText(_translate("TabWidget", "开始扫描"))
        self.pushButton_3.setText(_translate("TabWidget", "停止扫描"))
        self.label_2.setText(_translate("TabWidget", "线程数："))
        self.label_5.setText(_translate("TabWidget", "建议核心*5"))
        self.label_3.setText(_translate("TabWidget", "超时："))
        self.label_4.setText(_translate("TabWidget", "s"))
        self.textBrowser_5.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">#说明</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.字典文件位于同目录并且改名为 dic.txt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.URL输入格式应为http://xxxxxxxxx</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3.建议线程数不超过20</span></p>\n"))
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4.出现卡顿重新启动再扫描即可</span></p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">5.停止可能存在崩溃</span></p></body></html>"
        TabWidget.setTabText(TabWidget.indexOf(self.tabs), _translate("TabWidget", "目录扫描"))
        self.label_6.setText(_translate("TabWidget", " ip："))
        self.pushButton.setText(_translate("TabWidget", "开始扫描"))
        self.label_7.setText(_translate("TabWidget", "port："))
        self.textBrowser.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">#说明</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.输入ip格式:x.x.x.x</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.端口输入格式支持范围输入：1-80,445,3389,8080,3306,1433</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3.暂不支持多线程，点一下即可，耐心等待扫描完成。</span></p></body></html>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4.输出前缀为[+]为开放端口。</span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "端口扫描"))
        self.label_8.setText(_translate("TabWidget", "域名："))
        self.pushButton_4.setText(_translate("TabWidget", "获取ip"))
        self.pushButton_5.setText(_translate("TabWidget", "查询"))
        self.textBrowser_6.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">#说明</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.调用的是网络接口，暂时不支持自动化C段扫描，只支持旁站扫描。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.输入URL格式：http://xxxxxxxxx</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3.先获取IP或者这直接输入ip再查询旁站</span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "旁站扫描"))
        self.label_9.setText(_translate("TabWidget", "网址："))
        self.pushButton_7.setText(_translate("TabWidget", "识别"))
        self.label_10.setText(_translate("TabWidget", "http://www.test.com"))
        self.textBrowser_7.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">#说明</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.调用的是网络接口，存在无法识别的情况。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.输入URL:http://xxxxxxxxx</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3.暂时不支持批量识别</span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "CMS识别"))
        self.label_11.setText(_translate("TabWidget", "网址："))
        self.pushButton_8.setText(_translate("TabWidget", "检测"))
        self.label_12.setText(_translate("TabWidget", "http://www.test.com"))
        self.textBrowser_2.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">#说明</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.漏洞库来自网络公开，整理后统一化。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.漏洞库目录poc.md。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3.暂时不支持多线程，点一下即可，检测需要时间。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4.输出前缀为[+]为存在漏洞。</span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_5), _translate("TabWidget", "CMS安全检测"))
        self.label_13.setText(_translate("TabWidget", "网址："))
        self.pushButton_9.setText(_translate("TabWidget", "暂时不接入"))
        self.label_14.setText(_translate("TabWidget", "http://www.test.com"))
        self.textBrowser_3.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">#时暂时不接入该功能</span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_6), _translate("TabWidget", "信息泄漏检测"))
        self.label_15.setText(_translate("TabWidget", "网站："))
        self.pushButton_10.setText(_translate("TabWidget", "检测"))
        self.label_16.setText(_translate("TabWidget", "http://www.test.com"))
        self.textBrowser_4.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">#说明</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.并非纯粹的操作系统漏洞，主要针对的是中间件等应用的漏洞。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.输入URL：http://xxxxxxxx</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3.暂时不支持多线程，点一下即可，检测需要时间。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4.输出前缀[+]为存在漏洞。</span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_7), _translate("TabWidget", "系统漏洞检测"))

