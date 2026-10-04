// scope-04.cpp -- 全局变量，以及同名的局部变量把它挡住
#include <iostream>
using namespace std;

int fullScore = 100;            // 写在所有函数外面：全局变量

void printFull()
{
    int fullScore = 150;        // 本函数自己的同名局部变量
    cout << "函数里看到的满分：" << fullScore << endl;
}

int main()
{
    printFull();
    cout << "main 里看到的满分：" << fullScore << endl;
    return 0;
}
