// pparam-01.cpp -- 同一个变量，函数里看到的和外面看到的是不是同一个
#include <iostream>
using namespace std;

void tryByValue(int x)          // 形参不是指针：拿到的是副本
{
    x = 100;
    cout << "  函数里（值传递）x 现在是 " << x << endl;
}

void tryByPointer(int *p)       // 形参是指针：拿到的是地址
{
    *p = 100;
    cout << "  函数里（指针）*p 现在是 " << *p << endl;
}

int main()
{
    int score = 60;

    cout << "调用前 score 是 " << score << endl;
    tryByValue(score);
    cout << "值传递之后 score 是 " << score << endl;

    tryByPointer(&score);
    cout << "指针传参之后 score 是 " << score << endl;

    return 0;
}
