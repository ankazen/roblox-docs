# 网络所有权 
Time:<em>10  分钟</em>

Roblox 引擎会对游戏中所有未锚固的部件进行“物理特性模拟”。简单来说，这些部件将可以进行掉落、弹跳、漂浮在水中等动作。由于 Roblox 会对物理模拟进行自动处理，开发者将无需亲自编写物理引擎。

Roblox 游戏的运行`Articles/Roblox Client Server Model|会涉及多台电脑/装置`。为了分割计算物理特性的工作，Roblox 会自动将部件指派给服务器或客户端。一般来说，如果一个部件位于游戏内玩家角色的附近，其物理特性将交由该玩家使用的设备进行计算，而剩余部件将由服务器进行计算。在任一情况下，我们都会将计算该部件物理特性的服务器或客户端称之为其**所有者**。

由于物理特性的更新必须通过网络进行发送，从所有者进行物理特性改动到其他装置看到这些改动，这期间会有一点延迟。通常来说这种延迟并不明显，但若在延迟期间部件的所有权发生改变，则可能会出现问题。

## 示例1：投射物

在本示例中，我们将会探讨玩家 1 向玩家 2 投射物体对象时可能会出现的问题。

### 问题

随着物体在空中飞行并逐渐远离玩家 1，其所有权将会从玩家 1 移交给服务器。但当物体靠近玩家 2 时，其所有权又会从服务器移交给玩家 2。即使在网络连接质量良好的情况下，这个过程也可能会出现微小的延迟，从而导致物体所有权变更时的“跳跃”现象。

### 解决方案

利用 `BasePart/SetNetworkOwner|SetNetworkOwner()` 手动将该投射物的所有者设定为**服务器**。这样可以保证所有者**不会**变更，防止产生可见的“跳跃”现象。

以下代码会监听玩家的键盘输入并向服务器触发 `RemoteEvent`。此操作会创建一个投射物并设置其所有权。
    
    
     
    -- LocalScript（客户端） 
    game:GetService("ContextActionService"):BindAction("Throw", function(actionName, state, object)
    	if state == Enum.UserInputState.Begin then
    		game.ReplicatedStorage.RemoteEvent:FireServer()
    	end
    end, false, "h")
    
    
    
     
    -- Script（服务器） 
    game.ReplicatedStorage.RemoteEvent.OnServerEvent:Connect(function(player)
    	-- 获取玩家面向的方向
    	local direction = player.Character.Torso.CFrame.lookVector * 5
    
    	-- 创建投射物并向玩家面对的方向为其施加速度
    	local projectile = game.ServerStorage.Projectile:Clone()
    	projectile.Parent = game.Workspace
    	projectile:MakeJoints()
    	projectile.PrimaryPart.CFrame = CFrame.new(player.Character.Torso.Position + direction + Vector3.new(0,2,0))
    	projectile.PrimaryPart.Velocity = direction * 40 + Vector3.new(0,40,0)
    
    	-- 将服务器设为投射物的所有者
    	projectile.PrimaryPart:SetNetworkOwner(nil)
    end)
    

`BasePart/SetNetworkOwner|SetNetworkOwner()` 及其对应函数 `BasePart/GetNetworkOwner|GetNetworkOwner()` 必须在**服务器**端进行设置。这是因为客户端无法在 `LocalScript` 中更改所有权设定。 

## 示例2：车辆

在本示例中，我们将会探讨一辆拥有 `VehicleSeat` 驾驶席和 `Seat` 乘客席的车辆在搭乘两名玩家时可能出现的问题。

### 问题

在默认所有权规则下，如果一位玩家先坐进 `Seat`（乘客席），而另一位玩家随后坐进 `VehicleSeat`（驾驶席），则_乘客席上的玩家_会优先取得该车辆的物理所有权。在这种情况下，驾驶席上的玩家则需要等待数次网络数据交换才能获得其输入的响应。

### 解决方案

手动将车辆的网络所有权设置给驾驶员。当玩家坐下时，`VehicleSeat/Occupant` 会被设定为坐在上面的人形对象。开发者将可以监听座位的 `Instance/Changed` 事件。此时，该人形对象的父项应该是该玩家角色（除非人形对象为 NPC）。开发者可以利用这一点来决定获得车辆网络所有权的玩家。

当驾驶员离开座位时，空车的所有权将不再重要，因此可以将该车辆的网络所有权重新设置为自动（`BasePart/SetNetworkOwnershipAuto|SetNetworkOwnershipAuto()`）。
    
    
     
    -- VehicleSeat 中的脚本 
    local VehicleSeat = script.Parent
    
    VehicleSeat.Changed:Connect(function(prop)
    	if prop == "Occupant" then
    		local humanoid = VehicleSeat.Occupant
    		if humanoid then
    			local player = game:GetService("Players"):GetPlayerFromCharacter(humanoid.Parent)
    			if player then
    				VehicleSeat:SetNetworkOwner(player)
    			end
    		else
    			VehicleSeat:SetNetworkOwnershipAuto()
    		end
    	end
    end)
    

## 示例3：控制锁定

部分 Roblox 游戏拥有让玩家控制并非其角色模型对象的游戏机制。在默认情况下，应当受到玩家控制的对象会遵从自动网络所有权规则（其所有权将会为距离最近的玩家角色所有）。

### 问题

在某些情况下，操控此类对象的玩家可能并非离该对象最近的玩家角色。即使是这种情况下，操控对象的玩家仍应拥有其网络所有权，以便在操控时获得即时反馈。

举例来说，玩家可以通过按下键盘上的特定按键来控制地面上的球进行移动。若想获得即时反馈，此球型对象的 `BodyForce` 需要在 `LocalScript` 中通过键盘输入事件进行设置。但当其他玩家角色离球型对象过近时，就会获得对象的物理所有权，而控制玩家也就无法对其施加任何推力了。

### 解决方案

将球型对象的网络所有权指定给其控制玩家，以便 `LocalScript` 对推力的改动立即生效。
    
    
     
    -- LocalScript（客户端） 
    local Sphere = game.Workspace.Part
    local SphereForce = Sphere.BodyForce
    
    local ContextActionService = game:GetService("ContextActionService")
    
    local function pushBall(actionName, inputState, inputObject)
    	if inputState == Enum.UserInputState.End then
    		SphereForce.force = Vector3.new(0,0,0)
    	else
    		if actionName == "Left" then
    			SphereForce.force = Vector3.new(-100,0,0)
    		end
    		if actionName == "Right" then
    			SphereForce.force = Vector3.new(100,0,0)
    		end
    	end
    end
    
    ContextActionService:BindAction("Left", pushBall, false, "j")
    ContextActionService:BindAction("Right", pushBall, false, "l")
    
    
    
     
    -- Script（服务器） 
    game.Players.PlayerAdded:Connect(function(player)
    	game.Workspace.Part:SetNetworkOwner(player)
    end)
    

## 锚固部件

由于锚固部件不会进行物理模拟，其网络所有权也无法进行设置。在锚固的部件上调用 `BasePart/SetNetworkOwner|SetNetworkOwner()` 会导致脚本错误，但即使在这种情况下，锚固部件与网络所有权也不是毫无关系的。

为属于内部无锚固部件机构的集合设定所有权时，将会为整个机构中所有部件的所有权进行统一设置。如果该集合随后被锚固，则机构中未锚固的其他集合所有权将保持不变。解除之前集合的锚固后，会使其恢复先前设置的所有权。

如果集合是该机制中的唯一成员，则锚固该集合会使集合中所有部件的网络所有权重置为“自动”。此时再解除该集合的锚固时，集合所有权会遵从自动规则并忽略先前的所有权设置。



***__Roblox官方链接__:[网络所有权](https://developer.roblox.com/zh-cn/articles/Network-Ownership)