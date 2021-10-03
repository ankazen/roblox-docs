# 游戏缩略图和视频 
Time:<em>5  分钟</em>

**游戏缩略图**可用于推广游戏、展示游戏特性，甚至发布更新通告。Roblox 提供可自定义的 Studio 内部缩略图系统以满足任何游戏的需求。

![](https://developer.roblox.com/assets/blt87f621cb17ca7976/Game-Thumbnail-Example.jpg)

首次发布一款游戏时，将向其自动分配缩略图。此缩略图是从默认图像集合中随机选择的。 

## 上传缩略图

可以直接从 Roblox Studio 上传自定义游戏缩略图，步骤如下所示：

  1. 在 Studio 的 **Home**（主页）选项卡中单击 **Game Settings**（游戏设置）按钮。
![](https://developer.roblox.com/assets/bltd6af44e38b951d0a/Game-Settings.png)



  2. 在弹出窗口的 **Basic Info**（基本信息）部分中，向下滚动至 **Screenshots & Videos**（屏幕截图和视频）部分。
  3. 单击用虚线矩形指示的空栏位。
![](https://developer.roblox.com/assets/bltca07d90074bc77a3/Add-Game-Thumbnail.png)



  4. 从本地计算机中选择有效文件，然后继续上传过程。

除了自定义缩略图，还可以根据游戏本身设置自动生成的图像，以展示你的环境设计。自动生成的图像可通过 [Create（创建）](https://www.roblox.com/develop)页面来设置，方法是配置场景，选择 **Thumbnails（缩略图）**，然后选择 **Auto generated Image（自动生成图像）**。缩略图将根据上次发布场景时 Studio 中的镜头位置生成。 

## 链接视频

开发者还可以在针对移动设备和计算机用户的游戏页面上使用视频缩略图（Xbox 上的 Roblox 目前暂不支持视频缩略图）。若想使用视频作为缩略图，请遵循以下步骤：

  1. 访问 [Create（创建）](https://www.roblox.com/develop)页面。
  2. 配置场景，单击 **Thumbnails（缩略图）**选项卡，然后选择 **Video（视频）**。
  3. 输入视频的 YouTube URL 并单击 **Add Video（添加视频）**。视频经过审核机制审阅后即可被作为缩略图。

##### 自由镜头模式

在捕捉游戏内屏幕截图或视频时，启用 **Free Camera（自由镜头）**模式可能很有帮助。此功能允许你在游戏世界中移动镜头，并且捕捉在其他情况下不可能看到的特定视图/角度。

要在拥有服务器端开发人员控制台访问权限的任何游戏中启用自由镜头，请按左 Shift+P。

进入自由镜头模式后，使用 W A S D 或 U H J K 移动镜头，配合 Q / E 或 Y / I 上下移动。按住 Shift 可更改镜头移动速度，使用鼠标滚轮可缩放大小。

  


## 排序与删除

上传多个缩略图后，面向玩家的游戏详情页面将自动循环显示这些缩略图。只需在 Studio 的 **Game Settings（游戏设置）**窗口中将缩略图拖动至所需位置，就可更改此循环的顺序。

要删除缩略图，请将鼠标悬停在预览图标上，然后单击右下方的“垃圾桶”按钮。一旦确认操作，该缩略图将从队列中移除。

![](https://developer.roblox.com/assets/bltb80e7b5715a6d480/Delete-Game-Thumbnail.png)





***__Roblox官方链接__:[游戏缩略图和视频](https://developer.roblox.com/zh-cn/articles/Thumbnail)