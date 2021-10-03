# 不同场景间的传送 
Time:<em>5  分钟</em>

**Teleportation**（传送）功能有可能提升极大型世界的游戏性能。举例来说，如果一个奇幻类游戏世界中包含数个城镇、一座城堡、几个大型地下城和一座闹鬼的森林，开发者应当将这些地区制成多个场景，并在特定地点（例如地下城的入口或出口）允许玩家在场景间进行传送。

在 Roblox 中，传送由 `TeleportService` 处理。这可用于在游戏中的场景之间传送玩家，甚至将玩家传送至其他游戏。

`TeleportService` 在 Roblox Studio 的游戏测试期间无法使用 — 要测试本教程中的概念，你必须发布游戏，并在 Roblox 应用程序中操作游戏。 

## 获取目标 ID

`TeleportService` 中的大部分函数均需要目标场景或游戏的 ID。如果目的地场景与原始场景均位于同一个游戏中，则可从 **Game Explorer（游戏管理器）**获取 ID，方法是展开 **Places** （场景）树，右键单击



***__Roblox官方链接__:[不同场景间的传送](https://developer.roblox.com/zh-cn/articles/Teleporting-Between-Places)