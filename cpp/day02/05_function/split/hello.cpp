//
// Created by xiaomi on 2020/11/4.
//
//告诉所有人，这个源文件实际上就是实现了hello.h 头文件的。
#include "hello.h"

//这个源文件用到什么东西，那么就由自己来导入了。
#include <iostream>

using namespace std;

void sayHi(){
    cout << "你好~~" << endl;
}

