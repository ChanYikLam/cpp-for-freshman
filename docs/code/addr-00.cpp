// addr-00.cpp -- 第 9 章那个没解释的现象
#include <iostream>
using namespace std;

void tryByValue(int x)
{
    x = 100;
    cout << "函数里 x 现在是 " << x << endl;
}

int main()
{
    int score = 60;
    tryByValue(score);
    cout << "回到 main，score 还是 " << score << endl;
    return 0;
}
