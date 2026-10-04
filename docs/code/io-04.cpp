#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
    cout << "请输入三个成绩：";

    double score1 = 0.0;
    double score2 = 0.0;
    double score3 = 0.0;
    cin >> score1 >> score2 >> score3;

    cout << "读到的三个数：" << score1 << " " << score2 << " " << score3 << endl;
    cout << "输入是否成功：" << boolalpha << static_cast<bool>(cin) << endl;

    return 0;
}
