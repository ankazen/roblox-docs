# Badges – Special Game Awards 
Time:<em>10  分钟</em>

**Badges** let you create special awards for players who do something exceptional within your game. A badge might be awarded when a player:

  * Collects 100 gold stars.
  * Jumps across a challenging series of platforms over a poison swamp.
  * Finds all 7 keys to unlock the kingdoms of Earth, Air, Lava, Ocean, Light, Shadow, and Dreams.

## Creating a Badge

It costs ![](https://developer.roblox.com/assets/blt60814f4e9ed61103/Robux-Icon.png)

100 to create a badge. To begin:

  1. Go to the [Create](https://www.roblox.com/develop) page on the Roblox website. Once there, make sure that **Games** is selected in the left column.
  2. Determine the game you want to create a badge for.
  3. In the settings drop-down menu on the right-hand side, select **Create Badge**.
![](https://developer.roblox.com/assets/blte6e47358ebd81561/Create-Badge.png)



### Create an Icon

Badge icons should be designed as follows:

  1. In an image editing application, design a **circular** badge (a template of 512×512 pixels is recommended). The final icon will be **trimmed/cropped into a circular image**, so you shouldn’t include important details outside the circular boundaries.

![](https://developer.roblox.com/assets/blt40cecbc6b316187c/Circle-Y-L.png)



![](https://developer.roblox.com/assets/blt2bcfa994647e6308/KeyMaster-Circular-Design.png)



![](https://developer.roblox.com/assets/blt773ada4ae8c71724/r-arrow.svg)

![](https://developer.roblox.com/assets/blt79978052a378e1b0/KeyMaster-Circular-Result.png)



![](https://developer.roblox.com/assets/blt38a47bcfd3586afb/Circle-N-L.png)



![](https://developer.roblox.com/assets/blt04d2a0c31aaf78e9/KeyMaster-Square-Design.png)



![](https://developer.roblox.com/assets/blt773ada4ae8c71724/r-arrow.svg)

![](https://developer.roblox.com/assets/blt38919c6f1290c360/KeyMaster-Square-Result.png)



  2. Save the badge image in .jpg, .gif, .png, .tga, or .bmp format.

### Upload the Badge

The next step in the creation process is uploading the badge.

  1. Back on the Roblox website, click the small button next to **Find your image**.
![](https://developer.roblox.com/assets/bltbab22e91713f7bbe/Badge-Choose-File.png)



  2. Find the badge image on your computer and confirm that you’d like to upload it.
  3. Type in a name and description for the badge. It’s a good idea to describe how the badge can be earned so players have a specific goal to reach for.
  4. Click **Preview**, review the details for the badge, and purchase when you’re ready. Once the purchase is complete, the badge will appear in the **Game Badges** section of the game’s main page.
![](https://developer.roblox.com/assets/blt2f593945660307c3/Badge-Created.png)



## Scripting for Badges

To take full advantage of badges, you’ll need to use scripting. Here are some common examples:

### Awarding a Badge

In the following server-side `Script`, the `awardBadge()` function can be called whenever it fits your game design. Using properties of the badge fetched via `BadgeService/GetBadgeInfoAsync|BadgeService:GetBadgeInfoAsync()`, it confirms that the badge can be awarded and does so using `BadgeService/AwardBadge|BadgeService:AwardBadge()`.

服务器端脚本 ```    
    
    local BadgeService = game:GetService("BadgeService")
    
    local function awardBadge(player, badgeId)
    	-- 确认徽章可以被授予
    	if BadgeService:IsLegal(badgeId) and not BadgeService:IsDisabled(badgeId) then
    		-- 授予徽章
    		BadgeService:AwardBadge(player.UserId, badgeId)
    	end
    end


```
### Checking Earned Badges

The following script waits for any player to enter the game and checks if they own a specific badge. This is useful for creating a `articles/Collision Filtering Team Doors|restricted area` or `articles/Teleporting Between Places|teleporter` that only works if a player owns a special badge.

Checking Earned Badges ```    
    
    local BadgeService = game:GetService("BadgeService")
    local Players = game:GetService("Players")
    
    local badgeID = 00000000  -- Change this to your badge ID
    
    local function onPlayerAdded(player)
    	-- Check if the player has the badge
    	local success, hasBadge = pcall(function()
    		return BadgeService:UserHasBadgeAsync(player.UserId, badgeID)
    	end)
    
    	-- If there's an error, issue a warning and exit the function
    	if not success then
    		warn("Error while checking if player has badge!")
    		return
    	end
    
    	if hasBadge then
    		-- Handle player's badge ownership as needed
    	end
    end
    
    -- Connect "PlayerAdded" events to the "onPlayerAdded()" function
    Players.PlayerAdded:Connect(onPlayerAdded)


```
### Getting Badge Info

To simply get info about a badge, use the `BadgeService/GetBadgeInfoAsync|BadgeService:GetBadgeInfoAsync()` function as illustrated in the following example.

异步获取徽章信息 ```    
    
    local BadgeService = game:GetService("BadgeService")
    
    -- 获取信息（需要一点时间）
    local info = BadgeService:GetBadgeInfoAsync(2124421311)
    
    -- 打印我们刚才获取的信息
    print("Badge: " .. info.Name)
    print("Description: " .. info.Description)
    print("Icon: rbxassetid://" .. info.IconImageId)
    if info.IsEnabled then
    	print("Badge is enabled")
    else
    	print("Badge is disabled")
    end
    
    
    Badge: Dominator — 3 Victories
    Description: Win 3 matches.
    Icon: rbxassetid://2131632696
    Badge is enabled

```


***__Roblox官方链接__:[Badges – Special Game Awards](https://developer.roblox.com/zh-cn/articles/Badges-Special-Game-Awards)