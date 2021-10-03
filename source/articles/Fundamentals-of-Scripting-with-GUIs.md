# GUI 脚本简介 
Time:<em>15  分钟</em>

## 关于 UDim2

UDim2 是调整 GUI 的大小并进行定位的系统。与 `Vector3` 不同，它用于定位部件。`UDim2/new` 函数接受四个参数：xScale、xOffset、yScale 和 yOffset。xScale 和 yScale 将返回相对于其父对象大小的值。如果 GUI 的父对象宽度为 100，则将 xScale 设置为 0.5 将返回 50，而将 xScale 设置为 1 将返回 100。高度和 yScale 也是如此。xOffset 是添加到 xScale 返回的任意数的像素数。例如，如果父对象宽度为 100，xScale 为 0.5，xOffset 为 25，则将返回 75 (100*0.5 + 25)。yOffset 和 yScale 也是如此。

借助 UDim2，开发者可以在玩家屏幕上以编程方式调整 UI 元素的大小并进行定位。例如：
    
    
    local frame = Instance.new("Frame")
    frame.Position = UDim2.new(0.25, 0, 0.25, 0)
    frame.Size = UDim2.new(0.5, 0, 0.5, 0)
    

这样会创建定位在显示器中央的矩形 GUI，并覆盖 25% 的屏幕（一半宽度和一半高度）。

注意：这些 2D GUI 使用的 XY 网格与 Roblox 其余部分使用的坐标不同。(0, 0) 位置位于 GUI 元素的左上角。在此网格中，右侧为 X 正方向，下侧是 Y 正方向。 

## GUI 类型

在 Roblox 中，所有 GUI 必须位于特殊容器内。有三种不同类型的容器用于显示 GUI。它们是：

  * `ScreenGui`
  * `SurfaceGui`
  * `BillboardGui`

![GuiTypes.png](https://developer.roblox.com/assets/blt5c4ac4854c6270ae/GuiTypes.png)



### ScreenGui

`ScreenGui` 直接绘制到玩家屏幕（在游戏世界中没有位置）。这通常用于玩家旅行所需的 HUD、缩略图、任何信息或图形。ScreenGui 中的元素仅对拥有它们的玩家可见。要将 ScreenGui 添加到游戏中，可以将其置于 `StarterGui` 中（会将其复制到加入游戏的每位新玩家），也可以将其直接置于玩家的 `PlayerGui` 中（在这种情况下，仅对该玩家可见）。

### SurfaceGui

`SurfaceGui` 绘制在 `Part` 的表面上。这会粘在部件上，即使部件移动或旋转也是如此。要将 SurfaceGui 添加到游戏中，可以将其直接置于要在其上绘制的部件中（它会为所有玩家显示 GUI）。或者，可以将 SurfaceGui 置于 `StarterGui` 中（它会将其复制到加入游戏的每位新玩家），也可以将其直接置于玩家的 `PlayerGui` 中（在这种情况下，仅对该玩家可见）。如果将 SurfaceGui 置于 StarterGui 或 PlayerGui 中，则必须将 `SurfaceGui/Adornee` 设置为要显示 GUI 的部件。

### BillboardGui

`BillboardGui` 绘制在 `Part` 的位置上，但将始终面向玩家。如果部件移动，BillboardGui 也会随着一起移动。如果仅使用 `BillboardGui/Size` UDim2 的 Scale 组件设置 BillboardGui 的大小，则会根据与玩家的距离进行调整（即，玩家越近就会变得越大，玩家越远就会变得越小）。如果设置了 Size 的 Offset，则 BillboardGui 将保持相同大小，无论与玩家的距离为何。

可以将 BillboardGui 直接置于要在其上绘制的部件中（它会为所有玩家显示 GUI）。或者，可以将 BillboardGui 置于 `StarterGui` 中（它会将其复制到加入游戏的每位新玩家），也可以将其直接置于玩家的 `PlayerGui` 中（在这种情况下，仅对该玩家可见）。如果将 BillboardGui 置于 StarterGui 或 PlayerGui 中，则必须将 `BillboardGui/Adornee` 设置为要显示 GUI 的部件。

## GUI 对象

有多个 GUI 对象可用于创建用户界面，但所有 GUI 对象必须位于容器内（请参阅<a href="#gui-types>GUI 类型



***__Roblox官方链接__:[GUI 脚本简介](https://developer.roblox.com/zh-cn/articles/Fundamentals-of-Scripting-with-GUIs)