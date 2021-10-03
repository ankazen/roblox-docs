# 代码编写简洁化 
Time:<em>10  分钟</em>

开发者你好！今天我们来讨论一下如何编写更为高效与职业化的代码吧。

代码编写的简洁化十分重要，而且能够让他人更为轻易地阅读与调试你的代码。（但并不是说你所编写的代码就一定会出错喔。）

### 代码缩进

良好的代码编写习惯中最为重要的条目之一就是进行缩进。缩进听起来虽然好像有些困难的样子，但其实就是在每一层深度的代码块前多加一个制表符（Tab 键）。每个 if、while、for、funcion、repeat 等后都需要进行添加。也就是说，出现类似上述关键词时，下一行开始时都要再添加一个制表符（Tab 键）。养成代码缩进的习惯后，可以非常清晰地看到代码块的起始和结束行。而且这样一来就很不容易忘掉 “end” 语句了。

下面我们来看一段十分混乱的代码吧。由于缺失一个 end，这段代码无法运行，而且缺失的地方也很不好找：
    
    
    local powerLevel = -6
    function fancyFunction()
    powerLevel = powerLevel +1
    end
    for i = 1,10 do
    if 1 + 1 == 2 then
    fancyFunction()
    print(powerLevel)
    end
    

如果对这段代码进行缩进，就可以轻松地看到 end 应该放置在什么地方，且代码中有没有语句缺失了：
    
    
    local powerLevel = -6
    function fancyFunction()
    	powerLevel = powerLevel +1
    end
    for i = 1, 10 do
    	if 1 + 1 == 2 then
    		fancyFunction()
    	print(powerLevel) --这里看起来似乎有些不对喔！
    end
    

我们可以轻易看到函数与 for 循环的 end 语句都没有问题，但 if 语句似乎缺失了 end。那么就让我们将其加入，修复代码吧：
    
    
    local powerLevel = -6
    function fancyFunction()
    	powerLevel = powerLevel +1
    end
    for i = 1, 10 do
    	if 1 + 1 == 2 then
    		fancyFunction()
    	end
    	print(powerLevel)
    end
    

由于 Lua 解释器将会忽略空白符，对代码进行缩进时将**不会**影响脚本运行速度。

### 易懂的变量名称

另外一个重要的习惯就是在命名变量时一定要使其清晰易懂。

如果你的变量都使用了 “mj90_z” 这种混乱且毫无意义的名称，那么其他人将很难读懂你的代码。由于这些名称难以记忆，有时连你本人都会难以回忆起一段时间前自己到底想要用这段代码做些什么。

下列代码中的变量名称并没有遵循清晰易懂的规则，让人无法记起其意义：
    
    
    epic1337 = false
    georgewin = 1
    if not epic1337 then
        georgewin = 0
    end
    

虽然这段代码并不长，但让我觉得十分难懂。不知你感觉如何？

这段代码的名称好像是“上直升飞机的脚本！”，但我却完全无法对其进行理解。

如果能够对变量进行重命名，或许就能理解这段代码的用途了：
    
    
    atChopper = false
    peopleAtChopper = 1
    if not atChopper then
    	peopleAtChopper = 0
    end
    

原来如此。如果你的角色不在直升飞机处，那么在直升飞机处的人数将为 0。现在这段代码非常容易理解，我们也因此能对其作用进行了解。

### 加入注释

如果你正在和几个朋友一起制作非常大的游戏，每个人都需要编写与共享脚本时该怎么处理呢？

虽然**可以**希望自己与好友们心有灵犀，在他们添加你的脚本时知道脚本的意图，但更为有效的方法是在代码上添加注释，让他们通过阅读注释了解代码的功能。

下面让我们来看看这段难以理解的代码吧：
    
    
    codeIsConfusing = true
    if codeIsConfusing then
    	print("这代码好难懂喔。")
    end
    

不知你怎么认为，但我觉得这段代码真的很难懂。

但通过对代码添加注释，可以让人更为轻易地对其进行理解。如果只需写一行注释，请使用 – 。在此符号之后的所有文本都将成为注释。

但如果需要写一大篇注释，可以使用 `\--[[` （开始注释）和 `]]` （结束注释）将文本嵌套起来，其中就是需要注释的内容了。

下面让我们来为之前十分难懂的代码添加注释，帮助一起制作游戏的朋友们吧：
    
    
    --[[
    	此代码的作用为检查代码的难懂程度。
    	如果代码难懂，则将 CodeIsConfusing 设为 true，反之则设为 false。
    ]]
    CodeIsConfusing = true --此代码是否难懂的布尔值
    if CodeIsConfusing then --当代码难懂时…
    	print("这代码好难懂喔。") --输出文本。
    end --结束 if 语句。
    

这样一起做游戏的朋友们也能看懂上面的代码了。

–难懂的代码真的很难懂。

### 使用 for 循环

下列这种为逐渐淡出的门所编写的代码，你有没有见过？
    
    
    script.Parent.Transparency = 0.1
    wait(0.1)
    script.Parent.Transparency = 0.2
    wait(0.1)
    script.Parent.Transparency = 0.3
    wait(0.1)
    script.Parent.Transparency = 0.4
    wait(0.1)
    script.Parent.Transparency = 0.5
    wait(0.1)
    script.Parent.Transparency = 0.6
    wait(0.1)
    script.Parent.Transparency = 0.7
    wait(0.1)
    script.Parent.Transparency = 0.8
    wait(0.1)
    script.Parent.Transparency = 0.9
    wait(0.1)
    script.Parent.Transparency = 1
    wait(0.1)
    

如果能在此处使用 for 循环，就可以节省许多时间和内存消耗。

简单来说，我们可以将部件的透明度设为循环中的索引变量。

举例来说：
    
    
    for i = 1, 10 do
    	script.Parent.Transparency = i/10
    	wait(0.1)
    end
    

不过，即使是这么简单的代码也可以继续简化！没错！

通过使用循环的第三个参数，也就是其增量（increment），我们可以让循环每次增加 0.1 而不是 1。这样一来就不需要 /10 这个部分了。

请看以下示例：
    
    
    for transparency = 0, 1, 0.1 do
    	script.Parent.Transparency = transparency
    	wait(0.1)
    end
    

这个小技巧十分好用，在添加动画或创建物体时能够帮你省下不少时间。

–来此之人必心生希望。循环即是未来！

### 布尔值

在编写代码时，当出现 true 或 false 值时，或许会有使用 if value == true/false then 进行操作的习惯。

先不要着急，这里还可以进行优化！Roblox 的长处之一就是可以将 if 语句中的值转化为 true 或 false。

简单来说，如果值存在则会转化为 true，如果值为 nil 则会转化为 false。

这样一来，我们就能写出不使用 == true/false 的精简代码了。具体方法为：

只要删除 == true/false 即可。怎么样，是不是很简单？

下面先来看看这个反面代码示例：
    
    
    cake = Workspace:FindFirstChild("Cake")
    yummy = true
    if cake ~= nil then
    	if yummy == true then
    		print("蛋糕存在，而且很好吃。")
    	end
    end
    

将 == true/false 和 ~= true/false 移除后是这样的：
    
    
    cake = Workspace:FindFirstChild("Cake")
    yummy = true
    if cake then
    	if yummy then
    		print("蛋糕存在，而且很好吃。")
    	end
    end
    

其功能完全相同，而且更为有效简洁。并且使用 Roblox 提供的语句更为容易理解，就像是在说“if（如果） cake then（则）进行此操作”，而不是“if（如果）cake 等同于 true，then（则）进行此操作”。

但如果我们想要让这个事件在蛋糕（cake）并不存在而且不好吃时触发，该怎么处理呢？

这时可以使用 “not” 将布尔值进行反转！太简单了！

举例来说：
    
    
    cake = Workspace:FindFirstChild("Cake")
    yummy = true
    if not cake then
    	if not yummy then
    		print("蛋糕并不存在，而且肯定也不好吃。")
    	end
    end
    

–如果蛋糕真的是个谎言，我们概不负责喔。

### 数学运算

其实你在脚本中编写数学运算式时的语法对于脚本的可读性与可修改性也大有关联。

如果你在学校还没学到运算顺序，简单来说就是这样：

  * 数学运算中括号里的内容永远最先计算
  * 括号之后先对幂进行计算
  * 第三位进行计算的是乘法和除法
  * 最后进行计算的是加法和减法。

但我们应该怎样利用运算顺序让脚本变得更简洁呢？

让我们首先来看看不少人在编写数学运算式时的情形吧：
    
    
    5 * 2 + 6 / 3
    

这行代码看起来就像是数字和符号堆积在一起，虽然也不是看不懂，但如果简化一下会更好。

简化的方式有很多种，下面列举的是我个人喜欢使用的方法。

  * 不要在乘除运算中使用空格。
    
    
    5*2, 6/3
    

  * 在加减运算中需要使用空格。
    
    
    2 + 6, 10 - 4
    

  * 可用时就用上括号。
    
    
    (5*2), (6/3)
    

利用你所喜欢的数学运算写法可以让代码的运行更加一目了然。  
对之前的代码进行简洁化后是这样的：
    
    
    (5*2) + (6/3)
    

不知道你怎么想，我个人认为现在的运算式比之前的要易懂很多。



***__Roblox官方链接__:[代码编写简洁化](https://developer.roblox.com/zh-cn/articles/Writing-Clean-Code)