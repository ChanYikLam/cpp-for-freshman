// loops.cpp -- 参考解：读入一批成绩并累加出总分
//
// 自包含的可运行程序：拷进你的任务目录之后直接
//     g++ -std=c++17 -Wall -Wextra loops.cpp -o loops && ./loops < 5个成绩.in
// 就能跑，不依赖任务目录之外的任何东西。

#include <iostream>
using namespace std;

int main()
{
    int n = 0;
    cout << "请输入成绩个数：";
    cin >> n;

    double sum = 0.0;
    for (int i = 1; i <= n; i++)
    {
        double score = 0.0;
        cin >> score;
        sum += score;
    }

    cout << "共 " << n << " 个成绩，总分 " << sum << endl;
    return 0;
}
