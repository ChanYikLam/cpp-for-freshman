// stats.cpp -- 读入 10 个成绩，算出总分、平均分与最高分
//
// 这是留白版：三处 TODO 等你补。它能编译，但三个数字都不对。
// 任务说明与预期输出见同目录的 README.md。

#include <iostream>
#include <iomanip>
using namespace std;

const int N = 10;

// TODO 1：遍历 p 指着的 n 个成绩，交回总分。
//         形参标了 const，表示这个函数只看不改。
int totalOf(const int *p, int n)
{
    return 0;
}

// TODO 2：打擂台交回最高分。擂主初值取第一个元素，循环从第二个元素开始。
int highestOf(const int *p, int n)
{
    return 0;
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

    // TODO 3：均分要用小数算，别让整数除法把小数截掉。
    double average = total / N;

    cout << fixed << setprecision(1);
    cout << "总分：" << total << endl;
    cout << "平均分：" << average << endl;
    cout << "最高分：" << highest << endl;

    return 0;
}
