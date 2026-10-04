// stats-05.cpp -- 反例：找最大值的比较号写反了
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {90, 85, 78, 92, 88};

    int best = scores[0];
    for (int i = 1; i < 5; i++)
    {
        if (scores[i] < best)        // 写成 < 之后，留在擂台上的是最小的那个
        {
            best = scores[i];
        }
    }

    cout << "最高分：" << best << endl;      // 打印出来的其实是 78
    return 0;
}
