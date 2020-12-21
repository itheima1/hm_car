#include <iostream>

//引用 & 左值&右值 练习
using namespace std;
//参数接收普通变量
int add01(int a , int b){ // int a =num1 ; int b = num2;
    return a + b;
}
//接收左引用
int add02(int & a , int & b){
    return a + b;
}
// 接收左右引用，各一半。
int add03(int && a , int & b){
    return a + b;
}
//接右引用
int add04(int && a , int && b){
    return a + b;
}
int main() {
    int num1 = 10;
    int num2 = 20;

    //依次调用 add01 ...  add04 . 传参可选： num1 , num2 , 10 , 20
    cout << add01(num1, num2) << endl;
    cout <<  add02(num1 , num2)<< endl;
    cout << add03(10 , num2)<< endl;
    cout <<  add04(10, 20)<< endl;


    return 0;
}
