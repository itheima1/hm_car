#include <iostream>
#include <vector>

using namespace std;

//vector的基本操作： 增删改查
int main(){

    //1. 定义一个vector
    vector<int> scores {10,20,30,40,50,60};

    //2. 获取指定位置的值
    cout <<"scores[0]=" << scores[0] << endl;
    cout << "scores.at(0)=" << scores.at(0) << endl;

    //3. 修改值
    scores.at(0) = 100;
    cout << "scores.at(0)=" << scores.at(0) << endl;

    //4. 添加值
    scores.push_back(70);
    scores.push_back(80);

    //5. 遍历
    for (int i = 0; i < scores.size(); ++i) {
        cout << i << "=" << scores.at(i) << endl;
    }

    cout <<"--------------------------------" <<endl;

    //6. 删除，可以删除，但是比较麻烦。
    //得到第0个元素的迭代器

    scores.erase(scores.begin()); //删除第0个元素

    for (int i = 0; i < scores.size(); ++i) {
        cout << i << "=" << scores.at(i) << endl;
    }
    return 0;
}
