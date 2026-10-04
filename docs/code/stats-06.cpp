// stats-06.cpp -- 反例：循环少跑一个元素
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {90, 85, 78, 92, 88};

    double total = 0.0;
    for (int i = 0; i < 4; i++)      // 只跑到下标 3，最后一个元素没进统计
    {
        total += scores[i];
    }

    cout << "总分：" << total << endl;
    return 0;
}
