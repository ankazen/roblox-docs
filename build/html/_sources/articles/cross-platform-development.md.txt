# 跨平台开发 
Time:<em>10  分钟</em>

本文概述了在多个平台上进行 Roblox 游戏开发的最佳方法。

## Roblox 理念

与其他游戏引擎不同，Roblox **本身就是跨平台的**，玩家们可以在电脑上发现并游玩游戏，然后拿起手机并接着之前的进度继续游玩。在大多数情况下，Roblox 游戏应该可以在**所有**平台上游玩，而不是仅针对一个平台优化而在其他平台上“勉强能玩”。

## 手机第一

近期数据表明**超过 55%** 的 Roblox 游戏进程是在手机上进行的，所以您应该付出同等的努力来打造出色的手机游戏体验。在计划您的 UI 和控制时，请考虑以下几点：

### UI 布局

即使 GUI 完美地适合电脑屏幕，在较小的手机屏幕上也不一定同样好用。例如，这个 GUI 中的颜色自定义砖块在手机上就变得太小太窄了：

![](https://developer.roblox.com/assets/bltdfd5f2922f2d90a6/Cross-Platform-UI-Layout-1.png)



相比之下，稍微重新设计 GUI 就能同时提升电脑用户和手机用户的体验：

![](https://developer.roblox.com/assets/blt1c2c28ad6447cb63/Cross-Platform-UI-Layout-2.png)



### 保留区域

在移动设备上，`/articles/customizing game controls#mobile-controls|默认控制`占据屏幕左下角及/或右下角的一部分。在设计游戏 UI 时，请避免将重要信息或虚拟按钮放在这些区域。

![](https://developer.roblox.com/assets/blt16669895b1299201/Cross-Platform-Reserved-Regions.png)



如果您的游戏使用默认**UserChoice**控制设置（`/articles/customizing game controls#mobile-controls|reference`），屏幕上显示的控制可能会有少许偏差。在设计您的 UI 时请考虑到这个可能性。 

### 拇指区

大多数手机玩家使用两个大拇指，一个控制虚拟摇杆/方向键，另一个控制跳跃键。根据设备尺寸和玩家的手部大小， 远离底部角落的按钮会很难按或者根本够不到，所以您应当避免将常用按钮置于绿色区域外。

![](https://developer.roblox.com/assets/blt8500a5dd039d1510/Cross-Platform-Thumb-Zones.png)



### 适应性 UI

舒适的拇指区在手机与平板电脑上有所差别，因为平板电脑的屏幕更大。请记住一个放在屏幕顶部边缘 30% 以下的按钮在手机上可以轻易够到，但在平板电脑上几乎不可能够到。

![](https://developer.roblox.com/assets/bltcbf8f4be72c57d4e/Cross-Platform-Adaptable-UI.png)



相对跳跃按钮来设置自定义按钮的位置更为可靠。以下代码获取跳跃按钮的位置，并在上面创建一个占位的 `ImageButton` 按钮：

```    
    
    -- 获得玩家的跳跃键的参考
    local player = game.Players.LocalPlayer
    local PlayerGui = player:WaitForChild("PlayerGui")
    local ScreenGui = PlayerGui:WaitForChild("ScreenGui")
    local TouchGui = PlayerGui:WaitForChild("TouchGui")
    local TouchControlFrame = TouchGui:WaitForChild("TouchControlFrame")
    local JumpButton = TouchControlFrame:WaitForChild("JumpButton")
    
    -- 获得按键的绝对尺寸和位置
    local absSizeX, absSizeY = JumpButton.AbsoluteSize.X, JumpButton.AbsoluteSize.Y
    local absPositionX, absPositionY = JumpButton.AbsolutePosition.X, JumpButton.AbsolutePosition.Y
    
    -- 在跳跃键上创建新按键
    local customButton = Instance.new("ImageButton")
    customButton.Parent = ScreenGui
    customButton.AnchorPoint = Vector2.new(0.5, 1)
    customButton.Size = UDim2.new(0, absSizeX*0.8, 0, absSizeY*0.8)
    customButton.Position = UDim2.new(0, absPositionX+(absSizeX/2), 0, absPositionY-20)


```
### 基于内容的 UI

移动设备上的屏幕空间非常有限，因此在游玩时应当只显示最关键的信息。例如，如果玩家有一个特殊动作可以打开门，那么无需把“开门”的按钮一直显示在屏幕上，而应当只在玩家接近门的时候才显示，并在玩家离开一段距离之后消失。

## 输入检测

有时必须获知玩家当前的设备以便调整 UI，显示行动按钮或提示等等。例如，如果玩家接近一只宝箱，并且有一个获取金币的动作，您可以在电脑端玩家的屏幕上显示 T 键图标，但在移动端玩家的屏幕上激活“收集”按钮。

![](https://developer.roblox.com/assets/blt25ec84c0f29d3831/Cross-Platform-Input-Detection-Mobile.png)

 移动端：激活**收集**按钮

![](https://developer.roblox.com/assets/blt57b1b33eb3c0444f/Cross-Platform-Input-Detection-PC.png)

 电脑端：**T** 键提示

以下 `ModuleScript`，置于 `ReplicatedStorage` 内并重命名为 **PlayerInputModule**，可用于获取玩家的输入类型，以便您根据上文的建议调整 UI 布局或内容。

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    local PlayerInput = {}
    
    local inputTypeString
    -- 如果设备有激活的键盘和鼠标，默认使用这些输出
    if UserInputService.KeyboardEnabled and UserInputService.MouseEnabled then
    	inputTypeString = "Keyboard/Mouse"
    -- 或如果有触控功能但没有键盘和鼠标，默认使用触控输入
    elseif UserInputService.TouchEnabled then
    	inputTypeString = "Touch"
    -- 或如果设备有活动的手柄，默认手柄输入
    elseif UserInputService.GamepadEnabled then
    	inputTypeString = "Gamepad"
    end
    
    function PlayerInput.getInputType()
    	local lastInputEnum = UserInputService:GetLastInputType()
    
    	if lastInputEnum == Enum.UserInputType.Keyboard or string.find(tostring(lastInputEnum.Name), "MouseButton") or lastInputEnum == Enum.UserInputType.MouseWheel then
    		inputTypeString = "Keyboard/Mouse"
    	elseif lastInputEnum == Enum.UserInputType.Touch then
    		inputTypeString = "Touch"
    	elseif string.find(tostring(lastInputEnum.Name), "Gamepad") then
    		inputTypeString = "Gamepad"
    	end
    	return inputTypeString, lastInputEnum
    end
    
    return PlayerInput


```
请注意脚本使用 `UserInputService/GetLastInputType|UserInputService:GetLastInputType()` 方法，而不仅是检查设备是否有触控之类的输入“能力”。这是因为电脑端玩家可能会倾向于使用键盘和鼠标，即使他们的电脑有触控屏，而您的 UI 应该遵从**活动的**输入类型。 

在 **PlayerInputModule** 脚本就位后，您可以用如下方式从 `LocalScript` 获取玩家最后的输入类型：

```    
    
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    -- 对模块进行 Require
    local PlayerInputModule = require(ReplicatedStorage:WaitForChild("PlayerInputModule"))
    
    local currentPlayerInput, inputEnum = PlayerInputModule.getInputType()
    print(currentPlayerInput, inputEnum)


```


***__Roblox官方链接__:[跨平台开发](https://developer.roblox.com/zh-cn/articles/cross-platform-development)