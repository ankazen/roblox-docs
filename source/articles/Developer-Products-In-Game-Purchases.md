# Developer Products – In‑Game Purchases 
Time:<em>10  分钟</em>

**Developer products** are items which players can buy more than once, making them perfect for in-game currency, ammo, or similar purchases.

For items or abilities that a player might purchase just **once**, such as a special weapon or a permanent power-up, please refer to `Articles/Game Passes One Time Purchases|Game Passes`. 

## Creating a Developer Product

To create a new developer product:

  1. In Roblox Studio, click on the **Game Settings** button from the **Home** tab.
![](https://developer.roblox.com/assets/bltd6af44e38b951d0a/Game-Settings.png)



  2. Select the **Monetization** tab.
  3. Next to **Developer Products**, click the **Create** button.
![](https://developer.roblox.com/assets/blt0a372e91f5852e99/Developer-Product-Create.png)



  4. For the new placeholder product, click the ![](https://developer.roblox.com/assets/blt173a1a863c7190a4/PlayFab-Dots-Icon.png)

 button and select **Edit**.
![](https://developer.roblox.com/assets/bltae98cda6a17b56b1/Developer-Product-Edit.png)



  5. Specify the product’s name and the price.
  6. Click the **Save** button.

After creating a developer product, Roblox assigns it a unique ID and all products are neatly listed in the **Monetization** tab.

![](https://developer.roblox.com/assets/blt77098ed66bd4f813/Dev-Product-Listing.png)



## Scripting for Developer Products

To take full advantage of developer products, you’ll need to use scripting. Here are some common examples:

### Getting a Game’s Developer Products

To gather data for all of the developer products in a game, use the `MarketplaceService/GetDeveloperProductsAsync|GetDeveloperProductsAsync()` method. This returns a `Pages` object that you can inspect and filter to build an in-game store, product list GUI, etc.

### Getting Product Info

To get information (price, name, image, etc.) for a specific product, use the `MarketplaceService/GetProductInfo|GetProductInfo()` function with a second argument:

```    
    
    local MarketplaceService = game:GetService("MarketplaceService")
    
    local productID = 0000000  -- Change this to your developer product ID
    
    local productInfo = MarketplaceService:GetProductInfo(productID, Enum.InfoType.Product)


```
### Prompting a Purchase

You can prompt a player to purchase one of your developer products with the `MarketplaceService/PromptProductPurchase|PromptProductPurchase()` method of `MarketplaceService`. In the following code, the `promptPurchase()` function can be called when the player presses a `Articles/Creating GUI Buttons|button`, talks to a vendor NPC, or whatever fits your game design.

```    
    
    local MarketplaceService = game:GetService("MarketplaceService")
    local Players = game:GetService("Players")
    
    local productID = 0000000  -- Change this to your developer product ID
    
    -- Function to prompt purchase of the developer product
    local function promptPurchase()
    	local player = Players.LocalPlayer
    	MarketplaceService:PromptProductPurchase(player, productID)
    end


```
After a purchase is made, it’s your responsibility to handle and record the transaction. This can be done through a `Script` within `ServerScriptService` using the `MarketplaceService/ProcessReceipt|ProcessReceipt` callback. The function you define will be called repetitively until it returns `Enum.ProductPurchaseDecision.PurchaseGranted`.

ProcessReceipt 回调函数 ```    
    
    local MarketplaceService = game:GetService("MarketplaceService")
    local DataStoreService = game:GetService("DataStoreService")
    local Players = game:GetService("Players")
    
    -- 此数据存储用于跟踪已成功处理的购买流程
    local purchaseHistoryStore = DataStoreService:GetDataStore("PurchaseHistory")
    
    -- 表格相关设置，含有产品 ID 和处理购买操作的函数
    local productFunctions = {}
    -- ProductId 123123 的产品可以为玩家补满生命值
    productFunctions[123123] = function(receipt, player)
    	-- 玩家购买生命值回复所需的逻辑或编码（非固定）
    	if player.Character and player.Character:FindFirstChild("Humanoid") then
    		-- 将玩家的生命值补满
    		player.Character.Humanoid.Health = player.Character.Humanoid.MaxHealth
    		-- 标识购买成功
    		return true
    	end
    end
    -- ProductId 456456 的产品将为玩家提供 100 金币
    productFunctions[456456] = function(receipt, player)
    	-- 玩家购买 100 金币的逻辑或编码（非固定）
    	local stats = player:FindFirstChild("leaderstats")
    	local gold = stats and stats:FindFirstChild("Gold")
    	if gold then
    		gold.Value = gold.Value + 100
    		-- 标识购买成功
    		return true
    	end
    end
    
    -- 核心 ‘ProcessReceipt’ 回调函数
    local function processReceipt(receiptInfo)
    
    	-- 检查数据存储，判断产品是否已经发放  
    	local playerProductKey = receiptInfo.PlayerId .. "_" .. receiptInfo.PurchaseId
    	local purchased = false
    	local success, errorMessage = pcall(function()
    		purchased = purchaseHistoryStore:GetAsync(playerProductKey)
    	end)
    	-- 如果购买流程被记录下来，则说明产品已发放
    	if success and purchased then
    		return Enum.ProductPurchaseDecision.PurchaseGranted
    	elseif not success then
    		error("Data store error:" .. errorMessage)
    	end
    
    	-- 找到服务器中进行购买的玩家
    	local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
    	if not player then
    		-- 玩家可能离开了游戏
    		-- 玩家返回游戏时将会再次调用回调函数
    		return Enum.ProductPurchaseDecision.NotProcessedYet
    	end
    	
    	-- 从上面的 ‘productFunctions’ 表格中查找处理函数
    	local handler = productFunctions[receiptInfo.ProductId]
    
    	-- 调用处理函数并捕捉错误
    	local success, result = pcall(handler, receiptInfo, player)
    	if not success or not result then
    		warn("Error occurred while processing a product purchase")
    		print("\nProductId:", receiptInfo.ProductId)
    		print("\nPlayer:", player)
    		return Enum.ProductPurchaseDecision.NotProcessedYet
    	end
    
    	-- 在数据存储中记录好交易内容，确保同样的产品不会被再次发放
    	local success, errorMessage = pcall(function()
    		purchaseHistoryStore:SetAsync(playerProductKey, true)
    	end)
    	if not success then
    		error("Cannot save purchase data:" .. errorMessage)
    	end
    
    	-- 重要：告知 Roblox 购买流程已被成功处理
    	return Enum.ProductPurchaseDecision.PurchaseGranted
    end
    
    -- 设置回调函数，这个设置只能由服务器上的一个脚本进行一次！ 
    MarketplaceService.ProcessReceipt = processReceipt


```
Roblox itself does **not** record the purchase history of developer products by specific players, although you can view overall daily/monthly stats as outlined `articles/Developer Stats|here`. If you want to track player-specific purchase history, it's your responsibility to store the data, typically with `Articles/Data store|data stores`. See the `MarketplaceService/ProcessReceipt|ProcessReceipt` reference for a code example which includes data store usage. 

The `receiptInfo` table passed to the `processReceipt()` callback function contains detailed info on the purchase. See the `MarketplaceService/ProcessReceipt|ProcessReceipt` reference for a list of keys and descriptions. 



***__Roblox官方链接__:[Developer Products – In‑Game Purchases](https://developer.roblox.com/zh-cn/articles/Developer-Products-In-Game-Purchases)