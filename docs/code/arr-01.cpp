// arr-01.cpp -- 声明一个数组，用下标往里存、往外取
#include <iostream>
using namespace std;

int main()
{
    int scores[5];              // 5 个 int，共用一个名字 scores

    scores[0] = 90;
    scores[1] = 85;
    scores[2] = 78;
    scores[3] = 92;
    scores[4] = 88;

    cout << "第 1 个成绩：" << scores[0] << endl;
    cout << "第 5 个成绩：" << scores[4] << endl;
    return 0;
}
