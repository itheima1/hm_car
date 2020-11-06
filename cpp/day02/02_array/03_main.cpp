#include <iostream>
#include <synchapi.h>


//using命名空间
using namespace std;


//计算数组的长度
int main(){


    int scores []{10,20,30,40,50,60};


    //1. 计算数组占用的总空间
    cout << "数组的总空间大小：" << sizeof(scores) << endl; //24个字节

    //2. 每一个元素占用的空间。
    cout << "每一个元素占用的空间：" << sizeof(int) << endl; //4个字节

    //3. 数组的空间大小
    cout << "数组的长度大小：" << sizeof(scores) / sizeof(int) <<endl;


    //4. 遍历数组
    for (int i = 0; i < sizeof(scores) / sizeof(int); ++i) {
        cout << i << "===" << scores[i] <<endl;
    }


    return 0;
}
