#include <iostream>

using namespace std;
int main()
{
    int score = 72;

    if (score >= 90)
    {
        cout << "等级：优" << endl;
    }
    else if (score >= 80)
    {
        cout << "等级：良" << endl;
    }
    else if (score >= 70)
    {
        cout << "等级：中" << endl;
    }
    else if (score >= 60)
    {
        cout << "等级：及格" << endl;
    }
    else
    {
        cout << "等级：不及格" << endl;
    }

    return 0;
}
