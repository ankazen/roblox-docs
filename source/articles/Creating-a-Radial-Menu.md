# 创建摇杆快速菜单 
Time:<em>15  分钟</em>

摇杆快速菜单（Radial Menu）采用了模拟纵杆控制器，且易于使用，所以成为了主机游戏中经常出现的一种菜单形式。在摇杆快速菜单中，可将选项都置于一个圆环内。用户推动模拟杆时即可选择所推方向的选项。

本教程内容涵盖操作摇杆快速菜单的方法。虽然鼠标/键盘或手机游戏也可使用相同的方法，但这里我们会重点讲解游戏手柄。

## 设置菜单

可以手动或通过代码创建菜单。本教程采用代码，所以易于在各类游戏中应用：

构建一个摇杆快速菜单 ```    
    
    -- 决定打开和关闭状态下菜单框架的位置和大小
    local menuOpenPosition = UDim2.new(0.25, 0, 0.25, 0)
    local menuOpenSize = UDim2.new(0.5, 0, 0.5, 0)
    local menuClosedPosition = UDim2.new(.5, 0, .5, 0)
    local menuClosedSize = UDim2.new(0.005, 0, 0.005, 0)
    
    -- 决定菜单选项的元素
    local itemTemplate = Instance.new("TextButton")
    itemTemplate.Size = UDim2.new(0.3, 0, 0.2, 0)
    itemTemplate.AutoButtonColor = false
    itemTemplate.TextScaled = true
    
    -- 为菜单创建屏幕和框架
    local menuScreen = Instance.new("ScreenGui", player:WaitForChild("PlayerGui"))
    menuScreen.Name = "MenuScreen"
    local menuFrame = Instance.new("Frame", menuScreen)
    menuFrame.Size = menuClosedSize
    menuFrame.Position = menuClosedPosition
    menuFrame.Visible = false
    menuFrame.BackgroundTransparency = 1
    menuFrame.BorderSizePixel = 0
    menuFrame.Name = "MenuFrame"


```
摇杆快速菜单通常具有两种状态：打开和关闭。此代码首先会针对菜单的主框架定义位置和大小。有了当前值，打开状态的菜单将在屏幕上居中显示，宽和高占屏幕的一半。你可以调整 `menuOpenPosition` 和 `menuOpenSize`，用以调整菜单所占屏幕的比例以及在何处居中显示。

接下来，脚本会为菜单项创建一个模板。在本例中，使用 `TextButton` 是因为非常简便。你应当将其更改为使用与游戏和界面相符的更复杂元素。请记住，代码将通过大小变化来动态呈现菜单的打开。因此 `TextButton/TextScaled` 可以确保文本能够随着按钮而动态改变大小。

`AutoButtonColor` 被禁用，因为本教程着重于使用游戏手柄。如果将此代码改为使用鼠标，你应当启用此属性。

最后，代码会创建 `ScreenGui` 和 `Frame`。框架的 `GuiObject/Size` 和 `GuiObject/Position` 将分别设置为 `menuClosedSize` 和 `menuClosedPosition`，因为菜单最初应当为隐藏状态。

## 创建按钮

设置完菜单屏幕和框架，然后脚本就会自动创建圆圈中放置的按钮。你可使用几个常量来配置要显示在圆圈中的按钮数量及其方向。

创建摇杆快速菜单物品 ```    
    
    local RADIUS = .5
    local NUM_OPTIONS = 6
    local ANGLE_OFFSET = 90
    local menuItems = {}
    local function newMenuItem(name, angle, range)
    	local newItem = {}
    	local label = itemTemplate:Clone()
    	label.Text = name
    	label.Name = name
    	local angleRadians = math.rad(ANGLE_OFFSET + angle)
    	label.Position = UDim2.new(.5 + RADIUS * math.cos(angleRadians) - label.Size.X.Scale / 2, 0,
    							 .5 - RADIUS * math.sin(angleRadians) - label.Size.Y.Scale / 2, 0)
    	label.Parent = menuFrame
    	newItem.Label = label
    	newItem.Vector = Vector2.new(math.cos(angleRadians), math.sin(angleRadians))
    	newItem.Range = range
    	table.insert(menuItems, newItem)
    end


```
`newMenuItem` 函数用于创建新的菜单项，并将其添加到一表格中，随后在决定选择哪个项目时会用到表格和其中内容。该函数需要三个参数：`name` 表示选项的名称(也用于在 GUI 中标记它)，`angle` 设置选项在圆环转盘上的中心位置，`range` 设置输入弧的宽度。

![RadialMenu_Image01.png](https://developer.roblox.com/assets/blteede9255d5fdfdb5/RadialMenu_Image01.png)



该函数首先会创建一个先前创建好的 `itemTemplate` 的克隆副本。它还根据 `angle` 设置了按钮的位置。 该函数还存储了一个由输入的 `angle` 构成的 2D 向量。它将随后用于与用户输入进行比较，以确定哪个项目被选中。
    
    
    for i = 1, NUM_OPTIONS do
    	local angle = (360 / NUM_OPTIONS) * (i - 1)
    	local name = "Option" .. i
    	newMenuItem(name, angle, 360 / NUM_OPTIONS)
    end
    

声明 `newMenuItem` 函数之后，代码会执行一个循环来创建菜单项。常量 `NUM_OPTIONS` 决定了要创建多少个菜单选项。每个项目的角度是通过将 360（圆中的度数）除以 `NUM_OPTIONS`，然后乘以当前选项来确定。另外，范围同样也是由 360 除以 `NUM_OPTIONS` 来确定。这些值都会被传递到 `newMenuItem` 中，用以创建按钮。

## 打开菜单

在此教程中，菜单可通过左操纵杆在打开和关闭之间切换。`ContextActionService` 可用于将此按钮绑定到能打开和关闭菜单的自定义函数。
    
    
    -- 菜单和背包都使用左纵杆。禁用背包 UI 以防止冲突
    game.StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Backpack, false)
    
    local function toggleMenu(actionName, inputState)
    	if inputState == Enum.UserInputState.Begin then
    		openMenu()
    	elseif inputState == Enum.UserInputState.End then
    		closeMenu()
    	end
    end
    
    ContextActionService:BindAction("ToggleMenu", toggleMenu, false, Enum.KeyCode.ButtonL1)
    

默认的 Roblox 控制脚本会将操纵杆与道具包中项之间的开关绑定。要将此输入重新绑定到摇杆快速菜单，则必须使用 `StarterGui/SetCoreGuiEnabled` 将背包 UI 禁用。如果针对摇杆快速菜单使用其他输入而非操纵杆，则应当注意 Roblox 的默认设置以避免发生冲突。

`toggleMenu` 函数使用 `ContextActionService/BindAction` 绑定到左操纵杆。`toggleMenu` 会查看 `inputState` 以了解操纵杆处于何种状态。如果是 Begin 状态，那么用户只需开始按操纵杆并打开菜单。否则，如果是 End 状态，则需要关闭菜单。
    
    
    local function openMenu()
    	-- 存储 GuiNavigationEnabled 和 AutoSelectGuiEnabled 然后将二者设置为 false
    	wasGuiNavigationEnabled = GuiService.GuiNavigationEnabled		
    	wasAutoSelectGuiEnabled = GuiService.AutoSelectGuiEnabled
    	GuiService.GuiNavigationEnabled = false
    	GuiService.AutoSelectGuiEnabled = false
    	
    	-- 绑定 onThumbstickMoved 函数
    	ContextActionService:BindAction("RadialMenu", onThumbstickMoved, false, Enum.KeyCode.Thumbstick1)		
    	-- 确定框架可见并播放打开动画
    	menuFrame.Visible = true
    	menuFrame:TweenSizeAndPosition(menuOpenSize, menuOpenPosition, Enum.EasingDirection.Out, Enum.EasingStyle.Quart, .5, true)
    	menuOpen = true	
    end
    

`openMenu` 函数需要执行几点事项。首先，需要禁用 `GuiService/GuiNavigationEnabled` 和 `GuiService/AutoSelectGuiEnabled`，并存储该值，这样能够便于稍后执行恢复。这些设置适用于[其他菜单类型](http://wiki.roblox.com/index.php?title=Creating_a_Grid_Menu)，却不适合于摇杆快速菜单。

你可能会注意到，代码只是除以传入矢量的大小值（操纵杆的位置），而不是除以项矢量的大小值。这是因为项矢量保证为单位矢量，是通过 `Vector2.new(math.cos(angle), math.sin(angle))` 计算得出的。单位矢量大小为 1，所以可以从除数中忽略不计。

然后将矢量之间的角度与项范围值的一半做比较。如果小于此值，则表明操纵杆矢量位于针对该项定义的弧的某个位置。如果是这种情形，那么 `getButtonFromVector` 会返回项按钮。

如果 `getButtonFromVector` 返回一个按钮，`onThumbstickMoved` 会将 `GuiService/SelectedObject` 设置到该按钮。这样会高亮显示按钮，用户就知道已经选择了此按钮。

在 `onThumbstickMoved` 的末尾，如果操纵杆无法推过盲区，则会将 SelectedObject 设置为空，以便清除选项。

## 关闭菜单

菜单关闭后，如果存在已选项，代码需要基于该选项来调用一个函数。
    
    
    -- 选择物品时将调用的函数。您应把自己的自定义代码放在此处
    -- 来实现您自己的菜单
    local function onMenuSelect(option)
    	print(option, "selected")
    end
    
    local function closeMenu()
    	-- 恢复 GuiNavigationEnabled 和 AutoSelectGuiEnabled
    	GuiService.GuiNavigationEnabled	= wasGuiNavigationEnabled
    	GuiService.AutoSelectGuiEnabled = wasAutoSelectGuiEnabled	
    
    	-- 解除绑定 onThumbstickMoved 函数		
    	ContextActionService:UnbindAction("RadialMenu")
    	
    	if GuiService.SelectedObject then
    		-- 如果在菜单关闭时选择了一个选项，则认为该选项是用户想要的
    		onMenuSelect(GuiService.SelectedObject)
    	end
    	
    	-- 清除选择对象并播放关闭动画
    	GuiService.SelectedObject = nil
    	menuFrame:TweenSizeAndPosition(menuClosedSize, menuClosedPosition, Enum.EasingDirection.Out, Enum.EasingStyle.Quart, .4, true,
    		function()
    			-- 动画结束时的回调函数。如果用户没有重新打开菜单，则隐藏它
    			if not menuOpen then
    				menuFrame.Visible = false
    			end
    		end)
    	menuOpen = false
    end
    

鉴于游戏的剩余部分会依赖于这些设置，所以 `closeMenu` 函数首先会恢复 GuiNavigationEnabled 和 AutoSelectGuiEnabled。它还会解绑 `onThumbstickMoved`，便于操纵杆用于其他用途。然后，如果存在 SelectedObject，函数就会调用 `onMenuSelect`，作为参数传递给 SelectedObject。

`onMenuSelect` 表示你想要添加任意自定义代码的位置。根据传入的按钮，你可以在选定按钮的情况下，为需要生成的任何动作编写代码。

调用 `onMenuSelect` 后，`closeMenu` 会清除当前选项，并播放动画来隐藏菜单。

## 完成代码

下面是所有实施上述摇杆快速菜单的代码。代码应当包含在 `LocalScript` 内，且位于 `StarterPlayerScripts` 或 `StarterGui` 中。

创建摇杆快速菜单（完整代码） ```    
    
    local THUMBSTICK_DEADZONE = .4
    local RADIUS = .5
    local NUM_OPTIONS = 6
    local ANGLE_OFFSET = 90
     
    -- 服务
    local ContextActionService = game:GetService("ContextActionService")
    local GuiService = game:GetService("GuiService")
     
    -- 菜单和背包使用的都是左操纵杆。禁用背包 UI 以避免冲突
    game.StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Backpack, false)
     
    local player = game.Players.LocalPlayer
    local menuItems = {}
     
    -- 决定打开和关闭状态下菜单框架的位置和大小
    local menuOpenPosition = UDim2.new(0.25, 0, 0.25, 0)
    local menuOpenSize = UDim2.new(0.5, 0, 0.5, 0)
    local menuClosedPosition = UDim2.new(0.5, 0, 0.5, 0)
    local menuClosedSize = UDim2.new(0.005, 0, 0.005, 0)
     
    -- 决定菜单选项的元素
    local itemTemplate = Instance.new("TextButton")
    itemTemplate.Size = UDim2.new(0.3, 0, 0.2, 0)
    itemTemplate.AutoButtonColor = false
    itemTemplate.TextScaled = true
     
    -- 为菜单创建屏幕和框架
    local menuScreen = Instance.new("ScreenGui", player:WaitForChild("PlayerGui"))
    menuScreen.Name = "MenuScreen"
    local menuFrame = Instance.new("Frame", menuScreen)
    menuFrame.Size = menuClosedSize
    menuFrame.Position = menuClosedPosition
    menuFrame.Visible = false
    menuFrame.BackgroundTransparency = 1
    menuFrame.BorderSizePixel = 0
    menuFrame.Name = "MenuFrame"
     
    -- AutoSelectGuiEnabled 和 GuiNavigationEnabled 的存储
    local wasAutoSelectGuiEnabled = GuiService.AutoSelectGuiEnabled
    local wasGuiNavigationEnabled = GuiService.GuiNavigationEnabled
     
    local function newMenuItem(name, angle, range)
    	local newItem = {}
    	local button = itemTemplate:Clone()
    	button.Text = name
    	button.Name = name
    	local angleRadians = math.rad(ANGLE_OFFSET + angle)
    	button.Position = UDim2.new(.5 + RADIUS * math.cos(angleRadians) - button.Size.X.Scale / 2, 0,
    							 .5 - RADIUS * math.sin(angleRadians) - button.Size.Y.Scale / 2, 0)
    	button.Parent = menuFrame
    	newItem.Label = button
    	newItem.Vector = Vector2.new(math.cos(angleRadians), math.sin(angleRadians))
    	newItem.Range = range
    	table.insert(menuItems, newItem)
    end
     
    for i = 1, NUM_OPTIONS do
    	local angle = (360 / NUM_OPTIONS) * (i - 1)
    	local name = "Option" .. i
    	newMenuItem(name, angle, 360 / NUM_OPTIONS)
    end
     
    -- 通过菜单项目表，找到每个项目的向量和传递的向量之间的
    -- 角度。如果角度小于项目范围的一半，则该项目
    -- 被选中。
    local function getButtonFromVector(vector)
    	for i = 1, #menuItems do
    		local item = menuItems[i]
    		local dotProduct = vector.X * item.Vector.X + vector.Y * item.Vector.Y
    		local angle = math.acos(dotProduct / vector.magnitude)
    		if angle <= math.rad(item.Range) / 2 then
    			return item.Button
    		end
    	end
    	return nil
    end
     
    -- 绑定至左侧操纵杆的动作
    local function onThumbstickMoved(actionName, inputState, inputObject)
    	-- 确定操纵杆移动已经超过死区
    	if inputObject.Position.magnitude >= THUMBSTICK_DEADZONE then
    		-- 基于操纵杆位置计算角度
    		local selectedButton = getButtonFromVector(inputObject.Position)
    		GuiService.SelectedObject = selectedButton
    	else
    		-- 操纵杆移动在死区范围内，清除选择
    		GuiService.SelectedObject = nil
    	end
    end
     
    -- 物品被选择时要调用的函数。您应当在这里编写自定的代码
    -- 以实现您预期的菜单
    local function onMenuSelect(option)
    	print(option, "selected")
    end
     
    local function openMenu()
    	-- 存储 GuiNavigationEnabled 和 AutoSelectGuiEnabled 然后将二者均设置为 false
    	wasGuiNavigationEnabled = GuiService.GuiNavigationEnabled		
    	wasAutoSelectGuiEnabled = GuiService . AutoSelectGuiEnabled
    	GuiService.GuiNavigationEnabled	= false
    	GuiService.AutoSelectGuiEnabled = false
     
    	-- 绑定 onThumbstickMoved 函数
    	ContextActionService:BindAction("RadialMenu", onThumbstickMoved, false, Enum.KeyCode.Thumbstick1)		
     
    	-- 确保框架可见并播放打开动画
    	menuFrame.Visible = true
    	menuFrame:TweenSizeAndPosition(menuOpenSize, menuOpenPosition, Enum.EasingDirection.Out, Enum.EasingStyle.Quart, .5, true)
    	menuOpen = true	
    end
     
    local function closeMenu()
    	-- 恢复 GuiNavigationEnabled 和 AutoSelectGuiEnabled
    	GuiService.GuiNavigationEnabled	= wasGuiNavigationEnabled
    	GuiService . AutoSelectGuiEnabled = wasAutoSelectGuiEnabled	
     
    	-- 解绑 onThumbstickMoved 函数		
    	ContextActionService:UnbindAction("RadialMenu")
     
    	if GuiService.SelectedObject then
    		-- 如果菜单关闭时已经选择了一个选项，则认为该选项为用户所想要的
    		onMenuSelect(GuiService.SelectedObject)
    	end
     
    	-- 清楚选中的对象并播放关闭动画
    	GuiService.SelectedObject = nil
    	menuFrame:TweenSizeAndPosition(menuClosedSize, menuClosedPosition, Enum.EasingDirection.Out, Enum.EasingStyle.Quart, .4, true,
    		function()
    			-- 动画结束时的回调函数。如果用户未再打开菜单则隐藏它
    			if not menuOpen then
    				menuFrame.Visible =  false 
    			end 
    		end ) 
    	menuOpen =  false 
    end
     
    local function toggleMenu(actionName, inputState)
    	if inputState == Enum.UserInputState.Begin then
    		openMenu()
    	elseif inputState == Enum.UserInputState.End then
    		closeMenu()
    	end
    end
     
    ContextActionService:BindAction("ToggleMenu", toggleMenu, false, Enum.KeyCode.ButtonL1)


```


***__Roblox官方链接__:[创建摇杆快速菜单](https://developer.roblox.com/zh-cn/articles/Creating-a-Radial-Menu)