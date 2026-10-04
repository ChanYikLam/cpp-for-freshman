// func-03.cpp -- 参数默认值：调用时可以不写末尾那个实参
#include <iostream>
using namespace std;

void printScore(int score, int full = 100);      // 末尾的形参有默认值

int main()
{
    printScore(86);          // 只传一个实参，full 用默认值 100
    printScore(86, 150);     // 传两个实参，full 取 150
    return 0;
}

void printScore(int score, int full)
{
    cout << score << " / " << full << endl;
}
