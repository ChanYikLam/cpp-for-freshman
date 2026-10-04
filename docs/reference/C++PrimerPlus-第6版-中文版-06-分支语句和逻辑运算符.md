# 第 6 章 分支语句和逻辑运算符

> 来源：《C++ Primer Plus（第 6 版）中文版》Stephen Prata 著，张海龙、袁国忠译，人民邮电出版社。
> 本地 PDF：`/Users/chenyilin/Desktop/电子书/计算机/C++ Primer Plus：中文版（第六版） (Stephen Prata) (z-library.sk, 1lib.sk, z-lib.sk).pdf`
> 对应 PDF 第 183–219 页 / 原书第 165–201 页。
> 转换方式：PyMuPDF 抽取原扫描件内置文本层（该 PDF 为 2013 年扫描件，内置文本层由 OCR 生成，**中文标点与少数汉字有识别错误，代码行偶有粘连**）。**本节内容的权威性以原书为准；引用技术结论前请回查 PDF 原页。**

## 6.1 本章要讲什么（原书小节结构）

  - 6.1 if语句 … 165
    - 6.1.1 ifelse语句 … 167
    - 6.1.2 格式化ifelse语句 … 168
    - 6.1.3 ifelse ifelse结构 … 169
  - 6.2 逻辑表达式 … 170
    - 6.2.1 逻辑OR运算符：‖ … 171
    - 6.2.2 逻辑AND运算符：＆＆ … 172
    - 6.2.3 用＆＆来设置取值范围 … 174
    - 6.2.4 逻辑NOT运算符：！ … 175
    - 6.2.5 逻辑运算符细节 … 176
    - 6.2.6 其他表示方式 … 177
  - 6.3 字符函数库cctype … 177
  - 6.4 ？：运算符 … 179
  - 6.5 switch语句 … 180
    - 6.5.1 将枚举量用作标签 … 183
    - 6.5.2 switch和ifelse … 184
  - 6.6 break和continue语句 … 185
  - 6.7 读取数字的循环 … 187
  - 6.8 简单文件输入／输出 … 190
    - 6.8.1 文本I/O和文本文件 … 190
    - 6.8.2 写入到文本文件中 … 191
    - 6.8.3 读取文本文件 … 194
  - 6.9 总结 … 197
  - 6.10 复习题 … 198
  - 6.11 编程练习 … 199

---

## 正文

### 第 165 页

第6章分支语旬和逻辑运算符

本章内容包括:

• if i吾句。

```cpp
• ifelse i吾句。
```

• 逻辑运算符:&& 、11和! 。

• cctype字符函数库。

• 条件运算符:?: 。

```cpp
• switch i吾句。
```

• continue和break语句。

• 读取数字的循环。

• 基本文件输入/输出。

设计智能程序的一个关键是使程序具有决策能力。第51在介绍了一种决策方式一一乓盾环，布循环中，程序决定是否继续循环。现在，来研究一下C++是如何使用分支语句在可~拌的操作中做出决定的。程序应使用哪一种防止吸血鬼的方案(大蒜还是十字架〉呢?用户地择了哪个菜单洛项呢?用户是否输入了。?C++提供了if 和switch语句米进行决策，它们是本擎的主姿主题。另外，j&将介绍条件运算符和逻辑运算符，前在提供了另←种决策方式，而后者允许将两个测试组合在一起。故后，本最将首次介绍文件输入/输出。

## 6.1 if 语句

当C++程序必须决定是否执行某个操作时，通常使用if 雨‘句来实现边拣.if 有两种格式:if和ifelse.首先看一看简单的i巳毛’模仿英语，如“lfyou have a Captain Cookie card, you get a丘ee cookie (如果您有一张CaptainCook ie卡，就可获得免费的小甜饼〉飞如果测试条件为true，则if语句将引导程序执行语句戎语句块:如果条件是fal钮，程序将跳过这条语句或语句块。因此，if 语句让程序能够决定是否应执行特定的语句.

if语句的语法与while相似:

```cpp
if (test-condition)
st acement
```

如果tcst-condition(测试条件〉为true.则程序将执行stalement( 语句).盯着‘ 既可以是一条语句，也可以是语句块.如果测试条件为false，则程序将跳过语句〈参见图6.1)。和循环测试条件一样.if 测试条件也将被强制辛苦铁为bool值，因此O将被转换为fal se.非零为true 。郭个if 语句被视为一条语句。

通常情况下，测试条件那是关系表达式，如那些用来控制循环的表达式。例如，假设读者希望程序计算输入中的空格数和字符总数，则旬以在whi le循环中使用cin.get(char)来读取字符，然后使用if语句识

### 第 166 页

别空格字符并计算其总数。程序清单6 .1完成了这项工作，它使用句点(.)来确定句子的结尾.

阳

咀

阳

阁6.1if 语句的结构

程序清单6.1if.cpp

```cpp
11 if.cpp --using the if statement
掉incl ude<iost ream>
int ma in()
uu .••. nn dd ..cc .. nu ,,, ,,, u s n n3 -q e c a r a •. n s
```

、.

..

龟q&、A，A、

卢眼3nd『ω‘】.、、.&.，争., 、、‘。

‘、内e.a、。.’怡

3@、

```cpp
char 巳ch; 」
int spaces = 0;
int total = 0;
cin.get (ch) ;
while (ch != '. ') 11 quit at end of sentence
i f (ch == ' ') /1 check if ch is a space
+...spaceSi
++total; /1 done every time
c in.get(ch) ;
cout <;<; spaces << " spaces , ,. << total;
cout << • characters total in sentence\n" ;
return 0;
```

下而是该程序，的输出:

```cpp
The balloonist was an airhead
with lofty goals.
6 spaces , 46 çharacters total in sentence
```

### 第 167 页

正如程t:r.中的注释指出的，仅当ch为空格盹，- 1;蕃司样spãces;才被执手~-囱办语飞侍忡tota;位于ii 语句的州、外面，由比在每轮循环中都将被执行.在悉，字符总数中包括按回车键生成‘的换行符.

6.，:于毛1‘if“else语旬:-:-.._:._::... ...:-=、斗f 语赁让程序t)t1È，是否执在持定的、语-ff)或语龟块._-而i(el_s~语句则让程序:决定执行两条蜓句或语句一-扩H-块赏的哪-条，这种在句对于:选择其中二种操作很在且-;;:-C *1的山区畜苟模仿了简单丽英语二如~-~lfyo马二-_fïäÿe }i :çijþtäin -CQQ1ge car.d，;功b忌et-aCöòkie ,P!us Plus. dse-yoU:jii侨民t--aTòókïe d'Ordjnaire -CJ4l果您拥有=>-:-~--<&俨i豆é60k ie 长-将海军￡得toOkienusP}USJ否则只能获得C∞kië’d!Oi-di;‘-;ir~S飞ifèl~e节句的通用楠、了-. ~ .. :~~;_~.’二王号如下.-;.-:.~ .._,..;: -‘~二、气;二?二-、-二...二，-: - .、…、:_-:--:rt __Îtest-condiÚön)七飞-、?与:_st瓦telll~l) q,

.

“~ 一千一-二二飞-:e”l一së -_ ‘ .,. . - ’ .-、.-,,:..,-- . .:-.-.,.. ‘.’ 二__...、..、、- ~-‘:’“.. _.

sta-te咽ent2-，主二ζ二、·二‘巴如果测试条;能为由己或司悍，则程序;每执行咆temënO二-Jljt过$I<l_t~~en比如果测试条鲜为售后:(;#11_: 二之二ζ二三注二则程应将鼠目主t ~tl!teme~t ~ :执行主t~ti~~F:’困i1t“，-如果-是iis~;吃搓1~92i~Df盯丽的伏码片段lι将打闯第二二条二.-;_~-:”“-.;.:;.R 二三面主甜ú#tjï‘j呆在信ι工二- t...-:二二’三三ζ-二三江二;二二::-z tf:-7... ._~_..::飞-=.:...:、生f.l añ占wer正=-1492)、?γ，主=叩-‘”’;‘_’. . “-气τ二..~二~二.∞u泣i仨T支<<”，.~‘咐.’Th咀a扛.t.~浮￥正ii.均-司T肚1让t!可O白?江ì“!t.

eise --‘:’仨一…“.‘-:: γ -=”... ;:;.且~.: ..:..J...吹芝 ，.:• .~. 飞.. ::~...， 7飞-’. ,:. •• -. -.“. ~‘.--φ 俨-飞--主~...二~气.~-...:::号气Et?三~’You'd 快ETerrgi叩”Ch~~主r‘~: again 二、i1’-:;:.- --ι二每条语句部.齿iJ峡γ条1在句耐坠是阁‘大时理函语dkr以画~;2’)~阿拉函，整个Epk飞;二二.“~:-”:‘结构被括为一条语·负10---: -----’ -- ---_ -__- ::--;_ ~ 一

- - -..' _. -.--:. _--

.;...;; ___.__ø...γ甸ι--_、---，-『‘二-自一--一一_.,. _‘ .. ‘ . -、.._“’:_---、--..一...国民、…---、，-_.__.‘”…一一---一甲、…一一一--，一…·←、-~ _..~-...-. -品

、

--

. .,.，...,一‘ . -^

--‘". _, -:.. •

-_... _. _._.._,_ ... ---‘--., -'…... _.._.---_.. -

..,..._, -，、...，'_..-、。、-

. . ... _..“，、丰、τ=-_-‘-:;

. . :. ':

, 、

、

-

-…

.'.--、

--悔钮也已- -... -ι ‘“ -... -一一一...:.. .. 、._-ø<;. __- _ --ι..i.._-_

---、..…..._... ._ ..

-

‘_.‘ ._一…_..,-

…--

‘一一-一、

,,_ '': " '"' -、..-..

--_ 页、-、二‘，..‘、-牛鱼.- =-.-._--:’;..:、-:、一:; - -.复之巳-_-一_ 飞_‘-:‘-- • .::. 飞 .:’

--

_-一_.、4‘二-~ 可._...~.ζ:‘_._.-、- _-、’...:-何...:=_:;;:.‘.、’=..._τ飞--,.,..._Tι::-_:- --•... ... _!‘，“: 旦-_-• .;. ”、-. . ’“ _‘, 、-~ 一 .-- -句~ .. 。-_. • .-一吧’.‘---.;’” -‘“ ~

d、-~ ，.'-、-

-_..._.. ..__..._.,- --_ -.._..__...'. .. ., ._-...

、，ι、、…

.. ._.“ τ古民手言:_... 、::，...‘;..;、...:比-

• ,-. 7 ,;:C“. _ -,. ~.，

'.-'. , .-:''':'、'A.:::-_ -

.一...

-图6.ZJzfg牛语旬的给.拘“.::”吧- -7TY止，:.. .. _二‘二、二咙=二二例虫lh:~假设要通迂对字母进行到密撬码来语班输入的交木、，(抉有符不变Lj主样f;需;寄:输拦至于都被转~;:二主、士、干‘、为ι行输出向?仁-丰阜肚长草庚刚E楼乖变丸@二这精i意株靠瞅吹峭着程序对1塾些蚓4抒俯?珩符粱棚眉三种t缺附埃附作，洞对耳.艾向弛字符采丹脾翩手踢易二专飞刑科制阶￥仨仨仁.、飞jÈ豆逅如稳i与ν1于子、二’:、-二L二才. :::扣‘-气’ .，.‘三z的辛毯主代品之-元-- 二?=.二二忑e飞二_.--:...:工二-厅--

### 第 168 页

程F整清单6.2ifelse.cpp

```cpp
fI ife}:se-τcpp - -us.ing the if e15e sta tement
#incl ude <士。stream>
int marn-( )
char ch;
atd: :c∞t << "Tÿþe ‘and 1 5haU repeat. \n";
std: :cin..ge't Îch);
wllíle (ch 1 =俨~I)
```

if (ch == ‘\ n俨}

```cpp
std:均由~t<'< ch; ; ;':::done irnewUne
el'se
```

stct: ,cout <<++ch; /厂也neother、也e

```cpp
stc!TTëin.geE"(ch) ;
/1 try ch + 1 instead of ++ch f百rinterestin旦effect
std: ~cout << tI飞nPleaseexcuse the slight confus1on, \ n
/户- std::cin_get tt;,
1I std: :cin.get ();
```

.. -_ :- -retU1;‘n 0; -_~ ---~.~飞J--:_;::.. ,..“”_- . -.:-’--_ _-_ -_::“‘”_; ’:‘~’_:: - -:‘::::=.--:..--’“ -.二…J雪‘.←~ζ;”、--- 气~-吃-----“、h乞~-.:-;:;:., --...气”_-_--.. _... 之.’-;~.---_~-;_::‘-_’乞弓之.:_ _-.,_--. :---;，._“‘:”ι二-可~-~---.;;-=-ζ -‘二’,‘ 二飞-_=.-_;..:-一’飞‘ 子_-__/~::: “C:-=-电:,.. ~弓汇J三: -J-~J-飞三三ιι- 于予圭-、气’;‘-._-二工旦飞;.. -_亏￥E巳---.-二r二〉豆工‘飞气、主L二二--二-.--~1宅芒三三三:兰~….二于子士τ 亏二’.-户-~-_-”‘产-二=士二.:_.~二←飞ι‘工二二二二二ι主二_=::- _-.’ Tηÿpe， . añd -1 shaÌ1 -repeã-t:

An.. inef饪fa抽blej 。句y盹s‘uf饪fused皿酣e，as Lbeheld

B~!iofggbcmf!kp2!tvggvtfe!nf!ötrJ!cfifme

the wonders 0合皿。derncα皿puting_

```cpp
的臼xpoefst!pg!npe fsoldpnqvujoh
Pl ease excuse the:: slight confusion _
```

注意，程序清单6.2中的注释之一指出，将忡ch改为ch+1将产生一种有趣的效果.能推断出它是什么I吗?如果不能，就试验一下，然后看看是否可以解释发生的情况〈提示:想一想cout是如何处理不同的类型的).

### 6.1.2 格式化ifelse语旬

if else中的两种操作都必须是一条语句。如果需要多条词句，需要用大括号将它们括起来，组成一个块语句.和有些语言〈如BASIC和FORTRAN)不同的是，由于C++不会自动将i f 和else之间的所有代码视为一个代码块，因此必须使用大括号·将这些话句组合成一个ì-1‘t句块.例如1.下面的代码将出现编译器错误:

i:f fëh :.且‘Z俨γ

```cpp
zorro++ ;-/ I it ends here
cout << '‘Another Zorro candidate飞n";...
else I1 wrong
dullu;
cout. << "Not a Zorro cand idate飞n";
```

.编译苦苦把它看你是一条以zoπOHi语勾结尾的简单in百旬，接二F来是一条∞ut_语句.到目前为止，一饥度常.但之历编译器发现一个独立的else.这被视为语法错误寸

消添加λ;店号，将语句组合成二才诺句块:

一-...…. ~一.

### 第 169 页

```cpp
if (ch == 'Z ' )
// if true block
zorro+φ，
cout << "Another Zorro candidate\n";
else
// if false block
dull++;
cout << "Not a Zorro candidate\n";
```

由于C++是自由格式语言，因此只要使用大括号将语句括起，对大报号的位置没有任何限制.上述代码演示了一种流行的格式，下面是另一种流行的格式:

```cpp
if (ch == ,z,) {
zorro++;
cout << "Another Zorro candidate\n";
else {
dull++ ;
c。旧时"Nota Zorro candidate\n";
```

第一种格式强调的是语旬的块结构，第二种格式则将语句块与关键字if和e lsc更紧密地综合在一起.这两种风格清晰、一致，应该能够满足要求:然而，可能会有老师或庭主在这个问题上的观点强硬而固执。

```cpp
6.1.3 íf e lse if else结构
```

与实际生活中发生的情况类似，计算机程序也可能提供两个以上的选择.可以将C++的ife l se语句进行扩展来满足这种需求。正如读者知道的，elsc之后应是一条语句，也可以是语句块.由于ifelse 语句本身是一条语旬，所以可以放在else的后而2

```cpp
if (ch == 'A')
a_gradeφ 令J// alternative # 1
else
if (ch == 'B' ) /1 alternat ive # 2
b_grade++; /1 subalternative辑2a
else
8050++; /1 subalternative # 2b
```

如果ch不是‘A’，则程序将执行clsc.执行到那里，另一个if else又提供了两种选择.C忡的自由格式允许将这些元素排列成便于阅读的格式:

if (ch ==且‘)

```cpp
a_grade++; // alternative掉1
else if (ch == 'B')
b_grade+令J// alternative排2
e1ge
9090+φ， 1/ alternative曾3
```

这看上去像是一个新的控制结构一一ifelse if else结构.但实际上，它只是一个ifelse被包含在另一个if else中.修订后的格式更为清晰，使程序员通过浏览代码便能确定不同的选择.整个构造仍被视为一条语句。

程序消单6.3使用这种格式创建了一个小型测验程序。

### 第 170 页

程序清单6.3ifelseif.cpp

```cpp
11 i felseif.cpp --using if else if else
样include<iostream>
const int Fave = 27;
int main{)
{
using namespace std;
int n;
cout << "Enter a number in the range 1-100 to find ";
cout << "my favori te number : ";
```

do

```cpp
{
Cln >> n;
if (n < Fave)
cout << "Too 10'" - -guess again: ";
e1se i f (n > Fave)
cout << "TOO hi gh - -guess again: ";
else
cout << pave <;< " is right 1 \n 11 ;
} while (n != Fave);
return 0;
```

下面是该程序的输出:

```cpp
Enter a number in the range 1-100 to find my favorite number: SO
Too high --gues9 again: 25
Too 10w --guess agai口37
Too high --guess again: 31
Too high --guess aga in: 28
Too high --guess again: 27
27 i s right!
```

条件运篡符和错误防范

许多程序员将更直观的表达式variable = =value 反转为value = =variable ，以此来捕获将相等运算符误写为赋佳运算符的错误。例如.下述条件有效，可以正常工作:

```cpp
if (3 == myNumber)
```

但如果错误地使用下面的条件，编译2将生A错误消息，因为它以为程序员试图将一个值赋给一个字画佳(3总是等于3 ，而不能将另一个位赋给它):

```cpp
if (3 = myNumber)
```

假设犯了类似的错误，但使用的是箭一种表示方法:

```cpp
if (myNumber = 3)
```

编译器将只是把3赋给myNumber ，而if中的语句块将包含非常常见的、而又非常难以发现的错误(然而，很多编译s会发出警告，因此注意警告是明智的)。一般来说，编写让编译器能够发现错误的代码，比找出导致难以理解的错误的原因要容易得多。

## 6.2 逻辑表达式

经常需要测试多种条件.例如，字符要是小写，其值就必须大子或等子‘a’ ，且小于或等于Z。如果要求用户使用y或n进行响应，则希望用户无论输入大写( y和N)或小写都可以。为满足这种需要，C++提供了3种逻辑运算符，来组合成修改已有的表达式。这些运算符分别是逻辑OR(11) 、逻辑AND( &&)

### 第 171 页

和逻辑NOT(!).下面介绍这些运算符.

6.2.1 逻辐OR 运算符:11

在英语中，当两个条件中有一个或全部满足某个要求时，可以用单词。r 来指明这种情况。例如，如果您或您的配偶在MegaM icro公司工作，您就可以参加M鸣曲1icro公司的野餐会.C++可以采用逻辑OR 运算符(11)，将两个表达式组合在一起.如果原来表达式中的任何一个或全部部为true(或非零)，则得到的表达式的值为true;否则，表达式的值为false.下丽是一些例子2

```cpp
5 == 5 11 5 == 9 // true because first expression is true
5 > 3 11 5 > 10 // true because first expression is true
5 > 8 11 5 < 10 // true because second expression is true
5 < 8 11 5 > 2 // true because both expressions are true
5 > 8 11 5 < 2 // false because both expressions are false
```

由于11的优先级比关系运算符低，因此不需要在这些表达式中使用括号。表6.1总结了川的工作原理。

C++规定.11运算符是个l顺序点(sequencepoint ).也是说，先修改左侧的值，再对右侧的值进行判定(C忡11的说法是，运算符左边的子表达式先于右边的子表达式)。例如，请看下面的表达式:

i++ < 61Ii== j

假设i原来的值为10.则在对i和j进行比较肘.i的{且将为11.另外，如果左侧的表达式为true.则C++将不会去判定右侧的表达式，因为只要一个表达式为true，则整个逻辑表达式为true (读者可能还记得，冒号和逗号运算符也是顺序点〉。

程序消单6.4在一条if语句中使用11运算符来检盒某个字符的大写或小写。另外，它还使用了C忡字符净的拼接特性〈参见第4章〉将一个字符南分布在3行中。

表6.111运算符

```cpp
expr I 11 expr2 ir<J值
expr I = = true exprl = = false
```

expr2 = =町uetrue true expr2 = = false true false

程序清单6 .4or.cpp

```cpp
// or.cpp - -using the logical OR operator
#include <iostream>
int main (1
using namespace std;
cout << "Thi s program may reformat your hard disk\n"
"and destroy all your data. \n"
"00 you wish to continue? <y/n> ";
char ch;
cin >> éh;
if (ch == 'y' 11 ch == 'Y ') // y or Y
cout<< . You were warned!\a\a\n";
else if (ch == 'n' 11 ch == 'N' l // n or N
cout << .A wi se choice ... bye\n" ;
else
cout << "That wasn ' t a y or n! Apparent ly you "
"can ' t follow\ninstructions , 80 "
"1 '11 trash your disk anyway.飞a\a\a\n" ;
return 0;
```

### 第 172 页

该程序不会带来任何威胁，下面是其运行情况:

```cpp
Thi s program may reformat your hard disk
and destroy a11 your data .
00 you wish to continue? <y!n> N
A wige choice .. bye
```

由于程序只读取一个字符，因此只读取响应的第一个字符。这忿味着用户可以用NO!(而不是N)进行回答，程序将只读取N。然而，如果程序后面再读取输入时，将从O开始读取。

### 6.2.2 逻辅AND运算符:&&

逻槐AND 运算符(&&)，也是将两个表达式组合成一个表达式。仅当原来的两个表达式都为true时，得到的表达式的值才为true。下面是一些例子:

```cpp
5 == 5 && 4 == 4 / / true because both expressions are true
5 ~. 3 && 4 ~. 4 // false because first expression is fa1se
5 > 3 && 5 > 10 // false because second expression is fa l se
5 >自&&5 < 10 // false because first expression i9 false
5 <自&品5> 2 // true because both expressi ons are true
5 > 8 && 5 < 2 // fa l se because both expressi ons are fa l se
```

由于&&的优先级低于关系运算符，因此不必在这些表达式中使用括号.和11运算符一样.&&运算符也是)1阪Ff点，因此将首先判定左侧，并且在右侧被判定之前产生所有的副作用.如果左侧为false，则整个逻辑表达式必定为false.在这种情况下.C++将不会再对右侧进行判定.表6.2总结了&&运算符的工作方武.

表6.2&&运，事符

```cpp
e"pr 1 && e><pr2的也
exprl = = true expr 1 = = false
```

e><pr2 = = true 位uefalse e><pr2 --false false 也lse

程序消且在6.5演示了如何用&&来处理一种常见的情况一一由于两种不同的原因而结束whilc循环。在这个程序清单中，一个while循环将值读入到数组.一个测试(i<ArSize )在数组被填满时循环结束，另一个测试( temp>=O)让用户通过输入一个负值来提前结束循环.该程序使用&&运算符将两个测试组合成一个条件.该程序还使用了两条if语句、一条ifelse语句和一个for 循环，因此它演示了本章和第5章的多个主题.

程序清单6.5and.cpp

```cpp
// and.cpp --using the l ogical AND operator
曾include<iostream>
const int ArSize = 6;
i nt main{)
using namespace s t d;
float naaq(ArSize] ;
cout << "Enter the NAAQs (New Age Awareness Quotients) "
<< "of\nyour neighbors. program terminates "
<< "when you make\ nJl << ArSi2e << 11 entr立es11
<< "or enter a negative value . \n" i
int i = 0;
f10at temp;
cout << "First value: 11 j
```

### 第 173 页

```cpp
cin >> temp;
while (i < ArSize && temp >= 0) // 2 quitting criteria
naaq(i] • temp;
```

...1;

```cpp
if (i < ArSize) // room l eft in the array,
cout << "Next val ue: 11;
cin >> temp; // 5 0 get next val ue
if (i == 0)
cout << "No data- -bye\n";
else
cout << "Enter your NAAQ: ";
float you;
Cl n >> you;
int count = 0;
for (int j = 0; j < i; j H)
if (naaqljl > youl
+-tcountj
cout << counti
cout << " of your neighbors have greater a wareness of\n"
<< "the New Age than you do. \n";
return 0;
```

注意，该程序，将输入放在临时变盘temp中。在核实输入有效后，程序才将这个值赋给数组.

下面是该程序的两次运行情况.一次在输入6个值后结束:

```cpp
Ente r the NAAQs (New Age Awareness Quotients) of
your ne ighbors . Program terminates when you make
6 entr工esor enter a negative value .
First value : 28
Next value: 72
Next value : 15
Next value : 6
Next value: 130
Next val ue : 145
8nter your NAAQ: 50
3 of your neighbors have greater awareness of
the New Age than you do.
```

另一次在输入负值后结束:

```cpp
Enter t he NAAQs (New Age Awareness Quoti ents) of
your neighbors. program terminates when you make
6 entries or ent er a negative val ue
.irst value: 123
Next value: 119
Next value : 4
Next value : 89
Next value : - 1
Enter your NAAQ: 123.031
。ofyour neighbors have greater awareness of
the New Age than you do.
```

### 第 174 页

程序说明

来看看该程序的输入部分:

```cpp
cin >> temp;
while (i < ArSi ze && temp ~= 0) 11 2 quitting criteria
naaq(i] = temp;
++1;
if (i < ArSize) 11 room left in the array,
cout << "Next value: It ;
cin >> temp; 11 50 get next value
```

该程序首先将第一个输入值读入到临时变量( temp)中.然后，while测试条件查看数组中是否还有空间(i<ArSize)以及输入值是否为非负(temp>=O)。如果满足条件，则将temp的值复制到数组中，并将数组索引力U1.此时，由于数组下标从0开始，因此i 指示输入了多少个值。也是说，如果i从0开始，则第一轮循环将一个值赋给naaq[O] ，然后将i设置为1.

当数组被填满或用户输入了负值时，循环将结束.注意，仅当i小于ArSize时，即数组中还有空间时，循环才将另外一个值读入剑temp中.

获得数据后，如果没有输入任何数据〈即第一次输入的是一个负数)，程序将使用ifelse 语句指出这一点，如果存在数据，就对数据进行处理.

### 6.2.3 用&&来设置取值范围

&&运算符还允许建立一系列ifelse if else语句，其中每种选择都对应于一个特定的取值范围.程序清单6.6演示了这种方法。另外，它还演示了一种用于处理一系列消息的技术.与char指针变最可以通过指向一个字符串的开始位置来标识该字符*一样，char指针数组也可以标识一系列字符串，只要将每一个字符峭的地址赋给各个数组元素即可。程序，清单6.6使用quali命数组来存储4个字符串的地址，例如，qualify[ 1]存储字符唱“ mudtug-o仨war\n”的地址.然后，程序便能够将eout、由len( )或stremp( )用于quali命[汀，就像用于其他字符扇指针一样。使用const限定符可以避免无意间修改这些字符tI:l.

程序清单6.6more_and.cpp

```cpp
11 more_and.cpp --us ing the logical AND operator
掉inc lude<孔。stream>
con5t char • qualify l4] = 11 an array of pointer5
1/ t o str ings
"10. QOQ-meter race. \ n".
"mud tug-of-war.\n" ,
"masters canoe j oust ing. \n" ,
"pie-throwing festival.\n"
int main ()
using namespace std;
int age;
cout << "Enter your age in years: ";
cl nt >ae qdx AL--
.
```

立、，nAu ,

、牛

n

```cpp
l agn alvAU >tga mwe as <5 )
、&豆6i e x、A『，nv , a，似「。
```

2

### 第 175 页

> ［本页文本层 OCR 严重损坏（该页扫描阴影/插图区产生了大量乱码字符），以下为原始抽取结果（未删改），内容以 PDF 第 193 页图像为准］

宇十

二

树J

F-t…

叮J

…uE

JJ十

z

J

LW

I

-

J

-J一飞…一一k一L…一

一…

时

f

二

--二

午一

三}f…

'

叶一

一

…

F川

平

伸

-

呼

…

"

J

1r:…

Jr

一

-u

-

沪

V

二

…

f

…J

叮

-二

f

-J

二

EPJ、du

u

…二

吗

二

…

-

J

't

一

J

?

元

r2:

二…二…二

牛4

UJa

--

-L

J

牛

一三-

J

-

~二

"

丑

，

户

r

…?…

~

十

1川

ιrJ一

二

丁

…

之…I

十…

叮

J

r

-

…

f-丁

毗一-

-r

f

-

tν十l

-

f

十

，…

-

Jf

t二

二

-

-

u

斗

二…

--

uE一-

J

，

二一牛

L

v

-

~

二

f~…

I

汁

飞吵ιJy

山二-

…g二卢

叫…

~

元l…C…

十

-t二Jh

r

…

斗

…

a

『1UJUVγ川-j【二h川IU

l江J十-俨…

…

-wu一?『

vJ

…

n二-

M二川h

d-

γ

，

T

川

二

-f

TJ

u…

十f

)

y1←T

寸牛

悦

u二-J‘

…Z

叽

JK二

汪zT

-

二

r二

J

-J…

r川J

F

m

斗

斗二

t

二E一夺ι品J\

t

汪

3

Y兰旦二b

二

…

牛T

-}￥…

市

ιU二U，

干

ttL

川

飞

川

…-…川『

叫r

一

℃二艳J-…

三

u

u

L三$V飞

古

出

川干

二r-M吱…

打，

…

吨陋ν二

部

二

…川

-

二\J二

一

程白近:

棋

.

争阳

、f…

阳

叫

二U、二工飞、K…

啡

.

-的、…二括￡大u

十

8

拼

叫

在山

的

m

f

J

·

二二

γ

川

…

吨

·ω配

一

~何川

川

u，

优

乙

?付夜占9豆岁

一

沁三

州

二响

二跚

协

巳

'隙

-U、“二巩二〉祀夕

搏川

咿费

一

十

-

州

叫

川

…

…

以、

JJ-铲

u町

v

只…跚固祀妇

二

二

二嗣

U

E~

j

崎-…二-二

旦)瓦-时恻--文

财

矶地

…

f-…

巧

吨

W

巳t

…刊‘“U

v

…h』兰…

机

…呼r

吨…

昂

'-J

。

…运川…人

…测

向

二舱--E川三

…

山~

…-

-

'、

爪拉

…

川

侃、t二

K一

…

取

那…

系

的

，

U

中

u拉品

~

、崎J人二‘

晤

U巧弘

川

邵

~二

y

…五I…

刷

‘…马气

M

VtJJ-，飞

~

…

咱

哇m-

J

J

r时

.川

‘不m川f如

川

e

…

Mf兰牛

问J三二

工←

时

…

;

ift

u

-，d

蝉

-7

-十~

u

…

叫

)n

品

u

U

叶

k二

二L附叫f-气-f二

-

-~

豆

M以

-…

γ

编丁

山

二

-

一

h另民也结二-运式

…

u附~、J

叫叫

-义-二

f

…

UEe

Z豆十

二

叩

~

叫

，

阳

-

郎

时

J

叫

…，苔

S

…

·过

二-

何

叫ι

山

Jf

阳

f~

d

--

Y

…十

t

二

但~农-

…J

-

…y

"um

和

二

γy三

二

?类

-川叫

…

~布I3

…

二

f

平二

千

-川

-衍

f

?

Mk二

-二

…

、…

川u

…

时…

-pI二

M

问f

~

二

川

二树…IK州干:

时

川

-

川

时

o

向

f-U、、

…十

一

uL

L

u-二J

二

二

二

-

，

叫

可

:ι

斗二

h“一lu-二

-

穹-1々

-

?

:--U;

-

---

二-

…

Jt

什

…

J十

牛U-F--Y

f

如

η

协

叮

臼…阳果…

千

t号面--K牛J‘

叫

A

…

郎4

…

州j

…

时叫

准JL

-二A

~慰

川

，王

吵恤

阳m

t

茸

m-f♂

一

r一

二

-

…

←也通》工

J~

十表MJ--

1

可

J-←

τ?

一

M

-

捕

λ二r

州

---

-

YY矿

…

~子

二一

J

『

，

-

J

只前

胃

气-f

一引

…已

i

-

J月M

七

气

二

J

…

吵

~-飞←

茹E卢

泉C乓

苦

1有

刷7

n

哪

凡

-

W

守

十

可-细呼

万

叫…

7

ι

-

…

字铲

然叫rM，斗

ι

符v

茸

副-肌

号

川Y

…

J

二

M

口

乞F

明…

…

叫叫

{

…

-·

泣

同

r艺

\

-

y

导卫工毛“

注…叫“

J=

I

扩…

树

-J

返ι

=

:二

…一

归

三

二

果飞矿

咖

~干窒h二f-如

二

-江

九

A

h…一

工咐声M个旷

一

-洁后比

二

问-

-

…

川

r二二

，

川川

…飞

Z笃W

问

户

叫

Ez

JM-

u树

U

-

M

-汇v

t

十

-乙…

黯

U

啡

在川f阳4.

九

t，

程旦M他门

h

可

E

叫

栅垃

f♂

M兰

Jv-

门

…

…

AJ

…-二

-

--d飞-三了-

…

f

…

u

ρ

…二d甩

C

E

·h

mJ-

二

时

川brm…JU…r二

r

u

二

程ι二

桶

二

…

…

…

F

J

十刷r毗

飞

\

卫h，

V

-JJuu

二

~-二

二

二

信

-步

V

…

:-之二

一白

H

则--飞

七否

J-

叫

r

h

一

三e

二

品

M…「v

十

二

-

4

斗

、

川和川

t

-守『v-几WJ

气

十叫川

，

K

梢

-…

-兰

?

哇…飞

E

‘-川-

一

二f

『，-

-t

J~J

仰

…

v

W

…

叫-h

十

r

?

三

Eu

…

q…

内

…

户

### 第 176 页

on ·I‘@ u hu vi e

』肉-n 、

a 司A‘。

dP町

民

l、.-、

墨

```cpp
山u9ing namespace 9td,
doubl:'e ntlm;
cout << "Yo, dude! Enter an integer value: ";
C工n>> numi
while (!i9 int(num)) 1/ continue whi le num is not int-able
cout << "Out of range --please try again: ";
Cln >> num;
int val ~ int (num); 1/ type cast
cout << "You 've ent ered the integer " << val << "\nBye\n";
return 0;
bool is int(double x)
i f (x <= INT MAX && x >= INT MIN) /1 use climits values
return true;
else
retur百false;
```

下面是该程序在10t占32位的系统上的运行情况:

```cpp
YO , dude! Bnter an integer value: 6234128679
Out of range - -please try again: -8000222333
Out of range --please try again: 99999
You ' ve entered the integer 99999
Bye
```

程序说明

如果给读取int值的程序输入一个过大的值，很多C++实现只是将这个值截短为合适的大小，并不会通知丢失了数据.程序消单6.7中的程序，避免了这样的问题，它首先将可能的int值作为double值来读取.double类型的精度足以存储典型的int 值，且取值范倒更大.另一种选择是，使用longlong 来存储输入的值.I天| 为其取值范围比int大。

布尔函数is_int( )使用了climits 文件〈第3宰讨论过〉中定义的两个符号常蠢C INT_MA.X和剧T_M.剧〉来确定其参数是否位于适当的范围内。如果是，该函数将返回true.否则返回位lse.

main( )程序使用while循环来拒绝无效输入，直到用户输入有效的值为止。可以在输入超出取值范围时显示int的界限，这样程序将更为友好。确认输入有效后，程序将其赋给一个int 变量.

### 6.2.5 逻辐运算符缩节

正如本意前丽指出的，C++逻辑OR 和逻辑AND 运算符的优先级都低于关系运算符。这意味着下丽的表达式

x > 5 && x < 10

将被解释为:

(x > 5) && (x < 10)

另一方丽.!运算符的优先级高于所有的关系运算符和算术运算符。因此，要对表达式求反，必须用括号将其括起，如下所示:

### 第 177 页

```cpp
! (x > S) 11 is it false that x is greater than 5
!x > S 11 is !x greater than 5
```

第二个表达式总是为false ，因为!x的值只能为true或false ，而它们将被转换为l或o.

逻辑M也运算符他优先级高于逻辑OR 运算符。因此，表达式z

age- ,.-30-&& age口45I1崎ight> 300

被候释为:

(age > 30 && age < 45[_tl-we句h t:> 30

也是说了τ个条佟是age位于3 1 -4~好一个条件是we胆大子300.如果这荫个条件中的一个或全部和~办true，则‘在命表达式为true ~

当然，还可以甩括号将所希望的解释供诉程序。例如，假设要用于&&将鸣E大于50- 亘x:.wcight大于300‘的条件.tJdonation-大于1000的条件组合在一起，贝!J必须使用括号将OR部分拖走ç:

(age > SO 11 wefght > 300)ωdonãtion > 1000

否j)_~r.==‘编i辛苦苦将把w巳ight条111’写-donation象你(Illï不足age.条件〉组合征一起。

虽然三C++运算符-的优先级规贝l好臼I能不使用括号便可以编主导复:合比较的话坷，但最简单的方法应是用括号将耻试进行处组，而毛管:1是否需要报章。这样代码容纺阅读F 避免读者·歪着不部使妇1ft-}优先纵队! 则，并减少，1]:.:于没有准确记住所使矫凶甘规则mr出错的可能性..

C++确oc程序从丘向右进行计算逻辑表达式，)t在知道答案屉立刻停止。例如l，_假设有下面的条件」

x !~ ITω1. 0 1 x > roreo

如果第一个条件丸fålsc ，则整个表总式肯定丸fa!sc 。这是因为要使整个表达式丸阳c ，每个条件都必须约true .知道第一个条件为false后「程序将;;fS判定第二个条件.这个例子非常幸运，肉为计算第二个条件将导致被O除，这是计算机没有定文的操作。

6. 2“.6-其他表示亢式

并不;Ilk所有的键盘都提供子用作逻辑运算符的符号，肉此C++标准键供了另一种表示方式，如表6.3所示』标识符and 、0. 和Rot都是C+丰保留雯，这意咪着不能挽它们用作变最名缚。它们不是关键雯，阳为它们都是已在语言特性的另一种表示方式飞另外L它们芥不是C语言中的保留宅，但C语言程序可快将‘B.i门用作运算稚，只要在程穿中包含王头文钟iso646-.儿C扑不妥求使用头文件.一一一号子一一一←

另_.种表态方式

四d

。r

not

## 6.3 ~符~数库cctype

C忡从C谣言继承了一个与字符相关的、非常方便的局数轶件包，它可以简化i者如l确定字符是否为大写字卡~ ~ 数“‘7-、标点街号等工作F这些民数的原签定在头文件∞tyru:(老式的风格中为c纱pe:的中定义~(r.J.例如1 -如果c1宁是一奇在砾，贝IJisa刷1a(ch )- ~数返回一个斗草案值，否贝l}i返回o .同样v如果ch 是标点符寻〈如逗号或句吱)，函数ispunct( ch )将返回tJ:uc _< 这些fIt数的返回类型为-int ... 而--1’是boor.但通常bool转换让您能够将它们视为bool 类型。)

### 第 178 页

使用这些函-数比使丹也ANÐ‘ 和OR运算符更方便.例如，下面是使用M啡。和OR 来测试字徙ch是不趁字锦字符的代码:...:..._,’, ‘_ “ if:( (c且〉霉’ a‘&& çIL呵’z‘)I f--:-{ ch民’þ;‘&& ch气二”Z’))‘,.’. ,:.‘,‘

与使用isalpha()相比:· .· eE 飞•• .._ •••• ...:... . ,; . --? →』

iC( isalpha (ch) )、~. :‘ is.~lph.-a()不仅更夺易使用“而阜豆通用ι勾\fD/o.R 格式假设A~Z 的学校编码是连续的，ι某他字符的钝码不在这个范围内。这种假设对手-ASCII码来说在成立的<r{旦~常并非总是如此。

程序清单6τE 演示一些ctype 序函数。具体地说:官使拜毛isaJpha()来检盒字符是否为字龟字符，使用ïsdigitsn来测试字符是歪为数宅茅符，如l3 ，使用时pace~)来测试字符是否为空白，直rr换行符、空格和制表符，使甩ispunct()米测试事符是否为标点任军谈程序还复Jb了ifelse if 结构，并在一个whife-循环中

…-

，使用了.cin.ger. (cÞar )0“

,' .

,-\ 程序清早否.8.cctype!>ppp‘,’ “，、”,-·一+

```cpp
// cctypes .cpp --using the ctype.h library
#-includι_< iostream>.. ，.气，_.. eee z-.
```

内ïlirlël峭飞<cct玫e>二..j 且pr哩。typ更sf母L-characterfunctions --.

__ ‘ int, ma主n() ., ·

、

、

```cpp
using ñamespace std;
cout << "Enter text for analysis, and type @ "
'‘to terminate input, \n" ;
char-ch;
int whitespace ='O~
inè digits = 0:
ìnt chars =σγ
--.--.int punct = O~
int . others. =白J
-吗cin.get (ch) , 11 geí: 'first .cha.ractú: " , , ,
```

, ,产~二切

```cpp
whìle (ch ! = '@') 1/ test for sentineI
1f !isalpha (cli) L / 1-is主tan-alph'abet Ic character?
chars++:
else if(isspace (chr) _ 1/ i s it a wh主eespa.cecha,J'acter?
wh主tespace++:
el~e i f( isdigit (chl) // is it a d i git?
```

digi tSH厂-一---二

else if (isp山回t (ch)) 1/ is it p让nctuation乙

```cpp
punct++;
```

els邑__

```cpp
o t her:s+•J
cin.get(chF; / / get next. cl!_aracter
```

j 。u t <C h町<< ‘刷.民趾阳tte

```cpp
<< whitespace' << 11 wh毛i tespace~'性』
c< digits << • digíts, "
<< punct << " punctuations ,
,
```

'贸

```cpp
<< others << " oe.her S'. \n 11
r eturn 0;
```

L

下丽是该程序的运行情况。注意，空白字符计数中包括换行符:... .-:... ‘ι.、一-，.二..-_ ..价• 二一矿四毛e“、.每、...-、... 面-_-_’.一..‘一、一υz …, z ..、,,‘.. 二4牛-叩、一” _.且】ν，;-_..一一一--1、-• . ~ 一一、刊’一一.一…‘ ‘ ...,._-“_ •••••

... 、.'~.，

ι、“.-..、品、缸‘飞-、_:_”一..-.,. •• _._..哇,,-;.: __.-

### 第 179 页

```cpp
Ent er t ext for analysis , and type串tot e rmi nat e inpu t.
AdrenalVision International producer Adrienne vismonger
announced production of their new 3-D fil皿，a re皿akeof
"My Dinner with Andre," 8cheduled for 2013. "Wait until
you see the the new scene with an enraged Collossipede!"@
177 lett ers, 33 whi tespace , 5 digits , 9 punctua t ions, Oot hers .
```

表6.4对ωtype软件包中的函数进行了总结。有些系统可能没有表中列出的一些商数，也可能还有在表中没有列出的一些函数。

表6.4cctype电的字符函蚊

民数名利「堪回{Q‘_

isalnumω l‘ jm泉参舰字母效率，抑制数字.刷刷回阳e

is划þha()如果参敬是字母』该æ蚁返问Il'Uc

一十一一一一一一一一一一一一一一一一一一一一一

, _

iscn创()-直I棵参数是控制字符，该局壁t返问tru晴

isdigit({)

斗果参数是数字该函数返间

前‘M

isgr叩Iit-)-民一一一一一一一刊一二一一一一一

数一一的一

岳果参必除空格打印字符·该返回

islowe r~护:-一一一-一-切一-丁一-一-瞅-

E架参敛是小写字一该函饭返回『A一

isprintC) 阳如果参敛是托邱字符〔包娼也空格).该iii.I数返回true-

ISpun叫)--.-· ‘ F 如果重要数是标点符号早该函数返钮川中也

、.-‘. -. 1-~如果参数是标准空白事符γ如空梅、选纸、拱手苦符v罔ljõ ;~ 、水平海最符或者蚕豆俐表

isspace叫)-<,

t~符，该函数返回t阳e.、:- “.:-‘ -月P叫-二_，;.--:._ -._;，:::J 如时何?芽，及函数幽pce川二; 二...::..._‘二二二-二, _--、，

吨

.:"',.,' :..,

_-

i~xdigilt) .P!!:痕参数是十六异常j数宅，~Il~ ~;‘__9 ~旦:’- ~jj且岳二F;该函数返罔~true:‘

-~ ':::.-- -

‘节

阳lQwe时〉如果参数是大写字符.mll返回:民才、写.有则返回该参数

touPP“!i 1 虫n:Jit参数是4、写字符7则这回莫大写s否则返回该参数

、

二、二6净-7: 运算符，.二、二..一

喝采代号-hl烹制自誓要协抖抖事啧称7

的事算符.τ该在莫符的遮呵格式如~/二主‘飞-~:1~;~3

‘;fiù:ej; s>.c.ρ~.二，~XPi:it$5 i oi:l3-.=-’‘ 二-~.~‘~气川ZJfA ，-

f、\、JJ二、二...￥.;:-‘汁士γ .斗... . .: -~ ~;.于h芬e卢fι-:，.-;子.~.宇rιLγγ，γ>: :..，’吨专￥川、飞f_ ，‘“今、.豆E乌4斗乒二ιρ.，内、，呵吨?安哥飞h气~F，~心Z兰:、、

iρ~茄和νν1f:-μ句，句削言言ζ，:;二;矿且贝肘t饿j赘些飞夺悦「峰磊夜幅录运汹式共彷[蛐附峭啕惶喧-为J卢叫七妇叫x叩p沁孟函函l弘沁ωωs剑ω阳i阳0∞ n二三千吨?的号子?昂的可奇地l巧同乡均是?可i;j吨FJ;二;二二三γ二三汪E气“‘~’.:‘::.::::’:”:二_..乙，5;芹.:>::5卫♂i勾p二_1 ‘2’~jιL、:5盯q>γ，弓3￥ s. tril毗e;:<咱咄s盹6丁万ëx邓pres约E主户_1m;và剖11:1手-19吕飞;ioι~0三γ::. ‘;’_ :.:~ 、J、-~ν.γ-.二二τ二-斗... ._,三?巳.斗叫4二.川- 王“‘争J轩--芝片;9η1@空:~1::毕F仨宇〉μ、J刀J/.、主主与与;寻号手立立啕之fι三三-9e?f巧更芒E雪咒t，二F?ω。~-e手rS气Jon_:.~，~1飞?-11 ‘ilfdJ气’二二γ二二之气气王、儿• 、卢川亏宵可刊以运在醉释3荒在三匕立斗夺斗守i系伊柳机俯r只f:~切如县豆夭于C:3.副整斗哉注}注t画缸l ;ti豆10.:乒气亏否前酬贝川~凶为Et乞￥挺，1:在豆共-际的-蝠稳苟二〉专♀二=羊:二.‘二，二二二v气;斗R三g飞.二.三:、鼎中f二i这主乌B阜些霆达式咆夺包1瓮瓮雪耸』变彗J仨..-，...二;二飞主:二i产’-~~ ~:...-..，豆:-‘~ . ~.:.二’刀，二:...飞二3: 亏:-:~:气，、二--_‘

.:-

3':!. ' -

，-“”ξ-.. ;.:.~:三-JfE话雯，?9些用手?运算得明白叫卢亨雯的产/i'j 二三:王‘，:. -, “_:二=” -,-=--立于三-J=二二:.于，...二tλh、、- ι』乞J运~.~.二.. ~ i“’.乞『点γη:‘;~ ... ’.-:、~--υ-飞 、-川.飞--川二咀，_‘:”~. ., 牛二~’.;.‘-“:与灰白.• :-.’:”‘. ...-.;.:芝.:.. ..1“- 宇:弓子~~:二、-<γ、.:’.‘’‘’:.‘.-~γ町，、二♂-、、... ~ ..’:‘~...~二’丁_‘:-;:

“ ~‘，，’凶尘，气;土二:.，._”“υ宁，士;士兰兰-?~-.‘”:~ . ~. .. ...，吁:二二’ 、飞--主、工阿三:. ~;-; ~ ‘::、号’二~:‘-~::亏:山“-二-、、小...、\:’: ‘~-:::- .-;且、，_，:.’，:，工T‘→二，(.‘.; :’_., .:..:- :::..:...$”}

### 第 180 页

程序清单6. 9condit.cpp

```cpp
// condit.cpp •• using the conditional operator
#include <iostream>
int main ()
using namespace std;
int a , b;
cout << "Enter two integers: ";
cin >> a >> b;
cout << "The l arger of " << a << " and " << b;
int c = a > b ? a : b; // c ; a i f a > b , else c ; b
cout << It is .. << c << endl ;
return 0;
```

下面是该程序的运行情况2

```cpp
Enter two integers: 25 28
The larger of 25 and 28 is 28
```

该程序的关键部分是下面的语句:

```cpp
int c ; a > b ? a b;
```

它与下面的说‘句等效=

```cpp
lnt C;
if (a > b)
```

c = a;

```cpp
else
```

c = b;

与if else 序列相比，条件运算符更简洁，但第一次遇到时不那么容易理解.这两种方法之间的区别是，条件运算符生成一个表达式，因此是一个值，可以将其赋给变:毒或将其放到一个更大的表达式中，程序清单6.9中的程序正是这样做的，它将条件表达式的值赋给变:L1:c。条件运算符格式简洁、语法奇特、外观与众不同，因此在欣赏这些特点的程序员中广受欢迎.其中一个技巧(它完成一个应被谴责的任务一一隐藏代码〉是将条件表达式嵌套在另一个条件表达式中，如下所示:

```cpp
const char x (2) (20) = {"Jason "咱tyour service\n" ) ;
const char • y = "Quillstone ";
for (int i = 0; i < 3; i++)
cout << (( i < 2)? !i ? x [i ) : y x[l)} ;
```

这是一种费解的方式(但绝不是最难，理解的)，它按下面的顺序打印3个字符息:

Jason Quillstone at your service

从可读性来说，条件运算符敲适合于简单关系和简单表达式的值:

```cpp
x = (x > y) ? x y;
```

当代码变得更复杂时，使用if else语句来表达可能更为清晰。

## 6.5 switch 语句

假设宴创建一个屏幕菜单，要求用户从5个选项中选择一个，例如，便宜、适中、昂贵、奢侈、过度.虽然可以扩展if else if else 序列来处理这5种情况，但C++的switch语句能够更容易地从大型列表中进行选择.下面是switch语句的通用格式:

### 第 181 页

> ［本页文本层 OCR 严重损坏（该页扫描阴影/插图区产生了大量乱码字符），以下为原始抽取结果（未删改），内容以 PDF 第 199 页图像为准］

;_,. ..:.. _ --' _.'';'_:" .. __ .. --:---_ _..-

-..

，._-~--唱-.-ι『卢...，.‘-“’..:..._:.:.:-::i~.; 7‘ _._.’:‘ ~._:.--=~_”~.-:--.主-‘_..-z一--.-’--‘=气ι_-ζ-四_. :~~=~.-己=-~品.“...:.-.一咽’‘，:-‘---’--一-一-_，，‘._.. ... _f__一-_.--::.一=-:::...~~--...:;_... .~.~-~--←’”“.. ”‘-町=-. -一’.-..=-.=.=-.-•_‘. 号，、.: .ζ.. ;::-..二 ..,...~.. -. . ~ •’ ‘’7 ‘ ..,_’ -;-“ --:-~ ，，;~ _ :-.~” “-~_‘-;-. -.:;c . ~ .’. 汇『在二.”“‘_气、也-甲鱼e 户.-俨.’.~…

~‘. “”，’ .“”‘二~产~’.‘啡、.;..;’ \::“‘~--=’ ::-” . -.:--毛⑤φJι:._.:. ..~古气户~...‘. ~

...

._ •

Lζ--_“:=二‘二, 严.~-=工-’ ,__ -二五二·毛:.:_:_ ~-=.，乒‘-’:~~::::‘，_.’.~~毛~-:-; ‘:，-S7可气飞)一.-’, 二二蝇一卢~--丁J~ 手、迈士: ~ ‘._--;-’ - . ._.-吃伊刷刷峪---=-缸，宁已占』帽于『宫副=--‘饨’... :-号-_.;~‘. ”“

### 第 182 页

```cpp
çin ;胁>ehoicoj
while (choice 1. 5 )
switch(choice)
case 1 cout << "\a\n";
break;
case 2 report ();
break;
case 3 cout << "The boss was 1n a11 day. \n";
break;
case 4 comfort () ;
break;
defaul t cout << "That ' s not a choice. \n.;
showmenu() ;
cin >> choice ;
cout << "Bye !\n";
return 0;
void showmenu ()
cout << "Please enter 1, 2, 3 , 4 , or 5:飞n"
"1) a1arm 2) report\n.
'3) alibi 4) comfort\n"
```

“ 5)罕lit\n”j

```cpp
v‘,‘ r e nv ( l
,rAU
```

1 。。艺，、

```cpp
cout << "It's been an excellent week for business. \n"
"Sales are up 120\. Bxpenses are down 35在\n";
void comfort ()
cout << "Your employees thinl毛youare the finest CEO\n"
"in the industry. The board of directors think\ n"
"you are the finest CEO in the industry.飞n.';
```

下面是该程序的运行情况:

```cpp
P1ease enter 1, 2, 3 , 4 , or 5:
1) al arm 2) report
3) alibi 4) comfort
5) quit
```

4

```cpp
Your employees think you are the f inest CEO
主nthe industry . The board of directors think
you are the finest CEO i n the industry.
Please enter 1, 2, 3, 4, or 5:
1) alarm 2) report
3) alibi 4) comfort
5) quit
```

2

### 第 183 页

```cpp
It's been an excellent week for business.
Sales are up 120 苦.Expenses are down 35奄.
Please enter 1 , 2 , 3 , 4, or 5:
1 ) alarm 2) report
3) alibi 4) comfort
5) quit
```

6

```cpp
That ' s not a choice.
Please enter 1 , 2 , 3 , 4 , or 5 :
1) alarm 2) report
3) al ibi 4 ) comfort
5 ) quit
```

5

Bye!

当用户输入了5时，whi le循环结束。输入131U 4将执行switch列表中相应的操作，输入6将执行默认语句。

为让这个程序正确运行，输入必须是第数.例如，如果输入一个字母，输入语句将失效，导致循环不断运行，直到您终止程序。为应对不核指示办事的用户，最好使用字符输入。

如前所述，该程序需要break语句来确保只执行swi tch语句中的特定部分.为检查情况是否如此.可以删除程序消单6.1 0中的break语句，然后看看;It运行情况。例如，读者将发现，输入2后，将执行case标符为2 、3 、4和defualt中的所有语句。C++之所以这样，是自于这种行为很有用.例如.它使得使用多个标签很简单。例如，假设重新编写程序清单6.10.使用字符(而不是整数〉作为菜单选项和switch标签，则可以为大写标签和小写标签提供相同的语句:

```cpp
char choice;
cin >> choice;
while (choice != 'Q ' && choice != 'q' )
switch (choice)
case 'al:
case I 且t:cout << n\a\n";
break;
case I r':
case ' R': report();
break;
case '1':
case ' L': cout << "The boss was in all day. \ n";
break;
case 'ç':
case 'C': comfort ();
break;
defaul t cout<< "That' s not a choice. \ n" ;
showmenu () ;
cin >> choice ;
```

由于case'a‘后面没有break语旬，因此程序，将接着执行下一行一一叫case'A ’后面的话句。

### 6.5.1 将枚举量用i1=标签

程序清单6. 11使用enum定义了一组相关的常盘，然后在switch语句中使用这些常最.通常.cin无法识别枚举类型〈宫不知道程序员是如何定义它们的).因此该程序要求用户选择逃项时输入一个整数.当

### 第 184 页

> ［本页文本层 OCR 严重损坏（该页扫描阴影/插图区产生了大量乱码字符），以下为原始抽取结果（未删改），内容以 PDF 第 202 页图像为准］

switch语句将int值和枚举量标签进行比较肘，将枚举盘提71为int。另外，在whilc循环测试条件中，也会将枚举盘提升为int类型。

程序清单6.11enum.cpp

```cpp
// enum.Cpp --using enum
自include<iostream>
// create named constants for 0 -6
enum {red, orange, yellow, green, blue, viol et, indigo};
int main ()
using namespace std 户
cout <<-工Entercolor codι_(0- 6-): ";
int code.
cin >> code;..一-
while (code >= red &ιcode <= indigo)
{
swi tch. ( code~
```

←一

case rëd cout <ι二He ~lips were re岳飞n“;break;

case'orange : cout <<-. Her harr万言了。range ~\n“;break; -

```cpp
cas.e yellow cout <<-!Her shoes were yell。协\n .;break;
case green :. cout << "Her nails we 笠egre-en. \n";-15reak;
```

case blue----: cout < ~. Her sweatsui~咽且blue.\n“品br四k于

```cpp
case violet c。也tC'C ' Her eyes were violet . \n'‘ ; break;
```

case indigo∞ut <<-工Her_mood旧s- ind主90. \il“‘T”break;

L一

```cpp
cout << IIEnter color code伺-6) :
Cln >> co咀e;.
}
cout << 1‘Bye\ n" ;.
ret urn 0;
```

下面是该程序的输也:

```cpp
Enter color code (9- 6):-3
Her nails were green .
Enter color code (0-6)"-
Her eyes were violet.
Enter color code (0 - 创::- 2:'
Her shoes...市ereyellow
Enter color code CO-6)= ~
Bye
6.5.2 switch和ife lse
```

switch语句和ïfelsι语句都允许程序从边项咂进行选择.栩比之下，if else更通用.例如〕自可以处理取值范睡了直111之所示z

```cpp
ff rage > 1τ&岳age< 351
index、=0;
else it (age >= 35-&& age < 50}
i ndex.. = 1; -
else if (age >= 5 0-ωage-o< 65}
index. • 2.;
```

-.. . --_.. ._' 、- -.- -. .

工二.陶;-_. .二;: “=.-:: _. _...牛牛』户俨…句-，气…一一.~--_ ..-‘:”--.:.. ..:.. -. _，..一-一、-.~..~. ..-一-一... .--一一_-..:.---. 丐~~:，..:’;:‘:.:-~~.，-_ -.-::-;-::’:‘;:’~‘.←、?号-;.:_“--=--_., .~一一气二三，-二-手吃二:二一7:_:--.’_~三二二ι-_马兰.::.;._:->.;”，，:.:.“”“=￥γ-色叫‘-怡‘‘二c_ι‘马、ι..;~~~--.. 二町、二·一飞一.-._叭:..J-二，ζ~.-:一τ-;-..-”-’~; ‘-7’7“” “-;气7且”“‘，.二.:~.~圃7:~食_.气.--专T王=二”“-:-\今‘三马宁主二￥-~:_:...~..._斤。卢干--王三.-牛二τ二J牛二三三‘气芒二~~._;;.:;.玉毫:之工4二二i二三~’-::..:‘~P::”’:_.~.士、._τ千三..宇--..三吉z工电3飞...-;-=.~<-=--‘. ._.，~‘’- .→民十一工‘一~ ←.--→一一一一十宣一吐一一一…

### 第 185 页

```cpp
else
i n.dex = 3;
```

然而，switc百并本是为处理取E值范悻施设计的τswitch语句中的每一个cωe标签都必须是一个单独的值.另夕F:这个值必须是整数t包括char}，因此switch无法处理浮点测试.另外case标签值还必须是常最.如果选项涉及取值范围、- 浮点测试或两个变量的比较，贝1 应使用ifelse语骨.

然而，如果所有的地项都可以使用整数常量来;际识，则可以彼周switch语句或ifelse 语句.由于飞witch语句是专门为这科情况设计的，因此，如果选顶超过两个，则就代西长度和执每速度而言，s响他h选句的效率更高。

提示:如果就可以使用if elseif语句，也可以使用switch-诠句τ则当选项不少于3~ 町7应使M;switch 4岳句俨.6 .6 breaR和corrtinue字吾句一

break..和continu巳语句都使程序能够跳过部分代宵。iij以在switch 话句或任何循环中使用break说如佼程序跳到switch=或循环后丽的语句处执行.continue 语句用于循环中F迁程序跳过循环侄电余下的伐码，并开蜡新一轮循环(参见图6.4 ) 。

因6.4忧国k 和continue 语句的结构

程序清单6.1 2 演示了这两条语句是如何工作的.该程序让用户输入一行文本.循环将回显每个字符，如果该字符为句点，则使用break 结束循环。这表明，可以在某种条件为住ue时，使用break来结束循环。

### 第 186 页

接二F来，程序计算空格数，但不计算其itá字-符.当字符不为空格时，循环使用毛ontinue语句跳过计数部分。_-

_._--_-_ -,

程序清单6 . 12jump:cpp

```cpp
-ïl jump:cpp_ --uálng continue如dREeak"
排iric1 ude<ióstream> ‘, ，、R
```

...'...'OC""1'"" .、

```cpp
const i nt ArSi 主e= 80; "
int main ()
us主ng_namespacee-~td;
char -1 in(Ar$i zer;
int spaces ~ 0;
cout << . Enter a line of text: \ n";
ci n.get !1ine, ArSize ) ;
cout << . Comp1ete 1ine: \ n" << 1ine << end1;
cout << . Line t hrough first period:\口";
for (int i = 0; line(i) != ' \0 '; i ++ )
cout << line (川//displ ay character
if (1i ne (i) == , _,) /1 quit if it 's a period
break;
if (line(ij !. ' ') 1/ skip rest of 1∞p
continue;
spacesφφ;
cout << .\n" << spaces << " spaces\n";
cout << . Done. \ n";
return 0;
```

下面是该程序的运行惰‘况:

```cpp
Ent er a line of t ext:
Let's do 1uncb today. You can payl
C口mp1 ete1ine:
Let ' s do 1unch today. You can pay!
Line through f i rst peri od:
Let ' s do 1unch today.
3 spaces
Done
```

程序说明

虽然continue 语句导致该程序跳过循环体的剩余部分，但不会跳过循环的更新表达式.在for 循环中，continue语句使程序直接跳到更新表达式处，然后跳到测试表达式处.然而，对于whiJe循环来说，con由ue将使程序直接跳到测试表达式处，因此while循环体中位于continue之后的更新表达式都将被跳过。在某些情况下，这可能是一个问题.

该程序可以不使用continue语句，而使用下面的代码:

```cpp
i f (line (iJ ~=‘I
spaces令+元
```

然而，当continue之后有多条语句时，CÐßtmue语句可以提高程尾的可读性。这样，就不必将所有这-些语句放在if语句中τ

和C 语言一样，C忡也存gotQ 语句了下面的语句将跳到使用paris:~为标签的位置:

```cpp
goto paris;
```

也就走说，可以帮下面这样的代码:

、

、

### 第 187 页

```cpp
-ch'ar-ch;
```

Ci nγ:> C怡，;

```cpp
if (cn== 'P')
goto p&'r主S;
_ cout s< . ... ~
```

-二pari s.:cout啊‘Y。吐’vejust arrived at Paris. \nw ;

在大多数‘情况“E.(有些Ã认为z在任何情况下)，使用goto语句不好，...:r而应使用结构也控制i在句〈如if else.~ switclt, continue 等.j.来控制程序的流程~~

## 6.7 读取数~-的3盾环

假设要编写二今将一系列数亨读入到j数组中的程序，并允许府户在数组填满之前结束输入伽一种芳法J毛茸号是利出f二二哥贯坚阿兰兰运ZJZ三二三主主言拿主~-:~2:~飞￡去了享主岳王三字飞二辛苦三毛

```cpp
i nt n~;
```

c主n>> n;

4如果用户输入7个单词「而不是一个数字，情况将如甸呢‘1，发生这种类型不匹配的悦况时，将发生’4.-种情况2

.-n的值保持不变;

• 不匹配的输入将被留在输入队列中.

• cirr对象中的?今锻误标记被设置;

• 对cin:穷法的诱饵将返Iill false(如果被转换为b∞k类型〉。

方法返回fafse意味着可以用非数字输入来绪束渎收数字的循环σ 非数宅输大设发错误振ja意味着必须，茸茸该标记，程序才能继续读取输人。cle叫)方法重建错误输入标话，同时也重登文件尾(EOF 条件，参见第5î白，输入带误和E0F都将J噎致ClI..返回f画lser-第17置在将性论如何区开这两种情况r 下丽来看两个演示这些技术的示~l-

假设要编写了个程序扣来计算率均每天捕获的鱼的军蠢ρ-这里假设每天最多捕获3条鱼，因此一个包含5个元黎的数组将足以存储所有的数据，但也可能没有捕获这么多鱼。在程序清单6.13.中，如果妓主旦被填满或者棉入;r非数字输入，循环将结束。

程序清单6.13c阳fish.cpp

一一二一二一一~一..一一一→?一币‘一一二

“ 11 ciiiHsh.cpp 三nqn - n‘飞机eric.input terntinates l oop=.’ .0” .在-_. #incI百äe<lostr'eam>‘..‘...、二’γ、二.;‘，’‘‘~~.’

```cpp
.const int Max = 5';-' , '.'~
主nt; main{ 广
std; ~
飞ls ing- namespac'e
11 get data
doubl e fish[Maxr ;
cout c< "Please e由terthe weights of youe- fish.\p‘ι
```

cout << “YOu may-ente巳upt口伽<<Max

```cpp
<<_ . fish <q_to terminate> . \n";
cout << "fish掉1-•.
:mt F~ 0 ;
```

while-(i, < 阴阳&&cin-川fislÞH:t) (_.. ., . . if( 叶i.. < .Max) -..

ι‘ _.、-

J 、cout时“fi乡h<<11 <.:::... i+l...:-c:.:< i,. : ..;, ...二二‘舍

、-. .

### 第 188 页

```cpp
11 calculate average
double total = 0 .0;
for (int j = 0; j < i; j ++l
total += fish[j);
11 report results
if (i == 0)
cout << "No fish\n";
else
cout << total 1 i << • = average weight of ..
<< i << 11 f i sh\n";
cout << "Done. \n";
return 0;
```

注意:本书前面说过，在有些执行环境中，为让窗口打开以便能够看到输出，需妥添加额外的代码。在这个示例中，由于输入‘ q‘结束输入，处理起来更复杂在是:

```cpp
if (! cin) 11 input terminated by non-numeric response
{
cin.clear( ) ; 11 reset input
cin.get(); 11 read q
cin.get(); 11 read end of li ne after last input
cin.get (); 1/ wait for user to press <Enter>
```

在程序清单6.13中.如果要让程序在结束循环、后接收输入，也可使用类似的代码。

程序清单6.14史进了一步，它使用cin永远回值并宣置cin。

程序消单6.13中的表达式cin>>fish[i]实际上一个是cin方法函数调用，该函数返回Ctn.如果cin位于测试条件中，则将被转换为0001类型v如果输入成功，则转筷后的值为位ue，否则为fa忱。如果表达戏的值为倒钩，则循环结束.下面是该程序的运行情况z

```cpp
Please enter the-weights-of your岳ish.
You may enter up_to 5 fish <q to terminate>.
```

fish骨1:30

fish骨2:3S

fish辑3‘:2S

ffst!排4:4 0-

fish排5:q

```cpp
32.5 ~ average weight of ~ fish-
Done..
```

请注意下面的代码行:

```cpp
while (i <.. Max &阜cin>>-fisl\. [i)) {
```

自尊丽讲过，如果逻辑AND 表达式的左侧头p Îalse.则C忡将不会割麟右侧的表达式』在这壁，对右侧的表达式进行判定意味着用cin将输入放到数组中。如果t等于Max.贝。循环将结束，而不会将一个值读入到数级后面的位置中.

当用户输入的不是数字时，该程序将不再读取输入。下面来看了俨继续读取的例子俨假设程序要求用户提供5个商尔夫得分，-.以计算平均成绩。如果用户输入非数字输入，程序将拒绝』并要求用户继续输入数字。吨以看到，可以使用cin输入表达式的值来检测输入是不是敏宅.程序发现用户输入了错误内容畔，_“.-应采取- 3个步骤。

1.莲笠cin以接受新的输入。

2τ删除错误输入。

3.提示用户再输入.

, . . .-'.. -_.._-

._ι_.---

### 第 189 页

请注意，程序必须先窒置cin，然后才能删除错误输入。程序消单6.14 演示了如何完成这些工作。

程序清单6.14cingolf.cpp

```cpp
11 cingolf.cpp --non-numeric input skipped
#incl ude <iostream>
const int Max = 5;
int main(}
using namespace std;
11 get data
int g01f[阿ax];
cout <<‘Please enter your golf scores. \n" ;
cout << "You must enter " << Max << 11 rounds .\ntl;
int i;
for (i = 0; i < Max; ì ++)
cout << "round 辑"<< i+ l << ": ";
while (! (cin >> golf [il)) (
cin.clear(); 11 reset input
while (c in.get() ! = ' \n')
contìnue; 11 get rid of bad i nput
cout << "Please enter a number: ";
11 ca1culate averaqe
double total : -0.0;
for (i = 0; i < M拙;i++)
total +. golf(i);
11 report resul ts
cout << total 1 M缸<<n = average score ..
《问ax<< " rounds\n" ;
return 0;
```

下面是该程序的运行情况:

```cpp
Please enter your gol f scores
You must enter 5 rounds.
```

round骨1:88

```cpp
round #2: 87
round #3: mU8t 17
Please enter a number: 103
r ound #4: 94
round #5: 86
91.6 = average 9core 5 rounds
```

程序说明

在程序清单6. 14中，错误处理代码的关键部分如下:

```cpp
while (! (cin >> golf (i) ) ) (
cin.cl ear () ; 11 reset input
while (c 口1. get () ! = '\n ' )
continue; 11 get r id of bad i nput
cout << • please enter a number: .;
```

如果用户输入邸，则cin 表达式将为true，因此将一个值放到数组中:而表达式!(cin >> go)f[i])为false，

### 第 190 页

因此结束内部循环.然而，如果用户输入musti'l，则~cin 表达武将为“峙，因此%会将任部值放到数组中:再袋达式!(cin>>gol fEt))将为世ue;-因此:i!:入的部的while循环.该循环的第一条语句使用clear(.)方法重置输入，如果省略这条语句，程序将拒绝继续读取输入r 接下来，.程序在whi1e循环中，使用cÍl).g叫)来读取衍尾之前的所在输入，从而删除这一丰主中的错误输入』另一科7ï法是读取到T一个空向字符，这样将每疚，删除一个单i巧，而不应一次删除整伍最后，.程度告诉用户，应输入一个数字。E五8简单文件输入/革命也

有时候.- iifr过键盘输入并非最好的选择。例虫际假设您编写了一个股票分析程庭，并下载了一个文件，其中包企1 000种股裂的价格。在这秒1瓷况下且进程应直接读取文件，而不是手工精A文件中反资的值，‘民在芳傻得多』同样，让程7字将输出写入到文件将更苑方便，这样可寻寻到有英结果的习t久性记录.

幸运的是，C++使得将读取键盘输入和在屏幕上显示输陆(统称为控制台输入/输出〉的技巧用于文件输入/输出〈文件ν0 )非常简单。第1 7章将更详细地讨论这些主题，这里只介绍简单的文本文件uo.

### 6.8.1 文本1/0 和文本文件

这里再介绍一下文本1/0的概念.使用cin进行输入时，程序将输入视为一系列的字节，其中每个字节都被解释为字符编码。不管目标数据类型是什么，输入一开始都是字符数据一一文本数据。然后，cin对象负责将文本转换为其他类型.为说明这是如何完成的.来看一些处理同一个输入行的代码.

假设有如下示例输入行:

38 . 5 19.2

朱君王7下使用不回数据类型的变慧来存锚耐，CE-E如何处现该输大行的γ首先，来看使南char-叛黯类型肝情况:

```cpp
char ch;
c ih-: >> chj
```

输λ行中的第一个字符被赋给ch.在这里卢第一个字符是数字3 ，其字符编码〈二进制〉被存储在变髦ch中。输入和目标变量都是字符，因此不需要进行转换.注意，这里存储的数值3，而是字符s-的编码L tMT上述输入语句后，输入队列鼎的下一全字符为字符8，下一个输入操作将对其进行处理。

按:f来看看时类型:

```cpp
i-nt-n<.
c i?r>> n ;-
```

在这秘饿缸F.cin将不眠读取，直到遭到非数字宅f守J也就是说，在J悔读取3和8，这样句点将成为输大队列帘的下一个字符。cin--通过计算发现」这阵个字符对应数位38户因此拖到的二逃1M编码复fIj~ìlJ变量n中τ

接下来看看double类型:

```cpp
d。飞lbleX;
Cl~>> X;
```

在这种情况下.cin将不断读取，直到遇到第一个不属于撑点数的字符.也就是说“cin读取3 、8、句点和5，使得空格成为输入队列中ri9:下一个字符。cin 通过详算发现，这四个字，符对应予数值38 .5 1:因此将3 怠呈阳ι二遂制编码〈辛辛点格式L复制到变:屋. X中.

接下来看看char 数组的情况:

```cpp
char ,^'Ord (50 ):;
cín. >>- word;
```

在这种愤况下，cm将不断诙取，直到遇到空在L字符.也就是说宫读取3 、8、句点和5.使得空格成为输入队列中的下一个字符d然后.cin 将这4 个字符的字符编码存储到数组word中，并在末尾却瓦k二个

### 第 191 页

空字符。这里不需要进行任何转换。

最后，来看一下另一种使用char 数组来存储输入的情况:

```cpp
char word [50];
cin.geline(word, 50) ;
```

在这种情况下，cin 将不断íì卖取，直到遇到换行符〈示例输入行少于50 个字符).所有字符都将被存储到数组word中，并在末尾加上一个空字符。换行符被丢弃，输入队列中的下一个字符是下一行中的第一个字符.这里不需要进行任何转换.

对于输入，将执行相反的转换。即整数被转换为数字字符序列，浮点数被转换为数字字符和其他字符组成他字徒序7{Þ:(如284: 53-或::- 1. 58巴士06:)。宅符数据不需要做任伺转换.

这里的要点是，输入了-开始为文本。因此』控制台输大的文件版本是文本变件，阻每千字节都在储了二个字街编峙的文件。并非所有的文件都是文本文件，. i伊例F列l如L A数或津点:格格i茸支〉严-来存恃致偌数挥砾.妨娟~ ，γ:‘寻孚k处E量岳L立文:1’怦#忡￡年扫坷能包含文本信1忌主，但也可能包含用于描述格式:·..u‘二..字体、n:印机等的非文本数据。

本主运讨论的文件宵。相当于控制台110，因此仪适用于文本文位且要创建文本文件，用于提供输入，可使用文本编译器，声llDOS中的EDIT，‘Wináews中的“记事本”和UNIXILinux 系统中的vi或emacs.也卢一两i以传肘字处理程序来创建，倍必须将文件保存为文本格式。IQE中的激代码编辑苦苦生成的也是文本文件，事实主t 部代码1号件就属予主本坦牛.同样，.可以使周交本编辑苦苦采查看通i王文本输出创建的文件了二

-_.. _.: :. ' 6.8:2

.1军入到文本文件中.t ‘-言、、儿。ι句，毛争、、-: .y可天文件挣入，C++:使用类似予cout的东西。下面来复习一些在关将cout 用于控制台输出的基本窃头f.;“”.:.;一.为文件输出做准备二..._. ...-..._...巳...-... “”必须包食头文候iostream. . _-... ._.: .~ .• 头~传ió‘str白白定义了工:::’ffij 处理输出的‘Ostrea虱类正--:’:‘::. ’-_‘_’ι…‘.. l.; ~’:.~ 元、:.; ;. ,<:.. ,..;

e ~文件105位‘eam声明丁-二个名为∞ut的ostream变量〈对象L

.必须指明名称空间s.td:例如:为引用元素cωt 和endl;必须使用编译指令using或前缀std::.…二:_，.“~.:... .”可以-综合使用‘~üi和运算符<<笨重京各种类型的数报.---’--w -咛三二-

文件输出与此极其根似。严-_ “,: ~ ;_”_ • -: -

.必须包含头文件也tream“_‘ :._ 三._

• 头文件f沁-eam定义F一个用手处理输出的。f抽eam 类:.0_. _二

.e 需要声明二个常个做丽娟〈对象)，--:刑ti3;己喜欢切均1塞进行命名，条件是遵守常用声，‘: =---二的命名规贝IJ. ’~ ~，-, .., ‘.-:..二、:...~ -..;.::.

.必须f昆明名称空[母std;二例如，为费用元秦ofs忧am，必须使用统译指令using或前缀Std:: .‘ :. ’-=-‘γ、f产.; : 二;二气三舌云乏.. ’，.

j -

J丁γ令-….飞二~~二垃使脐主文件后乒二应使用方法法、cl句§笋酬óe()师将其矢闭。;二.丁:二二‘-’_二-…-丰‘~.’云二二?二一仁、?干二j二二-二，丁L丰.~.正二丁二_ ，~-ξ-二

ct吨综合使用。f始eam 对象和运策符〈ζ来输段?经替类型的数挠。-_=‘ ., • ...~注意，一垦然头妇牛i怜的叩提t共于-士预先定50H‘盟名为主out眼了。strearrí 对象，但您必须芦现自己ti<J_:’.:二ótStreãm 对象已、为其命名，并将其同文件关联起来。下面演示了如何声明这种对象:二·兰_.….，.二了:

‘ofs t rearn.outFile;二，.二.’/ / outE'il“e an ofstream ob开ët--- . -: ,. -但--~ófs t re~rn !outi. -. < - ~__‘ ’.‘ (1. foue afJ:::of:súeãm. ob~e:ct ~吨工

...~.-. --:‘-’ 在_.飞一--一一.

_-

，、...，，_.. -‘、-.，_句--..，- -.~

宁‘-:’‘ _“”- ’，、-..‘ ..“

.每·一-宁、_...,... .

.. '_,_ -- -... -

'_ ._' .-

. -.-:-.

『_‘ .“” -、__’ .; _, -, 品e户

--

、-、、、

.一‘.-. , ，-_...:_c .:., 、--、‘-“” , _“ ’, 夺

### 第 192 页

中的字符串ι

下面演示了如何使用这种对象:

```cpp
doub1e wt = 125.8:
outFi1e << wt: // writ e a number to fish .txt
char line (811 = "Objects are c 10ser than they appear.":
fout << 1ine <<end1: // write a 1ine of text
```

重要的是，声明一个ofstream 对象并将其同文件关联起来后，便可以像使用cout那样使用官.所有可用于cout的操作和方法〈如《、endl和setf() )都可用于of如ωm 对象〈如前述示例中的outFile 和fout) 。

总之，使用文件输出的主要步骤如下。

1.包含头文件f剑ream.

2.创建一个ofstream对象。

3.将该ofstream 对象同一个文件关联起来.

4 .就像使用∞ut 那样使用该ofstrcam对象.

程序清单6.15中的程序演示了这种方法。它要求用户输入信息，然后将信息显示到屏幕上，再将这些信息写入到文件中。读者可以使用文本编辑器来查看该输出文件的内容.

程序清单6.15outfìle.cpp

```cpp
// outfi1e.cpp --writing to a fi1e
Uinclude <i ostream>
幅inc1ude<fstream> / / for file I/O
int main ( )
using namespace std:
cldd hnoo atuu aeee ua trad bi.lee eJJ
rbb -Rd
```

。立υ《

佣

v

aJ

r--

、自C

毒JrC

、ι

J

```cpp
。fstreamoutFi 1e: 1/ create object for output
。utFile.open(" car info. txt" ) ; 1 / associate with a file
cout << "Enter the make and model of automobile: ":
cin.getl i ne(aut omabi le. 50):
cout << "Enter the model year: ":
Cl.n >> year;
cout << "Ent er the origina1 asking price: ":
Cl.n >> a_prlCej
d_price-= 0<:913-*气'price;
// dispia~information o~scr.een wit~cou~
cout << tixed:
cout-; precision ("2 }O:
cout.setf (ios_base : :showpointl ;
cout""<< "Make and model: " <<-automobi1e << end1;
cout << "Year: " << year << endl;
cout << "Was ask如19S' << a_旦rice=..<<endl;
COUt:""<< "Now askïng $" << d_price << endl;
/ / noW'" do exac 1:..四Illethíngs us主n9:: outFITe-instea<rof cout
```

### 第 193 页

```cpp
outFile <ιfixed;
outFile ..precisiorrt2 r ;
。utFile..set f(i os_base: :showpoint) ;
。utFi1e<< 'Make and model:-" << aut。阳。bil e-<<end1;
。utFil e<C" ' Year-: • << year << endl;
。utFil e<< ' Was asking $" << a_price << endL;_
outFile <<帽NOwasking ~ << d_price << end生;
outFi l e .closeO; 11 done with file
return 0-;
```

该程序的是后一百仍护主子cout部分梅同，只是将cout 替换为、outFilc丽B.下面是该程序的运行情况:

```cpp
Enter the make and model of automobile : Flitz perky _
Enter the model year:- 2009
Enter the origi nar- asking price: 13500-
Make-and:- model: Flitz perky
Year: 2009
Was asking ~1 3S00.00
Now-asking $12325.50
```

屏幕输出是使用cout的结果。如果您查毒该程序的可执行实侨所在的目录，将看到一个名为carinfo.txt的新文件(根据编译器的配置，该文件也可能位于其他文件夹).其中包含使用。utFile生成的输出.如果使用文本编篇器打开该文件，将发现其内容版F:

```cpp
Make and modeT, Flitz pe.rky-
Year: 2009
was askíng $13500.0Q
Nowasking- $12325.50
```

正如读者表到的.outFile~将∞ut显示到屏幕上的内容写入到了主件carinfo.剧中。

程序说明

在程序消单6.15的程序中丁声明一个ofstream 双重段后，便可以使用方法open( )将该对象特定文件关联起来=

。f:streamoutF-ile; / / create ob3 ect f悦。utput

。utFile. open (-“car去世。.txt.);// assoc叠atewitl子-afile

程序使用完该实佯话，应该将其关闭:

```cpp
aut F ile.cro唱e();
```

- 注意，方注clωe()不需要使府文件名位为参数，这是因为outFile已经同特定的文咎关联起来.如果您忘记关闭文件，程序正常终止时将自动关闭它._ outFile可使用cout可使用的任倪方法.宫不但能够使用运算符<<.还可以使局各砸格武化交王法，如:setf( )和preèision() ~这些方法只影响调用它们的对象。初阳J对于不同的刘象，可以提供不同的值:

c。以.preclsi∞( 2);“一//.uaea. precisíon af 2 for the飞displayr、

..。哈萨ile，pt:牛i8ion( 4‘)二二刀ûs￥a .prec'fsíön ò( 4 ~òr fle’ output ; ,

i:-,

读者循要iè住的重点是，创建好ofstream 对象〈如outFile }后，便可以像:使用ceut那样使用它二γ 二回到opim() :方法三: 丁-、穴

。ut P'i le.open‘(“cariiifò.txt，;);.,.

在这豆7该程序运行之前，文件C缸info.txt并本存在。在这种情况下，方法open()将新建一个名为carinfo.txt的文件.如果在此运行该程序，文件carin自).txt将存在，此时情况将如何呢?默认情况下.opωo将首先截断该文锐，即将其长度截娃到零一一丢其原有的的容，然后将新的曹先出胧λ到该文件中.第::- 17-乒ι一一军事丹:留如何修改这种默认行为O... ..:: 二‘山-.-

“ …响←.

, . • 一一‘γ

‘一“-.-工也钮一-…一一-一... .. _” -、.、一、·‘.气... .. .“’

### 第 194 页

警告L疗开已有你文件，以接受输出时，默议将它其长度截短-为零，因此原来的自容将丢失。

打开文件用于接受输入时可能失败.f9ìJ虫陡，指定的文件可能已经存在，_倪禁止E对其进行访问.倒此细心的程丐厅，员将被盗打开文件的操作是否成功，这将在下一全例子电介绍.~:“::‘---产_.:_6.段3←读取文本文僻r尹.:...::~-工ι

接王来介绍交本文件输入，二古定基予控制台输入的。-控帘始输末涉及‘$个方丽芝下两首先总结这些.方丽J

• 必须包合实文件iostream.

• 头文件iostrcarn定义予一个用处理输入的istream 类。

.• ... 头文件iostream声明子←个名为‘cin的istream变量〈对象h..

.飞必须指明名称空!可std:例如r;- 为号l甩元素cin;必须使用编译指令usÌÍlg 或前缀sω.. •

.可以综合‘使牌cin和运算符〉咪读取各种类型的数据.丁.“.”二…J

• 可以使用cin_和.getO方法来读取一个宗符，使用cin和getlinc( P夜读取一行字符7

-.‘~.:可以综合使用cin和民of() ，fail付方法来判断输入是否成功.·:，“_二-二二一.. 对象cin本身被周作测试条件时”.如果最后-，个读取操作成功，它将被转换为布尔值仕ue，否则一ι~-‘=被转换为falsè~“”

文件输血与此极其相似:

• 必须包含5写文饨化tream.

• 头文flj二tStream定义Z 一个用子处理输入的i fStream..类。

• lIiì要声明一个或多个情trean泛变茸(对象)，并以自己喜欢的方式对其进行命名，条件是遵守给用

的命名规则。

• 必须指明名称空间std:例如，为引用元素;ifstream ，~必须使用编译指令usmg或前缀std::-_

• 需妥将ifstream对象与文件关联起来。为此，方法之一是使用Qpen(}苏法。

• 使甩光文件后，应使用二.close()方法将其关闭.

• iiI纺台使用陈旧m对象和运算符》来读取各种类型的数据.

-. 可以使用ifstream 对象和get()方法来读取一个字符，使用i也悦m对象和getl iRe()来读取一行字符。

• 百I以结合使用ifstream二和eof号)、fait()等方法来判断输入是否成功。

• I也tream 对象本身被用作视试条件时，如果是雪后一个读取跺作成功，它将被转换为布尔佐truc ，否

则被辛苦换为falSc-..注意，虽然头文件iostream提供了一个预先定义好的名方cm的is悦am对象，但您必须严明包己的ifstfeam 对象，为其命名。r并将其同文咎关联起来.下面谈示了如何声明这种对象z

```cpp
ifst.r..eam inF i 民J/ / inFil'e-an主fst:reamobject
ifst:ream fín: / / fin an- ifstream obiecf
```

下面演示了如何将这种h对象与特定胁文件关联起来:

```cpp
inFile-. open'i:!'bowl:ing. txt 叫:/1 inFile used to read b咱wling. t xt file
char fileQame.[50.]:
```

ι、

‘. cÍn->> -fhè~ame卜·εγ f .ùsè’t sþec i“fiesιname

```cpp
fí""open{filename )..: ' . //. ..fin used to read: specif i ed Ole ';
```

注意，为法opcn()接受?个c-风格字符净、作为参数:这可以是?个字面字符且也可由是存倚在数组-气气一φ -、

卢‘、帘的字街串二

下面演示了如何使用法种对象:

double. wt:、, inFHe >> wti /1 read á .n!JÍnber fiom bowl ing ;tit. .‘-“’”‘ char..“1 iné ~IH'l ;广、

```cpp
f _i'n-,getline{Iii:le, -81);; 1/read a: line' of: text
.
```

‘

- .

### 第 195 页

重要的是，声明一个ifstream对象并将其同文件关联起来后，便可以像使用cin那样使用它。所有可用于cin的操作和方法都可用于ifs位eam 对象〈如前述示例中的inFile 和fm).

如果试图打开一个不存在的文件用于输入，情况将如何呢?这种错误将导致后面使用ifstream对象进行输入时失败。检查文件是否被成功打开的首先方法是使用方法is_open( )，为此，可以使用类似于下面的代码:

nf 4.lle e--x OFt P--( elE nex IB--‘A bs-<I--··abTnnu XJ P“

，"V··

```cpp
、a• •p缸,1 nez 。WPI nu)E
、4lZmn。d，飞J、
```

，，

、‘rU E

AD1、

a

如果文件被成功地打开，方法is_open()将返回true;因此如果文件没有被打开，表达式! inFi1e.isopen()将为true.函数exit()的原型是在头文件cstdlib中定义的，在该头文件中，还定义了一个用于同操作系统通信的参数值EXIT_FAILU阻。函数exit()终止程10/-.

方法is_openO是C++中相对较新的内容.如果读者的编译器不支持宫，可使用较老的方法g∞d()来代辛辛.正如第1 7:)‘苦将讨论的，方法good()在检查可能存在的问题方丽，没有is_open()那么广泛。

程序消单6.16中的程序，打开用户指定的文件，读取其中的数字，然后指出文件中包含多少个值以及它们的和与平均值.正确地设计输入循环至关重要，详细请参阅后面的“程序说明”.注意，通过使用了if语旬，该程序受益庭浅.

程序清单6.16$umafíle.cpp

```cpp
// sumafile.cpp --functions with an array argument
#include <iostream>
#include <fstream, // file 1/0 support
#include <cstdlib, // support for exit ()
const int S1ZE = 60;
int main ()
using namespace std;
char filename(S1ZE];
ifstream j.nFile; / / oþj~ct for handling f ile input
cout << "Enter name of data fíle: ";
c in.getline(filename , S1ZE);
inFile.open(filename); // associate inFile with a file
if (!inFile.is_open()) // failed to open file
cout << "Could not open the file " << filename << endl;
cout << "Program terminating. \n";
exit(EX1T FA1LURE);
double value;
double sum = 0.0;
int count = 0; // number of items read
inFile " value; // get first value
while (inFile .good ()) // while input good and not at EOF
++count; // one more item read
sum += value; // calculate running total
inFile " value; // get next value
if (inFile. eof () )
```

### 第 196 页

```cpp
cout << "End of file reached. \n";
else if (inFile. fail () }
cout << "Input terminated by data mismatch. \ n";
else
cout << "Input terminated for unknown reason.飞n";
if (count == 0)
cout << "No data processed. \n";
else
cout << "I tems read: " << count << endl;
cout << "Sum: " << sum << endl;
cout << "Average: • << sum / count << endl;
inFile. close ( ) ; // finished with the file
return 0 ;
```

要运行程序消单6.16中的程序，首先必须创建一个包含数字的文本文件.为此，可以使用文本编辑器〈如用于编写源代码的文本编辑错〉。假设该文件名为scores.txt，包含的内容如下:

18 19 18.5 13.5 14

16 19.5 20 18 12 18.5

17.5

程序还必须能够找到这个文件.通常，除非在输入的文件名中包含路径，否则程序将在可执行文件所属的文件夹中查找.

警告:Windows文本文件的每行都以回车字符和换行符结尾;通常情况下，C++在读取文件时将这两个字符转换为换行符，并在写入文件时执行相反的转换。有些文本编辑器(如MetrowerksCodeWarrior IDE编样器)，不会自动在最后一行本儿加上换行符。因此，如果读者使用的是这种编得荡，请在输入最后的文本后接下回车键.然后再保存文件。

下面是该程序的运行悄况:

```cpp
Enter name of data file: scores.txt
End of f i le reached.
Items read: 12
```

$um: 204.5

Average: 17.0417

程序说明

该程序没有使用硬编码文件名，而是将用户提供的文件名存储到字符数组filename中，然后将该数组用作open()的参数:

```cpp
inFile.open (f i lename};
```

正如本章前面讨论的，检查文件是否被成功打开至关重要.下面是一些可能出问题的地方:指定的文件可能不存在:文件可能位于另一个目录〈文件夹〉中:访问可能被拒绝:用户可能输错了文件名或省略了文件扩展名.很多初学者花了大嚣的时间检查文件读取循环的哪里出了问题后，缎终却发现问题在于程序没有打开文件.检查文件是否被成功打开可避免将这种将精力放在错误地方的情况发生.

读者需要特别注意的是文件读取循环的正确设计.读取文件时，有几点需要检查。首先，程序读取文件时不应超过EOF.如果最后一次读取数据时遇到EOF ，方法eof()将返回川队其次，程序可能遇到类型不匹配的情况.例如，程序消单6.16期望文件中只包含数字.如果最后一次读取操作中发生了类型不匹配的情况，方法fail( )将返回true(如果遇到了EOF，该方法也将返回true) .最后，可能出现意外的问题，如文件受损或硬件故障.如果撮后一次读取文件时发生了这样的问题，方法bad()将返回仕ue .不要分别检查这些情况，一种更简单的方法是使用good()方法，该方法在没有发生任何错误时返回true :

### 第 197 页

while I inFile . 900d () J 11. while‘ ïnput good and not. at EOF .

f

然后』如果愿意，百E以使用其他方法来确定循环终止的真正原因i

```cpp
ele s--''te elc EU•• eEF EE1
。.• 、zJf
n‘ecJ。υfaE r aw C UM AU .n k
```

"•-、

A s 。E a伽bn l町』。zτ. EE咱.A‘&性m、、·』

E，叫、Z叫、，、，、w

n.

-、主La、.‘A.、，，

```cpp
-cout r<< . "L:ntp4~ :' t erriliát èd by. data mismatc忖:-\n.~
e~se
cout << :' :H1put, termìnated for unknowlb reaso". \ 1\" ;
```

这些代码紧跟在循环的后面，用于判断循环为但终止.由于eo负)只能步IJ断是读到达EOF.而fa圳)可。--用于检查EE>F‘和类型不匹配，因此牛述代码-首先判断是否~J达EOF~这样，如-果执行到了elsei f 测试，便’可排除EOfo;因此，如果fair( )返回回ι便碍既定导致循环终止的原因是类型不匹配7￥.‘:’..:. ~ ..

}l法good()指出最后次i卖取输入的操作是否成功，这一点至关重妥r这意味着应该在执衍读JtY.输入的操作后，立刻应用这样测试。为此，一种标准方、法是，在循~之前ι首次执行循环测试前7放置一条输入语台i]“;并在循环的末尾C 下次执行循环测试之前〉放置另二，条输入语句、?

```cpp
11 s.tandard f孟le-readingloop design
inFìle >> value;-11 ge.t f irst value
while l inFi l e.good(}) 11 while input 900d and not at EOF
```

i

```cpp
// loop body goes-here
inFile >> value; // get next value
```

鉴圭阶下事实，可阳才上述代码迸行精简7菜达式inEile->>vafue的结果为inFi1e.而|在街妥.-“‘t- 0001值的悄况下，inFile的结果为inFi1e.g∞d()，即true或false .

因此，可以将两条输入语句用一条用作循环测试的输入语句代替。也就是说，可以将上述循环结构替换为如下循环结构:

```cpp
// abbreviat ed f i le- reading loop design
11 omit pre -l∞p input
while (inFile >>valuel 1/ read and test for success
/1 loop body goes here
/1 omi t end-of-loop i nput
```

这种设计仍然遵循了在测试之前进行读取的规则，因为要计算表达式inFile>> value的值，程序必须首先试图将一个数字读取到Uva1ue中.

至此，读者对文件1/。‘有了初步的认识.6 .9 总结

使剧号| 导程序选择不同操作的语句后，程序和编程将更有趣(这是否也自~51起程序员们的兴趣，我没有做过研究).C忡提供了i f 语句、if else 语句和switch语句来管理选项。i f语句使程序有条件地执行语句或说句块，也就是说，如果满足特定的条件，程序将执行特定的语句戎语句块。ife lse语句程序选择执行两个语句戎语句块之一.可以在这条语句后再加上ife1se.以提供一系列的选项.switch语句引导程序执行一系列地项之一.

C++还提供了帮助决策的运算符.第5章讨论了关系表达式，这种表达式对两个值进行比较.if和ife 1se

### 第 198 页

语句通常使用关系表达式作为测试条件.通过使用逻辑运算符C&&、11和! )，可以组合或修改关系表达式，创建更细致的测试。条件运算符(?:)提供于一科选择两个值之一的简洁方式.

cctype 字符函数J率提供了一组方便的、功能强大的工具，可用于分析字符输入.

对于文件uo 来说，循环和选择语句是很有用的工具:文件νo与控制台νo 极真相似。声明ifstream和ofstream对象，并将它们同文件关联起来后，便可以像使用cin 和cout 那样使用这些对象p

使用循环和决策语句丁便可以编军有趣的、智能的、功能混大的程序r 不过我们刚开始涉足C忡的强大功能，下一章将介绍函数。

## 6.10 复习二题

1.请看下丽两个计策空格和换行符数民的仪码片段=

```cpp
/ / Vers.i on 1-
whil'è (cin. get(ch)Jô' // quit 00 eof
ìf {ch "-= ' 'r
spaces+..;
```

ïf (ëh ==叫n‘)

```cpp
newlines++;
11 Vex:sion 2
whire-{cin. get(c~)) rrφit on eoι
if {ch == ' 'r
spaces++;
e Fse ff (Cn-== '、n')
new l'ine.s + +品
```

γ

策二种榕式比笼一种格式好在哪里呢?

2:-tE程序消单~ 6:之中丁二用ch+1替换++ch将发生什么情况呢?

3. i奇认臭考虑下面的程序:

```cpp
#include <豆。stream>
using namespace std;
int mai n ()
char ch;
int ctl , ct2;
ctl = ct2 = 0;
while ((ch = cin.get{)) != ' $' )
{
cout << ch;
ctl++i
if (ch = '$ ')
c t2++ i
cout << ch;
cout <<rlctl :. " << ct l <<" ct2 = " << ct2 << .'n'l;
return 0;
```

### 第 199 页

假设输入生u下〈请在每行末尾核回车键):

```cpp
HiI
Send $10 or $20 nowl
```

则输出将是什么(还记得吗，输入被缓冲)?

4.创建农示下述条件的逻辑表达式2

a. weight大于或等于115，但小于125.

b. ch为q或Q .

c. x为偶数，但不是26 .

d. x为偶数，但不是26的倍数。

e . donation为1000-2000或guest为1.

f. ch是小写字母或大写字母(假设小写字母是依次编码的，大写字母也是依次编码的，但在大小写字母间编码不是连续的〉。

5.在英语中，“1 will not not spealc ( 我不会不说) ”的意思与“1will spealc (我要说)”相同.在C++中，!!x是否与x 栩同呢?

6.创建一个条件表达式，其值为变霞的绝对值。也是说，如果变盘x为正，则表达式的值为X;但如果x为负，则表达式的值为-x一一这是一个正值.

7.用switch.&写下面的代码片段:

```cpp
if (ch == 'A')
a_grade++ i
elseif (ch== '8')
b_9rade++ ;
else if (ch == 'C')
c_grade++i
else if (ch == '0')
d_grade++;
else
f_grade++;
```

8.对于程序泊单6.10 ，与使用数字相比，使用字符〈如a和c)表示菜单选项和case 标签有何优点呢?〈提示:想想用户输入q 和输入5的情况。〉

9.请看下面的代码片段:

```cpp
int line = 0;
char ch;
while (cin.get(ch))
if (ch == 'Q')
break;
if (ch ! = ' \ n' )
continue;
line...+;
```

讷Æ:写该代码片段，不要使用brealc 和continuc语句。6 .11 主扁丰呈豆东习

J.编写一个程序，读取键盘输入，直到遇到@符号为止，并回显输入(数字除外)，同时将大写字符转换为小写，将小写字符转换为大写(jjlJ忘了cctype函数系列)。

### 第 200 页

2.编写一个程序，最多将10个donation值读入到一个double数组中〈如果您愿意，也可使用模板类array ).程序:ì1!1剑非数字输入时将结束输入，并报告这些数字的平均值以及数组中有多少个数字大于平均值.

3. 编写一个菜单驱动程序的雏形.该程序显示一个提供4个选项的菜单一一每个池项用一个字母标记。如果用户使用有效选项之外的字母进行响应，程序将提示用户输入一个有效的字母，直到用户这样做为止.然后，该程序使用一条switch语句，根据用户的选择执行一个简单操作。该程序的运行情况如下:

```cpp
Please enter one of the fol lowing choices:
c) carnivore p ) pianist
t) tree g ) garne
```

f

```cpp
Please enter a c , p , t, or g: q
Pl ease enter a c , p , t, or g : t
A rnaple is a tree .
```

4.加入BenevolentOrder of Programmer后，在BOP大会上，人们便可以通过加入者的真实姓名、头衔或秘密BOP姓名来了解他〈她).请编写一个程序，可以使用真实姓名、头衔、秘密姓名或成员偏好来列出成具.编写该程序时，请使用下面的结构=

```cpp
// Benevolent Order of Programrners name structure
struct bop {
char fullname(strsize); // r eal name
char title [strsi ze); // job ti tle
char bopname [strs i ze); // secre t BOP name
int preference; // 0 = fullname , 1 = title, 2 = bopname
```

该程序创建一个由上述结构组成的小型数组，并将其初始化为适当的值。另外，该程序使用一个循环，让用户在下面的选项中进行选择:

```cpp
a. display by name b . displ ay by title
c . display by bopname d. display by preference
q. quit
```

注意，“display by preference ”并不意味着显示成员的偏好，而是意咪着根据成员的偏好来列出成员。例如，如果偏好号为1.则选择d将显示程序，员的头衔.该程序的运行情况如下=

```cpp
Benevol ent Order of programrners Report
a. display by narne b . displ ay by ti t l e
c . d i splay by bopname d. display by preference
q . qult
Enter your choice: a
Wirnp Mach口
Raki Rhodes
Celia Laiter
Hoppy Hipman
Pat Hand
Next choice: d
Wirnp Mach。
Junior programmer
MIPS
Analyst Trainee
LOOPY
Next choice: q
Bye!
```

5.在Neutronia 王国，货币单位是tv呵，收入所得税的计算方式如下:

### 第 201 页

5000 tvarps:不收税

```cpp
5001 -15000 tvarps: 10%
15001 -35000tvarps: 15%
35000 tvarps以上:20%
```

例如，收入为3 8000tvarps 时，所得税为5000x 0.00 + 10000 x 0. 10 + 20000 x 0.15 + 3000 x 0.20. I‘!p 4600 tvarps.请编写一个程序，使用循环*要求用户输入收入，并报告所得税。当用户输入负数或非数字时，循环将结束.

6.编写一个程序，记录捐助给“维护合法权利自1休”的资金.该程序要求用户输入捐献者数目，然后要求用户输入何一个捐献者的姓名和款项.这些信息被储存在一个动态分配的结构数组中。每个结构有两个成员:用来储存姓名的字符敬组〈或string 对象)利用来存俯款项的doub!e成员.读取所有的数据后，程序将显示所有捐款超过1 0000的捐款者的姓名及其捐款数额.该列表前应包含一个标题，指出下面的捐款者是重姿销款人(GrandPatrons)。然后，程序将州出其他的捐款者，该列表要以Patrons开头。如果某种类别没有捐款者，贝。程序将打印且在词“none”。该程序只显示这两种类别，而不进行排序.

7.编写一个和-序，官每次读取一个单词，直到用户只输入q 。然后，该程序指出有多少个且在词以元音打头.有多少个单词以辅音打头，还有多少个单词不属于这两类。为此，刀法之一是，使用isalpha()来18:分以字母和其他字符打头的.Q‘1 词，然后对于通过了isalpha()测试的单词，使周if 或switch语句来确定哪些以元音打头.该程序的运行悄况如下:

```cpp
Enter words (q to qui t l :
The 12 awesome oxen a皿b led
quiet1y across 1 5皿etersof lawn . q
5 words beginning with vowels
4ω。rdsbeginning with consonants
2 others
```

8.编写一个程序，它打开一个文件文件，逐个字符地读取该文件，且主IJ到达文件末尾，然后指出该文件中包含多少个字符。

9.完成编程练习6.但从文件中读取所需的信息.i亥文件的第一项应为捐款人数，余下的内容应为成对的行。在每一对中，第一行为捐款人姓名，第二行为捐款数额.f!P该文件类似于下面.

4

Sam Stone

2000

preida Flass

100500

Tammy Tubbs

5000

Rich Raptor

55000

---

本章对应原书小节结构见文件开头。
