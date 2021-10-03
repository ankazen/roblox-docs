# GUI 动画 
Time:<em>5  分钟</em>

在动画中，**Tweening** （渐变）是 “in-betweening（中间过渡动画）”的缩写，指的是在一组镜头序列的两个关键点之间生成中间帧的过程。在设计用户界面时，渐变可以使 GUI 流畅地从一个位置/状态平滑过渡到另一个位置/状态，例如：

  * 流畅地增大一系列相关选项按钮中“已选定”按钮的尺寸。
  * 让 GUI 菜单滑入和滑出屏幕边缘。
  * 获得生命值提升效果时，以动画的形式让生命值栏在两种宽度间逐渐变化。

## 基本的渐变

在`articles/Intro to GUIs|GUI 简介`和`articles/Creating GUI Buttons|创建 GUI 按钮`两篇文章中，开发者已经学习了如何创建基本的文本标签和交互式按钮。这些内容和诸如 `Frame` 和 `ScrollingFrame` 等 GUI 均可通过直接附加到对象上的脚本来实现渐变。

  1. 在 “Explorer（管理器）”窗口当中，将鼠标悬停在 **StarterGui** 对象上，单击圆形 ![](https://developer.roblox.com/assets/blt0dd97240c2a0db2a/Explorer-Plus-Icon.png)

 按钮，插入一个 **ScreenGui** 对象。
  2. 选择新的 **ScreenGui** 对象，然后用相同的方法插入一个 **TextButton**。
  3. 选择新的 **TextButton** 并插入一个新的 `LocalScript`。
![](https://developer.roblox.com/assets/blta51533314e36660b/TextButton-LocalScript.png)



  4. 复制以下代码并粘贴到脚本中：

```    
    
    local object = script.Parent
    object.AnchorPoint = Vector2.new(0.5, 0.5)


```
这些变量就位之后，就可以用 GUI 基础 `GuiObject` 类的内置方法来实现 GUI 的渐变。

### 位置

GUI 的位置可以用 `GuiObject/TweenPosition|GuiObject:TweenPosition()` 方法来实现渐变。在最基本的形态下，这个方法需要一个**结束位置**（`datatype/UDim2`）来代表对象的目的地：

```    
    
    local object = script.Parent
    object.AnchorPoint = Vector2.new(0.5, 0.5)
    object.Position = UDim2.new(0.1, 0, 0.5, 0)
    
    wait(2)
    
    object:TweenPosition(UDim2.new(0.5, 0, 0.5, 0))


```
![](https://developer.roblox.com/assets/blt3e594936e6e71a36/GUI-Animation-Position.png)



请注意，这种渐变会使用 `datatype/UDim2` 的 **Scale** 参数来对比位置偏移值。这样无论屏幕的大小和方向如何，都能保证 GUI 会向屏幕的中心渐变。 

除此之外，还能通过偏偏移对象的起始位置宽度，从而让 GUI 从屏幕的左侧边缘开始渐变：

```    
    
    local object = script.Parent
    object.AnchorPoint = Vector2.new(0.5, 0.5)
    object.Position = UDim2.new(0, -object.Size.X.Offset, 0.5, 0)
    
    wait(2)
    
    object:TweenPosition(UDim2.new(0.5, 0, 0.5, 0))


```
### 尺寸

一个 GUI 的尺寸可以用 `GuiObject/TweenSize|GuiObject:TweenSize()` 方法来实现渐变，该方法能使 `datatype/UDim2` 来代表对象的最终尺寸：

```    
    
    local object = script.Parent
    object.AnchorPoint = Vector2.new(0.5, 0.5)
    object.Position = UDim2.new(0.5, 0, 0.5, 0)
    
    wait(2)
    
    object:TweenSize(UDim2.new(0.4, 0, 0.4, 0))


```
![](https://developer.roblox.com/assets/blt8ecdd717b0909821/GUI-Animation-Size.png)



上述示例使用了 `datatype/UDim2` 的 Scale（缩放）参数，但开发者也可通过使用显式 Size（尺寸）参数来调整 GUI 的大小：

```    
    
    local object = script.Parent
    object.AnchorPoint = Vector2.new(0.5, 0.5)
    object.Position = UDim2.new(0.5, 0, 0.5, 0)
    
    wait(2)
    
    object:TweenSize(UDim2.new(0, 400, 0, 100))


```
### 位置和尺寸

要用一条命令同时实现 GUI 位置和尺寸的渐变，请使用 `GuiObject/TweenSizeAndPosition|GuiObject:TweenSizeAndPosition()` 。该方法需要使用一个 `datatype/UDim2` 来代表 GUI 的最终尺寸和位置：

```    
    
    local object = script.Parent
    object.AnchorPoint = Vector2.new(0.5, 0.5)
    object.Position = UDim2.new(0, -object.Size.X.Offset, 0.5, 0)
    
    wait(2)
    
    object:TweenSizeAndPosition(UDim2.new(0.4, 0, 0.4, 0), UDim2.new(0.5, 0, 0.5, 0))


```
## 额外选项

上述所有方法都接受其他能够对 GUI 动画进行微调或对 GUI 动画加强控制能力的选项。

### 动画过渡

动画**过渡**定义渐变将出现在哪个“方向”以及渐变是什么样的风格。

方向 描述

**In（渐入）**
渐变开始时速度较慢，越接近结束时速度越快。

**Out（渐出）**
渐变开始时速度较快，越接近结束时速度越慢。

**InOut（渐入渐出）**
**渐入**和**渐出**存在于同一个渐变过程中，最开始是**渐入**，从中间开始**渐出**效果开始生效。 

风格 描述

**线性**
以恒定速度移动。

**正弦**
移动速度由一个正弦波来决定。

**返回**
渐变移动返回某个地方或者退出某个地方。

**Quad（二阶）**
以二阶插值的方式渐入或者渐出。

**Quart（四阶）**
和 **Quad（二阶）**类似，但更强调开始位置和（或）结束位置。

**Quint（五阶）**
和 **Quad（二阶）**类似，但对开始位置和（或）结束位置的强调程度更深了。

**跳动感**
移动时给人的感觉就好像渐变的起始位置和结束位置在跳动一样。

**弹性**
移动时给人的感觉就好像是对象连着一根橡皮筋一样。

过渡选项可以被定义为位于尺寸和（或者）位置 `datatype/UDim2` 值后面的 `Enum/EasingDirection` 和 `Enum/EasingStyle` 枚举值。

```    
    
    local object = script.Parent
    object.AnchorPoint = Vector2.new(0.5, 0.5)
    object.Position = UDim2.new(0, 0, 0.5, 0)
     
    wait(2)
     
    object:TweenPosition(UDim2.new(0.5, 0, 0.5, 0), Enum.EasingDirection.Out, Enum.EasingStyle.Quint)


```
### 时间

默认情况下，渐变将在 1 秒后发生，但也可以在下列过渡选项中指定具体秒数来进行调整：

```    
    
    local object = script.Parent
    object.AnchorPoint = Vector2.new(0.5, 0.5)
    object.Position = UDim2.new(0, 0, 0.5, 0)
     
    wait(2)
     
    object:TweenPosition(UDim2.new(0.5, 0, 0.5, 0), nil, nil, 3)


```
注意，如果开发者不需要更改 **Out（渐出）**的 `Enum/EasingDirection` 默认值或者 **Quad（二阶）**的 `Enum/EasingStyle` 默认值，则可使用 `nil` 可进行代替。 

## 高级渐变

上述方法都是实现 GUI 位置和尺寸的渐变方式，但这些方法无法实现旋转、颜色或透明度等层面的渐变，若要实现这些渐变，开发者就得使用一种名为 `TweenService` 的工具，该工具功能十分强大，能实现几乎所有属性或属性组合的渐变。

### 颜色渐变

某些动画需要 `datatype/Color3` 属性的渐变，例如当玩家的生命值降到特定百分比以下时，生命值栏的颜色会从绿色变为黄色。

  1. 在 Explorer（管理器）窗口中，将鼠标悬停在之前创建的 **ScreenGui** 对象上，然后插入一个 **Frame（框架）**。
  2. 选择新的框架对象，然后插入一个新的 `LocalScript`。
  3. 复制下列编码并将其粘贴到脚本中：

```    
    
    local TweenService = game:GetService("TweenService")
    
    local frame = script.Parent
    frame.Position = UDim2.new(0, 20, 0, 20)
    frame.BorderSizePixel = 0
    frame.Size = UDim2.new(0, 400, 0, 30)
    frame.BackgroundColor3 = Color3.fromRGB(0, 255, 75)
    
    -- 声明目标尺寸和颜色值
    local newSize = UDim2.new(0, frame.Size.X.Offset*0.5, 0, frame.Size.Y.Offset)
    local newColor = Color3.fromRGB(255, 255, 50)
    
    -- 设置渐变
    local tweenInfo = TweenInfo.new(1.5, Enum.EasingStyle.Quart, Enum.EasingDirection.Out)
    local tween = TweenService:Create(frame, tweenInfo, {Size=newSize, BackgroundColor3=newColor})
    
    wait(2)
    
    tween:Play()


```
此代码作用如下：

  * 在 4 至 7 行中设置框架的位置、边界、尺寸和背景颜色（绿色）。
  * 在 10 至 11 行显示目标的尺寸和背景颜色。
  * 在 14 行声明一个新的 `datatype/TweenInfo` 对象，令其以 **Out（渐出）**过渡的方式存在 1.5 秒。
  * 在 15 行创建一个新的 `Tween`，该渐变将框架的 `GuiObject/Size|Size` （尺寸）插补为 `newSize`、将框架的 `GuiObject/BackgroundColor3|Backgroundolor3` 插补为 `newColor`。
  * 在 19 行播放渐变。

### 连续渐变

连续性的设置对某些动画效果有利，例如在移动渐变后的旋转渐变。要实现这一效果，可以在第一个渐变事件 `TweenBase/Completed|Completed` （完成后）立马开始第二个渐变：

```    
    
    local TweenService = game:GetService("TweenService")
    
    local frame = script.Parent
    frame.AnchorPoint = Vector2.new(0.5, 0.5)
    frame.Position = UDim2.new(0, 70, 0, 70)
    frame.BorderSizePixel = 0
    frame.Size = UDim2.new(0, 100, 0, 100)
    frame.BackgroundColor3 = Color3.new(0, 0, 0)
    
    -- 设置渐变
    local tweenInfo1 = TweenInfo.new(1, Enum.EasingStyle.Sine, Enum.EasingDirection.Out)
    local tween1 = TweenService:Create(frame, tweenInfo1, {Position=UDim2.new(0.5, 0, 0.5, 0)})
    local tweenInfo2 = TweenInfo.new(1.5, Enum.EasingStyle.Quart, Enum.EasingDirection.InOut)
    local tween2 = TweenService:Create(frame, tweenInfo2, {Rotation=180})
    
    tween1.Completed:Connect(function()
    	tween2:Play()
    end)
    
    wait(2)
    
    tween1:Play()


```


***__Roblox官方链接__:[GUI 动画](https://developer.roblox.com/zh-cn/articles/GUI-Animations)