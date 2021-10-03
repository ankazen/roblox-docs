# 监控游戏崩溃与性能过滤功能 
Time:<em>2  分钟</em>

移动设备通常不具备与计算机或控制台相同的性能。一款游戏可能在 PC 或 Xbox 上运行得很好，但在手机或平板电脑上却很难运行，尤其是当游戏非常庞大或使用了很多资源时。

Roblox 移动应用程序在创建排序（例如热门排序）时会检查游戏的性能。如果一个游戏在某个设备上崩溃太多，那么该游戏将在该设备上的排序中被隐藏起来。

作为开发者，了解你的游戏是否崩溃非常重要。如果你的游戏因为崩溃而没有出现在 Roblox 应用程序中，那么玩家将很难找到该游戏，因此无法享受你的游戏。

## 监控游戏的崩溃

若要检查游戏是否在移动设备上发生崩溃，请访问游戏的 **Developer Stats（开发者统计资料）**页面。若要打开游戏的开发者统计资料，请访问游戏的网页，单击 **…** 按钮并选择 _Developer Stats（开发者统计资料）_。

![OpenDeveloperStats.png](https://developer.roblox.com/assets/blt377577c34340d1a1/OpenDeveloperStats.png)



“Developer Statistics（开发者统计资料）”页面有关于你的游戏的各种重要信息，但特别是，它显示了关于过滤设备的信息。**Filtered Devices（过滤的设备）**部分显示游戏在哪些设备上被过滤（不在排序中显示），以及游戏在这些设备上崩溃的程度。

![PerformanceFiltering.png](https://developer.roblox.com/assets/blt02ee948674d469d1/PerformanceFiltering.png)



## 修复崩溃的游戏

虽然没有解决游戏崩溃的办法，但移动设备上最常见的原因是内存使用。手机和平板电脑的内存很少，如果游戏占用过多内存，则可能会导致崩溃。“Memory Analyzer（内存分析器）”显示一个游戏使用了多少内存，以及游戏的哪些部分使用的内存最多。

对游戏进行修复和优化后，请确保发布更改。当游戏的新版本发布时，崩溃过滤器将重置，并且游戏将再次在排序中显示。



***__Roblox官方链接__:[监控游戏崩溃与性能过滤功能](https://developer.roblox.com/zh-cn/articles/Monitoring-Games-for-Crashes-and-Performance-Filtering)