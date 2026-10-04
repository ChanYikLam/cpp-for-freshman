// addr-02.cpp -- 用一个指针读到它指向的那个变量的值
#include <iostream>
using namespace std;

int main()
{
    int score = 87;

    int *p = &score;        // p 里存的是 score 的地址

    cout << "score 的值是 " << score << endl;
    cout << "score 的地址是 " << &score << endl;
    cout << "p 里存的地址是 " << p << endl;      // 和上一行是同一个数

    cout << "顺着 p 找到的房子装的是 " << *p << endl;   // 87

    *p = 100;               // 按门牌号进屋，把里面的东西换成 100

    cout << "改完之后 score 是 " << score << endl;
    cout << "p 里存的地址还是 " << p << "（没变）" << endl;

    return 0;
}
