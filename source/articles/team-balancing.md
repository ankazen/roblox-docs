# 平衡团队构成 
Time:<em>5  分钟</em>

![](https://developer.roblox.com/assets/blt506c733356766e41/Team-Balancing-Hero.jpg)

通过将游戏中互加好友的玩家放入同一队伍并确保双方队伍的平衡，可以保证所有玩家都能享受到公平健康的游戏氛围。向游戏添加保持团队平衡的代码后，公平竞争的玩家们会逐渐发展友谊，从而在你的游戏中投入更多的时间。

如果想要实现本文中的代码示例，建议对 Lua `/articles/Table|table（表）` 和 Roblox 的 `BindableEvent|BindableEvent` 有一定了解。 

本文中的脚本并不会为游戏自动添加/设置团队。如果对设置团队尚不了解，请参见`/articles/Player Spawns and Teams|玩家生成和团队`一文。 

## 将好友玩家成组分配

如果想要追踪一组好友玩家，需要先在 `ServerScriptService` 中包括 `Script`。在该脚本的代码中，首先需要添加查看游戏中是否有好友的函数，然后将其连接至 `Players/PlayerAdded` 事件。

ServerScriptService 中的 Script ```    
    
    local friendGroups = {}
    
    -- 将好友加入同一群组，以便其加入同一团队
    local function groupFriends(player)
    	local mutualGroups = {}
    
    	-- 对好友群组进行迭代
    	for groupIndex, group in ipairs(friendGroups) do
    		-- 对群组中发现的好友进行迭代
    		for _, user in ipairs(group) do
    			-- 将共同好友放入一个群组中
    			if player:IsFriendsWith(user.UserId) then
    				if (mutualGroups[group] == nil) then
    					table.insert(mutualGroups, groupIndex)
    				end
    			end
    		end
    	end
    
    	if #mutualGroups > 0 then
    		local groupIndex = mutualGroups[1]
     
    		-- 如果玩家拥有多个正在进行游戏的好友群组，则将其合并为一个群组
    		if #mutualGroups > 1 then
    			groupIndex = mergeGroups(mutualGroups)
    		end
     
    		table.insert(friendGroups[groupIndex], player)
    		assignInitialTeam(player, friendGroups[groupIndex])
    	else
    		table.insert(friendGroups, {player})
    		assignInitialTeam(player)
    	end
    end
    
    -- 将 "PlayerAdded" 事件连接至 "groupFriends()" 函数
    game.Players.PlayerAdded:Connect(groupFriends)


```
此段代码的作用如下：

  1. 第一行的 `friendGroups` 表将会储存至少拥有一个共同好友的多个玩家列表。
  2. 在查找进入游戏的玩家是否有好友在游戏内时，将会使用 `Player/IsFriendsWith|Player:IsFriendsWith()` 对 `friendGroups` 内各个群组的玩家进行查询。包含进入游戏玩家一名以上好友的群组将会被存储在 `mutualGroups` 表内。
  3. 如果找到了多个拥有好友的群组，则首先会将这些群组通过 `mergeGroups()` 辅助函数（在下文合并好友群组章节中进行了定义），然后玩家将会被分配至该群组。如果没有发现任何好友，则玩家将会被分配至新的群组。
  4. 当玩家与其线上好友进行分组后，使用辅助函数 `assignInitialTeam()` （在下文分配玩家团队章节中进行了定义）将其分配至团队中。

### 合并好友群组

如果想要将多个含有共同好友的群组合并为一个更大的群组，请直接在 `groupFriends()` 函数上方添加下列 `mergeGroups()` 辅助函数。该函数将会查看拥有共同好友的群组，对其进行合并，移除旧的群组，然后将合并过的群组返回至 `groupFriends()` 函数。

```    
    
    -- 将所有拥有共同好友的群组合并至一个群组
    local function mergeGroups(groups)
    	-- 将其它群组的成员添加至第一个群组
    	for i = 2, #groups do
    		for _, user in pairs(friendGroups[groups[i]]) do
    			table.insert(friendGroups[groups[1]], user)
    		end
    		-- 移除合并后的废弃群组
    		table.remove(friendGroups, groups[i])
    	end
    
    	return groups[1]
    end


```
### 分配玩家团队

如果玩家与好友共同游戏，开始时应该将其放入同一团队中。为了达成此目的，应当：

  1. 获取 `TeamService` 并与游戏团队交互。建议将服务放在脚本的最顶端。

```    
    
    local TeamsService = game:GetService("Teams")
    
    local friendGroups = {}


```
  2. 在 `mergeGroups()` 函数下添加名为 `assignInitialTeam()` 的函数，其作用为接收玩家及其可能加入群组的参数。如果函数收到了群组参数且群组人数不会因过大而造成游戏不平衡，则好友群组中第一条目的 `Player/Team` 属性将会被用来分配团队。如果没有收到群组参数，则玩家将填入人数最少的团队。

```    
    
    -- 当玩家加入游戏时，决定其应当加入的团队
    local function assignInitialTeam(player, group)
    	-- 检查玩家是否属于任何群组且该群组是否并未超过公平团队人数
    	if group and #group < game.Players.MaxPlayers / 2 then
    		player.Team = group[1].Team
    	else
    		local teams = TeamsService:GetTeams()
    		table.sort(teams, function(a, b) return #a:GetPlayers() < #b:GetPlayers() end)
    		player.Team = teams[1]
    	end
    end


```
## 处理玩家退出

当玩家离开游戏后，需要将其从 `friendGroups` 表中移除，否则游戏将会认为好友群组比实际上的人数要多。

如果想要移除玩家的条目，需要对 `friendGroups` 进行迭代，寻找与该玩家相符的用户，并将该玩家的当前索引设为 `nil`。如果玩家之前的群组为空，则将群组也设为 `nil` 。最后需要确保将函数连接至 `Players/PlayerRemoving` 事件。

```    
    
    -- 当玩家离开游戏时，清除其群组
    local function removeFromGroup(player)
    	-- 对好友群组进行循环，找到玩家
    	for groupIndex, group in ipairs(friendGroups) do
    		for userIndex, user in ipairs(group) do
    			if user.Name == player.Name then
    				-- 将其从之前加入的群组中移除
    				friendGroups[groupIndex][userIndex] = nil
    				-- 如果群组为空，则将其进行移除
    				if #friendGroups[groupIndex] == 0 then
    					friendGroups[groupIndex] = nil
    				end
    			end
    		end
    	end
    end
    
    -- 将 "PlayerRemoving" 事件连接至 "removeFromGroup()" 函数
    game.Players.PlayerRemoving:Connect(removeFromGroup)
    
    -- 将 "PlayerAdded" 事件连接至 "groupFriends()" 函数
    game.Players.PlayerAdded:Connect(groupFriends)


```
## 重新平衡团队

决定好友群组之后，在 `ReplicatedStorage` 内添加 `BindableEvent`，以供需要测试及重新平衡时使用。按照 Roblox 传统，将此代码置于脚本顶部。

```    
    
    local TeamsService = game:GetService("Teams")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    local balanceTeamsEvent = Instance.new("BindableEvent")
    balanceTeamsEvent.Name = "BalanceTeamsEvent"
    balanceTeamsEvent.Parent = ReplicatedStorage
    
    local friendGroups = {}


```
接下来，为了保证各团队分配到人数大致相当的好友群组并保持平衡，在 `removeFromGroup()` 下方添加下列 `balanceTeams()` 函数：

```    
    
    local function balanceTeams()
    	local teams = TeamsService:GetTeams()
    
    	-- 对群组进行排序，将更大的群组放在前面
    	table.sort(friendGroups, function(a, b) return #a > #b end)
    
    	-- 迭代好友群组（已经将其按从大到小进行排序）
    	for i = 1, #friendGroups do
    		-- 如果群组过大，则将其分开放入两个团队中
    		if (#friendGroups[i] > game.Players.MaxPlayers / 2) then
    			for _, player in pairs(friendGroups[i]) do
    				table.sort(teams, function(a, b) return #a:GetPlayers() < #b:GetPlayers() end)
    				player.Team = teams[1]
    			end
    		else
    			-- 对团队列表进行排序，最小的团队放在最前
    			table.sort(teams, function(a, b) return #a:GetPlayers() < #b:GetPlayers() end)
    			local groupTeam = teams[1]
    
    			-- 将群组中的所有人放入同一团队
    			for _, player in pairs(friendGroups[i]) do
    				player.Team = groupTeam
    			end
    		end
    	end
    end


```
此函数的作用如下：

  1. 为了保证各团队分配到人数大致相当的好友群组并保持团队平衡，将各 `friendGroups` 按照从大到小进行排序（第 90 行）。
  2. 排序之后，再次对 `friendGroups` 进行迭代。如果任何群组人数大于游戏 `Players/MaxPlayers` 值的一半，则会将该群组内好友分开并分配至人数更少的团队。如果人数小于该值一半，则将会对团队进行升序排序后将该群组分配至最小团队中去。

现在将 `BalanceTeamsEvent` 可绑定`BindableEvent/Event|事件`连接至 `balanceTeams()` 函数，在想要对团队进行重新平衡时`BindableEvent/Fire|触发`该事件即可。建议在两场比赛间触发事件，但也可以自行决定团队平衡的触发条件。

```    
    
    -- 将 "PlayerRemoving" 事件连接至 "removeFromGroup()" 函数
    game.Players.PlayerRemoving:Connect(removeFromGroup)
    
    -- 将 "PlayerAdded" 事件连接至 "groupFriends()" 函数
    game.Players.PlayerAdded:Connect(groupFriends)
    
    balanceTeamsEvent.Event:Connect(balanceTeams)


```
## 完整的脚本

```    
    
    local TeamsService = game:GetService("Teams")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    local balanceTeamsEvent = Instance.new("BindableEvent")
    balanceTeamsEvent.Name = "BalanceTeamsEvent"
    balanceTeamsEvent.Parent = ReplicatedStorage
    
    local friendGroups = {}
    
    -- 将所有拥有共同好友的群组合并至一个群组
    local function mergeGroups(groups)
    	-- 将其它群组的成员添加至第一个群组
    	for i = 2, #groups do
    		for _, user in pairs(friendGroups[groups[i]]) do
    			table.insert(friendGroups[groups[1]], user)
    		end
    		-- 移除合并后的废弃群组
    		table.remove(friendGroups, groups[i])
    	end
     
    	return groups[1]
    end
    
    -- 当玩家加入游戏时，决定其应当加入的团队
    local function assignInitialTeam(player, group)
    	-- 检查玩家是否属于任何群组且该群组是否并未超过公平团队人数
    	if group and #group < game.Players.MaxPlayers / 2 then
    		player.Team = group[1].Team
    	else
    		local teams = TeamsService:GetTeams()
    		table.sort(teams, function(a, b) return #a:GetPlayers() < #b:GetPlayers() end)
    		player.Team = teams[1]
    	end
    end
    
    -- 将好友加入同一群组，以便其加入同一团队
    local function groupFriends(player)
    	local mutualGroups = {}
    
    	-- 对好友群组进行迭代
    	for groupIndex, group in ipairs(friendGroups) do
    		-- 对群组中发现的好友进行迭代
    		for _, user in ipairs(group) do
    			-- 将共同好友放入一个群组中
    			if player:IsFriendsWith(user.UserId) then
    				if (mutualGroups[group] == nil) then
    					table.insert(mutualGroups, groupIndex)
    				end
    			end
    		end
    	end
     
    	if #mutualGroups > 0 then
    		local groupIndex = mutualGroups[1]
     
    		-- 如果玩家拥有多个正在进行游戏的好友群组，则将其合并为一个群组
    		if #mutualGroups > 1 then
    			groupIndex = mergeGroups(mutualGroups)
    		end
     
    		table.insert(friendGroups[groupIndex], player)
    		assignInitialTeam(player, friendGroups[groupIndex])
    	else
    		table.insert(friendGroups, {player})
    		assignInitialTeam(player)
    	end
    end
    
    -- 当玩家离开游戏时，清除其群组
    local function removeFromGroup(player)
    	-- 对好友群组进行循环，找到玩家
    	for groupIndex, group in ipairs(friendGroups) do
    		for userIndex, user in ipairs(group) do
    			if user.Name == player.Name then
    				-- 将其从之前加入的群组中移除
    				friendGroups[groupIndex][userIndex] = nil
    				-- 如果群组为空，则将其进行移除
    				if #friendGroups[groupIndex] == 0 then
    					friendGroups[groupIndex] = nil
    				end
    			end
    		end
    	end
    end
    
    local function balanceTeams()
    	local teams = TeamsService:GetTeams()
    
    	-- 对群组进行排序，将更大的群组放在前面
    	table.sort(friendGroups, function(a, b) return #a > #b end)
    
    	-- 迭代好友群组（已经将其按从大到小进行排序）
    	for i = 1, #friendGroups do
    		-- 如果群组过大，则将其分开放入两个团队中
    		if (#friendGroups[i] > game.Players.MaxPlayers / 2) then
    			for _, player in pairs(friendGroups[i]) do
    				table.sort(teams, function(a, b) return #a:GetPlayers() < #b:GetPlayers() end)
    				player.Team = teams[1]
    			end
    		else
    			-- 对团队列表进行排序，最小的团队放在最前
    			table.sort(teams, function(a, b) return #a:GetPlayers() < #b:GetPlayers() end)
    			local groupTeam = teams[1]
    
    			-- 将群组中的所有人放入同一团队
    			for _, player in pairs(friendGroups[i]) do
    				player.Team = groupTeam
    			end
    		end
    	end
    end
    
    -- 将 "PlayerRemoving" 事件连接至 "removeFromGroup()" 函数
    game.Players.PlayerRemoving:Connect(removeFromGroup)
    
    -- 将 "PlayerAdded" 事件连接至 "groupFriends()" 函数
    game.Players.PlayerAdded:Connect(groupFriends)
    
    balanceTeamsEvent.Event:Connect(balanceTeams)


```


***__Roblox官方链接__:[平衡团队构成](https://developer.roblox.com/zh-cn/articles/team-balancing)