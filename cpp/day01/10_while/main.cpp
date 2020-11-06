#include <iostream>
#include <synchapi.h>

int main() {


    //std::cout << "绿灯一直在闪！" << std::endl;

    int count = 0 ;
    while (count < 5){
        std::cout << "绿灯一直在闪！" << std::endl;
        count++;  //等同于count + 1 的意思。

        //休眠，单位是毫秒， 1000毫秒=1秒  linux下的休眠是uSleep(微秒) 1秒=1000毫秒 1毫秒=1000微秒
        Sleep(1000);
    }

   /*
    // 非0 的数字即为真，所以
    while(true){  // while(1)
        std::cout << "绿灯一直在闪！" << std::endl;
    }*/




    return 0;
}
