// temp.cpp -- 参考解：实验一 · 题目 A（体温换算）
//
// 自包含的可运行程序：拷进你的任务目录之后直接
//     g++ -std=c++17 -Wall -Wextra temp.cpp -o temp && ./temp < 体温输入.txt
// 就能跑，不依赖任务目录之外的任何东西。

#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
    cout << "请输入体温（华氏度，例如 98.6）：";

    double fahrenheit = 0.0;
    cin >> fahrenheit;

    const double kOffset = 32.0;
    const double kScale = 5.0 / 9.0;
    double celsius = (fahrenheit - kOffset) * kScale;

    cout << fixed << setprecision(1);
    cout << "华氏 " << fahrenheit << " 度";
    cout << " = 摄氏 " << celsius << " 度" << endl;

    return 0;
}
