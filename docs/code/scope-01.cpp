// scope-01.cpp -- 现象：在函数里改成满分，回到 main 打印还是原来的分数
#include <iostream>
using namespace std;

void makeFull(int score)          // 想把这份成绩改成满分
{
    score = 100;
    cout << "函数里看到的成绩：" << score << endl;
}

int main()
{
    int score = 58;
    makeFull(score);
    cout << "回到 main 看到的成绩：" << score << endl;
    return 0;
}
