# Restricted/Team Doors 
Time:<em>articles/Collision Filtering|collision filtering</em>

In some games, it’s desirable to have doors or forcefields that certain players can pass through but others cannot. For instance, many team combat games will spawn players of each team in a safe area that other teams can’t access (so they aren’t attacked the moment they join or spawn).

There are various ways to accomplish this, but this tutorial utilizes `articles/Collision Filtering|collision filtering` to create doors that only certain players can pass through.

## Creating the Doors

For this simple example, the doors are basic block parts in the workspace named “BlueDoor” and “RedDoor.” Their material is `enum/Material|Glass` and their `BasePart/Transparency|Transparency` is set to 0.5.

![](https://developer.roblox.com/assets/bltceceb46774515d80/Team-Doors.jpg)

### Collision Groups

Since these doors exist in the game world at the start, we can set up their collision groups immediately. In `ServerScriptService`, create a `Script` and paste the following code into it:

Collision Filtering – Team Doors: Code Sample 2 ```    
    
    local PhysicsService = game:GetService("PhysicsService")
    
    local blueDoors = "BlueDoors"
    local redDoors = "RedDoors"
    
    -- Create door collision groups
    PhysicsService:CreateCollisionGroup(blueDoors)
    PhysicsService:CreateCollisionGroup(redDoors)
    
    -- Add doors to their proper collision group
    PhysicsService:SetPartCollisionGroup(workspace.BlueDoor, blueDoors)
    PhysicsService:SetPartCollisionGroup(workspace.RedDoor, redDoors)
    
    
    0

```
## Player Assignment

Now we need to add spawning players to an appropriate collision group. There are various ways to assign individual players to a group, including:

  * Assign players a “color” based on their `articles/Player Spawns and Teams|team` color.
  * Check if the player has earned a special `articles/Badges Special Game Awards|badge` or purchased a `articles/Game Passes One Time Purchases|game pass` which lets them access a restricted area.

For simplicity in this tutorial, we’ll just assign all incoming players to the “blue” team and give them access through the blue door, but not the red door.

### Collision Groups

As with the doors, let’s first set up player collision groups by adding these lines to the script:

Collision Filtering – Team Doors: Code Sample 3 ```    
    
    -- Add doors to their proper collision group
    PhysicsService:SetPartCollisionGroup(workspace.BlueDoor, blueDoors)
    PhysicsService:SetPartCollisionGroup(workspace.RedDoor, redDoors)
    
    local bluePlayers = "BluePlayers"
    local redPlayers = "RedPlayers"
    
    -- Create player collision groups
    PhysicsService:CreateCollisionGroup(bluePlayers)
    PhysicsService:CreateCollisionGroup(redPlayers)
    
    
    0

```
### Character Parts

When adding players to collision groups, it’s critical to remember that **all parts** of their character must be allowed to pass through the door — head, torso, arms, legs, feet, etc. We can do this with a function that finds all `BasePart` objects, the base class of both `Part|Parts` and `MeshPart|MeshParts` which make up the player’s avatar:

Collision Filtering – Team Doors: Code Sample 4 ```    
    
    -- Create player collision groups
    PhysicsService:CreateCollisionGroup(bluePlayers)
    PhysicsService:CreateCollisionGroup(redPlayers)
    
    local function setCollisionGroup(character, groupName)
    	for _, child in ipairs(character:GetChildren()) do
    		if child:IsA("BasePart") then
    			PhysicsService:SetPartCollisionGroup(child, groupName)
    		end
    	end
    	character.DescendantAdded:Connect(function(descendant)
    		if descendant:IsA("BasePart") then
    			PhysicsService:SetPartCollisionGroup(descendant, groupName)
    		end
    	end)
    end
    
    
    0

```
When characters spawn, their body parts are "assembled" over the course of about one second, so this function loops through the initial children **and** uses the `Instance/DescendantAdded|DescendantAdded` event to detect when other parts are added. This ensures that all character parts receive the correct collision group assignment. 

With this function in place, we can detect the `Players/PlayerAdded` event which then listens for the `Player/CharacterAdded|CharacterAdded` event and runs our `setCollisionGroup()` function with the `bluePlayers` collision group.

Collision Filtering – Team Doors: Code Sample 5 ```    
    
    local Players = game:GetService("Players")
    
    local function onPlayerAdded(player)
    	local function onCharacterAdded(character)
    		setCollisionGroup(character, bluePlayers)
    	end
    	player.CharacterAdded:Connect(onCharacterAdded)
    end
    Players.PlayerAdded:Connect(onPlayerAdded)
    
    
    0

```
## Collision Filtering

To finish up, we just need to define the collision groups that **don’t** collide with each other — specifically, blue players should not collide with blue doors, and red players should not collide with red doors.

```    
    
    local function onPlayerAdded(player)
    	local function onCharacterAdded(character)
    		setCollisionGroup(character, bluePlayers)
    	end
    	player.CharacterAdded:Connect(onCharacterAdded)
    end
    Players.PlayerAdded:Connect(onPlayerAdded)
    
    PhysicsService:CollisionGroupSetCollidable(bluePlayers, blueDoors, false)
    PhysicsService:CollisionGroupSetCollidable(redPlayers, redDoors, false)


```
Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link](/zh-cn/assets/blt10aecbce6c561ff1/Team-Doors.mp4) to the video instead. 



***__Roblox官方链接__:[Restricted/Team Doors](https://developer.roblox.com/zh-cn/articles/Collision-Filtering-Team-Doors)