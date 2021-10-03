# 自定义游戏控制 
Time:<em>5  分钟</em>

Roblox 提供数种自定义游戏控制的选项，包括电脑和移动设备的内置控制方案，以及为几乎任何控制系统编写自定义脚本的功能。

## 内置控制

Roblox 自带一些常见的控制方案，您只需点击几下就可以变更游戏的控制。

  1. 在 **Explorer（管理器）**窗口中，选择 **StarterPlayer** 对象。
![](https://developer.roblox.com/assets/blt34c9e03e4869f001/Select-StarterPlayer.png)



  2. 在 **Properties（属性）**窗口中，向下滚动并找到 **Mobile（移动端）**和 **Controls（控制）**部分。利用这些选项，您可以轻松地将您的游戏的控制设为下方的默认方案。
![](https://developer.roblox.com/assets/blt5ef8fea84b90f580/Properties-Mobile-Controls.png)



### 电脑端控制

台式电脑/笔记本电脑的控制可通过更改 **Controls（控制）** → **DevComputerMovementMode** 来修改。

选项 描述

**ClickToMove**
玩家只能通过在游戏世界中**右键点击**目标地点来移动。

**KeyboardMouse**
传统 Roblox 控制使用 W A S D 或方向键移动，以及空格键跳跃。

**Scriptable**
禁用所有默认控制，并允许您编写自己的控制方案脚本。

**UserChoice**
允许玩家从游戏内的**设置**菜单选择喜欢的控制方案。

### 移动端控制

Roblox 游戏在移动设备（手机/平板电脑）上的控制可通过更改 **Controls（控制）** → **DevTouchMovementMode** 的值来更改。

选项 描述 Preview

**ClickToMove**
玩家只能通过在游戏世界中点击目标地点来移动。屏幕右下角有一个跳跃键。
![](https://developer.roblox.com/assets/blt71e59e8cfa6755c9/Mobile-Controls-ClickToMove.jpg)

**DPad**
此选项已从 Roblox 移动端应用中移除，不应在正式版游戏中使用。左下角



***__Roblox官方链接__:[自定义游戏控制](https://developer.roblox.com/zh-cn/articles/customizing-game-controls)