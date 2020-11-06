#include <iostream>
#include <synchapi.h>


//using命名空间
using namespace std;


//数组是一串连续的地址来存放数据。  &叫做取地址符，可以对变量|数组的元素进行取地址

//计算数组的长度
int main(){


    //数组，有6个元素
    int scores []{10,20,30,40,50,60};

    //遍历每一个元素出来，然后对元素进行取地址（看一看元素是放在什么地方的。）
    for (int i = 0; i < sizeof(scores) / sizeof(int); ++i) {
        cout << scores[i] << "的地址：" << &scores[i] << endl;
    }

    //数组有可能会异常
    cout << scores[500] << endl;


    return 0;
}
