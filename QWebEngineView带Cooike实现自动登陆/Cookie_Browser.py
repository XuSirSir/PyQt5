import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtNetwork import QNetworkCookie


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Browser')
        self.resize(800, 600)
        url = 'https://www.baidu.com'
        req_cookies = {
            'BD_UPN': '',
            'PSTM': '',
            'BIDUPSID': '',
            'BAIDUID': '',
            'BDORZ': '',
            'delPer': '',
            'BD_CK_SAM': '',
            'PSINO': '',
            'BDRCVFR[feWj1Vr5u3D]': '',
            'ZD_ENTRY': '',
            'H_PS_645EC': '',
            'BDUSS': '',
            'BD_HOME': '',
            'H_PS_PSSID': ''
        }

        self.webview = QWebEngineView()
        cookiestore = self.webview.page().profile().cookieStore()
        cookie = QNetworkCookie()
        for key, value in req_cookies.items():
            # 设置cookie的键
            cookie.setName(key.encode())
            # 设置cookie的值
            cookie.setValue(value.encode())
            # 设置cookie的域
            cookie.setDomain('.baidu.com')
            cookiestore.setCookie(cookie)

        self.webview.load(QUrl(url))
        self.setCentralWidget(self.webview)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
