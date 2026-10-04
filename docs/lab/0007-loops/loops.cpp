// loops.cpp -- 读入一批成绩并累加出总分
//
// 这是留白版：两处 TODO 等你补。它能编译，但总分永远是 0。
// 任务说明与预期输出见同目录的 README.md。

#include <iostream>
using namespace std;

int main()
{
    int n = 0;
    cout << "请输入成绩个数：";
    cin >> n;

    double sum = 0.0;

    // TODO 1：这个循环写死了 5 轮，而且读进来就扔了、没加进 sum。
    //         改成「跑 n 轮」，每一轮读一个成绩并加进 sum。

    for (int i = 1; i <= 5; i++)
    {
        double score = 0.0;
        cin >> score;
    }

    // TODO 2：这里打印的是原样的 sum，补完 TODO 1 之后数字就该对上了。

    cout << "共 " << n << " 个成绩，总分 " << sum << endl;
    return 0;
}
