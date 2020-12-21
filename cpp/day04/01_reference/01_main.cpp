#include <iostream>

//右引用|右值引用 ， 默认接收的是右值 , 符号是  &&

// 左引用 ， 默认可以接收左值， 如果加上const关键字，特殊一些，可以接收右值了。 符号是  &


int main() {

    //变量
    int age = 18; //age :左值  ,18 右值

    //左引用
    int & age2 = age; // age2 : 左引用 ， age 左值
    const int & age3 = 18 ; // age3 : 左引用 ， 18 : 右值

    //右引用
    int && age4 = 18; // age4 : 右引用 ， 18 : 右值

    return 0;
}
