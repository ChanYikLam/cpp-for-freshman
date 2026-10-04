// scope-03.cpp -- 反例：在花括号里声明的变量，出了花括号就不认识了
#include <iostream>
using namespace std;

int main()
{
    {
        int temp = 60;          // temp 的作用域就是这个花括号
    }

    cout << temp << endl;       // 编译错误：这里已经看不见 temp
    return 0;
}
