# 虚拟形象观察菜单 
Time:<em>5  分钟</em>

Roblox 提供的虚拟形象**观察菜单**，让玩家可以查看其他玩家所装备的物品。他们可以在菜单中查看到物品的详细信息、试穿或收藏该物品，甚至直接购买。和其他游戏内佣金一样，每笔通过观察菜单进行的购买，开发者都可以获得 10% 的佣金。

![](https://developer.roblox.com/assets/blt7aad8701a9041ab2/Inspect-Menu-Example.png)



注意**限量物品**不能通过观察菜单购买，因为我们希望用户在购买前能够多查看不同贩售者的情况。此外，目前动画也不能通过菜单”试穿“。 

## 访问观察菜单

观察菜单默认有三种访问方式：

  * 打开游戏的 ![](https://developer.roblox.com/assets/blte9c6314adf2dca29/Hamburger-Menu-Icon.png)

 菜单，然后在**玩家**标签中点击一个玩家旁边的**查看**按钮。
  * 在玩家列表（游戏视窗的右上方）中点击一个玩家的名字。
  * 作为`articles/Avatar Context Menu|虚拟形象菜单`中的一个选项。该菜单是一个可选功能，可辅助玩家与玩家的社交互动。

此外，观察菜单还可以通过 API 调用显式打开，具体如下。

## 查看游戏内物品

默认情况下，观察菜单显示的信息与玩家个人资料页面的“当前佩戴”选项卡相同，但这与他们在游戏中的外观**不一定**相同，因为您可能设置了在游戏中强制执行/装备指定的虚拟形象物品。

要查看某玩家在**游戏中**装备的物品，您可以：

  1. 以 `false` 调用 `GuiService/SetInspectMenuEnabled|GuiService:SetInspectMenuEnabled()`，以禁用默认的基于资料的观察菜单。
  2. 调用 `GuiService/InspectPlayerFromHumanoidDescription|GuiService:InspectPlayerFromHumanoidDescription()`，得到一个代表玩家穿着的 `HumanoidDescription` 以及唯一的**玩家名称**以供查看。

```    
    
    local GuiService = game:GetService("GuiService")
    local Players = game:GetService("Players")
    local player = Players.LocalPlayer
    
    -- 禁用基于资料的观察菜单
    GuiService:SetInspectMenuEnabled(false)
    
    local humanoid = player.Character and player.Character:FindFirstChild("Humanoid")
    if humanoid then
    	local humanoidDescription = humanoid:GetAppliedDescription()
    	GuiService:InspectPlayerFromHumanoidDescription(humanoidDescription, player.Name)
    end


```
## 查看其它玩家

观察菜单也可以用来查看不在当前游戏中的玩家。这是通过 `GuiService/InspectPlayerFromUserId|GuiService:InspectPlayerFromUserId()` 实现的，这个方法接受任何玩家的 `Player/UserId|UserId`。

```    
    
    local GuiService = game:GetService("GuiService")
    local Players = game:GetService("Players")
    
    -- 根据玩家名称获得用户 ID
    local success, userId = pcall(function()
    	return Players:GetUserIdFromNameAsync("IgnisRBX")
    end)
    
    if success then
    	GuiService:InspectPlayerFromUserId(userId)
    end


```


***__Roblox官方链接__:[虚拟形象观察菜单](https://developer.roblox.com/zh-cn/articles/avatar-inspect-menu)