# 设计多人游戏 
Time:<em>10  分钟</em>

作为社交平台，Roblox 上最成功的游戏都利用了促进玩家之间进行有意义的互动的机制。通过特定的设计选择来鼓励社交游戏，开发者将可以大幅提升玩家的参与度和留存度，以及游戏利润。

## 设计选择

### 平衡世界尺寸

考虑游戏世界的尺寸与最大玩家数量。少数玩家在巨大的地图上会让人感觉游戏人数稀少，而拥挤的大厅则会让人觉得不适。

以下是一些平衡地图尺寸与玩家数量的技巧：

  * 在较大的地图上创造关键点来聚集玩家，例如 FPS 中重要的 NPC 商店或建筑。
  * 使用头目战或假日挑战之类的社区活动将大量玩家聚集到一起。
  * 在开发过程中，以不同的玩家数量进行游戏测试，直到空间与玩家数量达到理想的比例。

### 考虑游戏类型

根据游戏类型，开发者可以用不同的方式设计环境。以角色扮演游戏 [Welcome to Bloxburg（欢迎来到方块堡）](https://www.roblox.com/games/185655149)为例，其环境设计中包含了多种用途的玩家聚集中心，让玩家可以去上班、购车及在饭店、俱乐部或者家庭聚会中社交。大地图并不是问题，因为玩家会聚集在这些社交中心。相比之下，[Phantom Forces（幻影力量）](https://www.roblox.com/games/292439477)这样的竞技类战斗游戏将地图设计得较小，以迫使玩家之间频繁交战。

![](https://developer.roblox.com/assets/bltefce3ee46dbbbfa7/bloxburg.png)

 [欢迎来到方块堡](https://www.roblox.com/games/185655149) 作者：[Coeptus](https://www.roblox.com/users/63700903/profile)

![](https://developer.roblox.com/assets/blt7475ca5da83d057c/phantom_forces_ds.png)

 [幻影力量](https://www.roblox.com/games/292439477) 作者：[StyLiS Studios](https://www.roblox.com/groups/group.aspx?gid=1103278)

### 避免分裂玩家基数

以多种游戏模式发布游戏时，可能带有分裂玩家基数的风险。例如，如果游戏是大逃杀类，在玩家基数足够多之前请考虑发布一个“小队”模式。一旦开发者认为游戏已有足够多的玩家，即使分段也不会影响服务器上的玩家数量，再考虑加入单人游戏等更多模式。

### 提供登录奖励

维持健康而稳固的社区的方法之一，是确保玩家经常返回。在 Roblox 中一种常见的办法是提供登录奖励，例如`/articles/Developer Products In Game Purchases|游戏内物品`或`/articles/Badges Special Game Awards|徽章`等。只要玩家为获取奖励而返回，游戏就会成为他们日常习惯的一部分，使其维持一定的活跃玩家基数。

可激励奖励的方式包括：

  * 如果玩家连续多天登陆可获得比普通奖励更好的奖励。例如，角色扮演游戏 [Adopt Me!（领养我！）](https://www.roblox.com/games/920587237)为每天登录的玩家提供游戏内货币，并在连续五天后提供一份神秘礼物。
  * 提供认可玩家连续登陆的方式，例如奖励专属的外观物品。这会提醒其他玩家连续登陆奖励的价值。

## 社交功能

友谊和社区可提高玩家的留存度与参与度。虽然 Roblox 包含诸如游戏内聊天和好友系统这样的功能，您也可以用特定的社交功能来增强游戏。

### 提示好友互相加入

Roblox 提供 `SocialService` 函数，让玩家可以邀请好友加入其当前的游戏服务器。

![](https://developer.roblox.com/assets/blt68abe5b46fb198c0/InviteFlow1.jpg)

以下代码示例演示如何使用 `SocialService` API 实现此功能：

发送游戏邀请 ```    
    
    local SocialService = game:GetService("SocialService")
    local Players = game:GetService("Players")
    local player = Players.LocalPlayer
    
    local function canSendGameInvite(targetPlayer)
    	local res, canSend = pcall(SocialService:CanSendGameInvite(targetPlayer))
    	return res and canSend
    end
    
    local function promptGameInvite(targetPlayer)
    	local res, canInvite = pcall(SocialService:PromptGameInvite(targetPlayer))
    	return res and canInvite
    end
    
    local function openGameInvitePrompt(targetPlayer)
    	local canInvite = canSendGameInvite(targetPlayer)
    	if canInvite then
    		local promptOpened = promptGameInvite(targetPlayer)
    		return promptOpened
    	end
    	return false
    end
    
    local function invitePromptClosed(senderPlayer, recipientIds)
    	-- 处理被发送者邀请的玩家的自定义逻辑
    end
    
    local function inputBegan(input, gameProcessed)
    	local inputType = input.UserInputType
    	local touch = Enum.UserInputType.Touch
    	local mouse1 = Enum.UserInputType.MouseButton1
    
    	if inputType == touch or inputType == mouse1 then
    		openGameInvitePrompt(player)
    	end
    end
    
    script.Parent.InputBegan:Connect(inputBegan)
    SocialService.GameInvitePromptClosed:Connect(invitePromptClosed)


```
要使此代码示例生效，必须将其置于 `GuiButton` 下的一个 `LocalScript` 中。当玩家激活按钮时，它将执行 `openGameInvitePrompt()` 函数，检查是否可以通过 `SocialService/CanSendGameInviteAsync|CanSendGameInviteAsync()` 发送游戏邀请。然后它将用 `SocialService/PromptGameInvite|PromptGameInvite()` 打开邀请提示。

### 凝聚玩家

通过添加凝聚玩家的系统来鼓励自然的社交互动。这可以是一个需要不止一位玩家参与的挑战，例如战斗游戏中的头目战，或社交游戏中的电影剧院。

### 在游戏内庆祝玩家的成功

认可玩家在游戏内的成就不仅奖励其个人，也会引起讨论或激励其他玩家追求该奖励。例如：

  * 给获得奖励的玩家加上临时粒子效果。
  * 向大厅里的全体玩家广播一条消息。
  * 使用排行榜来展示玩家的成就。

[Egg Farm Simulator（鸡蛋农场模拟器）](https://www.roblox.com/games/1828509885)就是一个认可玩家成就的例子。它包含一个排行榜，策略性地置于游戏区域的中央，以便展示最专注的玩家的成就。

## 更多资源

  * [社交游戏的社交机制](https://www.gdcvault.com/play/1014555/Social-Mechanics-for-Social-Games)
  * [经典社交机制：多人游戏背后的引擎](https://www.gdcvault.com/play/1013827/Classic-Social-Mechanics-The-Engines)



***__Roblox官方链接__:[设计多人游戏](https://developer.roblox.com/zh-cn/articles/designing-for-multiplayer)