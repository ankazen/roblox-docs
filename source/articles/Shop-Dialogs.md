# 商店对话框 
Time:<em>5  分钟</em>

`Dialog` 商店非常易于创建，且可以设为出售各种不同的物品（如武器、汽车或升级服务等）。这类商店也可以在各种不同的游戏（从冒险游戏到 RPG）中使用。本教程将介绍如何制作武器商店。

## 初始设置

我们将会建立一个出售武器的商店，因此需要至少选择一个能够出售的武器。“Toolbox（工具箱）” 的 “Tools & Weapons（工具与武器）” 类别中有一些非常棒的武器。

有了武器，我们就可以开始了。武器应位于 `Workspace` 中，并且我们需要将所有武器都放入 `ReplicatedStorage` 中。将武器重命名为 “Weapon1”；如果有多个武器，则按以下方式对其进行命名：“Weapon1”、“Weapon2” 等。此时，`ReplicatedStorage` 应如下所示（如果有多个武器，则会稍有不同）：

![Creating-A-Dialogue-Shop-Tree-0.png](https://developer.roblox.com/assets/blta2051edd9466bc5a/Creating-A-Dialogue-Shop-Tree-0.png)



## 创建商店

### 卖家

在实体商店里，柜台后面始终有人随时为你提供帮助，我们现在也需要设立这样一位人员。开发者可以在这位卖家上尽情发挥自己的创意。在本教程中，我们将使用 `Model` 内的一个基本 `Part`。现在，我们需要将 `Dialog` 插入这位卖家中，并确保你插入的目标部件名为 “Head”（头部）。接下来，我们需要将 `Humanoid` 插入这位卖家的 `Model` 中。

要插入 `Dialog`，请前往 _Insert（插入）-> Object（对象）-> Dialog（对话框）_ 。

### 商店

设置好卖家与可以出售武器的武器后，下一步就是创建商店了。创建商店时，我们将使用 `DialogChoice` 和 `DialogChoice/ResponseDialog` 来询问各种问题并给出答案。

首先请选择所创建的 `Dialog`，然后在属性窗口中，将 `Dialog/Purpose` 值更改为 “Shop”（商店）。然后将属性窗口中的 `Dialog/InitialPrompt` 值更改为当玩家开始与店主交谈时店主会说的话，本示例中将会使用 “Welcome to my shop!”（欢迎光临我的商店！）。

接下来，我们会为顾客添加可选择的选项，以便向卖家进行询问。该操作可通过将 `DialogChoice` 插入 `Dialog` 中来完成。要插入 `DialogChoice`，请前往

_Insert（插入）-> Object（对象）- > DialogChoice_ 。

在属性窗口中，将 `DialogChoice/UserDialog` 值更改为 “May I browse your goods?”（我可以浏览你的商品吗？），并将 `DialogChoice/ResponseDialog` 值更改为 “Sure!”（当然可以！）。

**注意：**上面所列举的所有对话文本都可以进行更改，并不会影响商店本身。

下一步，我们需要将更多 DialogChoice 插入刚刚创建的 `DialogChoice` 中，需要插入的 DialogChoice 数目应等同于出售武器的数目。可以从 “ChoiceA” 开始对其进行重命名，使其等同于出售的武器数目。举例来说，如果商店将会出售三个武器，则命名应为 “ChoiceA” 至 “ChoiceC”。

对话框现在应如下所示：  
![Creating-A-Dialogue-Shop-Tree.png](https://developer.roblox.com/assets/blt3915fe064436adca/Creating-A-Dialogue-Shop-Tree.png)



### 使商店运作

要使商店运作起来，需要将 `Script` 插入卖家头部的 `Dialog` 中。在脚本中，复制以下代码：

**注意:** 下面的代码使用了一个 `"Leaderboard` 。

Creating a Dialog Shop: Code Sample 1 ```    
    
    local dialog = script.Parent
    dialog.DialogChoiceSelected:Connect(function(player, choice)
        -- Check the player has a stats object
        local stats = player:FindFirstChild('leaderstats')
        if not stats then return end
    
        -- And that the stats object contains a gold member
        local gold = stats:FindFirstChild('Gold')
        if not gold then return end
    
        if choice == script.Parent.DialogChoice.ChoiceA then
            if gold.Value >= 5 then -- 5 is the amount of gold you need to purchase this weapon
                game.ReplicatedStorage.Weapon1:Clone().Parent = player.Backpack
                gold.Value = gold.Value - 5 -- subtract the amount of gold you need to purchase
            end
        elseif choice == dialog.DialogChoice.ChoiceB then
            if gold.Value >= 10 then
                game.ReplicatedStorage.Weapon2:Clone().Parent = player.Backpack
                gold.Value = gold.Value - 10
            end
        elseif choice == dialog.DialogChoice.ChoiceC then
            if gold.Value >= 15 then
                game.ReplicatedStorage.Weapon3:Clone().Parent = player.Backpack
                gold.Value = gold.Value - 15
            end
        end
    end)
    
    
    0

```


***__Roblox官方链接__:[商店对话框](https://developer.roblox.com/zh-cn/articles/Shop-Dialogs)