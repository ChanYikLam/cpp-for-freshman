// cstr-01.cpp -- 字符数组是怎么存一串字符的
#include <iostream>
#include <cstring>          // strlen 声明在这个头文件里
using namespace std;

int main()
{
    // 写法一：一个一个字符地列出来，最后一个必须是 '\0'
    char name1[8] = {'L', 'i', 'u', '\0'};

    // 写法二：直接用双引号里的字符串初始化，'\0' 由编译器自动补在末尾
    char name2[8] = "Zhang";

    cout << "名字一：" << name1 << endl;
    cout << "名字二：" << name2 << endl;

    cout << "name1 里装了 " << sizeof(name1) << " 字节" << endl;
    cout << "name1 这个名字有 " << strlen(name1) << " 个字符" << endl;

    cout << "name2 里装了 " << sizeof(name2) << " 字节" << endl;
    cout << "name2 这个名字有 " << strlen(name2) << " 个字符" << endl;

    return 0;
}
