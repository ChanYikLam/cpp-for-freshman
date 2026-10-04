// trap-03.cpp -- 现场三：越界——指针走到数组末尾之后还在解引用
#include <iostream>
using namespace std;

int main()
{
    int scores[5] = {88, 76, 95, 60, 82};

    int *p = scores;
    for (int i = 0; i < 3; i++)
        p++;                    // 走三格，指向 scores[3]

    cout << "p 现在指着 " << *p << endl;     // 60，还在范围内

    cout << "再往后走一格：" << *(p + 1) << endl;   // 82，也还在范围内

    cout << "继续往后：" << *(p + 5) << endl;       // 越界了，读到的是别处的字节

    return 0;
}
