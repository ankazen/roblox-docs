# 认可武器 
Time:<em>30  分钟</em>

![](https://developer.roblox.com/assets/blt5bfeb15605969ee9/Endorsed-Weapons-Banner.jpg)

为了帮助您创造有竞争力的战斗体验，我们有几种**认可武器**可供您在任何游戏中使用。核心系统以使用投射物的越肩视角镜头的武器为特色，将投射物速度设置得足够高可以模拟激光枪等射线投射武器。

要在您的游戏中使用认可武器：

  1. 在下列武器中选择其中之一：

![](https://developer.roblox.com/assets/blt326b57c590737740/Endorsed-Weapon-Pistol.jpg)[ 手枪](CATALOG_ITEM_PISTOL)

![](https://developer.roblox.com/assets/bltd84946701c009ae1/Endorsed-Weapon-Shotgun.jpg)[ 霰弹枪](CATALOG_ITEM_SHOTGUN)

![](https://developer.roblox.com/assets/blt379012a5f19fded3/Endorsed-Weapon-AR.jpg)[ 突击步枪](CATALOG_ITEM_ASSAULT_RIFLE)

![](https://developer.roblox.com/assets/blt40936fd7354b1feb/Endorsed-Weapon-Submachine-Gun.jpg)[ 冲锋枪](CATALOG_ITEM_SUBMACHINE_GUN)

![](https://developer.roblox.com/assets/blt6880301740f5ccfe/Endorsed-Weapon-Sniper-Rifle.jpg)[ 狙击步枪](CATALOG_ITEM_SNIPER_RIFLE)

![](https://developer.roblox.com/assets/blt92032747b444070c/Endorsed-Weapon-Crossbow.jpg)[ 十字弓](CATALOG_ITEM_CROSSBOW)

![](https://developer.roblox.com/assets/bltd2b1885af0ecee8d/Endorsed-Weapon-Grenade-Launcher.jpg)[ 榴弹枪](CATALOG_ITEM_GRENADE_LAUNCHER)

![](https://developer.roblox.com/assets/blt92b327d7afc16971/Endorsed-Weapon-Rocket-Launcher.jpg)[ 火箭筒](CATALOG_ITEM_ROCKET_LAUNCHER)

![](https://developer.roblox.com/assets/blt0c808b13a893369c/Endorsed-Weapon-Railgun.jpg)[ 磁轨炮](CATALOG_ITEM_RAILGUN)

  2. 在武器的物品页面上，点击绿色的 **Get**（获取）按钮并确认交易。
  3. 在 Roblox Studio 中，打开工具箱（**View（视图）** → **Toolbox（工具箱）**）。
  4. 选择工具箱 **Inventory**（物品栏）部分。
![](https://developer.roblox.com/assets/blt7d482aecd878107e/Toolbox-Select-Inventory.png)



  5. 找到武器并单击将其添加到场景中，当提示是否将该工具放入新手包时，如果您希望玩家使用该武器开始游戏，请点击**是**，或者单击**否**，即可将该武器作为拾取放入游戏世界。

##### 第一把认可武器？

Each endorsed weapon contains a complete copy of the entire weapons system, including sounds and decals for all weapons.

![](https://developer.roblox.com/assets/bltfd389b87b21fc0ab/Move-WeaponsSystem-Folder.png)

The first time you bring in an endorsed weapon, move its WeaponsSystem folder into `ReplicatedStorage`. Later, be sure to delete the WeaponsSystem folder from any **new** endorsed weapons you add to avoid confusion while configuring weapon options.

  


## 系统文件夹结构

WeaponsSystem（武器系统）文件夹控制所有的认可武器，其结构如下：

ReplicatedStorage

WeaponsSystem (`Folder`)

Assets (`Folder`)

Animations (`Folder`) 放置武器系统中使用的动画的地方。

Effects (`Folder`)

Casings (`Folder`) 储存所有弹壳的地方。

HitMarks (`Folder`) 储存所有命中痕迹效果的地方。

Shots (`Folder`) 储存所有射击效果的地方。

WeaponsSystemGui (`ScreenGui`) 详情请见 武器系统 GUI。

Configuration (`Folder`) 放置武器系统配置值的地方。

SlowZoomWalkEnabled (`BoolValue`)和冲刺控制有关。

SprintEnabled (`BoolValue`) 和冲刺控制有关。

Libraries (`Folder`) 储存所有其它在武器系统中使用的 `ModuleScript|ModuleScript` 的地方。

WeaponTypes (`Folder`) 定义所有武器系统的地方。

ServerWeaponsScript (`Script`) 确保只有一个武器系统实例在运行。

Version (`IntValue`)

ClientWeaponsScript (`LocalScript`) 确保只有一个武器系统实例在运行。

NetworkingCallbacks (`ModuleScript`)

WeaponData (`RemoteEvent`)

WeaponsSystem (`ModuleScript`)

在 WeaponsSystem 文件夹中，不同功能由以下各 `ModuleScript|ModuleScript` 分别控制：

功能 主要处理位置

**武器功能**

  * WeaponsSystem
  * Libraries/BaseWeapon
  * WeaponTypes/BulletWeapon
  * WeaponTypes/BowWeapon

**越肩镜头** (参考)

  * Libraries/ShoulderCamera

**武器 GUI** (参考)

  * Libraries/WeaponsGui
  * Libraries/DirectionalIndicatorGuiManager
  * Libraries/DamageBillboardHandler

##### 冲刺及缩放控制

By default, the weapons system adds “sprint” capability to the game, so players can sprint by holding the Shift key, pushing fully up on the dynamic thumbstick (mobile), or pushing fully up on the left joystick (gamepad). If you want to disable sprinting, set **SprintEnabled** within WeaponsSystem/Configuration to **false**.

The system also reduces player speed while they’re aiming/zooming, although this behavior can be disabled by setting the **SlowZoomWalkEnabled** boolean to **false**.

  


## 修改武器

下面是修改武器或创建新武器所需的所有通用子项，以及要覆盖的所有可选子项。武器选项中有更具体的选项。

##### 对象/命名规则

Throughout this documentation, note the following object and naming rules:

  * When something is specified as a `BasePart` such as "**Arrow** (`BasePart`)," the object type just needs to inherit from `BasePart`, so it can be a `Part`, `MeshPart`, etc. However, if something is noted as a specific inherited type such as "**Handle** (`Part`)," that object **must** be a `Part`.
  * Square brackets **[]** refer to the object in general and the name doesn't matter. For example, **[Model]** refers to the weapon's `Model` and you can rename it to whatever makes sense.

  


[Weapon] (`Tool`) 和在玩家背包里显示的一样命名。

WeaponType (`StringValue`) （必须） — WeaponsSystem/WeaponTypes 文件夹中对应的 `ModuleScript` 的名称（**BulletWeapon** 和 **BowWeapon** 是唯二的选项，除非您添加了新的武器类型）。

[WeaponModel] (`Model`) （必须）

一个或多个 `BasePart|BaseParts` （必须） — 这些组成了物理武器模型，其中一个应该设置为该模型的 `Model/PrimaryPart|PrimaryPart`。

Descendants of [WeaponModel]: 

  * TipAttachment (`Attachment`) （必须） — 将此附件置于武器模型 `BasePart` 您想让子弹/投射物发出来的地方。
  * HandleAttachment (`Attachment`) （必须） — 将此附件置于武器模型 `BasePart` 您想要接合手柄的地方。
  * Fired (`Sound`) （可选） — 武器开火时播放。
  * Reload (`Sound`) （可选） — 武器装弹时播放。
  * 武器选项的额外子项。

Handle (`Part`) （必须） — 将部件放置在您想让玩家拿着武器的地方。

[Configuration] (`Configuration`) — 放置武器配置项目的地方。请注意，所有项目都有默认值，因此您可以忽略那些不需要更改的项。

AmmoCapacity (`IntValue`) （可选） — "弹夹"可装的最大子弹数；默认为 **30**。请注意子弹是无限的，本项并**不**指定玩家可以携带的子弹数量。

FireMode (`StringValue`) （可选） — 在 **Semiautomatic** （半自动。一次点击射击一次）、 **Automatic** （全自动。按住连续射击）、或 **Burst**（点射。点击以点射出一定数量的子弹，数量取决于 NumBurstShots）中选择。默认为 **Semiautomatic**。

ShotCooldown (`NumberValue`) （可选） — 点击之间最小的等待时间；默认为 **0.1**。对于**全自动**武器，表示每发之间的最小时间间隔。

BurstShotCooldown (`NumberValue`) （可选） — 点射时每发之间的间隔时间；默认为 ShotCooldown 的值，只在您将 FireMode 设为 **Burst** 时生效。

NumBurstShots (`IntValue`) （可选） — 每次点击/点射的射击数；默认为 **3**，只在您将 FireMode 设为 **Burst** 时生效。

HitDamage (`NumberValue`) （可选） — 每次直接命中所造成的伤害；默认为 **10**。

FullDamageDistance (`NumberValue`) （可选） — 射击能够造成完全伤害的最大距离。默认为 **1000**，超过此距离，命中所造成的伤害就越来越低，直到子弹达到 ZeroDamageDistance，此时伤害为零。

ZeroDamageDistance (`NumberValue`) （可选） — 超过或处于此距离的命中造成的伤害为零。默认为 **10000**。

BulletSpeed (`NumberValue`) （可选） — 子弹/投射物飞行的速度；默认为 **1000**。将此值设为比如 **20000** 一样大的值可以模拟激光枪等射线投射武器。

MaxDistance (`NumberValue`) （可选） — 子弹/投射物在消失前可飞行的最大距离；默认为 **2000**。

MinSpread (`NumberValue`) （可选） — 武器扩散的最小值；默认为 **0**。

MaxSpread (`NumberValue`) （可选） — 武器扩散的最大值；默认为 MinSpread 的值。

GravityFactor (`NumberValue`) （可选） — 子弹/投射物受重力的影响量；默认为 **0**。例如，对于[十字弓](CATALOG_ITEM_CROSSBOW)，此值为 **1**，因为箭矢做弧线运动，但对于[火箭筒](CATALOG_ITEM_ROCKET_LAUNCHER)，此值为 **0**，因为火箭做直线运动。

HasScope (`BoolValue`) （可选） — Set to **true** 若您想使用在 武器系统 GUI中定义的倍镜，请设为 true。默认为 **false**。

ReloadAnimation (`StringValue`) （可选） — 在 WeaponsSystem/Assets/Animations 中的装弹动画的名称；默认为 **RifleReload**。

AimTrack (`StringValue`) （可选） — 在 WeaponsSystem/Assets/Animations 中的瞄准动画的名称；默认为 **RifleAim**。

AimZoomTrack (`StringValue`) （可选） — 在 WeaponsSystem/Assets/Animations 中的放大瞄准动画的名称；默认为 **RifleAimDownSights**。

RecoilMin (`NumberValue`) （可选） — 每次射击的最小反冲；默认为 **0.05**。

RecoilMax (`NumberValue`) （可选） — 每次射击的最大反冲；默认为 **0.5**。

TotalRecoilMax (`NumberValue`) （可选） — 累积反冲的最大值（武器的当前反冲不会比此值高）；默认为 **2**。

RecoilDecay (`NumberValue`) （可选） — 反冲的衰减倍数（本质即射击后反冲消失的速度）；默认为 **0.825**。

RecoilDelayTime (`NumberValue`) （可选） — 射击/点击后反冲添加到镜头之前的等待时间；默认为 **0.07**。

StartupTime (`NumberValue`) （可选） — 武器装备后玩家可以射击之前的等待时间；默认为 **0.2**。这可以防止玩家快速连续地用不同的武器开枪。

FiredPlaybackSpeedRange (`NumberValue`) （可选） — 武器的 Fired（射击）音效可以变调的程度。 若您希望音效总是在同一个调播放，请将此设为 **0**，默认为 **0.1**。

NumProjectiles (`NumberValue`) （可选） — 点击一次，子弹/投射物可以同时发射的数量；默认为 **1**。对于诸如[霰弹枪](CATALOG_ITEM_SHOTGUN)一类同时发射多发子弹的武器，此值很有用。请注意，无论此值如何，一次射击始终只使用一颗弹药。

武器选项的额外子项。

## 武器选项

您可以为任何武器添加/修改以下任意数量的选项。请注意有些项是依赖于其他的，例如枪口粒子需要投射物/命中效果和声音必要的子项。

### 枪栓动画和声音

认可武器的**枪栓**是指每次射击时来回移动的部件。

  * 武器 `Model`（模型）的子项：
![](https://developer.roblox.com/assets/blt71c6749646e34c4a/Weapon-Model-Descendants.png)



  * **Bolt** (`BasePart`) （必须） — 动画时实际移动的枪栓。
  * **BoltMotor** (`Motor6D`) （必须） — 用于为枪栓设置动画。请确保将 `JointInstance/Part0|Part0` 设置为武器的 `Model/PrimaryPart|PrimaryPart`，将 `JointInstance/Part1|Part1` 设置为 **Bolt**。****
  * **BoltMotorStart** (`Attachment`) （必须） — 当枪栓处于静止状态时所在的位置。
  * **BoltMotorTarget** (`Attachment`) （必须） — 射击时枪栓所在的位置。
  * **BoltOpenSound** (`Sound`) （可选） — 枪栓打开时播放。
  * **BoltCloseSound** (`Sound`) （可选） — 枪栓关闭时播放。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltd910143fc345c427/Weapon-Configuration-Children.png)



  * **ActionOpenTime** (`NumberValue`) （可选） — 枪栓动画到打开位置所需的时间；默认为 **0.025**。
  * **ActionCloseTime** (`NumberValue`) （可选） — 枪栓动画到关闭位置所需的时间；默认为 **0.075**。

### 弹出弹壳

武器可以包含物理弹壳，这些弹壳在开火时会弹出，然后落在地上。

  * 武器 `Model`（模型）的子项：
![](https://developer.roblox.com/assets/blt71c6749646e34c4a/Weapon-Model-Descendants.png)



  * **CasingEjectPoint** (`Attachment`) （必须） — 将此附件置于武器模型 `BasePart` 上子弹/投射物将会射出的位置。请注意，附件的方向决定了弹壳弹出的方向。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltd910143fc345c427/Weapon-Configuration-Children.png)



  * **CasingEffect** (`StringValue`) （必须） — WeaponsSystem/Assets/Effects/Casings 中的弹壳 `BasePart` 的名称。
  * **CasingEjectSpeedMin** (`NumberValue`) （可选） — 弹壳弹出的最小速度；默认为 **15**。
  *   * **CasingEjectSpeedMax** (`NumberValue`) （可选） — 弹壳弹出的最大速度；默认为 **18**。

  * WeaponsSystem/Assets/Effects/Casings 里的弹壳 `BasePart` 的额外子项：
![](https://developer.roblox.com/assets/blt825b80686ff44ac6/Weapon-CasingHitSound.png)



  * **CasingHitSound** (`Sound`) （可选） — 弹夹落到地上时播放。

### 投射/命中效果和声音

您可以为任何武器指定物理投射物，以及用于命中效果和其他特效的`Sound|声音`、`Beam|光束`和`ParticleEmitter|粒子发射器`。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltc94a1400b4411793/Weapon-Configuration-Children-Grenade-Launcher.png)



  * **ShotEffect** (`StringValue`) （必须） — WeaponsSystem/Assets/Effects/Shots 中储存的射击效果的名称。
  * **ShouldMovePart** (`BoolValue`) （可选） — 若您想让 **ShotEffect** 随投射物一起移动，请设为 **true**，如果不，请设为 **false** ；默认为 **false**。仅当每次射击都有可见对象（如箭矢或火箭）移动时，才能将其设置为 **true**。
  * **BeamFadeTime** (`NumberValue`) （可选） — 子弹/投射物击中某物后 **Beam0** 和 **Beam1** 淡出所需的时间。默认为 `nil`，表示没有代码手动应用的淡入淡出。
  * **BeamWidth0** (`NumberValue`) （可选） — **Attachment0** 处的**Beam0**/**Beam1** 的厚度；默认为 **1.5**。
  * **BeamWidth1** (`NumberValue`) （可选） — **Attachment1** 处的**Beam0**/**Beam1** 的厚度；默认为 **1.8**。
  * **NumHitParticles** (`IntValue`) （可选） — **HitParticles** `ParticleEmitter`（粒子发射器）发射的粒子的数量。默认为 **3**。
  * **HitParticlesUsePartColor** (`BoolValue`) （可选） — 若您希望命中粒子与命中表面有一样的颜色，请设为 **true**。若您不希望命中粒子改变颜色，请设为 **false**。默认为 **true**。

  * 前面部分提到的具体的 **ShotEffect** 的子项（位于 WeaponsSystem/Assets/Effects/Shots 中）：
![](https://developer.roblox.com/assets/blt014b835302d53afe/Weapon-Grenade.png)



  * **Flying** (`Sound`) （可选） — 子弹/投射物飞行时播放。
  * **Beam0** (`Beam`) （可选） — 子弹/投射物轨迹光束的第一个槽。别忘了设置附件（参见跟随的子项）。
  * **Beam1** (`Beam`) （可选） — 子弹/投射物轨迹光束的第二个槽。别忘了设置附件（参见跟随的子项）。
  * **Attachment0** (`Attachment`) （可选） — 轨迹光束的后面；确保将 **Attachment0** 设置在 **Beam0** 和 **Beam1** 上。 
    * **TrailParticles** (`ParticleEmitter`) （可选） — **Attachment0** 的一级子项；子弹/投射物飞行时，这会从 **Attachment0** 里发射。
  * **Attachment1** (`Attachment`) （可选） — 轨迹光束的前面；确保将 **Attachment1** 设置在 **Beam0** 和 **Beam1** 上。 
    * **LeadingParticles** (`ParticleEmitter`) （可选） — **Attachment1** 的一级子项；子弹/投射物飞行时，这会从 **Attachment1** 里发射。
  * **HitEffect** (`Attachment`) （可选） — 与位置无关，当子弹/投射物命中时，其位置将被设为 **Beam0.Attachment1**，因此您必须指定 **Beam0** 及其附件，此项才能正常工作。 
    * **HitSound** (`Sound`) （可选） — **HitEffect** 的一级子项；子弹/投射物命中时播放。
    * **HitParticles** (`ParticleEmitter`) （可选） — **HitEffect** 的一级子项；子弹/投射物命中时发射。
  * 您想作为物理投射物的任何 `Part`/`MeshPart`/`SpecialMesh` （可选）。若您想要使对象可见，确保您将前文提到的 **ShouldMovePart** 设为 **true**。

### 枪口粒子

此选项在武器发射时从武器特定 **TipAttachment** `Attachment`（附件）上的 `ParticleEmitter`（粒子发射器）发射粒子。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltee7d708eab38b55d/Weapon-Configuration-Children-Railgun.png)



  * **ShotEffect** (`StringValue`) （必须） — WeaponsSystem/Assets/Effects/Shots 中储存的射击效果的名称。
  * **NumMuzzleParticles** (`IntValue`) （可选） — 发射的枪口粒子数量；默认为 **50**。

  * 对于特定的射击效果（位于 WeaponsSystem/Assets/Effects/Shots）， 添加一个名为 **MuzzleParticles** 的 `ParticleEmitter`（粒子发射器）：
![](https://developer.roblox.com/assets/blt02953bc2985777a4/Weapon-MuzzleParticles.png)



### 枪口闪光

此选项在武器发射时创建一个 `Beam` 闪光。

  * 武器 `Model`（模型）的子项：
![](https://developer.roblox.com/assets/blt52dfdaccd68ce4c3/Weapon-Model-Descendants-Railgun.png)



  * **MuzzleFlash0** (`Attachment`) （必须） — 用于描述枪口闪光的一侧，位置不重要。
  * **MuzzleFlash1** (`Attachment`) （必须） — 用于描述枪口闪光的反侧，位置不重要。
  * **MuzzleFlash** (`Beam`) （必须） — 确保将 `Beam/Attachment0|Attachment0` 设为 **MuzzleFlash0**，将 `Beam/Attachment1|Attachment1` 设为 **MuzzleFlash1**。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltee7d708eab38b55d/Weapon-Configuration-Children-Railgun.png)



  * **MuzzleFlashTime** (`NumberValue`) （可选） — 枪口闪光显示的时间；默认为 **0.03**。
  * **MuzzleFlashRotation0** (`NumberValue`) （可选） — 枪口闪光的最小旋转；默认为 `-math.pi`。
  * **MuzzleFlashRotation1** (`NumberValue`) （可选） — 枪口闪光的最大旋转；默认为 `math.pi`。
  * **MuzzleFlashSize0** (`NumberValue`) （可选） — 枪口闪光的最小尺寸；默认为 **1**。
  * **MuzzleFlashSize1** (`NumberValue`) （可选） — 枪口闪光的最大尺寸；默认为 **1**。

### 投射物轨迹

此选项会创建从武器到投射物落点的不同长度的轨迹。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltee7d708eab38b55d/Weapon-Configuration-Children-Railgun.png)



  * **TrailLength** (`NumberValue`) （可选） — 子弹/投射物后面的轨迹的长度；默认为 `nil`，表示轨迹的长度由 **TrailLengthFactor** 计算。
  * **TrailLengthFactor** (`NumberValue`) （可选） — 轨迹长度将设置为此值乘以子弹/投射物在最后一帧中移动的距离；默认为 **1**。注意若您设置了 **TrailLength**，此值会被覆盖。
  * **ShowEntireTrailUntilHit** (`BoolValue`) （可选） — 设置为 **true** 将呈现从武器尖端一直到投射物所在位置的轨迹；这将覆盖 **TrailLength** 和 **TrailLengthFactor**，并且只有在投射物击中某些物体时，轨迹才会消失。设置为 **false** 可使用以上两个选项之一计算轨迹长度。默认为 **false**。

### 命中痕迹

这种视觉效果出现在投射物击中的表面上，可用于箭头、弹孔、焦痕等。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltd910143fc345c427/Weapon-Configuration-Children.png)



  * **HitMarkEffect** (`StringValue`) （可选） — WeaponsSystem/Assets/Effects/HitMarks 中储存的命中痕迹效果的名称；默认为 **BulletHole**。
  * **AlignHitMarkToNormal** (`BoolValue`) （可选） — 如果命中痕迹应与命中表面齐平，比如弹孔，则设置为 **true**；如果命中痕迹应从投射物来的方向卡在表面上（如箭头），则设置为 **false**。 默认为 **true**。

  * 前面部分提到的具体的 **HitMarkEffect** 的子项（位于 WeaponsSystem/Assets/Effects/HitMarks）：
![](https://developer.roblox.com/assets/blt085a852732ce4843/Weapon-BulletHole.png)



  * **Glow** (`Decal`) （可选） — 在命中表面上显示为完全不透明，然后迅速变得逐渐透明，就像表面上快速褪色的发光效果一样，可用于在爆炸击中的地方显示一个发光的红色痕迹等状况。
  * **BulletHole** (`Decal`) （可选） — 在命中表面上显示为完全不透明，4 秒之后，在 1 秒内逐渐变为透明。
  * **ImpactBillboard** (`BillboardGui`) （可选） — 在命中表面显示，始终面对玩家。 
    * **Impact** (`ImageLabel`) （可选） — **ImpactBillboard** 的一级子项；开始为完全不透明，在 0.1 秒内逐渐放大为 **ImpactBillboard** 的尺寸，然后缩小为一半大小，在 0.1 内褪至完全透明。 
  * 您想作为物理投射物的任何 `Part`/`MeshPart`/`SpecialMesh` （可选）。例如，添加箭矢 `MeshPart` 并将上面提到的 **AlignHitMarkToNormal** 设置为 **false** 将使箭矢以您射击的方向伸出表面。

### 爆炸投射物

开发者可以为投射物添加 `Explosion` （爆炸）对象，以对落点周围区域内的玩家造成伤害。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltc94a1400b4411793/Weapon-Configuration-Children-Grenade-Launcher.png)



  * **ExplodeOnImpact** (`BoolValue`) （可选） — 如果您希望武器的子弹/投射物在撞击时爆炸，请设置为 **true**，否则设置为 **false**。默认为 **false**。
  * **BlastRadius** (`NumberValue`) （可选） — 爆炸的 `Explosion/BlastRadius|BlastRadius`（爆炸半径）；默认为 **8**。
  * **BlastPressure** (`NumberValue`) （可选） — 爆炸的 `Explosion/BlastPressure|BlastPressure`（爆炸压力）；默认为 **10000**。
  * **BlastDamage** (`NumberValue`) （可选） — 爆炸中心可对物体造成的伤害。注意击中的物体离爆炸中心越远，所受到的伤害就越小。默认为 **100**。

### 充能武器

像[磁轨炮](CATALOG_ITEM_RAILGUN)一类的充能武器每次必须充能完毕才能射击。

  * 武器 `Model`（模型）的子项：
![](https://developer.roblox.com/assets/blt52dfdaccd68ce4c3/Weapon-Model-Descendants-Railgun.png)



  * **Charging** (`Sound`) （可选） — 充能时播放。
  * **Discharging** (`Sound`) （可选） — 释能时播放，例如当武器部分充能时您释放了射击按钮。
  * **ChargeComplete** (`Sound`) （可选） — 武器完全充能时播放。
  * **DischargeComplete** (`Sound`) （可选） — 武器完全释能时播放。
  * **ChargeGlow** (`BasePart`) （可选） — 当武器充能时，这个物体将逐渐变得不透明，在 100% 充能时它将完全不透明。
  * **ChargeCompleteParticles** (`ParticleEmitter`) （可选） — 武器完成充能时发射。此发射器可以是任何模型 `BasePart` 的子项，也可以是 `BasePart` 内的 `Attachment` 的子项。
  * **DischargeCompleteParticles** (`ParticleEmitter`) （可选） — 武器完成释能时发射。此发射器可以是任何模型 `BasePart` 的子项，也可以是 `BasePart` 内的 `Attachment` 的子项。
  * **ChargingParticles** (`ParticleEmitter`) （可选） — 在武器充能时发射。您可以使用多个该名称的发射器，每个发射器都将在充能时发射。此发射器可以是任何模型 `BasePart` 的子项，也可以是 `BasePart` 内的 `Attachment` 的子项。

  * 武器 `Configuration`（配置）的子项：
![](https://developer.roblox.com/assets/bltee7d708eab38b55d/Weapon-Configuration-Children-Railgun.png)



  * **ChargeRate** (`NumberValue`) （必须） — 武器充能的速率。必须指定此值以指示武器使用充能。
  * **DischargeRate** (`NumberValue`) （可选） — 武器释能的速率。默认为 **0**，表示武器不会释放能量。
  * **ChargePassively** (`BoolValue`) （可选） — 如果您希望武器被动充能，以便在您单击时能立即射击，请设置为 **true**；如果要单击/触摸为武器充能，并在充能完毕后立即开火，请设置为 **false**。默认为 **false**。
  * **ChargingParticlesRatePerCharge** (`IntValue`) （可选） — 将从所有 **ChargingParticles** 发射器中发射的粒子数乘以武器的当前充能。默认为 **20**，表示若武器充能 10%，每个 **ChargingParticles** 发射器会发射 2 个粒子（`20*0.1`），若武器充能到 90%，每个发射器将发射 18 个粒子（`20*0.9`）。
  * **FireDischarge** (`NumberValue`) （可选） — 射出一发完全充能后武器将损失的充能量；默认为 **1**。
  * **NumChargeCompleteParticles** (`IntValue`) （可选） — 武器完全充能后，**ChargeCompleteParticles** 发射器发射粒子的数量。默认为 **25**。
  * **NumDischargeCompleteParticles** (`IntValue`) （可选） — 武器完全释能后，**DischargeCompleteParticles** 发射器发射粒子的数量。默认为 **25**。

### 弓武器

如[十字弓](CATALOG_ITEM_CROSSBOW)一类的弓武器可以包含逼真的弦和弓臂构造，以及可视的指向弦的箭矢。

  * 按照充能武器中的规定可将武器制成充能武器。例如，在武器的 `Configuration`（配置）中添加必需的 **ChargeRate** 来规定拉弦速度。此外，还可以考虑在武器的 `Model`（模型）中添加可选的子项，例如为拉弦/弓臂添加一个**充能**声音。
  * 根据修改武器中所述将 **WeaponType** 设为 **BowWeapon**。
  * 武器 `Model`（模型）的子项：
![](https://developer.roblox.com/assets/blte839d97cf6fe3fa4/Weapon-Model-Descendants-Crossbow.png)



  * **LeftString** (`Beam`) （可选） — 弦的左半部外观。
  * **RightString** (`Beam`) （可选） — 弦的右半部外观。
  * **Arrow** (`BasePart`) （可选） — 弓拉满时出现的箭矢。注意只是外观 （实际发射的箭矢应是一个 **ShotEffect**，详情请见投射/命中效果和声音）。
  * **String1** (`Attachment`) （可选） — 弦的中心。
  * **StringLoose** (`Attachment`) （可选） — 弓在静止状态时，**String1** 所处的位置。
  * **StringTight** (`Attachment`) （可选） — 弓拉满时，**String1** 所处的位置。
  * **Arms** (`Part`) （可选） — 仅用作弓臂设置动画的内部指示器的部件，可能包含以下一级子项： 
    * **LeftString0** (`Attachment`) （可选） — 弦左侧附着在弓上的位置。
    * **RightString0** (`Attachment`) （可选） — 弦右侧附着在弓上的位置。
    * **LeftLoose** (`Attachment`) （可选） — 弓在静止状态时，**LeftString0** 所在的位置。
    * **RightLoose** (`Attachment`) （可选） — 弓在静止状态时， **RightString0** 所在的位置。
    * **LeftTight** (`Attachment`) （可选） — 弓拉满时，**LeftString0** 所在的位置。
    * **RightTight** (`Attachment`) （可选） — 弓拉满时，**RightString0** 所在的位置。
    * **[SpecialMesh]** (`SpecialMesh`) （可选） — 拉弓时弓实际弯曲的一部分。 注意您必须设定以下四个 `Vector3Value` 来为其设置动画。
    * **LooseOffset** (`Vector3Value`) （可选） — 弓在静止状态时，`SpecialMesh` 的偏移。
    * **TightOffset** (`Vector3Value`) （可选） — 弓拉满时，`SpecialMesh` 的偏移。
    * **LooseScale** (`Vector3Value`) （可选） — 弓在静止状态时， `SpecialMesh` 的缩放。
    * **TightScale** (`Vector3Value`) （可选） — 弓拉满时，`SpecialMesh` 的缩放。

## 武器系统 GUI

核心武器系统接口，可用于更新基于 GUI 的部分，诸如枪的范围、受到攻击和命中敌人的提示等。

在 WeaponsSystem/Assets 中，武器系统 GUI 的结构如下所示：

WeaponsSystem (`Folder`)

Assets (`Folder`)

Animations (`Folder`)

Effects (`Folder`)

WeaponsSystemGui (`ScreenGui`) 游戏开始后，作为 `PlayerGui` 的子项。

ScalingElements (`Folder`) 自动随屏幕尺寸缩放的元素。

DirectionalIndicators (`Folder`) 储存所有 方向指示器 的地方。

Crosshair (`Frame`) 当有武器被装备时，其四个子 `ImageLabel|ImageLabels` 会出现。注意边框的大小会随武器的范围而变化，但这四个子项的尺寸不会改变。 

[UIAspectRatioConstraint] (`UIAspectRatioConstraint`)

Bottom (`ImageLabel`)

Left (`ImageLabel`)

Right (`ImageLabel`)

Top (`ImageLabel`)

HitMarker (`Frame`)

[UIAspectRatioConstraint] (`UIAspectRatioConstraint`)

HitMarkerImage (`ImageLabel`) 当您命中其它玩家时显现，之后渐隐。

LargeTouchscreen (`Frame`) 在大型触摸屏上显示的按钮。

AimButton (`ImageButton`)

FireButton (`ImageButton`)

Scope (`Frame`)

ScopeImage (`ImageLabel`) 在使用 HasScope 设为 **true** （参见 修改武器）的武器调整视野时显示。

[UIAspectRatioConstraint] (`UIAspectRatioConstraint`)

BottomBlack (`Frame`)

LeftBlack (`Frame`)

RightBlack (`Frame`)

TopBlack (`Frame`)

SmallTouchscreen (`Frame`) 在小型触摸屏上显示的按钮。

AimButton (`ImageButton`)

FireButton (`ImageButton`)

### 创建方向指示器

方向指示器用于显示玩家十字准线周围物体的方向。例如，如果有人向您开枪，一个红色的半圆会显示在您的十字准线周围，标记射击来源的方向。其他的例子还有指示脚步方向、间接射击，甚至是箱子等环境物体的指示器。

要添加新的指示器，只需以如下结构将其加入 WeaponsSystemGui/ScalingElements/DirectionalIndicators：

WeaponsSystemGui (`ScreenGui`)

ScalingElements (`Folder`)

DirectionalIndicators (`Folder`)

[Indicator] (`Frame`)

[UIAspectRatioConstraint] (`UIAspectRatioConstraint`) (required)

[ImageLabel] (`ImageLabel`) （必须） — 方向指示器的图像。可能需要在 Studio 中调整图像的旋转，除非您上传的图像是朝下的，并且周围几乎没有空白。

[UIAspectRatioConstraint] (`UIAspectRatioConstraint`) (required)

[Configuration] (`Configuration`)

DistanceLevelFromCenter (`NumberValue`) （可选） — 到屏幕中心的距离等级（每一距离等级代表大约 0.03 的屏幕缩放）；默认为 **6**。

FadeTime (`NumberValue`) （可选） — 指示器激活后的渐隐时间及 **TimeBeforeFade** 时间；默认为 **1**。

Name (`StringValue`) （可选） — 您想要引用的方向指示器的名称；默认为最高级指示器的名称`Frame`.

TimeBeforeFade (`NumberValue`) （可选） — 指示器渐隐之前显示的时间；默认为 **1**。

TransparencyBeforeFade (`NumberValue`) （可选） — 指示器渐隐之前的透明度；默认为 **0**。

WidthLevel (`NumberValue`) （可选） — 到屏幕中心的宽度等级（每一宽度等级代表大约 0.03 的屏幕缩放）；默认等于 **DistanceLevelFromCenter** 的值。

创建后，您可以使用 WeaponsSystem/Libraries/WeaponsGui 中的以下命令激活指示器。`indicatorName` 表示要激活的指示器的名称， `worldPos` 表示指示器的世界位置。

```    
    
    self.DirectionalIndicatorGuiManager:ActivateDirectionalIndicator(indicatorName, worldPos)


```
  * 如果指示器在完全淡出之前再次被激活，则一个该类型的新的指示器将被实例化，允许您同时激活多个任意类型的指示器。
  * 您还可以在 WeaponsGui 以外激活指示，只需将上述代码中的 `self` 替换为您代码中的 WeaponsGui 实例。不过我们推荐您在 WeaponsGui 中激活，然后用 `RemoteEvent` 或 `BindableEvent` 触发。您可以参见 DamageIndicator 是如何在 WeaponsGui 中激活的。

### 显示伤害通知

伤害通知用于在玩家受到伤害时在他们的头顶上显示小数字。这些只会为造成伤害的玩家显示，观战的玩家则无法看到。

伤害通知在 WeaponsSystem/Libraries/DamageBillboardHandler 中处理，可以像下述一样从任意 客户端 代码激活，其中 `damage` 表示伤害数值，`adornmentPart` 为公告的装饰部件，如受害者的头部。

```    
    
    DamageBillboardHandler:ShowDamageBillboard(damage, adornmentPart)


```
## 越肩镜头

越肩镜头是从玩家的右肩上方观看的第三人称镜头。要自定义肩越肩镜头，请修改 WeaponsSystem/Libraries/ShoulderCamera 的 `ShoulderCamera.new()` 函数中 `\-- 配置参数（常量）`注释下的变量。您可以修改诸如视野、距玩家的偏移量、冲刺或瞄准时的行走速度等内容。



***__Roblox官方链接__:[认可武器](https://developer.roblox.com/zh-cn/articles/weapons-kit)