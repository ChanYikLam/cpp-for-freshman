// stats-01.cpp -- 遍历：挨个看一遍，把每个成绩打印出来
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {90, 85, 78, 92, 88};

    for (int i = 0; i < 5; i++)
    {
        cout << "第 " << i + 1 << " 个：" << scores[i] << endl;
    }
    return 0;
}
