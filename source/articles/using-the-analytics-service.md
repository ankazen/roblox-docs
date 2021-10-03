# 使用 PlayFab 分析 
Time:<em>5  分钟</em>

游戏发行后，开发者可以轻易通过`articles/introduction to analytics|分析工具`中的内置 `AnalyticsService` 和 [PlayFab](https://developer.rblx.playfab.com/en-US/sign-up) 对其进行持续监控与改进。

## PlayFab 设置

### 获取 API Key（接口秘钥）

参与 PlayFab 内测的开发者会收到含有注册账号链接的邮件。注册完毕后登陆至 PlayFab 仪表板，游戏的 API key 就在其标题下方。

![](https://developer.roblox.com/assets/blt487d66f618a48946/PlayFab-Key.png)



### 添加用户

若想从 PlayFab 仪表板中添加更多用户，请遵循以下步骤：

  1. 前往仪表板主页。
  2. 单击 Studio 名称右侧的 ![](https://developer.roblox.com/assets/blt173a1a863c7190a4/PlayFab-Dots-Icon.png)

 图标，从下拉框中选择 **Users**（用户）。
  3. 在下一页中单击 **ADD USER**（添加用户）。
![](https://developer.roblox.com/assets/blt0f2defb295f8b6e7/PlayFab-Add-User.png)



## AnalyticsService 设置

在开始使用 `AnalyticsService` 之前，开发者须按下列步骤设置 API Key：

  1. 在 Roblox Studio 中，从**View**（视图）选项卡中打开**Command Bar**（命令栏）。
  2. 键入下列指令来设置 `AnalyticsService/ApiKey|AnalyticsService.ApiKey` 属性（用开发者的唯一 API Key 取代命令中的 `API_KEY` ）。完成后秘钥将会被储存并与未来所有事件一起发送。

```    
    
    local AnalyticsService = game:GetService("AnalyticsService")
    AnalyticsService.ApiKey = "API_KEY"


```
## 发送事件

`AnalyticsService` 允许开发者汇报自定义游戏中事件，包括用户选择自己最喜爱的战场或使用某件物品/对象的频率等。

要将某个自定义事件汇报给 PlayFab，可以从 `Script` 或者 `ModuleScript` 中使用 `AnalyticsService/FireEvent|FireEvent()` 方法，指定一个**类别**和**值**。注意传递过去的值可以是字符串、数字或存有多个值的表格。

```    
    
    local AnalyticsService = game:GetService("AnalyticsService")
    
    -- 事件参数
    local eventCategory = "ItemPurchased"
    local eventValue = {
    	ItemName = "Ice Wand",
    	ItemPrice = 50
    }
    -- 触发事件
    AnalyticsService:FireEvent(eventCategory, eventValue)


```
为了方便开发者的工作，部分基础的玩家周期数据会自动汇报给 PlayFab，包括新玩家加入游戏的时间等。 

为了更方便的管理分析数据，开发者可以考虑使用 `ModuleScript`，将其转换为在游戏每个场景中都能快速进行更新的`articles/roblox packages|套装`。 

* * *

如本文所述，分析数据可以帮助开发者监控玩家行为并微调游戏体验。在了解如何连接 PlayFab 后，请查看下列文章，加深对基础概念的理解。



***__Roblox官方链接__:[使用 PlayFab 分析](https://developer.roblox.com/zh-cn/articles/using-the-analytics-service)