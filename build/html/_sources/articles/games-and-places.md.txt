# 游戏和场景 
Time:<em>5  分钟</em>

Roblox **游戏**由各种不同的**场景**组成。场景的概念就像游戏中的关卡。你可以直接对比 Unity 的场景和 Unreal Engine（虚幻引擎）的地图。场景包含环境、模型、UI、游戏逻辑以及构成关卡的所有其他内容。虽然游戏可以由多个场景组成，但每个游戏只有一个**起始场景**，玩家在开始玩游戏时将加载到这个场景。

## 制作游戏和场景

若要制作一个新游戏，首先需要创建一个新的场景并将其发布到云端。

  1. 通过 **File** （文件）→ **New** （新建）创建一个新场景。
  2. 在 **File** （文件）→ **Publish to Roblox** （发布到 Roblox）下将其发布为新游戏。
  3. 游戏发布到 Roblox 服务器之后，它的当前场景将在 **Game Explorer** （游戏管理器）窗口（可以通过屏幕顶部的 **View** （视图）选项卡访问）的 **Places** （场景）下列出。
![](https://developer.roblox.com/assets/blt920c84884e646d5b/Toggle-Game-Explorer.png)

 ![](https://developer.roblox.com/assets/bltac05e2228f55a807/Game-Explorer-Places.png)



### 创建其他场景

首次创建游戏时，会指定**起始场景**。该场景将在“Game Explore（游戏管理器）”中标记有 ![](https://developer.roblox.com/assets/bltaa05466e4937afd2/Start-Place-Icon.png)

 符号。

若要向游戏中添加多个场景，请右键单击 **Places** 文件夹并选择 **Add New Place（添加新场景）**。创建一个新场景之后，你便可以在“Game Explore（游戏管理器）”窗口中直接对其重命名。也可以双击场景，然后便开始在 Roblox Studio 中编辑。

## 项目的结构

### Roblox 游戏

Roblox 游戏的基本结构可以在“Game Explore（游戏管理器）”中找到。游戏包括名称和唯一标识符，以及属于游戏的其他资源，如徽章、开发者产品、图像、网格和套装。若要了解有关导入资源的更多信息，请参见 `articles/game assets|Roblox 中的游戏资源`。

### Roblox 场景

你的大部分工作都会在专门的场景中完成。在 Roblox Studio 中，可以使用[“Explorer（管理器）”](/resources/studio/Explorer)窗口管理脚本、UI、声音、环境以及玩家将与之交互的大多数其他游戏元素。

## 高级用法

### 在场景之间移动玩家

你可以在一个已发布的游戏中将玩家移动到不同的场景来作为单独的关卡。按照`articles/Teleporting Between Places|在场景之间传送`一文中的说明，了解如何在场景之间转换。

### 自定义加载屏幕

除了能够在不同场景之间传送玩家外，还可以为任何项目创建自定义加载屏幕。按照`articles/Custom Loading Screens|自定义加载屏幕`一文中的说明实现此功能。



***__Roblox官方链接__:[游戏和场景](https://developer.roblox.com/zh-cn/articles/games-and-places)