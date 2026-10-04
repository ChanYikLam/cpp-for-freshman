// loops-03.cpp -- while 循环：读到 -1 为止，事先不知道有几个成绩
#include <iostream>
using namespace std;

int main()
{
    double sum = 0.0;
    int count = 0;
    double score;

    cout << "逐条输入成绩，输入 -1 表示结束：" << endl;
    cin >> score;
    while (score >= 0)
    {
        sum += score;
        count++;
        cin >> score;
    }

    cout << "共 " << count << " 个成绩，总分 " << sum << endl;
    return 0;
}
