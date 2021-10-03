# 关于 GDPR 和 CCPA 
Time:<em>10  分钟</em>

##### 免责声明

本文档所包含的信息不构成法律意见。如果你有任何问题或疑虑，我们鼓励你**咨询律师**。Roblox 不会也无法充当你的律师，Roblox 不承担由于此类信息引发的任何责任或费用。

  


## GDPR 是什么？

GDPR 是 **General Data Protection Regulation** 《通用数据保护条例》的简称。GDPR 是欧盟的一项法律，其重点是保护欧盟和欧洲经济区内每个人的个人信息、保障他们个人信息的收集、使用和共享的具体权利。这些权利放之四海而皆准，因此，许多收集欧盟成员国内民众个人信息的公司或个人都受 GDPR 的约束。

## CCPA 是什么？

CCPA 是 **California Consumer Privacy Act** 《加州消费者隐私法》的简称，**2020 年 1 月 1 日**生效。该法案规定了居住在美国加利福尼亚州的消费者的权利，包括有权知悉他们有哪些信息被收集走、要求企业删除任何关于消费者的个人信息，以及如果消费者行使隐私权，企业不得对其区别对待。

##### 什么是个人信息？

大多数人将术语“个人信息”或“个人身份信息”（Personally Identifiable Information，简称 PII）与姓名、电子邮件地址或家庭地址等数据联系在一起。然而，GDPR 和 CCPA 对个人信息有更广泛的定义，这些信息也可以涵盖不直接链接到特定个人的信息，如用户的 ID 或 IP 地址。

一般来说，开发者收集的个人信息**不应该**多于 Roblox 提供的信息，如玩家的 ID 和用户名等。如需了解更多有关信息，请参见我们的[社区规则](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Rules)。

  


## 对开发者的影响

作为一名开发者，尊重并履行 GDPR 及 CCPA 的方式有：

  * 您可能会收到 Roblox 发来的关于**要求删除个人信息**的消息。Roblox 会特别注意核实这些请求，以确保其合法性。您应**只接受来自 Roblox 的相应要求**。如果有玩家先与您联系，请让他/她在 <https://www.roblox.com/support> 提出申请。
  * 除了用户 ID 和用户名外，**不要**存储其他形式的个人信息（例如出生日期或个人照片等）。
  * 如果您已经存储了 Roblox 提供的访问权限之外的其他个人信息，请将其删除并更新您的游戏，以便将来不再存储这些数据。

## 移除个人信息

如果** Roblox要求您**删除某个行使 GDPR 或 CCPA 规定权利的个人的信息，您可能需要从游戏中的`articles/Data store|数据存储`中删除特定数据。在数据存储中识别 Roblox 用户的一个常见模式是通过其唯一的 `Player/UserId|UserId` 前缀 Player_ 来识别 Roblox 用户，例如 Player_12345678。要创建一个删除玩家数据的控制台命令脚本，请按照以下步骤执行。

请注意，这些步骤基于[示例场景](https://www.roblox.com/games/3752087252/Data-Removal)所使用的数据存储。开发者可以按照步骤理解模式，但您的游戏可能使用了不同的数据设置，需要进行改动。 

  1. 打开游戏的起始场景。
  2. 在 **ServerStorage** 中创建一个 `BindableEvent` 并将其重命名为 **RemovePlayerData**。
![](https://developer.roblox.com/assets/blt84f22b9574bfa731/Data-Removal-BindableEvent.png)



  3. 在 **ServerScriptService** 中创建一个新的 `Script` 并将其重命名为 **ConsoleEvent**。
![](https://developer.roblox.com/assets/blt2d4e580a931c2751/Data-Removal-ConsoleEvent.png)



  4. 将下面的代码复制到新脚本中。注意，想要从数据存储中移除键值，需使用 `GlobalDataStore/RemoveAsync|RemoveAsync()`（第 13 行）方法。

```    
    
    local ServerStorage = game:GetService("ServerStorage")
    local DataStoreService = game:GetService("DataStoreService")
    local removePlayerDataEvent = ServerStorage:WaitForChild("RemovePlayerData")
    
    -- 玩家数据存储的引用（将 "PlayerData" 替换为你的数据存储的名称）
    local playerData = DataStoreService:GetDataStore("PlayerData")
    
    local function onRemovePlayerDataEvent(userID)
    	-- 玩家数据存储键值的模式，如 "Player_12345678"
    	local dataStoreKey = "Player_" .. userID
    
    	local success, err = pcall(function()
    		return playerData:RemoveAsync(dataStoreKey)
    	end)
    	if success then
    		warn("Removed player data for user ID '" .. userID .. "'")
    	else
    		warn(err)
    	end
    end
    removePlayerDataEvent.Event:Connect(onRemovePlayerDataEvent)


```
请记住， 这个脚本默认名为 **PlayerData** 的数据存储存在， 其数据键的格式为 Player_XXXXXXXX， 其中 XXXXXXXX 是用户的唯一 Roblox ID。如果你的游戏数据存储的命名方式不同、或者数据键的格式不同，您需要调整第 6 行和第 10 行。 

  5. 发布场景，然后在 Roblox **客户端**（而非 Studio）中运行场景。
  6. 进入游戏后，打开 `/articles/Developer Console|Developer Console`（开发者控制台），方式为点击 F9 或在聊天中输入 `/console` 。
  7. 在 **Log** 区中点击 **Server** 选项卡。
![](https://developer.roblox.com/assets/blt8526a8311943cd23/Developer-Console-Server-Tab.png)



  8. 在控制台的**命令行**中输入以下命令，其中 XXXXXXXX 是 Roblox 提供给您的用户 ID。

game.ServerStorage.RemovePlayerData:Fire("XXXXXXXX")

![](https://developer.roblox.com/assets/blt4718c74ed2ae2e6c/Developer-Console-Command-Line.png)



如果玩家数据键的为 Player_XXXXXXXX 模式，控制台将会显示消息，提醒开发者已成功从数据存储中删除玩家数据：

![](https://developer.roblox.com/assets/blt8122e7ff80dfc18d/Developer-Console-Output.png)





***__Roblox官方链接__:[关于 GDPR 和 CCPA](https://developer.roblox.com/zh-cn/articles/managing-personal-information)