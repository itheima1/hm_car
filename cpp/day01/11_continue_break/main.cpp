#include <iostream>

int main() {

    //1. 只想打印偶数， 就是奇数不要打印
    int number= 0;
    while(number < 20 ){
        number++;
        if(number % 2 != 0){ //这是奇数
            continue; //跳过当前轮次的循环（当前轮次后面的代码也不执行了），继续执行下一次的循环。
        }

        std::cout << "number=" << number << std::endl;

        if(number == 16){
            break; //跳出循环
        }
    }


    return 0;
}
