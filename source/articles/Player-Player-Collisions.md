# 玩家间的碰撞控制 
Time:<em>10  分钟</em>

默认情况下，Roblox 游戏中的角色是可以互相碰撞的。角色间的互相碰撞可以用来形成十分有趣的游戏体验。举例来说，一名玩家可以利用此特性跳到另一名玩家的头上，从而到达单人游戏中无法到达的区域。但在另外一些游戏中，玩家间的碰撞反而会降低游戏体验，应当对其进行禁用。在本教程中，我们将学习如何在不妨碍玩家角色与游戏世界中其它对象碰撞的前提下，禁用角色间的互相碰撞。

当想要禁用玩家间互相碰撞时，首先需要为所有玩家角色创建一个`Articles/Collision Filtering|碰撞组` 。该碰撞组将会设置为不与自身碰撞。也就是说，虽然碰撞组内的部件仍然会与游戏世界中的其它部件（这些部件通常隶属于 Default（默认）碰撞组）相互碰撞，但当遇到同一碰撞组内的部件时，将会互相穿透而不进行碰撞。

创建碰撞组的第一步是为 PhysicsService 创建变量，并为这个玩家碰撞组进行命名。
    
    
    local PhysicsService = game:GetService("PhysicsService")
    local playerCollisionGroupName = "Players"
    

然后，我们将会通过 CreateCollisionGroup 创建碰撞组，并对其调用 CollisionGroupSetCollidable，以将其设为不会与自身碰撞。
    
    
    local PhysicsService = game:GetService("PhysicsService")
    local playerCollisionGroupName = "Players"
    PhysicsService:CreateCollisionGroup(playerCollisionGroupName)
    PhysicsService:CollisionGroupSetCollidable(playerCollisionGroupName, playerCollisionGroupName, false)
    

下面我们只需将玩家角色的部件全部加入此碰撞组即可。由于这些部件在游戏开始时可能尚未存在，可以通过设置部分事件来提醒我们有新的玩家角色生成，需要将其添加至碰撞组内。
    
    
    local PhysicsService = game:GetService("PhysicsService")
    local Players = game:GetService("Players")
    
    local playerCollisionGroupName = "Players"
    PhysicsService:CreateCollisionGroup(playerCollisionGroupName)
    PhysicsService:CollisionGroupSetCollidable(playerCollisionGroupName, playerCollisionGroupName, false)
    
    local function onCharacterAdded(character)
    end
    
    local function onPlayerAdded(player)
      player.CharacterAdded:Connect(onCharacterAdded)
    end
    
    Players.PlayerAdded:Connect(onPlayerAdded)
    

通过上面的代码，我们先将 `onPlayerAdded` 绑定到 `PlayerAdded`，然后将 `onCharacterAdded` 绑定到 `CharacterAdded`。在 onCharacterAdded 内，我们可以通过添加代码来将角色的部件添加到玩家碰撞组中。

需要注意的是，部分角色模型的结构可能会十分复杂，因此我们需要顾及的将不仅仅是循环遍历角色模型的子项。举例来说，玩家角色佩戴的饰品中也会存在子项部件。虽然这些部件的 `CanCollide` 值通常都是 false，为防万一，也必须将其添加到我们的碰撞组中去。

要遍历玩家角色中的部件，最简单的方法就是利用递归函数。这种函数会简单地以 `Instance` 进行传递。如果该 Instance 是一个 BasePart，我们就可以设置其碰撞组。接着，我们会查看该对象的所有子项（不管其是否为部件），并对每个子项都调用递归函数。

递归函数设置完毕后，我们就可以从 `onCharacterAdded` 中对其进行调用，并对角色模型本身调用该函数。
    
    
    local PhysicsService = game:GetService("PhysicsService")
    local Players = game:GetService("Players")
    
    local playerCollisionGroupName = "Players"
    PhysicsService:CreateCollisionGroup(playerCollisionGroupName)
    PhysicsService:CollisionGroupSetCollidable(playerCollisionGroupName, playerCollisionGroupName, false)
    
    local function setCollisionGroupRecursive(object)
      if object:IsA("BasePart") then
        PhysicsService:SetPartCollisionGroup(object, playerCollisionGroupName)
      end
      for _, child in ipairs(object:GetChildren()) do
        setCollisionGroupRecursive(child)
      end
    end
    
    local function onCharacterAdded(character)
      setCollisionGroupRecursive(character)
    end
    
    local function onPlayerAdded(player)
      player.CharacterAdded:Connect(onCharacterAdded)
    end
    
    Players.PlayerAdded:Connect(onPlayerAdded)
    

当玩家的角色在游戏中生成时，这个脚本将会遍历该角色中的所有部件，并将这些部件添加至玩家碰撞组中。如果该角色撞上其他角色，物理引擎就会发现其所有部件都属于同一组（已配置为不会与其本身碰撞），并让角色穿过彼此。

按照当前脚本内容，玩家角色在生成时所包含的任何部件都将经过 `setCollisionGroupRecursive()` 的处理。但需要注意的是，如果在触发 `onCharacterAdded()` 后角色身上又增添了任何额外部件（例如 Tool（工具）或自定义套装）时，这些新的部件暂时还不会属于与角色相同的碰撞组。为了解决这一状况，我们需要监听角色上的 `DescendantsAdded` 事件。

当玩家角色添加新的子项时，脚本应该能够正确检查出该对象是否为 BasePart，如是则将其添加至玩家碰撞组。要实现这一效果，最好的方式就是从 `setCollisionGroupRecursive` 中分割出另一个函数 `setCollisionGroup`，该函数只会以非递归的方式处理一个对象。
    
    
    local function setCollisionGroup(object)
      if object:IsA("BasePart") then
        PhysicsService:SetPartCollisionGroup(object, playerCollisionGroupName)
      end
    end
    
    local function setCollisionGroupRecursive(object)
      setCollisionGroup(object)
    
      for _, child in ipairs(object:GetChildren()) do
        setCollisionGroupRecursive(child)
      end
    end
    
    local function onCharacterAdded(character)
      setCollisionGroupRecursive(character)
    
      character.DescendantAdded:Connect(setCollisionGroup)
    end
    

我们所编写的脚本不仅需要处理玩家角色上所添加的新对象，也需要在对象被移除时进行相应操作。处理对象移除的最佳方式为对被移除对象所属的前一个碰撞组进行记录。因此，我们需要在对象最初被添加至玩家碰撞组时将对象前一个碰撞组的信息储存在 table（表）内。拥有此信息后，脚本将能够监听 DescendantsRemoving 事件，对被移除对象的碰撞组位置进行重置，也就是将其放回前一个碰撞组中了。
    
    
    local previousCollisionGroups = {}
    
    local function setCollisionGroup(object)
      if object:IsA("BasePart") then
        previousCollisionGroups[object] = object.CollisionGroupId
        PhysicsService:SetPartCollisionGroup(object, playerCollisionGroupName)
      end
    end
    
    local function setCollisionGroupRecursive(object)
      setCollisionGroup(object)
    
      for _, child in ipairs(object:GetChildren()) do
        setCollisionGroupRecursive(child)
      end
    end
    
    local function resetCollisionGroup(object)
      local previousCollisionGroupId = previousCollisionGroups[object]
      if not previousCollisionGroupId then return end 
    
      local previousCollisionGroupName = PhysicsService:GetCollisionGroupName(previousCollisionGroupId)
      if not previousCollisionGroupName then return end
    
      PhysicsService:SetPartCollisionGroup(object, previousCollisionGroupName)
      previousCollisionGroups[object] = nil
    end
    
    local function onCharacterAdded(character)
      setCollisionGroupRecursive(character)
    
      character.DescendantAdded:Connect(setCollisionGroup)
      character.DescendantRemoving:Connect(resetCollisionGroup)
    end
    

在此脚本的作用下，当玩家角色生成时，该角色内的所有部件都会与其在上一碰撞组中的 Id 一起添加到表格当中。被移除的部件将会被重新分配至其旧碰撞组中。同样，所有新添加的部件也都会以同样的方式来分配和取消分配。

本示例的完整脚本如下：
    
    
    local PhysicsService = game:GetService("PhysicsService")
    local Players = game:GetService("Players")
    
    local playerCollisionGroupName = "Players"
    PhysicsService:CreateCollisionGroup(playerCollisionGroupName)
    PhysicsService:CollisionGroupSetCollidable(playerCollisionGroupName, playerCollisionGroupName, false)
    
    local previousCollisionGroups = {}
    
    local function setCollisionGroup(object)
      if object:IsA("BasePart") then
        previousCollisionGroups[object] = object.CollisionGroupId
        PhysicsService:SetPartCollisionGroup(object, playerCollisionGroupName)
      end
    end
    
    local function setCollisionGroupRecursive(object)
      setCollisionGroup(object)
    
      for _, child in ipairs(object:GetChildren()) do
        setCollisionGroupRecursive(child)
      end
    end
    
    local function resetCollisionGroup(object)
      local previousCollisionGroupId = previousCollisionGroups[object]
      if not previousCollisionGroupId then return end 
    
      local previousCollisionGroupName = PhysicsService:GetCollisionGroupName(previousCollisionGroupId)
      if not previousCollisionGroupName then return end
    
      PhysicsService:SetPartCollisionGroup(object, previousCollisionGroupName)
      previousCollisionGroups[object] = nil
    end
    
    local function onCharacterAdded(character)
      setCollisionGroupRecursive(character)
    
      character.DescendantAdded:Connect(setCollisionGroup)
      character.DescendantRemoving:Connect(resetCollisionGroup)
    end
    
    local function onPlayerAdded(player)
      player.CharacterAdded:Connect(onCharacterAdded)
    end
    
    Players.PlayerAdded:Connect(onPlayerAdded)
    



***__Roblox官方链接__:[玩家间的碰撞控制](https://developer.roblox.com/zh-cn/articles/Player-Player-Collisions)