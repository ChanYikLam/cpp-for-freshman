// average3.cpp -- 读入三门课的成绩，算出总分与平均分
//
// 这是留白版：四处 TODO 等你补。它能编译，但读进来的值和输出都还不对。
// 任务说明与预期输出见同目录的 README.md，做完照着 自查清单.md 核一遍。

#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
    cout << "请输入三门课的成绩（用空格或回车分开）：";

    double score1 = 0.0;
    double score2 = 0.0;
    double score3 = 0.0;
    cin >> score1 >> score2 >> score3;

    // TODO 1：科目数只该有一个定义处——把它声明成一个 const 常量。
    // TODO 2：算出三个成绩的总分，存进一个 total。

    double total = 0.0;                  // TODO 2 补完之后这行就该被替换掉

    double average = total / 3;          // TODO 3：分母要跟着 TODO 1 那个常量走

    // TODO 4：读到非数字时，cin 会进入失败状态，后面所有读取都会失败，
    //         坏输入还赖在输入队列里。在这里加一段「复位 + 丢掉坏输入 + 重新读」。
    //         提示：cin.clear() 与 cin.ignore(1000, '\n')。

    cout << fixed << setprecision(1);
    cout << "总分：" << total << endl;
    cout << "平均分：" << average << endl;

    return 0;
}
