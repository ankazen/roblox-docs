# 协同程序初学者指南 
Time:<em>10  分钟</em>

协同程序是 Lua 语言中最为有趣实用的组成部分之一，但同时也是 Lua 脚本编写中最容易被误解的概念之一。创建新的协同程序与在场景中创建新的脚本有些相似。在 Roblox 环境中，创建新脚本和新协同程序间最大的不同处之一在于创建新脚本时无需对其上下文进行创建。此区别在部分情况下能够节省执行时间。

Lua 的这些特性允许了多个线程的并行运行，无需创建单独的脚本实例或等待当前运行的代码块完成。

## 协同程序的创建

协同程序的创建其实较为简单，只需一个函数与 `coroutine.create()` 即可开始创建。其中，`coroutine.create()` 的参数即为需要进行运行的函数。请参考下列示例：
    
    
    local newThread = coroutine.create(function()
        print("hola")
    end)
    

遵循以上示例，你应该已经创建了属于自己的第一个协同程序，并启动了新的线程。但如果想要其开始工作，仍然需要对其进行运行：只需使用 `coroutine.resume()` 即可，其参数将为你所创建的线程。
    
    
    local newThread = coroutine.create(function()
        print("hola")
    end)
    
    coroutine.resume(newThread)
    

###### 输出结果：
    
    
    hola
    

当想要在协同程序中调用参数时，需要以如下方式使用 `coroutine.resume()`：
    
    
    local newThread = coroutine.create(function(a, b, c)
        print(a*b + c)
    end)
    
    coroutine.resume(newThread, 3, 5, 6)
    

###### 输出结果：
    
    
    21
    

## coroutine.wrap()

`coroutine.wrap()` 可以用来替代 `coroutine.resume()` 和 `coroutine.create()`。在函数上使用 `coroutine.wrap()` 的方法与 `coroutine.create()` 类似，但你将像函数一样使用为其分配的变量。可以将 `coroutine.wrap()` 视为一个其中包含协同程序的函数。
    
    
    local newThread = coroutine.wrap(function()
        print("Hola")
    end)
    
    newThread()
    

###### 输出结果：
    
    
    Hola
    

当需要添加参数时，可以参照向函数添加参数的方法。
    
    
    local newThread = coroutine.wrap(function(a, b, c)
        print(a * b + c)
    end)
    
    newThread(8,2,1)
    

###### 输出结果：
    
    
    17
    

## 协同程序的用途

学习上述协同程序函数后，接下来让我们浅谈其具体用途。协同程序最为突出的用途之一就是让循环与函数同时运行。
    
    
    local h = Instance.new("Hint", workspace);
    local m = Instance.new("Message", workspace);
    
    local changeHint = coroutine.wrap(function()
        for i = 60, 0, -1 do
           wait(0.5)
           h.Text = i
        end
    end)
    local changeMessage = coroutine.wrap(function()
        for i = 60, 0, -1 do
            wait(1)
            m.Text = i
        end
    end)
    
    changeHint()
    changeMessage()
    code
    

如你所见，消息和提示文本都会对其文本进行更改，但其更改速度不同。

同时，`coroutine.resume()` 可以像 `pcall` 一样返回错误信息：`coroutine.resume()` 会返回一个表明其是否成功的布尔值，当未成功时将会返回一个错误消息字符串。
    
    
    local success, errorMessage = coroutine.resume(coroutine.create(function()
        ppprint("HI")
    end))
    
    if not success then -- 检查是否发生错误
        print("There was an error:", errorMessage)
    end
    

###### 输出结果：
    
    
    There was an error: Script:2: attempt to call global ppprint (a nil value)
    

## 协同程序的扩展

### coroutine.yield()

`coroutine.yield()` 会将你的协同程序置于挂起模式。在该模式下，协同程序将停止并等待，直到其再次被调用为止。`coroutine.yield()` 不能包含元方法，C 函数或迭代器（对上述项尚未了解的开发者一般无需担心对其进行误用）。放入 `coroutine.yield()` 中的任何多余内容都将直接进入 `coroutine.resume()`。
    
    
    new_thread=coroutine.wrap(function(param)
      print(param)
      local resumedWith = coroutine.yield()
      print("Resumed with: " .. resumedWith)
    end) 
    new_thread("Hola mis amigos!")
    new_thread("This was retrieved with yield()")
    

###### 输出结果：
    
    
    Hola mis amigos!
    Resumed with: This was retrieved with yield()
    

### coroutine.status()

`coroutine.status()` 将会以字符串形式返回协同程序目前处于的状态：Dead（中止）、Suspended（挂起）、Running（运行中）或 Normal（正常）。下面让我们来看看这些状态的含义：

  * Running（正在运行）表示协同程序当前处于工作状态，并正在使用其代码。
  * Dead（中止）表示协同程序已停止运行，目前处于中止状态。
  * Suspended（挂起）表示 `coroutine.yield()` 已运行，协同程序正在等待再次启动。

开发者可以按照下列示例对 `coroutine.status()` 进行使用：
    
    
    function core()
        print("hola")
    end
    
    new_thread=coroutine.create(core)
    
    print(coroutine.status(new_thread))
    
    coroutine.resume(new_thread)
    
    print(coroutine.status(new_thread))
    

###### 输出结果：
    
    
    suspended
    hola
    dead
    

### coroutine.running()

`coroutine.running()` 将会返回正在运行的当前线程。请看下列示例：
    
    
    new_thread=coroutine.create(function()
       print("hola")
       print(coroutine.running())
    end)
    
    print(coroutine.running())
    coroutine.resume(new_thread)
    

###### 输出结果：
    
    
    thread: XXXXXXXX
    hola
    thread: YYYYYYYY
    

请注意：`XXXXXXXX` 和 `YYYYYYYY` 不仅会进行变换，而且会与彼此相异。这是因为在对 `coroutine.running()` 的调用间当前正在运行的协同程序产生了改变。

## 与线程计划程序的交互

Roblox 的`Articles/Thread scheduler|线程计划程序`由 [spawn()](Built-in-Functions-and-Variables/Roblox#spawn)、[wait()](Built-in-Functions-and-Variables/Roblox#wait) 和 [delay()](Built-in-Functions-and-Variables/Roblox#delay) 三个函数进行展现。而这三个函数都是基于协同程序进行运转的。

  * 当在线程计划程序（或线程顶层）的函数中使用 `coroutine.yield(...)` 时，其行为行为类似于没有参数的 `wait()`。
  * 用于构建协同程序的函数中的 `wait()` 将会在线程计划程序中把该协同程序放入运行队列。但协同程序可被立刻恢复，导致意外结果
    
    
    local coro = coroutine.wrap(function(arg)
        print("C start", arg)
        print("C yield", coroutine.yield("Y1"))
        print("C wait", wait(2))
        print("C yield", coroutine.yield("Y2"))
        print("C end")
    end)
    
    print("M start")
    -- R1 会处于 arg 中
    print("M resume", coro("R1"))
    -- 从 coroutine.yield 返回 R2
    print("M resume", coro("R2"))
    -- 从 wait 返回 R3！
    print("M resume", coro("R3"))
    print("M end")
    

###### 输出：
    
    
    M start
    C start R1
    M resume Y1
    C yield R2
    M resume
    C wait R3
    M resume Y2
    M end
    C yield 2.0028280779259 3.0923760618118
    C end
    

## 另请参阅

  * [在 Lua 中编程：协同程序](http://www.lua.org/pil/9.html)
  * [Lua 5.1 参考手册：协同程序](http://www.lua.org/manual/5.1/manual.html#2.11)
  * [Lua 5.1 参考手册：协同程序操作](http://www.lua.org/manual/5.1/manual.html#5.2)
  * [Lua 用户有关协同程序的 Wiki 页面](http://lua-users.org/wiki/CoroutinesTutorial)



***__Roblox官方链接__:[协同程序初学者指南](https://developer.roblox.com/zh-cn/articles/Beginners-Guide-to-Coroutines)