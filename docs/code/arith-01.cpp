#include <iostream>

using namespace std;
int main()
{
    int chineseScore = 92;
    int mathScore = 88;
    int englishScore = 87;
    int total = chineseScore + mathScore + englishScore;

    int average = total / 3;
    cout << "整数写法：" << total << " / 3 = " << average << endl;

    double decimalAverage = total / 3.0;
    cout << "小数写法：" << total << " / 3.0 = " << decimalAverage << endl;

    double castAverage = static_cast<double>(total) / 3;
    cout << "强制转换：" << total << " 转成 double 再 / 3 = " << castAverage << endl;

    return 0;
}
