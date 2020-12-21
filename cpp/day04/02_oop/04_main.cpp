#include <iostream>
#include <string>

using namespace std;

/*
 类当中的访问修饰符
    private :  默认就是private权限。  类的外部无法访问。

    public:  公开，任何地方都可以访问，只要有对象即可

    protected: 保护 ， 除了自己和子类| 友元类 |友元函数 可以访问之外，其他地方不能访问。
*/
class student{

protected:
    string name;
private:
    int age ;

public:
    void read(){
        age = 19;
    }
};


int main() {

    student s;
    s.name = "aa";
    s.age  = 19;



    return 0;
}
