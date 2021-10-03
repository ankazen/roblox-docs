# 数据储存 
Time:<em>15  分钟</em>

**Data Store**（数据存储）是 Roblox 为游戏提供的存储功能，可以用来保存需要在玩家退出游戏后仍然留存的数据，包括玩家物品栏中的物品、当前经验值或几乎任何其他需要保留的数据。

数据存储在**单个游戏**中是共享的，因此游戏中的任何场景，包括不同服务器上的场景，都可以访问和更改相同的数据。

## 结构

数据存储本质上是一个字典，就像 Lua 表格一样。数据存储中的每个值都可以通过唯一的键进行索引，比如使用玩家的 `Player/UserId|UserId`：

键 值

Player_1234
50

Player_2345
20

Player_7462
78000

Player_8934
1200

Player_10345
0

## 数据存储访问

数据存储由 `DataStoreService` 管理，因此开发者编写的脚本必须先获取该服务，然后才能执行其他操作。

```    
    
    local DataStoreService = game:GetService("DataStoreService")


```
将 `DataStoreService` 写入脚本之后，就可以使用 `DataStoreService/GetDataStore|GetDataStore()` 函数并用数据储存的**名称**对其进行访问。例如：

```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local experienceStore = DataStoreService:GetDataStore("PlayerExperience")


```
数据储存只能由服务器通过 `Script|Script` 访问。尝试从客户端通过 `LocalScript` 访问会导致错误。 

## 管理数据储存

### 设置数据

`GlobalDataStore/SetAsync|SetAsync()` 可以设置新的数据储存条目的值。此函数需要条目的**键名**和要设置的**值**。

```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local experienceStore = DataStoreService:GetDataStore("PlayerExperience")
    
    local success, err = pcall(function()
    	experienceStore:SetAsync("Player_1234", 50)
    end)
    
    if success then
    	print("Success!")
    end


```
诸如 `GlobalDataStore/SetAsync|SetAsync()` 等通过网络访问数据储存内容的调用有时会失败。正如我们前面说的，建议将这些调用打包在 `pcall()` 中，以捕获和处理所有错误。 

使用 `GlobalDataStore/SetAsync|SetAsync()` 拥有一定的潜在的风险，因为其会覆盖任何条目中的当前值。如果开发者想要更新一个已有的条目，推荐使用 `GlobalDataStore/UpdateAsync|UpdateAsync()`，因为此函数在进行更改前会考虑旧值。 

### 读取数据

`GlobalDataStore/GetAsync|GetAsync()` 函数可以通过数据储存条目的键名来获取该条目的值。

```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local experienceStore = DataStoreService:GetDataStore("PlayerExperience")
    
    local success, currentExperience = pcall(function()
    	return experienceStore:GetAsync("Player_1234")
    end)
    
    if success then
    	print("Current Experience:", currentExperience)
    end


```
### 数据增量

`GlobalDataStore/IncrementAsync|IncrementAsync()` 可以更改数据存储中的一个**数字值**。此函数需要条目的键名和数值增量。

```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local experienceStore = DataStoreService:GetDataStore("PlayerExperience")
    
    local success, newExperience = pcall(function()
    	return experienceStore:IncrementAsync("Player_1234", 1)
    end)
    
    if success then
    	print("New Experience:", newExperience)
    end


```
### 更新数据

`GlobalDataStore/UpdateAsync|UpdateAsync()` 可以更改数据存储中存储的任何值。此函数需要条目的键名以及一个定义条目更新方式的**函数**。此函数根据您定义的逻辑获取当前值并返回新值。

```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local nicknameStore = DataStoreService:GetDataStore("Nicknames")
     
    local function makeNameUpper(currentName)
    	local newName = string.upper(currentName)
    	return newName
    end
     
    local success, newName = pcall(function()
    	return nicknameStore:UpdateAsync("Player_1234", makeNameUpper)
    end)
    
    if success then
    	print("Uppercase Name:", newName)
    end


```
传递给 `GlobalDataStore/UpdateAsync|UpdateAsync()` 的函数**不**允许暂停，也就是说其不能包含任何例如 `wait()` 的暂停函数。 

### 删除数据

`GlobalDataStore/RemoveAsync|RemoveAsync()` 可以删除任何一条条目，且返回该键对应的值。

```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local nicknameStore = DataStoreService:GetDataStore("Nicknames")
    
    local success, nickname = pcall(function()
    	return nicknameStore:RemoveAsync("Player_1234")
    end)
    
    if success then
    	print("Removed Nickname:", nickname)
    end


```
## 有序数据存储

常规数据存储不会对其内容进行排序。大多数游戏并不需要这种功能，但有时以有序的方式获取数据也是有用的，比如排行榜的统计数据。

`OrderedDataStore`（有序数据存储）是一种特殊类型的数据存储，它可以：

  * 轻松按排序返回内容。
  * 一次请求返回多条记录（常规数据存储一次只能请求一个条目)。

有序数据存储使用与常规数据存储相同的函数，包括 `GlobalDataStore/GetAsync|GetAsync()`、`GlobalDataStore/SetAsync|SetAsync()`、`GlobalDataStore/UpdateAsync|UpdateAsync()` 等。此外，它还提供了 `OrderedDataStore/GetSortedAsync|GetSortedAsync()` 函数，该函数接受几个参数：返回的 `DataStorePages` 对象的“分页大小”、排序顺序和最小/最大值。

假设有一个由五个角色及其年龄填充的有序数据存储，此示例将数据按降序排序到每页 3 个条目的页面中，然后循环遍历这些页面并输出每个角色的姓名/年龄。

```    
    
    local DataStoreService = game:GetService("DataStoreService")
    local characterAgeStore = DataStoreService:GetOrderedDataStore("CharacterAges")
    
    -- 填充有序数据存储
    characterAgeStore:SetAsync("Mars", 19)
    characterAgeStore:SetAsync("Janus", 20)
    characterAgeStore:SetAsync("Diana", 18)
    characterAgeStore:SetAsync("Venus", 25)
    characterAgeStore:SetAsync("Neptune", 62)
    
    -- 将数据排列到每页三个条目的页面中（降序）
    local pages = characterAgeStore:GetSortedAsync(false, 3)
    
    while true do
    	-- 获取当前（第一个）页面
    	local data = pages:GetCurrentPage()
    	-- 遍历页面上的所有键值对
    	for _, entry in pairs(data) do
    		print(entry.key .. ":" .. tostring(entry.value))
    	end
    	-- 检查是否已经到达最后一页
    	if pages.IsFinished then
    		break
    	else
    		print("----------------")
    		-- 进行下一页
    		pages:AdvanceToNextPageAsync()
    	end
    end
    
    
    Neptune: 62
    Venus: 25
    Janus: 20
    ----------------
    Mars: 19
    Diana: 18

```
## 限制、排队和错误处理

像所有网络调用一样，对数据存储的请求有时可能由于连接不良或其他问题而失败。正如在整篇文章中所看到的那样，将数据储存命令打包到 `pcall()` 中以处理任何错误是很有必要的。开发者可以将返回的带有错误代码的数据储存消息和`Articles/Datastore Errors|数据存储错误和限制`中的表格进行交叉比对。

此外，数据存储模型也有应用的限制。如果游戏超出这些限制，Roblox 引擎将自动限制游戏的数据存储使用，导致数据请求花费更长时间。这些请求会被放入队列中，这将在 `Articles/Datastore Errors` 文章中进一步描述。

## 在 Studio 中使用数据储存

默认情况下，Studio 中模拟的场景没有数据储存的访问权限，所以在 Studio 中调用 `GlobalDataStore/SetAsync|SetAsync()` 或 `GlobalDataStore/GetAsync|GetAsync()` 这样的请求函数都会导致错误。

如果需要，开发者**可以**在 Studio 中启用数据存储，如下所示：

1.在 **Home**（主页）选项卡中，打开 **Game Settings**（游戏设置）窗口。

![](https://developer.roblox.com/assets/bltd6af44e38b951d0a/Game-Settings.png)



2.在 **Options**（选项）部分，启用 **Enable Studio Access to API Services**（允许 Studio 访问 API 服务）。  
3.单击 **Save**（保存）应用更改。

访问 Studio 中的数据存储对于实时游戏来说可能很危险，因为 Studio 访问的数据存储与客户端应用程序相同。为避免覆盖制作数据，开发者**不应**为实时游戏启用此设置，而应为游戏的单独测试版本启用此设置。 

如果开发者并非通过 Roblox 网站编辑场景（例如使用本地的 `.rbxl` 文件等)，则需要在**命令栏**中调用`DataModel/SetPlaceId|SetPlaceId()`，然后 Studio 中的游戏才能访问数据存储。 



***__Roblox官方链接__:[数据储存](https://developer.roblox.com/zh-cn/articles/Data-store)