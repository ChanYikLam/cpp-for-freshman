// arr-03.cpp -- 用数组存下 10 个成绩，再逐个打印
#include <iostream>
using namespace std;

int main()
{
    const int N = 10;           // 元素个数必须是编译时就能定下来的常量
    int scores[N];

    cout << "请依次输入 " << N << " 个成绩：" << endl;
    for (int i = 0; i < N; i++)
    {
        cin >> scores[i];
    }

    for (int i = 0; i < N; i++)
    {
        cout << "第 " << i + 1 << " 位：" << scores[i] << " 分" << endl;
    }
    return 0;
}
