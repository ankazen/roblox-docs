# Roblox 主从架构 
Time:<em>10  分钟</em>

Roblox 使用**主从架构**，这也是一种多玩家游戏的通用框架。在你畅玩使用 Roblox 创作的游戏时，你的个人计算机、手机、平板电脑或游戏机就成为了**客户端**，游戏中的每一位其他独特玩家也各自是一个客户端。

游戏中的所有客户端（玩家）都会连接到一台功能强大的 Roblox 计算机（也就是所谓的**服务器**）。服务器就像是这个游戏的管理员 — 它会确保每位玩家看到和体验到的游戏世界与其他玩家完全相同。

![](https://developer.roblox.com/assets/blt4be5ef28af5c29b4/Client-Server-Model.png)



## 客户端与服务器之间的通讯

在游戏过程中，服务器会不断更新已连接的客户端。例如，试想有一个游戏 `Script` 将白天变为午夜。`Script` 只能在服务器上运行，所以服务器是第一个看到日夜转变的地方。此时，服务器会自动通知所有客户端也更改它们的游戏时间。

客户端也可以与服务器进行对话。典型的情形就是当你按下设备（客户端）上的按钮/按键或其他控制键时，会告知服务器更新你在游戏世界中的游戏角色，这样所有其他玩家就能看到你所在的位置和正在进行的操作。

## 了解客户端与服务器脚本

在为游戏编写**脚本**时，客户端和服务器都能处理如下特定任务非常重要：

### 客户端代码

一般来说，**客户端**应检测玩家的输入，并向该特定玩家显示信息。例如，`Articles/intro to player tools|玩家工具`会响应玩家的输入并可能在服务器上触发更改，但它们首先会在客户端进行处理，以便向玩家提供实时反馈。同样，客户端的菜单、地图和其他 GUI 也应该由客户端代码进行管理。

客户端代码在 `LocalScript` 内运行。只有在 `LocalScript` 属于以下实例的子类时，此类代码才会开始运行：

  * 玩家的 `Player/Character|Character` （角色）模型
  * 玩家的 `PlayerGui`
  * 玩家的 `Backpack`
  * 玩家的 `PlayerScripts` 文件夹
  * `Tool`（仅限于由玩家装备的情况）
  * `ReplicatedFirst` 文件夹

### 服务器代码

游戏**服务器**应负责处理游戏逻辑、保存玩家数据、更新得分、创建部件等。决定此情形的原因包括以下几点：

  * 如果脚本代码会改变游戏世界（如创建或移除部件），服务器必须确保所有客户端看到同样的改变。
  * 如果玩家的生命值或得分由服务器进行控制，那么黑客就无法更改这些数值来影响其他玩家。

服务器代码在 `Script` 中运行。只有当 `Script` 属于以下实例的子类时，此类代码才会开始运行：

  * `Workspace`
  * `ServerScriptService`
  * 玩家的 `Backpack`

### 远程函数/事件

服务器会自动处理多项任务，但有时候你需要将游戏设计中所独有的特定指令发送到服务器。可以通过`Articles/Remote Functions and Events|远程函数和事件`（`Script|Script` 和 `LocalScript|LocalScript` 用于相互通讯的对象）来完成该目标。

##### 服务器端验证

`RemoteEvent|RemoteEvent` 和 `RemoteFunction|RemoteFunction` 是适用于客户端与服务器间通信的最佳选项，但它们并非绝对安全的通道。狡猾的黑客可能会伪造远程事件，或者更改随其传递的值。因此，你应该使用基本服务器端验证来确认传入的请求是否合法。

了解更多 

以一个带有商店系统的游戏为例。当玩家想要购买物品时，玩家将与客户端上的界面进行交互，例如含 “Buy（购买）”按钮的 `ScreenGui`。当按下此按钮时，客户端可以向服务器发送远程事件并请求购买。但是，**服务器**（最可靠的游戏管理器）必须检查玩家是否有足够资金来购买该物品。

![](https://developer.roblox.com/assets/blt5fcdc8ffa5581b4b/RemoteEvent-Flow.png)



  


### 例外

有些客户端动作会立即复制，无需服务器的许可。这些动作主要与玩家应该立即看到的内容有关，而其他动作则为了方便你的操作而提供。

对象 例外

**Humanoid**
`Humanoid/Jump|Humanoid.Jump` 以及 `Humanoid/Sit|Humanoid.Sit` 属性会立即从客户端复制到服务器。请注意，此情况仅适用于本地玩家的人形对象 — 如果 `LocalScript` 试图更新其他玩家的人形，该指令会被忽略。

**Sound**
`Sound/TimePosition|Sound.TimePosition` 以及 `Sound/Playing|Sound.Playing` 属性会从客户端复制到服务器，所以如果某个客户端开始播放声音，所有其他客户端也会播放此声音。请参阅 `Sound` 文档以了解详细信息。

**AnimationTrack**
如果客户端在 `AnimationTrack` 上调用 `AnimationTrack/Play|AnimationTrack:Play()` 或 `AnimationTrack/Stop|AnimationTrack:Stop()`，该动画模型会以动画呈现在客户端上并复制到服务器。

**BasePart**
从技术而言，虽然部件属性不会复制，但有一些例外情况。如果该部件是由客户端所创建，且该客户端**模拟了物理变化**（如部件掉落、击中其他物体、受约束而移动等），则产生的变动将会复制到服务器。

**ClickDetector**
大多数的 `ClickDetector` 事件在客户端和服务器上都会触发，包括 `ClickDetector/MouseClick|MouseClick`、`ClickDetector/MouseHoverEnter|MouseHoverEnter`、`ClickDetector/MouseHoverLeave|MouseHoverLeave` 和 `ClickDetector/RightMouseClick|RightMouseClick` 等输入事件。



***__Roblox官方链接__:[Roblox 主从架构](https://developer.roblox.com/zh-cn/articles/Roblox-Client-Server-Model)