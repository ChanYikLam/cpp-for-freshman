// cstr-04.cpp -- 成绩表带上"谁"：姓名表与分数表用同一个下标对齐
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char names[4][10] = {"Zhang", "Liu", "Chen", "Wang"};
    int  scores[4]    = {88, 76, 95, 60};
    int n = 4;

    cout << "成绩表：" << endl;
    for (int i = 0; i < n; i++)
        cout << "  " << names[i] << "  " << scores[i] << " 分" << endl;

    // 找一个人：把所有姓名挨个比一遍
    char who[10] = "Chen";
    int found = -1;                     // 约定 -1 表示没找到
    for (int i = 0; i < n; i++)
        if (strcmp(names[i], who) == 0)
            found = i;

    if (found >= 0)
        cout << who << " 的成绩是 " << scores[found] << " 分" << endl;
    else
        cout << "表里没有 " << who << endl;

    return 0;
}
