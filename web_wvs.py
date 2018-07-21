import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests
from queue import Queue
import time
import socket
import re
import json
from cmsscan.pocdata import *
from wvs import Ui_TabWidget





class url_scan(QThread):

    outsignal = pyqtSignal(str)
    def __init__(self, Queue, i, textBrowser, timeout):
        super(url_scan, self).__init__()
        self.url_queue = Queue
        self.all = i
        self.textBrowser = textBrowser
        self.timeout = timeout


    def run(self):

        while not self.url_queue.empty():
            url = self.url_queue.get(False)
            try:
                r = requests.get(url, timeout=self.timeout)
                if (r.status_code==requests.codes.ok):
                    message = "[+]" + url + "           " + str(r.status_code)
                else:
                    message = ""
            except:
                message = ""

            finally:
                self.outsignal.emit(message)






class progressBar_Dispaly(QThread):
    signal = pyqtSignal()
    def __init__(self, progressBar, Queue, i):
        super(progressBar_Dispaly, self).__init__()
        self.progressBar = progressBar
        self.urlQueue = Queue
        self.all = i


    def run(self):
        while not self.urlQueue.empty():
            self.progressBar.setValue((self.all - self.urlQueue.qsize()) * 100 / self.all)
        self.signal.emit()




class port_scan(QThread):
    def __init__(self, ip, port, sock, textBrowser):
        super(port_scan, self).__init__()
        self.ip = ip
        self.port = port
        self.sock = sock
        self.textBrowser = textBrowser
        self.ports =[]

    def run(self):
        self.sock.settimeout(1)
        for k in self.port:
            if "-" in k:
                j = k.split("-")
                for ports in range(int(j[0]), int(j[1])+1):
                    self.ports.append(str(ports))
                self.port.remove(k)
        self.port = self.port+self.ports
        length = len(self.port)
        i = 0
        while i<length:
            time.sleep(0.1)
            try:
                self.sock.connect((self.ip, int(self.port[i])))
                self.textBrowser.append("[+]"+self.ip + "            "*2 + self.port[i] + "            "*2 + "open")
            except Exception:
                self.textBrowser.append("[*]"+self.ip + "            "*2 + self.port[i] + "            "*2 + "close")
            finally:
                i = i + 1
                self.textBrowser.moveCursor(QTextCursor.End)



class what_cms(QThread):

    def __init__(self, url, textBrowser):
        super(what_cms, self).__init__()
        self.url = url
        self.time = 0
        self.textBrowser = textBrowser

    def run(self):
        url = 'http://whatweb.bugscaner.com/what/'
        start = time.clock()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
                   'Referer': 'http://whatweb.bugscaner.com/look/'}
        cocokies = {'saeut': 'CkMPHlqbqdBQWl9NBG+uAg=='}
        new_url = self.url.strip('/').replace('http://', '').replace('https://', '')
        data = {'url': new_url, 'hash': '0eca8914342fc63f5a2ef5246b7a3b14_7289fd8cf7f420f594ac165e475f1479'}
        content = json.loads(requests.post(url, headers=headers, data=data).text)
        end = time.clock()
        self.time = float('%.3f' % (end - start))
        if content['cms']:
            self.textBrowser.append("识别结果:"+content['cms']+"        用时:"+str(self.time)+"s")
            # return {'total':1424,'url':self.url,'result':content['cms'],'time':'%.3f s' % self.time}
        else:
            # return {'total':1424,'url':self.url,'result':'未知CMS','time':'%.3f s' % self.time}
            self.textBrowser.append("识别结果:" + "未知CMS" + "        用时:" + str(self.time) + "s")


class cmspoc_use(QThread):

    def __init__(self, cmsexp_url, textBrowser):
        super(cmspoc_use, self).__init__()
        self.cmsexp_url = cmsexp_url
        self.textBrowser = textBrowser


    def _cmspoc(self, i):
        cmsexp_poc_result = list(cmspocdict.values())[i](self.cmsexp_url).run()
        if cmsexp_poc_result is not None:
            if "[+]" in cmsexp_poc_result:
                cmsexp_poc_status = 1
            else:
                cmsexp_poc_status = 0
        else:
            cmsexp_poc_result = "[-]no vuln"
            cmsexp_poc_status = 0
        self.textBrowser.append(cmsexp_poc_result + "    poc:" + str(list(cmspocdict.values())[i].__name__) + "    status:" + str(cmsexp_poc_status))
    def run(self):
        for i in range(254):
            self._cmspoc(i)
            self.textBrowser.moveCursor(QTextCursor.End)
        self.textBrowser.append("-------------done-------------")

class information_out(QThread):

    def __init__(self):
        super(information_out, self).__init__()

    def run(self):
        pass

class system_use(QThread):

    def __init__(self, system_url, textBrowser):
        super(system_use, self).__init__()
        self.textBrowser = textBrowser
        self.system_url = system_url

    def _system(self, i):
        try:
            system_poc_result = list(systempocdict.values())[i](self.system_url).run()
            if "[+]" in system_poc_result:
                system_poc_status = 1
            else:
                system_poc_status = 0
                system_poc_result = "[-]no vuln"
            self.textBrowser.append(system_poc_result + "    poc:" + list(systempocdict.values())[i].__name__ + "     status:" + str(system_poc_status))
        except:
            pass
    def run(self):
        for i in range(39):
            self._system(i)
            self.textBrowser.moveCursor(QTextCursor.End)
        self.textBrowser.append("--------------------------done--------------------------")


class tabwindow(QTabWidget, Ui_TabWidget):

    def __init__(self):
        super(tabwindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('gen.png'))
        self.pushButton_2.clicked.connect(self.scan)
        self.pushButton_3.clicked.connect(self.stop)
        self.pushButton.clicked.connect(self.portsan_api)
        self.pushButton_4.clicked.connect(self.domain_ip)
        self.pushButton_5.clicked.connect(self.query_c_add)
        self.pushButton_7.clicked.connect(self.whatcms)
        self.pushButton_8.clicked.connect(self.cmspoc)
        self.pushButton_9.setDisabled(True)
        self.pushButton_10.clicked.connect(self.system_use)
        self.ip = ""
        self.i = 0
        self.url_queue = Queue()

    def scan(self):
        self.i = 0
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(False)
        time.sleep(0.3)
        timeout = self.spinBox_2.value()
        url = self.lineEdit_3.text()
        if url == "":
            QMessageBox.warning(self,
                                "Error",  # 标题
                                "请输入端口",  # 内容
                                QMessageBox.Ok)
            self.pushButton_3.setDisabled(True)
            self.pushButton_2.setDisabled(False)

        else:
            self.textBrowser_5.setText("")
            thread_number = self.spinBox.value()
            f = open('dic.txt', 'r')
            for line in f:
                self.i= self.i + 1
                self.url_queue.put(url+line.rstrip('\n'))
            f.close()
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(False)
            self.work_threads = []
            for work_thread_name in range(thread_number):
                self.work_thread = url_scan(self.url_queue, self.i, self.textBrowser_5, timeout)
                self.work_thread.start()
                self.work_threads.append(self.work_thread)
                self.work_thread.outsignal.connect(self.update_out)


    def update_out(self, message):
        self.textBrowser_5.append(message)
        self.textBrowser_5.moveCursor(QTextCursor.End)
        self.progressBar.setValue((self.i - self.url_queue.qsize()) * 100 / self.i)
        if (self.i - self.url_queue.qsize()) * 100 / self.i==100:
            self.pushButton_2.setDisabled(False)
            self.pushButton_3.setDisabled(True)

    def stop(self):
        self.pushButton_3.setDisabled(True)
        self.pushButton_2.setDisabled(False)
        for i in self.work_threads:
            i.terminate()
        self.progressBar.setValue(0)

    def portsan_api(self):
        ip = self.lineEdit.text()
        port = self.lineEdit_2.text().split(',')
        if ip == "":
            QMessageBox.warning(self,
                                "Error",  # 标题
                                "请输入地址",  # 内容
                                QMessageBox.Ok)

        elif self.lineEdit_2.text() == "":
            QMessageBox.warning(self,
                                "Error",  # 标题
                                "请输入端口",  # 内容
                                QMessageBox.Ok)
        else:
            self.textBrowser.setText("")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.port_scan_thread = port_scan(ip, port, sock, self.textBrowser)
            self.port_scan_thread.start()


    def portscan_stop(self):
        self.what_cms_thread.join()

    def domain_ip(self):
        domain = self.lineEdit_4.text()
        if (domain == ""):
            QMessageBox.warning(self,
                              "Error",  # 标题
                              "请输入地址",  # 内容
                              QMessageBox.Ok)
        else:
            self.textBrowser_6.setText("")
            try:
                self.ip = socket.gethostbyname(domain.split('/')[2])
                self.textBrowser_6.append(self.ip)
            except:
                self.ip = domain
                self.textBrowser_6.append(domain)

    def query_c_add(self):
        if self.ip == "":
            QMessageBox.warning(self,
                                "Error",  # 标题
                                "请先获取IP",  # 内容
                                QMessageBox.Ok)
        else:
            request_json_raw = requests.get('http://www.webscan.cc/?action=query&ip=%s' % self.ip)
            result = re.findall(r'{(.*?)}', request_json_raw.content.decode())
            for i in result:
                url = re.search(r'"domain":"(.*?)"', i).group().split(':')[2].lstrip('[\,/]').rstrip('"')
                self.textBrowser_6.append("    "+url)


    def whatcms(self):
        url = self.lineEdit_5.text()
        if url == "":
            QMessageBox.warning(self,
                                "Error",  # 标题
                                "请输入地址",  # 内容
                                QMessageBox.Ok)
        else:
            self.textBrowser_7.setText("")
            self.what_cms_thread = what_cms(url, self.textBrowser_7)
            self.what_cms_thread.start()


    def cmspoc(self):
        url = self.lineEdit_6.text()
        if (url==""):
            QMessageBox.warning(self,
                                "Error",  # 标题
                                "请输入地址",  # 内容
                                QMessageBox.Ok)
        else:
            self.textBrowser_2.setText("")
            self.cmspoc_thread = cmspoc_use(url, self.textBrowser_2)
            self.cmspoc_thread.start()


    def system_use(self):
        url = self.lineEdit_8.text()
        if (url == ""):
            QMessageBox.warning(self,
                                "Error",  # 标题
                                "请输入地址",  # 内容
                                QMessageBox.Ok)
        else:
            self.textBrowser_4.setText("")
            self.system_thread = system_use(url, self.textBrowser_4)
            self.system_thread.start()









if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = tabwindow()
    window.show()
    sys.exit(app.exec_())