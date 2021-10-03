# 本地化格式字符串 
Time:<em>5  分钟</em>

如果在游戏过程中需要实时更新字符串，例如显示玩家名称或使用计时器时，可以将**格式字符串**用作本地化翻译中的占位符。

![](https://developer.roblox.com/assets/bltd1f6fd7d58869347/Format-Strings-pt.jpg) 显示游戏中物品的数量。

![](https://developer.roblox.com/assets/blt0ff6755149222f8c/Format-Strings-username.jpg) 在消息中显示玩家的 Roblox 用户名。

![](https://developer.roblox.com/assets/blt9be06795530968f0/Format-Strings-score.jpg) 使用本地化分隔符显示高分。

## 构造格式字符串

格式字符串由**参数**和可选的**格式说明符**组成，格式说明符控制参数值的输出/格式化方式。

**{NumJewels**
**:**
**int}**

![](https://developer.roblox.com/assets/blt520577ecaffd5e7d/u-arrow-blue.png)


![](https://developer.roblox.com/assets/blt520577ecaffd5e7d/u-arrow-blue.png)



参数
可选的格式说明符

参数可以采用**命名**或**编号**风格。一个条目的所有参数必须使用相同的风格，不能同时使用命名和编号。

![](https://developer.roblox.com/assets/blt2de4b75f8a635fad/Circle-Y.png)



${1:fixed} cash and {2:int} jewels 

![](https://developer.roblox.com/assets/blt2de4b75f8a635fad/Circle-Y.png)



${AmountCash:fixed} cash and {NumJewels:int} jewels 

![](https://developer.roblox.com/assets/blt31c7fd261f84f0cc/Circle-N.png)



${1:fixed} cash and {NumJewels:int} jewels 

## 使用格式说明符

如上所述，格式字符串中可以包含可选的**格式说明符**。下表列出了每个说明符及其预期用途。

说明符 类型 描述 示例输出

**translate**
字符串
尝试在连接之前翻译参数（在同一上下文中）。这将只查找文本 **Source（源）**匹配，它不支持递归匹配。

**int**
数值
带有可选负号的整数； 没有千位分隔符。
1234

**fixed**
数值
带小数指示符的两位小数，带可选的负号，无千位分隔符。
1234.50

**num**
数值
带小数指示符的两位小数，带可选的负号和千位分隔符。
1,234.50  
1 234,50

**HEX**
数值
整数转换为十六进制；负数转换为 64 位二进制补码。
3FF

**hex**
数值
与 **HEX** 相同，但为小写。
3ff

**datetime**
数值
UTC 时间戳，作为通用的用户可读格式的数值。
2017-10-10 13:38:10

**iso8601**
数值
UTC 时间戳，作为 ISO-8601格式 UTC 时间的数值。
2017-10-12T22:02:38Z

**shorttime**
数值
本地“hour:minute”格式的 UTC 时间戳。
1:45 PM  
13:45

**shortdatetime**
数值
通用的日期+时间模式（短时间）的 UTC 时间戳。
10/10/2017 1:45 PM

**shortdate**
数值
短日期模式的 UTC 时间戳。
10/10/2017  
2017-10-10

### 非本地化替换

如果**未**包含格式说明符，则将完全按照给定的值显示参数值。这对于直接替换不会在语言之间更改的字符串（例如，专有名称、标题等）非常有用。

C
D
E
F

**源**
示例
**es**

Hello {Player_Name}!
Hola {Player_Name}!

My name is {NPC_Name}.
Me llamo {NPC_Name}.

示例输入 英语输出 西班牙语输出

Hello new_storm!
Hello new_storm!
Hola new_storm!

My name is Diva Dragonslayer.
My name is Diva Dragonslayer.
Me llamo Diva Dragonslayer.

### 本地化替换

当需要针对不同的区域设置直接翻译字符串时，**translate** 格式说明符将查找精确的参数匹配并替换翻译，前提是本地化门户中存在该翻译。

C
D
E
F

**源**
示例
**es**

I am from {Country_Name:translate}.
Soy de {Country_Name:translate}.

Brazil
Brasil

London
Londres

Germany
Alemania

示例输入 英语输出 西班牙语输出

I am from Brazil.
I am from Brazil.
Soy de Brasil.

I am from London.
I am from London.
Soy de Londres.

I am from Germany.
I am from Germany.
Soy de Alemania.

### 数值替换

若要以特定格式输出变量数值，请使用诸如 **int**, **fixed**, or **num** 之类的说明符。

C
D
E
F

**源**
示例
**es**

{race_time:fixed} seconds
{race_time:fixed} segundos

${1:num} cash and {2:int} jewels
${1:num} dinero y {2:int} joyas

示例输输入 英语输出 西班牙语输出

75.202844 seconds
75.20 seconds
75,20 segundos

$2500.5 cash and 99.8 jewels
$2,500.50 cash and 100 jewels
$2.500,50 dinero y 100 joyas

## 示例实现

考虑采用多种语言显示可变数量珠宝的实际示例。若要在游戏中实现此功能：

  1. 如`articles/localization portal additional features#localizing-with-csv-files|此处`所述，从本地化门户下载 .csv 电子表格。
  2. 插入带有命名格式字符串的 **Source** 字符串，以及支持语言的翻译，如 **es**（西班牙语） and **pt**（葡萄牙语）。

C
D
E
F
G

**源**
示例
**es**
**pt**

{NumJewels} jewels
{NumJewels} joyas
{NumJewels} jóias

翻译中使用的所有参数也必须出现 在**Source（源）**字符串中。如果没有，或者如果存在冲突的格式说明符，则该条目将不会用于翻译文本。 ****

  3. 向游戏中添加一个 GUI 对象，例如`TextLabel/Text|Text` （文本）属性为 **100 jewels** 的 `TextLabel`。
![](https://developer.roblox.com/assets/blt83cc36a6081801ad/Format-Strings-en.jpg)

确保标签与 **Source（源）**字符串的“模式”相匹配。例如，格式字符串后面的文本应为区分大小写匹配，为 **jewels**，而不是 **Jewels** 或 **JEWELS**。 ****

  4. 上传电子表格并按照`articles/localization portal additional features#upload-csv-file|此处`所述对游戏进行测试。翻译应该出现在游戏中的 GUI 实例上，包括变量 100。

![](https://developer.roblox.com/assets/blte4ef6dfda3c2266c/Format-Strings-en-2.jpg) 英语

![](https://developer.roblox.com/assets/bltf8ceb3372f5a5f7f/Format-Strings-es.jpg) 西班牙语

![](https://developer.roblox.com/assets/bltd1f6fd7d58869347/Format-Strings-pt.jpg) 葡萄牙语



***__Roblox官方链接__:[本地化格式字符串](https://developer.roblox.com/zh-cn/articles/localization-format-strings)