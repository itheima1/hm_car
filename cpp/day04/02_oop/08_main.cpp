#include <iostream>
#include <string>

using namespace std;

/*
  构造函数
    构造函数初始化列表的写法
*/

class student{
public:
    string name;
    int age;
/*
    student (string name , int age){
        //下面的这两行代码并不是对上面的两个属性进行初始化。
        //
        this->name = name ;
        this->age = age;
    }*/

    //构造初始化列表
    student (string name , int age):name(name) , age(age){
        cout <<"有参构造" <<endl;
    }

    void read(){
        cout <<age <<" 岁的 "<< name << " 在看书·" << endl;
    }
};


int main() {


    student s("张三" , 18);
    s.read();


    return 0;
}
