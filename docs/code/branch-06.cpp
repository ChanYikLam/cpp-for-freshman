#include <iostream>

using namespace std;
int main()
{
    char grade = 'B';

    switch (grade)
    {
    case 'A':
        cout << "优秀" << endl;
        break;
    case 'B':
        cout << "良好" << endl;
        break;
    case 'C':
        cout << "及格" << endl;
        break;
    default:
        cout << "不及格" << endl;
        break;
    }

    return 0;
}
