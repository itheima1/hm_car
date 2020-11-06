#include <iostream>
#include <synchapi.h>


//using命名空间
using namespace std;


//访问数组
int main(){

    //1. 声明数组
    int scores[3];

    //2. 查看每一个元素 数组的下标是从0开始的。
    cout << "scores[0] =" << scores[0] << endl;
    cout << "scores[1] =" << scores[1] << endl;
    cout << "scores[2] =" << scores[2] << endl;

    //__________________________________________________






    //3. 声明并初始化数组
    int scores2[]{10,20,30,40,50,60};


    //数组修改值...
    scores2[0] = 100;


    for (int i = 0; i < 6 ; ++i) {
        cout << i << "=" << scores2[i] <<endl;
    }

    //————————————————————————————————————————————
    //for(元素的类型 变量名: 容器){ 基于范围的for循环
    for(int s : scores2){
        cout << "s====" << s <<endl;
    }


    return 0;
}
