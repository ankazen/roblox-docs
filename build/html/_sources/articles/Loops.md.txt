# 循环（Loop） 
Time:<em>5  分钟</em>

**Loop**（循环）可用来多次执行代码。Lua 中存在多种循环，虽然都会重复运行一段代码，但其执行方式有着一定差异。

## 循环类型

### for — do

`for`—`do` 循环可以让开发者将命令或命令组运行指定次数。其基本语法包括一个**控制变量（control variable）**、一个**起始（start）**值、一个**结束（end）**值和一个非必须的**增量（increment）**值。

`for`

`count`  
![](https://developer.roblox.com/assets/blt520577ecaffd5e7d/u-arrow-blue.png)

控制  
变量

`=`

`1`  
![](https://developer.roblox.com/assets/blt520577ecaffd5e7d/u-arrow-blue.png)

起始

`,`

`10`  
![](https://developer.roblox.com/assets/blt520577ecaffd5e7d/u-arrow-blue.png)

结束

`,`

`1`  
![](https://developer.roblox.com/assets/blt520577ecaffd5e7d/u-arrow-blue.png)

增量

`do`

此循环从**起始**值开始运行，`do` 和 `end` 之间的代码每运行一次，就对此值进行增加或减少一次，直到达到**结束**值为止。例如，以下循环以 **1** 开始并增加到 **5** 为止，在每次迭代时都输出 `count`（控制变量）值：

```    
    
    for count = 1, 5 do
    	print(count)
    end
    
    
    1
    2
    3
    4
    5

```
当语句中包含**increment**（增量）时，增量为正值则向上计数，增量为负值则向下计数：

```    
    
    for count = 1, 10, 2 do
    	print(count)
    end
    
    
    1
    3
    5
    7
    9

```
```    
    
    for count = 3, 0, -0.5 do
    	print(count)
    end
    
    
    3
    2.5
    2
    1.5
    1
    0.5
    0

```
### while — do

`while`—`do` 循环将评估特定条件为 true 或 false。当条件为 false 时该循环将会结束，并继续执行其后的代码。当条件为 true 时循环将会执行 `do` 和 `end` 之间的代码，然后对条件的 true 或 false 进行再次评估。

```    
    
    local timeRemaining = 10
    
    while timeRemaining > 0 do
    	print("剩余秒数： " .. timeRemaining)
    	wait(1)
    	timeRemaining = timeRemaining - 1	
    end
    
    print("倒数计时已归零！")
    
    
    Seconds remaining: 10
    Seconds remaining: 9
    Seconds remaining: 8
    Seconds remaining: 7
    Seconds remaining: 6
    Seconds remaining: 5
    Seconds remaining: 4
    Seconds remaining: 3
    Seconds remaining: 2
    Seconds remaining: 1
    Timer reached zero!

```
当只使用 `true` 作为条件时，`while`—`do` 循环可以被用作无限游戏循环：

```    
    
    while true do
    	print("循环中...")
    	wait(0.5)
    end


```
当使用无限循环时，请务必在其中添加 `wait()` 等延时语句。如果省略此类语句，可能会导致游戏冻结。 

### repeat — until

`repeat`—`until` 循环将重复执行，直到满足特定条件。请注意：由于对条件是否满足的测试处于 `until` **后**，位于 `repeat` 和 `until` 之间的代码将至少执行一次。

```    
    
    local currentGoblinCount = 18
    
    -- 在游戏中最多生成 25 个哥布林
    repeat
    	spawnGoblin()
    	currentGoblinCount = currentGoblinCount + 1
    	print("当前哥布林数目： " .. currentGoblinCount)
    until currentGoblinCount == 25
    
    print("哥布林生成完毕！")
    
    
    Current goblin count: 19
    Current goblin count: 20
    Current goblin count: 21
    Current goblin count: 22
    Current goblin count: 23
    Current goblin count: 24
    Current goblin count: 25
    Goblins repopulated!

```
## 结束循环

当正在运行的循环不会以普通方式结束（例如无限 `while`—`do` 循环）时，则可以使用 `break` 命令强制其结束，以便脚本可继续运行其后的代码：

```    
    
    local secondsElapsed = 0
    local timeout = 5
    
    while true do
    	print("循环中...")
    	wait(1)
    	secondsElapsed = secondsElapsed + 1
    
    	if secondsElapsed == timeout then
    		break
    	end
    end
    
    print("循环结束；继续其他项目！")
    
    
    Looping...
    Looping...
    Looping...
    Looping...
    Looping...
    Loop ended; moving on!

```


***__Roblox官方链接__:[循环（Loop）](https://developer.roblox.com/zh-cn/articles/Loops)