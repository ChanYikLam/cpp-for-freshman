#include <iostream>

int main()
{
    int score = 89;

    std::cout << std::boolalpha;
    std::cout << "score < 60 -> " << (score < 60) << std::endl;
    std::cout << "score >= 60 -> " << (score >= 60) << std::endl;
    std::cout << "score >= 60 && score < 90 -> " << (score >= 60 && score < 90) << std::endl;

    return 0;
}
