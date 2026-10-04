#include <iostream>

int main()
{
    int score = 150;

    if (score >= 60 && score <= 100)
    {
        std::cout << "分数合法" << std::endl;
    }
    else
    {
        std::cout << "分数不合法" << std::endl;
    }

    return 0;
}
