# Lua 中的类型强制转换 
Time:<em>5  分钟</em>

“Type Coercion”（类型强制转换）指将值从一种类型_隐式_或_自动_转换成另一种类型的过程。在 Lua 环境中，此类转换指从字符串转化为数字或从数字转化为字符串。

为了执行计算，Lua 会自动将字符串和数字类型转换为正确的格式。举例来说，如果开发者对字符串应用算术运算，则 Lua 会首先尝试将该字符串转换为数字，否则运算将无法执行。如果该字符串无法被转换为数字，则会引发错误。

## 串联期间

使用串联（Concatenation）运算符时，Lua 会将数字转换为字符串。请参考下列示例：

  * `print("This is Lua version " .. 5.1 .. " we are using.")`
    * 输出：This is Lua version 5.1 we are using.
  * `print("Pi: " .. math.pi)`
    * 输出：Pi: 3.1415926535898
  * `print("Pi: " .. 3.1415927)`
    * 输出：Pi: 3.1415927

如上所示，开发者无法在强制转换中完全控制转换的格式。若希望将数字格式化为字符串，则可以使用 `string.format()` 函数。请参考下列示例：

  * `print(("%.3f"):format(5.1))`
    * 输出：5.100
    * _注意小数点后有三位。_
  * `print("Lua version " .. ("%.1f"):format(5.1))`
    * 输出：Lua version 5.1

以上示例使用了函数对数字进行转换，因此为显式转换而不是强制（隐式）转换。

## 算数运算期间

在考虑转换方式时，开发者应当尽可能避免使用强制转换。虽然强制转换有一定成效，但并非是最佳实践方法。举例来说，当函数可以接受转换前的数字时，数字转换就并非必要操作。即使如此，还请开发者尽可能对强制转换进行避免。

**示例**

  * `print(100 + "7")`
    * 输出：107
  * `print("1000" + 234)`
    * 输出：1234
  * `print(234 + "1000")`
    * 输出：1234
  * `print("hello" + 234)`
    * 输出：尝试对字符串值执行算术运算

由上可见，当字符串可以被转换为数字时，计算将会成功运行。字符串 “hello” 无法被转换为数字，因此触发了错误信息。由于在 C 语言等静态类型语言中无法将值分配给不兼容类型的变量，此操作在该类程序语言中将会导致错误。但因为 Lua 为动态类型语言，此操作可以正常运行。

## 比较期间

需要注意的例外：比较（Comparison）运算符（也就是 ==、~=、<、>、<= 和 >=）**无法**强制转换其参数。不等或等号运算符并不认为数字等同于其字符串表示形式或任何非数字形式。当向有序比较运算符提供非数字的类型时，其将会触发错误：

  * `print(100 == "100")`
    * 输出：false
  * `print(100 ~ "hello")`
    * 输出： true
  * `print(100 ~ {})`
    * 输出： true
  * `print(100 == tonumber("100"))`
    * 输出：true
  * `print(100 < "100")`
    * 输出：尝试比较数字和字符串

## 其他类型的强制转换

强制转换不仅局限于数字和字符串。Roblox 中同样存在其他的强制转换情况。

### 枚举

枚举（Enum）为其中之一。当在需要枚举或数字的地方使用字符串或数字时，该字符串或数字将被强制转换为枚举。

以下三个示例的效果相同，都会创建一个部件并使其具体化：
    
    
    local p1 = Instance.new(**Part**)
    p1.Material = 816
    p1.Parent = workspace
    
    local p2 = Instance.new(**Part**)
    p2.Material = **Concrete**
    p2.Parent = workspace
    
    local p3 = Instance.new(**Part**)
    p3.Material = Enum.Material.Concrete
    p3.Parent = workspace
    

### TimeOfDay

强制转换的另一个示例是照明的 TimeOfDay 属性。此属性可设置服务器的当前时间。也就是说，开发者可以通过此属性定义游戏世界现在处于晚上、白天或其他任何时间。TimeOfDay 属性为字符串，但向其发送数字类参数时仍然可以正常运行。

下列两个示例中前者使用数字，后者使用字符串。两者的效果相同：
    
    
    game.Lighting.TimeOfDay = 5
    print(game.Lighting.TimeOfDay)
    

输出为 “05:00:00”
    
    
    game.Lighting.TimeOfDay = "05:00:00"
    print(game.Lighting.TimeOfDay)
    

输出为 “05:00:00”

## 另请参阅

  * [Lua 5.1 参考手册：强制转换](http://www.lua.org/manual/5.1/manual.html#2.2.1)



***__Roblox官方链接__:[Lua 中的类型强制转换](https://developer.roblox.com/zh-cn/articles/Type-Coercion-in-Lua)