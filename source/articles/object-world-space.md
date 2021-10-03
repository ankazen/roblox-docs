# 对象空间与世界空间 
Time:<em>10  分钟</em>

在处理游戏几何时，您可能会遇到术语 **object space（对象空间）**和 **world space（世界空间）**。在 Roblox 里，您可以在 Vector3 和 CFrame 函数中找到这些术语。这些术语指的是不同类型的坐标系或定义位置的方式。本文将帮助您理解它们在 Roblox 开发中的作用。

## 世界空间

![一个 Roblox 角色站在足球场上](https://developer.roblox.com/assets/blt700c53125756d5fb/Football-Field.jpg)

把世界空间想象成橄榄球场上的码线。码线不会移动，它们的作用就像坐标：你可以用它们来找到运动员在球场上的位置。

就像橄榄球场中一样，世界空间在每个 Roblox 游戏中都是相同的：位置 (0, 0, 0) 是游戏的中心。“前”方向始终为负 Z 方向，“右”方向始终为正 X 方向。部件的 Position 属性通常是指部件在世界空间中的位置，也称为部件的绝对位置。

在代码中处理位置数据时，先将位置和方向转换为世界空间是非常有用的。把它作为解决你遇到的任何几何问题的基础吧！

## 对象空间

![两个足球运动员面对面。后方蓝色的有一个向右的箭头，标签为“His Left”（他的左方），前方红色的有一个向右的箭头，标签为“Your Right”（你的右方）](https://developer.roblox.com/assets/blt4094a60cc6ca9484/Object-Space.jpg)

要理解对象空间，假设你是一名橄榄球运动员，你们队正面对着对手。如果你听到对手喊“向左跑！”，该球员肯定指的是相对于他们球队的对象空间的方向。要知道运动员所指的方向，必须将该方向转换到你们队的对象空间中。换句话说，**他们的**左边是**你的**右边。

这就是说，当我们谈到一个方向（“他的左”）的“所有权”时，我们实际上是在说“对他来说，那个方向是左”。从不同的角度来看，或者在不同的对象空间中，他说“左”而你可能会说“右”，然而两者都在谈论以不同方式表达的同一个方向。

## 位置与方向

`datatype/Vector3` 可用于存储位置数据（3D 点）和方向数据（3D 矢量），它们都使用 X、Y 和 Z 坐标，重要的是要辨识 Vector3 代表的是哪一个方向或轴。通常来说，可以从其来源进行判断：

  * `Vector3.FromNormalId` 和 `Vector3.FromAxis` 返回指向给定方向或轴的向量。  
部件的 Orientation（朝向）是世界空间中的方向矢量。
  * `CFrame:VectorToWorldSpace` 和 `CFrame:VectorToObjectSpace1` 都接受和返回 Vector3 的方向向量。
  * 减去两个 Vector3，即 `A - B`，得到的 Vector3 是 B 向 A 的方向。

## 转换函数

用于将坐标数据从对象空间转换到世界空间的函数在 `datatype/CFrame` 数据类型中。对于每一个函数，调用时的 CFrame 都应该表示的是所求对象的 CFrame。  
*以 “ToObjectSpace” 结尾的函数转换世界空间中定义的数据，并返回对象空间中定义的相同数据。  
*反之，以 “ToWorldSpace” 结尾的函数转换对象空间中定义的数据，并返回世界空间中定义的相同数据。

`CFrame:ToObjectSpace()`  
`CFrame:ToWorldSpace()`
这些函数接受一个 CFrame 然后返回一个 CFrame。

`CFrame:PointToObjectSpace()`  
`CFrame:PointToWorldSpace()`
这些函数接受一个**位置** Vector3 然后返回一个位置 Vector3。

`CFrame:VectorToObjectSpace()`  
`CFrame:VectorToWorldSpace()`
这些函数接受一个**方向** Vector3 然后返回一个方向 Vector3。

## 示例

在这些示例中，我们将继续橄榄球的例子：红队球员和蓝队球员在试图接住一个抛出的橄榄球。我们拥有两个队员各自的 CFrame：
    
    
    local redPlayerCF = workspace.RedPlayer.HumanoidRootPart.CFrame
    local bluePlayerCF = workspace.BluePlayer.HumanoidRootPart.CFrame
    local footballCF = workspace.Football.CFrame
    

  * 要找到橄榄球相对于蓝色运动员的 CFrame：  
`footballCF:ToObjectSpace(bluePlayerCF)`
  * 要确定橄榄球是否在红色运动员前方：  
`footballCF:ToObjectSpace(redPlayerCF).Z > 0`
  * 红色运动员说相对于他，橄榄球移动到了指定 CFrame `newCF`。若想确定橄榄球球相对于蓝色运动员的位置：  
`redPlayerCF:ToWorldSpace(newCF):ToObjectSpace(bluePlayerCF)`



***__Roblox官方链接__:[对象空间与世界空间](https://developer.roblox.com/zh-cn/articles/object-world-space)