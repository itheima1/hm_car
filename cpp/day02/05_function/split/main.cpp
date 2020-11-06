#include <iostream>
#include <vector>

//导入hello.h 因为它里面有一个函数 sayHi()
//#include <hello.h> //<>  一般是用于导入 编译环境提供的头, mingw提供的头
#include "hello.h" //""  如果是我们自己写的头文件，或者是第三方的头文件。 ""

//一般不会在源文件当中导入源文件
//#include "hello.cpp"

using namespace std;

//函数原型 ::: 放在一个独立的头文件(.h)当中。
//void sayHi();

int main(){
    sayHi();

    return 0;
}

//函数的具体实现 ::: 放在一个独立的源文件(.cpp)当中
/*void sayHi(){
    cout << "你好~~" << endl;
}*/
