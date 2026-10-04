// parr-04.cpp -- *p++ 与 (*p)++ 到底差在哪
#include <iostream>
using namespace std;

int main()
{
    int a[3] = {10, 20, 30};
    int *p = a;

    cout << "*p++ 读出来的是 " << *p++ << endl;   // 先取 *p，再让 p 往后走一格
    cout << "走完之后 p 指着 " << *p << endl;

    int b[3] = {10, 20, 30};
    int *q = b;

    cout << "(*q)++ 读出来的是 " << (*q)++ << endl;  // 先取 *q，再把那个元素加一
    cout << "这时 b[0] 变成了 " << b[0] << "，q 还指着 " << *q << endl;

    return 0;
}
