// arr-04.cpp -- 越界访问：编译器不拦，程序照跑
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {90, 85, 78, 92, 88};

    cout << "scores[0] = " << scores[0] << endl;
    cout << "scores[4] = " << scores[4] << endl;
    cout << "scores[5] = " << scores[5] << endl;      // 下标 5 不存在
    return 0;
}
