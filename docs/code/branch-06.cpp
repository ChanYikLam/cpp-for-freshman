#include <iostream>

int main()
{
    char grade = 'B';

    switch (grade)
    {
    case 'A':
        std::cout << "优秀" << std::endl;
        break;
    case 'B':
        std::cout << "良好" << std::endl;
        break;
    case 'C':
        std::cout << "及格" << std::endl;
        break;
    default:
        std::cout << "不及格" << std::endl;
        break;
    }

    return 0;
}
