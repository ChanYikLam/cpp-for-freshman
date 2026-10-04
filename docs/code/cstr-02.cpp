// cstr-02.cpp -- 数组不够大时，拷贝会把名字截断
#include <iostream>
#include <cstring>          // strncpy、strlen 声明在这个头文件里
using namespace std;

int main()
{
    char name[6];           // 最多装 5 个字符，剩下的那 1 格留给 '\0'

    // 用备份来接收从别处拷过来的名字：最多拷 5 个字符，不写 '\0'
    strncpy(name, "Zhang", 5);
    name[5] = '\0';         // 自己补上结尾标记，这一格刚好是数组的最后一格

    cout << "拷贝后的名字：" << name << endl;
    cout << "它占了多少格：" << strlen(name) << endl;

    // 如果来的名字更长，多出来的部分会被丢掉，数组里不会多塞东西
    char shortName[6];
    strncpy(shortName, "ZhangSan", 5);
    shortName[5] = '\0';

    cout << "更长名字存进来只剩：" << shortName << endl;

    return 0;
}
