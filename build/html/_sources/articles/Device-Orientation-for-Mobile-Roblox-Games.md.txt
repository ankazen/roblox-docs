# 设备方向 
Time:<em>5  分钟</em>

在手机和平板电脑上，设备的方向可能会对游戏玩法产生深远影响。例如，**横向**模式最好用两个大拇指操作，而**纵向**模式则可以用一个手指进行游戏。

默认情况下，Roblox 游戏以横向模式运行，当玩家的设备旋转时，允许游戏在横向“左”和横向“右”之间切换。但是，如果需要，游戏可以锁定到特定的方向。

## 方向模式

共有五种不同的方向模式，包括两种**传感器**模式和三种**锁定**模式。

传感器模式

**横向传感器**
Roblox 的默认设置将**始终**以横向模式（无纵向模式）显示游戏，并且设备将检测其物理方向以确保游戏视图始终朝上。

**传感器**
设备将检测其物理方向，以确保游戏视图始终朝上，并根据需要在横向和纵向模式之间切换。

锁定模式

**横向左**
在带有物理主页按钮的设备上，它将位于显示屏的**左侧**。在带有虚拟主页/导航栏的设备上，其触摸区域将位于显示屏的底部。

**横向右**
在带有物理主页按钮的设备上，它将位于显示屏的**右侧**。在带有虚拟主页/导航栏的设备上，其触摸区域将位于显示屏的底部。

**纵向**
在带有物理主页按钮的设备上，它将位于显示屏的**下方**。在带有虚拟主页/导航栏的设备上，其触摸区域将位于显示屏的底部。

Roblox 不包含“纵向倒置”模式，因为许多设备本身不支持这种方向。 

## 方向属性

有三种方法处理设备方向的方法：

### 开始方向

`StarterGui/ScreenOrientation` 设置场景的默认方向。可接受的值包括：

  * `enum/ScreenOrientation|Enum.ScreenOrientation.LandscapeSensor`
  * `enum/ScreenOrientation|Enum.ScreenOrientation.Sensor`
  * `enum/ScreenOrientation|Enum.ScreenOrientation.LandscapeLeft`
  * `enum/ScreenOrientation|Enum.ScreenOrientation.LandscapeRight`
  * `enum/ScreenOrientation|Enum.ScreenOrientation.Portrait`

由于此属性影响所有加入游戏的新玩家，你只需在 Studio 中的 **StarterGui** → **ScreenOrientation** 中设置其值即可。

### 游戏中的方向

`PlayerGui/ScreenOrientation` 显式更改玩家的游戏方向。当此属性设置为 `LocalScript` 中的 `enum/ScreenOrientation|ScreenOrientation` 枚举值之一时，游戏将立即调整自身方向以匹配此设置。当游戏需要提供特定的体验时，这非常有用，比如将视图锁定为小型游戏的纵向视图。

```    
    
    local Players = game:GetService("Players")
    local playerGUI = Players.LocalPlayer:WaitForChild("PlayerGui")
    
    wait(2)
    
    playerGUI.ScreenOrientation = Enum.ScreenOrientation.Portrait


```
### 当前方向

`PlayerGui/CurrentScreenOrientation` 获取**当前**设备方向。可能的值包括：

  * `enum/ScreenOrientation|Enum.ScreenOrientation.LandscapeLeft`
  * `enum/ScreenOrientation|Enum.ScreenOrientation.LandscapeRight`
  * `enum/ScreenOrientation|Enum.ScreenOrientation.Portrait`

```    
    
    local Players = game:GetService("Players")
    local playerGUI = Players.LocalPlayer:WaitForChild("PlayerGui")
    
    print(playerGUI.CurrentScreenOrientation)


```


***__Roblox官方链接__:[设备方向](https://developer.roblox.com/zh-cn/articles/Device-Orientation-for-Mobile-Roblox-Games)