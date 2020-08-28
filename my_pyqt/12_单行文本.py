from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # 单行文本输入框
    edit = QLineEdit()

    # 模式设置
    # edit.setEchoMode(QLineEdit.NoEcho)
    # edit.setEchoMode(QLineEdit.Password)
    # edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    # placeholder
    edit.setPlaceholderText("请输入名字")

    edit.setText("abcdef")

    edit.setMaxLength(8)

    edit.setParent(window)

    window.show()

    print(edit.text())

    # 执行app
    sys.exit(app.exec_())
