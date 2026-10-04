// func-06.cpp -- 反例：void 函数里 return 一个值
#include <iostream>
using namespace std;

void printScore(int score)
{
    cout << "成绩：" << score << endl;
    return score;          // 编译错误：void 函数不能交回一个值
}

int main()
{
    printScore(86);
    return 0;
}
