// trap-06.cpp -- 反例：指针指着的变量已经出了作用域，还想继续用它
#include <iostream>
using namespace std;

int *makePointer()
{
    int score = 87;         // score 是函数的局部变量
    return &score;          // 把它的地址交出去
}

int main()
{
    int *p = makePointer();
    cout << *p << endl;     // 函数早就结束了，那块地方已经不归 score 了
    return 0;
}
