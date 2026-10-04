// pointerstats.cpp -- 用指针走两遍成绩表
//
// 这是留白版：两处 TODO 等你补。它能编译，但两个总分都是 0。
// 任务说明与预期输出见同目录的 README.md。

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
    // TODO 1：让 p 从 scores 出发，每轮把 *p 加进 totalByPointer，直到走过最后一格。
    int totalByPointer = 0;
    int *p = scores;

    cout << "指针版总分：" << totalByPointer << endl;

    // 第二遍：指针不动，用 *(p + i) 取元素
    // TODO 2：p 只指向起点，取元素写 *(p + i)，循环变量用 i。
    //         这一遍要把总分算进 totalByIndex。
    int totalByIndex = 0;

    double average = totalByIndex / N;      // 均分要用小数算

    cout << "*(p + i) 版总分：" << totalByIndex << endl;
    cout << fixed << setprecision(1);
    cout << "*(p + i) 版平均分：" << average << endl;

    return 0;
}
