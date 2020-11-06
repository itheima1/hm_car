#include <iostream>


//左值和右值 ， 左值可以出现在左边和右边， 右值只能出现在右边。

using namespace std;

int getAge(){
    int a = 18;
    return a;
}

int main() {

   int a = 3 ;  //  a :  左值 ，  3 ： 右值
   int b = 4 ; // b : 左值 ， 4 ：右值
   int c = a ; // c : 左值  , a : 左值

   int d = a + 3 ; //d :左值， a+3 : 右值

   int e = getAge(); // e : 左值 ， getAge()返回值 : 右值



    return 0;
}
