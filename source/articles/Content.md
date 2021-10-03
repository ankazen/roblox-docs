# 内容数据类型 
Time:<em>2  分钟</em>

在 Roblox 上，**内容**是一个指向资源（如图像、声音或网格）的特殊格式化字符串。出于安全原因，`ContentProvider` 服务会阻止加载指向**非**可信站点上的文件的链接。下图显示了过滤器的工作原理：

读取链接

检查链接

由过滤器决定通过或阻止

加载通过的内容

## 内容格式

内容有多种格式，所有格式都指向联机文件或保存到客户端计算机的文件。基本结构是 **protocol**（协议）名称，后跟 ://，，然后是**字符串**，这取决于使用的协议。

protocol://string

协议 字符串 描述

**rbxasset**
一个文件路径
从 Roblox 内容文件夹中获取一个文件

**rbxassetid**
一个有效的资源 ID
从 Roblox 网站获取一个用户创建的资源

**rbxgameasset**
文件夹/目录 + 资源名称
获取一个通过游戏管理器上传的资源

**rbxhttp**
一个 Roblox 网站上的路径
从 Roblox 网站获取内容

**rbxthumb**
有序的参数和值
允许轻松加载缩略图

**http / https**
网站 URL
使用 URL 获取网站上的内容

## 协议

### rbxasset

指向用户电脑上的 Roblox 内容文件夹。

rbxasset://textures/face.png

以下是支持的操作系统中内容文件夹的位置：

**Windows** — `%localappdata%\Roblox\Versions\<version>\content`  
**Mac** — `Applications/RobloxStudio.app/Contents/Resources/content`

### rbxassetid

指向本站上的一个用户创建的资源。例如，以下 **rbxassetid** 指向一个 Roblox 创建的图片：

rbxassetid://607948062

以下为它的 URL 对等形式：

https://www.roblox.com/asset/?id=607948062

### rbxgameasset

指向一个通过[游戏管理器](/resources/studio/Game-Explorer)上传的资源。这允许您使用用户友好的名称而不是 ID 来访问资源。因此如果您通过游戏管理器上传了一个名为 Potion.png 的图片，您可以用以下格式引用它：

rbxgameasset://Images/Potion

在上面的示例中，“Images” 是游戏管理器中的目录/文件夹，而 “Potion” 是资源的名称，除去其扩展名。

注意 **rbxgameasset** 只对当前游戏生效。如果您将使用该资源的父对象粘贴到另一个游戏中，则该资源不会被加载（或者，如果您在那个游戏中上传了一个同名的资源，则会加载那个资源）。如果您需要一项资源跨多个游戏工作，请使用 **rbxassetid**，而不是 **rbxgameasset**。 

### rbxhttp

相当于 `ContentProvider/BaseUrl` 的简写。例如：

rbxhttp://Thumbs/Avatar.ashx?x=100&y;=100&format;=png

可以扩展为：

https://www.roblox.com/Thumbs/Avatar.ashx?x=100&y;=100&format;=png

### rbxthumb

这是一种允许轻松加载缩略图的内容格式，它适用于图片内容 ID 可以使用的任何地方，例如 `ImageLabel/Image` 或`ContentProvider/PreloadAsync|ContentProvider:PreloadAsync()`。

**rbxthumb** 的格式如下，**参数顺序必须遵循**。

rbxthumb://type=[ThumbnailType]&id;=[TargetId]&w;=[Width]&h;=[Height]

例如：

rbxthumb://type=Asset&id;=24813339&w;=150&h;=150

##### 支持的类型和大小 »

类型 支持的尺寸

**Asset（资源）**
150×150、420×420

**Avatar（虚拟形象）**
100×100、352×352、720×720

**AvatarHeadShot（虚拟形象头像）**
48×48、60×60、150×150

**BadgeIcon（徽章图标）**
150×150

**BundleThumbnail（捆绑包略缩图）**
150×150、420×420

**GameIcon（游戏图标）**
50×50、150×150

**GamePass（游戏通行证）**
150×150

**GroupIcon（群组图标）**
150×150、420×420

**Outfit（服装）**
150×150、420×420

  


### http / https

指向内容在互联网上的确切位置。只能用于 Roblox 允许的站点，若用于其它站点，则会出现错误。

https://www.roblox.com/asset/?id=607948062



***__Roblox官方链接__:[内容数据类型](https://developer.roblox.com/zh-cn/articles/Content)