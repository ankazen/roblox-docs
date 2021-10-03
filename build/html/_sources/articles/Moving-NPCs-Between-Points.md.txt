# 在点之间移动 NPC 
Time:<em>10  分钟</em>

NPC（即**非玩家角色**）能够增加一款游戏的深度。NPC 可以是供玩家打击的敌人、玩家可以对话和互动的各色角色等等。

有些时候，NPC 可能站在某一个场景中，就像是在小型游戏内商店工作的店员一样。在另一些情况下，如果 NPC 四处走动，即便是在两个或多个点进行基本的移动，看起来就不会太像机器人（而更像是真人）。

请注意，本文讨论的是在游戏世界中两点间进行的直接直线运动。如果你需要让某个 NPC 沿着更加复杂的的路线移动或是绕过障碍，请参阅`Articles/Pathfinding|寻路`指南。 

## 向某一点移动

让 NPC 移动的其中一种简便方法，就是使用 `Humanoid` 对象，这是一种特殊的对象，能让某一 `Model|model` 获得角色的功能，即便其看起来并不像是真人。这能让该模型实实在在地在场景中移动，并与场景中的对象进行交互。

以这只僵尸为例。僵尸都不大聪明，所以我们可以让它走直线，不用担心中途会有什么障碍。

![](https://developer.roblox.com/assets/bltb886c30a94c8f5c5/Zombie-Direct-Path.jpg)

为方便起见，游戏中绿色的旗子模型已命名为 _GreenFlag_。我们会用其来作为僵尸前进的第一个目的地。请分析以下示例：

```    
    
    -- Variables for the zombie and its humanoid
    local zombie = game.Workspace.Zombie
    local humanoid = zombie.Humanoid
     
    -- Variables for the point(s) the zombie should move between
    local pointA = game.Workspace.GreenFlag
    
    -- Move the zombie to the primary part of the green flag model
    humanoid:MoveTo(pointA.PrimaryPart.Position)


```
在这段基本代码当中，我们在工作区内找到 **Zombie** 模型、获取其 `Humanoid` 对象、将绿色旗子设为目标点，然后让僵尸使用 `Humanoid/MoveTo|MoveTo()` 方法向其走去。

Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link]() to the video instead. 

## 向多个点移动

让 NPC 朝一个点移动固然很精彩，但是让其在一系列点之间移动又怎么样呢？你可以连续编写一串 `Humanoid/MoveTo|MoveTo()` 和 `wait()` 命令，但代码也会十分冗长繁琐。

更出色的解决办法，就是使用 `Humanoid/MoveToFinished|MoveToFinished` 事件。这种事件能让你在完成 `Humanoid/MoveTo|MoveTo()` 动作，且 NPC 到达其目标点前暂停某一脚本。然后，你就可以继续运行该脚本，让 NPC 继续向另一点移动，或是返回其原点。

![](https://developer.roblox.com/assets/bltf4a57ceedb11d465/Zombie-Direct-Path-2.jpg)

在以下代码中，我们会为紫色旗子创建另一个变量 `pointB`。在送僵尸走向绿色旗子后，我们会立即暂停脚本。一旦僵尸到达该旗子，脚本就会继续，我们就会送僵尸朝紫色旗子移动。

```    
    
    -- Variables for the zombie and its humanoid
    local zombie = game.Workspace.Zombie
    local humanoid = zombie.Humanoid
    
    -- Variables for the point(s) the zombie should move between
    local pointA = game.Workspace.GreenFlag
    local pointB = game.Workspace.PurpleFlag
    
    -- Move the zombie to the primary part of the green flag model
    humanoid:MoveTo(pointA.PrimaryPart.Position)
    
    -- Wait until the zombie has reached its first target
    humanoid.MoveToFinished:Wait()
    
    -- Move the zombie to the primary part of the purple flag model
    humanoid:MoveTo(pointB.PrimaryPart.Position)


```
Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link]() to the video instead. 

如配合事件使用，当事件发生时，大多数代码都会用 `DataType/RBXScriptSignal|Connect` 来调用自定义函数。在本示例中，我们只需**暂停**脚本，直到触发 `Humanoid/MoveToFinished|MoveToFinished` 事件，这就是事件的 `Wait()` 方法的具体作用！ 

## 在多个点间往返

既然僵尸已经能够在两个旗子间移动了，让我们通过添加以下内容来完成这一脚本：

  1. 让僵尸不断在旗子之间来回往复巡逻的循环；
  2. 可自定义的“巡逻延迟”，能让僵尸在向下一个点移动前短时间暂停。

```    
    
    -- Set patrol delay at 2 seconds
    local PATROL_DELAY = 2
    
    -- Variables for the zombie and its humanoid
    local zombie = game.Workspace.Zombie
    local humanoid = zombie.Humanoid
    
    -- Variables for the point(s) the zombie should move between
    local pointA = game.Workspace.GreenFlag
    local pointB = game.Workspace.PurpleFlag
    
    -- Variable to keep track of the zombie's next destination
    local nextDestinationObject = pointA
    
    -- Loop to move between the two points
    while wait(PATROL_DELAY) do
    	-- Move the zombie to the next destination
    	humanoid:MoveTo(nextDestinationObject.PrimaryPart.Position)
    
    	-- Wait until the zombie has reached its target
    	humanoid.MoveToFinished:Wait()
    
    	-- Switch the current target to the other target
    	if nextDestinationObject == pointA then
    		nextDestinationObject = pointB
    	else
    		nextDestinationObject = pointA
    	end
    end


```
就是这样！现在僵尸可以在两个旗子之间巡逻了，并且每次都会停下来休息 2 秒。

Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link]() to the video instead. 

* * *

下一步怎么走？如我们所见，在多个点之间直线移动十分简单，但也同样很有局限性。如果路线上有任何障碍存在（墙、河、悬崖等），NPC 可能永远都无法到达目的地。僵尸的智商的确不高，但是其他 NPC 却应该有“更聪明”的行为方式，并会尝试找到通往目的地的**最优**路线。具体方法，请参考 `Articles/Pathfinding|寻路` 指南！



***__Roblox官方链接__:[在点之间移动 NPC](https://developer.roblox.com/zh-cn/articles/Moving-NPCs-Between-Points)