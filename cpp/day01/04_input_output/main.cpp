#include <iostream>

int main() {

    //打印一句话：你好，中国！
    std::cout << "你好，中国！\n";


    //还想打印与句话： 你好，黑马程序员!
    std::cout << "你好，黑马程序员！";


    //std::endl 除了具备换行的功能，还有一个功能就是清空缓冲区.
    std::cout << "这是最后的一句话"  << std::endl;
    std::cout << "END" << std::endl;

    return 0;
}
