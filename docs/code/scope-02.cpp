// scope-02.cpp -- 两个函数里的同名变量，是两份互不相干的内存
#include <iostream>
using namespace std;

void report();
void adjust();

int main()
{
    report();
    adjust();
    return 0;
}

void report()
{
    int total = 90 + 85;                    // report 自己的 total
    cout << "report 里的 total：" << total << endl;
}

void adjust()
{
    int total = 10;                         // adjust 自己的 total
    cout << "adjust 里的 total：" << total << endl;
}
