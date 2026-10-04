// scorestats.cpp -- 实验二：存下 10 个成绩，算出总分、平均分与最高分
//
// 这是留白版：四处 TODO 等你补。能编译，但三个数字都不对。
// 任务书、验收标准与预期输出见同目录的 README.md。

#include <iostream>
#include <iomanip>
using namespace std;

// TODO 1：把成绩的个数写成一个常量，声明与下面的循环都用它。

// TODO 2：交回总分的函数（只读，形参加 const）。
int totalOf(const int *p, int n)
{
    return 0;
}

// TODO 3：打擂台交回最高分的函数。擂主初值取第一个元素，循环从第二个开始。
int highestOf(const int *p, int n)
{
    return 0;
}

int main()
{
    // TODO 4：用 TODO 1 那个常量声明数组，然后把成绩一个个读进来。

    int scores[10] = {0};
    for (int i = 0; i < 10; i++)
    {
        cin >> scores[i];
    }

    int total = totalOf(scores, 10);
    int highest = highestOf(scores, 10);

    // 均分要用小数算，别让整数除法把小数截掉。
    double average = total / 10;

    cout << fixed << setprecision(1);
    cout << "总分：" << total << endl;
    cout << "平均分：" << average << endl;
    cout << "最高分：" << highest << endl;

    return 0;
}
