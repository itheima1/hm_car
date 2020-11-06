#include <iostream>


//函数的参数传递指针，
//即便把指针当成函数的参数来传递，仍然避免不了拷贝的事情发生，
//拷贝的是地址 ， 因为地址就是一个十六进制的数字。

using namespace std;

void changeScore(int * s){ //参数是指针 s 指向了 score
    *s = 100; //使用了解引用的方式来修改score的数值
}

int main() {

    //原始分数
    int score = 50;

    //修改分数
    changeScore(&score);

    cout << "分数：" << score << endl;


    return 0;
}
