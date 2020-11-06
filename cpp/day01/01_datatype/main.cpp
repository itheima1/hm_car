#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;


    int age  = 18 ;
    float price  = 10.5;
    double pi = 3.1415;
    char c = 'a';
    std::string name = "张三";
    bool flag = true ;  //  1 和 0  ： 0 表示假， 非零的数字表示真

    //打印所有变量的占用的空间
    std::cout << "age占用的空间: " << sizeof(age) << std::endl;
    std::cout << "price占用的空间：" << sizeof(price) << std::endl;
    std::cout << "pi占用的空间：" << sizeof(pi) << std::endl;

    std::cout << "c占用的空间：" << sizeof(c) << std::endl;
    std::cout << "name占用的空间：" << sizeof(name) << std::endl;
    std::cout << "flag占用的空间：" << sizeof(flag) << std::endl;

    return 0;
}
