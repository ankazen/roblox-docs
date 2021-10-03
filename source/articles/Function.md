# 函数 
Time:<em>10  分钟</em>

**函数**是可以在脚本中多次使用的指令集。定义后，可以通过命令执行函数，也可以通过`/articles/events|事件`触发函数。

## 定义函数

基本函数声明包括 `function` 关键字，后跟**函数名**和一对圆括号 (`()`)。由于函数的主体是一个代码块，因此必须用 `end` 关键字将其关闭。

```    
    
    local function addNumbers()
    
    end


```
在 `()` 和 `end` 之间是命令和其他代码组成函数**主体**。这些命令将在调用函数时执行：

```    
    
    local function addNumbers()
    	-- Function body
    	print("Function called!")
    end


```
## 调用函数

定义函数之后，便可以通过**调用**来执行（函数不会自己执行）。若要调用函数，只需键入其名称，后跟括号 (`()`) 即可：

```    
    
    local function addNumbers()
    	-- Function body
    	print("Function called!")
    end
    
    addNumbers()
    
    
    Function called!

```
## 函数参数

函数可以利用**参数**传递数据。声明函数时，可以在括号中包含一个或多个参数名：

Function Example 2 ```    
    
    -- num1 and num2 are the parameters
    function add(num1, num2)
    	print(num1 + num2) 
    end
     
    -- 3 and 4 are the arguments
    add(3, 4)
    
    
    7

```
调用带有参数的函数时，请指定应传递给函数的**值**。例如，以下函数接受每次调用期间传入的两个数字，将它们相加，并输出结果：

```    
    
    local function addNumbers(num1, num2)
    	local result = num1 + num2
    	print(num1 .. " + " .. num2 .. " = " .. result)
    end
    
    addNumbers(2, 3)
    addNumbers(4, 0.5)
    addNumbers(1000, 500)
    
    
    2 + 3 = 5
    4 + 0.5 = 4.5
    1000 + 500 = 1500

```
函数参数始终是函数的本地参数，仅在函数的`/articles/Scope|作用域`及其下级作用域中使用。 

如果调用的 Lua 函数的参数比预期的多，多余的参数将被忽略。相反，如果函数期望的参数比你提供的多，则值 `nil` 将用于所有缺少的参数。 

## 返回值

除了接受参数外，函数还可以**返回**（发回）数据给调用命令。这是通过 `return` 值完成的。根据上面的例子，下面的函数**返回**总和，而不是输出：

Function Example 3 ```    
    
    function add(num1, num2)
    	print("Finding sum.") 
    	return num1 + num2 
    	--print("Sum found") 
    end
     
    x = add(5, 2) 
    print(x)
    
    
    Finding sum.
    7

```
不要在 `return` 命令之后放置任何命令，因为这样做将生成错误。 

当一个函数返回一个值时，它可以被分配给一个变量，或者在任何可以使用变量的地方使用。以下代码说明了这一概念：

Function Example 4 ```    
    
    function addNumbers(num1, num2)
        return num1 + num2
    end
     
    a = addNumbers(3, 5)
    print(a)
    
    
    8

```
与某些编程语言不同，Lua 甚至允许你从函数返回多个值：

```    
    
    local function addAndSubtract(num1, num2)
    	local sum = num1 + num2
    	local difference = num1 - num2
    	return sum, difference
    end
    
    local sum, difference = addAndSubtract(2, 3)
    print(sum)
    print(difference)
    
    
    5
    -1

```
## 其他函数技巧

### 事件触发的函数

函数并不总是需要用命令调用，它们也可以通过**事件**调用。有关详细信息，请参阅`/articles/events|处理事件`一文。

### 匿名函数

函数可以**匿名**创建，也就是说，不需要为它们分配名称。当需要从另一个函数或事件的结果调用函数时，这非常有用，例如 `delay()` 调用或 `/Players/PlayerAdded|PlayerAdded` 事件连接：

```    
    
    delay(2, function(exactTimeElapsed)
    	print(exactTimeElapsed)
    end)
    
    
    2.0064592329945

```
```    
    
    local Players = game:GetService("Players")
    
    Players.PlayerAdded:Connect(function(player)
    	print(player.Name .. " joined the game!")
    end)


```
请注意，匿名函数仍然需要在包含的函数或事件的结束符 `)` 之前先闭合 `end`，例如 `delay()` 或 `:Connect()`。 

### 表中的函数

由于函数是 Lua 数据类型，因此可以将它们存储在表中。 此技巧通常用于 `ModuleScript|ModuleScripts`，其中模块的表包含各种函数：

```    
    
    local MathModule = {}
    
    function MathModule.addNumbers(num1, num2)
    	local sum = num1 + num2
    	return sum
    end
    
    function MathModule.subtractNumbers(num1, num2)
    	local difference = num1 - num2
    	return difference
    end
    
    return MathModule


```
一旦包含在模块的表中，这些函数就可以被任何通过 `require()` 访问 `ModuleScript` 的脚本调用：

```    
    
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    -- Require module
    local MathModule = require(ReplicatedStorage:WaitForChild("MathModule"))
    
    local sum = MathModule.addNumbers(2, 3)
    print(sum)
    local difference = MathModule.subtractNumbers(2, 3)
    print(difference)
    
    
    5
    -1

```


***__Roblox官方链接__:[函数](https://developer.roblox.com/zh-cn/articles/Function)