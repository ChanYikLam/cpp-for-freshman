#include <iostream>

using namespace std;
int main()
{
    int score = 0;

    cout << "请输入成绩：";
    cin >> score;

    if (cin.fail())
    {
        cout << "\n这一段不是数字，读入失败了。丢弃这一行，重新读一次。\n";
        cin.clear();
        cin.ignore(1000, '\n');

        cout << "请重新输入成绩：";
        cin >> score;
    }

    cout << "最终读到：" << score << endl;

    return 0;
}
