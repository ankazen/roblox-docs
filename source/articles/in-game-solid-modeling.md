# 游戏内实体建模 
Time:<em>5  分钟</em>

无论是在 Studio 中还是游戏进行时，开发者都可以通过使用 **Union** （联合）和 **Negate** （忽略）工具来创建充满细节的`Articles/3D Modeling with Parts|实体模型`。这可以用来创建一些十分独特的游戏概念。

## 实体建模 API

### UnionAsync()

`BasePart/UnionAsync|UnionAsync()` 函数必须在 `BasePart` 上调用。此函数需要一个数组（由一个或多个部件（`otherParts`）组成）与调用的 `BasePart` 组合。

```    
    
    local part = workspace.Part1
    local otherParts = {workspace.Part2, workspace.Part3, workspace.Part4}
    
    -- 进行 union（联合）操作
    local newUnion = part:UnionAsync(otherParts)


```
![](https://developer.roblox.com/assets/blta80b0e04d8611992/In-Game-CSG-Union.png)



### SubtractAsync()

`BasePart/SubtractAsync|SubtractAsync()` 函数也需要将一个数组（由一个或多个部件组成）从调用的 `BasePart` 中减除。

```    
    
    local part = workspace.Part1
    local otherParts = {workspace.Part2, workspace.Part3, workspace.Part4}
    
    -- 进行 union（联合）操作
    local newUnion = part:SubtractAsync(otherParts)


```
![](https://developer.roblox.com/assets/blta2d35b0a0ba54157/In-Game-CSG-Subtract.png)



游戏中实体建模是**异步**操作，这意味着它可能会占用一定资源。为了获得最佳的游戏性能，开发者不应同时执行大量此类 API 调用。 

调用部件的以下属性将应用于结果部件： 

  * **Color**
  * **Material**
  * **Reflectance**
  * **Transparency**

  * **Anchored**
  * **CanCollide**
  * **Density**
  * **Friction**

  * **Elasticity**
  * **FrictionWeight**
  * **ElasticityWeight**

## 基本演示

让我们用一个简单的演示脚本来测试游戏中的实体模型吧！将其复制并粘贴到 **ServerScriptService** 中的 `Script` 中或任何方便的位置即可。

实体建模 API 仅在**服务器端**起作用（在 `LocalScript` 中不起作用）。 

```    
    
    -- 创建基础的窗户部件
    local window = Instance.new("Part")
    window.Size = Vector3.new(10, 16, 0.5)
    window.Material = "Glass"
    window.BrickColor = BrickColor.new("Persimmon")
    window.Reflectance = 0.2
    window.Transparency = 0.5
    window.Position = Vector3.new(0, 8, 0)
    window.Anchored = true
    window.Parent = game.Workspace
    
    -- 创建一个将从窗户中减去的部件
    local subBlock = Instance.new("Part")
    subBlock.Size = Vector3.new(4, 4, 4)
    subBlock.Material = "SmoothPlastic"
    subBlock.CanCollide = false
    subBlock.Position = Vector3.new(0, 8, 0)
    subBlock.Anchored = true
    subBlock.Parent = game.Workspace
    
    wait(2)
    
    -- 从窗户中删减去较小的部件
    local success, newUnion = pcall(function()
    	return window:SubtractAsync({subBlock})
    end)
    
    if success and newUnion then
    	newUnion.Position = window.Position
    	newUnion.Anchored = true
    	newUnion.Parent = game.Workspace
    	-- 移除原始部件
    	window:Destroy()
    	subBlock:Destroy()
    end


```
本脚本中，操作的基本顺序是：

  1. 在场景中央创建一扇红色玻璃窗（第 2-10 行） 。
  2. 在窗户部件中央创建一个较小的块（第 13-19 行） 。
  3. 在 2 秒后，对窗户调用 `BasePart/SubtractAsync|SubtractAsync()`，将较小的块作为要删减的部件。

数个原因可能导致游戏内实体建模操作失败（参见 API 文档）。因此，请始终使用 `pcall()` 以捕获意外错误。 

  4. 如果成功，将返回名为 **Union** （联合）的结果部件。此实例**不会**设为工作区父项，所以您必须手动将其设为父项使其返回游戏世界。

原始部件仍留在游戏中，包括操作调用的实例（`window`）和从中添加或删减的部件（`subBlock`）。因此，在成功完成建模操作后，这些部件将被显式销毁（第 33-34行）。 

## 实体建模游乐场

现在您已经了解了基础游戏实体建模，那就进入到[示例场景来体验一下吧](https://www.roblox.com/games/2309627316/Rotating-Windows)。

![](https://developer.roblox.com/assets/blt5a9c2e3521e643da/In-Game-CSG-Playground1.jpg)

#### [旋转的窗户](https://www.roblox.com/games/2309627316/Rotating-Windows)

从旋转的窗户中炸出碎片，或将新材料熔合在上面。其中包括一个帮助程序模块脚本，该脚本可以重建带有约束和附件的装置！



***__Roblox官方链接__:[游戏内实体建模](https://developer.roblox.com/zh-cn/articles/in-game-solid-modeling)