#include <iostream>
#include <vector>

using namespace std;

//vector的小细节： 越界检查
int main(){

    //1. 定义一个vector
    vector<int> scores{10,20,30,40,50,60};

    //2. 取值 [] 和  at()
    cout << scores[100] << endl;
    cout << scores.at(100) << endl;


    return 0;
}
