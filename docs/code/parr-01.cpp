// parr-01.cpp -- 数组名就是第一个元素的地址
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};

    cout << "scores[0] 的值是 " << scores[0] << endl;
    cout << "scores[0] 的地址是 " << &scores[0] << endl;
    cout << "scores 本身打印出来是 " << scores << endl;

    cout << "scores[1] 的地址是 " << &scores[1] << endl;

    int *p = scores;        // 把第一个元素的地址交给指针

    cout << "p 里存的地址是 " << p << endl;
    cout << "p 指着的那个元素是 " << *p << endl;

    return 0;
}
