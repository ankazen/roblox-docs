# 横向卷轴镜头 
Time:<em>10  分钟</em>

一般来说，横向卷轴类的游戏有几种不同的镜头风格。此教程中使用了一种较为常见的模式，在这种情况下，如果玩家的位置逐渐变得过于靠左或靠右，镜头就会相应地向着左侧或右侧移动。其他时候，镜头会保持静止。

## 设置

首先要设置的是镜头自身。我们需要覆盖 Roblox 默认镜头脚本，以便编写我们自己的脚本。为此，请将 “LocalScript” 插入至 “StarterPlayerScripts” 中，然后将其重命名为 _CameraScript_。

![CameraScript](https://developer.roblox.com/assets/blta84a5bf7d6c042d1/2D_Platformer_Image02.png)



现在，我们需要初始化镜头启动的位置。

自定义镜头控制：代码示例 1 ```    
    
    local cameraHeight = 12
    local cameraZOffset = 20
     
    local camera = game.Workspace.CurrentCamera
    local player = game.Players.LocalPlayer
     
    local function setupCamera()
    	camera.CFrame = CFrame.new(Vector3.new(0,cameraHeight,cameraZOffset), Vector3.new(0,cameraHeight,0))
    end
    setupCamera()
    player.CharacterAdded:Connect(setupCamera)


```
首先，为镜头高度以及我们希望镜头远离玩家所行走的平面的距离设置变量。我们会将这些变量置于顶部，以便稍后我们需要对其进行调整时可以轻松找到它们。

然后针对镜头和玩家获取变量。在 LocalScript 中，`game.Workspace.CurrentCamera` 将返回本地玩家的镜头，`game.Players.LocalPlayer` 则获取本地玩家。

接下来，我们创建一个函数以设置镜头的初始位置。当玩家首次进入游戏且角色复活时，我们都需要此信息。在此函数中，我们只需设置镜头的 CFrame。

CFrame（CoordinateFrame 的缩写）将存储对象的位置及其方位。它们的常见用途是操作部件，但是玩家的镜头也存在 CFrame。尽管创建 CFrame 的方式有多种，但我们将使用 CFrame 的新功能，即将两个 Vector3 视为参数。第一个 Vector3 用于确定 CFrame 的位置。第二个 Vector3 用于设置 CFrame 指向何处。

我们会在声明该函数后立即对其进行调用，以便镜头在玩家加入时就被置于右侧位置。此外，我们还会将该函数绑定至玩家的 CharacterAdded 事件，以便只要玩家角色复活时就可以调用此函数。

### 移动镜头

现在，我们需要随着玩家角色移至右侧时移动镜头。处理镜头移动时，了解渲染功能在 Roblox 中的工作方式至关重要。镜头决定了我们希望玩家在 3D 场景中所看向的确切位置，而该位置则决定要在屏幕上渲染的内容。Roblox 引擎将大约每 1/60 秒刷新一次该渲染；快速执行此渲染操作意味着观看者会看到帧之间是平滑过渡的。为确保镜头顺利移动，我们需要保证在每次刷新此渲染时更新镜头的位置。幸运的是，使用名为 `RunService/BindToRenderStep` 的函数可以非常轻松地完成此操作。

自定义镜头控制：代码示例 2 ```    
    
    local cameraHeight = 12
    local cameraZOffset = 20
    local cameraXChase = 10
    local cameraSpeed = .25
    
    local camera = game.Workspace.CurrentCamera
    local player = game.Players.LocalPlayer
    local RunService = game:GetService('RunService')
    
    local function setupCamera()
    	camera.CFrame = CFrame.new(Vector3.new(0,cameraHeight,cameraZOffset),
    										Vector3.new(0,cameraHeight,0))
    end
    setupCamera()
    player.CharacterAdded:Connect(setupCamera)
    
    local function onUpdate()
    	if player.Character and player.Character:FindFirstChild('Torso') then
    		local playerX = player.Character.Torso.Position.X
    		local cameraX = camera.CFrame.p.X
    		
    		if cameraX - cameraXChase < playerX then
    			camera.CFrame = camera.CFrame + Vector3.new(cameraSpeed, 0, 0)
    		end
    	end
    end
    
    RunService:BindToRenderStep('Camera', Enum.RenderPriority.Camera.Value, onUpdate)


```
此时我们要执行几项操作，现在让我们逐一进行。首先，再多声明几个变量，`cameraXChase` 表示在镜头开始移动之前，玩家可以离 X 维度的镜头有多远。`cameraSpeed` 表示在每次执行渲染步骤时镜头将移动多远才能追上玩家。

我们要声明的下一个变量是仅需要使用其 `RunService/BindToRenderStep` 函数的 “RunService”。跳至相应脚本末尾，你会发现，我们调用了具有三个值的 BindToRenderStep。第一个值是此绑定的名称，第二个值是要执行渲染步骤的时间，最后一个值是要绑定的函数（在此示例中，就是我们的自定义函数 `onUpdate()`）。

`onUpdate()` 会执行几项操作。首先，它会检查玩家是否具有人物模型，以及该模型是否具有名为 `Torso` 的部件。如果没有这些内容，玩家很可能正在生成或正在离开游戏。在任一情况下，我们实际上并不需要镜头执行任何操作。但是，如果玩家具有人物角色，我们可以获取该人物的 X 位置和镜头的 X 位置。然后，检查人物离镜头有多远。如果人物离镜头太近，我们可以将镜头的 `CFrame` 更新至右侧。

![2D_Platformer_Image01.png](https://developer.roblox.com/assets/blt20447ff54f63a829/2D_Platformer_Image01.png)



在这种情况下，镜头应该不会移动。

![2D_Platformer_Image04.png](https://developer.roblox.com/assets/blt6e7f8c0fee8cf0cc/2D_Platformer_Image04.png)



在这种情况下，镜头应该会移动。

## 控件

既然镜头已锁定至侧视图，现在我们来添加自定义控件以仅在 XY 平面移动人物。此代码将处理输入设备，因此它需要进入 `LocalScript`。将另一个 LocalScript 插入 `StarterPlayerScripts` 中，然后将其重命名为 `ControlScript`。如同插入名为 `CameraScript` 的 LocalScript 会覆盖默认镜头控件一样，`ControlScript` 将覆盖默认人物控件。你的 StarterPlayerScripts 现在应如下所示：

![2D_Platformer_Image03.png](https://developer.roblox.com/assets/blt22fde03920bd3508/2D_Platformer_Image03.png)



### 绑定控件

在 LocalScript 中，我们将需要创建多个函数并将其绑定至玩家的输入设备。执行此操作有多种方式，但是最便捷的一种方式是使用 `ContextActionService`。此服务可用于将多个输入源绑定至一个函数。如果你希望你的游戏处理各种受 Roblox 支持的输入设备（键盘、触摸屏、游戏手柄等），此方法将非常有用。

在编写实际上会移动玩家角色的代码之前，我们先设置控件绑定。在新的 LocalScript 中，添加以下内容：

与在 `CameraScript` 中一样，我们会为玩家和 RunService 创建各种变量。此外，我们还需要为 ContextActionService 创建变量。然后，为玩家可在游戏中执行的每个操作创建一个函数：`onLeft`、`onRight` 和 `onJump`。这些函数具有两个参数：操作名称和调用该函数的输入设备的状态。

即使我们仅针对输入函数使用 `inputState` 参数，也仍需要将操作名称作为第一个参数附上，因为调用这些参数的事件同时包含这两个参数。例如，请考虑使用以下代码：
    
    
    local function test1(a, b)
    	print(b)
    end
    
    local function test2(b)
    	print(b)
    end
    
    test1("dog", "cat")
    test2("dog", "cat")
    

如果我们希望该函数在此示例中打印输出“cat”，则需要使用 `test1`，因为 “cat” 是作为第二个参数传入的。

与在 `CameraScript` 中类似，我们还会创建绑定至 RenderStepped 的更新函数。此函数会在我们处理输入后实际移动人物。请确保将绑定的优先级设置为 `Input`（之前使用的是 `Camera`）。

接下来，我们使用 “BindAction” 绑定三个输入函数。BindAction 具有多个参数。第一个参数是操作名称。第二个参数是要绑定的函数。第三个参数是是否要在手机和平板电脑等触摸设备上为此操作自动创建按钮。最后，你可以附上要触发该操作的输入设备列表。如果输入设备只是键盘上的一个字母键，则可以将其作为由引号 ("") 包围的字符串附上。否则，你可以使用 `Enum/KeyCode` 来指定特殊键和按钮。

### 移动角色

现在，我们来添加以下代码以移动人物。我们将再次在 `onUpdate` 函数中执行实际移动操作。所有输入函数都将设置变量 _onUpdate_，该变量将用于确定移动人物的方式。
    
    
    local player = game.Players.LocalPlayer
    local RunService = game:GetService("RunService")
    local ContextActionService = game:GetService("ContextActionService")
    
    local jumping = false
    local leftValue, rightValue = 0, 0
    
    local function onLeft(actionName, inputState)
    	if inputState == Enum.UserInputState.Begin then	
    		leftValue = 1
    	elseif inputState == Enum.UserInputState.End then
    		leftValue = 0
    	end
    end
    
    local function onRight(actionName, inputState)
    	if inputState == Enum.UserInputState.Begin then
    		rightValue = 1
    	elseif inputState == Enum.UserInputState.End then
    		rightValue = 0
    	end
    end
    
    local function onJump(actionName, inputState)
    	if inputState == Enum.UserInputState.Begin then
    		jumping = true
    	elseif inputState == Enum.UserInputState.End then
    		jumping = false
    	end
    end
    
    local function onUpdate()
    	if player.Character and player.Character:FindFirstChild("Humanoid") then
    		if jumping then
    			player.Character.Humanoid.Jump = true
    		end
    		local moveDirection = rightValue - leftValue
    		player.Character.Humanoid:Move(Vector3.new(moveDirection,0,0), false)
    	end
    end
    
    RunService:BindToRenderStep("Control", Enum.RenderPriority.Input.Value, onUpdate)
    
    ContextActionService:BindAction("Left", onLeft, true, "a", Enum.KeyCode.Left, Enum.KeyCode.DPadLeft)
    ContextActionService:BindAction("Right", onRight, true, "d", Enum.KeyCode.Right, Enum.KeyCode.DPadRight)
    ContextActionService:BindAction("Jump", onJump, true, "w", Enum.KeyCode.Space, Enum.KeyCode.Up, Enum.KeyCode.DPadUp, Enum.KeyCode.ButtonA)
    

我们先设置三个新变量：`jumping`、`leftValue` 和 `rightValue`。`jumping` 仅为布尔值：玩家即将跳跃或未跳跃。不过，Left 和 right 变量要复杂一点。当玩家按下左键时，人物应该明显向左移动，但是当玩家在按住左键的同时按下右键，人物应该会停下来。如果玩家释放左键或右键，人物应该向仍被按住的键所对应的方向移动。为每个方向创建一个变量将会很有用，因为你会在 `onUpdate` 函数中看到它们。

你可能已经注意到，`leftValue` 和 `rightValue` 的编写方式很奇怪。在 Lua 中声明变量的方式有多种，并且这种样式在要使用更少的代码行来设置变量时非常有用。请注意，以下行
    
    
    local leftValue, rightValue = 0, 0
    

可以简单编写为
    
    
    local leftValue = 0
    local rightValue = 0
    

在每个输入函数中，我们会检查 `inputState`，该函数仅指出触发该函数的输入事件的类型。在这种情况下，我们只关心玩家何时按下按键 (`Enum/UserInputState/Begin`) 以及何时释放按键 (`Enum/UserInputState/End`)。在 `onLeft` 和 `onRight` 中，如果按下匹配键，我们会将相应变量设置为 1。如果按键被释放，值将设置为 0。在 `onJump` 中，我们会在 jump 输入启动时将 jumping 变量设置为 true，并在该输入结束时设置为 false。

在 `onUpdate` 中，我们会先检查代表玩家的人物是否存在，以及它的 `Humanoid` 是否完整。如果完整，我们会检查 jumping 变量是否设置为 true。如果是，我们会将玩家的 Humanoid 的 “Jump” 属性设置为 true。

你无需随时将 Jump 属性设置为 false。Roblox 引擎会自动为你执行该操作。 

接下来，`onUpdate` 会指出人物移动的方向，方法是从 `rightValue` 中减去 `leftValue`。请记住，这些变量可以单独进行设置。如果同时按住这两个键，结果将为 0，表示人物不会移动。如果按住其中一个键，则其中一个值为 1，差为 1 或 -1。然后，调用人物的 Humanoid 上的 `Move()` 函数，以传入我们刚刚计算出的差。此函数会强制人物朝我们提供的方向移动。由于我们仅在 X 维度设置了值，因此，人物只能沿该轴移动。



***__Roblox官方链接__:[横向卷轴镜头](https://developer.roblox.com/zh-cn/articles/Side-Scrolling-Camera-View)