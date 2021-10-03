# 添加团队 
Time:<em>5  分钟</em>

Teams（团队）是一项向 Roblox 游戏添加团队功能的游戏服务。团队名称和颜色以及该团队的所有玩家都可以在游戏排行榜上看到。

## 启用 Teams（团队）

若要启用团队，请遵循以下说明：

  1. 单击“Model（模型）”选项卡，然后单击“Advanced（高级）”部分中的“Service（服务）”按钮。

![InsertService.png](https://developer.roblox.com/assets/bltc9d73beb913130dd/InsertService.png)



  2. 选择 **Teams（团队）**，然后单击“Insert（插入）”。

![InsertTeams.png](https://developer.roblox.com/assets/bltc3751d7f858c9668/InsertTeams.png)



完成后，管理器将获得一个名为 Teams 的新对象。

![TeamsInExplorer.png](https://developer.roblox.com/assets/blt3328bd065a52ad0f/TeamsInExplorer.png)



## 添加新团队

`Teams` 服务被添加到游戏中后，你便可以通过在管理器中右键单击 **Teams（团队）**并选择“Insert Object（插入对象）>Team（团队）”来添加新的 `Team`。

可以在“Properties（属性）”窗口中更改团队的名称。在管理器中选择要更改的团队，然后确保“Properties（属性）”已打开。可以使用 `Instance/Name` 字段更改名称。使用 `Team/TeamColor` 字段可以更改团队的颜色。

![TeamProperties.png](https://developer.roblox.com/assets/bltdfe42f25c531cbea/TeamProperties.png)



## 团队的重生点位置

`SpawnLocation` 是一个与团队紧密联系的 Roblox 对象。当玩家加入游戏或死亡后重生时，其角色将在与玩家团队具有相同 TeamColor 的 `SpawnLocation` 处生成。

你可以通过单击“Model（模型）”选项卡，然后点击“Gameplay（游戏）”部分中的“Spawn（生成点）”按钮来创建 SpawnLocation。如果你单击 SpawnLocation，然后打开“Properties（属性）”窗口，你可以在“Teams（团队）”部分中看到生成点的 `SpawnLocation/TeamColor`。请记住，这与 SpawnLocation 的 `BasePart/BrickColor` 不同！BrickColor 只是部件的显示颜色，与团队无关。为了避免混淆，通常惯例是确保 SpawnLocation 的 `BasePart/BrickColor` 与 `SpawnLocation/TeamColor` 相同。

![SpawnTeamColor.png](https://developer.roblox.com/assets/blt59381207e52a699c/SpawnTeamColor.png)



如果你在某个 SpawnLocation 上打开 `SpawnLocation/AllowTeamChangeOnTouch` 设置，则玩家可以更改团队。如果某个玩家踩到了此重生点，那么这个玩家就会加入与这个重生点关联的团队。

## 自动将玩家分配到团队

默认情况下，Roblox 将自动为团队分配新玩家。当玩家加入团队游戏时，该游戏会将该玩家放入玩家人数最少的团队。如果你不希望玩家自动加入团队，请选择该团队，然后打开“Properties（属性）”窗口。 确保关闭 `Team/AutoAssignable`。

![AutoAssignableOff.png](https://developer.roblox.com/assets/bltc4c06059fca7bd87/AutoAssignableOff.png)





***__Roblox官方链接__:[添加团队](https://developer.roblox.com/zh-cn/articles/Team-Basics-on-Roblox)