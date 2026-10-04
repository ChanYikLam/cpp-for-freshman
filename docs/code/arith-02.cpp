#include <iostream>

using namespace std;
int main()
{
    int score = 89;

    cout << boolalpha;
    cout << "score < 60 -> " << (score < 60) << endl;
    cout << "score >= 60 -> " << (score >= 60) << endl;
    cout << "score >= 60 && score < 90 -> " << (score >= 60 && score < 90) << endl;

    return 0;
}
