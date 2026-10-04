// loops-05.cpp -- break 与 continue：一个提前结束，一个跳过本轮
#include <iostream>
using namespace std;

int main()
{
    for (int i = 1; i <= 10; i++)
    {
        if (i % 3 == 0)
        {
            continue;              // 跳过后面的输出，直接进入下一轮
        }
        if (i == 8)
        {
            break;                 // 整个循环到此结束
        }
        cout << i << " ";
    }

    cout << endl << "循环结束" << endl;
    return 0;
}
