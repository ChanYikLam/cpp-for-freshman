// loops-04.cpp -- do-while 循环：先读一次，再判断要不要继续
#include <iostream>
using namespace std;

int main()
{
    double sum = 0.0;
    int count = 0;
    double score;

    cout << "逐条输入成绩，输入 -1 表示结束：" << endl;
    do
    {
        cin >> score;
        if (score >= 0)
        {
            sum += score;
            count++;
        }
    } while (score >= 0);

    cout << "共 " << count << " 个成绩，总分 " << sum << endl;
    return 0;
}
