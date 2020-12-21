#include <iostream>
#include <string>

using namespace std;
//类
class student{
    string name;
    int age;

    void read(){

    }
};


int main() {


    //===================创建对象============================

    //1. 在栈里面创建  语法： 类名  对象名字;

    student s;
    student s2;


    //2. 在堆里面创建  语法：类名 * 指针名  = new 类名()
    // 在堆内存当中开辟一块空间，然后存放一个刚创建的学生对象
    //因为开辟空间没有任何的名字，只有一个地址返回，所以左边需要使用指针来接收它。
    // 使用指针来接收地址，主要是为了方便我们以后操作这个堆内存中创建的学生对象。
    student * s3 = new student;
    student * s4 = new student(); //建议跟上小括号。





    return 0;
}
