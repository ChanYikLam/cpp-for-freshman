// loops-01.cpp -- for 循环的三个部分，以及两种边界的差别
#include <iostream>
using namespace std;

int main()
{
    cout << "用 i < 5 控制，i 依次取到：";
    for (int i = 0; i < 5; i++)
    {
        cout << i << " ";
    }
    cout << endl;

    cout << "用 i <= 5 控制，i 依次取到：";
    for (int i = 0; i <= 5; i++)
    {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
