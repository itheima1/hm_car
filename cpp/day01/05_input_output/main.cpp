#include <iostream>

int main() {
    std::cout << "请输入您的年龄:" << std::endl;

    //获取键盘的输入 , 需要使用一个变量来接收。
    int age ;
    std::cin >> age;

    std::cout << "您的年龄是： " <<age << std::endl;

    //-----------------------------------------------------
    std::cout << "请输入您的名字：" << std::endl;

    std::string name ;
    std::cin >> name;

    std::cout << "您的姓名是：" << name << std::endl;
    return 0;
}