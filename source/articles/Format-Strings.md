# 格式字符串 
Time:<em>地理位置探查</em>

在部分应用程序中， Roblox 会使用拥有地理位置探查能力的**格式字符串**作为字符串匹配与格式重组的模式。举例来说，可以将格式字符串与 `LocalizationService` 自动文本替换与 `Translator` API 同时进行运用。

## 参数

格式字符串中的**参数**利用类似 `{1}` 的波形括号进行标记。为了便于识别认可，参数必须拥有明确的**序号**或**命名**。

当在格式字符串中使用参数时，请参考以下规则：

  * 使用数字作为序号的参数需要使用索引开头为1的编号方式，例如 `{1}` 、 `{2}` 等。
  * 为序号命名时需要采取例如 `{user}` 或 `{item}` 等的格式。
  * 命名类与序号类参数不能同时出现在同一格式字符串中！
  * 空字符串指示符 `{}` 可以用来代表空字符串，但括号的前后不能出现任何字符，否则指示符将无效。
  * 文本中的波形括号需要采用例如 `{{` 或 `}}` 等格式进行转义。

## 格式说明符

**格式说明符**的用途是控制参数值的格式，可用在地理位置探查的数字、日期以及时间格式上。

格式说明符可被放置在参数的名称/索引后方，使用 `:` 进行间隔。例如：

  * `{1:int}`
  * `{2:fixed}`
  * `{gametime:shorttime}`

说明符 格式 描述 输出示例

**int**
数字
可带负号的整数，无千位分隔符。
1234

**fixed**
数字
带小数点的两位小数数字，可带负号，无千位分隔符。
1234.50

**num**
数字
带小数点的两位小数数字，可带负号，有千位分隔符。
1,234.50  
1 234,50

**HEX**
数字
转换为十六进制的整数，负数将被转换为64位二进制补码。
3FF

**hex**
数字
与**HEX**相似，但使用小写字母。
3ff

**datetime**
数字
UTC 时间戳转换为数字格式，全世界用户通用格式。
2017-10-10 13:38:10

**iso8601**
数字
UTC 时间戳转换为数字格式， ISO-8601 格式的 UTC 时间。
2017-10-12T22:02:38Z

**shorttime**
数字
UTC 时间戳，转换为当地“小时：时间”格式。
1:45 PM  
13:45

**shortdatetime**
数字
UTC 时间戳，转换为通用日期+时间简短格式。
10/10/2017 1:45 PM

**shortdate**
数字
UTC 时间戳，转换为简短日期格式。
10/10/2017  
2017-10-10

**translate**
字符串
在（以相同上下文）串联前尝试翻译参数。该功能只会寻找 **Source（源）**中的字面匹配 — 并不支持递归匹配。

（无说明符）
字符串
插入字符串

（无说明符）
数字
整数时为 **int** ；非整数时为 **fixed** 。

使用类似 `translate` 等**字符串**类格式说明符的参数会尽可能与任何子字符串进行匹配，这点与 Lua 的 `.*` `Articles/string patterns reference|string pattern` 有些相似。而其它的说明符会更为严格。 

## 本地化匹配

在`Articles/Roblox Localization Tools|游戏本地化`中经常会用到格式字符串。在该应用程式中，如果在 **Source （源）**中出现了包含非空格式字符串的 `LocalizationTable` 条目，则该条目也将会被用来进行匹配。

请看下面 CSV 导入文件中的翻译示例：

D
E
F

Source
es-es

${1} Cash
${1} Efectivo

Hello {user}!
Hola {user}!

将其正确导入 `LocalizationService` 后，如果游戏中会出现上面写着 “$1000 Cash”的 GUI `TextLabel`，当西班牙语玩家进行游玩时，自动翻译功能会将其渲染成 “$1000 Efectivo”。

同时， `Translator/Translate|Translator:Translate()` 也可被用来返回翻译好的字符串。示例如下：

```    
    
    local players = game:GetService("Players")
    local localizationService = game:GetService("LocalizationService")
    
    local translator = localizationService:GetTranslatorForPlayer(players.LocalPlayer)
    local cashLabelInstance = game.StarterGui.ScreenGui.CashLabel
    
    local cashLabelTranslation = translator:Translate(cashLabelInstance, "$1000 Cash")
    print(cashLabelTranslation)
    
    
    $1000 Efectivo

```
用来进行翻译的所有参数都需要在 **Source（源）**字符串中存在。如果参数不存在，或出现了冲突的格式说明符，则该条目将不会用来进行文本翻译。 

如果出现两条有同一 **Source（源）**的条目，例如 “Play”，自动翻译功能将会在上下文对比更差的字面匹配与上下文对比更佳的参数化匹配中选择前者。 



***__Roblox官方链接__:[格式字符串](https://developer.roblox.com/zh-cn/articles/Format-Strings)