#include <iostream>

int main() {

    std::cout << "请输入您这次考试的成绩分数：" << std::endl;

    int score;

    std::cin >> score;

    if(score > 90){ // 分数 > 90
        std::cout << "奖励一块ipad" << std::endl;
    }else if(score > 80){
        std::cout << "奖励一包辣条" << std::endl;
    }else if(score > 70){
        std::cout << "奖励一根辣条" << std::endl;
    }else if(score > 60){
        std::cout << "奖励一粒瓜子" << std::endl;
    }else{
        //分数 <= 60
        std::cout << "禁止外出，拼命刷题" << std::endl;
    }

    return 0;
}
