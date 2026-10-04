// pparam-00.cpp -- 先试试"函数接收一个数组"最想写的样子
#include <iostream>
using namespace std;

int total(int table[5])         // 形参写成数组的样子
{
    int sum = 0;
    for (int i = 0; i < 5; i++)
        sum = sum + table[i];
    return sum;
}

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};
    cout << "总分：" << total(scores) << endl;
    return 0;
}
