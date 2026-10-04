#include <iostream>

int main()
{
    int chineseScore = 92;
    int mathScore = 88;
    int englishScore = 87;
    int total = chineseScore + mathScore + englishScore;
    double average = total / 3;

    std::cout << "总分：" << total << "，平均分：" << average << std::endl;

    return 0;
}
