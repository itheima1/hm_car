#include <iostream>
#include <synchapi.h>

//命名空间的简单处理方式

//表示要使用命名空间std
using namespace std;

int main(){


    // std 是一个命名空间
    // :: 叫做域操作符
    std::cout << "黄灯一直在闪烁" << std::endl;

    //--------------------------------------

    cout << "红灯在闪烁@！" << endl;


    return 0;
}
