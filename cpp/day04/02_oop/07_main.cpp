#include <iostream>
#include <string>

using namespace std;

/*
  构造函数
    1. 只要我们创建了对象，就一定会执行类的构造函数。
    2. 编译器默认会为我们的类提供一个无参构造函数。
    3. 构造函数：
        调用时机： 创建对象的时候调用
        作用： 用来初始化属性，完成初始化工作。

    4. 一旦我们写了自己的构造函数，那么编译器再也不会给我们提供默认的构造函数了。
*/

class student{
public:



    string name;
    int age;

    //默认的无参构造函数
   /* student (){
        cout << "student 无参构造" <<endl;
    }*/

    //有参构造函数
    student(string name2 , int age2){
        name = name2;
        age = age2;
    }

    void read(){
        cout <<age <<" 岁的 "<< name << " 在看书·" << endl;
    }
};


int main() {

    student s; //走无参构造
    s.name = "张三";
    s.age = 18;
    s.read();

    // 创建对象的同时，完成属性的赋值工作。
    student s2("李四" , 19);
    s2.read();


    return 0;
}
