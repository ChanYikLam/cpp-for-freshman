// trap-04.cpp -- 现场四：指针指着的变量已经出了作用域
#include <iostream>
using namespace std;

int main()
{
    int *p = nullptr;

    {
        int score = 87;         // score 只活在这对花括号里
        p = &score;             // p 记住了它的地址
        cout << "花括号里面，*p = " << *p << endl;
    }                           // 到这里 score 就没了

    cout << "花括号外面，p 里还存着 " << p << endl;
    cout << "但它指的那块地方已经不属于这个程序了" << endl;

    return 0;
}
