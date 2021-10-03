# 游戏手柄输入 
Time:<em>5  分钟</em>

Roblox 接受来自 USB 游戏手柄（例如 Xbox 和 Playstation 手柄）的输入。一个游戏可以支持每个客户端最多 8 个本地手柄。

## 检测游戏手柄

可以使用 `UserInputService/GamepadEnabled|UserInputService.GamepadEnabled` 属性来检测玩家设备当前是否有有效的游戏手柄。请注意，此属性仅显示是否连接了任何游戏手柄，而不显示插入多少游戏手柄或它们在哪个插槽中。

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    if UserInputService.GamepadEnabled then
    	print("玩家已启用手柄...")
    end


```
由于一次最多可以将八个游戏手柄连接到一个客户端，所以了解哪些是有效的游戏手柄很重要。一种方法是监听 `UserInputService/GamepadConnected|GamepadConnected` 和 `UserInputService/GamepadDisconnected|GamepadDisconnected` 事件，这些事件分别在设备启用或禁用时触发。两者都将向连接的函数传递一个 `Enum/UserInputType` 枚举值，指示是哪个游戏手柄导致了事件（在大多数情况下，它将是 `Enum.UserInputType.Gamepad1`，但如果开发者的游戏支持本地多人游戏，则应确认这一点）。

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    UserInputService.GamepadConnected:Connect(function(gamepad)
    	print("玩家已连接游戏手柄：" .. tostring(gamepad))
    end)
    
    UserInputService.GamepadDisconnected:Connect(function(gamepad)
    	print("玩家已断连游戏手柄：" .. tostring(gamepad))
    end)


```
开发者也可以使用 `UserInputService/GetGamepadConnected|UserInputService:GetGamepadConnected()` 函数主动查询特定控制器是否已连接。此函数以 `Enum/UserInputType` 枚举值作为参数，并且只接受 `Enum.UserInputType.Gamepad1` 至 `Enum.UserInputType.Gamepad8` 的值。

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    if UserInputService:GetGamepadConnected(Enum.UserInputType.Gamepad1) then
    	print("Gamepad1 已连接")
    elseif UserInputService:GetGamepadConnected(Enum.UserInputType.Gamepad2) then
    	print("Gamepad2 已连接")
    end


```
## 获取输入

有三种方法可以从游戏手柄获取输入：

  * 如果要将自定义游戏控件绑定到游戏手柄和其他输入源（如键盘或移动触摸控件），请使用 `ContextActionService`。
  * 直接使用 `UserInputService` 监听游戏手柄事件。
  * 使用 `UserInputService/GetGamepadState|UserInputService:GetGamepadState()` 函数查询游戏手柄输入的状态。

### ContextActionService

`ContextActionService` 对于将控件绑定到游戏手柄和其他输入源特别有用。例如，如果要将自定义的“打开法术书”操作绑定到游戏手柄上的右触发器（**R2**）**和**键盘上的 B 键，`ContextActionService` 可以在一个函数中处理这两种情况：

```    
    
    local ContextActionService = game:GetService("ContextActionService")
    
    local function openSpellBook(actionName, inputState, inputObject)
    	if inputState == Enum.UserInputState.Begin then
    		-- 打开法术书
    	end
    end
    
    ContextActionService:BindAction("OpenSpellBook", openSpellBook, false, Enum.KeyCode.ButtonR2, Enum.KeyCode.B)


```
绑定到 `ContextActionService` 的函数将在**所有**输入状态（`enum/UserInputState|Begin`、`enum/UserInputState|Change` 和 `enum/UserInputState|End`）上触发，因此强烈建议检查第 4 行的 `InputObject/UserInputState|UserInputState`，以确保所需操作仅在开发者希望的状态上发生。 

### UserInputService

使用 `UserInputService` 检测游戏手柄事件时，所有控件都将触发 `UserInputService/InputBegan|InputBegan` 和 `UserInputService/InputEnded|InputEnded` 事件。在处理函数中，`InputObject/UserInputType` 属性指出哪个游戏手柄触发了事件，`InputObject/KeyCode` 指出触发事件的特定按钮或摇杆。

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    UserInputService.InputBegan:Connect(function(input)
    	if input.UserInputType == Enum.UserInputType.Gamepad1 then
    		if input.KeyCode == Enum.KeyCode.ButtonA then
    			-- 按下了 A 按钮
    		end
    	end
    end)


```
大多数游戏手柄也支持模拟控制。要检测这些控制的输入，使用 `UserInputService/InputChanged|InputChanged` 事件并通过 `InputObject/Position` 检测输入轴的位置。摇杆的位置将始终位于 **X** 和 **Y** 轴上介于 -1 和 1 的值之间，而触发按钮将只在 **Z** 轴上拥有 0 和 1 之间的值（0 表示其起始位置，1 表示完全按下的情况）。

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    UserInputService.InputChanged:Connect(function(input, processed)
    	if input.UserInputType == Enum.UserInputType.Gamepad1 then
    		if input.KeyCode == Enum.KeyCode.Thumbstick1 then
    			print(input.Position.X, input.Position.Y)
    		end
    	end
    end)


```
### 游戏手柄输入状态

可以随时使用 `UserInputService/GetGamepadState|UserInputService:GetGamepadState()` 函数检测游戏手柄上所有按钮和摇杆的状态。如果需要在发生非手柄事件时检测游戏手柄输入，这将非常有用。例如，当玩家按下 RT 手柄按钮时，以下代码检测角色的左脚是否接触到某些东西：

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    local player = game.Players.LocalPlayer
    local character = player.Character
    if not character or not character.Parent then
    	character = player.CharacterAdded:Wait()
    end
    
    local leftFoot = character:WaitForChild("LeftFoot")
    leftFoot.Touched:Connect(function(hit)
    	local state = UserInputService:GetGamepadState(Enum.UserInputType.Gamepad1)
    	for _, input in pairs(state) do
    		if input.KeyCode == Enum.KeyCode.ButtonR2 and input.UserInputState == Enum.UserInputState.Begin then
    			print("按住 RT 按钮时时角色的左脚碰到了物体")
    		end
    	end
    end)


```
## 支持的输入

并不是所有的游戏手柄都有相同数量或类型的输入，所以检查连接的游戏手柄有哪些输入是很重要的。也可以使用 `UserInputService/GetSupportedGamepadKeyCodes|UserInputService:GetSupportedGamepadKeyCodes()` 函数执行此操作，该函数接受 `Enum/UserInputType` 枚举值作为参数，并返回一个表，其中包含指定手柄的所有可用输入的列表。

```    
    
    local UserInputService = game:GetService("UserInputService")
    
    local availableInputs = UserInputService:GetSupportedGamepadKeyCodes(Enum.UserInputType.Gamepad2)
    print("This controller supports the following controls:")
    for _, control in pairs(availableInputs) do
    	print(control)
    end


```
开发者也可以通过 `UserInputService/GamepadSupports|UserInputService:GamepadSupports()` 检查游戏手柄是否支持特定按钮。 

## 最佳做法

与任何用户输入方法一样，最好在不同的游戏和应用之间建立一定的一致性。这有助于玩家立即对开发者的控制方案感到熟悉和舒适。以下是在实装游戏手柄控件时的一些建议做法：

  * 如果实装了任何用户提示或 GUI 选择，则 **A** 按钮应表示“接受”。
  * 对于任何 GUI 或任何模式状态，**B**按钮应表示“取消”。
  * 屏幕提示哪些按钮可以做什么非常有帮助，特别是对于像物品栏系统、升级系统这样复杂的 GUI。
  * 角色移动应该关联左摇杆。
  * 镜头移动应该关联右摇杆。
  * 主要动作通常是通过右扳机（**R2**）或 **A** 按钮进行的。
  * 辅助动作通常是通过左扳机（**L2**）或 **R1** 和 **L1** 按钮进行的。如果开发者将辅助动作与正面按钮关联，那么 **X** 和 **Y** 是不错的选择。
  * 允许玩家重新映射按钮可以让开发者的游戏更容易操作。



***__Roblox官方链接__:[游戏手柄输入](https://developer.roblox.com/zh-cn/articles/Gamepad-Input)