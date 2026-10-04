// pparam-05.cpp -- const 与不带 const 的形参，用一张成绩表看清楚
#include <iostream>
using namespace std;

int total(const int *p, int n)      // 只读：加 const
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum = sum + p[i];
    return sum;
}

void everyonePass(int *p, int n)    // 要改：不加 const
{
    for (int i = 0; i < n; i++)
        if (p[i] < 60)
            p[i] = 60;
}

int main()
{
    int scores[3] = {88, 45, 30};

    cout << "改之前总分：" << total(scores, 3) << endl;

    everyonePass(scores, 3);

    cout << "改之后总分：" << total(scores, 3) << endl;
    cout << "改之后成绩表：" << scores[0] << " " << scores[1] << " " << scores[2] << endl;

    return 0;
}
