#include <iostream>

using namespace std;
int main()
{
    int score = 150;

    if (60 <= score <= 100)
    {
        cout << "分数合法" << endl;
    }
    else
    {
        cout << "分数不合法" << endl;
    }

    return 0;
}
