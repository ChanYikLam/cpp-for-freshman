// func-02.cpp -- 把求平均包成一个函数，在 main 里调用它
#include <iostream>
using namespace std;

double average(double sum, int count);      // 函数原型

int main()
{
    int n;
    cout << "请输入成绩个数：";
    cin >> n;

    double sum = 0.0;
    for (int i = 0; i < n; i++)
    {
        double score;
        cin >> score;
        sum += score;
    }

    cout << "总分：" << sum << endl;
    cout << "平均分：" << average(sum, n) << endl;      // 函数调用
    return 0;
}

double average(double sum, int count)       // 函数定义
{
    return sum / count;                     // 返回值
}
