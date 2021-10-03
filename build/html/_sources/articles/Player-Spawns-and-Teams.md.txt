# 角色生成与团队 
Time:<em>10  分钟</em>

在 Roblox 中，`SpawnLocation` 对象用于确定玩家角色开始游戏时或被击败后重生时出现的地点。同时也可以用于将隶属不同队伍的玩家角色生成在特定的不同位置。

## 插入生成点

若希望在 Studio 中插入生成点，请选择 **Model（模型）**选项卡，单击 **Spawn（生成）**按钮：

![](https://developer.roblox.com/assets/blta6b81380d6f6d389/Create-SpawnLocation.png)



##### 隐藏生成地块

如有需求，开发者可以按照以下步骤“隐藏” `SpawnLocation` 对象：

  1. 将 SpawnLocation 对象的 **Transparency** 属性设置为 **1**，让其不可见。
  2. 关闭该对象的 **CanCollide** 属性，让玩家角色不会看起来悬浮在半空中。
  3. 删除其子 **Decal** 对象。

  


##### 停用力场

默认情况下，角色生成时带有时长为 10 秒的 `ForceField`（力场），可以保护其不会在生成点被恶意杀死。不过此内置防护机制仅限于防范 `Explosion|Explosion`（爆炸）和 `Humanoid/TakeDamage|Humanoid:TakeDamage()` 所造成的伤害，**并不能**阻止脚本直接减少玩家的 `Humanoid/Health`。

若希望完全停用力场，请将生成点的 **Forcefield** → **Duration** 属性设为 **0**。

  


## 实现 Team（团队）

`Teams` 服务不但可以用来添加队伍功能，还与玩家的角色生成密切相关。队伍名称、队伍颜色以及队伍中所有玩家等信息都可以在游戏中的 `articles/Leaderboards|排行榜`上看到。

### 添加 Teams 服务

`Teams` 服务并未默认包含至游戏中，需要开发者自行添加：

  1. 选中 **Model**（模型）选项卡，单击 **Advanced**（高级）区域中的 **Service**（服务）按钮（![](https://developer.roblox.com/assets/bltd84657899c051ea0/Service-Icon.png)

）。
  2. 选择 **Teams**（团队）后单击 **Insert**（插入）。完成操作后，管理器会获得一个名为 **Teams** 的新对象。
![](https://developer.roblox.com/assets/bltd7764f2b5904de10/Explorer-Teams-Object.png)



### 添加新队伍

添加 `Teams` 服务后就可以创建新队伍了。将鼠标指针悬停于 **Teams** 对象上，单击 ![](https://developer.roblox.com/assets/blt0dd97240c2a0db2a/Explorer-Plus-Icon.png)

 图标后选择 **Team**（队伍）。

![](https://developer.roblox.com/assets/bltba4c76aede1f1ba6/New-Team-Object.png)



添加队伍之后：

  1. 将队伍的 **Name**（名称）改成一个合适的值。
![](https://developer.roblox.com/assets/bltc6de1106c5d988f5/Change-Team-Name.png)



  2. 给队伍分配唯一的 **TeamColor**，该设置可以和 `SpawnLocation` 对象一起使用。
![](https://developer.roblox.com/assets/blt678b45eb6caedd01/Set-TeamColor.png)



队伍 **Name**（名称）和选定的 **TeamColor**（队伍颜色）都会在游戏的`articles/Leaderboards|排行榜`中出现，因此需要对其进行合理设置。在此示例中，“蓝队”就被分配了极为适合队名的颜色：“Really blue”（深蓝色）。 

### 配置生成点

在默认情况下，生成点为**中立*，允许任何玩家在此处生成。但在大多数游戏里，各个队伍都拥有独立的“领地”与生成点，或者被类似`articles/Collision Filtering Team Doors|队伍专用门`的物理屏障所分隔。

若希望为特定队伍锁定专用生成点，请遵循以下步骤：

  1. 选中 `SpawnLocation` 对象。
  2. 在 Properties（属性）窗口中禁用其 **Neutral**（中立）属性。
  3. 将其 **TeamColor** 属性设置为你所创建队伍的对应颜色。
![](https://developer.roblox.com/assets/blt29eb9250256e2382/Set-SpawnLocation-TeamColor.png)



需要注意的是，生成点的 **TeamColor** 与其 **BrickColor** 或 **Color** 属性（这两个属性代表对象的外观颜色，与队伍并无关联）是不同的。 

### 分配玩家

在默认情况下，Roblox 会将新玩家**自动分配**到目前人数最少的队伍中。若希望将玩家分配至你所配置的特定队伍与生成点，请遵循以下步骤：

  1. 在 **Teams** 服务中选择每个 `Team` 对象并**禁用**其 `Team/AutoAssignable|AutoAssignable` 属性。
![](https://developer.roblox.com/assets/blt19df1cdc7ebc1f6f/Disable-Team-AutoAssignable.png)



  2. 要将玩家分配至指定团队，需要将该玩家的 `Player/Team` 属性改为队伍的名称，例如 `Teams["Blue Team"]`。若想达成该目的，有几种不同的方法。举例来说，可以如下方 [Team Picker](https://www.roblox.com/games/3705707230/Team-Picker)（队伍选择器）示例所示，使用选择队伍的 GUI。同时也可以创建含有多个`articles/How to teleport within a Place|传送器`的大厅，将玩家分配至不同队伍。

![](https://developer.roblox.com/assets/blt11c40ad39c14f32e/TeamPicker.jpg)

#### [Team Picker（队伍选择器）示例](https://www.roblox.com/games/3705707230/Team-Picker)

从 GUI 选择器所显示的 4 个队伍中选中 1 个，并从该队伍对应的生成点进行角色生成。



***__Roblox官方链接__:[角色生成与团队](https://developer.roblox.com/zh-cn/articles/Player-Spawns-and-Teams)