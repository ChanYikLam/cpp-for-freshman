#include <iostream>
#include <iomanip>

int main()
{
    std::cout << "请输入三个成绩：";

    double score1 = 0.0;
    double score2 = 0.0;
    double score3 = 0.0;
    std::cin >> score1 >> score2 >> score3;

    std::cout << "读到的三个数：" << score1 << " " << score2 << " " << score3 << std::endl;
    std::cout << "输入是否成功：" << std::boolalpha << static_cast<bool>(std::cin) << std::endl;

    return 0;
}
