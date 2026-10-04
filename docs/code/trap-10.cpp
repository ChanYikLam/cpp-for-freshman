// trap-10.cpp -- 反例：以为在遍历，其实在改数据
#include <iostream>
using namespace std;

int main()
{
    int scores[4] = {88, 76, 95, 60};
    int *p = scores;

    for (int i = 0; i < 4; i++)
        (*p)++;                 // 每一轮都是把 scores[0] 加一，p 一直没动

    cout << "走完之后 p 指着 " << *p << endl;
    for (int i = 0; i < 4; i++)
        cout << scores[i] << " ";
    cout << endl;

    return 0;
}
