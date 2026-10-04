// pointerstats.cpp -- 实验三：用指针改写核心操作
//
// 这是留白版：四处 TODO 等你补。能编译，但三个结果都不对。
// 任务书、验收标准与预期输出见同目录的 README.md。

#include <iostream>
#include <iomanip>
using namespace std;

const int N = 5;

// TODO 1：交回平均分。先判空与边界，再遍历求和。
//         形参是只读指针，所以标 const。
double averageOf(const int *p, int n)
{
    return 0.0;
}

// TODO 2：打擂台交回最高分。擂主初值取 p[0]。
int highestOf(const int *p, int n)
{
    return 0;
}

// TODO 3：就地按从大到小排好 p 指着的 n 个元素。
//         要点：交换的是元素的值，不是两个指针变量。
void sortDescending(int *p, int n)
{
    // 这里现在什么都没做。
}

int main()
{
    int scores[N] = {88, 76, 95, 60, 82};

    // TODO 4：把这一处下标遍历改成指针遍历（p 从 scores 出发，走到 scores + N）。
    cout << "原成绩表：";
    for (int i = 0; i < N; i++)
    {
        cout << scores[i] << " ";
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
