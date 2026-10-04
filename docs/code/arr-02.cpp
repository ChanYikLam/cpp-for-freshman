// arr-02.cpp -- 初始化列表：写几个就填几个，剩下的一律补 0
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {90, 85, 78};       // 只写三个，后面两个补 0
    int blank[5] = {};                  // 一对空花括号：全部为 0

    cout << "scores：";
    for (int i = 0; i < 5; i++)
    {
        cout << scores[i] << " ";
    }
    cout << endl;

    cout << "blank：";
    for (int i = 0; i < 5; i++)
    {
        cout << blank[i] << " ";
    }
    cout << endl;
    return 0;
}
