# 禁用游戏界面 
Time:<em>2  分钟</em>

Roblox 附带了一组 GUI 元素，这些元素在默认情况下对所有游戏都启用。其中包括：

  * 玩家列表
  * 当前玩家的生命条
  * 玩家的背包
  * 聊天窗口

如果你不需要这些元素中的任何一个，或者你已经编写了自己的元素，那么 StarterGui 服务具有启用和禁用每个元素的功能。

## 如何启用/禁用 GUI 元素

StarterGui 有一个名为 `StarterGui/SetCoreGuiEnabled|SetCoreGuiEnabled` 的函数，用于启用和禁用 Roblox 提供的基本 GUI 元素。该函数首先需要的是一个 `CoreGuiType`。这是你要设置的元素。该函数第二个需要的是一个布尔值（true/false 值），它表示你是要启用还是禁用该元素。可以启用或禁用的元素列表包括：

  * Enum.CoreGuiType.PlayerList
  * Enum.CoreGuiType.Health
  * Enum.CoreGuiType.Backpack
  * Enum.CoreGuiType.Chat
  * Enum.CoreGuiType.All

`SetCoreGuiEnabled` 只能在本地脚本中调用。这意味着对 GUI 所做的任何更改都将只应用于拥有该本地脚本的玩家。

## 示例

此示例只是禁用生命条：
    
    
    local StarterGui = game:GetService("StarterGui")
    StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Health, false)
    

此示例禁用所有核心 GUI：
    
    
    local StarterGui = game:GetService("StarterGui")
    StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.All, false)
    

此示例禁用除了 Chat 之外的所有核心 GUI：
    
    
    local StarterGui = game:GetService("StarterGui")
    StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.All, false)
    StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Chat, true)
    

## 顶栏 GUI

顶栏包含默认的 Roblox GUI，并且可以禁用。这将导致所有其他 Roblox GUI 被禁用。使用 `StarterGui/SetCore`（而非 `StarterGui/SetCoreGuiEnabled|SetCoreGuiEnabled`！），你可以采取如下方式禁用它：
    
    
    local StarterGui = game:GetService("StarterGui")
    StarterGui:SetCore("TopbarEnabled", false)
    

请注意，不能禁用左上方的汉堡包菜单按钮。

## 触摸 GUI

在具有触摸功能的设备上玩 Roblox 游戏时，会在玩家 GUI 中添加另外两个元素：一个控制板和一个跳转按钮。可以使用 UserInputService 按照如下方式隐藏它们：
    
    
    local UIS = game:GetService("UserInputService")
    UIS.ModalEnabled = true
    

## Xbox One GUI

Roblox 的 Xbox One 版本与其他平台相比有一些差异。

  * Chat - 聊天 GUI 不会出现，并且对 SetCoreGuiEnabled(Enum.CoreGuiType.Chat) 的任何调用都将被忽略
  * Playerlist - 玩家列表始终处于启用状态，对 SetCoreGuiEnabled(Enum.CoreGuiType.PlayerList) 的任何调用都将被忽略
  * Topbar - 顶栏不会出现



***__Roblox官方链接__:[禁用游戏界面](https://developer.roblox.com/zh-cn/articles/Disabling-Parts-of-Game-Interface)