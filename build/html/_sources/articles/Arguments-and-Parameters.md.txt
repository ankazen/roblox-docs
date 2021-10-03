# 实参和形参 
Time:<em>10  分钟</em>

在函数的定义中，形参的正式名称是变量。而实参的正式名称则是调用函数时出现在函数中的值。让我们看看下面这段代码：
    
    
    local function printStuff(x) -- 这是一个函数，含有一个形参 x。
    	print(x)
    end
    
    printStuff("Hello world.") -- "Hello world.” 是一个实参
    

在本例中，_x_ 是函数 _printStuff_ 的一个形参。形参始终会以这种格式来声明，即位于函数声明的括号内。

在这个函数中，有一个语句 `print(x)`。该语句会将 _x_ 包含的任何值打印到输出结果中。即便 _x_ 未定义且为空，编译器也不会提示错误，因为该函数尚未被调用。

### 定义含有形参的函数

以下是定义函数的基本语法：

`function name(argument1, arg2, arg3, ...)` – 只有在需要的情况下才插入实参

定义函数时，你可以使用形参。因为函数可针对多个值执行任务，所以形参十分实用。例如：
    
    
    local function addNumbers(x, y)
    	return (x + y) -- 你可能希望了解 return 语句
    end
    

上一段代码包含两个形参，因此当调用该函数时，由于 `return (x + y)` 语句，我们可以向形参 **x** 和 **y** 插入**任意**两个值并返回其和。当前 _x_ 和 _y_ 没有值，但在调用函数时，将会赋予形参 _x_ 和 _y_ 值。请注意，由于函数在声明后会存储于计算机内存中，因此在调用前不会提示错误（除非一开始就存在语法错误）。若情况并非如此，就会像包含以下脚本一样报错：`print(x + y)` \--> `attempt to perform arithmetic on global x (a nil value)`。

形参非常有助于构成能够执行多重任务的函数。

请注意，对于函数及其递减区间来说，所有形参都属于本地参数。

### 调用含有实参的函数

调用含有实参的函数十分简单，与调用不含实参的函数十分相似。以下是调用含有实参的函数的基本语法：

`functionName(value1, value2, value3, ...)` – 调用任意数量的实参

请注意，在上述语法中，你在函数声明中创建的第一个形参会变为与 _value1_ 相等，而第二个形参则与 _value2_ 相等，以此类推。

让我们用上一个示例来进行本次演示。
    
    
    local function addNumbers(x, y)
    	return (x + y)
    end
    
    local sum = addNumbers(2, 5) -- 注意我是如何调用函数的（请注意，返回值时，函数会包含返回的值）
    print(sum) -- 7
    

**注意：**当调用含有实参的函数时，可以使用任意所需数量的实参。调用的实参过多时，代码将忽略过量的实参；而调用的实参过少时，未表现的形参将返回为空。

#### 可变实参

你可能已发现，诸如 `print()` 等全局函数可能采用数量不限的实参。无论有多少个实参，它都会将其所有实参打印到输出结果中（每个打印值之间都有一个空格）。例如：
    
    
    print("LOL", "OMG", "C++ IS PRETTY NEAT IF YOU ASK ME", 1241425717231) -- 4 个实参
    print(1, 122, "Hi!", "Roblox", "Give it your best shot!", "C++", "Interesting") -- 7 个实参
    

看一下输出结果，你将再次看到所有实参都打印在输出结果中。在自定义函数中，你同样可以加入任意数量的实参！字符组 “…” 代表可变实参。请观察以下代码：
    
    
    local table1 = {}
    
    local function appendToTable(tab, ...)
    	local args = {...} -- 你可能希望了解该示例的表格
    	for i, v in pairs(args) do
    		table.insert(tab, v)
    	end
    end
    
    appendToTable(table1, "xD", ":D", "lol")
    

含有实参的函数能够实现非常强大的功能，因为它们可以在脚本的开头声明，并能以各种方式用于整个代码中。存储经常用作函数的代码可以让脚本制作变得格外轻松。



***__Roblox官方链接__:[实参和形参](https://developer.roblox.com/zh-cn/articles/Arguments-and-Parameters)