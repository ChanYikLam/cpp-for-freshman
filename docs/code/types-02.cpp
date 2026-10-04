#include <iostream>

using namespace std;
int main()
{
    int chineseScore = 92;
    int mathScore = 88;
    int englishScore = 87;
    int total = chineseScore + mathScore + englishScore;
    double average = total / 3;

    cout << "总分：" << total << "，平均分：" << average << endl;

    return 0;
}
