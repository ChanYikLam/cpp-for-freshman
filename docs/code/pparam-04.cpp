// pparam-04.cpp -- 反例：标了 const 却还想改
#include <iostream>
using namespace std;

int total(const int *p, int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum = sum + p[i];
        p[i] = 0;           // 想把读过的格子清零，编译器不允许
    }
    return sum;
}

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};
    cout << total(scores, 5) << endl;
    return 0;
}
