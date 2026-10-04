// func-05.cpp -- 反例：分支里的 return 漏了一条路径
#include <iostream>
using namespace std;

int level(int score)
{
    if (score >= 60)
    {
        return 1;
    }
    // 成绩小于 60 时没有 return，函数直接走到末尾
}

int main()
{
    cout << level(75) << endl;
    cout << level(40) << endl;      // 这里打印出来的值没有意义
    return 0;
}
