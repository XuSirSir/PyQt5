import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout

# 主窗口类
class ParentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.iniUi()

        self.childwindow = ChildWindow()


    def iniUi(self):
        pushbutton = QPushButton('点击弹出子窗口')

        layout = QVBoxLayout()
        layout.addWidget(pushbutton)
        pushbutton.clicked.connect(self.use_childwindow)
        self.setLayout(layout)
        self.resize(300, 300)

    def use_childwindow(self):
        self.childwindow.show()


class ChildWindow(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    parent = ParentWindow()
    parent.show()
    sys.exit(app.exec_())
