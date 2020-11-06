#include <iostream>

int main() {


    std::cout << "请输入你这次的考试成绩(A,B,C,D): "<< std::endl;
    char level ;
    std::cin >> level;

    switch (level){
        case 'A': //每一个分支都有case 和 break 搭配，千万不能省略掉。
            std::cout << "马尔代夫一日游" << std::endl;
            break;
        case 'B':
            std::cout << "楼下的小区玩一天" << std::endl;
            break;
        case 'C':
            std::cout << "阳台玩半小时" << std::endl;
            break;
        case 'D':
            std::cout << "赶紧去写作业！" << std::endl;
            break;
        default:
            std::cout << "输入错误，请重新输入！" << std::endl;
            break;
    }


    return 0;
}
