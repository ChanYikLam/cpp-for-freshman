// pparam-03.cpp -- 形参里的 sizeof 量不到数组的长度
#include <iostream>
using namespace std;

int total(const int *p, int n)      // 形参 p 是一个指针
{
    cout << "函数里 sizeof(p) = " << sizeof(p) << " 字节" << endl;
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum = sum + p[i];
    return sum;
}

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};

    cout << "main 里 sizeof(scores) = " << sizeof(scores) << " 字节" << endl;
    cout << "也就是说这个数组有 " << sizeof(scores) / sizeof(scores[0]) << " 个元素" << endl;

    cout << "总分：" << total(scores, 5) << endl;

    return 0;
}
