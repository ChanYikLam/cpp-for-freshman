#include <iostream>

using namespace std;
int main()
{
    char firstLetter = 'L';
    int letterCode = firstLetter;

    cout << "首字母是 " << firstLetter << endl;
    cout << "它的编码是 " << letterCode << endl;

    firstLetter = firstLetter + 1;
    letterCode = firstLetter;
    cout << "再加 1，字符变成 " << firstLetter
              << "，编码变成 " << letterCode << endl;

    return 0;
}
