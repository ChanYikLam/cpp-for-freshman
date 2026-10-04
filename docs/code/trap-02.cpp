// trap-02.cpp -- 现场二：野指针——没初始化的指针里是什么
#include <iostream>
using namespace std;

int main()
{
    int *p;                 // 只说了"p 是个能存地址的变量"，没给地址

    cout << "p 里现在装着 " << p << endl;
    cout << "第二次运行，这个数又会不一样" << endl;

    return 0;
}
