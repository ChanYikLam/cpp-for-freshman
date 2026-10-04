// trap-01.cpp -- 现场一：空指针解引用之前的那个地址
#include <iostream>
using namespace std;

int main()
{
    int *p = nullptr;       // p 明确写着"我不指向任何东西"

    cout << "p 存的值是 " << p << endl;
    cout << "p 是不是空的：" << (p == nullptr) << endl;

    // 下一行就是崩溃点，这里先注释掉：
    // cout << *p << endl;      // 顺着地址 0 去取数据 → 段错误

    cout << "程序活着走到这里" << endl;
    return 0;
}
