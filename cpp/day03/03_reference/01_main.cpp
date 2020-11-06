#include <iostream>


//引用

using namespace std;

int main() {

    //变量
    int age = 18;
    cout << "地址1：" << &age <<endl;

    //引用
    int &age2 = age;
    cout << "地址2：" << &age2 <<endl;

    // 引用声明就必须立即初始化，否则报错。
    //int &age3;

    //不能创建数组的引用
    //int score[]{10,20,30};
    //int[3] &s = score;


    return 0;
}
