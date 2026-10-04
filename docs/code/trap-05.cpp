// trap-05.cpp -- 加一道判空检查，崩溃消失
#include <iostream>
using namespace std;

int highest(const int *p, int n)
{
    if (p == nullptr || n <= 0)     // 先问清楚：这张表到底存不存在
        return -1;                  // 没有成绩表，就交回一个说得清的标志

    int top = p[0];
    for (int i = 1; i < n; i++)
        if (p[i] > top)
            top = p[i];
    return top;
}

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};

    cout << "正常调用：" << highest(scores, 5) << endl;
    cout << "交一张不存在的表：" << highest(nullptr, 5) << endl;
    cout << "交一张空的表：" << highest(scores, 0) << endl;
    cout << "三种情况都打印完了，程序没有崩" << endl;

    return 0;
}
