// arr-06.cpp -- sizeof：数组占多少字节，里面有几个元素
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {90, 85, 78, 92, 88};

    cout << "整个数组占的字节数：" << sizeof scores << endl;
    cout << "一个元素占的字节数：" << sizeof scores[0] << endl;
    cout << "元素个数：" << sizeof scores / sizeof scores[0] << endl;
    return 0;
}
