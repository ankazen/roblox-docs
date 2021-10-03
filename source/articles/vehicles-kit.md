# 载具工具包 
Time:<em>20  分钟</em>

![](https://developer.roblox.com/assets/blt57fb33293bc6967e/Endorsed-Vehicles-Banner.jpg)

为了帮开发者创建乐趣十足的驾驶、竞速以及飞行体验，在任何游戏中都会提供几个**认可 载具**供开发者使用，所有的载具都完全基于约束且使用真实的物理规则来模拟驾驶体验。

在开发者的游戏中使用认可载具的方法是：

  1. 选择下列其中之一：

![](https://developer.roblox.com/assets/blta3452699c82eda13/Endorsed-Vehicle-Sports-Car.jpg)[ VEHICLE_NAME](CATALOG_URL_SPORTS_CAR)

![](https://developer.roblox.com/assets/blt05fd5c2401db688c/Endorsed-Vehicle-Sedan.jpg)[ VEHICLE_NAME](CATALOG_URL_SEDAN)

![](https://developer.roblox.com/assets/blt8d658bbcc623d3e4/Endorsed-Vehicle-High-End-Sports-Car.jpg)[ VEHICLE_NAME](CATALOG_URL_HIGH_END_SPORTS_CAR)

![](https://developer.roblox.com/assets/blt6454a961dde43855/Endorsed-Vehicle-SUV.jpg)[ VEHICLE_NAME](CATALOG_URL_SUV)

![](https://developer.roblox.com/assets/bltdcadea1946008537/Endorsed-Vehicle-Light-Utility.jpg)[ VEHICLE_NAME](CATALOG_URL_LIGHT_UTILITY)

![](https://developer.roblox.com/assets/blt396c82a542974813/Endorsed-Vehicle-Police-Car.jpg)[ VEHICLE_NAME](CATALOG_URL_POLICE_CAR)

![](https://developer.roblox.com/assets/bltbcefb6fc0b347ac0/Endorsed-Vehicle-Pickup-Truck.jpg)[ VEHICLE_NAME](CATALOG_URL_PICKUP_TRUCK)

![](https://developer.roblox.com/assets/bltca1fb2eb9e1b7d24/Endorsed-Vehicle-Dune-Buggy.jpg)[ VEHICLE_NAME](CATALOG_URL_DUNE_BUGGY)

![](https://developer.roblox.com/assets/blt413844ce9442d052/Endorsed-Vehicle-Van.jpg)[ VEHICLE_NAME](CATALOG_URL_VAN)

![](https://developer.roblox.com/assets/bltdd09578ccf1b987b/Endorsed-Vehicle-Motorcycle.jpg)[ VEHICLE_NAME](CATALOG_URL_MOTORCYCLE)

![](https://developer.roblox.com/assets/blt3946160512b6056b/Endorsed-Vehicle-Scooter.jpg)[ VEHICLE_NAME](CATALOG_URL_SCOOTER)

![](https://developer.roblox.com/assets/blt0e0094c1a812b258/Endorsed-Vehicle-Bicycle.jpg)[ VEHICLE_NAME](CATALOG_URL_BICYCLE)

![](https://developer.roblox.com/assets/blt3fdd188003a5519f/Endorsed-Vehicle-Helicopter.jpg)[ VEHICLE_NAME](CATALOG_URL_HELICOPTER)

![](https://developer.roblox.com/assets/blt5dc4f130267fe635/Endorsed-Vehicle-Plane.jpg)[ VEHICLE_NAME](CATALOG_URL_PLANE)

![](https://developer.roblox.com/assets/blt41383e8d87bdc307/Endorsed-Vehicle-Semi-Truck.jpg)[ VEHICLE_NAME](CATALOG_URL_SEMI_TRUCK)

![](https://developer.roblox.com/assets/blte034a1594e17950f/Endorsed-Vehicle-Front-End-Loader.jpg)[ VEHICLE_NAME](CATALOG_URL_FRONT_END_LOADER)

  2. 在载具的物品页面，点击绿色的 **Get**（获取）按钮来确认交易。
  3. 在 Roblox Studio 中打开工具箱（**View**（视图） → **Toolbox**（工具箱））。
  4. 选择开发者工具箱中的 **Inventory**（物品栏）部分。
![](https://developer.roblox.com/assets/blt7d482aecd878107e/Toolbox-Select-Inventory.png)



  5. 找到并点击载具，将其添加到场景中。

## 载具结构

每一个认可载具的结构如下所示，但请注意载具的模型可能不会包括所有列出对象。

[Vehicle] (`Model`)

Animations (`Folder`) — 用来存储那些坐在载具中使用的动画资源。

Configuration (`Folder`) — 存储着载具的配置项，注意每辆载具并不一定包括所有这些属性。

**_地面载具和直升机_**

BrakingTorque (`NumberValue`) — 当使用制动器或者在前进和倒退间切换时所施加的扭矩系数，这个数值越高，减速效果就越快。

DrivingTorque (`NumberValue`) — 在加速时施加的扭矩系数；在所有的 `CylindricalConstraint|CylindricalConstraint`上面设置 `CylindricalConstraint/MotorMaxTorque|MotorMaxTorque` 属性。数值越高，加速度越大。

MaxSpeed (`NumberValue`) — 载具前进时的最高速度。

MaxSteer (`NumberValue`) — 限制`PrismaticConstraint` 由一侧到另一侧的转向距离。值越低说明急转弯能力越差。

ReverseSpeed (`NumberValue`) — 载具倒退行进时的最高速度。

StrutSpringDampingFront (`NumberValue`) — 前支柱 `SpringConstraint|SpringConstraint` 的阻尼值。

StrutSpringDampingRear (`NumberValue`) — 后支柱 `SpringConstraint|SpringConstraint` 的阻尼值。

StrutSpringStiffnessFront (`NumberValue`) — 前支柱 `SpringConstraint|SpringConstraint` 的刚度值。

StrutSpringStiffnessRear (`NumberValue`) — 后支柱 `SpringConstraint|SpringConstraint` 的刚度值。

TakeOffAccessories (`BoolValue`) — 如果值为 **true**，玩家的 **RightFoot**、**RightLowerLeg**、**LeftFoot** 以及 **LeftLowerLeg** 就会在进入载具后变成全透明状态，其他那些与 **BodyBackAttachment**、 **WaistBackAttachment** 以及 **HatAttachment** 相关的饰品也会变成全透明。

TorsionSpringDamping (`NumberValue`) — 所有的 4 个扭力杆 `SpringConstraint|SpringConstraint` 的阻尼值。

TorsionSpringStiffness (`NumberValue`) — 所有 4 个扭力杆 `SpringConstraint|SpringConstraint` 的刚度值。

WheelFriction (`NumberValue`) — 被包含时覆盖车轮摩擦的默认值。

**_飞机_**

AngleOfAttack (`NumberValue`) — 外力的倍数因子，该外力用于帮助飞机升空且受到航向矢量、速度矢量、以及飞机速度的平方影响，然后会与此因子相乘。

BaseThrottle (`NumberValue`) — 施加于飞机来自引擎的外力。

Drag (`NumberValue`) — 拖拽的系数。力与飞机速度的平方成比例。

Lift (`NumberValue`) — 抬升的系数，力与飞机前进速度的平方成比例。

PitchSpeed (`NumberValue`) — 基准俯仰速度的倍数因子。基准速度由速度矢量与飞机前进矢量的相似度来决定。

RollSpeed (`NumberValue`) — 基准翻滚速度的倍数因子，它和 PitchSpeed 不同，不受矢量相似度的影响。

TakeOffAccessories (`BoolValue`) — 如果值为 **true**，玩家的**RightFoot**、 **RightLowerLeg**、 **LeftFoot** 和 **LeftLowerLeg** 将会在进入飞机之后变成全透明状态，就连那些与 **BodyBackAttachment**、 **WaistBackAttachment** 和 **HatAttachment** 相关的饰品也会一并变成全透明。

Torque (`NumberValue`) — 拖拽力的旋转倍数因子，用来设置俯仰、偏航或者翻滚的强度。值越低说明飞机越不容易因为惯性而转身，而值越高则说明更容易因为惯性而转身。如果这个值因为飞机的重量而过低，那么转身的速度可能会受到影响。

YawSpeed (`NumberValue`) — 基准偏航速度的倍数因子。和 PitchSpeed 类似，它的基准速度由速度矢量和飞机前进矢量的相似度来决定。

Constraints (`Folder`) — 含有可以驱动载具底架的物理约束。

Effects (`Folder`) — 用来存储 `Sound|Sound`、`ParticleEmitter|ParticleEmitter`、`Trail|Trail` 以及其他效果。

Remotes (`Folder`) — 存储用于处理座位的远程事件和函数。

Scripts (`Folder`)

Vehicle (`Script`) — 处理下列内容： 

  * 确保在加入游戏时玩家可以得到 SeatLocatorScreenGui 和 SeatLocator 脚本的副本（位于玩家的 `PlayerGui` 中）。
  * 执行记载于上述 TakeOffAccessories 中的过程。
  * 当玩家进入载具时，为玩家显示用于驾驶控制的 `ScreenGui`（VehicleGui）。
  * 使用 VehicleSeating 模块脚本来登记驾驶座位和乘客座位。

Driver (`LocalScript`) — 当玩家进入驾驶员座位时就会将其传递给玩家，它用于解释执行载具动作（包括驾驶、进入载具、离开载具）所需的输入。此脚本还会对镜头进行配置，并从 Chassis 脚本中调用函数来根据输入更新每一帧的约束。

Passenger (`LocalScript`) — 当玩家进入乘客座位时就会将其传递给玩家，它只描述用于上车和下车的输入，同时为乘客配置镜头。

SeatLocator (`LocalScript`) — 与其他脚本一起用在座位和提示系统中。

Chassis (`ModuleScript`) — 唯一的一个直接与 Constraints 文件夹中的约束对象进行交互的脚本。对约束值的初始化基于在 Configuration 文件夹中设置的配置值和当前的重力设置。

Effects (`ModuleScript`) — 管理存储在 Effects 文件夹中的载具效果。

InputImageLibrary (`ModuleScript`) — 和其子项一起处理屏幕上的 GUI 图像，用于接收各种手柄输入。

Keymap (`ModuleScript`) — 用来定义各个动作对应的键位或者按钮配置。动作中的每个条目都是一个独立的字典，需要一个 `enum/KeyCode|KeyCode` 来接收按下的键或者手柄按钮，还有一个轴用于模拟输入。注意在这里定义的动作必须在 Driver 或者 Passenger 脚本中实现。

LocalVehicleGui (`ModuleScript`) — 包含 VehicleGui 的 `ScreenGui`，用于显示屏幕上的载具控制信息。

LocalVehicleSeating (`LocalScript`) — 与其他脚本一起用于座位和提示系统中。

VehicleSeating (`ModuleScript`) — 与其他脚本一起用于 座位和提示系统中。

Body (`Model`) — 包含所有的非必须网格和装饰部件（这些网格和装饰部件组成了载具的可视化外形），可以对它们进行移除或者自定义，但注意下面的密度分布。

Chassis (`Model`) — 此载具功能部件用于处理驾驶相关事宜，它含有与物理约束相连接的所有底架部件，座位部件和权重来平衡载具的前端和后端。底架经过调整，可以适用于默认的 `Workspace/Gravity|Gravity` 值（35） 、同时也适用于 “Action” 重力设置值（75），但如果游戏使用极端重力设置，要想让底架正常工作可能就需要额外再对它进行调整。

##### 密度分布

Most of a vehicle’s mass is isolated in the “weight” parts and other parts of its **Chassis** model. This keeps the center of mass low and reduces the chances of the vehicle tipping or flipping. In contrast, the parts within the **Body** model are kept as light as possible so they have minimal impact on driving behavior.

  


## 座位和提示系统

每辆载具只能有一个驾驶员座位，但可以有无数个乘客座位（具体数量由开发者决定）。

  * 驾驶员座位必须是名为 **VehicleSeat** 的 `VehicleSeat` 对象，它应该是载具 **Chassis** 模型的直接子项并被准确放置在开发者想让驾驶员所坐的位置。**记住驾驶员座位只能有一个**。

  * 乘客座位必须是 `Seat` 对象，每一个乘客座位都应该是拥有唯一名称的 **Chassis** 模型子项。在 Scripts/Chassis `ModuleScript` 中按照下列方式将每个乘客座位添加到 `Chassis.passengerSeats` 数组中，其中 `[SeatName]` 就是 `Seat` 对象的名称：
    
    
    Chassis.passengerSeats = {
    	Chassis.root:FindFirstChild("[SeatName]"),
    	-- 额外的乘客座位，如果存在的话
    }


在内部，座位和提示系统由三个高亮脚本处理：

Scripts (`Folder`)

Vehicle (`Script`)

Driver (`LocalScript`)

Passenger (`LocalScript`)

SeatLocator (`LocalScript`) 

  * 每隔给定时间间隔（0.1 秒）就去寻找距离玩家最近的座位（该时间间隔可以更改，只需要修改脚本顶部的 `SEAT_POLL_INTERVAL` 常量即可）。
  * 通知 LocalVehicleSeating 脚本去显示提示信息，这样每次当一个新座位成为距离玩家最近的座位时就会显示坐上座位的提示。

Chassis (`ModuleScript`)

Effects (`ModuleScript`)

InputImageLibrary (`ModuleScript`)

Keymap (`ModuleScript`)

LocalVehicleGui (`ModuleScript`)

LocalVehicleSeating (`LocalScript`) 

  * 存有 `ShowPrompt()` 函数，该函数的作用是当玩家离身边最近的座位足够近时，函数就会显示进入驾驶员座位或者乘客座位的图标、如果载具被翻转则函数就会显示翻转图标。开发者可以在此脚本的顶端修改 `MIN_FLIP_ANGLE` 常量来更改载具需要被翻多少度才会被定义为翻转过来。
  * 监听玩家的输入并作出恰当的响应，根据最后的输入类型（键盘、游戏手柄、触摸设备）来更改在提示中该显示哪个图标来进入或者翻转载具，如果玩家通过正确输入激活当前显示的提示，此文件将会告诉服务器如何处理，并在玩家进入载具时为玩家播放相应的动画效果。

VehicleSeating (`ModuleScript`) 

  * 当玩家进入或者离开载具时，处理将玩家放入座位或者让玩家脱离座位。
  * 让门迅速打开和关闭。
  * 登记 FlipSeat 远程事件的 `RemoteEvent/OnServerEvent|OnServerEvent` 回调函数，该回调函数通知底架在玩家触发它时将车翻转。

## 载具控制

个人电脑 移动设备 主机

**地面载具**

动作 键 / 控制

加速 / 前进
W 或者 ↑

制动 / 倒行
S 或者 ↓

左转
A 或者 ←

右转
D 或者 →

紧急制动 / 漂移
空格键

进入 / 离开 / 翻转
E

**直升机**

动作 键 / 控制

驾驶操纵
移动鼠标（镜头控制）

加速 / 前进
W 或者 ↑

减速 / 倒退
S 或者 ↓

向左平移
A 或者 ←

向右平移
D 或者 →

上升
Q 或者 Shift

下降
Z 或者 Ctrl

进入 / 离开 / 翻转
E

**飞机**

动作 键 / 控制

驾驶操纵
移动鼠标（镜头控制）

加速 / 前进
W 或者 ↑

减速 / 停止
S 或者 ↓

向左翻滚
A 或者 ←

向右翻滚
D 或者 →

进入 / 离开 / 翻转
E

**地面载具**

动作 按钮 / 控制

加速 / 前进
跳跃按钮 （视觉变动）

制动 / 倒退
**加速** 按钮左侧的更小的按钮

向左转/向右转
移动摇杆

紧急制动 / 漂移
在最大转弯时出现

进入 / 翻转
载具上方的按钮提示

离开
**加速**按钮上方的更小按钮

**直升飞机**

动作 按钮 / 控制

驾驶操纵
触摸屏（镜头控制）

加速 / 前进
向前推摇杆

减速 / 后退
向后推摇杆

向左平移/向右平移
向左推摇杆/向右推摇杆

上升
跳跃按钮（视觉改变）

下降
**上升**按钮左侧的更小按钮

进入 / 翻转
直升机上方的按钮提示

离开
**上升**按钮上方的更小的按钮

**飞机**

动作 按钮 / 控制

驾驶操纵
移动摇杆

加速 / 前进
跳跃按钮（视觉改变）

减速 / 停止
**加速**按钮左侧的更小的按钮

进入 / 翻转
飞机上方的按钮提示

离开
**加速**按钮上方的更小按钮

**地面载具**

动作 按钮 / 控制

加速 / 前进
RT

制动 / 倒行
LT

向左转/向右转
将左摇杆向左推/向右推

电子制动 / 漂移

X

进入 / 离开 / 翻转

Y

**直升机**

动作 按钮 / 控制

驾驶操纵
右模拟杆（镜头控制）

加速 / 前进
将左摇杆往前推

减速 / 后退
将左摇杆往后推

向左平移/向右平移
将左摇杆向左推/向右推

上升
RT

下降
LT

进入 / 离开 / 翻转

Y

**飞机**

动作 按钮 / 控制

驾驶操纵
右摇杆（镜头控制）

加速 / 前进
RT

减速 / 停止
LT

向左翻滚/向右翻滚
将左摇杆向左推/向右推

进入 / 离开 / 翻转

Y

## 相关参考文章

[ ](/articles/weapons-kit)

### [认可武器](/articles/weapons-kit)

[ ](/articles/npc-kit)

### [NPC 套组](/articles/npc-kit)



***__Roblox官方链接__:[载具工具包](https://developer.roblox.com/zh-cn/articles/vehicles-kit)