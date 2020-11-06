#include <iostream>


//左值引用 实际上就是以前我们写过的引用，它使用&的符号来表示
//1. 使用&符号来表示
//2. 左值引用默认情况下只能接受左值
//3. 给左引用加上 const关键字之后，左引用就特殊一些，它可以接收右值了。

using namespace std;

int main() {

    int a = 3 ;

    int & aa = a ; //aa ： 左值引用|左引用|引用  ，  a：左值
    //int & bb = 3; // bb : 左值引用  ，3 : 右值

    const int & cc = 3; // cc 左值引用  ， 3 ：右值


    return 0;
}
