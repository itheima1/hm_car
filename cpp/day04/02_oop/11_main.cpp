#include <iostream>
#include <string>

using namespace std;

/*
  拷贝构造函数
*/

class student{
public:
    string name;
    student(){
        cout <<"无参构造" <<endl;
    }

    student(string name ) :name(name){
        cout <<"有参构造" <<endl;
    }

    //拷贝构造 , 有一个参数，还是固定的，就是当前类的(左)引用类型。
    //拷贝构造，还建议给参数加上const 让引用变成常量引用
    //可以防止我们修改拷贝源。
    student(const student &  s){ // student s = s1;
        cout << "拷贝构造函数" <<endl;
        name = s.name;
    }



    ~student(){
        cout <<"析构" <<endl;
    }
};
int main() {

   //创建对象 s1 , 有参构造
    student s1("张三");
    cout <<"s1.name=" <<s1.name <<endl;

   //创建对象s2  , 拷贝构造
    student s2 = s1;

    cout <<"s2.name=" <<s2.name <<endl;

    return 0;
}
