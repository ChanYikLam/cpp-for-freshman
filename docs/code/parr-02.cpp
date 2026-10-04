// parr-02.cpp -- 指针算术：p+1 走多远，sizeof 量什么
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};
    int *p = scores;

    cout << "p     指向的地址是 " << p << "，值是 " << *p << endl;
    cout << "p + 1 指向的地址是 " << (p + 1) << "，值是 " << *(p + 1) << endl;
    cout << "p + 2 指向的地址是 " << (p + 2) << "，值是 " << *(p + 2) << endl;

    cout << "sizeof(scores) 是 " << sizeof(scores) << " 字节" << endl;
    cout << "sizeof(p) 是 " << sizeof(p) << " 字节" << endl;
    cout << "5 个 int 一共占 " << 5 * sizeof(int) << " 字节" << endl;

    return 0;
}
