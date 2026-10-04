// scorestats.cpp -- 参考解：实验二 · 存下 10 个成绩，
// 算出总分、平均分与最高分
//
// 自包含的可运行程序：拷进你的任务目录之后直接
//     g++ -std=c++17 -Wall -Wextra scorestats.cpp -o scorestats
//     ./scorestats < 10个成绩.in
// 就能跑，不依赖任务目录之外的任何东西。

#include <iostream>
#include <iomanip>
using namespace std;

const int N = 10;

int totalOf(const int *p, int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += p[i];
    }
    return sum;
}

int highestOf(const int *p, int n)
{
    int top = p[0];
    for (int i = 1; i < n; i++)
    {
        if (p[i] > top)
        {
            top = p[i];
        }
    }
    return top;
}

int main()
{
    int scores[N];

    cout << "请依次输入 " << N << " 个成绩：" << endl;
    for (int i = 0; i < N; i++)
    {
        cin >> scores[i];
    }

    int total = totalOf(scores, N);
    int highest = highestOf(scores, N);
    double average = static_cast<double>(total) / N;

    cout << fixed << setprecision(1);
    cout << "总分：" << total << endl;
    cout << "平均分：" << average << endl;
    cout << "最高分：" << highest << endl;

    return 0;
}
