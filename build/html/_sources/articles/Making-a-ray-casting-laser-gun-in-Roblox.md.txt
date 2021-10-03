# 射线投射：创建激光枪 
Time:<em>10  分钟</em>

Roblox 中的射线投射功能可用于检测某个部件是否与某条线段相交。本教程介绍如何使用射线投射功能创建激光枪。

### 教程

#### 设置

![PaintballGunInToolbox.png](https://developer.roblox.com/assets/blt2696396188d4757e/PaintballGunInToolbox.png)



要创建激光枪，玩家需要手握一个工具。请前往工具箱，选择 **Roblox Sets** （Roblox 集合），然后选择 _Weapons_ （武器）集合。单击彩弹枪，并在系统提示时将它放入 StarterPack 中。打开 StarterPack 并移除名为 Handle 的部件之外的所有内容。然后，将 `LocalScript` 插入工具。请确保它不是 `Script`，否则当你在线开始游戏时，该函数将不起作用！可以随意对该工具进行重命名，但不要更改部件名称！

#### 框架

既然我们已经完成设置，现在该开始对我们的枪进行脚本处理了。我们先从一些变量开始：
    
    
    local tool = script.Parent
    local player = game:GetService("Players").LocalPlayer
    

`tool` 变量用于引用工具，`player` 变量用于引用使用这把枪的玩家。现在，我们执行一些操作，通过连接至工具的 `Tool/Equipped` 事件来装备工具：
    
    
    local tool = script.Parent
    local player = game:GetService("Players").LocalPlayer
    
    tool.Equipped:connect(function(mouse)
    	print("Tool equipped!")
    end)
    

现在，每当工具装备完毕，它就可以将 Tool equipped! 打印至“Output（输出）”窗口。你可能会注意到该函数的鼠标参数；即可用于响应玩家鼠标单击操作的 `Mouse` 对象。连接至鼠标的 `Mouse/Button1Down` 事件，如下所示：
    
    
    local tool = script.Parent
    local player = game:GetService("Players").LocalPlayer
    
    tool.Equipped:connect(function(mouse)
    	print("Tool equipped!")
    	
    	mouse.Button1Down:connect(function()
    		print("Mouse pressed!")
    	end)
    end)
    

现在，当你单击你的鼠标时，Mouse pressed! 将被打印至输出窗口。快试试吧！开始游戏、装备工具并按下几次鼠标，你应该会看到如下内容：
    
    
    Mouse pressed!
    Mouse pressed!
    Mouse pressed!
    Tool equipped!
    Mouse pressed!
    

#### 射线投射

既然我们已经完成框架设置，接下来我们开始投射射线。将此射线添加到鼠标下移函数：
    
    
    local ray = Ray.new(tool.Handle.CFrame.p, (mouse.Hit.p - toolHandle.CFrame.p).unit * 300)
    

这将创建从工具手柄中央开始射出的射线 (`tool.Handle.CFrame.p`)，并朝鼠标的位置射出 300 格 (`(mouse.Hit.p - tool.Handle.CFrame.p).unit * 300`)。但是就其自身而言，此操作不会检测是否有部件挡住射线，所以我们需要使用 `Workspace` 的 `Workspace/FindPartOnRay` 方法。FindPartOnRay 包含四个参数：检查部件时所用的射线、要忽略的对象、是否将所有地形单元格视为完整的立方体，以及是否忽略水。由于这是激光，我们希望忽略水，也希望玩家不要朝自己开枪，因此我们希望像下面这样调用激光：
    
    
    local part, position = workspace:FindPartOnRay(ray, player.Character, false, true)
    

`part` 是指被击中的部件（或是 type|nil，如果没有部件挡道），`position` 是指射线击中部件的位置。让我们将此射线添加到函数中吧。在 Button1Down 连接中，添加之前的线。你的脚本现在应该如下所示：
    
    
    local tool = script.Parent
    local player = game:GetService("Players").LocalPlayer
    
    tool.Equipped:connect(function(mouse)
    	print("Tool equipped!")
    	
    	mouse.Button1Down:connect(function()
    		print("Mouse pressed!")
    		local ray = Ray.new(tool.Handle.CFrame.p, (mouse.Hit.p - tool.Handle.CFrame.p).unit * 300)
    		local part, position = workspace:FindPartOnRay(ray, player.Character, false, true)
    	end)
    end)
    

完成该操作后，你就可以创建激光束了！

#### 创建激光束

能够看到挡住鼠标的对象后，我们可以在射线的起点（工具手柄中央）与射线击中的位置之间创建激光束。现在我们按如下所示创建激光束：

![RaycastingGunBeamExample.png](https://developer.roblox.com/assets/blt63cfa1ad4a7f75b9/RaycastingGunBeamExample.png)



要开始创建激光束，我们需要在 Button1Down 连接中创建一个部件，如下所示：
    
    
    local beam = Instance.new("Part", workspace)
    

但是此部件只是青砖，不是光束。要使其与我们的示例类似，需要执行以下几项操作：

  * 需要将其 `BasePart/BrickColor` 属性设置为“Bright red（亮红色）”。
  * 需要将其 `FormFactorPart/FormFactor` 属性设置为“Custom（自定义）”
  * 需要将其 `BasePart/Material` 属性设置为“Neon（氖气）”
  * 需要将其 `BasePart/Transparency` 属性设置为 0.25
  * 需要将其 `BasePart/Anchored` 和 `BasePart/Locked` 属性设置为 true，并将 `BasePart/CanCollide` 属性设置为 false。

让我们执行这些操作吧！创建部件后，设置激光束的属性：
    
    
    beam.BrickColor = BrickColor.new("Bright red")
    beam.FormFactor = "Custom"
    beam.Material = "Neon"
    beam.Transparency = 0.25
    beam.Anchored = true
    beam.Locked = true
    beam.CanCollide = false
    

但是，如果将此激光束放在工作区中，它看起来就像一块红砖。我们需要修改其 `BasePart/Size` 和 `BasePart/CFrame` 属性，以便激光束在手柄和击中点之间延伸。为此，请使用以下脚本:
    
    
    local distance = (tool.Handle.CFrame.p - position).magnitude
    beam.Size = Vector3.new(0.3, 0.3, distance)
    beam.CFrame = CFrame.new(tool.Handle.CFrame.p, position) * CFrame.new(0, 0, -distance / 2)
    

现在，激光枪可以正常使用 - 它会射出可击中部件的射线光束。你甚至可以朝天空发射，它会在天上射出光束（即使天空中没有部件）。但是存在一个问题：光束无法移除。要移除光束，我们应使用 `Debris` 服务的 `Debris/AddItem` 方法。请将此方法添加到 Button1Down 连接的底部：
    
    
    game:GetService("Debris"):AddItem(beam, 0.1)
    

这意味着，在光束后添加了 0.1 (1/10) 秒，光束将被移除。你的脚本现在应如下所示：
    
    
    local tool = script.Parent
    local player = game:GetService("Players").LocalPlayer
    
    tool.Equipped:connect(function(mouse)
    	print("Tool equipped!")
    	
    	mouse.Button1Down:connect(function()
    		print("Mouse pressed!")
    		local ray = Ray.new(tool.Handle.CFrame.p, (mouse.Hit.p - tool.Handle.CFrame.p).unit * 300)
    		local part, position = workspace:FindPartOnRay(ray, player.Character, false, true)
    		
    		local beam = Instance.new("Part", workspace)
    		beam.BrickColor = BrickColor.new("Bright red")
    		beam.FormFactor = "Custom"
    		beam.Material = "Neon"
    		beam.Transparency = 0.25
    		beam.Anchored = true
    		beam.Locked = true
    		beam.CanCollide = false
    		
    		local distance = (tool.Handle.CFrame.p - position).magnitude
    		beam.Size = Vector3.new(0.3, 0.3, distance)
    		beam.CFrame = CFrame.new(tool.Handle.CFrame.p, position) * CFrame.new(0, 0, -distance / 2)
    		
    		game:GetService("Debris"):AddItem(beam, 0.1)
    	end)
    end)
    

#### 伤害对象

画出光束后，现在需要使其伤害玩家和其他具有 `Humanoid` 对象的部位。首先，我们需要在创建光束后使用 if 语句，以检查部件是否存在：
    
    
    if part then
    end
    

有时，部位不存在，射线就找不到它，因此 `part` 将为零。我们需要将这种情况考虑在内，以免脚本出错。完成这些操作后，我们应查看两个位置以查找对象的人形：部位的父项（以防击中手臂或腿）和部位父项的父项（以防击中帽子或工具）。要查找该人形，请使用以下脚本：
    
    
    if part then
    	local humanoid = part.Parent:FindFirstChild("Humanoid")
    
    	if not humanoid then
    		humanoid = part.Parent.Parent:FindFirstChild("Humanoid")
    	end
    end
    

首先，我们检查部位的父项。如果未找到，则查看部位父项的父项。但愿我们能找到人形，但有时找不到，因此在尝试伤害它之前，我们需要确保存在人形。请将你的 if 语句更改为如下所示：
    
    
    if part then
    	local humanoid = part.Parent:FindFirstChild("Humanoid")
    	
    	if not humanoid then
    		humanoid = part.Parent.Parent:FindFirstChild("Humanoid")
    	end
    	
    	if humanoid then
    		humanoid:TakeDamage(30)
    	end
    end
    

现在我们将进行检查，以确保存在人形，然后使用 `Humanoid/TakeDamage` 方法对它造成 30 点伤害。TakeDamage 无法伤害受 `ForceField` 保护的人形。你的脚本现在应如下所示：
    
    
    local tool = script.Parent
    local player = game:GetService("Players").LocalPlayer
    
    tool.Equipped:connect(function(mouse)
    	print("Tool equipped!")
    	
    	mouse.Button1Down:connect(function()
    		print("Mouse pressed!")
    		local ray = Ray.new(tool.Handle.CFrame.p, (mouse.Hit.p - tool.Handle.CFrame.p).unit * 300)
    		local part, position = workspace:FindPartOnRay(ray, player.Character, false, true)
    		
    		local beam = Instance.new("Part", workspace)
    		beam.BrickColor = BrickColor.new("Bright red")
    		beam.FormFactor = "Custom"
    		beam.Material = "Neon"
    		beam.Transparency = 0.25
    		beam.Anchored = true
    		beam.Locked = true
    		beam.CanCollide = false
    		
    		local distance = (tool.Handle.CFrame.p - position).magnitude
    		beam.Size = Vector3.new(0.3, 0.3, distance)
    		beam.CFrame = CFrame.new(tool.Handle.CFrame.p, position) * CFrame.new(0, 0, -distance / 2)
    		
    		game:GetService("Debris"):AddItem(beam, 0.1)
    		
    		if part then
    			local humanoid = part.Parent:FindFirstChild("Humanoid")
    			
    			if not humanoid then
    				humanoid = part.Parent.Parent:FindFirstChild("Humanoid")
    			end
    			
    			if humanoid then
    				humanoid:TakeDamage(30)
    			end
    		end
    	end)
    end)
    

所有操作均已完成！尽情享受你的新激光枪吧！

### 最终产品

![RaycastingGunFinished.png](https://developer.roblox.com/assets/bltc5f175680683c96f/RaycastingGunFinished.png)



制作一把射线投射激光枪 ```    
    
    local tool = script.Parent
    local player = game:GetService("Players").LocalPlayer
     
    tool.Equipped:Connect(function(mouse)
    	print("Tool equipped!")
     
    	mouse.Button1Down:Connect(function()
    		print("Mouse pressed!")
    		local ray = Ray.new(tool.Handle.CFrame.p, (mouse.Hit.p - tool.Handle.CFrame.p).unit * 300)
    		local part, position = workspace:FindPartOnRay(ray, player.Character, false, true)
     
    		local beam = Instance.new("Part", workspace)
    		beam.BrickColor = BrickColor.new("Bright red")
    		beam.FormFactor = "Custom"
    		beam.Material = "Neon"
    		beam.Transparency = 0.25
    		beam.Anchored = true
    		beam.Locked = true
    		beam.CanCollide = false
     
    		local distance = (tool.Handle.CFrame.p - position).magnitude
    		beam.Size = Vector3.new(0.3, 0.3, distance)
    		beam.CFrame = CFrame.new(tool.Handle.CFrame.p, position) * CFrame.new(0, 0, -distance / 2)
     
    		game:GetService("Debris"):AddItem(beam, 0.1)
     
    		if part then
    			local humanoid = part.Parent:FindFirstChild("Humanoid")
     
    			if not humanoid then
    				humanoid = part.Parent.Parent:FindFirstChild("Humanoid")
    			end
     
    			if humanoid then
    				humanoid:TakeDamage(30)
    			end
    		end
    	end)
    end)


```


***__Roblox官方链接__:[射线投射：创建激光枪](https://developer.roblox.com/zh-cn/articles/Making-a-ray-casting-laser-gun-in-Roblox)