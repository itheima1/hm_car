#include <iostream>

int main() {


    std::cout << "请输入您的考试成绩: " << std::endl;
    int score;
    std::cin >> score;

    //if方式
    if(score > 90){
        std::cout << "A" << std::endl;
    }else{
        std::cout << "B" << std::endl;
    }


    //三元表达式来写 成绩大于 90吗？如果大于，就得到A ，否则就得到B。
    char result = score > 90 ? 'A' : 'B';
    std::cout << "result=" << result <<std::endl;

    //如果不想接收结果，想直接打印表达式的结果
    std::cout << "结果：" <<  (score > 90?'A':'B')  << std::endl;


    return 0;
}
