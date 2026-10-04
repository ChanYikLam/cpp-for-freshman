#include <iostream>

int main()
{
    int score = 72;

    if (score >= 90)
    {
        std::cout << "等级：优" << std::endl;
    }
    else if (score >= 80)
    {
        std::cout << "等级：良" << std::endl;
    }
    else if (score >= 70)
    {
        std::cout << "等级：中" << std::endl;
    }
    else if (score >= 60)
    {
        std::cout << "等级：及格" << std::endl;
    }
    else
    {
        std::cout << "等级：不及格" << std::endl;
    }

    return 0;
}
