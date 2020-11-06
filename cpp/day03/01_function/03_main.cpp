#include <iostream>


//c++ 函数传参 :: 引用的传递

using namespace std;

//要想让函数内部能够修改外部变量的数据，只需要满足一个条件即可。
//就是让函数的参数和外部的变量是同一个变量，
//就是让函数的参数成为外部变量的别名。
//谁是别名，谁就是引用。

void changeScore(int & score){
    score = 100;
}

int main() {

    //定义的分数
    int score = 50;

    //修改分数
    changeScore(score);

    cout << "score="<<score<<endl;

    return 0;
}
