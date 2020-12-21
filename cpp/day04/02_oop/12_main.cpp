#include <iostream>
#include <string>

using namespace std;

/*
  浅拷贝引发的问题
*/

class student{
public:
    //string * name; //野指针，会乱指向
    string * name = nullptr;
    student (string name ) : name(new string(name)){
        cout << "有参构造函数" <<endl;
    }
    student (const student & s){
        name = s. name;
    }
    ~student (){
        cout << "析构函数" << endl;
    }
};
int main() {
    student s1("张三");
    student s2 = s1;


    cout <<"s1.name=" << *s1.name <<endl;
    cout <<"s2.name=" << *s2.name <<endl;

    *s2.name = "李四";


    cout <<"====s1.name=" << *s1.name <<endl;
    cout <<"====s2.name=" << *s2.name <<endl;


    return 0;
}
