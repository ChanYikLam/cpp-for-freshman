#include <iostream>

int main()
{
    int score = 0;

    std::cout << "请输入成绩（0 到 100）：";
    while (!(std::cin >> score) || score < 0 || score > 100)
    {
        std::cout << "这个数不能用，请重新输入一个 0 到 100 的整数：";
        std::cin.clear();
        std::cin.ignore(1000, '\n');
    }

    std::cout << "收到的成绩是 " << score << std::endl;

    return 0;
}
