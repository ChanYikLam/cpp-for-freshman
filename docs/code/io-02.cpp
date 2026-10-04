#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
    const int kSubjectCount = 3;

    cout << "请输入三门课的成绩（用空格或回车分开）：";

    double score1 = 0.0;
    double score2 = 0.0;
    double score3 = 0.0;
    cin >> score1 >> score2 >> score3;

    double total = score1 + score2 + score3;
    double average = total / kSubjectCount;

    cout << fixed << setprecision(1);
    cout << endl;
    cout << "三门成绩：" << score1 << "、" << score2 << "、" << score3 << endl;
    cout << "总分：" << total << endl;
    cout << "平均分：" << average << endl;

    return 0;
}
