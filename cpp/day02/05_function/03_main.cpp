#include <iostream>
#include <vector>

using namespace std;

//函数的原型；

// 函数在使用之前，必须得先声明（告诉编译器，函数名字叫什么，函数的参数有哪些，函数的返回值是什么。）

/*void sayHi(){
    cout << "你好~" << endl;
}*/


//前面只要声明出来函数即可。 这就是函数的原型。
void sayHi();


int main(){
    //undefined reference to `sayHi()' 这句话可能经常会见到，它的意思就是： 没有定义sayhi函数，syahi函数没有实现。
    sayHi();
    return 0;
}

//这里就是函数的具体实现，也可以叫做函数的定义。
void sayHi(){
    cout << "你好~" << endl;
}
