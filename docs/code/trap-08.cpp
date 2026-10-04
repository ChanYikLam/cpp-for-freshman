// trap-08.cpp -- 反例：把成绩写到数组外面去了
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};

    for (int i = 0; i <= 5; i++)     // i 从 0 到 5，一共 6 次
        scores[i] = 100;             // 最后一次写的是 scores[5]，那格不属于这张表

    cout << "循环跑完了，程序看着没事" << endl;
    for (int i = 0; i < 5; i++)
        cout << scores[i] << " ";
    cout << endl;

    return 0;
}
