# NPC 对话框 
Time:<em>5  分钟</em>

**Dialog** 对象能让你通过内置界面来创建能够与之交谈的 NPC 角色。界面简单易用，甚至无需进行脚本编写。不仅如此，你还能通过 `Dialog/DialogChoiceSelected` 事件来添加额外的功能。

可应用于以下场景：  
*创建提供奖励或任务的 NPC 角色；  
*创建机器人助手；  
*创建会说话的敌人；  
*可以创建任何物品，请尽情发挥你的想象！

## 基本概述

对话应用实际上非常简单，即使没有完成 Lua 语言学习的制作者，也不必进行脚本编写。对话的构成如下图所示：

![DialogExample.PNG](https://developer.roblox.com/assets/blt9dea6289967fa3c9/DialogExample.PNG)

Dialog 对象会显示初始提示，随后会从 DialogChoice 对象向用户提供回答选择；而 DialogChoice 接着会通过自身所包含的 DialogChoice 对象向用户提供回答选择。

## 创建基本的对话

### 制作对话气泡

首先，打开 Roblox Studio 并创建一个新场景。在管理器（View（视图）-> Explorer（管理器））中，选择你想要显示的对话气泡部件。单击“Insert（插入）”，选择“Basic Objects（基本对象）”，然后在出现的窗口中选择“Dialog（对话）”。第一个对话对象就创建完成了！在使用角色运行游戏（联机或单人测试模式）前，暂时无法看到对话气泡。  
在属性窗口（View（视图）-> Properties（属性））中，可以看到 `Dialog/InitialPrompt` 属性。将该属性更改为当你单击对话气泡时该部件所要说的话。

好啦！你已经完成了第一个单击其图标就会说话的部件！

#### 添加选择

你已经做好了对话气泡。效果不错，不过你还是没法跟它交谈，对吧？  
选择原始的 Dialog 对象并单击“Insert（插入）”，单击“Basic Objects（基本部件）”，接着从窗口中选择 `DialogChoice`。在已经打开的属性窗口中将会看到一条名为 `DialogChoice/UserDialog` 的属性。**这是用户将会得到的选择**，**而非**该属性或任何其他属性的名称。`DialogChoice/ResponseDialog` 属性是用户选择后部件会说的话，请将其更改为想要说的话。  
向原始的 Dialog 对象添加多少个 DialogChoice 对象，就能向用户提供多少种选择。

#### 添加更多选择

现在，我们的 Dialog 能向用户提供多种选择，每种选择都能让部件给出一种回答。此外，我们还能在这些选择中添加更多选择，从而用该部件创建一组更加丰富的对话。  
要实现这一目的，只需在完成上一步时不将 DialogChoice 对象插入原始 Dialog 对象，而是将其插入已有的 DialogChoice 对象当中。

#### 更多属性和自定义内容

可以利用其他属性进一步自定义自己的 Dialog。请通过属性窗口更改这些属性。  
_注意：这些都是只会在游戏中呈现视觉效果的属性。_

`Dialog/ConversationDistance`：请将其设为能够与部件对话的最大距离。走出该范围，对话就会终止。

`Dialog/Purpose`：这些是显示在部件上方供你单击的各种图标。任务用 **!** 表示，帮助用“?”表示，而商店则用“$”表示。

`Dialog/Tone`：这是对话（即对话气泡）和选择 GUI 的颜色。友好用绿色表示，中立用蓝色表示，敌对则用红色表示。

#### 示例

以下是一个使用中的 Dialog 示例。

![Final_Dialog_Example.gif](https://developer.roblox.com/assets/bltc80572d5d73b3459/Final_Dialog_Example.gif)

### 脚本编写

如果你已经完成了 Roblox Lua 的学习，还可以向自己的 NPC 部件添加更多的功能。脚本编写事件 DialogChoiceSelected 包含两种参数，即玩家对象和玩家所作选择的**对象**。该事件_不会_返回选择的名称。每当玩家作出一种选择时，都会触发该事件。
    
    
    workspace.Dialog.DialogChoiceSelected:connect(function(player,choice)
    	print(player.Name,choice.Name)
    end)
    

该事件会打印玩家的名称，以及**每次玩家作出选择时**所作选择的名称。你不能用 Dialog 方法将其本地化为具体的选择。如果希望在玩家作出特定选择时触发事件，就需要赋予其一个唯一的 Name 属性，并将其与 if 语句进行比较。
    
    
    workspace.Dialog.DialogChoiceSelected:connect(function(player,choice)
    	if choice.Name == "No" then
    		player.Character.Humanoid.Health = 0
    	elseif choice.Name == "Yes" then
    		player.Character.Humanoid.Health = 1000
    	end
    end)
    

你也可以在特定玩家作出特定选择时触发事件。

示例：
    
    
    workspace.Dialog.DialogChoiceSelected:connect(function(player,choice)
    	if choice.Name == "isplayer" and player.Name == "pighead10" then
    		player.Character.Humanoid.Health = 10000
    	end
    end)
    

你可以通过该类事件可以给予角色任务、奖励、商店物品等！



***__Roblox官方链接__:[NPC 对话框](https://developer.roblox.com/zh-cn/articles/Usage-of-dialogs)