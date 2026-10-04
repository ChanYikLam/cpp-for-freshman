# C++ Primer Plus（第 6 版）中文版 · 第 7 章 函数——C++的编程模块

> 抽取方式：页面图像 → tesseract 5.5.2 `-l chi_sim+eng --psm 3`，450 dpi。
> PDF 页范围 220–270（书页 202–252）。
> 这是**重抽稿**，用于替代原 PDF 文本层里质量很差的第 4/7 章；引用前仍以 PDF 原页图像为准。

---

### 第 202 页（PDF p220）

第7了章 ”函数一 C++的编程模块

本章内容包括:

@ ”函数基本知识。

@ HAE BASH,

蚊“设计处理数组的函数。
e@ “使用 const 指针参数二    -=一志
图”设计处理文本字符串的函数-

@ ”设计处理结枸的函数。
人
@ 调用 自 身的函数 Lae de

o FEAL E TE H.

了 Slee FRR AMIR; -读者将在 rues ent Fs ema SIE te ANSI fee

人 但真正的编程乐趣在于编写自己的范数; 区=-方面;要提高编种效率 可更深入地学习STEE
AEBOOST C++提供的功能。 本章和第 8 章介绍如何定义函数 给邓闪传递信息以及从函数那里获得信息。 木章 “，

ee ee 最后介绍递归和函数指 -

，如果读者熟悉 CH, ARATE AIRE. ITT: 人 -产生错误认识。 itis —*

as 提供原型， 1
里”调用函数-

aon CHEE C 语言 I 的基础 E新增了- Saas 这将在第8章 介绍。     + ERE 基础知识上
|   8k)   下介细过的有关国数的知识  人用 Co,  DRS FT ifs     sieges greatest o, « meemeye: HM ce I

“库 RE OA de ri RE INR: 二 Poti eee ee  aes wir aia

ry oe  A PATTER AL ZU OM  “Bilt 标准 CEPR strlen( ) pA Me, 可用来确定字

_符趾的长度。相关的标准闫文件 cstring 包含了 strlen()和其他- BEET IR. JERR ie we

ze 作使程序员能够在程序中随意使用 stlen( pa.

时， UAE HAR 3 ii   HEM “提供原型和调时， rg TBE

beer RMA categ OPP a. Ob ee Pai ee TE RL ae 1
f/ calling.cpp -   - defining,  ‘prototyping,  and calling a. function :    ey         :
和 Hinctude.. <iostream>.    eG      =   ee      和 ARNE Be

### 第 203 页（PDF p221）

void simple ();    // €unetion prototype

int main()
using namespace std;
cout << "main{) will call the simple() function:\n";

simple () ;     /f f£unetion call

cout << "main() is finished with the simple() function, \n";
// cin.get();
return 0;


//f €unetion definition
void simple |)


using Namespace std;
cout << "I'm but a simple function. \n";


main() will call the simple{) function:

I'm but a simple function,
main{) is finished with the simple() function.

HUT PAL simpleO时，将暂停执行 main( )中的代码; ee simple0执行完毕后，继续执行 main0中的
代码。在每个函数定义中，都使用了一条 using 编译指令，因为每个函数都使用了 cout。另一种方法是，
在国数定义之前放置一条 using 编译指令或在函数中使用 std::cout.

下面详细介绍这 3 个步骤。
7.1.1 定兴函数

可以将图数分成两类: 没有返回值的函数和有返回值的函数。没有返回值的函数被称为 void 函数，其
通用格式如下:
void functionName|parameterList)


statement fs)
return;          // optional

其中，parameterList 指定了传递给函数的参数类型和数量，本章后面将更详细地介绍该列表。可选的
返回语句标记了函数的结尾; 否则, 函数将在右花括号处结束。void 函数相当于 Pascal 中的过程.FORTRAN
中的子程序和现代 BASIC 中的子程序过程。 通常，可以用 void 函数来执行某种操作。例如，将 Cheers!打
印指定次数 n) 的函数如下:

void cheers(int n)}           // no return value


std::cout << "Cheers! ";
std::cout << std::endl;
参数列表 int n 意味着调用函数 cheers( )时，应将一个 int 值作为参数传递给它。
有返回值的函数将生成一个值, 并将它返回给调用函数。换句话来说, 如果函数返回 9.0 的平方根 (sqrt
(9.0))，则该函数调用的值为 3.0。这种函数的类型被声明为返回值的类型，其通用格式如下:

### 第 204 页（PDF p222）

typeName functionName(parameterList)


statements
return value;   // walue is type cast to type typeName


对于有返回值的函数，必须使用返回语句，以便将值返回给调用函数。值本身可以是常量、变量，也
可以是表达式，只是其结果的类型必须为 typeName 类型或可以被转换为 typeName《例如，如果声明的返
回类型为 double，而函数返回一个 int 表达式，则该 int 值将被强制转换为 double 类型)。然后，函数将最
终的值返回给调用函数。C++对于返回值的类型有一定的限制: 不能是数组, 但可以是其他任何类型一一整
数、浮点数、指针，甚至可以是结构和对象! CIE, BR C++函数不能直接返回数组，但可以将数
组作为结构或对象组成部分来返回。)

作为一名程序员，并不需要知道函数是如何返回值的，但是对这个问题有所了解将有助于澄清概念。(男
外，还有助于与朋友和家人交换意见。) 通常，函数通过将返回值复制到指定的 CPU 寄存器或内存单元中来
将其返回。随后，调用程序将查看该内存单元。返回函数和调用函数必须就该内存单元中存储的数据的类型
达成一致。函数原型将返回值类型告知调用程序，而函数定义命令被调用函数应返回什么类型的数据〈参见
图 7.1)。在原型中提供与定义中相同的信息似乎有些多余，但这样做确实有道理。要让信差从办公室的办全
桌上取走一些物品，则向信差和办公室中的同事交代自己的意图，将提高信差顺利完成这项工作的概率。

double cubetdouble x); 1 function prototype

int main()
double q = cube(1.2}; // function eal] ———

double cube(double x) // function ¢

H— returns" * Hy

| cubeO计算返回值
“| 将它冒于此处-函数
“本 头告诉cube()要使用

 = ae    7 :

图7.1 典型的返回值机制

函数在执行返回语句后结束。如果函数包含多条返回语句〔例如，它们位于不同的证else 选项中)，则
函数在执行遇到的第一条返回语句后结束。例如，在下面的例子中，else 并不是必需的，但可帮助马虎的
读者理解程序员的意图:

int bigger({int a, int b)

if (a> b)
return a; // if a > b, function terminates here
else
return b; // otherwise, function terminates here

如果函数包含多条返回语句，通常认为它会令人迷惑，有些编译器将针对这一点发出警告。然而，这
里的代码很简单，很容易理解。

### 第 205 页（PDF p223）

第7章 函数一一C++的编程模块


有返回值的函数与 Pascal. FORTRAN # BASIC 中的函数相似，它们同调用程序返回一个值，然后调
用程序可以将其赋给变量、显示或将其用于别的用途. 下面是一个简单的例子, 函数返回 double 值的立方;

double cube({double x)    // x times x times x


return x * x * x; // a type double value


例如，函数调用 cube(1, 2)4HR1] 1.728。请注意，上述返回语句使用了一个表达式，函数将计算该表

达式的值 (这里为 1.728)，并将其返回。
7.1.2 函数原型和函数调用

至此，读者已熟悉了函数调用，但对函数原型可能不太熟悉，因为它经常隐藏在 include 文件中。 程序

清单 7.2 在一个程序中使用了函数 cheer( )和 cubel )。请留意其中的函数原型

程序清单 7.2 protos.cpp

// protos.cpp -- using prototypes and function calls
#include <iostream>

void cheers (int);       // prototype: no return value
double cube(double x); // prototype: returns a double
int main()


using namespace std;

cheers (5);          // £unction call

cout << "Give me a number: ";

double side;


double volume = cube(side} ;    // funetion call

cout << "A" << side <<"-foot cube has a volume of ";
cout << volume << " cubic feet.\n";

cheers (cube(2));    // prototype protection at work
return 0;


void cheers(int n)

using namespace std;
cout << "Cheers! ";
cout << endl;


double cube(double x)


return x * = * =;

在程序清单 7.2 的程序中，只需要使用名称空间 std 中成员的函数中使用了编译指令 using。下面是该

程序的运行情况，
Cheers! Cheers! Cheers! Cheers! Cheers!
Give me a mumber: 5
A 5-foot cube has a volume of 125 cubic feet.
Cheers! Cheers! Cheers! Cheers! Cheers! Cheers! Cheers! Cheers!

### 第 206 页（PDF p224）

main( )使用函数名和参数〈后面跟一个分号) 来调用 void 类型的函数: cheers (5);，这是一个函数调
用语句。但由于 cube( )有返回值，因此 main( )可以将其用在赋值语句中:

double volume = cube(side);

但正如前面指出的，读者应将重点放在原型上。那么，应了解有关原型的哪些内容呢? 首先，需要知
道 C++要求提供原型的原因。其次，由于 C++要求提供原型，因此还应知道正确的语法。最后，应当感谢
原型所做的一切。 下面依次介绍这几点，将程序清单 7.2 作为讨论的基础。

1为什笃需要原型

原型描述了函数到编译器的接口，也就是说，它将函数返回值的类型〈(如果有的话) 以及参数的类型
和数量告诉编译器。例如，请看原型将如何影响程序清单 7.2 中下述函数调用:

double volume = cube(side} :;

首先，厚型告诉编译器，cube( )有一个 double 参数。如果程序设有提供这样的参数，原型将让编译器
能够捕获这种错误。其次，cube( )函数完成计算后, AEE I AE ae i    可能是 CPU 2 47-45.
也可能是内存中。然后调用函数【这里为 main( )) 将从这个位置取得返回值。由于原型指出了 cube( )的类
型为 double，因此编译器知道应检索多少个字节以及如何解释它们。如果疫有这些信息，编译器将只能进
行狂测，而编译器是不会这样恢的。

读者可能还会问，为何编译器需要原型，难道它就不能在文件中进一步查找，以了解函数是如何定义
的吗? 这种方法的一个问题是效率不高。编译器在搜索文件的剩余部分时将必须停止对 main( )的编译。一
个更严重的问题是，函数甚至可能并不在文件中。C++允许将一个程序放在多个文件中，单独编译这些文
件，然后再将它们组侣起来。 在这种情况下，编译器在编译 main( I, AYRE ICAU fel PARAS. WR ee
位于库中，情况也将如此。避免使用函数原型的唯一方法是，在首次使用函数之前定义它，但这并不总是
可行的。另外，C++的编程风格是将 main( )放在最前面，因为它通常提供了程序的整体结构。

2，原型的语法
并添加分号。对于 cube( )，程序清单 7.2 中的程序正是这样做的:

double cube{double =); // add ; to header to get prototype

然而，函数原型不要求提供变量各，有类型列表就足够了。对于 cheer )的原型，该程序只提供了参数
类型:

void cheers(int); // okay to drop variable names in prototype

通常，在原型的参数列表中，可以包括变量名，也可以不包括。原型中的变量名相当于占位符，因此
不必与函数定义中的变量名相同。

C++原型与 ANSI 原型

ANSIC HET C++中的原型，但这两种语言还是有区别的。其中最重要的区别是，为与基本 C 菲容，
ANSIC 中的原型是可选的，但在 C++中，原型是必不可少的。 例如，请看下面的函数声明:

void say hi{);

ECHYP, TASH AGS PRMARFT void 是等效的一 意味着函数没有和参数。在 ANSIC 中，
括号为空意味着不指出参数一一这意味着将在后面定勾和囊列表。在 C++中，不指定参数列表时应使用省

void say_bye(...);   // C++ abdication of responsibility

通常，仅当与接受可变参数的C 函数(如 printft ) ) 交互时才需要这样做。

3，原型的荔能
正如您看到的，原型可以帮助编译器完成许多工作; 但它对程序员有什么帮助昵? 它们可以极大地降

### 第 207 页（PDF p225）

第7章 函装一一C++的绢程模块              207

低程序出错的几率。具体来说，原型确保以下几点:

@ 编译器正确处理函数返回值;

e 网译器检查使用的参数数目是否正确;

© 编译器检查使用的参数类型是否正确。如果不正确，则转换为正确的类型“如果可能的话)

前面已经讨论了如何正确处理返回值。下面来看一看参数数目不对时将发生的情况。例如，假设进行
了如下调用:

double z = cube();

WRIA PAR, Bee CIP Ei. “SPR AHI, “ERE ERE cube( )调用存放值的位置，并
使用这里的值。这正是ANSIC 从C++借鉴原型之前，C 语言的工作方式。由于对于 ANSIC ili, bat
可选的，因此有些C 语言程序正是这样工作的。但在 C++中，原型不是可选的，因此可以确保和不会发生这
类错误。

EPR. HRT TSR, HARRIE. CHAT, DHMH. Hin, WR
数需要一个 int 值 5假设占 16 位)，而程序员传递了一个 double 值〈《假设占 64 位)，则函数将只检查 64 位
中的前 16 位，并试图将它们解释为一个 int 值。但 C++目动将传递的值转换为原型中指定的类型，条件是
两者都是算术类型。例如，程序清单 7.2 将能驶应付下述语句中两次出现的类型不匹配的情况，

cheers (cube(2));

首先，程序将 int 的值 2 传递给 eube( )，而后者期望的是 double 类型。编译器注意到，cubet )原型指
定了一个 double 类型参数,因此将 2 转换为 2.0一一一个double 值.接下来,cube( )返回一个 double {/i( 8.0),
这个值被用作 cheer( )的参数。编译器将再一次检查原型，并发现 cheerl( )要求一个 int 参数，因此它将返回
值转换为整数8。通常，原型自动将被传递的参数强制转换为期望的类型.(但第 8 章将介绍的函数重载可
能导致二义性，因此不允许某些自动强制类型转换。)

月动类型转换并不能避免所有可能的错误。例如，如果将 8.33E27 传递给期望一个int 值的函数，则这
样大的值将不能被正确转换为 int 值。当较大的类型被自动转换为较小的类型时，有些编译器将发出警告，
指出这可能会竺失数据。

仅当有意义时，原型化才会导致类型转换。例如，原型不会将整数转换为结构或指针。

在编译阶段进行的原型化被称为静态类型检查〈static type checking)。可以看出,静态类型检查可捕获
许多在运行阶段非常难以捕获的错误。

7.2 GRAB FRIAR

下面详细介绍一下函数参数。C++通常按值传递参数，这意味着将数值参数传递给函数，而后者将其
赋给一个新的变量。例如，程序清单 7.2 包含下面的函数调用，

double volume = cube(side);

其中，side 是一个变量，在前面的程序运行中，其值为 $。cube( )的函数头如下:

double cube(double x)

被调用时，该函数将创建一个新的名为 x WY double Bit, JPME 5. KEE, cube( )执行的操
作将不会影响 main( )中的数据，因为 cube( )使用的是 side 的副本，而不是原来的数据。稍后将介绍一个实
现这种保护的例子。用于接收传递值的变量被称为形参。传递给函数的值被称为实参。出于简化的目的，
C++标准使用参数 (argument) 来表示实参，使用参量 (parameter) 来表示形参，因此参数传递将参量赋
给参数【参见图 7.2)。

在函数中声明的变量(包括参数) 是该函数私有的。在函数被调用时，计算机将为这些变量分配内存，
在函数结束时,计算机将释放这些变量使用的内存 (有些 C++文献将分配和有释放内存称为创建和毁坏变量，
这样似乎更激动人心)。这样的变量被称为局部变量，因为它们被限制在函数中。 前面提到过,这样做有助

### 第 208 页（PDF p226）

ores Ps “( 4 oi. ria


ie    手 i tet. 这还意味着， “Wade ain PET = Ra x HSE :博时在另二个高数中也声

aoe  Th AR WES ALDH EAS EAE AS TA). EE SFA IEE, 1S Fe NTA Albany 与纽     2

YEG Albany 是两个完全不同的地方是: 样的道理《参见图7.3)。 -这样的变量也被称为自动变最， tame ai =


double side = 5;

fz            double cube(double x)

void .cheers{ int ny;
int main{)

int n= 20;
int i= 1000;
are y= ay
cheers (yh

void cheers{int n})

|             ee ae
for (int i= 0; i <n; ite}
cout += "Cheers!"
scout: << "hn";

### 第 209 页（PDF p227）

第7章 ”函数一一C++的编程模块              209

n_chars('R', 25);

上述函数调用将两个参数传递给函数 n_chars( )，我们将稍后定义该函数。

同样，在定义函数时，也在函数头中使用由逗号分隔的参数声明列表:

void n_chars(char c, int n) // two arguments

PBL, BMC n char )接受一个 char 参数和一个 int 参数。传递给函数的值被赋给参数c Al n.
如果函数的两个参数的类型相同，则必须分别指定每个参数的类型，而不能像声明常规变量那样，将声明
组侣在一起:

void f£ifi(float a, float b) // declare each variable separately

void fufu(float a, b)        // NOT acceptable

和其他函数一样，只需添加分号就可以得到该函数的原型，

void n_chars(char c, int n); // prototype, style 1

和一个参数的情况一样，原型中的变量名不必与定义中的变量名相同，而且可以省略:

void n_chars(char, int);     // prototype, style 2
然而，提供变量名将使原型更容易理解，尤其是两个参数的类型相同时。这样，变量名可以提醒参量
和参数间的对应关系，

double melcn aqernsityiadouble weight, double volume) ;
程序清单 7.3 演示了一个接受两个参数的函数，它还表明，在函数中修改形参的值不会影响调用程序
中的数据。

程序清单 7.3 twoarg.cpp

// twoarg.cpp -- a function with 2 arguments
#include <iostream>

using namespace std;

void n_chars(char, int);

int main()

int times;
char ch;

cout << "Enter a character: "
cout << "Enter an integer: ";
cin >> times;
n_chars(ch, times); // function with two arguments
cout << "\nEnter another character or press the"
" q-key to quit: ";
cout << "The value of times is " << times << ".\n";
cout << "Bye\n";
return 0;


void n_chars(char c, int n) // displays c n times

while ({n-- > 0)         // continue until n reaches 0

### 第 210 页（PDF p228）

he Boasts an “integer:.  “50-:  ae

ee = 122 BR 个接受两个参数的生数 ea 三 ae a5 ee ae


2前; .美国许多州都采用某种纸幅游戏的形式来改行彩票 Tee = a
 phi Bk St A EF PSI 6 CBRL RE A EL I 6 OC MRE FARROW DR 6 NI

os SHAT, AALS PR BAR RE ILE CEN Lee AMR SO


7  Ree 73 WEE, SIE wing deme LT Rei. Fane |
Ce ee ee ee

oe | Enter a- ‘gharacter:  We,    : on ere ee = = ee =e pee = a   ee — as

= a ee :  es ae
Si ee ea Ce 它
使用cin>>eh,， Re oa Gn) ch = cing RMI EY A AR IL ATE at

fuer WAL NIDA SE Eni LSSAnes eer yeaa ;


Spans = sae aK HERE ear it ne BRO  RR MSO

一

sens Mee uaa te EMEA AERA RWH) oe

=o     5X4x3x2X   fe hes a

= i: seit AI “whibise 个数中选取 picks 4%  ey

3   oe. Long double, result =   LO;            Johcbisnge! vie east      eee ee       Se ee
-. 5.) = for, fh = numbers. p - “picks; Boe On Bes Pos) oe SE tee ae ee
、   ae c=  ‘Kesult. = result * n /: os:  pare   Co os Tere ae ee ee    ae
=      _策环不证首先将所有的分子项相洪，而是首范将【0 与第二不分了项相生 RRR hae. 二
然后下-  -轮循环乘以第二  -个分子项-并除以第二  -个分母项: 这样得到的乘积将比先进行乘法运算得到的小:  Ss=e  =
pte,  对于(10 *9)/(2 * 和(107 2)*(9 上， 前者将计算 90/2, 得到 45i::后者将计算为.5*9; -得到.45。 这两一
 二但前者的中 间值 (90) 大于后 痢=  RTRs 一中间值的差别就越大。  _当数字非常一

### 第 211 页（PDF p229）

第7章 函数一一C++的编程模块                               211

大时，这种交替进行乘除运算的策略可以防止中间结果超出最大的译点数。

程序清单 7.4 在 probability( )函数中使用了这个公式。由于选择的数目和总数目都为正，因此该程
序将这些变量声明为 unsigned .int 类型〔(简称 unsigned)。将若干整数相乘可以得到相当大的结果，因
此 lotto.cpp 将该函数的返回值声明为 Iong double 类型。另外，如果使用整型，则像 49/6 这样的运算
将出现舍入误差。

SER: 有些 C++实现不支持 long double 类型 ，如果所用的 C++实现是这样的，请使用 double 类型。
程序清单 7.4 lotto.cpp

// lotto.epp -- probability of winning

#include <iostream>

// Note: some implementations require double instead of long double
long double probability(unsigned numbers, unsigned picks);

int main({)


using namespace std;
double total, choices;
cout << "Enter the total number of choices on the game card and\n"
"the number of picks allowed:\n";
while ((cin >> total »=> choices) && choices <= total)
cout << "You have one chance in ";
cout << probability([total, choices) ;      // compute the odds
cout << " of winning.\n";
cout << "Next two numbers (q to quit): ";
cout << "bye\n";
return 0;


// the following function calculates the probability of picking picks
// tumbers correctly from numbers choices
long double probability(unsigned numbers, unsigned picks)
long double result = 1.0; // here come some local variables
long double n;
unsigned p;

for (n = numbers, p = picks; p >» 0; n--, p--)
result = result * n/p ;
return result;

下面是该程序的运行情况;

Enter the total number of choices on the game card and
the number of picks allowed:

49 6

You have one chance in 1.39838e+007 of winning.

Next two numbers (q to quit): 51 6

You have one chance in 1.80095e+007 of winning.

Next two numbers {q to quit): 38 6

You have one chance in 2.76068e+006 of winning.

Next two numbers (q to quit): q

bye

### 第 212 页（PDF p230）

请注意，增加游戏卡中可供选择的数字数目，获奖的可能性将急剧降低，

程序说明

程序清单 7.4 中的 probability( )函数演示了可以在函数中使用的两种局部变量。首先是形参 (number
和 picks)，这是在左括号前面的函数头中声明的;其次是其他局部变量 (result、na Alp), 它们是在将函数
定义插起的括号内声明的。形参与其他局部变量的主要区别是，形参从调用 probability( )的函数那里获得
自己的值，而其他变量是从函数中获得自己的值。

7.3 画数和数组

到目前为正，本书的函数示例都很简单，参数和返回值的类型都是基本类型。但是，函数是处理更复
厅的类型【如数组和续构) 的关键。下面来如何将数组和冰数绪全在一起。

假设使用一个数组来记录家庭野餐中每人吃了多少个研饼〈每个数组索引都对应一个人，无素值对应
于这个人所吃的甜饼数量)。 现在想知道总数。这很容易，只需使用循环将所有数组元素累积起来即可。将
数组元素累加是一项非常营见的任务，因此设计一个完成这项工作的函数很有意义。这样就不必在每次计
算数组总和时者编写新的循环了，

考虑函数接口所涉及的内容。由于函数计算总数，因此应返回答案。如果不分吃甜饼，则可以让函数
的返回类型为 nt。另外，函数需要知道要对哪个数组进行累计，因此需要将数组名作为参数传递给它。为
使二数通用，而不限于特定长度的数组，还需要传递数组长度。这里唯一的新内容是，需要将一个形参声
明为数组名。下面来看一看函数头及其其他部分:

int sum arr(int arr[], int n) // arr = array name, n= size

这看起来似乎合理。方括号指出 arr 是一个数组，而方括号为空则表明，可以将任何长度的数组传递
给该函数。但实际情况并非如此，arr 实际上并不是数组，而是一个指针! 好消息是，在编写函数的其余部
分时，可以将 arr 看作是数组。首先，通过一个示例验证这种方法可行，然后看看它为什么可行。

程序清单 7.5 演示如同使用数组名那样使用指针的情况.程序将数组初始化为某些值,并使用sum_arr( )
上因数计算总数。注意到 sum_arr( PARE arr 时，束像是使用数组名一样。

程序清单 7.5 arrfun1.cpp

// arrfunl.cpp -- functions with an array argument
#include <iostream>
const int ArSize = 日
int sum_arr(int arr[], int n);        // prototype

using Namespace std;

int cookies (ArSize] = {1,2,4,8,16,32,64,128};
// some systems require preceding int with static to
/f enable array initialization

int sum = sum_arr(cookies, ArSize) ;
eout << "Total cookies eaten: " << sum << "\n";

Feturn Oy;

// veturn the sum of an integer array
int sum arr{int arr[], int n)


int total = 0;

### 第 213 页（PDF p231）

total = total + arr[il;
return total;


Total ceokies eaten: 255
从中可知，该程序管用。下面讨论为何该程序管用。
7.3.1 范数如何使用指针来处理数组

在大多数情况下，C++和 C 语言一样，也将数组名视为指针。第 4 章介绍过，C++将数组名解释为其
第一个元素的地址;

cookies == &cookies[0] // array name is address of first element

该规则有一些例外。首先，数组声明使用数组名来标记存储位置，其次，对数组名使用 sizeof 将得到
整个数组的长度〈以字节为单位); 第三，正如第 4 章指出的，将地址运算符信用于数组名时，将返回整个
数组的地址，例如&&cookies 将返回一个 32 字节内存块的地址《如果 int 长 4 字节)。

程序清单 7.5 执行下面的函数调用

int sum = sum_arr(cookies, ArSize)j;

He, cookies 是数组名，而根据 C++ ALM, cookies AHA —P ICR HHHE, Pte Bere A EME
由于数组的元素的类型为 nt，因此 cookies 的类型必须是 int 指针，即 int* 。这表明，正确的函数法应该是

int sum_arr(int * arr, int n) // arr = array name, m = size

其中用 int * arr HR S intarr[]. 这证明这两个函数头都是正确的，因为在 C++中，当【且仅当)
用于函数头或函数原型中，int *arr Al int arr []的含义才是相同的。它们都意味着 arr 是一个 int 指针。
然而，数组表示法 Cint arr[ ]) 提醒用户，arr 不仅指向 int，还指向 int 数组的第一个 int。当指针指向
数组的第一个元素时，本书使用数组表示法，而当指针指向一个独立的值时，使用指针表示法。别二
了，在其他的上下文中，int* arr 和 int ar []的含义并不相同。例如，不能在函数体中使用 int tip[ PK
声明指针 。

鉴于变量 arr 实际上就是一个指针，函数的其余部分是合理的。第 4 章在介绍动态数组时指出过，
同数组名或指针一样，也可以用方插号数组表示法来访问数组元素。无论 arr 是指针还是数组名，玫
达式 arr [3]都指的是数组的第 4个元素。就目前而言，提请读者记住下面两个恒等式，将不会有任何
坏处:

arr[i] == *(ar + i)    // values in two notations

&arr[i] == ar + i      // addresses in two notations

记住，将指针【包括数组名) 加 1，实际上是加上了一个与指针指向的娄型的长度【以字节为单位)
相等的值。对于唤历数组而言，使用指针加法和数组下标时等效的。

7.3.2 将数组作为参数意味着什么

我们来看一看程序清单 7.5 暗示了什么。函数调用 sum_arrfcoolies，ArSize)将 cookies 数组第一个元素
的地址和数组中的元素数目传递给 sum_arr( )函数。sum_arr( PR BCH cookies 的地址赋给指针变量 arr，将
ArSize 赋给 int 变量nm。这意味着，程序清单 7.5 实际上并没有将数组内容传递给函数，而是将数组的位置
(Hott). GAM CHA (RN) 以及元素数目 人n 变量) 提交给函数〈参见图 7.4)。有了这些信息后，
函数便可以使用原来的数组。传递常规变量时，函数将使用该变量的拷贝，但传递数组时，函数将使用原
来的数组。实际上，这种区别并不违反 C++按值传递的方法，sum_arr( )函数仍传递了一个值，这个值被赋
给一个新变量，但这个值是一个地址，而不是数组的内容。

### 第 214 页（PDF p232）

ae a ee ot

-一   - - 图7.4 告知函数有关数给的信息

数组名与指针对应是好事吗? 确实是一件好事: 将数组拒址作为参数可以节省复制整个数组所需的蛙:
间和内存。如果数组很大，则使用排贝的系统开销将非常大,程序不仅需要更多的计算机内在，还需要花
费时间来复制天块的数据。另一方面，使用原始数据增加了破坏数据的风险 在经典的C语言中，这确实
是一个问题*但 ANSIC 和C++中的const-限定符提供子解决这种问题的办法, 稍后将介绍一企这样的示例，
但先来修改程序清单 7.5，以演示数组函数是如何运作的: 程序清单7.6 AAG. cookies 和Earr的值相同。它-

还演示了指针概念如何使 sum_arr 函数比以前更通腓。 该程序使用限定逢std::而不是编译指令 using 来提供-


// arrfun2.cpp -- fiinctions with an array argument
#include <iostream>

coneat—int ArSize = 8;

int. sum_arr(int.arr[], int n);
//-use std:: instead of using directive                 ;

int cookies [ArSize] =—{h-274,6,16,32,64,128};
// some systems require preceding int with static to
// enable array initiaFization

std::cout << cookies << " = array address; ";
// some systems require a type cast: unsigned (cookies)

stdrscout << sizeof cookies << " = sizeof cookies\n";
int sum = sum-arr{cookies, ArSize);          :
std::cout << "Total cookies eaten: " << sum-<< std::endl;

Bum = sum_arr(cookies, 3);        // a lie
std::cout << “First three eaters.ate "<< sum <<" cookies. \n";
sum = sumiarr(cookies + 4,'4); __// another lie

std::cout << "Last four eaters ate " << sum=<< " cookies. \n";— -<--—

### 第 215 页（PDF p233）

61% GH CHAMBER         ee

/*. return the sum of an-integer array. .
_ int sum_arr(int arrf], int ne       :
int. totaF= 0;°      ,
= peti. cry, Stdircout << arr <e "= arr, "7

 /7 SDme . _eygtems require EYRE cast:  - unsigned hae


for “(lint i Pas Oj i Sg i++)  i  加  Ailey     a ee       fT  Lee net

s     和
二 return total;   TE an fh eR ESAT aereemacres wean ee Sait = ciety ete) See Slletan pein     see
foie es Si aes TE eee  eg
Saas  oe   003EF9FCG : =, atray “Baareas  33 = = 时 cookies = su see = ae fee =   seh  Sie   isin oe
03BF9FCG = arr, 4 = ‘sizeof, i eee ae a BS gto Gao Seatei Ne ACN IR TSS pane ar eee
”TotaE cookies eaten:  255     aa :    =   a. yee Be eR       ae   本
See ae “OO3EFSFC : 三 Sarr,  Aes. sizeof “arr a 一 RE   a eas ie Ee ents es ee ee
ty ee  - First. three eaters ate 7 cookies.  samen nes 2   . -: JE Soe rie - Ree e       省

 03EFROC = arr, 4s “sizeof arr - ae: 5     Bourse

face — ae Last-four’ eaters ‘ate 346 ‘cookies. -  cE Se SO Ma eer Ae aN ate ae ee

“HER LHL ERO KERR SETTIE TH ‘tec ear MoMA,

:     HAMEL FR Ss,  Ait EHH Ons     (aaa ie ene
ge EI MRM TO ee ie ee ee ee

oe    ~ BFP 716 WO F MEER BL — PALA NOTE YH 4Es cookies A art 8 FHP aot eokies 二，
1    的值为 32， 而:sizeof arr 为:4.-这是由于-sizeof cookies:是整个数组的长度--而 sizeof am 只是指针变量的长-=.
Oe Cem aR -个使用生字节地址的系统中获得的= 顺便说=名， EO SO   ae
© ERA im. ita :指针本身并没有指出数组的长度二-二3    ae
LAS AFP summa) 2 eal La Ne RRL Fi RM ATO “RO

eee oe RATE

| age -一-um sum aricookiee7 aie  se ane oe < ae ae = 二 es
ae ee ee   Dee EE Ree
Bt 5 free: = ‘sum: rare (cogkies. +4,  ay; a a purer ce  a ri ead                     hast

Peet  由于 cookies 是第一 一个元素的地赴，因此 cookies «410% 5 个元素的地址， -这条语各将计关数组第5、
7个元素的总和。 “请注意输出中第三次函数调用选择将不同于前两个调用的地址贼给 ae 的 是的，
ore        “可以将各cookies[4]，  -而不是 cookies士4 作为参数:   :它们的含义是相同 同的。  ae oe ae   os Sy ee a

oS eae AERA AA fo ME SH MOAT qatmexnwsnauaco ~~
rie Ses void... fillarray(int at个， int: Bize}; —/ ih: prototype. Teed Se aes eee  pee ae aa a
ne ee eee
Pen ee pe er Cnk 2 arr isize) })          off: HOT- bad prototyoe: sd Be


PEMA Ob RELL BIE RMERR,. MENEMRICL DEANE RATAN.    :
an 这里讲的好处指的是程序的可靠性更高、修改和调试更为方便)。 另外, 构思程序时将存储属性与操作结

a= fee 便是前 GOP Raa T aE. 羽后交这明这是很有好处的*   oo es eS:

### 第 216 页（PDF p234）

来看一个简单的案例。假设要使用一个数组来记录房地产的价值《假设拥有房地产)。在这种情况下，
程序员必须确定要使用哪种类型。当然，double 的取值范围比 int 和 long 大，并且提供了足够多的有将位
数来精确地表示这些值。接下来必须决定数组元素的数目。(对于使用 new 创建的动态数组来说，可以稍
后再决定，但我们希望使事情简单一点)。如果房地产数目不超过 5 个，则可以使用一个包含 5 个元素的
double 数组。

现在,考虑要对房地产数组执行的操作。郴个基本的操作分别是，将值读入到数组中和显示数组内容，
我们再添加另一个操作: 重新评估每种房地产的值。为简单起见，假设所有房地产都以相同的比率增加或
者减少。(别忘了，这是一本关于 C++的书，而不是关于房地产管理的书。) 接下来，为每项操作编写一个
函数，然后编写相应的代码。下面首先介绍这些步骤，然后将其用于一个完整的示例中

1，填充数组

由寺接受数组名参数的函数访问的是原始数组，而不是其副本，因此可以通过调用该函数将值赋给
数组元素。该函数的一个参数是要填充的数组的名称. 通常，程序可以管理多个人的投资，因此需要
多个数组，因此不能在函数中设壮数组长度，而要将数组长度作为第二个参数传递，就像前一个示例那
样。另外，用户也可能希望在数组被十满之前停止读取数据，因此需要在函数中建立这种特性。由于
用户输入的元素数目可能少于数组的长度，因此函数应返回实际输入的匹素数目。因此，该函数的原
型如下:

int fill _array{double ar[], int limit) ;

PARES SR, NA, iE TI ACR; 该函数返回实际读取的元
素煞。例如，如果使用该函数来处理一个包售 5个元素的数组，则将 作为第二个参数。如果只输入3个
什，则该图数将返回 3。
可以使用循环连续地将值读入到数组中，但如何提早结束循环呢? 一种方法是，使用一个特殊值来指
出输入结束。由于所有的属性都不为负，因此可以使用负数来指出输入结束。另外，该函数应对错误输入
作出反应，如停止输入等。这样，该函数的代码如下所示;
int fill] array(double ar[], int limit}
using namespace std;
double temp;
inte:
if (lein)    {/ bad input
cin.clear();
while (ciniget[{) != '"\n'"}
continue;

cout << "Bad input; input process terminated. \n";
break;


else if (temp < 0)     // signal to terminate
break;

ar[i] = temp;


return i;

Hm, NSPHAa MHP Ma. MRAP MADER, Wk MERA a, BG
结束。 如果用户输入的都是有效值，则循环将在读取最大数目的值后结束。循环完成的最后一项工作是

### 第 217 页（PDF p235）

第7章 ”函数一一C++的编程模块              217

将i加 1，因此循环结束后，i 将比最后一个数组索引大 1，即等于填充的元素数目。然后，函数返回这
个值。

2，显示数组及用 ceonst 保护数组

创建显示数组内容的函数很简单。只需将数组名和填充的元素数目传递给函数，然后该函数使用循环
来显示每个元素，然而，还有另一个问题一一确保显示函数不修改原始数组。除非函数的目的就是修改传
递给它的数据，否则应避免发生这种情况。使用普通参数时，这种保护将自动实现，这是由于 C++按值传
递数据，而且函数使用数据的副本。然而，接受数组名的函数将使用原始数据，这正是 fill_array( )函数能
够完成其工作的原因。为防止函数无意中修改数组的内容, 可在声明形参时使用关键字 const(参见第 3 Bt):

vold show_array(const double ar[], int n);

该声明表明，指针 ar 指向的是常量数据。这意味着不能使用 ar 修改该数据，也就是说，可以使用像
ar[0]这样的值，但不能修改。注意，这并不是意味着原始数组必须是常量，而只是意味着不能在 show_array( )
函数中使用 ar 来修改这些数据。因此，show_array( )将数组视为只读数据。假设无意间在 show_array( )PA
数中执行了下面的操作，从而违反了这种限制

ar[0)] += 10;

编译器将禁止这样做。例如，Borland C++将给出一条错误消息，如下所示《〈稍作了编辑):

Cannot modify a const object in function
show _array(const double *, int)

其他编译器可能用其他措词表示其不满。
这条消息提醒用户，C++将声明 const double ar [ ]解释为 const double *ar。因此，该声明实际上是说，
ar 指癌的是一个常量值。结束这个例子后，我们将详细讨论这个问题。下面是 show_array( )函数的代码:

void show_array(const double ar[], int n)

using namespace std;


cout << ar[i] << endl;


3. 修改数组
在这个例子中，对数组进行的第三项操作是将每个元素与同一个重新评估因子相乘。需要给函数传递
3 个参数: 因子、数组和元素数目。该函数不需要返回值，因此其代码如下;

void revalue(double r, double ar[], int n)
for {int i = 0; i < my; i+4)

由于这个函数将修改数组的值，因此在声明 ar 时，不能使用 const.

4. HERE RGASR AR

至此，您根据数据的存储方式〈数组) Ak (3 个函数) 定义了数据的类型，因此可以将它
们组合成一个程序。 由于已经建立了所有的数组处理工具，因此 main( )的编程工作非常简单。该程序检
查用户输入的是否是数字，如果不是，则要求用户这样做。余下的大部分编程工作只是让 main( )调用前
面开发的函数。程序清单 7.7 列出了最终的代码，它将编译指令 using 放在那些需要 iostream 工具的函
数中。

### 第 218 页（PDF p236）

程序清单 7.7 arrfun3.cpp

// arrfun3.cpp -- array functions and const

#include <iostream>

const int Max = 5;

// Eunction prototypes

int £ill_array(double ar[], int limit);

void show_array(const double ar[], int n); // don't change data
void revalue(double r, double ar[], int nj);

int main()

using namespace std;
double properties [Max] ;

int size = fill_array(properties, Max) ;
show_array(properties, size);
if (size > 0D)
cout << "Enter revaluation factor: ";
double factor;
while (!(cin >> factor) )    // bad input
cin.,clear();
while {cin.get() != '\n")
continue;
cout << "Bad input; Please enter a number: ";
revaluel(factor, properties, size);
show _array(properties, size);
cout << "Done.\n";
cin.get();
cin.get();
return 0;

int fill_array(double ar[], int limit}

using namespace std;
double temp;
Bf i A
if (!cin)    // bad input
ein.clear();
while (cin.get(} != '\n"}

eontinue;
cout << "Bad input; input process terminated. \n";
break;

### 第 219 页（PDF p237）

第7章 BR CHHRERR


else if (temp < 0)     // signal to terminate
break;
ar[i] = temp;

return i;

// the following function can use, but not alter,
// the array whose address is ar
void show_array(const double ar[], int n)
using namespace std;
cout << ar[i] << endl:

/f multiplies each element of ar[] by r
vold revalue(double r, double ar[], int n)


下面两次运行该程序时的输出:
Enter value #1: 100000

Enter value #2: 80000

Enter value #3: 222000

Enter value #4: 240000

Enter value #5: 118000
Property #1: $100000
Property #2: $80000
Property #3: $222000
Property #4: $240000
Property #5: $118000

Enter revaluation factor: 0.8
Property #1: $8o000

Property #2: $64000
Property #3: $177600
Property #4: $192000
Property #5: $94400

Done.
Enter value #1: 200000

Enter value #2: 84000
Enter value #3: 160000
Enter value #4: -2
Property #1: $200000
Property #2: $84000
Property #3; $160000
Enter reevaluation factor: 1.20
Property #1: 5240000
Property #2: $100800
Property #3: 5192000
Done.

### 第 220 页（PDF p238）

ee eee   Cau. Pike FR C6 EC —

[S -MAL all aryOHh: MAPA SE te    将结来答入。 第二 -次运行演示了输入5项
房地产信的情况，第一次运行演示了输入殴值的情况:

5:   RPT

前面已经讨论了 与该示例相关的重要编程细节， 因此这里回顾-- AME. 我们首先考虑的是通过
数据类型和设计适当的函数来处理数据，然后将这些函数组合成一个程序。有时也称为自下面上的程序设 =
it 《bottom-up_programming)，因为设计过程从组件到整体进行。这种方法非常适合于 OOP一一它首先强
调的是数据表示和操纵。而传统的过程性编程倾向于从上而下的程序设计 《top-down programming)，首先
指定模块化设计方案，  然后再研究细节。  这两种方法都很有用，  最终的产品都是模块化程序。     四

6. Peverr Cray tere        =
假设要编写一 TEM double ACA FLINT: 如果该函数要修改数组， 其原型可能类似于下面这样

=        如果函数不修改数组，  -其原型可能类似于下面这样:-              -        =

- = 当然，在函数原型中可以省略变量名，  也可将返回类型指定为类型。  这里的要点是，ar 实际上是一个
_    指针，指向传入的数组的第一个元素; 另外，  二手通过参数传递了元素数， 这两个函数都可使用任何长度
-  的数组，只要数组的类型为 double:      ee   il  5  az
double faults [50] ; :
€ Gcatey meabeaa:! 1000) ;
oe   AME Ne CRURIMALL EAM BIR, EMG ADIN, mM Ok >— Hea Xe
Se 数组的知识; 例如，它不能使用 sizeof 来获悉原始数组的长度， 而必须依赖于程序员传入正确的元素数。

- 734 ”使用数组区间的函数    ss           _

-=正如您看到的，对于处理数组的:C++函数，必须将数组中的数据种类、 数组的起始位置和数组中元素
数量提交给它; 传统的 C/C++方法是，将指向数组起始处的指针作为一个参数， 将数组长度作为第二个参
数〈指针指出数组的位置和数据类型)，这样便给函数提供了找到所有数据所需的信息。

还有尺一种给函数提供所需信息的方法，即指定元素区间 〈range), .这可以通直传递两企指鲁来完成: 一
一个指针标识数组的开头,-另一个指针标识数组的尾部。例如， C++标准模板库 (SEL, HECER 16-章介绍)
将区间方法广义化了。STL 方法使用“超尾”概念来指定区间。世就是说，对于数组而言， 标识数组结尾
 的参数将是指向最后一个元素后面的指针。 例如， 假设存这样的声明


_ WARE elboud 和 elboud + 20 定义了区间。 首先，数组名 elboub 指向第一个元素。 FEAR elboud + 19
4   指向最后一个元素(即 elboud[19]), 因此，elboud + 20 指向数组结尾后面的一个位置。将区间传递给函数
将告诉函数应处理哪些元素。 程序清单 7.8 对程序清单 7.6 做了修改，使用两个指针来指定区问。                二

程序清单了8 arrfun4.cpp

// arrfun4.cpp --— functions with an array range
Hinclude <iostream>

const int ArSize = 日;

int sum arr(const int * begin, const int * end) ;
int main()


using namespace std;

### 第 221 页（PDF p239）

61 ee CEM a

— “int ‘cookies {ArSizel -   =, 2,4, 8, 16, 32; 64, yeh:      oe a Thi Se    Eve
f= some “systems “require preceding int: with static to eis sites ENO We ee ar

mS)  enable array initialization: *.-t. 22°: Til: 75 pe ye ae ee


cout <¢ "Total cookies eaten: "<e sum <<  endl ;
“sgumr= sum_arr(ecookies, cookies=+ 3+; ~    // first 3 elements
cout. << "First three eaters ate “ << Sums<< " cookies. \n";
_ gum = sum_arrtcookies + 4i2.cookiés-+ 8);     // last 4 eFements
Sout _s< “Last—four ez eaters ate | " < BUT < " cookies. An";     =      Teen tee

“// return the sum of- an integer array
int sum_arr(const int * begin, const int * end

const int * pt;
int total =-0;
pills return’ ‘total:  : =     seat       a MEANS ees    i ae
Pa ae a :          =

Total cookies eater: 255
First three eaters ate 7 cookies.
Last four eaters ate 240 cookies.

程序说明

请注意程序清单 7.8 中 sum_array( )函数中的 for 循环，

for (pt = begin; pt f= end; pt++)}

total = total + *pt;

它将 pt 设置为指向要处理的第一个元素 (begin-指向的元素) MET. FARE pt COC EL DEA Bi total
中。然后，循环通过递增操作来更新 pt，使之指向下一个无素。上内要 pt 不等手 end，这一过程就将继续下
去。当pt 等于 end时，它将指向区间中最后一个元素后面的一个位置，此时循环将结束

其次，请注意不同的函数调用是如何指定数组中不同的区间的:

int sum-= sum arr{cookies,cookies + ArSize} ;
sum = sum_arr(cookies, cookies + 3) ;-      // first 3 elements

sum = sum_arr(cookies + 4, cookies + 4);   // last 4 elements

指针 cookies + ArSize 指向最后一个元素后面的一个位置〈数组有 ArSize 个元素，因此 cookies[ArSize — 1]
是最后一个元素，其地址为 cookies + ArSize - 1)。因此，区间[cookies，cookies + ArSize]指定的是整个数
组。同样，cookies，cookies + 3 指定了前 3 个元素，依此类推。

请注意，根据指针减法规则，在 sum_amf )中，表达式 end —begin 是一个整数值，等于数组的元素数目。

另外，必须按正确的顺序传递指针，因为这里的代码假定 begin 在前面，end 在后面。

7.3.5 指针和 const

将 const 用于指针有一些很微妙的地方〈指针看起来总是很微妙)，我们来详细探讨一下。可以用两种不
同的方式将 const 关键字用于指针。第一种方法是让指针指向一个常量对象，这样可以防止使用该指针来修

### 第 222 页（PDF p240）

CTR, AARP ASR PAR, ROP DER aie. ERR aa

首先，声明一全指际常量的指针-pt:

int age = 39;

const int * pt = &age;

该声明指出;-pt 指向一个 constint (ie HL 3995 ABE AS RE (EA pt RHESUR MA. RAKES *pt 的
值为 const，不能被修改:

*pt. += 1;        // INVALID because pt points—to a const_int-

gin >> *pt;        // INVALID for the same reason

LCE “i Me Spe BRB EAS eR ATT ES Bis EE, Te RAE RY pt
而言，这个值是常量。例如，pt 指向age，而 age 42 const. A) LEA Heit age 变量来修改 age (HA. 18
不能使用 pt 指针来修改它:

a * pt = 20;        // INVALID because pt points to a const int
age = 20;        // VALID because age is not declared-to be const

LA Hi BRAT AS AS EB A A ER Ss EL. Tk AL A eB A SS a I const 的指针。因此还
有两种可能，将 const 变量的地址赋给指向 const 的指针、将 const 的十址赋纵常规指针。这两种操作都可
行吗? 第一种可行，但第二种不可征:

const float g earth = 9.80; .- -ts-   =      aaa


const Eloat g moon =二:6主;
float * pm = &G moon; ~ _   ff INVALID .

对于第一种情况来说，既不能使用 g_earth 来修改值 9. 80，也不 \能使用 pe 来修改。C+T禁上正第二种情
况的原因很简单-一-如果将Emoon .的地址赋给 pm，则可以使用 pm 来修改 g moon Mf, 这使得 g_ moon
的,const 状态很荒证，因此 C++禁止将 const 的地址赋给非 const 指针。如果读者非要这样做，可以使用强
制类型转换来突破这种限制，详情请参阅第 14 章中对运算符 const_cast 的讨论。

如果将指针指向指针，则情况将更复杂。 前硬i过，假如涉及的是一级间接其系，则将非 const 指针
赋给 const 指针是可以的:

int age =-39;        // age++ is we valid operation
int * pd= kage;      /f_*pd = 41 is a valid operation
const_int.* pt = pd;   f/f *pt-= 42 is an invalid operation

然而; 进入两级间接关系时, 与一级间接关系一样将 ceonsf MISE const (AA HIRE A RAAB ES.
如果多许这样做，则可以编写这样的代码，

const int **pp2;

int. *pl;

const int n= 13;

pp2 = &pl-// not aliowed, but suppose it were:

*pp2 = én; // valid, both const, but sets pl-to point at n

pi se 10; // valid, but changes const n

上述代码将非 const HHHE C&epl) BRAS T const 指针 (pp2).— 因此可以使用pl 来修改 const数据:z 因此，
仅当只有一层间接关系 (如指针指向基本数据类型) 时y ACB CREE const 地址或指针赋给 const 指针。

注意，如果教据类型本身并址是指针，则可以将 const 数据或非 const 数据的地址赋给指向 const 的指
针，但只能将非 const 数据的地址赋给非 const 指针。

假设有一个贞const 数据组成的数组:

const int months[12] = {31,28,31,30,35F,30, 31, 31,30,31,30,31};

TUARS EOS ES ER AE eB ET REA TER © (ESR EERE SA Me

### 第 223 页（PDF p241）

a 一 Toe a Ee    “aa a  6c mma Ss Cae
.  2 int RE 让  ive = Wf Should have. been conat: int’ arr [hk          pay            a ‘
7      |: LED o const cial (months) 由给非 const Hatt (ar), Ine.
=   he       = RATHER cimet   re La foe eee en rene Sen ae ata
CHORE ENS AE PRN RR RARE.
@ 30 FP PPG HT A IR CAH tn FA AE AA
@ 4 Ff const £47 Hak He 4b 2 const 和非 const KH, FM AFR H+ LAE const ams ee
TRE AI,   i) 4S 4b IG BR POA A 45H const 的指针。
为说明另一个微妙之处， 请看下面的声明天
int age = 39;
“第二个声明中的 const AB pe aa 《这里为3 39), mT pt 的值。  emi,
- pt = &sage; // -okay—to ae to 二 location
(AVATAR peRe EHR CLEA 800.
AE const rE A ERE He:
=        int sloth =
const int * ps = &sloth;     万 a pointer to const int
int * const finger = &sloth; // a const pointer to int
TET AA, RES const 的位置与以前不同。  这种声明格式使得 finger russes sloth, {ft
许使用 finger 来修改 sloth WO. “PIMA See eps 来修改-slGth 的值，但允许将 ps 指向另一个位_
i. fait, finger 和?ps都是 const，而*finger Al ps AE CBSE 7.595
eet aoe ee       : int gore = i |-}
:  : “gonst int * psaach = 和 dies:
指向的值      :   另一个变量
可 ant.*  ER me ake 2  or

### 第 224 页（PDF p242）

Se eS ee eens CE Primer Pus-( #6 88) 中文版

 STUER cont 0 cons Sapetensirincieces


加    -- const ， double ， * const’ stick .= -&trouble; ES eat Se     aan      Bae       ~    Sees tee
i            sep,  “stick 只能指向 trouble,      而 stick K不能用类修改 trouble © Ht.   A ia   ae, stick Aitsick 名-

 os       - 通常,:-  将指针 ie aR HRIEEN,  arpa const tein MORO. 6 is aR 1. 3 oF

2 _yoid show_ array (const: double: ar {T;  ak aie                   =

i ROTELLA 9 REISER ACA meen 8名指向指针的指针， Ae  a
EE const    ae ee Pe eet tees  ee se   Se ee

证 7a 丁数和二维类级  人

aos ie ACMOT SRI: 29, Ha ARRON HE, MCAT ERE, ee
JB — eMC — PP ECR AL Je TE HA. lt fr Fm  aie se OES


ieee   Wy sum PREF PARE? mC TITRE CG) 作为参数: cert aoe Ce   oi

eae         Data 3A, AES: MTC BATRA EN SE. 全 int 值给成。 =因此， data” sete

a sun int 2 _(tar2). Bore Ant t Size) ¢

SP Sa A

pam in aI aR IER     es ee
SE   =还有另外-- -种格式二 =这种格式与: Eis HIB A 全相同; “Lara ak     |
0     下述两不原型部挤晶，  ar2 证指针而不是数给。 -还谊注意的是  指针美列指让  它指向由 4 int 组成
tes tia  因此， 指针类型指定了列数，  这就是没有将列数作为独立的函数参数进行传递的原因。       agate —
.由于指针类型指定了列数: 因此 sum( RCRA ET 4 列组成的数组 Asem TAT, BE 5s
. nae sum) EL EAT BBB FB fil       ee  =the  =] Seis Se es see =
ley ane “biel tay     fare Php = .  cone i 加 S 1 er uae S — ae eee . s = ee ;  Ss a ee

sa Mowe,   rina a  100) 3    WE sum ‘alt oe ae

{7 95 “dnt-toetal3 <:sum(a, 10); <= //*sum first- Ai eave see 2 eerh on Seth Ger      i.

¢ te ye int total4’=. ‘sum (a+10,-  20});° f/f sum next 20 rows Of ae: jet fee le el Sa a po Re
ae        te 由于参数 ah 是指向数组的指针  A RA HIE NEN emer 最条间的方法将 ar2 2 ate       |

ee ee ee ee
SE ge ee pid el ee

### 第 225 页（PDF p243）

第7章 函数一 C++的编程模块                           225

total += ar2(r]j [ec];
return total;


同样，行数被传递给 size 参数，但无论是参数 ar2 的声明或是内部 for 循环中，列数都是固定的一一4 列，

可以使用数组表示法的原因如下。由于 枯2 指向数组〈它的元素是由4个int组成的数组) 的第一个元素
元素0)，因此表达式 ar2 +r 指向编号为r 的元素。因此 ar2加是编号为r的元素。由于该元素木身就是一个
由4个int组成的数组，因此 ar是由4个int组成的数组的名称。将下标用于数组名将得到一个数组元素，因
此ar2frl[c]是由4个int 组成的数组中的一个元素，是一个int 值。必须对指针 ar2 执行两次解除引用，才能得到
数据。最简单的方法是使用方括号两次: ar2[rl[cl]。然而，如果不考虑难看的话，也可以使用运管符*两次;


为理解这一点，读者可以从内向外解析各个子表达式的售义，

ar2              // pointer to first row of an array of 4 int

ar2 + 工          // pointer to row r (an array of 4 int)

t(arZ 4x)       // row r (an array of 4 int, hence the name of an array,

// thus a pointer to the first int in the row, i.e., ar2[r]

*(ar2 +r) +c    // pointer int number c in row r, i.e., ar2[xr] + ¢
*(*(ar2 +r) + c // value of int number c in row r, i.e. ar2{(r] [c]

sum( )的代码在声明参数 ar2 时，没有使用 const，因为这种技术只能用于指向基本类型的指针，而 ar2
是指向指针的指针。

7.5 ”本数和 C-风格字符串

C-风格字符串由一系列字符组成，以空值字符结尾。前面介绍的大部分有关设计数组函数的知识也适
用于字符串函数。

例如，将字符串作为参数时意味着传递的是地址，但可以使用 const 来禁止对字符串参数进行修改。
然而，下面首先介绍一些有关字符串的特殊知识。

7.5.1 将 C-风格字符串作为参数的函数 --  - =   和 S

二假设要将字符昌作为参数传递给函数，则表示字符惠的方式有三种:…
char S41; -
@ ”用引号括起的: 字符让常量 《也称字符品字面值              _
(1 ER 3 种选择的类型都是hiF 指针(准确地说是share)， Wa BL DLS Se a
char ghost [15] = "galloping";
3... Char_* str =."galumphing"; _       a 83 Sees    ere
-= . int nl *-strlen{ghost);~. ~~" -// ghost is ghost [0]

int m2 = strlen{str);            // pointer to char
int nd = strlen("gamboling"};    // address of string

可以说是将字符串作为参数来传递，但实际传递的是字符串第一个字符的地址。这意味着字符串函数
原型应将其表示字符串的形参声明为 char*#类型。

C-风格字符串与常规 char 数组之间的一个重要区别是，字符串有内置的结束字符《前面讲过，包含
字符，但不以空值字符绪尾的 char 数组只是数组，而不是字符串)。这意味着不必将宇符串长度作为参
数传递给函数，而函数可以使用循环依次检查字符串中的每个字符，直到过到结尾的空值字符为止。程序
清单 7.9 演示了这种方法，使用一个函数来计算特定的字符在字符串中出现的次数。由于该程序不需要处

### 第 226 页（PDF p244）

理负数，因此它将计数变量的类型声明为 unsigned int.
程序清单 7.9”strgfun.cpp

// strafun.cpp--- funmetions with a string argument
#include <iostream>

unsigned int c_in_str(const char * str, char ch);
int main (}


using namespace std;

char mmm[15} = "minimum";    // atring in an array
// some systems- require preceding char with static to
// enable array imitfalization

char *wail = "vlulate";    // wail points to string

unsigned int ms = c in str(mmm, 'm'};
unsigned int us = c in str(wail, ‘u'};
cout << ms << "
COUT << Yea-<< 下
return 0;

characters in " << mmm << endl;


characters in " << wail << endl;


// this- function counts the number of ch characters
// in the string str
unsigned int c_in_ str(const char * str, char chr


unsigned int count = 0;

while (*str)        f/ quit when *str is '\o'
if {(*str == ch)
count+t+:
str++;        // move-pointer to next char

return-count;

PB PRE FEF SH:

3 m characters in minimum
2 u characters_in ululate

程序说明

由于程序清单 7.9 电的 cint str函数在应修改原始字符奈，因此它在声明形参:s6 时使用于限定符
const。这样，如有果错误地扯函数修改了字符串的内容，凡译器将捕获这种错误。当然，可屋在函数淆中使
用数组表示法，而求声明 str:

unsigned int c_in_str({const char Str[] ，char ch? // also okay

然而，使用指针表示法提醒读者注意，参数不一定必须是数组名，也可以是其他形式的指针。

该国数本身演示了处理字符串中字符的标准方式:

while (*str)


statements
号七工十十，

### 第 227 页（PDF p245）

bei    ieee   ira 全 一
  - ste: RUA AEH NER: ert ers 例如， 第一 RM

二 工的箱将为 mr二- “minimum” 的第-  -个字符=  *只要字符不为空值字符 (0)- *str 就为非零值，  因此循环将

-继续* 在每轮循环的结尾处， -表达式 strt+将指针增加一个宝节， 使之指向字符时中的下一个字符。 SA,

人 Ab beste

ee      75.2 -返回 c -风格字符的函数      人 See ea fie
a    ~ de ieee HEM nem eee ee eget siunieenne
-一- -这样做的效率更高。 fiat: : 程序清单7.16 定义了一个名为buildstrC)的函数， 该函数返回三个指针， iK-- aoe
=  ARES BASAL. :三个字符和一个数字。= AEF new 创建一个长度 与数字参数相等的字符囊， 然后将
| PERMIT. whi. -返回指向新字符种的指针 Os
程认清单7.10  stgback cpp
阿 etrgback. cpp — 县 function: ‘that returns a pointer to char
in char * ‘buikdstr (char c,  int er     a preketne yt
~ int times;—""_     ;
cout. ee “enter a character: a
‘ein 33 ch;            ;
cout ¢< "Enter an. anteger: ";
| char “ps = : ui ldete ted times) j
‘cout << pes << endl;
‘+ delete []--pays5            // free memory.
ps.= ‘bui Fister (*+ ©, ZOE;        te reuse pointer
~* gout: <<_ps <<. a ~DONE~ Wee ps << endl;
’ return 0;
_#/ builds string made of nc characters
    he    char, * petro = new charfin.+ 1); .
ee      pstr (n}  So8NO'; pe ee   Mt teritinate string.   nee   coh tanh Ae eee  ns a SED
nash Or        “petr {nd SF <a  ewe iar 6 0 和      ee peas
Seas ee ae reEuin -二 au  i 75 See en eet a     ey Se  4: are By    a   Ee  id
* ait wwwvwvwvvwwuvgwrvvimrvwvvwvvvwvvwvvwwrwvrvaFruv
a       at    PEREE REE RE Rept DONE- tHe PEPE b EERE tte EE
_ 5 AME HRN. RENEE TH elwpded Bit, a

### 第 228 页（PDF p246）

-228   Ae   )  os rene eS Ce

清单 7.10 中的通数请求分本 n+ ANH ALLE CERO,  并将最后一个字节设置为空值字符，  处后从
-=后向前对数组进往填充。在程序清单 7.10 中,= 下面的循环将循环= YR, 直到nm减少到0,，这将填充nm 个元素:

while (n-- > 0)
“_pstr inl” er;   pee

二和最请= eT eT eee as eis SEM, Ba while HER =
二三 测试条件将对1 和0 BET ECR, RLM BO true, HAASE. WRG. PROS n WY 0. 因此 pstr[0]是最后 = 三
-一个被设置为c 的元素。 之所以从后向前《而不是从前向后) SEE AER i cated alg

一“二 从前向后填充的代码将与下面类似， Be eee   eee   |   faunas

 pet ilies} = Cy                  Geese   :    eee ee et ea eee A Se etm a Be
= 注意，变量 pstr 的作用域为 binildstr 函数内;-  - RE Bee MAIR pte 《而不是字答哩) 使用的内存将 二

被释放。但由于函数返回了 pstr 的值，因此程序仍证以通过 main(]中的指针 ps 来访问新建的字符串。

。 当该字符串不再需要时,程序清单 7.10 中的程序使用 delete 杰放该字符串占用的内存。然后将. ps
-指向为下一个字符串分配的内存块，然后释放它们。 这种设计《让函数返回一个指针，该指针指向new 分--
ROMA) 的缺点是,程序员必须记住使用-deietie。在第 12 章中，读者将知道 C++类如何使用构造函数和
: 拆构函煞负责为您处理这些纲节， ag UP eee alert Be oe Bald Steer ee Sane se


-现在将注意力从数组转到结构: i am HL a RS CT cree TT es
(= SRE, BT CEPR TL CCE GB RMT 结构变量的行为更接近于基本的单值变量; 也就是说，
 5数组不同，结构将其数据组从成单不实体或数据对象，该实体被视为二不整体。前面讲过，订以将一个
-= 结构赋给另外一个结构。同样，也可以按信传递结构;就像普通变量那样。 SEMEL, EER
pe REIS. 另外，函数也可以返回结构。与数组名就是数组第一个元素的地址不同的是,结构名只是 -
”- - “结构的名称，要获得结构的地址，必须使用地址运算符&。在 C 语言和-C++中， 都使用符号&来表示地址
-运算符* ASP, CHR REE APPR RARER, BORER 8 章讨论。
使用结构编程时,，最直接的方式是像处理基本类型那样来处理结构; 也就是说, 将结构作为参数传递，
” 并在需要时将结构用作返回值使用。然而，按值传递结构有一个后点。如果结构非常大，则复制结构将增
加内存要求，降低系统运行的速度。出于这些原因《同时直于最初-C 语言不允许按值传递结构)， 许多 C
程序员倾向于传递结构的地址，然后使用指针来访问结构的内容。C++提供了第三种选择一一按引用传递
(将在第 8 章介绍)。下面介绍其他两种传递方式，首先介绍传递和返回整个结构。

7.6.1 传递和返回结构:

当结构比较小时，按值传递结构最合理，下面来看两个使用这种技术的示例。第一个例子处理行程时

间。有些地图指出，从 Thunder Falls 到:Bingo 城需要 3 小时 50-分钟，而从 Bingo 城到Gotesquo 需要1 小

时 25 分钟。对于这种时间，焉以使用结构来表示一一一个成抽表示小时值，另一个成员表示分钟值。将两
   个时间加起来需要一些技巧，因为可能需要将分钟值转换为小时。例如，前面列出的两个时间的总和为4
-水时75 分钟，应将它转换为 5 小时 15 分钟。 下面开发用王表示时间值的结构， 然后再开发一个函数，它
Rg Sa eee ay    a eee a
“定义结构的工作很简单:  eee me     ti    vee  hire

io eae ees Geaieies ene Gy ot eo ee ce aoa 0 2 Re eee ir

### 第 229 页（PDF p247）

第7章 ”函数一一C++的编程模块


接下来，看一下返回两个这种结构的总和的 sum( )函数的原型。返回值的类型应为 travel_time，两个

参数也应为这种类型。因此，原型应如下所示，

bravel 七ime sum(travel_time tl, travel_time t2);

要将两个时间相加，应首先将分钟成员相加。然后通过整数除法〈除数为 60) 得到小时值，通过求模
运算符 〈%) 得到剩余的分钟数。程序清单 7.11 在 sum( )函数中使用了这种计算方式，并使用 show_time( )

函数显示 travel_time 结构的内容。
程序清单 7.11 travel.cpp

// travel.cpp -- using structures with functions
#include <iostream>
struct travel_time

int hours;

int mins;

const int Mins per hr = 60;

travel time sum(travel time tl, travel _time 七2) ;
void show_time(travel_time t);

int main()

using namespace std;

travel time dayl = {5, 45};    // 5 hrs, 45 min
travel time day2 = {4, 55};    // 4 hrs, 55 min

travel time trip = sum(dayl, day2);
cout << "Two-day total: ";
show _time(trip) ;

travel time day3= {4, 32};
cout << "Three-day total: ";
show_time(sum(trip, day3));

return 0;


travel_time sum(travel_time tl, travel_time t2)


travel time total;

total.mins = (tl.mins + t2.mins) % Mins per hr;

total. hours = tl-hours + t2.hours +

{tl.mins + t2.mins) / Mins_per_hr;

return total;


void show_time(travel_ time 七)
using namespace std;
cout << t.hours << " hours, "
<< t.ming << " minutes\n";

### 第 230 页（PDF p248）

其中,-travel_time 就像是一个标准的类型名，可被用来声明变量、范数的返回类型和国数的参数类型 ，
由于 total Al tl 变量是 travel time 结构，因此可以对它们使用句点成员运算符。 由于 sum(J函数返回
travel_time 结构，因此可以将其用作 show_time( )函数的参数。 由于在默认情况下，C3#+图数按值传递参数，
因此函数调用 show_time(sum(trip, day3))# PUsLe SEH] suml(trip，day3)，引获得其返回值。然后，
show_time( )调用将 sum( )的返回值《而不是函数自身三传递给 show_time( )e 下面是该程序的输出;

Two-day total: 工作 hours, 40 minutes

Three-day total: 15 hours, 12 minutes

7.6.2”另一个处理结构的函数示例

方面介绍的有关函数和 C++结构的大部分知识都可用于 C++类中，国此有必要介绍另一个示例。这次
要处理的是空间，而不是时间。有具体地说，这个例子将定义两个结构;用于表示两种不同的描述位置的方
法，然后开发-个函数，将一种格式转换为另一种格式，并显示结果。这个例子用到的数学知识比前一个
要多，但并不需要像学习数党那样学习 CH.
的水平偏移量和垂直偏移重。 传统上, 数学家使用x 表示水平偏移量, 使用y 表示垂直偏移量(参见图7.6和5
x Al y 一起构成了直和角坐标_(rectangular coordinates)。可以定艾由两个坐标组成的结构来表示位置;

Micromips相对于Byteville的直角坐标

图 7.6 直角坐标
struct rect
double x;          // horizontal distance frem origin
double y;         // vertical distance from origin


另一种描述点的位置的方法是，指出它偏离原点的距离和方向〈例如，东偏北 40 度)。传统上，数学
家从正水平轴开始按道时针方向度量角度(参见图 7.7)。 距离和角度一起构成了极坐标 (polar coordinates ) .
可以定义另一个结构来表示这种位置:

struct polar

double distance; // distance from origin
double angle;      // direction from origin

### 第 231 页（PDF p249）

第7章 函数一一(C++的编程模块                               231

图77 极坐标

下面来创建一个显示 polar 结构的内容的函数。C++库 CM C 语言借鉴而来) 中的数学函数假设角度的-

单位为台度-因此应以统度为单位来测量和角度。但为了便于显示，我们将弧度值转换为角度值。这意味着=

需要将听麻值磁以 180/mc 一一约为 57.29$77951+。该 国数的代码如下:

// show polar. coordinates, converting angle to degrees
一 _VeciG enhow polar {polar 人

全

using namespace std;
const double Rad to deg = 57.29577951;

cout << "distance = " ee dapos.distance;
cout << ", angle =—™<<- dapos. angle * Rad_to 3
cout << " degrees\n";
请注意，形参的类型为 polars 将一个 polar 结构传递给该函数时，该结构的内容将被复制到 dapos 结
构中-函数随后将使用该拷贝完成工作。由于 dapos 是一个结构，因此该函数使用成员运算符句点〈参贴-
第 4 章) 来标识结枸成员。
接下来，让我们试着再前进一步，编写一个将- PEs be By A  该函数接受一个 rect S
数，并返回一个 polar 结构。这需要使用数学库中的函数-因此程序必须包含头文件 cmath《〈在较旧的系统
中为 math.h). 54h, 在有些系统中，  还必须命令编译器载入数学库 (参见第 1 章)。可以根据毕达哥拉斯

定理，使用水平和垂直坐标来计 #5
distance = sqrt x * x+ y =¥)
”数学库中的 atan2( )函数可根据二和y 的值计算角度:
还有一个 atan( pa, (AE AER a 180-度之内和之外的角雇。在数学函数下，这种不确定性与在生
他手册中一样不受人欢迎。                                   -
// convert rectangular to-polar coordinates

polar rect_to-polar(rect xypos)   // type polar

### 第 232 页（PDF p250）

polar answer;

answer.distance =

sqrt{ xypos.x * xypos.x + xypos.y * xypos.y);
answer.angle = atan2(xypos.y, xypos.x);
return answer;      // returns a polar structure

编写好函数后，程序的其他部分编写起来就非常简单了。程序清单 7.12 列出了程序的代码。

程序清单 7.12 atrctfun.cpp

// stretfun.cpp -- functions with a structure argument
#include <iostream>
#include <emath>

// structure declarations
struct polar
double distance;      // distance from origin
double angle;         // direction from origin
struct: rect


double x;             // horizontal distance from origin
double y;             // wertical distance from origin


// prototypes
polar rect_to polar(rect xypos) ;
void show polar(polar dapos);

int main()

using namespace std;
rect rplace;
polar pplace;

cout «< "Enter the x and y values: ";
while (cin >> rplace.x => rplace.y} // slick use of cin


pplace = rect_to polar(rplace) ;

show _polar|pplace) ;

cout << "Next two numbers (q te quit}: ";

cout << "Done.\n";
return 0;

// convert rectangular to polar coordinates
polar rect_to polar(rect xypos)

using namespace std;
polar answer;

answer.distance =
sqrt | xypos.x * xypos.x + xypos.y * xypos.y);

### 第 233 页（PDF p251）

第7章 函数一一C++的编程模块              233

answer.angle = atan2(xypos.y, xypos.x);
return answer;      // returns a polar structure


// show polar coordinates, converting angle to degrees
void show polar (polar dapos)


using namespace std;
const double Rad_to_deg = 57.29577951;

cout << "distance = " << dapos.distance;
cout << ", angle = " << dapos.angle * Rad to deq;
cout << " degrees\n";

ER: 有些编译器仅当被明确指示后，才会搜索数学库。例如，较早的 gH+版本使用下面这样的命

g++ structfun.c -1lm

下面是该程序的运行情况:

Enter the x and y values: 30 40

distance = 50, angle = 53.1301 degrees

Next two numbers (q te quit): -100 100

distance = 141.421, angle = 135 degrees

Next two numbers {q to quit): q

程序说明

程序清单 7.12 中的两个函数已经在前面讨论了，因此下面复习一下该程序如何使用 cin 来控制 while

while (cin >> rplace.x >> rplace.y)

前面讲过, cin 是 istream 类的一个对象。抽取运算符(>>])被设计成使得 cin>>rplace.x 也是一个 jstream
对象。正如第 11 章将介绍的，类运算符是使用函数实现的。使用 cin>>rplace.x 时，程序将调用一个函数，
该函数返回一个 istream 值。将抽取运算符用于 cin>>rplace.x Xf CHAR cin>>rplace.x>>rplace.y 这样)，也
将获得一个 istream 对象。因此，整个 while 循环的测试表达式的最终结果为 cin，而 cin 被用于测试表达式
中时，将根据输入是否成功，被转换为 bool 值 tue 或 包lse。例如，在程序清单 7.12 中的循环中，cin 期户
用户输入两个数字，如果用户输入了 q (前面的输出示例就是这样做的)，cin>>将知道 q 不是数字，从而
将q留在输入队列中，并返回一个将被转换为 fasle 的值，导致循环结束。

请将这种读取数字的方法与下面更为简单的方法进行比较:

for (int i = 0; i < limit; i++)

人

if (temp < 0)
break;
arti] = temp;


要提早结束该循环，可以输入一个负值。 这将输入限制为非负值。这种限制符合某些程序的需要，但通
常需要一种不会将某些数值排除在外的、终止循环的方式。将 cin>>用作测试条件消除了这种限制，因为它
接受任何有效的数字和输入。在需要使用循环来输入数字时，别忘了考虑使用这种方式。另外请记住，非数字
和输入将设置一个错误条件，禁止进一步读取输入。如果程序在输入循环后还需要进行输入，则必须使用
cin.clear( )重置输入，然后还可能需要通过读取不合法的输入来丢弃它们。程序清单 7.7 演示了这些技术。

### 第 234 页（PDF p252）

7.6.3 ”传递结构的地址

假设要传递结构的地址而不是整个结构以节省时间和空间，则需要重新编写前面的函数，使用指向结
构的指针。首先来看一看如何重新编写 show_polar( )函数。需要修改三个地方;

曙。”调用函数时，将结构的地址〈总pplace) 而不是结构本身 (pplace) 传递给它;

e HSAs polar KEE, EN polar *类型。由于函数不应该修改结构, 因此使用了 const 修饰符;

和”由于形参是指针而不是结构，因此应间接成员运算符〔〈-> )，而不是成员运算符〔句点)。

完成上述修改后，该函数如下所示，

// show polar coordinates, converting angle to degrees
void show _polar (const polar * pda)


using namespace std;
const double Rad_to_deg = 57.29577951;

cout << "distance = " << pda->distance;
cout << ", angle = " << pda->angle * Rad_to_deq;
cout << " degrees\n";


接下来对 rect_to_polar 进行修改。由于厚来的 rect_to_polar 函数返回一个结构，因此修改工作更复杂
些。为了充分利用指针的效率，应使用指针，而不是返回值。为此，和需要将两个指针传递给该函数。第一
个指针指向要转换的结构，第二个指针指向存储转换结果的结构。函数不返回一个新的结构，而是修改调
用函数中已有的结构。因此，虽然第一个参数是 const 指针，但第二个参数却不是。也可以像修改函数
show_polar( ) 修改这个函数。程序清单 7.13 列出了修改后的程序。

程序清单 7.13 strctptr.cpp

// stretptr.cpp -- functions with pointer to structure arguments

#include <iostream>
#include <cmaths>

// structure templates
struct polar
double distance;      // distance from origin
double angle;         // direction from origin
struct rect
double x;             // horizontal distance from origin
double y;             // vertical distance from origin


// prototypes
void rect_to polar(const rect * pxy, polar * pda);
void show_polar (const polar * pda);

int main(}

using Namespace std;
rect rplace;
polar pplace;

### 第 235 页（PDF p253）

第7章 ”函数一一C++的编程模块                            235

gout << "Enter the x and y values: ";

while (cin >> rplace.x >> rplace.y)

rect to polar(&rplace, &pplace);    // pass addresses
show polar (&pplace) ;        // pass address
cout << "Next two numbers ({q to quit): "


cout << "Done. \n";

return 0;


// show polar coordinates, converting angle to degrees
void show_polar (const polar * pda)

using namespace std;

const double Rad_to_deg = 57.29577951;

cout << "distance = " << pda-sdistance;
cout << ", angle = " << pda->angle * Rad_to deg;

cout << " degrees\n";


// convert rectangular to polar coordinates
void rect_to_polar(const rect * pxy, polar * pda)


using namespace std;
sqrt (pxy->x * pxy->x + pxy->y * pxy->y);
pda->angle = atan2(pxy->y, pxy->x);

注意，有些编译器需要明确指示，才会搜索数学库。例如，较早的 g++版本司用下面这样的命令行:
g++ structfun.c -lm

从用户的角度来说,程序清单 7.13 的行为与程序清音 7.12 相同。它们之间的差别在于，程序清单 7.12
使用的是结构副本，而程序清单 7.13 使用的是指针，让函数能够对原始结构进行操作。

7.7 RF string BR

虽然 C-风格字符串和 string WRAL A lal, (8-45 Se EL, string WR SAM PA. Pn,
AY RK — HRS AS, HET LEP RR POR BY ORE TE Se MS ES
函数，也可以将对象作为完整的实体进行传递。如果需要多个字符串，可以声明一 Bika, iad a
=     - 程序清单 7.14 提供了二 -不下型示例， emmy fang Perry ace Te
AHA.


oes : OL “程序清单7. 14°  _topfive. cpp   See Se i ca es Bie 这 本 Coy ee

 f/ topfive.cpp '-~ handling an array ‘of string objects ee ee al:     一


#include. <string>’.     SB fiat!
using. namespace ase ae =  ss ea      ie ee

### 第 236 页（PDF p254）

‘const int SIZE = r?
oy void display (const-string eat” int a);


_ string list [SIZE] ;      // amarray-holding 5 string object
: cout ee. "Enter “your "ee SIZE <<.-" favorite astronomical: sights: MEE igen
_ for’ (an i= -0;-i < SIZE;  oad  ze mee,
; ‘cout << 4-4 lec": -*
getline(cin,list [i]);

I 3 =  nestle ese     a  二 SS

“cout ec "Your. fists \n";
2 和  SIZE) ;

return 0;

上

_ wotd-display(const string SRE ni

-下面是 该程序的运行情况: :

Enter: -your 5 favorite astronomical sights; vo
1: Orion Nebula—
2: M13
3: Saturn
4: Jupiter >
25: Moon -
“1: Orion Nebula
2 一M13
3;—Saturn
i Jupiter .
5:Moon

对手该示例，和需要指出的一点是，除函数 getline( Yt. ARPA A BAY Cal int) 一样对待 string
对象。如果和需要-string 数组; 只需使用通常的数组声明格式即可:

string list [SIZE] ;     /f/-an array holding. 5 string object

这样，数组 list 的每个元素都是一个 string HR. WOR PRA:

getline(cin,list[i]);

同样，形参 sa 是一个指向 string MRM, Att sa[订是一个 string WR, ALR FEE:


7.8 ”本数与 array PR

在 C++中，类对象是基于结构的，因此结构编程方面的有些考虑因素也适用于类。例如，可按值将对
象传递给函数，在这种情况下，函数处理的是原始对象的副本。恤外，也可传递指向对象的指针，这让函
数能够操作原始对象。 下面来看一个使用 C++11 模板类 array 的例子。

### 第 237 页（PDF p255）

“假设您要使用一个array 对象来存储一 =年四个季度的开支,，     fee

本 yaa  ied  BR Crim

sit std;  jarray<double, 4> expenses ;,

ASTGITBELL,.  要使用 array. 2.   需要包含头文件 arya array. UF AE std 1s   EE -

" show (expenses); ee

Oe ewe exes expenses, 由需将该对象的地址传递给函数 CF: eNO 种方法一使

用引用):

— ab expenses WAR, IBM sipeenets a  -    poeta —

ets  Salhi eed  : Ba ag

全于和可全          -      加
-这 与程序清单 ce  13  eB GMa 使用 的方法相 rt.

void sho

wtetidi  ‘aerayedibie, do dak . ff da_an object

void fill(std::array<double, 4> * pa); // pa-a pointer te an object

这些考虑因素是这们示例程序的核心。 该程序还包含其他一些功能。首先，

const in

t Seasons = 4:

Aisi 如何声明这两个函 HE? expenses 的类型为 a 4>， | baad mM bane OS

它用符号常量蔡换了了4:

其次，它使用了一个 constarray HR, AMIR 4 + string WHR. AP RARILPBEE:

const std::arrayestd::string, Seasons> Snames-=


ring", "Summer", "FaFl"; "Winter"}>—

请注意，模板 array FIER REAP SEAR BRR. CIEE ARERR.  程序清音 TAS 列出了该程序的

程序清单7.15 arrobj.cpp

/ farrobj
#include
#include
#include

.Cpp -- functions with array objects {C+411)


ant data

const int Seasons = 4;

conse st

d::arrayestd::string, Seasons> Snames =

{"Spring", "Summer", "Fall", "Winter"};

// Eunction to modify array object

void fil

l(std::array<double, Seasons> * pa);
ion that uses array object without modifying it

void show(std::array<double, Seasons> da);

int main()


std:
fill

tarray<double, Seasons> expenses;
(fexpenses) ;

show (expenses) ;

return 0;


void fill(std::array<double, Seasona> * pa)


using namespace std;

for


{int 1 = GO; i <« Seasons; i++)

cout << "Enter " << Snames[i] << " expenses: ";
cin >> (*pa) [i];

### 第 238 页（PDF p256）

void show(std::array<double, Seasons> da)


using namespace std;

double total = 0.0;

cout << "\nEXPENSES\n";

for {int i = 0; i < Seasons; i++)

total += da[i];


cout << "Total Expenses: $" << total << endl;

下面是该程序的运行情况:

Enter Spring expenses: 212

Enter Summer expenses: 256

Enter Fall expenses: 208

Enter Winter expenses: 244

EXPENSES

Spring: $212

Summer: $256

Fall: 5208

Winter: $244

Total: $920

程序说明

由于 const array 对象 Snames 是在所有函数之前声明的，因此可后面的任何函数定义中使用它。与
const Seasons 一样，Snames 也有整个源代码文件共享。这个程序没有使用编译指令 using，因此必须使
用 std::限定 array 和 string。为简化程序，并将重点放在函数可如何使用对银上，函数 OMAR A

函数 fl0和 showO都有缺点。函数 show0存在的问题是，expenses 存储了四个 double 值，而创建一个
新对象并将 expenses 的值复制到其中的效率太低。如果修改访程序，使其处理每月甚至每日的开支，这种
问题将更严重。

函数 fllO使用指针来直接处理原始对象, 这避免了上述效率低下的问题, 但代价是代码看起来更复杂:

fill(&expenses);    // don't forget the &

ein => (*pa) [il;

 在最后一条语句中，pa 是一个指向 array<double, 4-7 RNR, Alle*pa 为这种对象，而(*pal) [是该
对象的一个无束。由于运算符优先级的影响，其中的括号必不可少。这里的逻辑很简单，但增加了犯错的
机会。

使用第 8 章将讨论的引用可解决效率和表示法两方面的问题。

7.9 i?#VA

下面介绍一些完全不同的内容。C++函数有一种有趣的特点一一可以调用自己《然而，与 C 语言不同
的是，C++不允许 main( )调用自己)，这种功能被称为递归。尽管递归在特定的编程《例如人工智能) 中是
一种重要的工具，但这里只简单地介绍一下它是如何工作的。

### 第 239 页（PDF p257）

第7章 ”函数一一C++的编程模块              239

7.9.1 包含一个递归调用的递归

如果递归函数调用自己，则被调用的函数也将调用自己，这将无限循环下去，除非代码中包含终止调
用链的内容。 通常的方法将递归调用放在 证语句中。例如，void 类型的递归函数 recurs( )的代码如下:

void recurs(argumentlist)

人

statements1
if (test)

recurs (arguments)
statements2


test 最终将为 但lse，调用链将断开。

递归调用将导致一系列有趣的事件。只要 评语句为 tue，每个 recursf )调用都将执行 statements 1，然
后再调用 recurs( )，而不会执行 statements 2。当 if ANA false 时，当前调用将执行 statements2。当前调用
结束后，程序控制权将返回给调用它的 recurs(), 1% recurs( )将执行其 stataments2 部分，然后结束，并将
控制权返回给前一个调用，依此类推。因此，如果 recurs( )进行了 5 次递归调用，则第一个 statements! 部
分将接函数调用的顺序执行5 次，然后 statements2 部分将以与函数调用相反的顺序执行5次。进入5$层递

后，程序将沿进入的路径返回。程序清单 7.16 演示了这种行为。

程序清单 7.16 recur.cpp

// recur.cpp -- using recursion
#include <iostream>
void countdown(int n);

int main()


countdown (4);           // call the recursive function
return 0;


void countdownl{int n)


using namespace std;

cout << "Counting down ... " << n << endl;
countdown (n-1);     // function calls itself


下面是该程序的输出;

Counting down     4    «level 1; adding levels of recursion
Counting down ... 3    «level 2

Counting down ... 2    slevel 3

Counting down ... 1    <level 4

Counting down ... 0    slevel 5; final recursive call
0: Kaboom!             ¢level 5; beginning to back out


4: Kaboom!             clevel 1

注意，每个递归调用都创建自己的一套变量，因此当程序到达第 5 次调用时，将有 5 个独立的n 变量，

### 第 240 页（PDF p258）

Beret t  为验证这  se 读者可以修改程序清单了16; -使之显示下的地十和值，


i 耳


Counting down ... 4 (n at OO}T2FEOC}

Counting down ... 3_(n at 0012FD34)

Counting dewn ....2-(m at QO12FCcsCc}

Count fig down ...1 (mn at 0012FB84)

Counting down ...-0 (nm at-0012FAAC)        “ire
0: Kaboom! 三-一:    fn at 0012FAAC)       ee
Ll: Kaboom!         (n at 0012FR84)

2: Kaboom!       (mat O012FCSC) _

3: Kaboom!         (rat 0012FD34}


注意，在一个内存单元《内存地址为001H2FE0OC)一存储的mn 值为4= CES AA ee OA Pet
0012FD34,. fF itn (4 33 等等，另外，注意到在 Counting down 阶段和Kaboom 阶段的相同层级，nm 的
地址相同:

79.2 和包含多个递归调用的递归-

在希要将一项工作不断分为两项较小的~ 类似的工作时，递归非常有有用。例如65 请考虑使用这种谨法
来绘制标尺的情况.。 PP, EAP ASE eR. 然后将同样的操作用于标尺的下半部分和种半部分
如果要进一步细分，可特同样的操作用于当前的每一部分。 递归方法有时被称为分而治这策略
(divide-and-conquer strategy)。程序清单-7.17 (87H eB eR BY subdivide( )壮示工这种方法，该函数使用一个
字符囊，该字符串除两端为上字符外-其他全部为空格。 mair函数使用循环调用 supdivide(])函数6 次，得
次将递归层编号加 1，并打印得到的字符串。这样，每行输出表示一层递时。该程序使用限定符 std::而不
是编译指令 using，以提醒读者还可以采取这种方式。

程序清单 7.17 ruler.cpp

// culer.cpp -- using recursion to subdivide a ruler
flinclude <iostream>

const int Len = 66;

const int Divs = 6;

void subdivide(char ar[], int low, int high, int level);
int main()


char ruler[Len];

int 2}

fuler fi} =! %y

ruler[Len - 1] = '"\o';

int max = Len - 2;

int min = 0;

ruler [min]l = ruler[max] = '|';

std::cout << ruler << std::endl:


subdivide(ruler,min,max, i);
std::cout << ruler << std::endl;

### 第 241 页（PDF p259）

第7章 函数一 C++的编程模坪              241

ruler[j) = 1 '; // reset to blank ruler


return 0;


void subdivide(char ar[{], int low, int high, int level)

LE (level == 0)

return;

int mid = {high + low) / 2;

ar[mid] = '|';

subdivide({ar, low, mid, level - 1);

gubdivide(ar, mid, high, level - 1);

下面是程序清单 7.17 Pa:

LIT

程序说明

在程序清单 7.17 中，subdividet )函数使用变量 level 来控制递归层。函数调用自身时，将把 level 减 1，
当level 为 0 时，该函数将不再调用自己。注意，subdivide( )调用自己两次，一次针对堪半部分，另一次针
对右半部分。量初的中点被用作一次调用的右端点和另一次调用的堪端点。请注意，调用次数将呈几何级
数增长。也就是说，调用一次导致两个调用，然后导致 4 个调用，再导致 8 个调用，依此类推。这就是6
层调用能够填充 64 个元素的原因【26=-64)。这将不断导致丽数调用数〔《以及存储的变量数) 翻倍，因此如
果要求的递归层次很多，这种递归方式将是一种糟糕的选择，然而，如果递娄层次较少，这将是一种精致
而简单的选择。

7.10 WRisttr

如果未提到函数指针，则对 C 或 C++函数的讨论将是不完整的。我们将大致介绍一下这个主题，将完
整的介绍留给更高级的图书。

与数据项相似，函数也有地址。于数的地址是存储其机器语言代码的内存的开始地址。通常，这些地
址对用户而言，既不重要，也没有什么用处，但对程序而言，却很有用。例如，可以编写将另一个函数的
地址作为参数的函数，这样第一个函数将能够找到第二个函数，并运行它。与直接调用另一个函数相比，
这种方法很佛拙，但它允许在不同的时间传递不同函数的地址，这意味者可以在不同的时间使用不同的
函数。

7.10.1 函数指针的基础知识

首先通过一个例子来阐释这一过程。 假设要设计一个名为 estimate( )的函数，佑算编写指定行数的代码
所需的时间，并且希望不同的程序员都将使用该函数。对于所有的用户来说，estimate( )中一部分代码都是
相同的，但该函数允许每个程序员提供自己的算法来估算时间。为实现这种目标，采用的机制是，将程序

### 第 242 页（PDF p260）

员要使用的算法函数的地址传递给 estimate( )。为此，必须能够完成下面的工作:
@ 获取函数的地址;
e ”声明一个函数指针;
@ 使用函数指针来调用函数。

1. FRR BAK A Hebe

获取函数的地址很简单: 只要使用函数名《〈后面不跟参数) 即可。也就是说，如果 think( )是一个函数，
则 think 就是该函数的地址。要将函数作为参数进行传递，必须传递函数名。一定要区分传递的是函数的
地址还是函数的返回值;

process (think) ;    // passes address of think[) to process ({}

thought (think()); // passes return value of think() to thought ()

process( )调用使得 process( )pA SURE 4 FLA BURA] think( )函数。thought( )调用首先调用 think( ) 3,
然后将 think( )的返回值传递给 thought( )函数。

2. 上声明函数指针

声明指向某种数据类型的指针时，必须指定指针指向的类型。同样，声明指向函数的指针时，也必须
指定指针指向的函数类型。这意味着声明应指定函数的返回类型以及函数的特征标(和参数列表)。也就是说，
声明应像函数原型那样指出有关函数的信息。例如，假设 Pam leCoder 编写了一个估算时间的函数，其原
型如下:

double pam(int); // prototype

UTES Fa EP SS FSB OT

double (*pf){int); // pf points to a function that takes
// one int argument and that
// returns type double

这与 pamt )声明类似，这是将 pam 替换为了《〈*pf)。由于 pam 是函数，因此《〈*pf) 也是函数。而如果
(*pf) 是函数，则 pf 就是函数指针。

提示: 通常，要声明指向特定类型的函教的指针，可以首先编写这种函数的原型，然后用 (*pf) ee
BIZ, AF pf HAAR HAHAH,

为提供正确的运算符优先级，必须在声明中使用括号将*pf 括起。括号的优先级比*运算符高，因此*pf
Cint) 意味着 pf )是一个返回指针的函数，而〈*pf) (int) 意味着 pf 是一个指向函数的指针:

double (*PE) (int); // pf points to a function that returns double
double *pf({int);  // pf() a function that returns a pointer-to-double

正确地声明bf后，便可以将相应函数的地址研给它;

double pam(int);

double (*p£) (int);

pf = pam;           // pf now points to the pam{) function

TER. pam( MAEM ADE AR aS pe 相同。如果不相同，编译器将拒绝这种赋值
double ned(double) ;

int ted{int);

double {*pf) {int) ;

pi = ned;         // invalid -- mismatched signature

pi = ted;         // invalid -- mismatched return types

现在回过头来看一下前面提到的 estimate( )函数。假设要将将要编写的代码行数和估算算法(如 paml )
pai) 的地址传递给它，则其原型将如下:

void estimate(int lines, double (*pf} (int)};

### 第 243 页（PDF p261）

a = j mena es      7 ae  Biker aie     per a waed ae pee ae

ak 述志 muti,   第一个参数是 < 数指针，  “emia 过个 int SMe   并加   a double fits


am We “estimate (50,”  - pam); // fuhctien carl telling pt use pant = = teas :  全 repay ma

     a  AGP ue  HAE EH  TE MH LE A        re  .
a  Tie Rian aa  a 2 ae     | sees wats see       Te eesti oe - pes  pace Daa atte z

oe  “Bide NE,  a dae Sw a I. iemknmtt ea. mt, Cp rts

-二 角色与函数名相同,因此使用 pf): Rh, FR CA MAT, Fo

a  ae  doubie’ “pant Eat la:   ey ee 22 Hist EEE  “Se ghee mean ee a = Bs ne cee r - Bo va Alas   a

|  ne ae pam; a 7    vy, bE s ‘now. points ta the pam (e function |  - ‘(rl     .    aie
as dees ant Boe Call: “pam Q)> “using “the” ‘function name = ey Snape ey Nat re Taos: it fs wes ie   :

i: jE eoubie y=: epee 3)  的 “yping.. the: Pointer Be   = coer a ey es

区 ea =, pe (SI ie    otk. also call pant using | tbe pointer: “PEE woes oe ee = oo See

aeeee es 为何 pt (ph) “Sire? ae,  aT pride, wtp Dba, =
因此应将 (pf) OREN. 另一种学派认为,由于函数名是指向该函教的指狂，措向冰数的指针的-、

 “二 ARS BRS A, BLL pil) Pe AA eA CH+进行了拆圳-一 这 2 Ay AE EA, 或-

和 rk hi. BRENALALA EH RH: BTA HAAS HS BANA, SEM

法自轩其说的观点正是人类思维活动的特点。    ee

7.102, 函数据针示全 ree as Feat aves ao aes ee “lie i :

-一

Ri is a ECFA estima 通数2   一次传递 betsy( RMT pe :
ARE pam PR AAMT Sine HA ant AONB: 在第三种情

 -的算法时; .将不需要重新编写 ca人- HUB He reaper ip BML. onic beast

“和返回类型正确即可。 当然,重新编写 estimatet BI ASAE — 件非常困难的工作，但同样的原则也适用于更
”复杂的代码。 ah REE RA sap HEA ese we BARTS -estimate( ve os


WE finiper:< cpp RE to, » Funct ions Fee a ee a ee me

和 本 double. betsy(inthi

oe double ineitae hy     : 3 ne Donan eons

"See / ‘A ‘second, argament is” “pointer, to a ‘type double function, chat °
f/ takes a type int argument

ope void estimate (int. lines,  double. (pf) vane) rf gees es Be sy pee aap

int maint

using namespace std;
int code;

### 第 244 页（PDF p262）

cout << "How many lines of code do you need? ";
cin »> code;

eout << "Here's Betsy's estimate: \n";
estimate(code, betsy);

cout << "Here's Pam's estimate: \n";
estimate(code, pam) ;

return 0;

double betsylint Ins)


return 0.05 * Ins;

double pam(int ins)
return 0.03 * lns + 0.0004 * Ins * Ines;

void estimate(int lines, double (*pf) {int} )
using namespace std;
eout << lines << " lines will take ";


下面是运行该程序的情况:

How many lines of code do you need? 30
Here's Betsy's estimate:

30 lines will take 1.5 hour(s)

Here's Pam's estimate:

30 lines will take 1.26 hour(s}

下面是再次运行该程序的情况，

How many lines of code do you need? 100
Here's Betsy's estimate:

100 lines will take 5 hour(s)

Here's Pam's estimate:
160 lines will take 7 hourts)

7.10.3 深入探讨函数指针

函数指针的表示可能非常恐怖。下面通过一个示例演示使用函数指针时面临的一些挑战。首先，下面
-些函数的原型，它们的特征标和返回类型相同，

const double * £l{(const double ar[], int n)};
const double * f2{(const double [], int);
const double * £3(const double *, int);

这些函数的特征标看似不同，但实际上相同。首先，前面说过，在函数原型中，参数列表 const double
ar[]与 const double * ar 的含义完全相同。其次，在函数原型中，可以省覆标识符。因此，const double ar [ ]
可简化为 const double [ ]，而 const double * ar 可篇化为 const double *。因此，上述所有函数特征标的含义
都相同。另一方面，函数定义必须提供标识符，因此需要使用 const double ar [ ]或 const double * ar.

接下来,假设要声明一个指针，它可指向这三个函数之一。假定该指针名为 pa，则只需将目标函数原

型中的函数名奉换为(*pal:

### 第 245 页（PDF p263）

a nearer       ee ee ee
-* Usonst: double “* -(*pl):(const° -Acuble - et Neey Sei eae SEER Cec riay oe, ae On ee ee
a | ae a 自动类型推断功能时> 代码要简单得多::
eh aes auto: P2 a      al Cer ‘automat ic type deduction” = — Pg! — 2 geige eg es hee - 过 a
ROR THN.    fe nee Ce bee Be
“根据前面介绍的知识可逢，(*p1) (av-3)和 p2(av, 3都调用指认的函数(这里为f f1QAE 120). IPH av 和 fa. |
Sh Bie. Balke “ED 7 JE 7 HALA. -返回值的类型为:const double * (即-dauble 值的地下)

二因此在每条 cout 语句中; 前半部分量示的都是一全dobbie值的士址。 OBO AT ES SESE ROT SIM

-=需要将运算符*应用于这些地址， 如表达式*(*p1)(av3)和*p2(av3)所示，

鉴于需要使用三个函数，如果有一 Aon HCALRS LS A, RES OTA for MORIA

eee ee Ce ree ee ee ae eae
: AED DAA Me 2 A Ra. RE CHT 2 E.# PLE CaS 、-、，

AR REHOME. EAT SEIMEI EES RIELEZ: AFAR const double win °° 22
= 二 即将 const double *Alint 作为参数，:并返回二个 const double*,. 2, —       sens

ae mn eR Te 2 Se et eee

“+ -Genst double: “(*pa[3])}-(const double.“*; int} = (£1.62: £3];

2g fH [TIARA HAT 2 pa SE = LS Re RL + SE 7 RE OP BEA a3]
ONE RR RT RU 运算符上的优先级高手#，因此*pal3]表明pa 是二个

-二 汪汪回类型为 const double yea ee. TARE  pa是二个包含:= 三全指针的数组;: eu ali age a oo

二 BCAA AMO auto We? ASHE. :目动类型礁断具能用于单值初冶化 ee hit  “eutinae

‘autozpb:= pay 2 tm     Pe i aap tN as ea      -       eect a

pee MUZE ATT ieee mam


2 conbt “double: bed "py (Ct pb) (ay; 33   oS need var

, double ve F(epp il avi 3) }      a

nnd 3— PAPE OREN RCH ACHE HHA Z pa ee Ct  因此指疝娄组的-

“Lt gaan. RUA AE RR Af FT TS

-因此可使用auto;    Spite EyesSg erer
e    saute Pos pai!   eas: C++15 automatic. _type deduct don oe vit ae:     :        pte =e  5 ane
ena 大果您喜欢自己声明， 该如何办呢? 显然， 这种声明应类似于愉 的声明 :但由于增加了一层间接。
eae In — 个*。 具体地说- 如果这个指针名为 pt，则需要指出它是一个指针，而不是数组。
ARORA RACIR), FHS HSH RE Some i
(*pd) [3] // (a pointer to an array of 3 elements
to | BATA. it  -个指针，  罗汉  个包人三  -个元素的数组。 oe AME? 由 pa sie cde Ts

const acupte: + ep) (cna -double + tnt) ea  de.

### 第 246 页（PDF p264）

要调用函数，需认识到这样一点: 既然 pd 指向数组，那么*pd 就是数组，而(*pd)[j是数组中的元素，
即函数指针。因此，较简单的函数调用是(*pd)j[iltav3)，而*(*pd)[il(av,3)是返回的指针指向的值。也可以
使用第二种使用指针调用函数的语法， 使用(*(*pdj[il)(av3)来调用函数，而*(*(*pd)[i])(av3)是指向的
double 值。

请注意 pa(它是数组名，表示地址) 和上pa 之间的差别。正如您在本书前面看到的,在大多数情况下，
pa 都是数组第一个元素的地址，即有pa[0]。因此，它是单个指针的地址。但有pa 是整个数组〈即三个指针
块) 的地址。从数字上说，pa M&pa 的值相同，但它们的类型不同。一种差别是，pa+1 为数组中下一个元
素的地址，而位pa+l 为数组 pa 后面一个 12 字节内存块的地址《这里假定地址为4字节)。另一个差别是，
要得到第一个元素的值，只需对 pa 解除一次引用，但需要对皮pa 解除两次引用:

*tEpa == *pa == Da[0]

程序清单 7.19 使用了这里讨论的知识。出于演示的目的，函数 fi()等都非常简单。正如注释指出的，
这个程序演示了 auto 的 C++98 替代品。

程序清单 7.19 arfupt.cpp

// arfupt.cpp -- an array of function pointers
#include <iostream>

// various notations, same signatures

const double * f1(const double ar[], int n);
const double * £2{const double [], int);

const double * £3(const double *, int);

int main()
using namespace std;
double av[3] = {1112.3, 1542.6, 2227.9];

// pointer to a function

const double *(*p1) (const double *, int) = f1;

auto p2 = £2; // C++ll automatic type deduction

// pre-C++1l can use the following code instead

// const double *(*p2) (const double *, int) = f2;
cout << "Using pointers to functions: \n";

cout << " Address Value\n";


// pa an array of pointers
// auto doesn't work with list initialization
const double *(*pa[3]) (const double *, int) = {f1,f2,£3};
// but it does work for initializing to a single value
// pb a pointer to first element of pa
auto pb = pa;
// pre-C++11 can use the following code instead
// const double *(**pb) (const double *, int) = pa;
cout << "\nUsing an array of pointers to functions:\n";
cout << " Address Value\n";
cout << "\nUsing a pointer to a pointer to a function:\n";
cout << " Address Value\n";

### 第 247 页（PDF p265）

”第7章 函数二Ceh的编程模均          ye

cout_<< pb [i] fav, 3) ec rom << *pb[i] (av, 3) ec 6nd;

//-what about a pointer to-an array of function pointers
cout_<<« "\nUsing pointers te an array of pointers: \n"}
cout-<<« " Address Value\n">—
//-easy way to declare-pe
auto pe-= &pa-
//-pre-C++11 can use the following_code instead
// const double_*(*(*pe) §3]) (const double *, int) = &pa;
// hard way to declare pd
const double *(*(*pd) [3]) (const double *, int) = kpa;
//-store return value in pdb
const double * pdb = (*pd) (lLfavini +
-(/ alternative notation = coe Boe SE ase                   :   吕
return 0;


YY广some rather dull -functioris es   se         ;  a a    apes Sees

ie const..double * El({const double.* ar, int n}


return ar;


return ar+l;


const double * £3(const double-ar[], int n}
return ar+2;


该程序的输出如EE:

Using pointers to functions:
Address Value

QOO2APSEQ; 1112.3°

CO2ZAPSEG; 1542.6

Using an array of pointers-to functions:

Address
OO2AFSEO:
OO2AP9ER:
QO2ZAF9FO:

ising a.pointer ‘toa

Address

1 OO2ZAF9EO:.
OO2AFSES:
OO2AF9FO:

Using pointers te an array of pointers: ~

Value
1112.
1542.6
2227.9

pointer''to a function: . .... Sate See
Valuer
Lites

### 第 248 页（PDF p266）

a 8. eS ee Bs Se Se ee


io = OO2AF9ES: 1542.6 - gd Me one eNOS a net Se ent AE es ae, eee ee we ae ee
2O02AF9RO: 2227. oi aaa Sa ee pa ip eess

这个去例可能看起来比较深奥;  em mditest Bea eA “i. Aiea

-一=

ae    eS    =

Re wee a ape ne a ieee Ze ee


eee AoA LANA AA RIM REID Pitre

Fee

—= = const. double. “€((#pd) fal). (const, double. ee int) i= ‘spa;  he: 下98  do- tt: "yourself -    OSes Sea Le


AKA A, 编译器的角色发生了改变- 在C++98 中， 编译器种用其知识帮助您现错误，
ACHP 编译器利用其知识帮助您进行正确的声明
四 存在一个潜在的缺志。 BARMAN AR REM KD Bee ra se, ee

auto pe = *pa;   WE oa “Used. aoe instead oe ree

bik PASM pc 的类型与印#一致，在程床清单 7.19-中，后面使用它时假定其类型与点pa tee, at
导致蝙译错误。

7.10.4   使用typedef进行简化

"BR auto SF. CH还提供了其他简化声明的工具:  您可能还记得地第 5 章说过， KE TF typedef 让您能够
创建类型别名:

typedef double real; //-makes real another name for double

这里采用的方法是，将别名当做标识符进行声明，并在开拓使用关键宁 typedef. 因此，可将 p_fun声
明为程序清单 7.19 使用的函数指针类型的别名:

“typedef const double *(*p fun) (const 二 a  int);  // p fun now a type name  mt
pefun-pl = fi; // pl-points to the fii} 二

然后使用这个别名来简化代码:

一   p_fun Pa二= {f1;f2,£3};-// pa an array of 3 functfon pointers
pfun (*pd) [3] = &pap    // pd points-to an array of 3 function pointers

使用 typedef 可减少输入量，让您编写代码时不容易犯错，并让程序更容易理解。         区

7.11 dot

函数是 C++ ite. EPA, ee QA, FRU ee 函数定义是实现函数功
能的代码，函数原型描述了函数的接口: 传递给函数的值的数目和种类以及函数的返回类型。冰数调用使
得程序将参数传递给函数，并执行函数的代码。

ERR Ot 下，C++函数按值传递参数。这意味着函数定义中的形参是新的变量，它们被初始化为函
数调用质提供的值。国此，C+E困数通过使用拷见，保护了原始数据的完整性。

C++将数组名参数视为数组第一个元素的地址。丛技术上讲，这仍然是按值传递的，因为指针是原始
地年的持风:但函数将使用指针来访问诛始数组的内容。 当且仅当声明函数的形参时,- 下面两个声明才是
等价的;

### 第 249 页（PDF p267）

-RE [二7  ee : os ee a =a = 57 ley See 到 ne 二

ea cee ane Ul OR aril) BORE SAH AB OTLB AD const 指针，来保护原始数据的完整性;

eee ee ee oe 一

SF iammamminmaba, -并不会传输有关数组长度的信息， rc ae a als

aie aay ALITA OCA JE, ThA A FRNA aE ASE


5 Ghar HEED A iar AT OER HE it eee Bue
: os       GT提供大 string, gi   sf aad Ip   函数 可以接受   ‘string atime be coe sete

= 三 CHERULT 3 BER C- Pie FREI ean. crite tars EAN EAH char* -

oe  es AER RAID mi. aOR SU mACEEAM.

C++函数可以是递归的，也就是诺，函数代码中可以外括对阔数本身的调用。
C++函数名与函数地址的作用相同。通过将函数指针作为参数，可以传递要调用的函数的名称。

7.12 82>

，使用函数的3 个步骤是什么?
.请创建与下面的描述匹配的函数原型-
igor()湾有参数，且设有返回值。
.tofu(j接受一个 int 参数，并返回一个 float。
- mpg( )接受两个 double 参数，并返回一个double。 _

dsummation()将 long 数组名和数组长度作为参数=   并返回-   一 long {fi

e. doctor( )接受一个字符串参数〈不能修改该字符串)，并返回一个 double fi.

人fourse人将 boss 结构作为参数，不返回值。   —
gplot()将 map MMR SM, IREI—7 FH      eg At susie  =

3. 编写=-个接受 3 个参数的图数:- int 数组名、数组长度和一个 int 值，  并将数组的所有元素都没秆为
该-int 值。

4. 编写一个接受了个参数的函数: 指自数组区间中第-一个元素的指针、指向效组区间最后:一  个元素后
面的指针以及一个 int 值，并将数给中的每个元素都设置为该 int 值*

5编写将 double 数维名和数组长度作为参数，  APPLES ER  该函数不应修改数组
的内容。

6- 为什么不对类型为基本类型的函数参数使用 const 限定符?

7._C+H+程序可使用哪 3 种 C风格字符串格式?

= 编写一个函数，其原型如下，

int replace(char * str, char cl, char ¢2);

APR BOR SEB PLAT EK cl AERA 02, FERMI EL.

9. 表达式*"pizza"的含义是什么?_ "taco" [2]呢?

10. C++克许按值传递结构，也允许传递结构的地址。如果 glitz 是一个结构变量，如何按值传递它2-
妞何传递它的地址? 这两种方法有何利弊?

11. 函数 judge( )的返回类型为 nt，它将这样一个函数的地址作为参数: 将 const char 指针作为参数，

or ePN 一

### 第 250 页（PDF p268）

并返回一个 int 值。请编写 judge( )函数的原型。
12. 假设有如下结构声明，
struct applicant {
char name[30];
int credit_ratings [3];


a. 编写一个函数，它将 application 结构作为参数，并显示该结构的内容。

b，编写一个函数，它将 application 结构的地址作为参数，并显示该参数指向的结构的内容。

13. 假设函数人TO0和 他0O的原型如下:

void fl{applicant * a};

const char * f2(const applicant * al, const applicant * a2};

请将 pl 和 p2 分别声明为指向 fi 和 亿 的指针;将 ap 声明为一个数组，它包含 5 个类型与 pl 相同的
指针;将 pa 声明为一个指针，它指向的数组包含 10 个类型与 p2 相同的指针。使用 typedef 来帮助完成这
项工作。

7.13 ”编程练习

1，编写一个程序，不断要求用户输入两个数，直到其中的一个为0。对于每两个数，程序将使用一个
函数来计算它们的调和平均数，并将结果返回给 main( )，而后者将报告结果。调和平均数指的是倒数平均
值的倒数，计算公式如下:

调和平均数=2.0*xX#*yyCK+人内

2. 编写一个程序，要求用户输入最多 10 个高尔夫成绩，并将其存储在一个数组中。程序多许用户提
早结束输入，并在一行上显示所有成绩，  然后报告  i平均成绩。请使用 3 个数组处理函数来分别进行输入、
显示和计算平均成绩。

3. 下面是一个结构声明:

struct box


char maker [40] ;
float height;
float width;
float length;
float volume;


a，编写一个国数，按值传递 box 结构，并显示每个成员的值。

b. Oe kee 传递 box 结构的地址，并将 volume 成员设置为其他三维长度的乘积。

c，编写一个使用这两个函数的简单程序。

4.  RE al einen  在这些玩法中，玩家从
一组被称为域号码 Cfield number) 的号码中选择几个。例如，可以从域号码 1一47 中选择 5 个号码; 还可
以从第二个区间〈如 1一27) 选择一个号码〈称为特选号码)。要赢得头奖，必须正确猜中所有的号码。中
头奖的几率是选中所有域号码的几率与选中特选号码几率的乘积。例如，在这个例子中，中头奖的几率是
从 47 个号码中正确选取 5 个号码的几率与从 27 个号码中正确选择 1 个号码的几率的乘积。请修改程序清
单 7.4，以计算中得这种彩票头奖的几率。

5，定义一个递归函数，接受一个整数参数， ee 前面讲过，3 的阶乘写作 31, G+
3*21，依此类推， 而 0!被定义为 1= 通用的计算公式是-= MR ASS, WM nl=a* Cn-b) 8& 在程序中对该
“本数进行测试， eFC ‘arene  这些值的阶乘。

### 第 251 页（PDF p269）

第7章 函数一 C++的编程模块                               251

6. 编写一个程序，它使用下列函数，

Fill_array( )将一个 double 数组的名称和长度作为参数。它提示用户输入 double 值，并将这些值存储到
数组中。当数组被填满或用户输入了非数字时，输入将停止，并返回实际输入了多少个数字。

Show_array( )将一个 double 数组的名称和长度作为参数，并显示该数组的内容。

Reverse-array( )将一个 double 数组的名称和长度作为参数，并将存储在数组中的值的顺序反转。

程序将使用这些函数来填充数组，然后显示数组; 反转数组，然后显示数组，反转数组中除第一个和
最后一个元素之外的所有元素，然后显示数组。

7. 修改程序清单 7.7 中的 3 个数组处理函数，使之使用两个指针参数来表示区间。fill_array( )函数不
返回实际读取了才少个数字，而是返回一个指针，该指针指向最后被填充的位置， 其他的函数可以将该指
针作为第二个参数，以标识数据结尾。

8. 在不使用 array 类的情况下完成程序清单 7.15 所做的工作。编写两个这样的版本，

a. {#1 const char *+数组存储表示季度名称的字符串，并使用 double 数组存储开支。

b，使用 const char *数组存储表示季度名称的字符串，并使用一个结构，该结构只有一个成员
个用于存储开支的 double 数组。这种设计与使用 array 类的基本设计类似。

9. 这个练习让您编写处理数组和结构的函数。下面是程序的框架，请提供其中描述的函数，以完成该

#Hinclude <iostream>
using namespace std;
eonst int SLEN = 30;
struct student [
char fullname ([SLEN] ;
char hobby [SLEN] ;
int ooplevel;

// getinfo() has two arguments: a pointer to the first element of
// an array of student structures and an int representing the

// number of elements of the array. The function solicits and

// stores data about students. It terminates input upon filling
// the array or upon encountering a blank line for the student

// name. The function returns the actual number of array elements

int getinfo(student pal], int mn);

// displayl() takes a student structure as an argument
// and displays its contents
void displaylistudent st);

// display2() takes the address of student structure as an
// argument and displays the structure’s contents
void display2(const student * ps);

// display3() takes the address of the first element of an array
// of student structures and the number of array elements as

// arguments and displays the contents of the structures

void display3 (const student pal], int n);

int main!)
cout << “Enter class size: *;
int. class size;
Cin >> Class_size;

### 第 252 页（PDF p270）

二一24一一CAAPrimerPlus (第6版入中文版 -    -一-一              =
See 二 fot: nat te 和 有


student * ptr Su -= new student [class-size] ;
. -int-entered = getinfo(ptr stu, class_size);
for timti = 0; t-e«_entered; i1++L—
dispkayl (ptr_stu [i] };
display2 (aptr_stu[il] t;

-display3 (ptr_stu,  entered) ;.

~~ - 48 (12.9):

ee  “delete Ho ptr ~ Btu;

cout << “Done\n";

|   10. 设计一个名为 calculate )的闷数，它接受两个 double 值和一个指向函数的指针，而被指向的函数
-接受两个double 参数，并返回一个 double fi. calculate( )函数的类型也是 double，并返回被指向的函数使:
用 calculate( )的两个 double 参数计算得到的值例如，假设 add6)函数的定义如下;

doupte-add faocub1Le x, double y)


则下述代码中的函数调用将导致 calculate( 2.5 和 10.4 传递给 add( )函数，   ane tal eer

return x-+ YF

.  Subnes = i ce 5, 10.4,  :ai

清编写一个程序， 它调用上还两不函数和至少另一 一个与 add()类似的函数。该程序使用循环来让用户
成对地输入数字。对于每对数字，程序都使用 calculate( )来调用 add( )和至少一个其他的函数。如果读者爱
冒险，可以尝试创建一个指针数组，其中的指针指向 add( )样式的函数，并编写一个循环，使用这些指针
“连续让 calculate( )调用这些函数。提示: 下而是声明这种指针数组的方式 其中包含三个指针;

Er doupTe -trpf[3]j (double,  doubler; :

_ IRCA GE, ee ee  oe a a

