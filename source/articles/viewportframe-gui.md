# ViewportFrame GUI 
Time:<em>5  分钟</em>

`ViewportFrame` 是一种 `GuiObject`，可在其边界内呈现 3D 对象。它可以在 `ScreenGui` 等 2D GUI 空间中很好的显示 3D 对象/模型。

如果你还没有阅读 `articles/Intro to GUIs|GUI 简介`指南，请先阅读该指南，然后再继续学习本教程。 

## 创建 ViewportFrame

可按以下步骤创建新的 `ViewportFrame`：

  1. 在 **ScreenGui** 文件夹中创建一个新的 **StarterGui**。
![](https://developer.roblox.com/assets/blt37c2628537f9d291/Create-ScreenGui.png)



  2. 在新的屏幕 GUI 对象中插入一个 `LocalScript`。
![](https://developer.roblox.com/assets/blt72517c1a2eb7b775/ScreenGui-LocalScript.png)



  3. 在脚本中粘贴以下代码：

```    
    
    local viewportFrame = Instance.new("ViewportFrame")
    viewportFrame.Size = UDim2.new(0.3, 0, 0.4, 0)
    viewportFrame.Position = UDim2.new(0, 15, 0, 15)
    viewportFrame.BackgroundColor3 = Color3.new(0, 0, 0)
    viewportFrame.BorderColor3 = Color3.new(0.6, 0.5, 0.4)
    viewportFrame.BorderSizePixel = 2
    viewportFrame.BackgroundTransparency = 0.25
    viewportFrame.Parent = script.Parent
    
    local part = Instance.new("Part")
    part.Material = Enum.Material.Concrete
    part.Color = Color3.new(0.25, 0.75, 1)
    part.Position = Vector3.new(0, 0, 0)
    part.Parent = viewportFrame
    
    local viewportCamera = Instance.new("Camera")
    viewportFrame.CurrentCamera = viewportCamera
    viewportCamera.Parent = viewportFrame
    
    viewportCamera.CFrame = CFrame.new(Vector3.new(0, 2, 12), part.Position)


```
  4. 进行游戏测试，你会看到一个包含 `part` 对象的新视口帧。

Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link]() to the video instead. 

### 关键点

检查脚本中用于创建视口帧的主要因素：

  * 第 1-8 行设置基本的视口帧，并将其作为 `ScreenGui` 的父对象。许多属性与 `articles/Intro to GUIs|GUI 简介`指南中说明的属性相似。

```    
    
    local viewportFrame = Instance.new("ViewportFrame")
    viewportFrame.Size = UDim2.new(0.3, 0, 0.4, 0)
    viewportFrame.Position = UDim2.new(0, 15, 0, 15)
    viewportFrame.BackgroundColor3 = Color3.new(0, 0, 0)
    viewportFrame.BorderColor3 = Color3.new(0.6, 0.5, 0.4)
    viewportFrame.BorderSizePixel = 2
    viewportFrame.BackgroundTransparency = 0.25
    viewportFrame.Parent = script.Parent


```
  * 在下一个代码块中，创建一个基本的 `Part`。最重要的是，该部件是第 14 行视口帧的**父对象**：

```    
    
    local part = Instance.new("Part")
    part.Material = Enum.Material.Concrete
    part.Color = Color3.new(0.25, 0.75, 1)
    part.Position = Vector3.new(0, 0, 0)
    part.Parent = viewportFrame


```
  * 在第 16-18 行中，创建一个新的 `Camera`，然后将其分配至 `ViewportFrame/CurrentCamera|CurrentCamera` 属性，并将其作为 `viewportFrame` 的父对象。这是一个关键点，因为视口不使用默认的通用镜头，而使用自身镜头来呈现玩家看到的“视图”。

```    
    
    local viewportCamera = Instance.new("Camera")
    viewportFrame.CurrentCamera = viewportCamera
    viewportCamera.Parent = viewportFrame


```
  * 在最后一行，通过重置其 `datatype/CFrame|CFrame`，将新镜头置于部件的相对位置。

```    
    
    viewportCamera.CFrame = CFrame.new(Vector3.new(0, 2, 12), part.Position)


```
如果你不熟悉 CFrames，请查看文章 `articles/Understanding CFrame|CFrames 须知`。 

## 控制镜头

如上所示，可通过重置其 `datatype/CFrame|CFrame` 来移动视口镜头。这意味着可以通过操纵镜头的方向来动态更改帧的游戏内视图。

考虑在脚本中添加以下内容。在第一行，我们通过 `TweenService` 服务逐步移动镜头。2 秒钟后，配置并播放一个新的 `Tween`，让镜头更靠近部件。

```    
    
    local TweenService = game:GetService("TweenService")
    
    local viewportFrame = Instance.new("ViewportFrame")
    viewportFrame.Size = UDim2.new(0.3, 0, 0.4, 0)
    viewportFrame.Position = UDim2.new(0, 15, 0, 15)
    viewportFrame.BackgroundColor3 = Color3.new(0, 0, 0)
    viewportFrame.BorderColor3 = Color3.new(0.6, 0.5, 0.4)
    viewportFrame.BorderSizePixel = 2
    viewportFrame.BackgroundTransparency = 0.25
    viewportFrame.Parent = script.Parent
    
    local part = Instance.new("Part")
    part.Material = Enum.Material.Concrete
    part.Color = Color3.new(0.25, 0.75, 1)
    part.Position = Vector3.new(0, 0, 0)
    part.Parent = viewportFrame
    
    local viewportCamera = Instance.new("Camera")
    viewportFrame.CurrentCamera = viewportCamera
    viewportCamera.Parent = viewportFrame
    
    viewportCamera.CFrame = CFrame.new(Vector3.new(0, 2, 12), part.Position)
    
    wait(2)
    
    local cameraGoal = {
    	CFrame = CFrame.new(Vector3.new(0, 6, 4), part.Position)
    }
    
    local tweenInfo = TweenInfo.new(2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out)
    
    local tween = TweenService:Create(viewportCamera, tweenInfo, cameraGoal)
    
    tween:Play()


```
Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link]() to the video instead. 

## 备注/性能

以下是创建视口帧的一些重要考虑因素：

  * 每个视口帧都将创建一个用于呈现的纹理。该纹理具有最大尺寸限制，因此如果帧太大，内容可能会看起来很模糊。

  * 仅当其子对象（镜头或其中的对象）发生变更时，视口才会更新。

  * 移动视口的物理子对象不如使其保持静态。如果您需要更新视图，最好移动镜头，而不是移动部件/模块。

  * 视口帧并不是为了呈现大量复杂对象而设计；如果在其中放置太多对象，可能导致响应缓慢。

  * 视口内的对象将使用固定光源设置来呈现，尽管将来可能会有更多选项可用。当前并无阴影或后期特效可用。



***__Roblox官方链接__:[ViewportFrame GUI](https://developer.roblox.com/zh-cn/articles/viewportframe-gui)