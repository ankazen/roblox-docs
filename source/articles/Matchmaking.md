# 玩家匹配系统 
Time:<em>30  分钟</em>

在竞技类游戏中，如果能把水平相当的玩家进行匹配，会给玩家带来更好的游戏体验。目前 Roblox 可以自动将玩家分配到不同的 `Team` （队伍）中，但该功能并不包括玩家的水平匹配。在这篇文章中，我们将会学习如何在 Roblox 中实现 Elo 等级分制度，以及如何使用排名对两名玩家进行匹配。

## Elo 等级分制度

Elo 等级分制度是衡量玩家水平的一种评级方法，被广泛运用于多种体育运动之中，其中尤为突出的是国际象棋方面的应用。这种评级制度不仅能够帮助玩家查看自己与其他玩家之间的差距，还可以按照玩家评级进行玩家匹配。由于同一评级的玩家水平大致相当，因此只需将同一评级的玩家互相进行匹配，极为简单直观。同时，通过这种制度也可以预估玩家在对战中的胜率等。

Elo 等级分制度只用对战胜利、失败与平手（算作半个胜利和半个失败）进行玩家评级排行。当两个玩家完成一场对战后，其评级也会进行相应的调整。调整数目与每个玩家的个人评级相关联。如果高排名的玩家打败了低排名的玩家，则高排名的玩家只会获得较小的评级提升（同理，低排名的玩家也只会获得较小的评级降低）。而如果低排名的玩家打败了高排名的玩家，将会获得大幅度的评级提升。

本文将不会赘述 Elo 等级分制度的具体理论与计算方法，有兴趣的开发者可以前往官方[维基页面](http://en.wikipedia.org/wiki/Elo_rating_system)进行延伸阅读。我们对 Elo 等级分制度将会进行以下列三条重点为中心的运用：

  * 每场对战结果都会为每个参战玩家生成一个分数。玩家胜利时分数为 1；平手时为 0.5；失败时为 0。
  * 每个玩家都会拥有预期分数。这个分数参照玩家排行生成，代表了玩家的获胜概率，且也将在1和0之间。
  * 玩家的排名将会根据对战结果分数与预期分数进行调整。同时一场对战能够进行的排名调整最大值也将被限制（这个限制将会被称为 K系数）。

## 玩家匹配大厅

游戏的第一个部分将会为游戏大厅。虽然大厅在 Roblox 中极为常见，但玩家将会在我们这个大厅中进行匹配。匹配完成后，配对的玩家将会被传送到另外的竞技场场景，在一个简单的游戏中互相对战。

### 获取玩家排名

当玩家第一次加入游戏时，需要给予其一个排名。排名可以选择任何数字，但在本示例中我们将会把初始排名设为 1500 。这样不管是上行或下移都有一定空间，不必担心其排名过于接近负数。如果玩家以前曾经加入过游戏，则需要从 DataStore 中获取其排名。无论是不是初次加入游戏，我们都会将把玩家排名显示在排名榜中。
    
    
    local ratingData = game:GetService("DataStoreService"):GetDataStore("RatingData")
    
    -- 处理玩家加入游戏。如果是新玩家，则需要给予其
    -- 初始排名；如果是已有玩家，则需要从 DataStore 
    -- 中获取其排名。最后需要将排名显示在排行榜中
    game.Players.PlayerAdded:connect(function (player)
    	local playerData = {}
    	
    	-- 如果玩家数据不存在于 DataStore 中，则为其创建 1500 的初始排名
    	ratingData:UpdateAsync(player.userId, function(oldValue)
    		local newValue = oldValue
    		if not newValue then
    			newValue = { Rating = 1500 }
    		end
    		return newValue
    	end)
    	playerData.Score = ratingData:GetAsync(tostring(player.UserId)).Rating
    
    	-- 在排行榜中显示排名
    	local leaderstats = Instance.new("Folder", player)
    	leaderstats.Name = "leaderstats"
    	
    	local displayRating = Instance.new("IntValue", leaderstats)
    	displayRating.Name = "Rating"
    	displayRating.Value = playerData.Score
    end)
    

### 排名列表

在匹配玩家时，构建一个让寻找匹配的玩家快速在排名范围内找到匹配对象的结构会大幅提升玩家体验。虽然这个问题有许多解决方法，但在本示例中我们将会使用双链表。如果能确保链表的排序依据为玩家排名，则为玩家寻找匹配时只需在该玩家节点附近搜寻即可。

由于该列表的实现过程较长，为了更方便的查看示例，我们将把 Rank （排行）列表的所有代码放入一个 `ModuleScript` 中。

#### 基础列表结构

链表乃是节点的结合（也就是一张表格）。其中每个节点中都含有对列表中下一个节点的引用。双链表中的节点同时也拥有对列表中上一个节点的引用。
    
    
    local rankList = {}
    rankList.Top = nil
    rankList.Bottom = nil
    
    -- 在列表中的 oldNode 前插入 newNode 。如果 oldNode 在列表顶端则重新分配 rankList.Top
    function rankList:InsertBefore(newNode, oldNode)
    	if oldNode.Prev then
    		newNode.Prev = oldNode.Prev
    		oldNode.Prev.Next = newNode
    	end
    	newNode.Next = oldNode
    	oldNode.Prev = newNode
    	if rankList.Top == oldNode then
    		rankList.Top = newNode
    	end
    	return newNode
    end
    
    -- 从链表中移除节点。确保列表的 Top （顶部）和 Bottom （底部）都指向正确的节点。
    -- 同时从查找字典中移除节点
    function rankList:RemoveNode(node)
    	if node.Prev then
    		node.Prev.Next = node.Next
    		if rankList.Bottom == node then
    			rankList.Bottom = node.Prev
    		end
    	end
    	if node.Next then
    		node.Next.Prev = node.Prev
    		if rankList.Top == node then
    			rankList.Top = node.Next
    		end
    	end
    	keyTable[tostring(node.userId)] = nil
    end
    

#### 将玩家添加至列表

至此为止，我们只是编写了链表的基本结构。接下来需要将玩家数据添加至列表中。为了确保列表正常工作，每添加一个玩家后都需要确保将玩家按照排名添加到了列表中的正确位置。这样一来，列表的排序将不会出现混乱，对之后寻找匹配也会有帮助。

另外，我们也将添加将 userIds 连接至其相应节点的字典，这样就可以快速到达列表的任意位置。否则我们需要迭代列表才能找到玩家节点。
    
    
    -- 将 userIds 连接到对应链表节点的字典，方便快速查找
    local keyTable = {}
    
    -- 添加玩家至列表。通过依照排名将玩家添加至列表的正确
    -- 位置来确保列表的排序无误。同时将玩家添加至查找字典
    function rankList:AddPlayer(userId, rank, startedWaiting)
    	local node = {UserId = userId, Rank = rank, Age = startedWaiting, Next = nil, Prev = nil}
    	keyTable[tostring(userId)] = node	
    	
    	-- 首先检查列表是否为空。如是则将列表的 Top （顶部）和 Bottom （底部）指向新增节点
    	if not rankList.Top then
    		rankList.Top = node
    		rankList.Bottom = node
    		return node
    	else
    		-- 如果列表非空，则寻找新增节点的添加位置。
    		-- 从 Top （顶部）节点开始，沿列表向下比较排名
    		local currentNode = rankList.Top
    		
    		while currentNode do
    			if currentNode.Rank	> rank then
    				return rankList:InsertBefore(node, currentNode)
    			end		
    			
    			currentNode = currentNode.Next
    		end
    		
    		-- 如果代码运行至此，则新增节点需要被添加至列表最后
    		rankList.Bottom.Next = node
    		node.Prev = rankList.Bottom
    		rankList.Bottom = node
    		return node
    	end
    end
    
    -- 将玩家从列表中移除
    function rankList:RemovePlayer(userId)
    	local playerNode = keyTable[tostring(userId)]
    	rankList:RemoveNode(playerNode)
    end
    

#### 寻找匹配

接下来的步骤可能会更为激动人心，我们将会使用刚刚制作的双链表为玩家寻找匹配。链表中不仅包含了玩家的排名，还包括了其等待对战的时长。当为玩家寻找匹配时，我们会尝试寻找玩家排名特定范围内的匹配。因此，匹配的对象应该是排名范围内等待时间最长的玩家。

进行搜索时，我们将会从寻找匹配的玩家节点开始向列表的上方和下方进行搜寻，同时也要追踪等待时间最长的玩家。
    
    
    -- FindPlayerInRangeWithNode 的私人搜索函数。可基于
    -- searchAscending 向列表的顶部或底部进行搜索
    local function Search(current, rank, searchAscending, range, oldestWait)
    	local retNode = nil	
    	while current do
    		if math.abs(rank - current.Rank) > range then
    			break
    		end		
    		if current.Age < oldestWait then
    			oldestWait = current.Age
    			retNode = current
    		end
    		if searchAscending then 
    			current = current.Next
    		else
    			current = current.Prev
    		end
    	end
    	return retNode, oldestWait
    end
    
    -- 返回处于 startNode 玩家排名范围内的玩家节点。
    -- 返回的玩家同时也是范围内等待时间最长的。
    function rankList:FindPlayerInRangeWithNode(startNode, range)
    	local oldestWait = math.huge
    	local rank = startNode.Rank
    	local current = startNode.Next
    	local retNode = nil
    	
    	retNode, oldestWait = Search(startNode.Next, startNode.Rank, true, range, oldestWait)
    	retNode, oldestWait = Search(startNode.Prev, startNode.Rank, false, range, oldestWait)
    	
    	return retNode
    end
    
    -- 返回在 userId 排名范围内找到玩家的用户 ID 。
    -- 若未找到玩家则返回 nil 。
    function rankList:FindPlayerInRange(userId, range)
    	local playerNode = keyTable[tostring(userId)]
    	if playerNode then
    		local otherPlayer = rankList:FindPlayerInRangeWithNode(playerNode, range)
    		if otherPlayer then 
    			return otherPlayer.UserId 
    		end
    	end
    	return nil
    end
    

### 匹配队列

游戏中的玩家可能并不想马上进入游戏，不如为他们创造等待匹配的队列吧。由于我们想要优先匹配等待时间最长的玩家，队列在这方面也将会十分有用。在创建队列时，我们将会使用含有所有排队玩家 userId 和玩家进入队列时间的表格。在无位置参数的情况下使用 table.insert 将会确保最后一个进入队列的玩家总处于队列最末尾。同时我们也要确保玩家在找到匹配对象、离开游戏或想要停止排队时能够离开队列。
    
    
    -- 含有排队寻找匹配玩家的表格
    local matchMakingQueue = {}
    
    -- 将玩家的 id 与进入队列时间添加至队列中
    local addToMMQueue = function(playerId, enteredTime)
    	local data = {}
    	data.UserId = playerId
    	data.EnteredQueue = enteredTime
    	table.insert(matchMakingQueue, data)
    end
    
    -- 从队列中移除玩家
    local removeFromMMQueue = function(playerId)
    	for i, playerData in pairs(matchMakingQueue) do
    		if playerData.UserId == playerId then
    			table.remove(matchMakingQueue, i)
    			return
    		end
    	end
    end
    

#### 将玩家添加至队列中

为了将玩家添加至队列中，我们将会在游戏中添加可以触发 `RemoteEvent` 的简单按钮。触发事件后，玩家将会被添加至队列与链表中。再按一次按钮就可以将玩家从队列和链表中移除了。
    
    
    local button = script.Parent
    local lookForGameEvent = game.ReplicatedStorage.LookForGameEvent
    
    local lookForGameNextClick = true
    
    -- 处理点击按钮，使其从队列中添加/移除玩家
    button.MouseButton1Click:connect(function()
    	if lookForGameNextClick then
    		button.Text = "正在寻找匹配。再次点击取消匹配"
    	else
    		button.Text = "寻找匹配。"
    	end
    	lookForGameEvent:FireServer(lookForGameNextClick)
    	lookForGameNextClick = not lookForGameNextClick	
    end)
    

回到主脚本中：
    
    
    local rankedList = require(game.ServerStorage.MatchmakingRankedListModule)
    local lookForGameEvent = game.ReplicatedStorage.LookForGameEvent
    
    -- 当玩家离开游戏时，将玩家从列表与队列中移除
    game.Players.PlayerRemoving:connect(function(player)
    	removeFromMMQueue(player.userId)
    	rankedList:RemovePlayer(player.userId)
    end)
    game.Players.PlayerRemoving:connect(function(player)
    	removeFromMMQueue(player.userId)
    	rankedList:RemovePlayer(player.userId)
    end)
    
    -- 处理远程事件，使其从队列中添加/移除玩家
    lookForGameEvent.OnServerEvent:connect(function(player, lookingForGame)
    	if lookingForGame then
    		print(player.Name .. "正在寻找匹配")
    		local enteredTime = os.time()
    		addToMMQueue(player.userId, enteredTime)
    		rankedList:AddPlayer(player.userId, player.leaderstats.Rating.Value, enteredTime)
    	else
    		print(player.Name .. "已经离开队列")
    		removeFromMMQueue(player.userId)
    		rankedList:RemovePlayer(player.userId)
    	end
    end)
    

#### 处理队列

获取将玩家添加至队列与链表中的能力后，我们现在可以循环遍历队列，对正在排队的玩家进行匹配。同时，我们还需要定义一个寻找匹配的排名范围。简单来讲，互相匹配的玩家应当排名较为靠近（例如排名差异在 100 之内）。但有时在范围内找不到合适的玩家，需要对范围进行扩张。我们将会使用玩家进入队列的时间来决定寻找匹配的排名范围。

需要注意的是，该循环使用了 **spawn** （生成）对函数进行调用，为两名互相匹配的玩家开始游戏。也就是说游戏进行设置时匹配循环仍将进行，可能会需要一段时间。
    
    
    -- 根据排队等待时间返回搜寻匹配的排名范围。
    -- 如果玩家等待时间过长则返回 math.huge，
    -- 允许玩家与任何人进行匹配。
    local getRange = function(timeWaiting)
    	if timeWaiting < 10 then
    		return 100
    	elseif timeWaiting >=10 and timeWaiting < 20 then
    		return 200
    	elseif timeWaiting >=20 and timeWaiting <= 35 then
    		return 300
    	end
    	return math.huge
    end
    
    -- 匹配循环。每 5 秒左右进行循环，为玩家寻找匹配。
    while true do
    	local now = os.time()
    	-- 循环遍历队列，尝试寻找范围内的玩家
    	for _, mmData in pairs(matchMakingQueue) do
    		print("正在匹配。请稍候，" .. mmData.UserId)
    		-- 获取搜索的排名范围
    		local range = getRange(now - mmData.EnteredQueue)
    		-- 使用列表寻找符合排名范围的匹配玩家
    		local otherPlayerId = rankedList:FindPlayerInRange(mmData.UserId, range)
    		if otherPlayerId then
    			-- 找到了另一名玩家。将两位玩家从队伍中移除，
    			-- 防止其与其他玩家匹配
    			print("找到玩家：" .. otherPlayerId)
    			rankedList:RemovePlayer(mmData.UserId)
    			rankedList:RemovePlayer(otherPlayerId)
    			removeFromMMQueue(mmData.UserId)
    			removeFromMMQueue(otherPlayerId)
    			-- 为两名玩家开始游戏。该函数运行可能需要一段时间，
    			-- 请在新线程中生成该函数，以便循环继续。
    			spawn(function() startGame(mmData.UserId, otherPlayerId) end)
    		end
    	end
    	wait(5)
    end
    

### 创建竞技场与传送

通过匹配找到两名玩家后，我们可以使用 `AssetService/CreatePlaceAsync` 创建一个独立场景供其对战使用。创建完成后，我们可以使用 `TeleportService/Teleport` 将一名玩家传送进该场景。虽然可以再次运用 Teleport （传送）将另一名玩家传送进去，且两人很可能会处于同一实例，但我们将无法保证两人一定处于同一实例中。更为保险的方法是等待第一名玩家传送完毕后，使用 `TeleportService/GetPlayerPlaceInstanceAsync` 获取玩家所在的实例，然后使用 `TeleportService/TeleportToPlaceInstance` 将另一名玩家传送过去。
    
    
    local teleportService = game:GetService("TeleportService")
    local arenaPlaceTemplateId = 181238621
    
    -- 为对战创建场所，并将两名玩家传送进去
    local startGame = function(playerAId, playerBId)
    	local message = ""
    	print("即将开始对战：" .. playerAId .. "对" .. playerBId)
    	
    	-- 获取两名玩家对象
    	local playerA = nil
    	local playerB = nil
    	for _, player in pairs(game.Players:GetPlayers()) do
    		if player.userId == playerAId then
    			playerA = player
    		end
    		if player.userId == playerBId then
    			playerB = player
    		end
    	end
    	
    	-- 创建竞技场场所并获取其 id
    	local arenaPlaceId = game:GetService("AssetService"):CreatePlaceAsync(
    		"Arena place for " .. playerA.Name .. " and " .. playerB.Name, arenaPlaceTemplateId)
    
    	-- 绑定 OnTeleport 事件至将会被先传送至场景的 playerA 。
    	-- 若传送成功则将 playerB 传送至同一实例
    	local connection = playerA.OnTeleport:connect(function(teleportState, placeId)
    		if teleportState == Enum.TeleportState.Started then
    			local teleportStarted = os.time()
    			-- 持续检查 playerA 是否到达其它实例。
    			while true do
    				local success, error, placeId, arenaInstanceId = teleportService:GetPlayerPlaceInstanceAsync(playerAId)
    				-- 如果 playerA 传送场所正确，则将 playerB 也传送至同一场景
    				if placeId == arenaPlaceId then
    					teleportService:TeleportToPlaceInstance(arenaPlaceId, arenaInstanceId, playerB)
    					return
    				end
    				wait()
    			end	
    		end
    	end)
    	wait(1)
    	
    	-- 传送 playerA 至竞技场
    	teleportService:Teleport(arenaPlaceId, playerA)
    end
    

## 调整玩家排名

目前，我们已经建立了一个大厅，可以让玩家们与排名相近的对手进行匹配，并让他们进行对战。现在让我们来看看玩家们用来对战的游戏，以及如何根据其在游戏中的表现调整排名。为了让示例简明易懂，我们将会使用极为简单的游戏：两个玩家都会获取一把剑，最先击败对方的玩家将会是胜者。如果出现两个玩家同时击败对方的少见情况，则比赛结果将为平手。

### 设置

在这个游戏中，我们需要持续关注两名玩家是否生存。同时，也需要了解两人的排名。当玩家进入对战游戏时，我们将会把这些信息都放入表中。
    
    
    local players = {}
    local ratingData = game:GetService("DataStoreService"):GetDataStore("RatingData")
    local playerHasDied = false
    
    -- 处理 PlayerAdded 事件，设置玩家表格
    game.Players.PlayerAdded:connect(function(player)
    	
    	-- 当玩家被击败时，需要更新玩家表格。同时也需要将
    	-- 全局变量 playerHasDied 设为 true 以结束对战游戏
    	player.CharacterAdded:connect(function(character)
    		character.Humanoid.Died:connect(function()
    			print(player.Name .. "已被击败")
    			players[tostring(player.userId)].Died = true
    			playerHasDied = true
    		end)
    	end)
    	
    	-- 从 DataStore 获取玩家排名，将玩家表格内的击败状态设为 false
    	print("正在获取玩家数据：" .. player.Name)
    	local playerData = {}
    	playerData.Rating = ratingData:GetAsync(tostring(player.userId)).Rating
    	playerData.Died = false
    	players[tostring(player.userId)] = playerData
    end)
    

### 计算排名变化

我们将会在这里使用 Elo 等级分制度计算每名玩家的排名变化。该函数将会根据每个玩家的当前排名、对战胜败与常数 K 系数来进行计算。请参见 [Elo 等级分制度维基页面](http://en.wikipedia.org/wiki/Elo_rating_system) 查看所使用的函数。
    
    
    local kfactor = 30
    
    -- 使用 Elo 等级分制度计算每个玩家的排名变化
    local calculateRatingChange = function(playerA, playerB)
    	-- 从玩家表格获取每个玩家的排名
    	local playerARating = players[tostring(playerA.userId)].Rating
    	local playerBRating = players[tostring(playerB.userId)].Rating
    
    	-- 从玩家表格获取每个玩家的胜败
    	local playerADied = players[tostring(playerA.userId)].Died
    	local playerBDied = players[tostring(playerB.userId)].Died	
    	
    	-- 计算每个玩家的胜率。需要注意的是： expectedA + expectedB = 1
    	local expectedA = 1 / (1 + math.pow(10,(playerBRating - playerARating)/400))
    	local expectedB = 1 - expectedA
    	
    	-- 根据玩家对战结果计算分数。注意以下值：
    	-- 胜 = 1
    	-- 平 = .5
    	-- 败 = 0
    	-- 我们以 .5 开始（设想结果为平局）。如果玩家被击败则失去 .5 分数，
    	-- 胜利玩家获取 .5 分数
    	local scoreA = .5
    	local scoreB = .5
    	if playerADied then
    		scoreA = scoreA - .5
    		scoreB = scoreB + .5
    	end	
    	if playerBDied then
    		scoreA = scoreA + .5
    		scoreB = scoreB - .5
    	end
    	
    	-- 根据分数、胜率计算每个玩家的排名变化
    	-- 然后以 kfactor 对变化量加以限制
    	local playerAChange = kfactor * (scoreA - expectedA)
    	local playerBChange = kfactor * (scoreB - expectedB)
    	
    	return playerAChange, playerBChange
    end
    

### 检测对战结束

最后一件需要做的事情就是检测对战结束。对战结束之后，我们就可以计算玩家排名变化，更新 DataStore，然后将玩家传送回大厅了。
    
    
    local teleportService = game:GetService("TeleportService")
    local lobbyId = 181194460
    
    -- 等待对战结束
    while not playerHasDied do
    	wait()
    end
    print("玩家已被击败！即将调整分数")
    
    -- 稍作等待，检查是否两人都被击败，以便算为平局
    wait(1)
    
    local playerA = nil
    local playerB = nil
    for _, player in pairs(game.Players:GetPlayers()) do
    	if playerA == nil then
    		playerA = player
    	else
    		playerB = player
    	end
    end
    
    -- 计算每个玩家的排名变化
    local playerAchange, playerBchange = calculateRatingChange(playerA, playerB)
    print("PlayerA points should change by " .. playerAchange)
    print("PlayerB points should change by " .. playerBchange)
    
    -- 修改每个玩家的点数与排名
    adjustPlayerRating(playerA, playerAchange)
    adjustPlayerRating(playerB, playerBchange)
    
    print("即将传送回大厅")
    wait(5)
    
    -- 将玩家传送回大厅
    for _, player in pairs(game.Players:GetPlayers()) do
    	teleportService:Teleport(lobbyId, player)
    end
    

## 示例

### 大厅脚本
    
    
    local lookForGameEvent = game.ReplicatedStorage.LookForGameEvent
    local rankedList = require(game.ServerStorage.MatchmakingRankedListModule)
    local ratingData = game:GetService("DataStoreService"):GetDataStore("RatingData")
    local teleportService = game:GetService("TeleportService")
    local arenaPlaceTemplateId = 181238621
    
    -- 含有排队寻找匹配玩家的表格
    local matchMakingQueue = {}
    
    -- 将玩家的 id 与进入队列时间添加至队列中
    local addToMMQueue = function(playerId, enteredTime)
    	local data = {}
    	data.UserId = playerId
    	data.EnteredQueue = enteredTime
    	table.insert(matchMakingQueue, data)
    end
    
    -- 从队列中移除玩家
    local removeFromMMQueue = function(playerId)
    	for i, playerData in pairs(matchMakingQueue) do
    		if playerData.UserId == playerId then
    			table.remove(matchMakingQueue, i)
    			return
    		end
    	end
    end
    
    -- 处理玩家加入游戏。如果是新玩家，则需要给予其
    -- 初始排名；如果是已有玩家，则需要从 DataStore 
    -- 中获取其排名。最后需要将排名显示在排行榜中
    game.Players.PlayerAdded:connect(function(player)
    	local playerData = {}
    	
    	-- 如果玩家数据不存在于 DataStore 中，则为其创建 1500 的初始排名
    	ratingData:UpdateAsync(player.userId, function(oldValue)
    		local newValue = oldValue
    		if not newValue then
    			newValue = {Rating = 1500}
    		end
    		return newValue
    	end)
    	playerData.Score = ratingData:GetAsync(tostring(player.userId)).Rating
    
    	-- 在排行榜中显示排名
    	local leaderstats = Instance.new("Model", player)
    	leaderstats.Name = "leaderstats"
    	
    	local displayRating = Instance.new("IntValue", leaderstats)
    	displayRating.Name = "Rating"
    	displayRating.Value = playerData.Score
    end)
    
    -- 将玩家添加至队列和列表中寻找匹配
    local function playerSearchingForMatch(userId, rank)
    	local now = os.time()
    	addToMMQueue(userId, now)
    	rankedList:AddPlayer(userId, rank, now)
    end
    
    -- 当玩家离开游戏时将其从队列和列表中移除
    game.Players.PlayerRemoving:connect(function(player)
    	removeFromMMQueue(player.userId)
    	rankedList:RemovePlayer(player.userId)
    end)
    
    -- 处理远程事件，使其从队列中添加/移除玩家
    lookForGameEvent.OnServerEvent:connect(function(player, lookingForGame)
    	if lookingForGame then
    		print(player.Name .. "正在寻找匹配")
    		local enteredTime = os.time()
    		playerSearchingForMatch(player.userId, player.leaderstats.Rating.Value)
    	else
    		print(player.Name .. "已经离开队列")
    		removeFromMMQueue(player.userId)
    		rankedList:RemovePlayer(player.userId)
    	end
    end)
    
    -- 根据排队等待时间返回搜寻匹配的排名范围。
    -- 如果玩家等待时间过长则返回 math.huge，
    -- 允许玩家与任何人进行匹配。
    local getRange = function(timeWaiting)
    	if timeWaiting < 10 then
    		return 100
    	elseif timeWaiting >=10 and timeWaiting < 20 then
    		return 200
    	elseif timeWaiting >=20 and timeWaiting <= 35 then
    		return 300
    	end
    	return math.huge
    end
    
    -- 为对战创建场所，并将两名玩家传送进去
    local startGame = function(playerAId, playerBId)
    	local message = ""
    	print("即将开始对战：" .. playerAId .. "对" .. playerBId)
    	
    	-- 获取两名玩家对象
    	local playerA = nil
    	local playerB = nil
    	for _, player in pairs(game.Players:GetPlayers()) do
    		if player.userId == playerAId then
    			playerA = player
    		end
    		if player.userId == playerBId then
    			playerB = player
    		end
    	end
    	
    	-- 创建竞技场场所并获取其 id
    	local arenaPlaceId = game:GetService("AssetService"):CreatePlaceAsync(
    		"Arena place for " .. playerA.Name .. " and " .. playerB.Name, arenaPlaceTemplateId)
    
    	-- 绑定 OnTeleport 事件至将会被先传送至场景的 playerA 。
    	-- 若传送成功则将 playerB 传送至同一实例
    	local connection = playerA.OnTeleport:connect(function(teleportState, placeId)
    		if teleportState == Enum.TeleportState.Started then
    			local teleportStarted = os.time()
    			-- 持续检查 playerA 是否到达其它实例。
    			while true do
    				local success, error, placeId, arenaInstanceId = teleportService:GetPlayerPlaceInstanceAsync(playerAId)
    				-- 如果 playerA 传送场所正确，则将 playerB 也传送至同一场景
    				if placeId == arenaPlaceId then
    					teleportService:TeleportToPlaceInstance(arenaPlaceId, arenaInstanceId, playerB)
    					return
    				end
    				wait()
    			end	
    		end
    	end)
    	wait(1)
    	
    	-- 传送 playerA 至竞技场
    	teleportService:Teleport(arenaPlaceId, playerA)
    end
    
    -- 匹配循环。每 5 秒左右进行循环，为玩家寻找匹配。
    while true do
    	local now = os.time()
    	-- 循环遍历队列，尝试寻找范围内的玩家
    	for _, mmData in pairs(matchMakingQueue) do
    		print("正在匹配。请稍候，" .. mmData.UserId)
    		-- 获取搜索的排名范围
    		local range = getRange(now - mmData.EnteredQueue)
    		-- 使用列表寻找符合排名范围的匹配玩家
    		local otherPlayerId = rankedList:FindPlayerInRange(mmData.UserId, range)
    		if otherPlayerId then
    			-- 找到了另一名玩家。将两位玩家从队伍中移除，
    			-- 防止其与其他玩家匹配
    			print("找到玩家：" .. otherPlayerId)
    			rankedList:RemovePlayer(mmData.UserId)
    			rankedList:RemovePlayer(otherPlayerId)
    			removeFromMMQueue(mmData.UserId)
    			removeFromMMQueue(otherPlayerId)
    			-- 为两名玩家开始游戏。该函数运行可能需要一段时间，
    			-- 请在新线程中生成该函数，以便循环继续。
    			local thread = coroutine.create(function() startGame(mmData.UserId, otherPlayerId) end)
    			coroutine.resume(thread)
    		end
    	end
    	wait(5)
    end
    

### 大厅链表模块
    
    
    -- 玩家匹配双链表模块
    local rankList = {}
    rankList.Top = nil
    rankList.Bottom = nil
    
    -- 将 userIds 连接到对应链表节点的字典，方便快速查找
    local keyTable = {}
    
    -- 在列表中的 oldNode 前插入 newNode 。如果 oldNode 在列表顶端则重新分配 rankList.Top
    function rankList:InsertBefore(newNode, oldNode)
    	if oldNode.Prev then
    		newNode.Prev = oldNode.Prev
    		oldNode.Prev.Next = newNode
    	end
    	newNode.Next = oldNode
    	oldNode.Prev = newNode
    	if rankList.Top == oldNode then
    		rankList.Top = newNode
    	end
    	return newNode
    end
    
    -- 从链表中移除节点。确保列表的 Top （顶部）和 Bottom （底部）都指向正确的节点。
    -- 同时从查找字典中移除节点
    function rankList:RemoveNode(node)
    	if node.Prev then
    		node.Prev.Next = node.Next
    		if rankList.Bottom == node then
    			rankList.Bottom = node.Prev
    		end
    	end
    	if node.Next then
    		node.Next.Prev = node.Prev
    		if rankList.Top == node then
    			rankList.Top = node.Next
    		end
    	end
    	keyTable[tostring(node.userId)] = nil
    end
    
    -- 添加玩家至列表。通过依照排名将玩家添加至列表的正确
    -- 位置来确保列表的排序无误。同时将玩家添加至查找字典
    function rankList:AddPlayer(userId, rank, startedWaiting)
    	local node = {UserId = userId, Rank = rank, Age = startedWaiting, Next = nil, Prev = nil}
    	keyTable[tostring(userId)] = node	
    	
    	-- 首先检查列表是否为空。如是则将列表的 Top （顶部）和 Bottom （底部）指向新增节点
    	if not rankList.Top then
    		rankList.Top = node
    		rankList.Bottom = node
    		return node
    	else
    		-- 如果列表非空，则寻找新增节点的添加位置。
    		-- 从 Top （顶部）节点开始，沿列表向下比较排名
    		local currentNode = rankList.Top
    		
    		while currentNode do
    			if currentNode.Rank	> rank then
    				return rankList:InsertBefore(node, currentNode)
    			end		
    			
    			currentNode = currentNode.Next
    		end
    		
    		-- 如果代码运行至此，则新增节点需要被添加至列表最后
    		rankList.Bottom.Next = node
    		node.Prev = rankList.Bottom
    		rankList.Bottom = node
    		return node
    	end
    end
    
    -- 将玩家从列表中移除
    function rankList:RemovePlayer(userId)
    	local playerNode = keyTable[tostring(userId)]
    	rankList:RemoveNode(playerNode)
    end
    
    -- FindPlayerInRangeWithNode 的私人搜索函数。可基于
    -- searchAscending 向列表的顶部或底部进行搜索
    local function Search(current, rank, searchAscending, range, oldestWait)
    	local retNode = nil	
    	while current do
    		if math.abs(rank - current.Rank) > range then
    			break
    		end		
    		if current.Age < oldestWait then
    			oldestWait = current.Age
    			retNode = current
    		end
    		if searchAscending then 
    			current = current.Next
    		else
    			current = current.Prev
    		end
    	end
    	return retNode, oldestWait
    end
    
    -- 返回处于 startNode 玩家排名范围内的玩家节点。
    -- 返回的玩家同时也是范围内等待时间最长的。
    function rankList:FindPlayerInRangeWithNode(startNode, range)
    	local oldestWait = math.huge
    	local rank = startNode.Rank
    	local current = startNode.Next
    	local retNode = nil
    	
    	retNode, oldestWait = Search(startNode.Next, startNode.Rank, true, range, oldestWait)
    	retNode, oldestWait = Search(startNode.Prev, startNode.Rank, false, range, oldestWait)
    	
    	return retNode
    end
    
    -- 返回在 userId 排名范围内找到玩家的用户 ID 。
    -- 若未找到玩家则返回 nil 。
    function rankList:FindPlayerInRange(userId, range)
    	local playerNode = keyTable[tostring(userId)]
    	if playerNode then
    		local otherPlayer = rankList:FindPlayerInRangeWithNode(playerNode, range)
    		if otherPlayer then 
    			return otherPlayer.UserId 
    		end
    	end
    	return nil
    end
    
    return rankList
    

### 大厅 LocalScript
    
    
    local button = script.Parent
    local lookForGameEvent = game.ReplicatedStorage.LookForGameEvent
    
    local lookForGameNextClick = true
    
    button.MouseButton1Click:connect(function()
    	if lookForGameNextClick then
    		button.Text = "正在寻找匹配。再次点击取消匹配"
    	else
    		button.Text = "寻找匹配。"
    	end
    	lookForGameEvent:FireServer(lookForGameNextClick)
    	lookForGameNextClick = not lookForGameNextClick
    	
    end)
    

### Arena （竞技场）脚本
    
    
    local players = {}
    local kfactor = 30
    local teleportService = game:GetService("TeleportService")
    local ratingData = game:GetService("DataStoreService"):GetDataStore("RatingData")
    local lobbyId = 181194460
    local playerHasDied = false
    
    -- 处理 PlayerAdded 事件，设置玩家表格
    game.Players.PlayerAdded:connect(function(player)
    	
    	-- 当玩家被击败时，需要更新玩家表格。同时也需要将
    	-- 全局变量 playerHasDied 设为 true 以结束对战游戏
    	player.CharacterAdded:connect(function(character)
    		character.Humanoid.Died:connect(function()
    			print(player.Name .. "已被击败")
    			players[tostring(player.userId)].Died = true
    			playerHasDied = true
    		end)
    	end)
    	
    	-- 从 DataStore 获取玩家排名，将玩家表格内的击败状态设为 false
    	print("正在获取玩家数据：" .. player.Name)
    	local playerData = {}
    	playerData.Rating = ratingData:GetAsync(tostring(player.userId)).Rating
    	playerData.Died = false
    	players[tostring(player.userId)] = playerData
    end)
    
    -- 使用 Elo 等级分制度计算每个玩家的排名变化
    local calculateRatingChange = function(playerA, playerB)
    	-- 从玩家表格获取每个玩家的排名
    	local playerARating = players[tostring(playerA.userId)].Rating
    	local playerBRating = players[tostring(playerB.userId)].Rating
    
    	-- 从玩家表格获取每个玩家的胜败
    	local playerADied = players[tostring(playerA.userId)].Died
    	local playerBDied = players[tostring(playerB.userId)].Died	
    	
    	-- 计算每个玩家的胜率。需要注意的是： expectedA + expectedB = 1
    	local expectedA = 1 / (1 + math.pow(10,(playerBRating - playerARating)/400))
    	local expectedB = 1 - expectedA
    	
    	-- 根据玩家对战结果计算分数。注意以下值：
    	-- 胜 = 1
    	-- 平 = .5
    	-- 败 = 0
    	-- 我们以 .5 开始（设想结果为平局）。如果玩家被击败则失去 .5 分数，
    	-- 胜利玩家获取 .5 分数
    	local scoreA = .5
    	local scoreB = .5
    	if playerADied then
    		scoreA = scoreA - .5
    		scoreB = scoreB + .5
    	end	
    	if playerBDied then
    		scoreA = scoreA + .5
    		scoreB = scoreB - .5
    	end
    	
    	-- 根据分数、胜率计算每个玩家的排名变化
    	-- 然后以 kfactor 对变化量加以限制
    	local playerAChange = kfactor * (scoreA - expectedA)
    	local playerBChange = kfactor * (scoreB - expectedB)
    	
    	return playerAChange, playerBChange
    end
    
    -- 用玩家的新排名值更新 DataStore
    local adjustPlayerRating = function(player, rankingChange)
    	ratingData:UpdateAsync(tostring(player.userId), function(oldValue)
    		local newValue = oldValue
    		newValue.Rating = newValue.Rating + rankingChange
    		return newValue
    	end)
    end
    
    -- 等待两名玩家就绪后再降低屏障
    print("正在等待玩家")
    while game.Players.NumPlayers < 2 do
    	wait()
    end
    print("玩家已就绪")
    
    -- 玩家进入游戏后，降低屏障
    for _, barrier in pairs(game.Workspace.Barriers:GetChildren()) do
    	barrier.CanCollide = false
    	barrier.Transparency = 1
    end
    
    print("正在等待玩家被击败")
    while not playerHasDied do
    	wait()
    end
    print("玩家已被击败！即将调整分数")
    
    -- 稍作等待，检查是否两人都被击败，以便算为平局
    wait(1)
    
    local playerA = nil
    local playerB = nil
    for _, player in pairs(game.Players:GetPlayers()) do
    	if playerA == nil then
    		playerA = player
    	else
    		playerB = player
    	end
    end
    
    -- 计算每个玩家的排名变化
    local playerAchange, playerBchange = calculateRatingChange(playerA, playerB)
    print("PlayerA points should change by " .. playerAchange)
    print("PlayerB points should change by " .. playerBchange)
    
    -- 修改每个玩家的点数与排名
    adjustPlayerRating(playerA, playerAchange)
    adjustPlayerRating(playerB, playerBchange)
    
    print("即将传送回大厅")
    wait(5)
    
    -- 将玩家传送回大厅
    for _, player in pairs(game.Players:GetPlayers()) do
    	teleportService:Teleport(lobbyId, player)
    end
    

## 示例场景

你可以在 Roblox 网站上查看本示例中编写的大厅与竞技场，其锁定复制选项都已禁用：

  * [大厅](https://www.roblox.com/Matchmaking-Lobby-place?id=181194460)
  * [竞技场](https://www.roblox.com/Matchmaking-Arena-place?id=181238621)



***__Roblox官方链接__:[玩家匹配系统](https://developer.roblox.com/zh-cn/articles/Matchmaking)