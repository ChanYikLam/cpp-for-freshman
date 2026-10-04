// loops-06.cpp -- 反例：循环体里忘了更新循环变量
#include <iostream>
using namespace std;

int main()
{
    int i = 0;
    while (i < 5)
    {
        cout << "第 " << i + 1 << " 次循环" << endl;
        // 这里本该有 i++，漏掉了：i 一直是 0，条件永远成立
    }

    cout << "循环结束" << endl;
    return 0;
}
