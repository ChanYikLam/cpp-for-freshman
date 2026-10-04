// broken-intro-02.cpp -- 反例：忘了写 #include <iostream>
// 只该产生一个错误：cout 与 endl 都找不到
int main()
{
    cout << "Hello" << endl;
    return 0;
}
