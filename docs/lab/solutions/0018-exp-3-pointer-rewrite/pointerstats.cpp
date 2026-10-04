// pointerstats.cpp -- 参考解：实验三 · 用指针改写核心操作
//
// 自包含的可运行程序：拷进你的任务目录之后直接
//     g++ -std=c++17 -Wall -Wextra pointerstats.cpp -o pointerstats && ./pointerstats
// 就能跑，不依赖任务目录之外的任何东西。

#include <iostream>
#include <iomanip>
using namespace std;

const int N = 5;

double averageOf(const int *p, int n)
{
    if (p == nullptr || n <= 0)
    {
        return 0.0;
    }

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += p[i];
    }
    return static_cast<double>(sum) / n;
}

int highestOf(const int *p, int n)
{
    if (p == nullptr || n <= 0)
    {
        return -1;
    }

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

void sortDescending(int *p, int n)
{
    if (p == nullptr || n <= 1)
    {
        return;
    }

    for (int i = 0; i < n - 1; i++)
    {
        int *largest = p + i;
        for (int *q = p + i + 1; q < p + n; q++)
        {
            if (*q > *largest)
            {
                largest = q;
            }
        }

        if (largest != p + i)
        {
            int temp = *(p + i);
            *(p + i) = *largest;
            *largest = temp;
        }
    }
}

int main()
{
    int scores[N] = {88, 76, 95, 60, 82};

    cout << "原成绩表：";
    for (int *p = scores; p < scores + N; p++)
    {
        cout << *p << " ";
    }
    cout << endl;

    cout << fixed << setprecision(1);
    cout << "平均分：" << averageOf(scores, N) << endl;
    cout << "最高分：" << highestOf(scores, N) << endl;

    sortDescending(scores, N);

    cout << "排好序：";
    for (int *p = scores; p < scores + N; p++)
    {
        cout << *p << " ";
    }
    cout << endl;

    return 0;
}
