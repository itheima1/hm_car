#include <iostream>
#include <string>

using namespace std;

/*
  拷贝的含义
*/

class student{
public:
    string name;

    student(string name ):name(name){

    }
};
int main() {

    //变量
    int a = 3;
    int b = 3;

    // 创建c这个变量的时候，把a的值拷贝过来。
    int c = a;

    //-================================================
    //对象
    student s1("张三");
    student s2("张三");


    //创建了s3对象，s3对象的数据是从s1拷贝过来的。
    student s3 = s1;




    return 0;
}
