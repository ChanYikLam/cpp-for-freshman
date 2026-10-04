// func-04.cpp -- 函数重载：同名函数，靠实参对号入座
#include <iostream>
using namespace std;

void show(int score);
void show(double score);
void show(int score, int full);

int main()
{
    show(86);            // 一个 int 实参，匹配 show(int)
    show(86.5);          // 一个 double 实参，匹配 show(double)
    show(86, 150);       // 两个 int 实参，匹配 show(int, int)
    return 0;
}

void show(int score)
{
    cout << "整数成绩：" << score << endl;
}

void show(double score)
{
    cout << "带小数的成绩：" << score << endl;
}

void show(int score, int full)
{
    cout << "成绩 " << score << "，满分 " << full << endl;
}
