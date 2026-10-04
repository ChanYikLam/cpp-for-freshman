// parr-03.cpp -- 用指针走完整张成绩表，求出总分与最高分
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};
    int n = 5;

    int total = 0;
    int highest = *scores;          // 打擂台：先让第一个元素站上擂台

    for (int *p = scores; p < scores + n; p++)
    {
        total = total + *p;
        if (*p > highest)
            highest = *p;
    }

    cout << "成绩表：";
    for (int *p = scores; p < scores + n; p++)
        cout << *p << " ";
    cout << endl;

    cout << "总分：" << total << endl;
    cout << "平均分：" << total * 1.0 / n << endl;
    cout << "最高分：" << highest << endl;

    return 0;
}
