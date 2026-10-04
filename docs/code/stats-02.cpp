// stats-02.cpp -- 累加求和，再除以个数得到均分
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {90, 85, 78, 92, 88};

    double total = 0.0;
    for (int i = 0; i < 5; i++)
    {
        total += scores[i];
    }

    double average = total / 5;      // total 是小数，除出来的也是小数
    cout << "总分：" << total << endl;
    cout << "均分：" << average << endl;
    return 0;
}
