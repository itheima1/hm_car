#include <iostream>


//交换两个变量的值

using namespace std;

//要记住一点：要想在函数内部完成外部变量的值的交换，那么必然涉及到修改外部变量的这一行为。
void swap01(int *p1 , int *p2){

    //交换p1 和 p2各自指向位置的值
    //1. 使用中间变量来寄存p1指向位置的值
    int temp =*p1;

    //2. 把p2指向位置的值倒给p1指向的位置
    *p1 = *p2 ;

    //3. 把中间变量的值，倒给p2
    *p2 = temp;

}

int main() {

    int a = 3;
    int b = 4;

    cout << "交换之前：a=" <<a << " , b=" << b <<endl;

    swap01(&a , &b );

    cout << "交换之后：a=" <<a << " , b=" << b <<endl;

    return 0;
}
