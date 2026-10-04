#include <iostream>

using namespace std;
int main()
{
    cout << "请输入三门课的成绩：";

    int score1 = 0;
    int score2 = 0;
    int score3 = 0;
    cin >> score1 >> score2 >> score3;

    double average = (score1 + score2 + score3) / 3;

    cout << endl;
    cout << "平均分：" << average << endl;

    return 0;
}
