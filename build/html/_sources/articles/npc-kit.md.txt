# NPC 套组 
Time:<em>15  分钟</em>

NPC（非玩家角色）可以为游戏增加很多深度。您可以自定义以下所有 NPC 的外观、修改它们的行为，还可以让僵尸/士兵守卫一个区域。

要在游戏中使用 NPC，请遵循以下步骤：

  1. 选择以下其中之一：

![](https://developer.roblox.com/assets/bltadcabf0fb6dc2fa4/Endorsed-NPC-Zombie.jpg)[ 流涎僵尸](https://www.roblox.com/library/3924238625/Drooling-Zombie-Rthro)

![](https://developer.roblox.com/assets/blt953ce09dabc0b9bf/Endorsed-NPC-Soldiers.jpg)[ 士兵](https://www.roblox.com/library/3924234975/Soldiers-Rthro)

![](https://developer.roblox.com/assets/bltf1ad85473508277a/Endorsed-NPC-RO-01-Robots.jpg)[ RO-01 机器人](https://www.roblox.com/library/3924232032/RO-01-Robots)

![](https://developer.roblox.com/assets/blt78de6767d81f4a73/Endorsed-NPC-NP-C-9000-Robots.jpg)[ NP-C 9000 机器人](https://www.roblox.com/library/3924229481/Robots)

  2. 在 NPC 的物品页面上，点击绿色的 **Get**（获取）按钮并确认交易。
  3. 在 Roblox Studio 中，打开工具箱（**View（视图）** → **Toolbox（工具箱）**）。
  4. 选择工具箱 **Inventory**（物品栏）部分。
![](https://developer.roblox.com/assets/blt7d482aecd878107e/Toolbox-Select-Inventory.png)



  5. 找到 NPC 并单击将其添加到场景中。

## 角色结构

各个 NPC 的结构如下所示。注意其模型不一定包含列出的所有对象。

[NPC] (`Model`)

Animations (`Folder`) — 包含僵尸和士兵角色的额外动画。

AttackAnimation (`Animation`) — 当角色试图对另一个角色造成伤害时播放。

DeathAnimation (`Animation`) — 角色死亡时播放。

InitialPoses (`Folder`) — 包含姿势信息。

Animate (`Script`) — 在人物模型上加载和播放动画。

ScaleDampeningPercent (`NumberValue`) — 定义缩放角色时动画速度变化的方式（小于** 1** 表示动画播放速度和角色缩放成反比）。

PlayEmote (`BindableFunction`) — 可以由其它脚本调用来强制采用姿势。

[Pose] (`StringValue`) — 代表一个可播放动画类别，比如**闲置**、**跳跃**、**行走**等等。

[Animation] (`Animation`) — 定义制作姿势时加载到人物模型上的动画。

Weight (`NumberValue`) — 用于在采用姿势期间，从多个动画中选择一个动画播放；通常用于丰富闲置姿势和舞蹈姿势。

[Accessory] (`Accessory`) — 多种 NPC [饰品](https://www.roblox.com/catalog/?Category=11&Subcategory=19)之一，比如帽子和武器等。

Health (`Script`) — 逐渐回复 `Humanoid` 的生命值。禁用后角色则不能回复生命值。

Humanoid (`Humanoid`) — 管理 `Humanoid/Health|Health`、`Humanoid/WalkSpeed|WalkSpeed`、`Humanoid/DisplayDistanceType|DisplayDistanceType` 等。

Animator (`Animator`) — 使用 `AnimationTrack|AnimationTrack` 管理角色上的 `Animation|Animation`。

NPC (`Script`) — 定义角色专属的 行为，比如咆哮、攻击等等。

Maid (`ModuleScript`) — 定义一个类别，用于释放已使用的资源。

Ragdoll (`ModuleScript`) — 定义一个函数，该函数可以将角色转换为一具松散但受物理影响的身体。

RigTypes (`ModuleScript`) — 定义在不同的角色模型关节中使用的辅助函数。

RbxNpcSounds (`Script`) — 定义和管理与角色音效相关的行为，如奔跑、死亡等。

[BodyParts] (`BasePart|BaseParts`) — 通过`Motor6D` 或约束对象附加到 HumanoidRootPart 或相邻身体部件的各种角色身体部件。

AvatarPartScaleType (`StringValue`) — 决定部件缩放的方式；可以是 **Classic**、**ProportionsNormal** 或者 **ProportionsSlender**。

OriginalSize (`Vector3Value`) — 决定当角色比例为 **1** 时部件的大小。

[Attachment] (`Attachment`) — 定义相对于单个部件的点。脚本、特效和对象（如 `Tool`（工具）或 `Accessory`（附件））在移动时可以利用该点。



***__Roblox官方链接__:[NPC 套组](https://developer.roblox.com/zh-cn/articles/npc-kit)