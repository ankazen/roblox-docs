# 创建 VIP 专用门 
Time:<em>10  分钟</em>

**警告：**Roblox 将有效地禁止将所有衬衫称为“管理员”衬衫，因为其名称具有误导性。请不要将你的衬衫命名为**管理员衬衫**，应将它们命名为 VIP 衬衫之类的名称。 

受限制的门，通常也称为 VIP 门，用来限制只有特定用户才能进入某一特定区域。一个受限制的门可能要应用许多限制，本文不能涵盖所有限制。但是，将涵盖最常用的限制：

  * 限制某个玩家。
  * 限制某个群组。
  * 限制场景的创建者。

但是，在制作限制进入特定区域的受限制的门之前，你应该始终仔细考虑。在大多数情况下，会有更好的方法。问题在于受限制的门经常被过度使用。有时，它们用于保护包含某些物品的房间。但是，这些物品可以自动提供给玩家，而不必每次死亡时都进入房间。如果可以采用更清洁的方式，请尽量避免使用受限制的门。

### 建造门

![Door.png](https://developer.roblox.com/assets/blta737fca1f558f29a/Door.png)



建造门应该不是问题，但是我仍然要描述一下。首先，你需要创建门。通常，你希望它的大小与角色大小相同，以便玩家可以通过。你可能希望门也要锚固，除非你希望每当玩家触碰门时门就会移动…

玩家角色的大小为 4 x 5 x 1，因此你可能希望门也有这样的尺寸。另一个解决方案是只是让门稍大于角色的实际大小。通常，你还希望在门周围建造一个房间，但这超出了本教程的范围。

### 编写门的脚本

#### 结构

首先，我们需要在门中创建一个脚本。将鼠标悬停在管理器中的门部件上，然后单击加号图标 ![](https://developer.roblox.com/assets/blt82bf8ce3b7caad67/Explorer-Plus-Icon.png)

，然后单击 `Script`。

![Insert Script](https://developer.roblox.com/assets/blt569463ecf72aee15/New-Script-2.png)



因为在脚本中会对门进行很多操作，所以最好定义一个包含对它的引用的变量。该脚本将调用变量 door，但你可以随意调用。
    
    
    local door = script.Parent
    

你可能想打开和关上门。我们做一个开门的函数，再做一个关门的函数。

有很多方法可以打开门，但是，对于本教程，我们将选择一种使门逐渐消失的方法，正如你在此处所见：

![Animated Fading Door.gif](https://developer.roblox.com/assets/blt38e99998e35a1d35/Animated_Fading_Door.gif)

别担心，你的门会消失得比这还要快。此处的动画比你的门实际消失的速度要慢。

我们将使用循环使门消失，并使用它的 `BasePart/Transparency` 属性来更改它的不透明度。最后，我们将更改门的 `BasePart/CanCollide` 属性，以允许玩家通过它。
    
    
    local doorOpen = false
    
    local function open()
    	if doorOpen then 
    		-- 门已打开，无需再次打开！
    		return 
    	end 
    
    	doorOpen = true
    	door.CanCollide = false -- Make players able to walk through the door.
     
    	for transparency = 0, 1, 0.1 do
    		door.Transparency = transparency
    		wait(.1)
    	end
    end
    

如果有一个开门的函数，当然也得有一个关门的函数。关门函数的作用与开门函数的作用正好相反！
    
    
    local function close()
    	for transparency = 1, 0, -0.1 do
    		door.Transparency = transparency
    		wait(.1)
    	end
     	
    	doorOpen = false
    	door.CanCollide = true -- Make players unable to walk through the door.
    end
    

你可能希望门在被触碰时打开，因此应该使用 `BasePart/Touched` 事件。因此，让我们将 Touched 事件连接到某个函数。然后，我们将检查触碰门的部件是否在角色中。
    
    
    local function onTouched(hit)
    	local character = hit.Parent
    	if character then
    		local player = game.Players:GetPlayerFromCharacter(character)
    		if player and not doorOpen then
    			open()
    			wait(3)
    			close()
    		end
    	end
    end
    

现在，当门被触碰时，我们想做什么？我们要检查玩家是否符合其中一个限制！

#### 限制

有很多方法可以检查玩家是否符合其中一个限制，但在本例中，我们将使用一个简单的系统。但我们鼓励你尝试用其他的方法去做，因为这会帮助你学习。

我们将在本例中使用的系统很简单。我们将用 or 关键字分隔所有限制。所有的限制都将采用布尔表达式的形式。如果这些布尔表达式中的任何一个为 true，门都将打开。

让我们看看你可能要应用的一些常用限制。

##### 限制某个玩家

通常，你会想授权某些特定的玩家通过这扇门。在本例中，你可能会这样做。

你可能已经猜到了如何应用这个限制，但是，如果你没有猜到也没有关系，方法很简单。你只需检查玩家的名称是否等于某个字符串：
    
    
    player.Name == "PlayerName"
    

##### 限制某个群组

使用 `Player/IsInGroup` 可以很容易地检查玩家是否在某个群组中。

IsInGroup 方法接受一个参数，该参数是某个群组的 id。如果玩家在具有该 id 的群组中，该方法将返回 true。否则，将返回 false。

下面是应用此限制的示例（注意：你可以将 8 更改为任何群组的 _id_）：
    
    
    player:IsInGroup(127081)
    

##### 限制场景的创建者

只需将玩家的名字与某个预定义的名字（场景所有者的名字）进行比较，并检查它们是否相等即可实现这一限制。但是，这种方法很有用，因为它可以在任何场景中使用。例如，在将脚本提供给朋友之前，无需编辑脚本，因为该脚本会适应场景。该脚本使用 `DataModel/CreatorId` 并将其与玩家的 id 进行比较。如果它们相等，那么该玩家就是所有者。因此，它可以在任何场景中使用，甚至在给朋友时，都无需将其名字更改为朋友的名字。

下面是应用此限制的方法：
    
    
    game.CreatorId == player.UserId
    

##### 限制某个用户的朋友

如果你想让你所有的朋友都能通过那扇门呢？为此，请使用 `Player/IsFriendsWith`。它有一个参数，名为 userId，它是用户的 id。如果你希望允许创建者的所有朋友，可以将 game.CreatorId 作为参数发送到此方法。

此限制应用起来非常简单：
    
    
    player:IsFriendsWith(2032622)
    

#### 使用限制

现在，让我们在脚本中添加我们的限制！下面是一个示例，它只允许 [Roblox](https://www.roblox.com/groups/group.aspx?gid=7) 群组中的人通过：
    
    
    local door = script.Parent
    local doorOpen = false
    
    local function open()
    	doorOpen = true
    	door.CanCollide = false -- Make players able to walk through the door.
     
    	for transparency = 0, 1, 0.1 do
    		door.Transparency = transparency
    		wait(.1)
    	end
    end
    
    local function close()
    	for transparency = 1, 0, -0.1 do
    		door.Transparency = transparency
    		wait(.1)
    	end
     	
    	doorOpen = false
    	door.CanCollide = true -- Make players unable to walk through the door.
    end
    
    local function onTouched(hit)
    	local character = hit.Parent
    	if character then
    		local player = game.Players:GetPlayerFromCharacter(character)
    		if player then
    			if player:IsInGroup(7) then
    				-- 只在门处于关闭状态时打开。
    				if not doorOpen then
    					open()
    					wait(3)
    					close()
    				end
    			elseif doorOpen then
    				-- 有入侵者！可别让他们活着穿过这道门。
    				character:BreakJoints()
    			end
    		end
    	end
    end
    
    door.Touched:Connect(onTouched)
    
  *[id]: identifier



***__Roblox官方链接__:[创建 VIP 专用门](https://developer.roblox.com/zh-cn/articles/Creating-VIP-Doors)