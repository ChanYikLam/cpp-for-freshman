// pparam-02.cpp -- 把统计写成接收指针的函数
#include <iostream>
using namespace std;

int total(const int *p, int n)      // 只看不改，加 const 让编译器帮忙看着
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum = sum + p[i];
    return sum;
}

int highest(const int *p, int n)
{
    int top = p[0];
    for (int i = 1; i < n; i++)
        if (p[i] > top)
            top = p[i];
    return top;
}

void addBonus(int *p, int n, int bonus)   // 要通过指针改调用方的数据
{
    for (int i = 0; i < n; i++)
        p[i] = p[i] + bonus;
}

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};

    cout << "总分：" << total(scores, 5) << endl;
    cout << "最高分：" << highest(scores, 5) << endl;

    addBonus(scores, 5, 2);         // 全班各加 2 分

    cout << "加分后：";
    for (int i = 0; i < 5; i++)
        cout << scores[i] << " ";
    cout << endl;

    return 0;
}
