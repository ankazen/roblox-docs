# 基础字符串模式 
Time:<em>5  分钟</em>

**字符串模式**是一种字符组合，可用于查找存在于较长字符串当中的具体片段（通常称为_子字符串_）。

在您的游戏中，您可以使用字符串模式找到一个单词中的所有字母 **A**，或者查找句子中的数字。

## 简单匹配

简单的匹配可以通过 Lua 的 `Lua Libraries/string|string.match()` 函数来完成。此示例中，我们将在两个字符串中查找单词 **Roblox**：

```    
    
    print( string.match("Welcome to Roblox!", "Roblox") )
    print( string.match("Welcome to my awesome game!", "Roblox") )
    
    
    Roblox
    nil

```
如您所见，我们在第一个字符串中找到了匹配项，因此向控制台输出了 `Roblox`。但我们在第二个字符串中**没有**找到匹配项，所以输出了 `nil`。

## 完美匹配

简单匹配的作用是很有限的，最多只能实现这样的查找。下面请考虑这三种陈述：

**云之国有 25 个力量宝石**

**闹鬼矿洞有 10 个力量宝石**

**巫师村有 50 个力量宝石**

假设您只想提取每个世界中“力量宝石”的数量(**25**、**10** 或 **50**)，因为每个世界中的宝石数量不同，所以您并不能使用简单匹配，而需要使用**字符类**搜索每条语句。

简单地说，字符类提供了一种方法，能用来搜索并不_具体_但又符合某一已知类别（类）的内容。在 Lua 中，您可以在字符串中搜索**字母**、**数字**、**空格**、**标点符号**等。

![](https://developer.roblox.com/assets/bltad916cfeb252618d/Character-Tiles.png)



下表中是一些常见的和有用的字符类：

类 代表 匹配示例

`.`
任意字符
`32kasGJ1%fTlk?@94`

`%a`
任意大小写的字母
`aBcDeFgHiJkLmNoPqRsTuVwXyZ`

`%l`
小写字母
`abcdefghijklmnopqrstuvwxyz`

`%u`
大写字母
`ABCDEFGHIJKLMNOPQRSTUVWXYZ`

`%d`
任意数字
`0123456789`

`%p`
任意标点符号
`!@#;,.`

`%w`
任意数字或字母
`aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789`

`%s`
空格或空格字符
`_`、`\n` 和 `\r`

## 使用字符类

上面的表格可能看起来难以消化，但是不要担心，我们将通过一些基本的示例向您展示它的作用。

首先让我们看看这个陈述：

**云之国有 25 个力量宝石**

在表中我们可以看到 `%d` 字符类允许您在字符串中查找**数字**，正好就能用来找出每个虚构的游戏世界中有多少“力量宝石”！让我们来试试这些代码：

```    
    
    print( string.match("The Cloud Kingdom has 25 power gems", "%d") )
    
    
    2

```
注意这段代码输出的是 `2`— 可是云之国有 **25** 个力量宝石，而不是 2 个呀！那到底出了什么问题呢？

有关字符类的一个重要细节是，它们本身只匹配字符串中的**一个**字符。上面的模式（`%d`）从左到右开始读取字符串，查找它找到的_第一个_数字（`2`），然后就停止了！

好在您还可以使用**量词**来扩展字符类的功能。

## 量词

**Quantifier**（量词）是在字符类之后键入的符号，它允许您匹配特定数量的某类字符。

量词 含义

`+`
匹配大于等于 1 个指定类别的字符

`-`
匹配尽可能少的指定类别的字符

`*`
匹配大于等于 0 个指定类别的字符

`?`
匹配小于等于 1 个指定类别的字符

让我们使用量词来找到云之国力量宝石的正确数量吧：

```    
    
    local pattern = "%d+"  -- 注意 '+' 量词要在 '%d' 之后
    
    print( string.match("The Cloud Kingdom has 25 power gems", pattern) )
    
    
    25

```
如您所见，此模式找到第一个数字（`2`），并继续查找到了 `5`！而且它还会继续查找更多的数字（如果它们存在），例如：

```    
    
    local pattern = "%d+"
    
    print( string.match("The Cloud Kingdom has 25 power gems", pattern) )
    print( string.match("The Cloud Kingdom has 25001000 power gems", pattern) )
    
    
    25
    25001000

```
## 组匹配

…

## 字符串捕捉

…



***__Roblox官方链接__:[基础字符串模式](https://developer.roblox.com/zh-cn/articles/basic-string-patterns)