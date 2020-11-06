#include <iostream>


//指针解引用

using namespace std;

int main() {

    //变量
    int age = 18;

    cout <<"age的值：" << age <<endl; // 18

    //指针
    //这里的* 仅仅表示page是一个指针，
    int * page = &age;

    //通过解引用额方式来修改指针指向位置的值！
    *page = 20;

    //这里的*是解引用的符号，因为在这里page本身已经是指针了。我们只能对指针进行解引用
    cout<< "通过指针来获取age的值：" << *page  << endl; // age的地址
    cout <<"age的值：" << age <<endl; // 20




    return 0;
}
