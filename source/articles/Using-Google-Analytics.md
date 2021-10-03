# 在 Roblox 中使用 Google Analytics 
Time:<em>推出后</em>

游戏发布后，Roblox 游戏开发者的工作并未停止。测试过程中没有出现的错误有可能出现，玩家会以你无法想象的方式就游戏设计作出回应，你还需要逐步为游戏添加新功能。

在游戏推出后进行监控的一种方式是借助`articles/introduction to analytics|分析`，你可以使用 [Google Analytics](https://analytics.google.com/) 等工具实现。

## 获取跟踪 ID

要使用 Google Analytics 分析游戏的各个方面，你需要**跟踪 ID**，这是一串唯一编号，可在游戏的所有场景间共享。如有需要，你稍后可为其他游戏生成其他跟踪 ID。

[注册](https://analytics.google.com/) Google Analytics 帐户后，请提供以下信息：

项目 指导原则

**帐户类型**
请选择**网站**作为跟踪帐户类型（即使是跨平台 Roblox 游戏，也可通过这种帐户类型来分析数据）。

**帐户名称**
由于一个帐户可以为多个游戏保留多个跟踪 ID，因此请输入非特定名称，如“Roblox Games”。

**网站名称**
也称为**属性名称**，一般可描述你计划分析的内容。如果你最有兴趣跟踪游戏中的一个场景，则可以使用特定场景名称，如“游戏大厅”或“赛道 1”。如需分析多个场景，最好使用游戏标题。请注意，你稍后可以更改此名称和添加其他属性。

**网站 URL**
请输入任何有效的网址（不会跟踪网站本身）。

其他信息与 Roblox 使用 Google Analytics 的方式无关，所以请视需要提供其他详细信息。

准备好后，请单击 **Get Tracking ID（获取跟踪 ID）**。此操作将打开包含以下格式的新跟踪 ID 的页面：

UA-#########-#

## 使用跟踪 ID

### 启用 HTTP 请求

要在 Roblox 游戏中使用 Google Analytics，必须启用 `HttpService`：

  1. 在 Roblox Studio 中，单击 **Home** （主页）选项卡中的 **Game Settings（游戏设置）**。
![](https://developer.roblox.com/assets/bltd6af44e38b951d0a/Game-Settings.png)



  2. 在弹出窗口的 **Options** （选项）选项卡中，启用 **Allow HTTP Requests（允许 HTTP 请求）**选项。请注意单击 **Save** （保存）以存储偏好设置。

### 跟踪场景

要开始跟踪场景中的操作和事件，请执行以下简单步骤：

  1. 在 **ServerScriptService** 中创建新服务器 `Script`。
  2. 将以下行粘贴至脚本。

```    
    
    local GA = require(153590792)
    GA.Init("UA-#########-#")


```
  3. 使用之前获取的跟踪 ID 替换 `UA-#########-#`。操作完成；现在，Google Analytics 即可跟踪你的场景！

若要使用更精细的方法，则可以将 `config` 表传递至 `GA.Init()` 函数：

```    
    
    local config = {
    	-- Report or omit script errors (set as 'true' to omit)
    	DoNotReportScriptErrors = false,
    	-- Report or omit a 'ServerStartup' action when a server starts (set as 'true' to omit)
    	DoNotTrackServerStart = false,
    	-- Report or omit player visits under the 'Visit' action (set as 'true' to omit)
    	DoNotTrackVisits = false
    }
    
    local GA = require(153590792)
    GA.Init("UA-#########-#", config)


```
## Google Analytics 基础知识

本文并未概述 Google Analytics 的详细用法（请参考平台内帮助），而是提供有助于你入门的指导原则。

### 实时事件

为某场景设置了跟踪 ID 后，即可轻松查看实时统计数据。

  1. 将游戏发布至 Roblox 以确保将跟踪 ID 添加至新 `Script`。
  2. 开始在 Roblox Studio 或 Roblox 应用程序中体验所跟踪的场景。
  3. 在 Google Analytics 页面，展开左侧的 **Real-Time（实时）**菜单。
  4. 单击 **Events（事件）**子项可出现一个图表，其中展示了游戏中发生的事件。如果你没有通过脚本中的 `config` 表禁用它们，则可以看到类似 ServerStartup 和 Visit 等新事件。如果游戏中存在任何 Lua 错误，则错误发生时也会在图表中显示。

### 历史行为

你也可以单击 **Behavior（行为）** → **Events（事件）**以查看事件历史记录。此操作可显示一段时间内所有跟踪的事件，并提供了多种筛选数据和分析趋势的方法。例如，下方的 **Overview（概览）**页面显示了事件总数以及相关数据。单击 **Event Action（事件操作）**即可显示 ServerStartup 和 Visit 等操作，每项均可展开以显示详细信息。

![](https://developer.roblox.com/assets/blte54c4406db8d370d/Google-Analytics-Screen.png)



## 报告自定义事件

Roblox 与 Google Analytics 集成后，你可以报告自定义游戏内事件，从玩家发现秘密藏宝室到各物品/对象的使用频率对比都包含在内。

要向 Google Analytics 报告自定义事件，请使用已在上方 `Script` 示例中初始化的 `GA` 模块的 `ReportEvent()` 函数：

```    
    
    local GA = require(153590792)
    GA.Init("UA-#########-#")
    
    local category = "PlaceId-" .. game.PlaceId
    local action = "Category-Action"
    local label = "none"
    local value = 1
    
    GA.ReportEvent(category, action, label, value)


```
如前所述，`GA.ReportEvent()` 调用需要四个参数：

参数 说明

`category`
默认值为 `"PlaceId-" .. game.PlaceId`，可生成类似 PlaceId-5432167890 的字符串，但你可以指定更具描述性的类别，如`“GameItemActions”`。

`action`
此值在 Google Analytics 中显示为 **Event Action（事件操作）**，如上方屏幕快照中的 Visit 部分所示。这可用于识别与类别相关的特定操作，例如，`"GameItemActions”` 的 `action` 值可能 是`"Equipped”`。

`label`
此值在 Google Analytics 中显示为 **Event Label（事件标签）**，可用于定义有关类别或操作的特定详细信息。例如，`"GameItemActions”` → `"Equipped”` 可能以实际装配的物品标注，如 `"Ice Wand”`。

`value`
你可以使用此参数定义与事件相关的特定值。例如，你可以记录**装配**了某物品的玩家实际**使用**该物品的次数，然后以 `action` 值 `"TimesUsed”` 将该值报告给 Google Analytics，从而分析玩家是否喜欢使用该物品。

* * *

如你所见，你可以使用分析功能微调游戏并提升玩家体验。掌握了如何将 Google Analytics 与游戏相关联后，你还可以通过`articles/measuring engagement|衡量参与度`和`articles/designing for engagement|设计参与度`指南探索分析的基本概念。



***__Roblox官方链接__:[在 Roblox 中使用 Google Analytics](https://developer.roblox.com/zh-cn/articles/Using-Google-Analytics)