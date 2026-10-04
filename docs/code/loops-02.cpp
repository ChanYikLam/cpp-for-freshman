// loops-02.cpp -- 读入已知个数的一批成绩，累加出总分
#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "请输入成绩个数：";
    cin >> n;

    double sum = 0.0;
    for (int i = 0; i < n; i++)
    {
        double score;
        cin >> score;
        sum += score;
    }

    cout << "共 " << n << " 个成绩，总分 " << sum << endl;
    return 0;
}
