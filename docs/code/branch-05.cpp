#include <iostream>

using namespace std;
int main()
{
    int score = 0;

    cout << "请输入成绩（0 到 100）：";
    while (!(cin >> score) || score < 0 || score > 100)
    {
        cout << "这个数不能用，请重新输入一个 0 到 100 的整数：";
        cin.clear();
        cin.ignore(1000, '\n');
    }

    cout << "收到的成绩是 " << score << endl;

    return 0;
}
