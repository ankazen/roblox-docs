# Roblox 游戏设置 
Time:<em>Studio</em>

本文概述了 Roblox 游戏在 Studio 上的设置，包括游戏的易玩性、推广、玩家虚拟形象等选项。

要访问游戏设置，请从 Roblox Studio 的 **Home** （首页）选项卡点击 **游戏设置**按钮：

![](https://developer.roblox.com/assets/bltd6af44e38b951d0a/Game-Settings.png)



在打开后，您将在窗口左侧看到五个选项卡：**Basic Info（基本信息）**，**Permissions** （权限），**Avatar** （虚拟形象），**Options** （选项）以及 **World** （世界）。

## 基本信息

**基本信息**选项卡包含一般游戏设置、游戏图标、截图/视频、支持的设备等选项。

设置 描述

**Name（名称）**
玩家看到的游戏名称。

**Description（描述）**
玩家看到的游戏描述。

**Game Icon（游戏图标）**
允许您上传一个游戏图标。关于创建游戏图标的建议，参见`articles/Game Icons Tips|设计游戏图标`。

**Screenshots & Videos（截图和视频）**
允许您上传宣传截图和视频。有关建议请参见`articles/Thumbnail|游戏缩略图和视频`。

**类型**
游戏的基本类型。

**可游玩设备**
设置游戏可在哪些设备上游玩。

## 权限

**Permissions** （权限）选项卡允许您控制游戏的受众，以及`articles/Group Games|群组`成员和协作者。

设置 描述

**Playability（可玩性）**
设置哪些玩家可访问/游玩 Roblox 上的游戏。

**Game Owner（游戏所有者）**
允许您根据游戏所有权设置游戏访问级别。 

  * 对于用户拥有的游戏，所有者拥有完全访问权限，所以此选项无法更改。 
  * 对于`articles/Group Games|群组游戏`，可以为群组中的每个用户角色设置唯一的访问级别(**No Access（无权访问）**、**Play（游玩）**或 **Edit（编辑）**)。

**Collaborators（协作者）**
允许您将 Roblox 用户添加为`articles/Team Create|组队创作`协作者，并为其设置访问级别。此段只会出现在用户拥有的游戏。 

  * **游玩** — 协作者只能试玩游戏。
  * **Edit** — 协作者可以试玩并编辑游戏。

## 虚拟形象

**Avatar** （虚拟形象）选项卡提供玩家虚拟形象的多种设置，包括根据您的需求限制虚拟形象的某些方面的能力。

设置 描述

**Presets（预设）**
将窗口下部的选项设为各种预设，之后可单独进行调整。

**Avatar Type（虚拟形象类型）**
变形为 `Articles/r6 vs r15 avatars|R6`，`Articles/r6 vs r15 avatars|R15`，或让玩家自行选择。

**Animation（动画）**
使用默认虚拟形象动画或让玩家使用自定义动画。如需详情，请参见`articles/using animations in games|在游戏中使用动画`。

**Collision（碰撞）**
使用固定大小的碰撞盒或动态大小的碰撞盒。

**Scale（比例）**
设置玩家虚拟形象的各方面比例。将滑块拖动到最末端（左右两侧）可允许虚拟形象变形为每个玩家在 Roblox 上选择的设置，或缩小范围让所有虚拟形象使用更具体的比例。

**Body Parts（身体部件）**
允许您按资源 ID 强制所有玩家使用特定的身体部件，或让玩家保留自己的虚拟形象部件。

**Clothing（服装）**
允许您按资源 ID 强制所有玩家使用特定的服装，或让玩家保留自己的虚拟形象服装。

## 选项

**Options** （选项）选项卡包含通常为特殊环境而保留的游戏设置。

设置 描述

**Allow HTTP Requests（允许 HTTP 请求）**
允许游戏服务器通过 `HttpService` 向远程服务器发出请求。

**Enable Studio Access to API Services（允许 Studio 访问 API 服务）**
允许 Studio 访问 API 服务，可用于测试如`articles/Data store|数据存储`之类的服务的实施。

**Enable Collaborative Editing（启用协作编辑）**
在组队创作进程中启用`articles/Team Create#collaborative-scripting|协作脚本编写`。

## 世界

**World** （世界）选项卡包括重力、角色跳跃行为、行走速度等全局游戏设置。

设置 描述

**预设**
将窗口下部的选项设为各种预设，之后可单独进行调整。

**Gravity（重力）**
设置整体世界重力，单位为格/秒²（请注意，相当于括号内的米/秒²）。

**Jump（跳跃）**
以格为单位设置人形的跳跃高度，或以格/秒为单位设置跳跃能力。请注意，对此值的调整会改变与行走速度有关的最大跳跃距离。

**Walk（行走）**
以格/秒为单位设置人形的行走速度。请注意，对此值的调整会改变与跳跃高度或能力有关的最大跳跃距离。

**Slope（斜率）**
确定人形可攀爬的最大倾斜角度。如果倾斜角度大于此值，则人形将从斜坡滑下。



***__Roblox官方链接__:[Roblox 游戏设置](https://developer.roblox.com/zh-cn/articles/game-settings)