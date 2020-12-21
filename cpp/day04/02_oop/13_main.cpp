#include <iostream>
#include <string>

using namespace std;

/*
  浅拷贝引发的问题

    只要见到类似这样的一句话就一定会发生拷贝 stu s2 = s1;
        1. 函数传参
        2. 接收函数的返回值
        3. 手动使用原有对象来创建新对象
            stu s1;
            stu s2 = s1;
*/

class student{
public:
    //string * name; //野指针，会乱指向
    string * name = nullptr;
    student (string name ) : name(new string(name)){
        cout << "有参构造函数" <<endl;
    }
    student (const student & s){

        //如果类当中有指针的成员，那么不能直接做简单的拷贝，
        //这会让两个对象中的同名成员指向同一个地方。
        //以后只要用其中一个对象修改指向的数据，另一个对象的数据也会发生改变。
        //name = s. name;

        //=============深拷贝=====================
        //1. 开辟自己的空间
        //name = new string();

        //2. 把数据拷贝过来
        //*name = *s.name;

        //==========简写方式========================
        name = new string(*s.name);
    }
    ~student (){
        cout << "析构函数" << endl;
    }
};
int main() {
    student s1("张三");
    student s2 = s1;

    cout <<"s1.name=" << *s1.name <<endl;
    cout <<"s2.name=" << *s2.name <<endl;

    *s2.name = "李四";

    cout <<"====s1.name=" << *s1.name <<endl;
    cout <<"====s2.name=" << *s2.name <<endl;


    return 0;
}
