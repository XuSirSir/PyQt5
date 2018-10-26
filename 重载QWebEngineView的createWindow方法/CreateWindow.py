import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Browser')
        self.resize(800, 600)
        url = 'https://www.baidu.com'
        self.webview = MyWebEngineView()
        self.webview.load(QUrl(url))
        self.setCentralWidget(self.webview)


class MyWebEngineView(QWebEngineView):
    # 重载creatWindow方法
    def createWindow(self, QWebEnginePage_WebWindowType):
        return self


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())