# 创建移动端按钮 
Time:<em>10  分钟</em>

在 Roblox 上设计最佳的跨平台体验时，`ContextActionService` 是一项便捷的服务，可让你将功能绑定到传统的 PC 输入并同时创建仅在移动设备上可见的屏显按钮。同时，此服务还允许快速设置输入与功能的关联，以及移动终端操作按钮的显示状况。

## 添加移动按钮

在 `LocalScript` 中声明 `ContextActionService`之后，可以使用 `ContextActionService/BindAction|BindAction()` 方法将特定输入与函数关联。此方法采用以下参数：

参数 类型 描述

`actionName`
字符串
由 `ContextActionService` 中的其他函数用来操作绑定的“键”。

`functionToBind`
函数
触发指定的输入时要调用的函数。此函数将接收三个参数： 

  * 等于操作名称的字符串。
  * 定义调用函数时输入状态的 `enum/UserInputState|UserInputState`。
  * 导致函数调用的 `InputObject`。

`createTouchButton`
布尔值
在移动设备上运行游戏时，是否要创建屏显按钮。

`inputTypes`
元组
你要绑定到函数的输入，例如从 `enum/KeyCode|KeyCode` 获取的枚举值等。

```    
    
    local ContextActionService = game:GetService("ContextActionService")
    
    local function interactNPC(actionName, inputState, inputObject)
    	if inputState == Enum.UserInputState.Begin then
    		print(actionName, inputObject)
    	end
    end
    
    -- 将动作绑定至函数
    ContextActionService:BindAction("InteractNPC", interactNPC, true, Enum.KeyCode.T, Enum.KeyCode.ButtonR1)


```
##### 保留的绑定键 »

为 `ContextActionService`/`UserInputService` 选择 `enum/KeyCode` 值或检测 `Mouse` 事件时，请注意有些绑定是 **Roblox 保留的绑定**，通常不应分配给游戏的自定义控件绑定。

角色移动

关键代码和事件 操作

**W** / **向上箭头键**
前进

**S** / **向下箭头键**
后退

**A** / **向左箭头键**
向左

**D** / **向右箭头键**
向右

**空格键**
跳跃

镜头

关键代码和事件 操作

`鼠标 / Button2Down（鼠标 2 键）`
转动镜头

`鼠标/WheelForward（向前滚轮）` / `Mouse/WheelBackward（向后滚轮）`
放大/缩小

**I**
放大

**O**
缩小

**LeftShift（左 Shift）**/**RightShift（右 Shift）**
切换鼠标锁定（启用 `StarterPlayer/EnableMouseLockOption|EnableMouseLockOption` 时的玩家设置）

饰品

关键代码和事件 操作

**0** / **1** / **2** / **3** / **4** / **5** / **6** / **7** / **8** / **9**
装备工具或取消装备工具

`鼠标/Button1Down（鼠标 1 键）`
使用工具

**Backspace**
放下工具

菜单和 UI

关键代码和事件 操作

**Escape**
主菜单

**Tab**
玩家列表

**斜线**
聊天

**反引号**
背包

**F11**
全屏模式

其他

关键代码和事件 操作

**PrintScreen**（Windows）  
**LeftControl（左 Ctrl）**/**RightControl（右 Ctrl）** + **LeftShift（左 Shift）**/**RightShift（右 Shift）** + **3** （Mac）
截图

**F12**
录制视频（仅限 Windows）

**F10**
提高图形级别

**LeftShift（左 Shift）**/**RightShift（右 Shift）** + **F10**
降低图形级别

**F9**
开发者控制台

**LeftControl（左 Ctrl）**/**RightControl（右 Ctrl）** + **LeftShift（左 Shift）**/**RightShift（右 Shift）** + **F7**（Windows）  
**LeftControl（左 Ctrl）**/**RightControl（右 Ctrl）** + **LeftAlt（左 Alt）**/**RightAlt（右 Alt）** + **F7** （Mac）
性能统计

**LeftControl（左 Ctrl）**/**RightControl（右 Ctrl）** + **F6**
显示微型性能分析器

**LeftControl（左 Ctrl）**/**RightControl（右 Ctrl）** + **P**
暂停微型性能分析器（如果显示）

  


## 移除移动按钮

如果要从屏幕中移除移动按钮，请使用传递给 `ContextActionService/BindAction|BindAction()` 的 `actionName` 字符串的唯一参数调用 `ContextActionService/UnbindAction|UnbindAction()`。

```    
    
    -- 通过名称解绑动作
    ContextActionService:UnbindAction("InteractNPC")


```
## 自定义按钮

`ContextActionService` 提供了几个函数来自定义由 `ContextActionService/BindAction|BindAction()` 生成的按钮。

### 按钮文本

要更改移动按钮的文本标签，请使用 `actionName` 字符串和标题调用 `ContextActionService/SetTitle|SetTitle()`：

```    
    
    -- 为 "Talk" 设置按钮标签
    ContextActionService:SetTitle("InteractNPC", "Talk")


```
### 按钮图像

移动按钮可以像其他 GUI 按钮一样通过 `ContextActionService/SetImage|SetImage()` 方法使用自定义图像：

```    
    
    -- 设置按键图像
    ContextActionService:SetImage("InteractNPC", "rbxassetid://0123456789")


```
### 按钮位置

若要定位移动按钮，请使用 `ContextActionService/SetPosition|SetPosition()` 并指定所需的 `datatype/UDim2`：

```    
    
    -- 设置按键位置
    ContextActionService:SetPosition("InteractNPC", UDim2.new(1, -80, 1, -150))


```
如果不设置按钮的位置，它将出现在屏幕右下方的移动端跳跃按钮附近。需要注意的是：按钮位置在移动设备上**非常**重要，详见`articles/cross platform development|跨平台开发`一文中概述的“拇指区”。

## 覆盖输入

由于移动设备上的屏幕空间非常有限，因此最好使用**上下文按钮**，这些按钮显示玩家在当前场景下可以执行的操作。例如，当玩家站在金币宝箱附近时，开发者或许想要在附近显示可用的 “Collect（拿取）”按钮：

![](https://developer.roblox.com/assets/blt25ec84c0f29d3831/Cross-Platform-Input-Detection-Mobile.png)



```    
    
    local ContextActionService = game:GetService("ContextActionService")
    
    -- 拿取宝物所用的函数
    local function collectTreasure(actionName, inputState, inputObject)
    	if inputState == Enum.UserInputState.Begin then
    		print("Collect treasure")
    	end
    end
    
    ContextActionService:BindAction("RightButton1", collectTreasure, true, Enum.KeyCode.T, Enum.KeyCode.ButtonR1)
    ContextActionService:SetPosition("RightButton1", UDim2.new(1, -80, 1, -150))
    -- 为蓝色的 "Collect" 按钮设置图像
    ContextActionService:SetImage("RightButton1", "rbxassetid://0123456789")


```
游戏中另外一种情形下，开发者可能希望在玩家站在 NPC 附近时将按钮更改为“对话”。不必在同一位置添加新按钮（并移除旧按钮），只需将其所进行的操作**重新绑定**至新函数并更改其图像即可：

```    
    
    ContextActionService:BindAction("RightButton1", talkToNPC, true, Enum.KeyCode.T, Enum.KeyCode.ButtonR1)
    -- 将图像设置到黄色的 "Talk" 按钮
    ContextActionService:SetImage("RightButton1", "rbxassetid://0011223344")


```


***__Roblox官方链接__:[创建移动端按钮](https://developer.roblox.com/zh-cn/articles/ContextActionService-Creating-Mobile-Buttons)