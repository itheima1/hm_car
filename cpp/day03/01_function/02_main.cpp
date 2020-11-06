#include <iostream>


//引用

using namespace std;


int main() {

    int age = 18;
    age = 20;
    cout << "age=" << age <<endl;


    //可以定义age的别名
    //声明age的一个引用，引用的名字叫做： age2
    int &age2 = age;
    age2 = 33; //使用引用（别名）来修改值，那么原有的数据也会跟着修改。
    cout << "age=" << age <<endl;


    cout <<"age的地址：" << &age<<endl;
    cout <<"age2的地址：" << &age2<<endl;

    return 0;
}
