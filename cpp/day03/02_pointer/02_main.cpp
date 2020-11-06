#include <iostream>


//指针的地址和指针的大小
// 取地址，用取地址符&
// 看占用的大小，使用sizeof()

using namespace std;

int main() {


    //变量
    int age = 18;
    cout << "age的地址：" << &age  << endl;
    cout << "age占用多大的空间：" << sizeof(age) << endl; //4个字节



    //指针 * 的意思仅仅是起到了标识符的作用，告诉编译器， 变量p是指针。
    int * p = &age;
    cout << "p的地址：" << &p <<endl;
    cout << "p占用多大的空间：" << sizeof(p) << endl; //8个字节, 在64位的系统下，指针的占用空间永远是8， 32位的系统就是4.


    string name = "张三";
    string *pname = &name;
    cout << "pname的空间：" << sizeof(pname) <<endl;


    return 0;
}
