// stats-03.cpp -- 打擂台找最高分
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {90, 85, 78, 92, 88};

    int best = scores[0];            // 先让第一个元素站在擂台上
    for (int i = 1; i < 5; i++)      // 从第二个元素开始挨个挑战
    {
        if (scores[i] > best)
        {
            best = scores[i];        // 挑战者赢了，换它站在擂台上
        }
    }

    cout << "最高分：" << best << endl;
    return 0;
}
