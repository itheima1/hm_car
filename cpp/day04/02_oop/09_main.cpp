#include <iostream>
#include <string>

using namespace std;

/*
  析构函数
    调用时机： 对象销毁的时候就执行。
    作用：一般在里面做收尾的工作。
*/

class student{
public:
    string * name;
    //构造函数
    student(){
        cout <<"构造函数" << endl;
    }

    //析构函数  和 无参构造函数相似度高达99.9%

    ~student(){
        cout <<"析构函数" << endl;
    }
};
int main() {

    //栈内存方式创建对象
    //student s1;

    //堆内存方式创建对象
    student *s2 = new student();
    cout <<"-------------1-----------" <<endl;
    delete s2;
    cout <<"-------------2-----------" <<endl;

    return 0;
}
