# 可变参函数 
Time:<em>5  分钟</em>

可变参函数（Variadic Function）与只能接收指定数量参数的常规函数不同，可以接收任意数量的参数。

### 库中的可变参函数

Lua 和 Roblox 的库中包括多个可变参函数。许多开发者都未意识到，我们所常用的 `print()` 函数就是十分典型的可变参函数。

**代码**
    
    
    print(2, "+", 2, "=", 2+2)
    print( string.format("The %s is a %s!", "cake", "lie") )
    print( string.byte(115, 101, 99, 114, 101, 116) )
    

**输出**
    
    
    2 + 2 = 4
    The cake is a lie!
    secret
    

### 可变参函数的使用

定义可变参函数时，开发者应当使用 `...` 符号作为该函数的最后或唯一参数（请勿将其与两个句点构成的串联运算符 `..` 混淆）。这个由三个句点构成的符号稍后可在该函数中作为变量集合使用。在大多数情况下，最为便利的做法是将所有实参都打包至表（table）中：

**代码**
    
    
    local function variadic(named, ...)
        local arguments = {...} -- 将额外参数打包至表中
        print("Named argument = ", named)
        for i, value in ipairs(arguments) do
            print("Input No. ", i, "=", value)
        end
    end
    
    variadic(10, "Hi", 20, "Variadic Function")
    

**输出**
    
    
    Named argument = 10
    Input No. 1 = Hi
    Input No. 2 = 20
    Input No. 3 = Variadic Function
    

同时，我们也可以运用此功能来编写 “sum”（总和）函数：

**代码**
    
    
    function sum(...)
        local sum = 0
        for _, value in ipairs({...}) do
            sum = sum + value
        end
        return sum
    end
    print( sum(1, 2, 3, 4) )
    print( sum(9, 8, 7, 6, 5, 4, 3) )
    

**输出**
    
    
    10
    42
    

#### 实参传递

此功能的另一个常见用法为对实参的传递。在以下示例中，假设开发者需要在调用函数前后分别进行打印（print）：
    
    
    local function printAround(func)
        print("Before")
        func()
        print("After")
    end
    
    local function foo()
        print("bar")
    end
    
    printAround(foo)
    

**输出**
    
    
    Before
    bar
    After
    

当我们希望为 `foo()` 添加参数时，可以使用 `...` 符号进行以下处理：

**代码**
    
    
    local function printAround(func, ...)
        print("Before")
        func(...)
        print("After")
    end
    
    local function foo(x, y, z)
        print("x =", x)
        print("y + z =", y + z)
    end
    
    printAround(foo, 1, 2, 3)
    

**输出**
    
    
    Before
    x = 1
    y + z = 5
    After
    

#### 从实参表中调用可变参函数

当需要将值表传递给可变参函数时，开发者可以使用 `unpack()` 函数。

**代码**
    
    
    local squares = {1, 4, 9, 16, 25}
    print( "The first 5 square numbers are:", unpack(squares) )
    

**输出**
    
    
    The first 5 square numbers are: 1 4 9 16 25
    请注意：如果开发者编写了能够获取可变参数的函数，且正在对多个值表使用 unpack 函数，则应当考虑将表直接传递给函数本身。
    



***__Roblox官方链接__:[可变参函数](https://developer.roblox.com/zh-cn/articles/Variadic-Functions)