#include <iostream>
#include <vector>

using namespace std;


//返回值  参数名 作 可有可无的变化，组合出来4种类型。

//1. 没有返回值，没有参数。
void sayHi01(){
    cout <<"你好呀~~" << endl;
}

//2. 没有返回值， 有参数
void sayHi02(string name){
    cout << "你好，" << name << endl;
}

//3. 有返回值，没有参数
string sayHi03(){
    return "你好呀~~03";
}

//4. 有返回值，有参数
string sayHi04(string name){
    return "你好，" + name ;
}
int main(){
    sayHi01();
    sayHi02("张三");

    string result = sayHi03();
    cout << result << endl;

    string result2 = sayHi04("李四");
    cout << result2 << endl;



    return 0;
}
