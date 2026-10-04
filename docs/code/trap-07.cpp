// trap-07.cpp -- 反例：把没初始化的指针直接传出去用
#include <iostream>
using namespace std;

int main()
{
    int *p;
    *p = 90;                // p 里还不知道是什么地址，就往那儿写数据
    cout << *p << endl;
    return 0;
}
