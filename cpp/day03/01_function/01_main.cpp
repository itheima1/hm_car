#include <iostream>


//c++ 函数传参的默认方式 :: 值的拷贝

using namespace std;

//专门用于修改分数
// 函数的参数，实际上就是函数内部的一个变量，这个变量是一个独立的个体。
void changeScore(int s){  // int s = score ;
    cout << "s的地址：" << &s << endl;
    s = 100;
}
int main() {
    //考试的成绩
    int score = 50 ;
    cout << "score的地址：" << &score << endl;

    changeScore(score);

    //打印分数：
    cout <<"score = "<< score <<endl;
    return 0;
}
