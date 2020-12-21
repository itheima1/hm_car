#include <iostream>
#include <string>

//永远只会在源文件当中导入头文件。
#include "stu.h"

using namespace std;

/*
 实现类当中的成员函数

    把类的声明放到头文件当中
    把类的实现放到源文件当中。
*/
// 以下代码得放到头文件当中...
/*class student{
public:
    string name;
    int age ;

    //函数的原型
    void read();
};*/


// 以下代码得放到源文件当中
/*void student::read(){
    cout <<age << " 岁的 "<< name << " 在看书~" <<endl;
}*/



int main() {


    stu s;
    s.name ="张三";
    s.age = 18;

    s.read();

    return 0;
}
