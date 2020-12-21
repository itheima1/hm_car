#include <iostream>
#include <string>

using namespace std;

// 访问对象中的成员

class student{
public:
    string name;
    int age ;

    void run(){
        cout << age <<" 岁的 " << name << " 在跑步~" <<endl;
    }
};


int main() {

    //1. 栈内存方式创建对象
    student s;
    s.name = "张三";
    s.age = 18;
    s.run();


    //2. 堆内存的方式 创建对象回来一定是一个指针接收，使用指针来访问对象的成员，简单的操作就是使用 ->
    student *s2 = new student();
    s2->name = "李四";
    s2->age = 19 ;
    s2->run();

    return 0;
}
