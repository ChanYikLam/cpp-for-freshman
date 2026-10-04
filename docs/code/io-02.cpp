#include <iostream>
#include <iomanip>

int main()
{
    const int kSubjectCount = 3;

    std::cout << "请输入三门课的成绩（用空格或回车分开）：";

    double score1 = 0.0;
    double score2 = 0.0;
    double score3 = 0.0;
    std::cin >> score1 >> score2 >> score3;

    double total = score1 + score2 + score3;
    double average = total / kSubjectCount;

    std::cout << std::fixed << std::setprecision(1);
    std::cout << std::endl;
    std::cout << "三门成绩：" << score1 << "、" << score2 << "、" << score3 << std::endl;
    std::cout << "总分：" << total << std::endl;
    std::cout << "平均分：" << average << std::endl;

    return 0;
}
