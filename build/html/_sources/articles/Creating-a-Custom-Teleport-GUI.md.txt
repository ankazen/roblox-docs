# 创建自定义传送屏幕 
Time:<em>5  分钟</em>

当玩家在实例之间进行传送时，Roblox 会提供一条消息。如果需要，可以禁用此 GUI 以便使用自定义屏幕。添加自己的自定义 GUI 可以使游戏中各个场景之间的过渡看起来不那么明显，从而为玩家提供更流畅的体验。

## 如何禁用默认 GUI

禁用默认消息非常简单。在 `Script` 或 `LocalScript` 中将 `TeleportService/CustomizedTeleportUI|CustomizedTeleportUI` 设置为 true 即可：
    
    
    game:GetService("TeleportService").CustomizedTeleportUI = true
    

## 显示自定义 GUI

在传送玩家时显示 GUI 也非常简单。只需将想要的 GUI 移动到玩家的 `PlayerGui` 中，或者事先将那里的 GUI 隐藏，然后使用 `GuiObject/Visible` 将其显示出来即可。你可以随意加入任何你想要的效果。例如，单击传送按钮时，此代码将在纯黑屏幕中淡入：
    
    
    button.MouseButton1Click:connect(function()
    	-- 触发 RemoteEvent
    	game:GetService("TeleportService"):Teleport(otherPlaceId)
    	
    	-- 将读取页面可视化
    	loadingScreen.Visible = true
    	
    	-- 淡入屏幕
    	for i = 1, 0, -.05 do
    		loadingScreen.BackgroundTransparency = i
    		wait()
    	end
    	loadingScreen.BackgroundTransparency = 0
    end)
    

## 传送后显示自定义 GUI

你可以通过将 LocalScripts 和 GUI 元素放在 ReplicatedFirst 中来创建自定义加载屏幕，如 `Articles/自定义加载屏幕` 中所示。但是，当游戏通过传送加载时，会出现一个小窗口，其中会显示默认的 Roblox 加载屏幕。为了填补这一空白，TeleportService 中的所有传送功能都允许使用 `ScreenGui` 作为可选参数，该参数将在传送后立即显示。
    
    
    local loadingScreen = Instance.new(**ScreenGui**, player.PlayerGui)
    local loadingScreenFrame = Instance.new(**Frame**, loadingScreen)
    loadingScreenFrame.Name = **loadingScreenFrame**
    loadingScreenFrame.BackgroundColor3 = Color3.new(0,0,0)
    loadingScreenFrame.Size = UDim2.new(1,0,1,50)
    loadingScreenFrame.Position = UDim2.new(0,0,0,-50)
    loadingScreenFrame.Visible = false
    
    TeleportService:Teleport(otherPlaceId, player, nil, loadingScreen)
    

上面的代码将创建一个黑屏，然后将其与传送调用一起传递。当新游戏加载时，将自动为该玩家显示黑屏。

## 简单示例

尽管没有有关如何管理你的传送的指导原则，但建议采取以下几个措施。如果要显示全屏图像，则可能需要隐藏核心 GUI。根据你的游戏，你可能还想使用诸如 `ForceField` 之类的方法来保护玩家免受伤害。最后，无论你是否使用自定义 GUI 进行传送，请做好准备处理无法传送的情况！这种情况不会经常发生，但是一定要小心。

Creating Custom Teleport GUI Code Sample 1 ```    
    
    -- LocalScript for Lobby place
    
    -- Declare local variables for Roblox Services
    local TeleportService = game:GetService('TeleportService')
    local UserInputService = game:GetService('UserInputService')
    local StarterGui = game.StarterGui
    
    -- Declare local variables
    local player = game.Players.LocalPlayer
    local otherPlaceId = 277345328
    local forceField = Instance.new('ForceField')
    local teleportButton = script.Parent
    
    -- Create loading screen to fade in and pass with teleport function
    local loadingScreen = Instance.new('ScreenGui', player.PlayerGui)
    local loadingScreenFrame = Instance.new('Frame', loadingScreen)
    loadingScreenFrame.Name = 'loadingScreenFrame'
    loadingScreenFrame.BackgroundColor3 = Color3.new(0,0,0)
    loadingScreenFrame.Size = UDim2.new(1,0,1,50)
    loadingScreenFrame.Position = UDim2.new(0,0,0,-50)
    loadingScreenFrame.Visible = false
    
    -- Hide default teleport GUI elements
    TeleportService.CustomizedTeleportUI = true
    
    -- Bind function to OnTeleport in case teleport fails
    player.OnTeleport:Connect(function(teleportState)
    	if teleportState == Enum.TeleportState.Failed then
    		-- Disable force field
    		forceField.Parent = nil
    		
    		-- Hide teleport GUI and show teleport button
    		loadingScreenFrame.BackgroundTransparency = 1
    		loadingScreenFrame.Visible = false
    		teleportButton.Visible = true
    		
    		-- Show Core GUI elements and mouse cursor
    		StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.All, true)
    		UserInputService.MouseIconEnabled = true		
    	end
    end)
    
    -- Bind function to GUI button
    teleportButton.MouseButton1Click:Connect(function()
    	-- Hide button, Core GUI, and mouse
    	teleportButton.Visible = false
    	StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.All, false)	
    	UserInputService.MouseIconEnabled = false	
    	
    	-- Activate force field to protect player during teleport
    	forceField.Parent = player.Character	
    		
    	-- Show loading screen and fade it in
    	loadingScreenFrame.Visible = true
    	for i = 1, 0, -.05 do
    		loadingScreenFrame.BackgroundTransparency = i
    		wait()
    	end
    	loadingScreenFrame.BackgroundTransparency = 0
    	
    	-- Teleport player and pass the loading screen
    	TeleportService:Teleport(otherPlaceId, player, nil, loadingScreen)
    end)
    
    
    0

```
Creating Custom Teleport GUI Code Sample 2 ```    
    
    -- Local script in other place
    
    -- Declare local variables for Roblox Services
    local TeleportService = game:GetService('TeleportService')
    local UserInputService = game:GetService('UserInputService')
    local StarterGui = game.StarterGui
    
    -- Hide Core GUI and mouse
    StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.All, false)	
    UserInputService.MouseIconEnabled = false	
    
    -- Bind function to teleport arrival
    TeleportService.LocalPlayerArrivedFromTeleport:Connect(function(loadingGui, data)
    	-- Pause briefly to allow level to load	
    	wait(2)	
    	
    	-- Fade out loading screen
    	for i = 0, 1, .05 do
    		loadingGui.loadingScreenFrame.BackgroundTransparency = i
    		wait()
    	end
    	loadingGui.loadingScreenFrame.BackgroundTransparency = 1
    	
    	-- Show Core GUI and mouse
    	game.StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.All, true)
    	UserInputService.MouseIconEnabled = true	
    end)
    
    
    0

```


***__Roblox官方链接__:[创建自定义传送屏幕](https://developer.roblox.com/zh-cn/articles/Creating-a-Custom-Teleport-GUI)