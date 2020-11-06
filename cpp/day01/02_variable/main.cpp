#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;


    //语法：  类型  变量名称  = 变量值;


    //1. 声明变量的同时，并立即初始化
    int age = 18;
    double price = 20.5;


    //2. 可以先声明， 后赋值
    int score;
    score = 100;


    //3. 错误的示范： 没有声明就直接使用
    //number = "10086";


    //4. 变量的初始化写法有三种！
    int a = 3;  //从C语言借鉴过来的，
    int b (4); //采用构造方法方式
    int c {5}; // c++ 11版本提出，初始化列表的方式

    //5. 也可以查看变量占用的空间有多大，得到的结果其实和查看数据的类型是一样的。
    std::cout << "a占用的空间：" << sizeof(a) << std::endl;
    std::cout << "int占用的空间：" << sizeof(int) << std::endl;

    return 0;
}
