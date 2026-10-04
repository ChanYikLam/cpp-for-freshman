// stats-04.cpp -- 完整版：读入 10 个成绩，算总分、均分、最高分
#include <iostream>
using namespace std;

int main()
{
    const int N = 10;
    int scores[N];

    cout << "请依次输入 " << N << " 个成绩：" << endl;
    for (int i = 0; i < N; i++)
    {
        cin >> scores[i];
    }

    double total = 0.0;
    int best = scores[0];
    for (int i = 0; i < N; i++)
    {
        total += scores[i];
        if (scores[i] > best)
        {
            best = scores[i];
        }
    }

    double average = total / N;
    cout << "总分：" << total << endl;
    cout << "均分：" << average << endl;
    cout << "最高分：" << best << endl;
    return 0;
}
