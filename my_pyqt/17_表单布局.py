
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def click_send():
    print("点击了按钮")

    name = le_name.text()
    age = le_age.text()
    phone = le_phone.text()

    print(name)
    print(age)
    print(phone)


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # UI实现
    # 表单布局
    layout = QFormLayout()
    # 为窗体设置布局
    window.setLayout(layout)

    # 姓名输入
    le_name = QLineEdit()
    layout.addRow("姓名", le_name)

    le_age = QLineEdit()
    layout.addRow("年纪", le_age)

    le_phone = QLineEdit()
    layout.addRow("电话", le_phone)

    btn_send = QPushButton('发送')
    layout.addRow(btn_send)

    window.show()

    # 设置按钮点击事件的捕获
    btn_send.clicked.connect(click_send)

    # 执行app
    sys.exit(app.exec_())
