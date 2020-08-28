from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def do_click():
    # QMessageBox 对话框
    # information： 信息对话框 parent, title, content 阻塞式
    # QMessageBox.information(window, '我是对话框的title', '我是对话框的内容')

    # question: 问答对话框
    # result = QMessageBox.question(window, 'title', 'content')
    # print(type(result))
    # if result == QMessageBox.Yes:
    #     print('yes')
    # else:
    #     print('no')

    # warining
    # QMessageBox.warning(window, 'title', 'content')

    # critical
    # QMessageBox.critical(window, 'title', 'content')

    # about
    QMessageBox.about(window, 'title', 'content')

    print('对话框消失了')


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # 按钮
    btn = QPushButton('弹出对话框')
    # 设置到界面
    btn.setParent(window)

    window.show()

    # 事件绑定
    btn.clicked.connect(do_click)

    # 执行app
    sys.exit(app.exec_())
