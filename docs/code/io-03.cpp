#include <iostream>

int main()
{
    int age = 0;
    char grade = ' ';

    std::cout << "请输入年龄：";
    std::cin >> age;
    std::cout << "请输入等级（A/B/C）：";
    std::cin >> grade;
    std::cout << "年龄：" << age << "，等级：" << grade << std::endl;

    return 0;
}
