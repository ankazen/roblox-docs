# 分析游戏数据 
Time:<em>5  分钟</em>

在 Roblox 平台上，你可以轻松查看和下载统计游戏数据，包括：

  * 当前玩游戏的玩家数量以及他们使用的平台（PC、平板电脑、手机或游戏机）。
  * 关于玩家访问总量的历史数据、他们玩了多长时间，以及在某个场景中花费了多少 Robux (![](https://developer.roblox.com/assets/blt924b50fb6c9e0995/Robux-Icon-NoRightMargin.png)

)。
  * 每日和每月销售的`articles/Developer Products In Game Purchases|开发者产品` （游戏中购买）。

使用此数据，你可以确定游戏中收益最高的物品、访问量最高的场景等。

## 打开开发者统计资料

若要访问统计数据，请导航到游戏中特定场景的主页，单击 ![](https://developer.roblox.com/assets/blt738fe32bb9c285f9/Config-Dots.png)

 按钮，然后从上下文菜单中选择 **Developer Stats（开发者统计资料）**。

![](https://developer.roblox.com/assets/blt81763f7cb93478ba/Open-Developer-Stats.png)



在目标页上，是数据的摘要：

部分 描述

**Live Stats（实时统计资料）**
整个游戏（所有场景）中的玩家数量，按平台分隔。这些值每 30 秒更新一次。

**Filtered Devices（筛选的设备）**
如果你的游戏经常在某个平台上崩溃，那么当玩家在该平台上浏览 Roblox 游戏时，可能会忽略这个问题。如果发生这种情况，你应该确定游戏崩溃的原因并修复它（有关指南，请参阅`articles/Developer Console|开发者控制台`和 `/articles/Improving Performance|提高性能`）。

**Historical Data（历史数据）**
此部分包含图表和表格，例如 **Visits（访问次数）**、**Average Visit Length（平均访问时长）**、**Robux Revenue（Robux 收入）**和 **Developer Product Sales（开发者产品销售）**。这些数据可以按小时/天/月和平台进行筛选。

请注意，**Live Stats（实时统计资料）**和 **Filtered Devices（筛选的设备）** 下的数据代表整个游戏，而 **Historical Data（历史数据）**下的统计资料都是按场景的统计资料。 

## 下载数据

若要查看更详细的统计数据，可以下载 .csv 或 .xlxs 电子表格。例如，电子表格可以显示有多少人在他们的手机上购买了某一特定物品，或者你的收入中有多少百分比来自特定的`articles/Game Passes One Time Purchases|游戏通行证`或`articles/Developer Products In Game Purchases|开发者产品`销售。

若要下载电子表格文件：

  1. 在“Developer Stats（开发者统计资料）”页面的顶部，单击 **Data Export** （数据导出）选项卡。
  2. 选择你要下载的月份并单击 **Generate** （生成）按钮。
  3. 生成完文件之后，单击 **Download** （下载）按钮，找到文件并在电子表格编辑程序中打开该文件。

### 数据组织

你会注意到，电子表格并不是所发生的每笔销售占一行，而是按天对数据进行了分类。这意味着，如果同一天同一物品有两次销售，它们将显示为一行，其中 **SalesVolume** 为 **2**。

列名称 描述 示例

**PlaceId**
发生交易的场景的 ID。
0123456789

**PlaceName**
发生交易的场景的名称。
Ice Cavern

**GameId**
发生交易的游戏的 ID。
955573389

**GameName**
发生交易的游戏的名称。
Gem Hunter

**ItemId**
所销售的物品的产品 ID。这是内部 Roblox ID，与资源 ID 不同。
1492051

**ItemName**
所销售的物品的名称。
Energy Bar（能量条）

**ItemType**
所销售的物品的类型。
Developer Product（开发者产品）

**Date**
销售日期。
2019_06_01

**SalesVolume**
物品的销售数量。
68

**Impressions**
如果该行显示广告展示次数，则为观看移动视频广告的次数。
140

**Revenue**
你从物品中获得的利润。
80

**RevenueSource**
收入是来自销售还是来自广告展示。
Transactional（交易）

**Device**
玩家所使用的设备类型。
Phone（手机）

##### 组织数据

When inspecting the spreadsheet, note that it does not contain a row for every sale that occurs. Instead, the data is bucketed by day. That means if there were two sales of the same item on the same day, they appear as a single row with **SalesVolume** of **2**.

Column Description Example

**PlaceId**
ID of the place in which the transaction occurred.
0123456789

**PlaceName**
Name of the place in which the transaction occurred.
Ice Cavern

**GameId**
ID of the game in which the transaction occurred.
955573389

**GameName**
Name of the game in which the transaction occurred.
Gem Hunter

**ItemId**
Product ID of the item that was sold. This is an internal Roblox ID and is not the same as an asset ID.
1492051

**ItemName**
Name of the item that was sold.
Energy Bar

**ItemType**
Type of item that was sold.
Developer Product

**Date**
The day that the sale occurred on.
2020_01_01

**SalesVolume**
Number of sales of the item.
68

**Impressions**
If the row displays ad impressions, this is the number of times the mobile video ad was viewed.
140

**Revenue**
The profit that you made from the item.
80

**RevenueSource**
Whether the revenue was from a sale or an ad impression.
Transactional

**Device**
Type of device the player was on.
Phone

  


## Premium Payouts

The **Premium** tab at the top of the Developer Stats page is related to `articles/premium payouts#payout-data|Premium Payouts` data.



***__Roblox官方链接__:[分析游戏数据](https://developer.roblox.com/zh-cn/articles/Developer-Stats)