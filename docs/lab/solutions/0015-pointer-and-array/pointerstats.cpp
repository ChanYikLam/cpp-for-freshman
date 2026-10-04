// pointerstats.cpp -- 参考解：用指针走两遍成绩表
//
// 自包含的可运行程序：拷进你的任务目录之后直接
//     g++ -std=c++17 -Wall -Wextra pointerstats.cpp -o pointerstats && ./pointerstats
// 就能跑，不依赖任务目录之外的任何东西。

#include <iostream>
#include <iomanip>
using namespace std;

const int N = 5;

int main()
{
    int scores[N] = {88, 76, 95, 60, 82};

    cout << "成绩表：";
    for (int i = 0; i < N; i++)
    {
        cout << scores[i] << " ";
    }
    cout << endl;

    // 第一遍：指针自增，从头走到尾
    int totalByPointer = 0;
    for (int *p = scores; p < scores + N; p++)
    {
        totalByPointer += *p;
    }

    cout << "指针版总分：" << totalByPointer << endl;

    // 第二遍：指针不动，用 *(p + i) 取元素
    int totalByIndex = 0;
    int *p = scores;
    for (int i = 0; i < N; i++)
    {
        totalByIndex += *(p + i);
    }

    double average = static_cast<double>(totalByIndex) / N;

    cout << "*(p + i) 版总分：" << totalByIndex << endl;
    cout << fixed << setprecision(1);
    cout << "*(p + i) 版平均分：" << average << endl;

    return 0;
}
