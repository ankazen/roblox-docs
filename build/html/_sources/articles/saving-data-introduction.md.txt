# 保存数据：简介 
Time:<em>5  分钟</em>

`DataStoreService` 保存在游戏进程之间保留的数据，例如玩家的金钱、经验值或物品栏中的道具等等。保存的数据可从游戏中的任何场景访问，也可跨服务器访问。

## 启用 Studio 访问

默认情况下，在 Studio 中测试的游戏无法访问数据存储，所以您必须手动**启用**。

  1. 在 **Home（主页）**选项卡中，打开 **Game Settings（游戏设置）**窗口。如果您的游戏尚未发布，您将被询问是否发布。
![](https://developer.roblox.com/assets/bltd6af44e38b951d0a/Game-Settings.png)



  2. 在 **Security（安全）**部分，打开 **Enable Studio Access to API Services（启用 Studio 访问 API 服务）**.
  3. 点击 **Save（保存）**来注册您的变更。

如果游戏已上线且有活跃玩家，通过 Studio 访问数据存储时请谨慎。Studio 访问与上线的游戏相同的数据，所以建议您在独立的测试版本中访问数据存储。 

## 访问数据存储

数据存储最初通过一个独特的**名称**创建并访问。例如，一个名为 **PlayerGold** 的数据存储可以在游戏进程中与进程之间存储玩家的金钱。

  1. 在名为 **DataStoreTest** 的 `ServerScriptService` 内创建一个新的 `Script`。
![](https://developer.roblox.com/assets/blta132586c9ea9dcc4/DataStoreTest-Object.png)



  2. 数据存储通过 `DataStoreService` 进行管理，所以请在第一行获取服务。

访问数据存储 ```    
    
    local DataStoreService = game:GetService("DataStoreService")


```
  3. 用 `"PlayerGold"` 字符串调用 `DataStoreService/GetDataStore|DataStoreService:GetDataStore()`。如果已存在，这将访问 **PlayerGold** 数据存储，否则将新建。

访问数据存储 ```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local goldStore = DataStoreService:GetDataStore("PlayerGold")


```
##### 数据排序 »

Data returned by `DataStoreService/GetDataStore|GetDataStore()` is not sorted. This isn’t a concern when reading specific individual keys, but sorted data fetched via `DataStoreService/GetOrderedDataStore|GetOrderedDataStore()` is essential for user interfaces like persistent leaderboards.

  


## 保存数据

数据存储本质上是字典，就像 Lua 表。数据存储中的每个**值**都由一个独特的**键**索引，例如玩家的独特 `Player/UserId|UserId` 或一个命名的字符串。

玩家数据 游戏数据

Key Value

31250608
50

351675979
20

505306092
78000

Key Value

ActiveSpecialEvent
SummerParty2

ActivePromoCode
BONUS123

CanAccessPartyPlace
true

要将数据保存进 **PlayerGold** 数据存储，请用键和一个值调用 `GlobalDataStore/SetAsync|SetAsync()`：

保存至数据存储 ```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local goldStore = DataStoreService:GetDataStore("PlayerGold")
    
    -- 数据存储键和值
    local playerUserID = 505306092
    local playerGold = 250
    
    -- 设置数据存储键
    local setSuccess, errorMessage = pcall(function()
    	goldStore:SetAsync(playerUserID, playerGold)
    end)
    if not setSuccess then
    	warn(errorMessage)
    end


```
类似`GlobalDataStore/SetAsync|SetAsync()`这种访问数据存储内容的函数是网络调用，并且有时可能会失败。如上图所示，您应当将这些调用打包在`pcall()`中以捕获和处理错误。关于错误处理的详情，请参见`articles/Datastore Errors|此文`。 

对数据存储键的请求置于队列中。如果短时间内有对同一个键的大量请求，队列可能会爆满，使后续的请求被丢弃。所以与其在玩家每次拾取金钱时更新，不如将玩家的金钱存在一个表中并偶尔更新数据存储，例如当玩家离开时（`Players/PlayerRemoving|Players.PlayerRemoving`事件）。

## 读取数据

要从数据存储中读取数据，请用需要的键名称调用 `GlobalDataStore/GetAsync|GetAsync()`：

从数据存储中读取 ```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local goldStore = DataStoreService:GetDataStore("PlayerGold")
    
    -- 数据存储键和值
    local playerUserID = 505306092
    local playerGold = 250
    
    -- 设置数据存储键
    local setSuccess, errorMessage = pcall(function()
    	goldStore:SetAsync(playerUserID, playerGold)
    end)
    if not setSuccess then
    	warn(errorMessage)
    end
    
    -- 读取数据存储键
    local getSuccess, currentGold = pcall(function()
    	return goldStore:GetAsync(playerUserID)
    end)
    if getSuccess then
    	print(currentGold)
    end


```
## 测试

当您完成脚本后，便可测试 **PlayerGold** 数据存储。

  1. 点击 **Run（运行）**按钮。
![](https://developer.roblox.com/assets/blt806e39d14fd0bf40/Play-Button-Upper.png)



  2. 如果一切正确，`playerGold` 值应该会在 **Output（输出）**窗口中打印出来。注意这可能需要几秒钟的时间，因为函数必须连接至数据存储服务器。
![](https://developer.roblox.com/assets/blt3e151e0aec8a4260/DataStoreTest-Output.png)



## 示例场景

现在您已掌握了数据存储的基本用法，请在示例场景中测试一下。

![](https://developer.roblox.com/assets/blt377b3c22f1e549a2/Sample-Place-Gold-Rush.jpg)

#### [淘金热](https://www.roblox.com/games/5268331031/Gold-Rush)

尽可能多地收集金块，您的个人最佳纪录将在游戏进程之间保存。



***__Roblox官方链接__:[保存数据：简介](https://developer.roblox.com/zh-cn/articles/saving-data-introduction)