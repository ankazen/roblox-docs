# 网络模拟模式 
Time:<em>2  分钟</em>

在 Roblox 中制作游戏时，定期进行测试非常重要，尤其是当测试模拟次优条件时。Studio 的**网络模拟**模式旨在模拟较差的连接性，以便可以开发网络连接不好的玩家也能玩的游戏。

网络模拟模式专门做两件事。第一件事，它模拟通过网络发送信息时的时间延迟。无论何时在网络模拟模式下进行 web 调用，调用都会延迟 300 到 600 毫秒之间的一个随机时间。

第二件事，它模拟随机网络故障。在网络模拟模式进行 web 调用时，模拟有 30％ 的机会使调用失败。如果这些调用未封装在 `pcall` 标签内，则运行该代码的脚本将出错。

## 启用网络模拟模式

网络模拟模式仅在 Studio 的 **Local Server（本地服务器）**模拟中有效。若要启用它：

  1. 导航到 Studio 中的 **Test（测试）**选项卡。
  2. 确保 **Local Server（本地服务器）**为所选择的模式。
  3. 单击 **Start（开始）**启动 Studio 的新会话（一个会话用于服务器，一个会话用于配置的玩家数量）。
  4. 在服务器的新会话中，单击 **Network Simulator（网络模拟器）**按钮。这将启用该模式。再次单击将禁用该模式。

![NetworkSimulationToggle.PNG](https://developer.roblox.com/assets/bltfc7a965eafed28a4/NetworkSimulationToggle.PNG)

启用后，“Output（输出）”窗口将在其标题栏中显示 **Network Simulator Enabled（网络模拟器已启用）**。

![NetworkSimulationEnabled.PNG](https://developer.roblox.com/assets/blt56af6687c4e4aaca/NetworkSimulationEnabled.PNG)

## 受网络模拟影响的服务

请注意，网络模拟模式仅适用于以下特定的 Roblox 服务：

  * `DataStoreService`

  * `MarketplaceService`

  * `HttpService`

  * `ContentProvider`

  * `GamePassService`

  * `InsertService`

  * `Players`

  * `AssetService`

  * `GroupService`

  * `PointsService`

  * `TeleportService`

  * `BadgeService`

  * `Chat`

  * `TextService`



***__Roblox官方链接__:[网络模拟模式](https://developer.roblox.com/zh-cn/articles/Network-Simulation-Mode)