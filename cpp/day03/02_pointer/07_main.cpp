#include <iostream>
#include <synchapi.h>


//函数返回指针

using namespace std;

//通过函数返回年龄
int getAge(){
    int age = 18;
    return age;
}

//永远要记住，指针不要普通的东西，只要地址！
int* getAge02(){
    int age = 19;
    return &age;
}

int* getAge03(){
    int *p1 =new int(20);
    return p1;
}

int main() {

    int a = getAge();
    cout << "a=" << a <<endl;

    cout <<"--------------------------------------------------" << endl;
    int *page = getAge02();
    Sleep(3000);
    cout << "结果：" << *page <<endl;

    cout <<"--------------------------------------------------" << endl;
    int *page3 = getAge03();
    cout << "结果2：" << *page3 <<endl;
    delete page3; //释放堆内存的空间。

    return 0;
}
