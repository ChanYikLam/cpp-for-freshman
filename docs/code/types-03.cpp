#include <iostream>

int main()
{
    char firstLetter = 'L';
    int letterCode = firstLetter;

    std::cout << "首字母是 " << firstLetter << std::endl;
    std::cout << "它的编码是 " << letterCode << std::endl;

    firstLetter = firstLetter + 1;
    letterCode = firstLetter;
    std::cout << "再加 1，字符变成 " << firstLetter
              << "，编码变成 " << letterCode << std::endl;

    return 0;
}
