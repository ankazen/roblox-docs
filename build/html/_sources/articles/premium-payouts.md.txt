# Premium 收益系统 
Time:<em>5  分钟</em>

![](https://developer.roblox.com/assets/blt36e71900f6ebf19e/Premium-Banner.jpg)

**Premium Payout**（Premium 收益系统）为通过游戏对玩家的吸引度决定开发者 Robux 游戏收益的系统。Premium Player Playtime（Premium 玩家游戏时间）作为决定玩家在游戏中所花费时间的代理度量，用于计算开发者 Robux 收益。开发者无需进行任何登记手续加入 Premium 收益系统，整个系统将会自动操作，且此系统收入独立于`articles/Game Passes One Time Purchases|游戏通行证`及`articles/Developer Products In Game Purchases|开发者产品`等其他系统所带来的收入。

为了保证 Premium 会员的游戏体验，Premium 收益系统不适用于 Paid Access（付费访问）游戏。 

## 鼓励玩家购买 Premium 会员

游戏所能吸引的玩家越多，玩家中的 Premium 用户也就越多，因此开发者也就能够从 Premium 收益系统中获取更多利润。通过在游戏中添加 Premium 购买模式窗口可以让非 Premium 玩家更为轻松地升级会员资格。

##### Premium 购买 — 最佳实践

When implementing Premium purchasing, strongly consider the following:

#### Avoid Paywalls

Do not present the modal as a "paywall" when players enter the game. This type of aggressive selling irritates most players and some may not return to play your game. 

#### Be Honest and Accurate

To improve buyer confidence and trust, clearly describe the benefits of upgrading, both in-game and in your game's description. **Do not promise benefits like Robux or other out-of-game rewards that you do not control.**

#### Avoid Pay-to-Win Upgrades

Do not give Premium members a tactical gameplay advantage over others, such as an array of ultra-powerful weapons that non-Premium players can't compete against. 

  


## 查看 Premium 数据

若想查看游戏中特定场景的 Premium 收益系统数据，请前往该场景的主页面并单击 ![](https://developer.roblox.com/assets/blt738fe32bb9c285f9/Config-Dots.png)

 按钮，从弹出菜单中选择 **Developer Stats**（开发者数据）。单击数据页面中的 **Premium** 选项卡查看各种数据图表。

![](https://developer.roblox.com/assets/blt81763f7cb93478ba/Open-Developer-Stats.png)

 ![](https://developer.roblox.com/assets/bltf2682631cd3c7e36/Developer-Stats-Premium-Tab.png)



### Premium Payout（Premium 收益系统）

该图表将会根据下列度量标准跟踪 Premium 收益系统的运作情况。

![](https://developer.roblox.com/assets/blt8429608ca7aac7e6/Premium-Data-Payout.png)



![](https://developer.roblox.com/assets/blt5b737b404b533d8a/Premium-Payouts-Chart-Score.png)



**Premium Playtime Score**（Premium 游戏时间评分）：此数值基于给定日期 Premium 用户在该游戏中的游戏时间。此度量在评估新添加游戏功能对游戏的即时影响或 Premium 用户在游戏中花费的时长时非常有效。 

![](https://developer.roblox.com/assets/blte89355bd23e7f499/Premium-Payouts-Chart-Robux.png)



**Premium Playtime Robux Earned**（Premium 游戏时间的 Robux 收益）：此数值能够直观地反映出 Premium 玩家参与度将为开发者带来的 Robux 收益。需要注意的是，此数值并非直接基于每日 Premium 玩家在游戏中所花费的时间，而是对过去 28 天内个体玩家行为进行统计后得出的结果。因此该指标和 Premium Playtime Score（Premium 游戏时间评分）并无数学上的直接关系，但其在图表上的行进趋势大体相似。无论游戏大小，每单元 Premium 游戏时间所奖励的 Robux 都是相同的。 

注意：当每日具体收益数目确定完毕后，加点的 “Projected Earnings”（预估收益）线将会用实线表示。届时收益金额将会被整合入位于[此处](https://www.roblox.com/My/Money.aspx#/#Summary_tab)的 **Pending Robux**（待支付 Robux）额度。 

### Premium Visits（Premium 用户访问量）

此图表展示了 Premium 会员对游戏的访问量，其中包括 **Premium Visit Percentage**（Premium 访问量占比）、**Premium Visits**（Premium 用户访问量）及 **Total Visits**（总用户访问量）。

![](https://developer.roblox.com/assets/blt97b4472997d9b673/Premium-Data-Visits.png)



## 为 Premium 会员编写脚本

### 检查会员资格等级

若想检查给定玩家的 Premium 订阅情况，请检查其 `Player/MembershipType|MembershipType` 属性。举例来说，下列代码片段可被放入解锁 Premium 限定商店物品的 `LocalScript` 中。如果玩家尚未购买 Premium 会员，同时也可为其触发购买模式界面，鼓励玩家订阅 Premium 会员。

检查玩家的会员资格状态 ```    
    
    local Players = game:GetService("Players")
    local player = Players.LocalPlayer
    
    if player.MembershipType == Enum.MembershipType.Premium then
    	-- 采取一些专门针对 Premium 会员的操作
    
    end


```
### Premium Purchase Modal（Premium 购买模式窗口）

开发者可以使用 **Premium 购买模式窗口**鼓励玩家购买 Premium 会员资格，整个购买流程都可以在游戏中完成。当玩家完成会员资格购买后，将会获取 Premium 身份及相应的 Robux 数额。

![](https://developer.roblox.com/assets/blt621af438e478bb7a/Premium-Modal-Example.jpg)

若想触发此模式窗口，请使用 `MarketplaceService/PromptPremiumPurchase|PromptPremiumPurchase()` 方法。当用户的虚拟角色接触包含此 `Script` 的部件时，下列代码将会提示用户购买 Premium 会员。举例来说，此代码可应用在访问 Premium 限定区域的传送器上。

提示购买 Premium 会员 ```    
    
    local MarketplaceService = game:GetService("MarketplaceService")
    local TeleportService = game:GetService("TeleportService")
    local Players = game:GetService("Players")
    
    local teleporter = script.Parent
    local showPrompt = true
    
    local placeID_Premium = 012345678
    
    local function onTeleporterTouch(otherPart)
    
    	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
    	if not player then return end
    
    	-- 如果用户已经拥有了 Premium 权限，直接将其传送至 Premium 限定场景
    	if player.MembershipType == Enum.MembershipType.Premium then
    		TeleportService:Teleport(placeID_Premium, player)
    	-- 否则提示用户购买 Premium 升级(使用 debounce 来让该通知在一段时间内只显示一次)
    	else
    		if showPrompt == false then return end
    		showPrompt = false
    		delay(5, function()
    			showPrompt = true
    		end)
    		MarketplaceService:PromptPremiumPurchase(player)
    		warn("Prompted Premium purchase")
    	end
    end
    teleporter.Touched:Connect(onTeleporterTouch)
    
    -- 如有必要可以使用这一事件来获知 Premium 模式窗口的关闭时间
    MarketplaceService.PromptPremiumPurchaseFinished:Connect(function(player)
    	warn("Premium modal closed")
    end)
    
    -- 处理用户在游戏过程中可能从游戏外购买 Premium 的情况
    Players.PlayerMembershipChanged:Connect(function(player)
    	warn("Player membership changed; new membership is " .. tostring(player.MembershipType))
    	if player.MembershipType == Enum.MembershipType.Premium then
    		-- 传送玩家至 Premium 限定区域
    		TeleportService:Teleport(placeID_Premium, player)
    	end
    end)


```


***__Roblox官方链接__:[Premium 收益系统](https://developer.roblox.com/zh-cn/articles/premium-payouts)