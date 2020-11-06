#include <iostream>
#include <vector>

using namespace std;

//字符串
int main(){


    //std::vector
    int scores2[10];

    // vector是一种容器，跟数组差不多太多，都能够存放数据
    //<int> 就是表示这个vector里面能够存放的数据类型。
    vector<int> scores;
    vector<double>scores3;
    vector<string> scores4;


    //vector声明并且立即初始化
    vector <int> scores5{10,20,30,40,50,60};


    return 0;
}
