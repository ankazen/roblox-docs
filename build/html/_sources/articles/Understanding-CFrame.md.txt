# 了解 CFrame 
Time:<em>0, 0, 0</em>

`datatype/CFrame` 为 **Coordinate Frame（坐标框架）**的缩写，是一种用于旋转和定位 3D 对象的数据类型。CFrame 同时为对象属性和独立单位，其中包含全局 **X**、**Y** 和 **Z** 坐标以及各轴上的旋转数据。除此之外， CFrames 还含括在 3D 空间中处理对象所需的有用函数。

以下为在游戏中应用 CFrame 的几个示例：

  * 为子弹或弓箭等投射武器寻找远处的目标位置，例如被玩家激光爆能枪所瞄准敌人的位置。
  * 在玩家与特定 NPC （非玩家角色）互动时移动镜头，使其聚焦于该 NPC。
  * 当玩家获取麻痹、加速、中毒等状态时在其头顶放置相应的状态指示器。

## CFrame 基础知识

### CFrame 定位

开发者可以通过 `datatype/CFrame|CFrame.new()` 在游戏世界中的默认位置 **0**, **0**, **0** 创建一个空白 CFrame。但若希望将 CFrame 定位到指定位置点，则需为 `CFrame.new()` 函数提供 **X**、**Y**、**Z** 参数。在以下示例中，我们将使用存储在 `newCFrame` 中的值对 `redBlock` 对象的 CFrame 属性进行覆盖，使其重定位至 **-2**, **2**, **4** 位置。

```    
    
    local redBlock = game.Workspace.RedBlock
    
    -- 创建新 CFrame
    local newCFrame = CFrame.new(-2, 2, 4)
    
    -- 用新的 CFrame 覆盖红色方块的当前 CFrame
    redBlock.CFrame = newCFrame


```
![](https://developer.roblox.com/assets/blt0a2965ab605115c7/CFrame-Strict-Position-A.png)

 ![](https://developer.roblox.com/assets/blt442e40504909e1fa/CFrame-Strict-Position-B.png)



除此之外，开发者也可以通过为 `CFrame.new()` 提供新的 `datatype/Vector3` 位置以获取相同结果：

```    
    
    local redBlock = game.Workspace.RedBlock
    
    -- 创建新 CFrame
    local newVector3 = Vector3.new(-2, 2, 4)
    local newCFrame = CFrame.new(newVector3)
    
    -- 用新的 CFrame 覆盖红色方块的当前 CFrame
    redBlock.CFrame = newCFrame


```
### CFrame 旋转

当需要创建带有旋转角度的 CFrame 时，请通过 `datatype/CFrame|CFrame.Angles()` 构造函数为需要旋转的轴提供旋转角度，以弧度（Radian）为单位：

```    
    
    local redBlock = game.Workspace.RedBlock 
    
    -- 创建旋转后的新 CFrame
    local newCFrame = CFrame.Angles(0, math.rad(45), 0)
    
    -- 用新的 CFrame 覆盖红色方块的当前 CFrame
    redBlock.CFrame = newCFrame


```
![](https://developer.roblox.com/assets/blteb98af1431d42902/CFrame-Strict-Rotation-A.png)

 ![](https://developer.roblox.com/assets/bltd10d764204c799d5/CFrame-Strict-Rotation-B.png)



如上所述， `CFrame.Angles()` 的参数应以**弧度**为单位，而非角度。开发者可通过上个示例中的 `math.rad()` 转换器将角度转换为弧度。 

### 面向指定位置点

`CFrame.new()` 最强大的用途之一为使 CFrame 的前方指向游戏世界中的特定点。在以下示例中，我们会将 `redBlock` 部件定位至 **0**, **3**, **0**，并使其前方（白色圆圈所标记的一面）面向 `blueCube` 部件：

```    
    
    local redBlock = game.Workspace.RedBlock
    local blueCube = game.Workspace.BlueCube
    
    -- 为初始位置和目标位置各创建一个 Vector3
    local startPosition = Vector3.new(0, 3, 0)
    local targetPosition = blueCube.Position
    
    -- 将红色方块放至 'startPosition' 并使其前方面向 'targetPosition'
    redBlock.CFrame = CFrame.new(startPosition, targetPosition)


```
![](https://developer.roblox.com/assets/blt72d8472377a49d6a/CFrame-Front-Face-Pointing-A.png)

 ![](https://developer.roblox.com/assets/blt73df55f9f1d48c13/CFrame-Front-Face-Pointing-B.png)



### 偏移 CFrame

在特定情况下，开发者或者需要将对象从当前位置偏移指定格数。这时只需向位于对象位置的新建 CFrame 增加或削减 Vector3 值即可。

```    
    
    local redBlock = game.Workspace.RedBlock
    
    redBlock.CFrame = CFrame.new(redBlock.Position) + Vector3.new(0, 1.25, 0)


```
![](https://developer.roblox.com/assets/blt5e1879b28774407e/CFrame-Self-Offset-A.png)

 ![](https://developer.roblox.com/assets/blt53a1de299d94e8df/CFrame-Self-Offset-B.png)



如上方代码所示，当需要获取正确格式的对象 Vector3 位置并将其作为 `CFrame.new()` 参数时，可使用对象的 **Position** 属性（在此示例中为 `redBlock.Position`），非常便捷。 

当使一个对象从另一个对象所在的位置偏移时，也可以使用同样的技巧。但在此情况下，我们需要将 Vector3 值添加至在蓝色方块（而不是红色方块）位置新建的 CFrame，如下所示：

```    
    
    local redBlock = game.Workspace.RedBlock
    local blueCube = game.Workspace.BlueCube
    
    redBlock.CFrame = CFrame.new(blueCube.Position) + Vector3.new(0, 2, 0)


```
![](https://developer.roblox.com/assets/bltebba6931e2a1fcca/CFrame-Other-Part-Offset-A.png)

 ![](https://developer.roblox.com/assets/bltecec911e4056ffa2/CFrame-Other-Part-Offset-B.png)



## 动态 CFrame 朝向

`CFrame.new()` 和 `CFrame.Angles()` 构造函数虽然功能强大，但其应用情况的要求也较为严格：只能将对象定位或旋转至游戏世界中的特定方向。虽然这些功能在许多状况下十分有用，但当无法依赖固定的世界位置或旋转角度时，又该如何进行处理呢？举例来说：

  * 在世界中任意位置及任意朝向的玩家面前生成漂浮的宝物。
  * 在玩家的右肩上方生成一个魔法精灵。

上述情况更适合使用 CFrame **函数**，而非要求严格的构造函数。

### 相对位置

`datatype/CFrame|CFrame:ToWorldSpace()` 函数可以将对象的局部朝向 CFrame 转换为新的**全局**朝向。因此，这个函数非常适合用来使部件相对自身或其他对象进行偏移，无需在意对象当前的位置或旋转。

在以下代码和图像示例中，请注意红色方块在向上偏移 2 格时所使用的是蓝色方块的 **Y** 轴（穿过蓝色方块的绿色箭头），而**并未使用**指向正上方的全局 **Y** 轴。

```    
    
    local redBlock = game.Workspace.RedBlock
    local blueCube = game.Workspace.BlueCube
    
    local offsetCFrame = CFrame.new(0, 2, 0)
    redBlock.CFrame = blueCube.CFrame:ToWorldSpace(offsetCFrame)


```
![](https://developer.roblox.com/assets/blt9dd6d0186dbb8d4f/CFrame-Other-Part-Relative-Position-A.png)

 ![](https://developer.roblox.com/assets/blt009c402c0ef6ab75/CFrame-Other-Part-Relative-Position-B.png)



### 相对旋转

`CFrame:ToWorldSpace()` 也可以用来使对象相对自身进行旋转。举例来说：使对象相对当前 **Y** 轴逆时针旋转 70 度并相对当前 **Z** 轴顺时针旋转 20 度。

```    
    
    local redBlock = game.Workspace.RedBlock
    
    local rotatedCFrame = CFrame.Angles(0, math.rad(70), math.rad(20))
    redBlock.CFrame = redBlock.CFrame:ToWorldSpace(rotatedCFrame)


```
![](https://developer.roblox.com/assets/blt52904f5c2fdf1177/CFrame-Self-Rotate-A.png)

 ![](https://developer.roblox.com/assets/blt1374580558ae6595/CFrame-Self-Rotate-B.png)



### 使指定表面朝向特定点

如前例所示，开发者可以通过为 `CFrame.new()` 提供 Vector3 点作为第二参数来使对象“面向”另一个对象。但此操作的局限性在于其只与移动对象的**前方**表面关联。

当希望将对象的任意表面朝向 Vector3 点时，可以使用相对旋转功能。以下示例由两个连续 CFrame 操作构成：

  1. 将对象的**前**面（白色圆圈所标记的一面）指向目标。
  2. 旋转 CFrame，使其**顶**面（黑色圆圈所标记的一面）指向目标。

```    
    
    local redBlock = game.Workspace.RedBlock
    local blueCube = game.Workspace.BlueCube
    
    -- 为目标位置创建一个 Vector3
    local targetPosition = blueCube.Position
    
    -- 使红色方块的前方面向 'targetPosition'
    redBlock.CFrame = CFrame.new(redBlock.Position, targetPosition)
    
    -- 以红色方块自身为轴心旋转其 CFrame，使其顶面（而非前面）面向目标
    local rotatedCFrame = CFrame.Angles(math.rad(-90), 0, 0)
    redBlock.CFrame = redBlock.CFrame:ToWorldSpace(rotatedCFrame)


```
![](https://developer.roblox.com/assets/bltafd0efe0526112fd/CFrame-Top-Face-Pointing-A.png)

 ![](https://developer.roblox.com/assets/blt5e07a6edca9396a7/CFrame-Top-Face-Pointing-B.png)



### 找到两点之间的特定位置点

开发者可以通过名为 **Linear Interpolation**（也就是线性插值，常被简称为 **Lerp**）的方法将 CFrame 定位至两点之间的特定位置。举例来说，以下代码将会使用值 `0.7` 将 `redBlock` 放置在 `greenCube` 与 `cyanCube` 部件之间，该值将会使其绿色和红色部件之间的距离为总距离的 70%。

```    
    
    local redBlock = game.Workspace.RedBlock
    local greenCube = game.Workspace.GreenCube
    local cyanCube = game.Workspace.CyanCube
    
    redBlock.CFrame = greenCube.CFrame:Lerp(cyanCube.CFrame, 0.7)


```
![](https://developer.roblox.com/assets/bltb789de58c08eb890/CFrame-Lerp-A.png)

 ![](https://developer.roblox.com/assets/bltd29b3ab2aedada4c/CFrame-Lerp-B.png)



* * *

学习以上要领之后，开发者将可以顺利通过 CFrame 构造函数和函数对于游戏世界中的对象进行定向。完全理解本文概念的开发者可以考虑参阅`articles/CFrame Math Operations|CFrame 数学运算`一文，进一步探索更为高级的 CFrame 操作。



***__Roblox官方链接__:[了解 CFrame](https://developer.roblox.com/zh-cn/articles/Understanding-CFrame)