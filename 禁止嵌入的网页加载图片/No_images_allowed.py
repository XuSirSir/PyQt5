import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

class WebView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://www.baidu.com'))
        # 设置不加载图片
        self.browser.page().settings().setAttribute(QWebEngineSettings.AutoLoadImages, False)
        self.setCentralWidget(self.browser)
        self.resize(800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    webView = WebView()
    webView.show()
    sys.exit(app.exec_())