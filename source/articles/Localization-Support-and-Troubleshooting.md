# 本地化常见问题和错误排查 
Time:<em>articles/utilizing localization apis|本地化 API</em>

本错误排查指南可以帮助你解决本地化方面的特定问题。

## 常见问题

#### 如果自动文本捕获 (ATC) 不能捕获游戏中的所有文本怎么办？

ATC 仅捕获在 Roblox 应用程序中进行游戏时遇到的文本（ATC 在 Roblox Studio 中进行游戏测试时不会运行）。如果你的游戏中包含的文本在典型游戏过程中并不总是出现，例如复杂的 NPC 对话树，则可以：

  1. 手动将条目添加到本地化门户并为其提供翻译。
  2. 可以选择在使用翻译的 GUI 对象上禁用 ATC，并通过游戏中的`articles/utilizing localization apis|本地化 API` 对其进行管理。

##### ATC 无法捕获的对象 »

ATC 无法捕获某些游戏对象，或需要通过脚本进行特殊处理。当前 ATC 无法捕获的游戏对象有：

  * 默认的 Roblox 排行榜和聊天。
  * 玩家所拥有的`articles/intro to player tools|物品/工具`。
  * 具有嵌入文本的图像（但是请注意，可以根据玩家的区域设置通过`articles/localizing non text instances|交换图像`进行脚本化来“翻译”这些内容）。
  * 从平台提取的`articles/Badges Special Game Awards|徽章`名称和描述。
  * 从平台提取的`articles/Game Passes One Time Purchases|游戏通行证`名称和描述。

  


#### 如何防止自动文本捕获 (ATC) 尝试翻译字符串/ GUI？



***__Roblox官方链接__:[本地化常见问题和错误排查](https://developer.roblox.com/zh-cn/articles/Localization-Support-and-Troubleshooting)