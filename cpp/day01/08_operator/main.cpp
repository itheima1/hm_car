#include <iostream>

//关系运算符和逻辑运算符

int main() {


    //需求： 语文和数学的成绩必须要达到140分以上，才能报考清北
    std::cout << "请输入您的语文成绩: " << std::endl;
    int score1 ;
    std:: cin >>score1;

    std::cout << "请输入您的数学成绩：" << std::endl;
    int score2;
    std::cin >>  score2;

    if(score1 > 140 &&  score2 > 140){ //两者都达标
        std::cout << "可以报考清北" << std::endl;
    }else{
        std::cout << "可以报考其他的院校" << std::endl;
    }

    return 0;
}
