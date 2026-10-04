// trap-09.cpp -- 反例：把 p 和 *p 弄混了
#include <iostream>
using namespace std;

int main()
{
    int score = 60;
    int *p = &score;

    p = 100;        // 想给成绩满分，写成了给指针赋值

    cout << score << endl;
    return 0;
}
