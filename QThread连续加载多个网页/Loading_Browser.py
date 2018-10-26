from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.thread = Worker()

        layout = QVBoxLayout()
        self.pushButton = QPushButton("开始")
        self.pushButton.setCheckable(True)

        self.pushButton.clicked.connect(self.slotStart)
        self.thread.sinOut.connect(self.slotAdd)

        self.browser = MyWebEngineView()
        layout.addWidget(self.browser)
        layout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.change_name)
        self.setLayout(layout)
        self.resize(1000, 800)

    def change_name(self):
        if self.pushButton.isChecked():
            self.pushButton.setText('停止')
        else:
            self.pushButton.setText('开始')

    def slotAdd(self, url):
        self.browser.load(QUrl(url))

    def slotStart(self):
        self.thread.start()


class MyWebEngineView(QWebEngineView):
    def creatWindow(self):
        return self


class Worker(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)

        self.lis = ["https://www.baidu.com", "https://www.qq.com"]

    def run(self):
        for url in self.lis:
            # 发射信号
            self.sinOut.emit(url)
            # 线程休眠 5 秒
            self.sleep(5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec_())
