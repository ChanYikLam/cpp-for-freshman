// addr-03.cpp -- 同一个变量，值传递改不动，传地址改得动
#include <iostream>
using namespace std;

void tryByValue(int x)          // 形参是 int：拿到的是副本
{
    x = 100;
}

void tryByAddress(int *p)       // 形参是 int *：拿到的是地址
{
    *p = 100;
}

int main()
{
    int score = 60;

    tryByValue(score);
    cout << "值传递之后 score 是 " << score << endl;

    tryByAddress(&score);       // 把 score 的地址交出去
    cout << "传地址之后 score 是 " << score << endl;

    return 0;
}
