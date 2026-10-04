// addr-01.cpp -- 把变量住的门牌号打印出来
#include <iostream>
using namespace std;

int main()
{
    int score = 87;
    int other = 92;
    double avg = 88.5;

    cout << "score 的值是 " << score << endl;
    cout << "score 的地址是 " << &score << endl;

    cout << "other 的值是 " << other << endl;
    cout << "other 的地址是 " << &other << endl;

    cout << "avg 的地址是 " << &avg << endl;

    // sizeof 也能量地址本身：一个地址占多少字节
    cout << "存一个地址要 " << sizeof(&score) << " 字节" << endl;

    return 0;
}
