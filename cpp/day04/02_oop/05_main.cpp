#include <iostream>
#include <string>

using namespace std;

/*
 实现类当中的成员函数

    1. 在类的里面，直接把函数写完了。

    2. 把函数的函数体拿到外面来写，把函数拆分一下，函数的原型（声明） + 函数的实现。
*/

class student{
public:
    string name;
    int age ;

    //函数的原型
    void read();
};

//在类的外面实现类的read函数
//为了表示这里的read函数就是student类当中read函数的具体实现。需要在方法名字的前面加上类名::
void student::read(){
    cout <<age << " 岁的 "<< name << " 在看书~" <<endl;
}

int main() {

    student s;
    s.name = "张三";
    s.age = 18;

    s.read();
    return 0;
}
