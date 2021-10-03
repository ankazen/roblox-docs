# 寻路 
Time:<em>15  分钟</em>

在 `Articles/Moving NPCs Between Points|在点之间移动 NPC` 教程当中，你学习了角色的直接直线移动。在本文中，我们将探讨如何让 NPC 沿着更加复杂的路线移动或是绕过障碍物。这叫做**寻路**。

## 设置

在 Roblox 当中，寻路是由 `PathfindingService` 驱动的，因此你的脚本必须先取得该服务，然后才能实现众多其他功能。

```    
    
    local PathfindingService = game:GetService("PathfindingService")


```
## 创建路径

在你的脚本当中加入 `PathfindingService` 后，你就能通过 `PathfindingService/CreatePath|CreatePath()` 方法创建一个新的 `Path`：

```    
    
    local PathfindingService = game:GetService("PathfindingService")
    
    local path = PathfindingService:CreatePath(pathParams)


```
### 路径参数

正如你所见，这一方法会接受一个参数 `pathParams`，这是一个 Lua 表格，能让你针对**行为主体**（将要沿路径移动的人形对象）的大小对路径进行微调。

以下是可供 `pathParams` 表格使用的参数：

键 值类型 默认值 描述

AgentRadius
整数
2
人形对象的半径。用于确定与障碍物的最小距离。

AgentHeight
整数
5
人形对象的高度。小于该值的空白空间（如台阶下的空间）都会标记为无法穿越。

请注意，参数的数量会随着时间推移而增加，包括哪些材质/区域更适合通过！ 

## 沿路径移动

让我们来将寻路付诸操作吧！下面僵尸的智商比`Articles/Moving NPCs Between Points|直线移动`教程中的僵尸还要高一点点，所以不应直接朝着粉色旗子的方向走进岩浆。我们来让它安全地走过木板。

![](https://developer.roblox.com/assets/blt0f3ac93c8b6083df/Zombie-Pathfinding-1.jpg)

以下代码会取得 `PathfindingService`、为僵尸及其 `Humanoid` 创建变量、设置目标点（粉色旗子），并创建 `Path` 对象。

```    
    
    local PathfindingService = game:GetService("PathfindingService")
    
    -- Variables for the zombie, its humanoid, and destination
    local zombie = game.Workspace.Zombie
    local humanoid = zombie.Humanoid
    local destination = game.Workspace.PinkFlag
    
    -- Create the path object
    local path = PathfindingService:CreatePath()


```
在本示例当中，我们不会向 `PathfindingService/CreatePath|CreatePath()` 传递满满一表格的自定义参数，因为行为对象（僵尸）是一个正常大小的角色，默认的半径/高度值都很适中。 

### 计算路线

用 `PathfindingService/CreatePath|CreatePath()` 创建完有效的 `Path` 对象后，你就需要**计算**路线了 — 这是一个**不会**在路径创建完毕后自动进行的显式步骤！

要计算路径，就要对 `Path` 对象调用 `Path/ComputeAsync|ComputeAsync()`，从而为起始位置和目标目的地提供一个 `Vector3`。

```    
    
    local PathfindingService = game:GetService("PathfindingService")
    
    -- Variables for the zombie, its humanoid, and destination
    local zombie = game.Workspace.Zombie
    local humanoid = zombie.Humanoid
    local destination = game.Workspace.PinkFlag
    
    -- Create the path object
    local path = PathfindingService:CreatePath()
    
    -- Compute the path
    path:ComputeAsync(zombie.HumanoidRootPart.Position, destination.PrimaryPart.Position)


```
### 获取路径的途经点

用 `Path/ComputeAsync|ComputeAsync()` 计算出 `Path` 后，其中会出现一系列**途经点**，循着这些点，角色就能沿路径前进。这些点会通过 `Path/GetWaypoints|GetWaypoints()` 函数来采集：

```    
    
    local PathfindingService = game:GetService("PathfindingService")
    
    -- Variables for the zombie, its humanoid, and destination
    local zombie = game.Workspace.Zombie
    local humanoid = zombie.Humanoid
    local destination = game.Workspace.PinkFlag
    
    -- Create the path object
    local path = PathfindingService:CreatePath()
    
    -- Compute the path
    path:ComputeAsync(zombie.HumanoidRootPart.Position, destination.PrimaryPart.Position)
    
    -- Get the path waypoints
    local waypoints = path:GetWaypoints()


```
### 显示途经点

保存途经点后，我们就能通过在其位置创建一个小部件来显示每个途经点：

```    
    
    -- Get the path waypoints
    local waypoints = path:GetWaypoints()
    
    -- Loop through waypoints
    for _, waypoint in pairs(waypoints) do
    	local part = Instance.new("Part")
    	part.Shape = "Ball"
    	part.Material = "Neon"
    	part.Size = Vector3.new(0.6, 0.6, 0.6)
    	part.Position = waypoint.Position
    	part.Anchored = true
    	part.CanCollide = false
    	part.Parent = game.Workspace
    end


```
![](https://developer.roblox.com/assets/blt9d4bd8a7eae40778/Zombie-Pathfinding-2.jpg)

如你所见，路径途经点会穿过木板一直延伸到粉色旗子！

### 路径移动

路径看起来没问题，那么我们来让僵尸沿着路径行走吧。最简单的方式就是从一个途经点到另一个途经点调用 `Humanoid/MoveTo|MoveTo()`。在这个脚本中，我们只需向同一个途经点循环添加两个命令：

```    
    
    -- Loop through waypoints
    for _, waypoint in pairs(waypoints) do
    	local part = Instance.new("Part")
    	part.Shape = "Ball"
    	part.Material = "Neon"
    	part.Size = Vector3.new(0.6, 0.6, 0.6)
    	part.Position = waypoint.Position
    	part.Anchored = true
    	part.CanCollide = false
    	part.Parent = game.Workspace
    
    	-- Move zombie to the next waypoint
    	humanoid:MoveTo(waypoint.Position)
    	-- Wait until zombie has reached the waypoint before continuing
    	humanoid.MoveToFinished:Wait()
    end


```
Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link]() to the video instead. 

## 处理堵塞的路径

很多 Roblox 的世界都是动态的 — 部件可能会移动或掉落、地板会塌陷等等。这可能会堵塞计算好的路径，并会阻碍 NPC 抵达其目的地。

要解决这一问题，你可以将 `Path/Blocked|Blocked` 事件与 `Path` 对象连接，然后重新计算绕过堵塞障碍的路线。请思考以下寻路脚本：

```    
    
    local PathfindingService = game:GetService("PathfindingService")
    
    -- Variables for the zombie, its humanoid, and destination
    local zombie = game.Workspace.Zombie
    local humanoid = zombie.Humanoid
    local destination = game.Workspace.PinkFlag
    
    -- Create the path object
    local path = PathfindingService:CreatePath()
    
    -- Variables to store waypoints table and zombie's current waypoint
    local waypoints
    local currentWaypointIndex
    
    local function followPath(destinationObject)
    	-- Compute and check the path
    	path:ComputeAsync(zombie.HumanoidRootPart.Position, destinationObject.PrimaryPart.Position)
    	-- Empty waypoints table after each new path computation
    	waypoints = {}
    
    	if path.Status == Enum.PathStatus.Success then
    		-- Get the path waypoints and start zombie walking
    		waypoints = path:GetWaypoints()
    		-- Move to first waypoint
    		currentWaypointIndex = 1
    		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
    	else
    		-- Error (path not found); stop humanoid
    		humanoid:MoveTo(zombie.HumanoidRootPart.Position)
    	end
    end
    
    local function onWaypointReached(reached)
    	if reached and currentWaypointIndex < #waypoints then
    		currentWaypointIndex = currentWaypointIndex + 1
    		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
    	end
    end
    
    local function onPathBlocked(blockedWaypointIndex)
    	-- Check if the obstacle is further down the path
    	if blockedWaypointIndex > currentWaypointIndex then
    		-- Call function to re-compute the path
    		followPath(destination)
    	end
    end
    
    -- Connect 'Blocked' event to the 'onPathBlocked' function
    path.Blocked:Connect(onPathBlocked)
    
    -- Connect 'MoveToFinished' event to the 'onWaypointReached' function
    humanoid.MoveToFinished:Connect(onWaypointReached)
    
    followPath(destination)


```
脚本中加入或更改了很多东西，那么我们来从头到尾看一下这段代码：

  1. 第一部分与先前类似：获取 `PathfindingService`、设置几种变量，然后创建 `Path` 对象。添加的主要内容就是 `waypoints` 和 `currentWaypointIndex` 两种变量。`waypoints` 会存储计算出的途经点，`currentWaypointIndex` 则会追踪僵尸到达的每个途经点的索引编号，编号从 **1** 开始，并随着僵尸沿路径行走而增加。

```    
    
    local PathfindingService = game:GetService("PathfindingService")
    
    -- Variables for the zombie, its humanoid, and destination
    local zombie = game.Workspace.Zombie
    local humanoid = zombie.Humanoid
    local destination = game.Workspace.PinkFlag
    
    -- Create the path object
    local path = PathfindingService:CreatePath()
    
    -- Variables to store waypoints table and zombie's current waypoint
    local waypoints
    local currentWaypointIndex


```
  2. 下一个函数 `followPath()` 包含我们之前使用过的多种命令，还在第 21 行加入了一个小错误检查功能。如果 `Path/ComputeAsync|path:ComputeAsync()` 成功，我们会获取途经点并将其存储在 `waypoints` 变量中。接着，我们要将 `currentWaypointIndex` 计数器设为 *_1_，并让僵尸移动到第一个途经点。

```    
    
    local function followPath(destinationObject)
    	-- Compute and check the path
    	path:ComputeAsync(zombie.HumanoidRootPart.Position, destinationObject.PrimaryPart.Position)
    	-- Empty waypoints table after each new path computation
    	waypoints = {}
    
    	if path.Status == Enum.PathStatus.Success then
    		-- Get the path waypoints and start zombie walking
    		waypoints = path:GetWaypoints()
    		-- Move to first waypoint
    		currentWaypointIndex = 1
    		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
    	else
    		-- Error (path not found); stop humanoid
    		humanoid:MoveTo(zombie.HumanoidRootPart.Position)
    	end
    end


```
  3. 路径可能堵塞的动态场景中，要遍历 `pairs()` 循环中所有的途经点是很成问题的。如果有任何物体堵塞了路径，则很难阻止/打破该循环。在该脚本中， `onWaypointReached()` 函数只有在僵尸到达下一个途经点后，才会让僵尸继续前进。

```    
    
    local function onWaypointReached(reached)
    	if reached and currentWaypointIndex < #waypoints then
    		currentWaypointIndex = currentWaypointIndex + 1
    		humanoid:MoveTo(waypoints[currentWaypointIndex].Position)
    	end
    end


```
  4. 最后一个函数 `onPathBlocked()` 会与第 49 行中的 `Path/Blocked|Blocked` 事件连接。如果路径遭到堵塞，该函数将会触发，且 `blockedWaypointIndex` 将会是被堵塞的途经点索引编号。

```    
    
    local function onPathBlocked(blockedWaypointIndex)
    	-- Check if the obstacle is further down the path
    	if blockedWaypointIndex > currentWaypointIndex then
    		-- Call function to re-compute the path
    		followPath(destination)
    	end
    end
    
    -- Connect 'Blocked' event to the 'onPathBlocked' function
    path.Blocked:Connect(onPathBlocked)


```
在第 42 行中，我们会检查堵塞的途经点索引是否**大于**当前的途经点索引。别忘了，路径的堵塞位置可能在僵尸的**身后**，但是这不代表应当停止检查。该检查能够确保只有当堵塞的途经点位于僵尸**前方**时，才会重新计算路径。 

请注意，`Path/Blocked|Blocked` 事件可能在路径生命周期内的任何时候触发。如果涉及移动障碍（比如在路径上滚动的巨石），事件还可能多次触发。正因如此，你可能需要 `Instance/Destroy|destroy` 路径，或是取消注册 `Path/Blocked|Blocked` 连接，直到路径计算完毕。 

* * *

正如你所见，`PathfindingService` 让你能够创建智商远超一般僵尸的 NPC。配合自定义行为对象参数和 `Path/Blocked|Blocked` 事件，你可以让任何 NPC 到达目的地，即使是在不断变化的动态场景当中！



***__Roblox官方链接__:[寻路](https://developer.roblox.com/zh-cn/articles/Pathfinding)