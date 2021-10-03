# 保存玩家数据 
Time:<em>15  分钟</em>

Roblox 支持将数据保存到其服务器上。此功能主要用于存储上次会话的玩家数据，可完整保存其统计数据、道具和其他数据。在本教程中，我们将创建一个系统，该系统自动存储玩家的资金和体验数据，以便在他们再次加入游戏时可取回这些数据。

如果你想在开始本教程前更深入地了解 Roblox 数据存储系统，请参见`Articles/Data store|数据存储`文章。 

API 访问权限必须处于有效状态，以便能访问和测试 Roblox Studio 中的数据存储。请参见`Articles/Data store|数据存储`文章了解有关启用 API 访问权限的说明。 

## 创建数据模块

在深入了解数据存储前，我们将设置一个系统，用于在游戏过程中记录玩家的资金和体验数据。首先，我们将创建 `ModuleScript`，这是一种可在其他脚本中引用的特殊脚本。此 `ModuleScript` 的理想位置是放在 **ServerStorage** 中。

```    
    
    -- Set up table to return to any script that requires this module script
    local PlayerStatManager = {}
    
    -- Table to hold player information for the current session
    local sessionData = {}
    
    local AUTOSAVE_INTERVAL = 60
    
    -- Function that other scripts can call to change a player's stats
    function PlayerStatManager:ChangeStat(player, statName, value)
    	local playerUserId = "Player_" .. player.UserId
    	assert(typeof(sessionData[playerUserId][statName]) == typeof(value), "ChangeStat error: types do not match")
    	if typeof(sessionData[playerUserId][statName]) == "number" then
    		sessionData[playerUserId][statName] = sessionData[playerUserId][statName] + value
    	else
    		sessionData[playerUserId][statName] = value
    	end
    end
    
    -- Function to add player to the "sessionData" table
    local function setupPlayerData(player)
    	local playerUserId = "Player_" .. player.UserId
    	sessionData[playerUserId] = {Money=0, Experience=0}
    end
    
    -- Connect "setupPlayerData()" function to "PlayerAdded" event
    game.Players.PlayerAdded:Connect(setupPlayerData)
    
    return PlayerStatManager


```
请注意，`PlayerStatManager:ChangeStat()` 函数可处理**数值**或**非数值**变更。这意味着你可以安全地使用数值（正值或负值）或字符串值作为 `value` 参数来调用此函数。 

## 保存玩家数据

现在，我们开始使用数据存储来存储实际信息。

### 初始化数据存储

首先，我们将在同一 `ModuleScript` 中为数据存储添加一个新变量，并调用 `DataStoreService/GetDataStore|GetDataStore()` 以打开新的 **PlayerData** 数据存储。

```    
    
    -- Set up table to return to any script that requires this module script
    local PlayerStatManager = {}
    
    local DataStoreService = game:GetService("DataStoreService")
    local playerData = DataStoreService:GetDataStore("PlayerData")
    
    -- Table to hold player information for the current session
    local sessionData = {}
    
    local AUTOSAVE_INTERVAL = 60


```
你可以方便地命名数据存储。数据存储将在游戏中的所有场景之间共享，因此，如果你的游戏中有多个场景，则这些场景都可以通过名称访问同一个数据存储。 

### 读取/写入初始数据

就下来，让我们更改 `setupPlayerData()` 函数的工作方式。目前，此函数只在玩家加入游戏时为玩家创建新数据，但此数据不会保存在任何位置！现在，通过访问 `playerData` 数据存储，我们可以调用 `GlobalDataStore/GetAsync|GetAsync()` 来检查它是否保存玩家的任何信息。如果此调用返回有效数据，我们会将此数据保存到 `sessionData` 表，否则会将**新**玩家数据保存到 `sessionData` 表中。

```    
    
    -- Function to add player to the "sessionData" table
    local function setupPlayerData(player)
    	local playerUserId = "Player_" .. player.UserId
    	local data = playerData:GetAsync(playerUserId)
    	if data then
    		-- Data exists for this player
    		sessionData[playerUserId] = data
    	else
    		-- Data store is working, but no current data for this player
    		sessionData[playerUserId] = {Money=0, Experience=0}
    	end
    end
    
    -- Connect "setupPlayerData()" function to "PlayerAdded" event
    game.Players.PlayerAdded:Connect(setupPlayerData)


```
### 退出时保存数据

建议在玩家退出游戏时保存玩家数据。可以通过绑定到 `Players/PlayerRemoving|PlayerRemoving` 事件的新 `savePlayerData()` 函数来实现此功能。

```    
    
    -- Function to save player's data
    local function savePlayerData(playerUserId)
    	if sessionData[playerUserId] then
    		playerData:SetAsync(playerUserId, sessionData[playerUserId])
    	end
    end
    
    -- Function to save player data on exit
    local function saveOnExit(player)
    	local playerUserId = "Player_" .. player.UserId
    	savePlayerData(playerUserId)
    end
    
    -- Connect "setupPlayerData()" function to "PlayerAdded" event
    game.Players.PlayerAdded:Connect(setupPlayerData)
    
    -- Connect "saveOnExit()" function to "PlayerRemoving" event
    game.Players.PlayerRemoving:Connect(saveOnExit)


```
### 自动保存

最后，有必要让系统处理游戏崩溃等意外事件。为此，可以使用将等待`AUTOSAVE_INTERVAL` 秒（60）的函数，此函数循环遍历 `sessionData` 表中的所有玩家，并使用 `savePlayerData()` 函数保存当前信息。请注意，此函数最初会通过使用 `spawn()` 函数在协同程序中运行。

```    
    
    -- Function to periodically save player data
    local function autoSave()
    	while wait(AUTOSAVE_INTERVAL) do
    		for playerUserId, data in pairs(sessionData) do
    			savePlayerData(playerUserId)
    		end
    	end
    end
    
    -- Start running "autoSave()" function in the background
    spawn(autoSave)
    
    -- Connect "setupPlayerData()" function to "PlayerAdded" event
    game.Players.PlayerAdded:Connect(setupPlayerData)


```
实现以上所有函数后，我们将得到一个简单的统计数据保存系统，可用于自动保存玩家数据。

## 处理数据存储失败

对数据存储的请求（如所有网络调用）可能偶尔会因连接不良或其他问题而失败。正如你在`Articles/Data store|数据存储`文章中所了解的，应将这些调用打包在 `pcall()` 中以捕获和处理错误。下面我们将此做法应用于当前脚本：

```    
    
    -- Set up table to return to any script that requires this module script
    local PlayerStatManager = {}
    
    local DataStoreService = game:GetService("DataStoreService")
    local playerData = DataStoreService:GetDataStore("PlayerData")
    
    -- Table to hold player information for the current session
    local sessionData = {}
    
    local AUTOSAVE_INTERVAL = 60
    
    -- Function that other scripts can call to change a player's stats
    function PlayerStatManager:ChangeStat(player, statName, value)
    	local playerUserId = "Player_" .. player.UserId
    	assert(typeof(sessionData[playerUserId][statName]) == typeof(value), "ChangeStat error: types do not match")
    	if typeof(sessionData[playerUserId][statName]) == "number" then
    		sessionData[playerUserId][statName] = sessionData[playerUserId][statName] + value
    	else
    		sessionData[playerUserId][statName] = value
    	end
    end
    
    -- Function to add player to the "sessionData" table
    local function setupPlayerData(player)
    	local playerUserId = "Player_" .. player.UserId
    	local success, data = pcall(function()
    		return playerData:GetAsync(playerUserId)
    	end)
    	if success then
    		if data then
    			-- Data exists for this player
    			sessionData[playerUserId] = data
    		else
    			-- Data store is working, but no current data for this player
    			sessionData[playerUserId] = {Money=0, Experience=0}
    		end
    	else
    		warn("Cannot access data store for player!")
    	end
    end
    
    -- Function to save player's data
    local function savePlayerData(playerUserId)
    	if sessionData[playerUserId] then
    		local success, err = pcall(function()
    			playerData:SetAsync(playerUserId, sessionData[playerUserId])
    		end)
    		if not success then
    			warn("Cannot save data for player!")
    		end
    	end
    end
    
    -- Function to save player data on exit
    local function saveOnExit(player)
    	local playerUserId = "Player_" .. player.UserId
    	savePlayerData(playerUserId)
    end
    
    -- Function to periodically save player data
    local function autoSave()
    	while wait(AUTOSAVE_INTERVAL) do
    		for playerUserId, data in pairs(sessionData) do
    			savePlayerData(playerUserId)
    		end
    	end
    end
    
    -- Start running "autoSave()" function in the background
    spawn(autoSave)
    
    -- Connect "setupPlayerData()" function to "PlayerAdded" event
    game.Players.PlayerAdded:Connect(setupPlayerData)
    
    -- Connect "saveOnExit()" function to "PlayerRemoving" event
    game.Players.PlayerRemoving:Connect(saveOnExit)
    
    return PlayerStatManager


```
## 数据存储重试

作为最后一项可靠性措施，有必要在第一次尝试失败后重新尝试保存数据。可以使用 `savePlayerData()` 函数中简单的 `repeat` 循环将此功能添加到现有脚本中：

```    
    
    -- Function to save player's data
    local function savePlayerData(playerUserId)
    	if sessionData[playerUserId] then
    		local tries = 0	
    		local success
    		repeat
    			tries = tries + 1
    			success = pcall(function()
    				playerData:SetAsync(playerUserId, sessionData[playerUserId])
    			end)
    			if not success then wait(1) end
    		until tries == 3 or success
    		if not success then
    			warn("Cannot save data for player!")
    		end
    	end
    end


```


***__Roblox官方链接__:[保存玩家数据](https://developer.roblox.com/zh-cn/articles/Saving-Player-Data)