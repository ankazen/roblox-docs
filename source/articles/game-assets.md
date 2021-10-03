# Roblox 中的游戏资源 
Time:<em></em>

Roblox 的所有游戏资源都实现了在线存储，其中包括纹理、模型和音频文件等。与许多引擎不同，玩家和开发者都无需进行任何本地游戏资源存储。这样可以实现更好的团队协作，并有助于减轻版本较为陈旧的玩家设备上可能出现的存储空间问题。

![](https://developer.roblox.com/assets/blt93eb723202a3718a/Client-Server-Model-Banner.jpg)

以下简介旨在帮助开发者在游戏资源方面尽快入门。此外，若想要获取本文中出现主题的进一步说明，请参阅页面底部的相关文章。

## 一般资源信息

所有资源都有与单个 Roblox 帐户关联的唯一 ID，并且在上传时会自动将其提交给 Roblox 的审核团队。审核通常只需几分钟，获得批准的资源可以在 [Roblox Studio](https://www.roblox.com/create) 中使用。请前往[此处](https://en.help.roblox.com/hc/en-us/sections/200866010-Moderation-and-Guidelines)了解有关资源审核的更多信息。

## 图像

开发者可以在 Studio 中上传图像作为 3D 世界中的纹理使用，也可以用作菜单和交互式对象 GUI 的一部分。

![](https://developer.roblox.com/assets/blt42b1347723bdf6b2/Game-Assets-Game-Textures.jpg)

![](https://developer.roblox.com/assets/blt9f3d8170134af168/Game-Assets-GUI-Textures.jpg)

Roblox 接受 **.png**、**.jpg**、**.tga** 或 **.bmp** 格式的图像。最简单的图像上传方法为 **Game Explorer（游戏管理器）**窗口，可从 Roblox Studio 的 **View** （视图）选项卡处进行访问。

![](https://developer.roblox.com/assets/blt283d9c0bd225cb4d/Toggle-Game-Explorer.png)



打开窗口并发布游戏后，单击 “Game Explorer（游戏管理器）”窗口底部的 **Import** （导入）按钮。

![](https://developer.roblox.com/assets/blt10bc752362fb19f8/Bulk-Import-Button.png)



## 网格

`MeshPart` 为物理模拟类网格，支持上传 **.fbx** 或 **.obj** 格式的自定义网格。与图像一样，向游戏添加网格的最简单方法是通过 **Game Explorer（游戏管理器）**窗口。打开窗口并发布场景后，单击 **Import** （导入）按钮并找到网格文件。

![](https://developer.roblox.com/assets/blt10bc752362fb19f8/Bulk-Import-Button.png)



## 音频

Roblox 接受 **.mp3** 或 **.ogg** 格式的音频。若要为游戏上传自定义音频资源，请从 Roblox 网站的 [Audio（音频）](https://www.roblox.com/develop?View=3)页面开始。

上传音频文件需花费少量的 **Robux**（即 Roblox 的虚拟货币），因为我们需要花时间检查每个音频文件是否有不适当的内容。 

## 模型

在 Roblox 开发中，术语“模型”可以指代任何游戏对象，类似于 Unity 中的 “Prefabs”。此模型机制对于创建和共享部件/对象组、3D 网格、脚本、物理设备等非常有用。将对象或成组对象作为模型上传时，请遵循以下步骤：

  1. 在 **Explorer** （管理器）窗口中选中需要上传的项，并对其右键单击。
  2. 从弹出菜单中选择 **Save to Roblox…（保存至 Roblox…）**。
  3. 选择新的栏位或者覆盖现有栏位。

当作为`articles/Group Games|团队`进行合作开发游戏时， 或许应当将模型保存至上传窗口的 **Group Models（团队模型）**部分中。 

## 套装

通过 Roblox `articles/roblox packages|套装`，开发者在第一次创建对象层次结构后即可在之后的任意游戏中重复使用此套装。此工作流程的主要优点为：在更新任何游戏中的任何套装副本后，所有套装都将会同步至同一版本。有关详细信息，请参阅`articles/roblox packages|Roblox 套装 – 可重复使用的游戏资源`。

## 动画

通过`articles/using animation editor|动画编辑器`创建的角色动画可以保存在游戏本身中，也可以上传至 Roblox。详情请参阅`articles/using animation editor|使用动画编辑器`。



***__Roblox官方链接__:[Roblox 中的游戏资源](https://developer.roblox.com/zh-cn/articles/game-assets)