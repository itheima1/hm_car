#include <iostream>


//创建指针的两种方式

using namespace std;

int main() {


    //栈内存的方式
    int age = 18;
    int *p1 = &age; //指针p1 指向的是栈内存的地址。

    //堆内存的方式 , 采用new关键字 , 在堆内存中申请空间
    int * p2 = new int(20);

    //回收p2
    delete p2;


    return 0;
}
