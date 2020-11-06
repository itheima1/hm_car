#include <iostream>
#include <synchapi.h>

//do-while循环 一上来先执行再说，如果条件不满足，就不执行循环了，如果条件还满足，那么接着循环走。
int main(){

    int count = 100 ;
    do{
        std::cout <<"绿灯一直在闪！" << std::endl;
        count++;
        Sleep(1000);
    }while (count < 5);

    //-------------------------------------------------

    for (int i = 0; i < 5; ++i) {
        std::cout << "黄灯一直在闪烁" << std::endl;
        Sleep(1000);
    }

    // 无限循环 |  死循环...
    while(1){
        std::cout << "黄灯一直在闪烁" << std::endl;
    }

    //前面有无限循环了，所以这行代码是无法执行的。
    std::cout << "黄灯一直在闪烁" << std::endl;

    return 0;
}
