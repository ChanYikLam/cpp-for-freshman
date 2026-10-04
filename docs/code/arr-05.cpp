// arr-05.cpp -- 反例：数组没初始化就直接累加
#include <iostream>
using namespace std;

int main()
{
    int scores[5];                  // 没有初始化，元素里是内存中原有的数据
    int total = 0;

    for (int i = 0; i < 5; i++)
    {
        total += scores[i];         // 读到的是没有意义的值
    }

    cout << "总分：" << total << endl;
    return 0;
}
