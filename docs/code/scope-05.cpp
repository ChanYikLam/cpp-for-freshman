// scope-05.cpp -- 局部变量的寿命：每次调用都重新出生一次
#include <iostream>
using namespace std;

void countCall()
{
    int count = 0;              // 每次进入函数都重新声明、重新赋 0
    count++;
    cout << "这一次调用看到的 count：" << count << endl;
}

int main()
{
    countCall();
    countCall();
    countCall();
    return 0;
}
