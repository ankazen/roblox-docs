# Scope（作用域） 
Time:<em>5  分钟</em>

进行脚本编写时，开发者可以通过 **Scope**（作用域）对变量或函数的“可见”和可访问区域进行定义。`articles/Loops|循环`、`articles/Function|函数`及`articles/Conditional Statements in Lua|条件语句`等元素都会创建新的 **Scope Block**（作用域区块）。每个区块都能够访问处于其父项区块中的剧本变量或函数，但当这些数据位于其子项区块时将无法对其进行获取。

![](https://developer.roblox.com/assets/bltd46ee264544ef2f3/Scope-Diagram.png)



![](https://developer.roblox.com/assets/blt0ae9a4266bb09810/Green-Bullet.png)



B 区块**可以**访问 A 区块中的局部变量。

![](https://developer.roblox.com/assets/blt0ae9a4266bb09810/Green-Bullet.png)



C 区块**可以**访问 A 区块与 B 区块中的局部函数与变量。

![](https://developer.roblox.com/assets/blt4250e428bdfc7e26/Red-Bullet.png)



A 区块**无法**访问 B 区块与 C 区块中的局部函数与变量。

![](https://developer.roblox.com/assets/blt4250e428bdfc7e26/Red-Bullet.png)



B 区块**无法**访问 C 区块中的局部变量。

## Local Scope（局部作用域）

在变量与函数前添加 `local` 前缀后，可以将其作用域限制为**局部作用域**。下列示例中的 `testFunc()` 函数和 `testVar` 变量的作用域均已被设为局部：

Local Scope（局部作用域） ```    
    
    local function testFunc()  -- 作用域为局部
    	local testVar = 64  -- 作用域为局部
    	print(testVar)
    end
    
    testFunc()
    
    print(testVar)
    
    
    64
    nil

```
此示例中 `testVar` 的作用域限制为 `testFunc()` 函数内（其访问范围受到了同样限制），因此在第 3 行对其进行输出时将会按照预期产生 `64` 。但在第 8 行尝试输出该变量时则会产生 `nil`：这是因为在离开特定作用域后，在该作用域级别下创建的变量会被弃用，也就是被“遗忘”了。

## Global Scope（全局作用域）

对全局变量和函数进行声明后，就可以在同一脚本声明后的任意代码块中对其进行使用。变量和函数的作用域默认为全局，除非开发者特意用 `local` 关键字对其进行标记。

下列示例中的 `testVar` 在局部函数 `testFunc()` 函数中进行了全局声明。调用该函数后，`testVar` 被设置为 `64` 。由于该变量为全局作用域并可以在函数外进行访问，因此对其在第 7 行进行输出时同样按预期输出了 `64`。

Global Scope（全局作用域） ```    
    
    local function testFunc()  -- 作用域为局部
    	testVar = 64  -- 作用域为全局
    end
    
    testFunc()
    
    print(testVar)
    
    
    64

```
##### 全局注意事项

Although it may seem convenient to use global scope throughout a script, note the following:

  * Because global variables and functions must be accessed by a hash lookup, they can be expensive to use in terms of performance. In fact, a global variable accessed in a time-critical loop can perform 10% slower (or worse) than a local variable in the same loop.
  * As noted earlier, global variables and functions are only accessible within the associated script, not between multiple scripts. Thus, a global variable/function doesn't provide any benefit over an in-scope local equivalent or a forward declaration.

  


## 作用域的实用实践

### Forward Declaration（前向声明）

在需要时，开发者可以对局部变量进行定义而不为其进行赋值。进行该操作后，可以在其作用域范围**及**子项作用域级别中对该变量进行读取。该操作通常被称为**前向声明**或 **Upvalue**（外部局部变量）。

下列示例的第 8 行对局部变量 `fruitName` 进行了前向声明。在其后的 `for` 循环中（该循环的子项作用域区块）对 `fruitName` 分配了一个值，且该值在循环后被返回。整个 `getFruitByColor()` 函数中的 `fruitName` 一直都是同一个局部变量，此示例中的前向声明避免了当对 `fruitName` 进行全局声明时可能会出现的冲突或覆盖情况。

Forward Declaration（前向声明） ```    
    
    local fruitTable = {
    	Lemon = "Yellow",
    	Apple = "Red",
    	Orange = "Orange"
    }
    
    local function getFruitByColor(color)
    	local fruitName
    	for key, value in pairs(fruitTable) do
    		if value == color then
    			fruitName = key
    		end
    	end
    	return fruitName
    end
    
    local fruit = getFruitByColor("Yellow")
    print(fruit)
    
    
    Lemon

```
### 多脚本数据模块

当需要创建可供多个脚本访问的“全局数据表”时，开发者可以首先在 `ReplicatedStorage` 等其他脚本可以访问的位置创建一个 `ModuleScript` ；然后在 `local module = {}` 和 `return module` 之间创建适配数据的组织表以及子表：

数据模块 ```    
    
    local module = {}
    
    module.VehicleData = {
    	-- 火箭滑车
    	RocketSled = {
    		displayName = "Rocket Sled",
    		topSpeed = 120
    	},
    	-- 蜘蛛坦克
    	SpiderTank = {
    		displayName = "Spider Tank",
    		topSpeed = 40
    	},
    }
    
    return module


```
接下来在每个需要访问该数据的其他脚本中对模块进行 `require()`，如下：

```    
    
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    -- 对模块进行 Require
    local DataModule = require(ReplicatedStorage:WaitForChild("DataModule"))


```
完成之后，即可通过简单操作读取表中的值了：

```    
    
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    -- 对模块进行 Require
    local DataModule = require(ReplicatedStorage:WaitForChild("DataModule"))
    
    local vehicleData = DataModule.VehicleData.RocketSled
    
    local displayName = vehicleData.displayName
    local topSpeed = vehicleData.topSpeed


```


***__Roblox官方链接__:[Scope（作用域）](https://developer.roblox.com/zh-cn/articles/Scope)