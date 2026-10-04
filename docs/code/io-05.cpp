#include <iostream>

int main()
{
    int score = 0;

    std::cout << "请输入成绩：";
    std::cin >> score;

    if (std::cin.fail())
    {
        std::cout << "\n这一段不是数字，读入失败了。丢弃这一行，重新读一次。\n";
        std::cin.clear();
        std::cin.ignore(1000, '\n');

        std::cout << "请重新输入成绩：";
        std::cin >> score;
    }

    std::cout << "最终读到：" << score << std::endl;

    return 0;
}
