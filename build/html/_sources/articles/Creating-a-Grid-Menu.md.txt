# 创建栅格菜单 
Time:<em>15  分钟</em>

在创建带有游戏手柄控件的菜单系统时必须特别小心。使用常规界面，用户可以轻松单击或点选要选择的位置。对于简单快捷的菜单，`Articles/Creating a Radial Menu|摇杆快速菜单`很适合游戏手柄，但是对于更复杂和传统的菜单，用户必须通过在元素之间移动选择器来导航菜单。`GuiService` 会自动尝试确定用户要使用游戏手柄选择的元素，但有时需要额外的配置才能使菜单正常工作。

本教程将使用 GuiService 和 `ContextActionService` 来实现一个简单的设备管理菜单系统。

## 概述

本教程中的代码创建了设备管理系统的框架：首先在屏幕上创建一个按钮，如果用户在选中该按钮的情况下按 A，则游戏会弹出一个模型菜单，其中显示了简单的角色模型和物品栅格。

![GamepadGrid_Image00.png](https://developer.roblox.com/assets/blt6878b1384d7603d3/GamepadGrid_Image00.png)



![GamepadGrid_Image04.png](https://developer.roblox.com/assets/blt6ddc57d871cb6bd9/GamepadGrid_Image04.png)



![GamepadGrid_Image03.png](https://developer.roblox.com/assets/bltdf5323e2df741820/GamepadGrid_Image03.png)



## 设置

该代码要做的第一件事是创建菜单。游戏中的菜单当然可以事先创建和存储，但在本例中，菜单元素是在脚本中独立创建的。

![GamepadGrid_Image01.png](https://developer.roblox.com/assets/bltc1e521564b56469a/GamepadGrid_Image01.png)



关于菜单最为重要的就是将在定义选择群组时使用的层次结构。角色栏位的所有按钮都是 `CharacterFrame` 的子级，所有栅格按钮都是 `ScrollingFrame` 的子级

![GamepadGrid_Image02.png](https://developer.roblox.com/assets/blt05cb0e09fb8e6ba4/GamepadGrid_Image02.png)



## 打开菜单

定义菜单布局后，代码将绑定输入以打开和关闭菜单。Gui 按钮（例如 `ImageButton` 和 `TextButton`）都可以接受游戏手柄输入。如果玩家在选中按钮的情况下按下 A 按钮，则会触发 `GuiButton/MouseButton1Click` 事件。

创建栅格菜单 代码示例 1 ```    
    
    -- 关闭装备菜单
    local function closeEquipmentMenu()
    	-- 播放关闭动画
    	menuFrame:TweenPosition(MENU_CLOSED_POSITION, Enum.EasingDirection.Out, Enum.EasingStyle.Quad, 0.25, false, function(status)
    		-- 当动画播放完毕时，取消关闭函数绑定，重设 Gui 选择		
    		ContextActionService:UnbindAction(CLOSE_EQUIPMENT_MENU_BINDING)
    		GuiService.SelectedObject = nil
    		GuiService.AutoSelectGuiEnabled = oldAutoSelectGuiEnabled
    	end)
    end
    
    -- 打开装备菜单
    local function openEquipmentMenu()
    	-- 存储先前的 AutoSelectEnabled 值，然后设置为 false
    	oldAutoSelectGuiEnabled = GuiService.AutoSelectGuiEnabled
    	GuiService.AutoSelectGuiEnabled = false
    	
    	-- 播放打开动画
    	menuFrame:TweenPosition(MENU_OPEN_POSITION, Enum.EasingDirection.Out, Enum.EasingStyle.Quad, 0.25, false, function(status)
    		-- 当动画播放完毕时，绑定 closeEquipmentMenu 至 B 按键
    		ContextActionService:BindAction(CLOSE_EQUIPMENT_MENU_BINDING, function(actionName, inputState, inputObject)
    			if inputState == Enum.UserInputState.Begin then
    				closeEquipmentMenu()
    			end
    		end, false, Enum.KeyCode.ButtonB)
    		-- 默认选择躯干
    		GuiService.SelectedObject = torsoFrame
    	end)
    end
    
    -- 输入绑定
    equipmentButton.MouseButton1Click:Connect(openEquipmentMenu)


```
该代码定义了两个函数：`openEquipmentMenu` 和 `closeEquipmentMenu`。`openEquipmentMenu` 绑定到屏幕左上角的 `equipmentButton`。调用该函数时，将禁用 `GuiService/AutoSelectGuiEnabled` 并存储该值以供以后使用。启用此属性时，按下选择按钮，游戏将自动选择一个元素。需要在打开菜单之前执行此操作，以便可以激活设备按钮，但是当玩家处于菜单中时，应将其禁用。

`GuiObject/TweenPosition` 用于设置菜单打开和关闭的动画。该函数的最后一个参数是动画完成后调用的自定义回调函数。完成打开动画时，使用此函数将 B 按钮绑定到 `closeEquipmentMenu` 并将所选内容移动到躯干按钮。在 `closeEquipmentMenu` 中，播放结束动画后，B 按钮将被解除绑定，所选内容将被清除，并且将恢复 AutoSelectGuiEnabled 的原始值。

## 导航角色栏位

Roblox 具有自动行为，可帮助用户通过游戏手柄导航 GUI 元素。当用户按下游戏手柄上的“Select（选择）”按钮时，游戏将围绕一个启用 `GuiObject/Selectable` 的可见 GUI 元素创建一个选择内容。当用户按下左操纵杆或 dpad 时，游戏将试图在被推的方向上找到另一个 GUI 元素并将选择内容移动到那里。如果此方向上没有元素，则选择内容将不会更改。

菜单右侧的栅格在此系统上运行良好（因为元素始终在彼此的基本方向上），但是角色框中的元素在默认系统上不能很好地运行。`GuiObject` 有几个属性可以用来指定要切换到哪个元素（例如，`GuiObject/NextSelectionDown`）。使用这些属性，可以按照如下所示设置每个角色栏位的方向：

![GamepadGrid_Image05.png](https://developer.roblox.com/assets/blt03a451e9d6d734f4/GamepadGrid_Image05.png)


    
    
    headFrame.NextSelectionDown = torsoFrame
    headFrame.NextSelectionLeft = rightArmFrame
    headFrame.NextSelectionRight = leftArmFrame
    
    torsoFrame.NextSelectionUp = headFrame
    torsoFrame.NextSelectionLeft = rightArmFrame
    torsoFrame.NextSelectionRight = leftArmFrame
    torsoFrame.NextSelectionDown = rightLegFrame
    
    rightArmFrame.NextSelectionUp = headFrame
    rightArmFrame.NextSelectionRight = torsoFrame
    rightArmFrame.NextSelectionDown = rightLegFrame
    
    leftArmFrame.NextSelectionUp = headFrame
    leftArmFrame.NextSelectionLeft = torsoFrame
    leftArmFrame.NextSelectionDown = leftLegFrame
    
    rightLegFrame.NextSelectionUp = torsoFrame
    rightLegFrame.NextSelectionRight = leftLegFrame
    rightLegFrame.NextSelectionLeft = rightArmFrame
    
    leftLegFrame.NextSelectionUp = torsoFrame
    leftLegFrame.NextSelectionRight = leftArmFrame
    leftLegFrame.NextSelectionLeft = rightLegFrame
    

请注意，以上代码中有几个未定义的边缘。例如，该代码未定义从左臂向右移动的行为。如果用户选择了左臂并按下右键，因为该行为没有用 `GuiObject/NextSelectionRight` 明确定义，因此游戏将试图在右侧找到一个可选择的 GUI 元素。这是我们不希望的行为，因为在菜单的该部分中时，用户应被限制在角色栏位中。尽管可以通过将值设置为 nil 来定义，但更简单的方法是使用选择群组。

在 GuiService 中，选择群组是可以在之间导航的一组 GUI 元素。有两种定义选择群组的方法：`GuiService/AddSelectionParent` 和 `GuiService/AddSelectionTuple`。AddSelectionParent 具有两个参数，所选内容的名称以及 GuiObject。在这种选择群组中，只能在之间导航在 GuiObject 中传递的子级。对于另一个函数 AddSelectionTuple，你只需传入要加入群组的所有 GuiObject。在这种情况下，由于所有角色栏位都是 `characterFrame` 的子级，因此可使用较简单的函数 AddSelectionParent。
    
    
    GuiService:AddSelectionParent("CharacterMenu", characterFrame)
    

现在，当用户通过 `openEquipmentMenu` 进入菜单时，他们只能在 `characterFrame` 的子级之间导航。

接下来，必须绑定角色栏位按钮才能将所选内容移动到物品栏栅格：

创建栅格菜单 代码示例 2 ```    
    
    -- 将选择从物品菜单移回到角色菜单
    local function exitInventoryMenu()
    	ContextActionService:UnbindAction(EXIT_INVENTORY_MENU_BINDING)
    	GuiService.SelectedObject = currentEquipmentSlot
    end
    
    -- 玩家 "点击了" 角色栏位。选择移动至物品菜单
    local function onCharacterSlotClicked()
    	-- 存储当前的角色栏位
    	currentEquipmentSlot = GuiService.SelectedObject
    	-- 将 exitInventoryMenu 绑定至 B 按键
    	ContextActionService:BindAction(EXIT_INVENTORY_MENU_BINDING, function(actionName, inputState, inputObject)
    		if inputState == Enum.UserInputState.Begin then
    			exitInventoryMenu()
    		end
    	end , false, Enum.KeyCode.ButtonB)
    	-- 默认为选择物品格中的第一格
    	GuiService.SelectedObject = firstCell
    end
    
    for _, child in pairs(characterFrame:GetChildren()) do
    	child.MouseButton1Click:Connect(onCharacterSlotClicked)
    end


```
同样，使用 MouseButton1Click 来检测用户何时在选择了一个角色栏位的情况下按下 A 按钮。触发此事件时，将调用 `onCharacterSlotClicked`。此函数首先存储选择供以后使用的角色栏位，然后绑定 B 按钮来调用 `exitInventoryMenu`，最后在物品栏菜单中选择第一个栅格单元。`exitInventoryMenu` 只是解除了对 `onCharacterSlotClicked` 设置的 B 绑定的绑定，并将选择内容移回到之前选择的物品栏栏位。

## 导航物品栏栅格

物品栏栅格比角色框导航简单得多，因为默认的游戏手柄选择代码在栅格中运行得非常好。唯一需要为物品栏栅格设置的是选择群组以及用户在选中一个单元格的情况下按 A 时的事件。
    
    
    GuiService:AddSelectionParent("InventoryMenu", inventoryScroll)
    
    -- 玩家“单击”了物品栏槽位。如果想要使用 currentEquipmentSlot 和
    -- SelectedObject 进行操作则需在此处放置相关代码
    local function onInventorySlotClicked()
    	print("角色栏位：", currentEquipmentSlot)
    	print("物品栏位：", GuiService.SelectedObject)
    	-- 在此处放置你的代码！
    	exitInventoryMenu()
    end
    
    for _, child in pairs(inventoryScroll:GetChildren()) do
    	child.MouseButton1Click:connect(onInventorySlotClicked)
    end
    

再次使用 AddSelectionParent 设置选择群组。尽管默认的游戏手柄选择代码将有助于在网格中移动选择，但此函数仍然需要确保选择不会移动到网格之外。

对于栅格中的每个单元格，`onInventorySlotClicked` 都绑定到 MouseButton1Click。你可以修改此函数以执行任何自定义代码，例如，装备用户选择的物品。在此函数的末尾调用 `exitInventoryMenu` 将选择内容移回角色框。

一旦绑定此函数，菜单系统的框架也就完成了。

## 项目源代码

下面是本文概述的菜单的完整源代码。要正常运作，必须将其插入到位于 `StarterPlayerScripts` 中的 `LocalScript` 中。

创建栅格菜单 ```    
    
    -- 常量
    local INVENTORY_CELL_WIDTH = 0.2
    local INVENTORY_CELL_X_MARGIN = 0.04
    local INVENTORY_CELL_HEIGHT = 0.1
    local INVENTORY_CELL_Y_MARGIN = 0.02
    
    local INVENTORY_COLUMNS = 3
    local INVENTORY_ROWS = 7
    
    local CHARACTERFRAME_Y_SCALE = 1/8
    local CHARACTERFRAME_X_SCALE = 1/8
    
    local MENU_OPEN_POSITION = UDim2.new(0.05, 0, 0.05, 0)
    local MENU_CLOSED_POSITION = UDim2.new(0.05, 0, -.9, -36)
    
    local CLOSE_EQUIPMENT_MENU_BINDING = "CloseEquipmentMenu"
    local EXIT_INVENTORY_MENU_BINDING = "ExitInventoryMenu"
    
    -- 服务
    local GuiService = game:GetService("GuiService")
    local ContextActionService = game:GetService("ContextActionService")
    
    -- 变量
    local player = game.Players.LocalPlayer
    local playerGui = player:WaitForChild("PlayerGui")
    
    local firstCell = nil
    local currentEquipmentSlot = nil
    
    local oldAutoSelectGuiEnabled = GuiService.AutoSelectGuiEnabled
    
    -- 创建菜单
    -- 主要 screenGui
    local screenGui = Instance.new("ScreenGui", playerGui)
    
    -- 屏幕上的装备按钮
    local equipmentButton = Instance.new("TextButton", screenGui)
    equipmentButton.Name = "EquipmentButton"
    equipmentButton.Text = "Equipment"
    equipmentButton.Size = UDim2.new(0, 300, 0, 75)
    equipmentButton.Font = Enum.Font.SourceSans
    equipmentButton.FontSize = Enum.FontSize.Size60
    
    -- 菜单框架
    local menuFrame = Instance.new("Frame", screenGui)
    menuFrame.Size = UDim2.new(0.9, 0, 0.9, 0)
    menuFrame.Position = MENU_CLOSED_POSITION
    menuFrame.BackgroundTransparency = 1
    
    -- 角色栏框架
    local characterFrame = Instance.new("Frame", menuFrame)
    characterFrame.Name = "CharacterFrame"
    characterFrame.Size = UDim2.new(0.5, 0, 1, 0)
    
    local headFrame = Instance.new("ImageButton", characterFrame)
    headFrame.Name = "Head"
    headFrame.Size = UDim2.new(CHARACTERFRAME_X_SCALE, 0, CHARACTERFRAME_Y_SCALE, 0)
    headFrame.Position = UDim2.new(0.5 - CHARACTERFRAME_X_SCALE/2, 0, CHARACTERFRAME_Y_SCALE, 0)
    
    local torsoFrame = Instance.new("ImageButton", characterFrame)
    torsoFrame.Name = "Torso"
    torsoFrame.Size = UDim2.new(2 * CHARACTERFRAME_X_SCALE, 0, 2 * CHARACTERFRAME_Y_SCALE, 0)
    torsoFrame.Position = UDim2.new(0.5 - CHARACTERFRAME_X_SCALE, 0, 2.5 * CHARACTERFRAME_Y_SCALE, 0)
    
    local leftArmFrame = Instance.new("ImageButton", characterFrame)
    leftArmFrame.Name = "LeftArm"
    leftArmFrame.Size = UDim2.new(CHARACTERFRAME_X_SCALE, 0, 2 * CHARACTERFRAME_Y_SCALE, 0)
    leftArmFrame.Position = UDim2.new(0.5 + 1.5 * CHARACTERFRAME_X_SCALE, 0, 2.5 * CHARACTERFRAME_Y_SCALE, 0)
    
    local rightArmFrame = Instance.new("ImageButton", characterFrame)
    rightArmFrame.Name = "RightArm"
    rightArmFrame.Size = UDim2.new(CHARACTERFRAME_X_SCALE, 0, 2 * CHARACTERFRAME_Y_SCALE, 0)
    rightArmFrame.Position = UDim2.new(0.5 - 2.5 * CHARACTERFRAME_X_SCALE, 0, 2.5 * CHARACTERFRAME_Y_SCALE, 0)
    
    local leftLegFrame = Instance.new("ImageButton", characterFrame)
    leftLegFrame.Name = "LeftLeg"
    leftLegFrame.Size = UDim2.new(CHARACTERFRAME_X_SCALE, 0, 2 * CHARACTERFRAME_Y_SCALE, 0)
    leftLegFrame.Position = UDim2.new(0.5 + .5 * CHARACTERFRAME_X_SCALE, 0, 5 * CHARACTERFRAME_Y_SCALE, 0)
    
    local rightLegFrame = Instance.new("ImageButton", characterFrame)
    rightLegFrame.Name = "RightLeg"
    rightLegFrame.Size = UDim2.new(CHARACTERFRAME_X_SCALE, 0, 2 * CHARACTERFRAME_Y_SCALE, 0)
    rightLegFrame.Position = UDim2.new(0.5 - 1.5 * CHARACTERFRAME_X_SCALE, 0, 5 * CHARACTERFRAME_Y_SCALE, 0)
    
    -- 覆盖选择边缘
    headFrame.NextSelectionDown = torsoFrame
    headFrame.NextSelectionLeft = rightArmFrame
    headFrame.NextSelectionRight = leftArmFrame
    
    torsoFrame.NextSelectionUp = headFrame
    torsoFrame.NextSelectionLeft = rightArmFrame
    torsoFrame.NextSelectionRight = leftArmFrame
    torsoFrame.NextSelectionDown = rightLegFrame
    
    rightArmFrame.NextSelectionUp = headFrame
    rightArmFrame.NextSelectionRight = torsoFrame
    rightArmFrame.NextSelectionDown = rightLegFrame
    
    leftArmFrame.NextSelectionUp = headFrame
    leftArmFrame.NextSelectionLeft = torsoFrame
    leftArmFrame.NextSelectionDown = leftLegFrame
    
    rightLegFrame.NextSelectionUp = torsoFrame
    rightLegFrame.NextSelectionRight = leftLegFrame
    rightLegFrame.NextSelectionLeft = rightArmFrame
    
    leftLegFrame.NextSelectionUp = torsoFrame
    leftLegFrame.NextSelectionRight = leftArmFrame
    leftLegFrame.NextSelectionLeft = rightLegFrame
    
    -- 物品栅格框架
    local inventoryFrame = Instance.new("Frame", menuFrame)
    inventoryFrame.Name = "InventoryFrame"
    inventoryFrame.Size = UDim2.new(0.5, 0, 1, 0)
    inventoryFrame.Position = UDim2.new(0.5, 0, 0, 0)
    
    local inventoryScroll = Instance.new("ScrollingFrame", inventoryFrame)
    inventoryScroll.Size = UDim2.new(0.9, 0, 0.9, 0)
    inventoryScroll.CanvasSize = UDim2.new(0.9, 0, 1.8, 0)
    inventoryScroll.Position = UDim2.new(0.05, 0, 0.05, 0)
    inventoryScroll.Selectable = false
    inventoryScroll.ScrollBarThickness = 0
    
    -- 创建物品格里的各小格
    for y = 0, INVENTORY_ROWS do
    	for x = 0, INVENTORY_COLUMNS do
    		local inventoryCell = Instance.new("ImageButton", inventoryScroll)
    		inventoryCell.Image = "rbxassetid://133293265"
    		inventoryCell.Name = "InventoryCell(" .. x .. "," .. y .. ")"
    		if not firstCell then firstCell = inventoryCell end
    		inventoryCell.Size = UDim2.new(INVENTORY_CELL_WIDTH, 0, INVENTORY_CELL_HEIGHT, 0)
    		inventoryCell.Position = UDim2.new(INVENTORY_CELL_X_MARGIN + INVENTORY_CELL_X_MARGIN * x + INVENTORY_CELL_WIDTH * x, 0,
    										 INVENTORY_CELL_Y_MARGIN + INVENTORY_CELL_Y_MARGIN * y + INVENTORY_CELL_HEIGHT * y, 0)
    		
    	end
    end
    
    -- 为菜单的两部分添加选择群组
    GuiService:AddSelectionParent("CharacterMenu", characterFrame)
    GuiService:AddSelectionParent("InventoryMenu", inventoryScroll)
    
    -- 关闭装备菜单
    local function closeEquipmentMenu()
    	-- 播放关闭动画
    	menuFrame:TweenPosition(MENU_CLOSED_POSITION, Enum.EasingDirection.Out, Enum.EasingStyle.Quad, 0.25, false, function(status)
    		-- 动画完成时，取消绑定关闭函数并重设 Gui 选择		
    		ContextActionService:UnbindAction(CLOSE_EQUIPMENT_MENU_BINDING)
    		GuiService.SelectedObject = nil
    		GuiService.AutoSelectGuiEnabled = oldAutoSelectGuiEnabled
    	end)
    end
    
    -- 打开装备菜单
    local function openEquipmentMenu()
    	-- 保存先前的 AutoSelectEnabled 值并设置为 false
    	oldAutoSelectGuiEnabled = GuiService.AutoSelectGuiEnabled
    	GuiService.AutoSelectGuiEnabled = false
    	
    	-- 播放打开动画
    	menuFrame:TweenPosition(MENU_OPEN_POSITION, Enum.EasingDirection.Out, Enum.EasingStyle.Quad, 0.25, false, function(status)
    		-- 动画播放完成时，绑定 closeEquipmentMenu 至 B 按键
    		ContextActionService:BindAction(CLOSE_EQUIPMENT_MENU_BINDING, function(actionName, inputState, inputObject)
    			if inputState == Enum.UserInputState.Begin then
    				closeEquipmentMenu()
    			end
    		end, false, Enum.KeyCode.ButtonB)
    		-- 默认选择躯干
    		GuiService.SelectedObject = torsoFrame
    	end)
    end
    
    -- 将选择从物品菜单移回到角色菜单
    local function exitInventoryMenu()
    	ContextActionService:UnbindAction(EXIT_INVENTORY_MENU_BINDING)
    	GuiService.SelectedObject = currentEquipmentSlot
    end
    
    -- 玩家 "点击了" 一个角色栏位。将选择移动到物品菜单
    local function onCharacterSlotClicked()
    	-- 储存当前的角色栏
    	currentEquipmentSlot = GuiService.SelectedObject
    	-- 绑定 exitInventoryMenu 至 B 按键
    	ContextActionService:BindAction(EXIT_INVENTORY_MENU_BINDING, function(actionName, inputState, inputObject)
    		if inputState == Enum.UserInputState.Begin then
    			exitInventoryMenu()
    		end
    	end , false, Enum.KeyCode.ButtonB)
    	-- 默认选择物品格中的第一格
    	GuiService.SelectedObject = firstCell
    end
    
    -- 玩家 "点击了" 一个物品栏位。您写在这里的代码将会通过
    -- currentEquipmentSlot 和 SelectedObject 来发挥作用
    local function onInventorySlotClicked()
    	print("Character slot:", currentEquipmentSlot)
    	print("Inventory cell:", GuiService.SelectedObject)
    	
    	-- 将您的代码写在这里！
    	
    	exitInventoryMenu()
    end
    
    -- 输入绑定
    equipmentButton.MouseButton1Click:Connect(openEquipmentMenu)
    
    for _, child in pairs(characterFrame:GetChildren()) do
    	child.MouseButton1Click:Connect(onCharacterSlotClicked)
    end
    
    for _, child in pairs(inventoryScroll:GetChildren()) do
    	child.MouseButton1Click:Connect(onInventorySlotClicked)
    end


```


***__Roblox官方链接__:[创建栅格菜单](https://developer.roblox.com/zh-cn/articles/Creating-a-Grid-Menu)