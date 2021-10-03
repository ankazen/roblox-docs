# 试验模式 
Time:<em>10  分钟</em>

当 “Experimental Mode”（试验模式）仍然可用时，开发者们创建了许多旧式场景与模型。但[但模式目前已被禁用](https://devforum.roblox.com/t/removal-of-experimental-mode/152807)。本文概述了一些在当前 Roblox 架构中无法使用的常见设计实例及解决方案。

## 创建部件

有时在玩家进行操作时，需要向游戏世界内插入新的部件。在“试验模式”中， `LocalScript` 可以创建新部件并通知服务器，而后服务器将会更新其他客户端。

转换试验模式的游戏：代码示例 1 ```    
    
    local Players = game:GetService("Players")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    local player = Players.LocalPlayer
    local playerGui = player:WaitForChild("PlayerGui")
    local screenGui = playerGui:WaitForChild("ScreenGui")
    local spawnCarButton = screenGui:WaitForChild("SpawnCarButton")
    
    local carTemplate = ReplicatedStorage:WaitForChild("Car")
    
    local function onClick()
    	local car = carTemplate:Clone()
    	local character = player.Character
    	local humanoidRootPart = character:FindFirstChild("HumanoidRootPart")
    	if humanoidRootPart then
    		local spawnPosition = humanoidRootPart.CFrame + Vector3.new(0, 10, 0)
    		car:SetPrimaryPartCFrame(spawnPosition)
    		car.Parent = game.Workspace
    	end
    end
    
    spawnCarButton.MouseButton1Click:Connect(onClick)


```
而且，此代码在“试验模式”下运行顺畅，但现在只能针对本机玩家生成车辆，其他玩家无法看到或与之互动！

查看解决方案

`LocalScript` 应当触发 `RemoteEvent` 并且服务器 `Script` 应当管理车的实际生成。
    
    
    -- LocalScript（客户端）
    local Players = game:GetService("Players")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    
    local player = Players.LocalPlayer  
    
    local playerGui = player:WaitForChild(“PlayerGui”)  
    
    local screenGui = playerGui:WaitForChild(“ScreenGui”)  
    
    local spawnCarButton = screenGui:WaitForChild(“SpawnCarButton”)
    
    
    
    
    local spawnCarEvent = ReplicatedStorage:WaitForChild(“SpawnCarEvent”)
    
    
    
    
    local function onClick()  
    
    spawnCarEvent:FireServer()	  
    
    end
    
    
    
    
    spawnCarButton.MouseButton1Click:Connect(onClick)  
    
    



***__Roblox官方链接__:[试验模式](https://developer.roblox.com/zh-cn/articles/Converting-From-Experimental-Mode)