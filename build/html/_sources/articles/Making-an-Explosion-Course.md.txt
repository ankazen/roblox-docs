# 制作爆炸赛道 
Time:<em>5  分钟</em>

![](https://developer.roblox.com/assets/blt0a85022115c39188/Explosion-Course-Banner.jpg)

在本教程中，我们将利用 for 循环和随机数来制作一项爆炸挑战。

## 构建路线

第一件事就是就是构建玩家将要跑过的路线。请务必加入重生点。

如上图所示，这一路线最重要的特点就是，可以在你希望发生爆炸的位置填充部件。每个部件都应命名为 _ExplosionPart_，并直接放置在 `Workspace` 当中。

## 编写脚本

现在，让我们添加一个用来让这些部件爆炸的脚本。

首先，在 `ServerScriptService` 中插入一个脚本。通过代码添加爆炸的函数与我们用来创建新部件的函数是同一种：:
    
    
    local explosion = Instance.new("Explosion")
    explosion.Parent = game.Workspace
    

爆炸的关键在于，我们需要告诉它们起爆的位置。我们可以用爆炸的 **Position** （位置）属性来实现这一目的 —但是，我们究竟想要爆炸出现在哪里呢？我们可以按照下面这样操作：
    
    
    local explosion = Instance.new("Explosion")
    explosion.Position = game.Workspace.ExplosionPart.Position
    explosion.Parent = game.Workspace
    

这会让爆炸出现在我们之前插入的其中一个部件的中心。

这段代码只会创建**一**次爆炸，而我们想要所有命名为 _ExplosionPart_ 的部件都发生爆炸。为了达到这种效果，我们将会使用通用 `for` 循环。通用 `for` 循环有多种使用方式，其中一种就是在一组对象当中循环，并对每个对象都执行同样的操作。在本教程中，我们将使用这一技巧，在 `Workspace` 的所有子项当中循环，使效果影响每个 _ExplosionPart_。

首先，我们需要获取 `Workspace` 中所有子项的列表。我们可以用 `Instance/GetChildren|GetChildren()` 成员函数来实现这一目的，并将结果存储在一个变量当中：
    
    
    local children = game.Workspace:GetChildren()
    

现在，我们就可以使用 for 循环来操作该列表中的所有子项了。
    
    
    local children = game.Workspace:GetChildren()
    for _, child in ipairs(children) do
    	local explosion = Instance.new("Explosion")
    	explosion.Position = child.Position
    	explosion.Parent = game.Workspace
    end
    

遗憾的是，如果我们运行这段代码，我们的游戏将会报错：

![Scripting6_Error.png](https://developer.roblox.com/assets/bltc1558f7f9ca1ee16/Scripting6_Error.png)



这是由于 `Instance/GetChildren|GetChildren()` 返回了工作空间当中的 **所有** 子项，包括 **Camera** （镜头）、**Terrain** （地形）和我们游戏当中可能存在的任何其他部件。

因此，我们需要检查自己看到的子项是否为 _ExplosionPart_。我们可以通过一个用来检查子项名称的条件语句来达到这种效果：
    
    
    local children = game.Workspace:GetChildren()
    for _, child in ipairs(children) do
    	if child.Name == "ExplosionPart" then
    		local explosion = Instance.new("Explosion")
    		explosion.Position = child.Position
    		explosion.Parent = game.Workspace
    	end
    end
    

现在，我们的代码将会正常运行，并会在所有正确的位置制造爆炸了！不过，就爆炸一次可不怎么过瘾。让我们用一个 `while true` 循环和一个 `wait()` 来让代码循环运行，这样就可以得到反复爆炸的效果：
    
    
    local children = game.Workspace:GetChildren()
    while true do
    	for _, child in ipairs(children) do
    		if child.Name == "ExplosionPart" then
    			local explosion = Instance.new("Explosion")
    			explosion.Position = child.Position
    			explosion.Parent = game.Workspace
    		end
    	end
    	wait(1)
    end
    

### 随机数

现在，我们所有的 _ExplosionPart_ 部件都会在每个循环当中制造一次爆炸。让我们来添加一个 **随机** 要素，使得每次循环时只有某些部件会起爆。

我们首先要做的，就是将我们的爆炸代码放到一个 **function** （函数）当中。后面还要向其中添加更多内容，所以我们不想让循环当中的代码变得太难懂。
    
    
    local function explodePart(part)
    	local explosion = Instance.new("Explosion")
    	explosion.Position = part.Position
    	explosion.Parent = game.Workspace
    end
    
    local children = game.Workspace:GetChildren()
    while true do
    	for _, child in ipairs(children) do
    		if child.Name == "ExplosionPart" then
    		explodePart(child)
    	end
    	end
    	wait(1)
    end
    

该代码的运行效果与之前并无二致，唯一的区别就是使用函数后，使其变得更有条理。现在，让我们制作一个随机数，用来决定我们是否想制造爆炸。随机数的生成是通过一种特殊的函数来完成的：
    
    
    local number = math.random(1,3)
    

`math.random()` 将会输出一个随机数，该数介于你在括号里提供的两个数字之间。在本案例中，我们会得到一个介于 `1` 和 `3` 之间的随机数。我们可以用一个条件语句来检查这个数字：
    
    
    local function explodePart(part)
    	local number = math.random(1,3)
    	if number == 1 then
    		local explosion = Instance.new("Explosion")
    		explosion.Position = part.Position
    		explosion.Parent = game.Workspace
    	end
    end
    
    local children = game.Workspace:GetChildren()
    while true do
    	for _, child in ipairs(children) do
    		if child.Name == "ExplosionPart" then
    			explodePart(child)
    		end
    	end
    	wait(1)
    end
    

### 警示玩家

游戏目前并没有给玩家提供某一指定部件即将爆炸的指示。我们现在来添加某种能让部件在爆炸前变红的代码。

在我们的 `explodePart()` 函数当中，我们会添加一个新的 `if` 语句，还有一个称为 `else` 的新语句，它的作用是在第一个语句没有得到满足时运行逻辑。
    
    
    local function explodePart(part)
    	if part.BrickColor == BrickColor.Red() then
    		local explosion = Instance.new("Explosion")
    		explosion.Position = part.Position
    		explosion.Parent = game.Workspace
    		part.BrickColor = BrickColor.White()
    	else
    		local number = math.random(1,3)
    		if number == 1 then
    			part.BrickColor = BrickColor.Red()
    		end
    	end	
    end
    

让我们从头到尾看一下这个函数，了解一下现在正在进行哪些动作。函数会先检查部件是否已经变红。如果已经变红，则会引发爆炸，并让部件变回白色。如果部件_不是_红色（默认不是红色），函数将会生成一个随机数。如果随机数等于 1，则我们会将部件变为红色。这将导致部件在下次被该函数调用时发生爆炸。

整个脚本应为如下所示：
    
    
    local function explodePart(part)
    	if part.BrickColor == BrickColor.Red() then
    		local explosion = Instance.new("Explosion")
    		explosion.Position = part.Position
    		explosion.Parent = game.Workspace
    		part.BrickColor = BrickColor.White()
    	else
    		local number = math.random(1,3)
    		if number == 1 then
    			part.BrickColor = BrickColor.Red()
    		end
    	end	
    end
    
    local children = game.Workspace:GetChildren()
    while true do
    	for _, child in ipairs(children) do
    		if child.Name == "ExplosionPart" then
    			explodePart(child)
    		end
    	end
    	wait(1)
    end
    

现在，各部件将会随机变红然后再爆炸，让你的玩家能有机会逃出升天！



***__Roblox官方链接__:[制作爆炸赛道](https://developer.roblox.com/zh-cn/articles/Making-an-Explosion-Course)