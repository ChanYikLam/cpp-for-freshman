#include <iostream>

using namespace std;
int main()
{
    int age = 0;
    char grade = ' ';

    cout << "请输入年龄：";
    cin >> age;
    cout << "请输入等级（A/B/C）：";
    cin >> grade;
    cout << "年龄：" << age << "，等级：" << grade << endl;

    return 0;
}
