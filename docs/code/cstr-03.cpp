// cstr-03.cpp -- 比较两个姓名：为什么 == 不管用，strcmp 怎么用
#include <iostream>
#include <cstring>          // strcmp 声明在这个头文件里
using namespace std;

int main()
{
    char a[8] = "Zhang";
    char b[8] = "Zhang";
    char c[8] = "Liu";

    if (a == b)                       // 比的是两个数组各自的地址
        cout << "a == b 说：两个名字相同" << endl;
    else
        cout << "a == b 说：两个名字不同（其实内容是一样的）" << endl;

    if (strcmp(a, b) == 0)            // 比的是逐个字符的内容
        cout << "strcmp(a, b) 说：两个名字相同" << endl;
    else
        cout << "strcmp(a, b) 说：两个名字不同" << endl;

    if (strcmp(a, c) != 0)
        cout << "strcmp(a, c) 说：两个名字不同" << endl;

    cout << "strcmp(a, c) 返回 " << strcmp(a, c) << "（正数表示 a 排在 c 后面）" << endl;
    cout << "strcmp(c, a) 返回 " << strcmp(c, a) << "（负数表示 c 排在 a 前面）" << endl;

    return 0;
}
