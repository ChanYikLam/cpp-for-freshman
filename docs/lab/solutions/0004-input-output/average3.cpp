// average3.cpp -- 参考解：读入三门课的成绩，算出总分与平均分
//
// 这是一份自包含的可运行程序：把它拷进你的任务目录，直接
//     g++ -std=c++17 -Wall -Wextra average3.cpp -o average3 && ./average3 < 成绩.txt
// 就能跑，不依赖任务目录之外的任何东西。

#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
    cout << "请输入三门课的成绩（用空格或回车分开）：";

    double score1 = 0.0;
    double score2 = 0.0;
    double score3 = 0.0;

    while (!(cin >> score1 >> score2 >> score3))
    {
        cout << "这组输入不是三个数，请重新输入：";
        cin.clear();
        cin.ignore(1000, '\n');
    }

    const int kSubjectCount = 3;
    double total = score1 + score2 + score3;
    double average = total / kSubjectCount;

    cout << fixed << setprecision(1);
    cout << "总分：" << total << endl;
    cout << "平均分：" << average << endl;

    return 0;
}
