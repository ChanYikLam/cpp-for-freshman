// func-01.cpp -- 使用一个函数的三个步骤：定义、原型、调用
#include <iostream>
using namespace std;

void printLine();            // 函数原型
int add(int a, int b);       // 函数原型

int main()
{
    printLine();
    int total = add(90, 85);          // 函数调用
    cout << "两个成绩相加：" << total << endl;
    printLine();
    return 0;
}

void printLine()             // 函数定义
{
    cout << "--------------------" << endl;
}

int add(int a, int b)        // 函数定义
{
    return a + b;                   // 返回值
}
