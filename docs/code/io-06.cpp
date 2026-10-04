#include <iostream>

int main()
{
    std::cout << "请输入三门课的成绩：";

    int score1 = 0;
    int score2 = 0;
    int score3 = 0;
    std::cin >> score1 >> score2 >> score3;

    double average = (score1 + score2 + score3) / 3;

    std::cout << std::endl;
    std::cout << "平均分：" << average << std::endl;

    return 0;
}
