# 鼠标指针控制 
Time:<em>5  分钟</em>

这篇文章详细解释了如何自定义鼠标指针行为。

## 设置鼠标图标

开发者可以在 `LocalScript` 中更换玩家的鼠标图标，只要将其 `Mouse/Icon|Icon` （图标）设置为一个自定义的 Roblox 资源 ID：

```    
    
    local Players = game:GetService("Players")
    local mouse = Players.LocalPlayer:GetMouse()
    mouse.Icon = "rbxassetid://3400146391"


```
注意，由于图标是在 `LocalScript` 中设置的，因此每个玩家的图标可以不尽相同，开发者也可以让某个图标只在特定情况下出现（比如当某个能力处于冷却时间或将鼠标悬停于某个敌人目标上时）。

## 隐藏鼠标图标

可以使用 `LocalScript` 中的 `UserInputService/MouseIconEnabled` 打开或关闭鼠标图标的可见度。例如下列编码每隔两秒就会切换一次鼠标的可见状态：

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    while true do
    	wait(2)
    	UserInputService.MouseIconEnabled = false
    	wait(2)
    	UserInputService.MouseIconEnabled = true
    end


```
## 锁定鼠标位置

可以使用值为 `enum/MouseBehavior|Enum.MouseBehavior.LockCurrentPosition` 或者 `enum/MouseBehavior|Enum.MouseBehavior.LockCenter` 的 `UserInputService/MouseBehavior` 属性来将鼠标位置锁定在屏幕上。如果想解除鼠标锁定，则把此属性的值设定回 `enum/MouseBehavior|Enum.MouseBehavior.Default` 即可。

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    wait(1)
    
    UserInputService.MouseBehavior = Enum.MouseBehavior.LockCurrentPosition
    
    UserInputService.InputChanged:Connect(function(inputObject)
    	if inputObject.UserInputType == Enum.UserInputType.MouseMovement then
    		print("Mouse delta is (" .. tostring(inputObject.Delta.X) .. ", " ..  tostring(inputObject.Delta.Y) .. ")")
    	end
    end)


```
请注意，即使鼠标处于锁定状态，当玩家移动鼠标时，仍旧会触发 `UserInputService/InputChanged`，并传入鼠标已移动距离。



***__Roblox官方链接__:[鼠标指针控制](https://developer.roblox.com/zh-cn/articles/Mouse-Icon-Appearance)