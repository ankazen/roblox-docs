# Game Passes – One‑Time Purchases 
Time:<em>10  分钟</em>

**Game passes** let you create special items that can only be bought once per player using Robux (![](https://developer.roblox.com/assets/blt924b50fb6c9e0995/Robux-Icon-NoRightMargin.png)

). Examples are special access to a `articles/Collision Filtering Team Doors|restricted area`, an in-game avatar item, or a permanent power-up.

For items that a player might purchase **multiple** times, such as potions, temporary power-ups, or in-game currency, please refer to [Developer Products](/articles/Developer-Products-In-Game-Purchases). 

## Creating a Game Pass

To make a new game pass, go to the [Create](https://www.roblox.com/develop) page on the Roblox website. Once there, make sure that the **My Creations** tab is selected and that **Games** is selected in the left column.

![](https://developer.roblox.com/assets/bltc5b09b208db3e46a/My-Creations-Tab.png)



Now follow these steps to create a game pass:

  1. Determine the game you want to create a pass for.
  2. In the settings drop-down menu on the right-hand side, select **Create Game Pass**.
![](https://developer.roblox.com/assets/bltde41a9e5d7d7d278/Create-Game-Pass-2.png)



### Create an Icon

Game pass icons should be designed as follows:

  1. In an image editing application, design a **circular** game pass (a template of 512×512 pixels is recommended). The final icon will be **trimmed/cropped into a circular image**, so you shouldn’t include important details outside the circular boundaries.

![](https://developer.roblox.com/assets/blt40cecbc6b316187c/Circle-Y-L.png)



![](https://developer.roblox.com/assets/blt0895054f0b32e2e7/SlimeShield-Circular-Design.png)



![](https://developer.roblox.com/assets/blt773ada4ae8c71724/r-arrow.svg)

![](https://developer.roblox.com/assets/blt825910f454de69fe/SlimeShield-Circular-Result.png)



![](https://developer.roblox.com/assets/blt38a47bcfd3586afb/Circle-N-L.png)



![](https://developer.roblox.com/assets/blt6332a1c24391100e/SlimeShield-Square-Design.png)



![](https://developer.roblox.com/assets/blt773ada4ae8c71724/r-arrow.svg)

![](https://developer.roblox.com/assets/blt972d49d21cf7bd07/SlimeShield-Square-Result.png)



  2. Save the game pass image in .jpg, .gif, .png, .tga, or .bmp format.

### Upload the Pass

The next step in the creation process is uploading the pass:

  1. Back on the Roblox website, click the small button next to **Find your image**.
![](https://developer.roblox.com/assets/bltc099f654a0619d87/Game-Pass-Choose-File.png)



  2. Find the game pass image on your computer and confirm that you’d like to upload it.
  3. Type in a name and description for the game pass. Remember that players will see this on your game’s page, so be creative and accurately describe what the pass does.
  4. When you’re ready, click **Preview**. On the next screen, review the details for the game pass and click **Verify Upload**.

### Configure the Pass

Once you’ve created the game pass, it will appear on the same page, slightly further down. The final step is configuring the pass so players can buy it.

  1. Select **Configure** from the right-side pull down menu for the new pass.
![](https://developer.roblox.com/assets/bltf2d629757ea59a30/Configure-Game-Pass-1.png)



  2. On the configuration page, click the **Sales** tab.
![](https://developer.roblox.com/assets/bltc19c086d4acd0b56/Configure-Game-Pass-Sales-Tab.png)



  3. Click the **Item for Sale** toggle switch to make the pass available to players.
![](https://developer.roblox.com/assets/blt8a4432af462bd86a/Configure-Game-Pass-Sale-Toggle.png)



  4. Set the price (in Robux) for players. Notice that the price affects how many Robux you will earn for each sale.
![](https://developer.roblox.com/assets/blt3cd5787645c3534e/Configure-Game-Pass-Set-Price.png)



  5. Click the **Save** button to confirm your settings.

## Giving Game Passes an Effect

Once a player buys a game pass, they will naturally expect to get its special ability or bonus when they start playing. This does **not** happen automatically, so you must check which players already own the pass and assign the ability/bonus to them.

This example script checks when any player enters the game and then checks if they own the game pass with the matching ID set in the variable `gamePassID`.

```    
    
    local MarketplaceService = game:GetService("MarketplaceService")
    local Players = game:GetService("Players")
    
    local gamePassID = 0000000  -- Change this to your game pass ID
    
    local function onPlayerAdded(player)
    
    	local hasPass = false
    
    	-- Check if the player already owns the game pass
    	local success, message = pcall(function()
    		hasPass = MarketplaceService:UserOwnsGamePassAsync(player.UserId, gamePassID)
    	end)
    
    	-- If there's an error, issue a warning and exit the function
    	if not success then
    		warn("Error while checking if player has pass: " .. tostring(message))
    		return
    	end
    
    	if hasPass == true then
    		print(player.Name .. " owns the game pass with ID " .. gamePassID)
    		-- Assign this player the ability or bonus related to the game pass
    		--
    	end
    end
    
    -- Connect "PlayerAdded" events to the "onPlayerAdded()" function
    Players.PlayerAdded:Connect(onPlayerAdded)


```
To find the ID of a game pass, inspect the URL in your web browser which will look similar to one of these, depending on whether you're configuring or viewing the pass: 

https://www.roblox.com/game-pass/configure?id=0123456

https://www.roblox.com/game-pass/0123456/Slime-Shield

The game pass ID is the number within the URL, for example **0123456** as shown here. Simply use that ID on line 4 of the code example above. 

This code should be located in a `Script` object (not a `LocalScript`) within `ServerScriptService` so the server can handle the ability or bonus given to the player. 

## Prompting In-Game Purchases

Players can buy game passes directly from your game’s main page by clicking the **Store** tab and browsing the game passes you’ve made available to them:

![](https://developer.roblox.com/assets/blt47dd099817c55e22/Game-Pass-Listing.png)



However, it’s also a great idea to offer **in-game purchases** to players through a shop or vendor NPC within the game. The following scripts are a basic model for prompting players to buy a game pass.

### Server-Side Code

This code should be located in a `Script` object (not a `LocalScript`) within `ServerScriptService` so the server can handle the ability or bonus given to the player.

```    
    
    local MarketplaceService = game:GetService("MarketplaceService")
    
    local gamePassID = 0000000  -- Change this to your game pass ID
    
    -- Function to handle a completed prompt and purchase
    local function onPromptGamePassPurchaseFinished(player, purchasedPassID, purchaseSuccess)
    
    	if purchaseSuccess == true and purchasedPassID == gamePassID then
    		print(player.Name .. " purchased the game pass with ID " .. gamePassID)
    		-- Assign this player the ability or bonus related to the game pass
    		--
    	end
    end
    
    -- Connect "PromptGamePassPurchaseFinished" events to the "onPromptGamePassPurchaseFinished()" function
    MarketplaceService.PromptGamePassPurchaseFinished:Connect(onPromptGamePassPurchaseFinished)


```
### Client-Side Code

This code can be placed in a `LocalScript` and the `promptPurchase()` function can be called when the player presses a `Articles/Creating GUI Buttons|button`, when their character touches a part, or whatever fits your game design.

```    
    
    local MarketplaceService = game:GetService("MarketplaceService")
    local Players = game:GetService("Players")
    
    local gamePassID = 0000000  -- Change this to your game pass ID
    
    -- Function to prompt purchase of the game pass
    local function promptPurchase()
    
    	local player = Players.LocalPlayer
    	local hasPass = false
    
    	local success, message = pcall(function()
    		hasPass = MarketplaceService:UserOwnsGamePassAsync(player.UserId, gamePassID)
    	end)
    
    	if not success then
    		warn("Error while checking if player has pass: " .. tostring(message))
    		return
    	end
    
    	if hasPass then
    		-- Player already owns the game pass; tell them somehow
    	else
    		-- Player does NOT own the game pass; prompt them to purchase
    		MarketplaceService:PromptGamePassPurchase(player, gamePassID)
    	end
    end


```
Roblox itself does **not** record the purchase history of game passes by specific players, although you can view overall daily/monthly stats as outlined `articles/Get and Analyze Revenue Data|here`. If you want to track player-specific purchase history, it's your responsibility to store the data, typically with `Articles/Data store|data stores`. 



***__Roblox官方链接__:[Game Passes – One‑Time Purchases](https://developer.roblox.com/zh-cn/articles/Game-Passes-One-Time-Purchases)