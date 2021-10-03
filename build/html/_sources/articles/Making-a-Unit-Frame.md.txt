# 单元框：制作生命槽 
Time:<em>5  分钟</em>

尽管在默认情况下 Roblox 提供了一个生命条，但如果它不太适合你的游戏的视觉风格，那么你可以自己制作一个生命条。 在本教程中，我们将介绍如何使用 UDim2 的 Scale 属性制作一个显示玩家姓名、虚拟角色和生命值的单位框架。

### 添加框架

让我们从单元框架的容器开始。在你的 **ScreenGui** 中，插入一个新的 **Frame** 并将其命名为 _UnitFrame_。若要将其从屏幕边缘移开一点，请将 position 设置为 {0, 10,},{0, 10}。将 size 设置为 {0.3, 0},{0.15, 0}。现在，我们在左上角有一个框，这是我们的单位框架将要出现的位置：

![UnitFrame_Frame.png](https://developer.roblox.com/assets/bltb83712f481dbb8df/UnitFrame_Frame.png)



以原始像素为单位设置 size 是很有诱惑力的，就像我们对屏幕边缘的边距所做的那样。但我们必须考虑我们游戏的玩家和他们使用的设备。考虑下面的示例。 

这是我们将在本教程中制作的单位框架，就像在普通笔记本电脑上看到的一样。 通过偏移将单位框架的大小设置为 410px x 115px：

![enter image description here](https://developer.roblox.com/assets/blt49c058efbdedb234/UnitFrameScaleiPhone6.png)



在你看到它在 iPhone6 上的外观之前，看起来尺寸相当不错：

![enter image description here](https://developer.roblox.com/assets/blt49c058efbdedb234/UnitFrameScaleiPhone6.png)



现在，单位框架占据了屏幕的大部分！几乎没有空间真正看到任何东西，更不用说玩家的大拇指会遮住下角。如果通过缩放将单位框架的大小设置为 .3 x.15（屏幕宽度的 30%，高度的 15%），则单位框架看起来与在笔记本电脑上完全相同，在 iPhone 上看起来更好：

![enter image description here](https://developer.roblox.com/assets/blt49c058efbdedb234/UnitFrameScaleiPhone6.png)



### 添加 LocalScript

在我们继续之前，让我们添加一个 LocalScript，这样我们就可以继续向框架中添加功能。在 _UnitFrame_ 中插入一个 **LocalScript**。在该脚本中，让我们为玩家和框架本身声明变量，这两个变量都将在稍后使用。
    
    
    local player = game.Players.LocalPlayer
    local unitFrame = script.Parent
    

### 玩家虚拟形象

现在，让我们在 UnitFrame 中插入一个 **ImageLabel** 并将其命名为 _Avatar_。该标签将用于玩家的虚拟形象。同样，因为我们希望我们的单位框架能够很好地缩放，所以我们将只使用 Size 的 Scale 组件。将 ImageLabel 的 Size 设置为 {0.25, 0},{0.9, 0}。在此处，重要的是要知道 Scale 属性根据父元素的大小设置尺寸。到目前为止，我们添加的所有 2D 元素的父元素都是 ScreenGui，因此设置 scale 将缩放这些元素相对于屏幕的比例。但是，在本例中，我们将 ImageLabel 的宽度设置为 .25，这意味着它将是我们插入的 Frame 宽度的 25%。

若要将 ImageLabel 移到框架的右侧，请将其位置设置为 {0.75, 0}, {0,0}。我们知道 ImageLabel 将是 Frame 宽度的 25%，因此将位置设置为 75% 会将其一直移到框架的右侧。

![UnitFrame_ImageLabel.png](https://developer.roblox.com/assets/blt8dcb025ca8acdc5d/UnitFrame_ImageLabel.png)



我们应该为 ImageLabel 使用什么图像呢？使用加入我们游戏的任何玩家的实际虚拟形象，将非常不错。由于我们无法提前知道玩家，因此我们将向脚本中添加代码来获取玩家的虚拟形象缩略图并将其放入 ImageLabel 中。
    
    
    local player = game.Players.LocalPlayer
    local unitFrame = script.Parent
    
    unitFrame:WaitForChild("Avatar").Image = "http://www.roblox.com/Thumbs/Avatar.ashx?x=100&y=100&username=" .. player.Name
    

注意我们如何使用 `WaitForChild` 访问 `Avatar`。当 Roblox 游戏启动时，StarterGui 的所有内容都将复制到玩家的 PlayerGui 中。这种复制不是立即发生，也不是同时发生。此 LocalScript 完全有可能在其他 GuiElement 复制之前复制并开始执行。 

这种问题的解决方案是 WaitForChild。该函数将暂停，直到子对象实际存在。请记住，你不必在每次访问 GUI 元素时都使用此函数，但是它对于在脚本首次运行时执行的代码非常有用。

### 玩家名称

若要显示玩家的名称，请在 _UnitFrame_ 中插入一个 **TextLabel**。将此标签命名为 _PlayerName_。可以将此标签保留在框架的左侧，因此 Position 可以保持在 {0, 0},{0, 0}。我们确实想拉伸标签，以使其充满框架中的其余空间，因此请将 Size 设置为 {0.75, 0},{0.9, 0}。另外，将标签的 **TextScaled** 属性设置为 _true_，以便文本也可以拉伸。

![UnitFrame_NameLabel.png](https://developer.roblox.com/assets/blt9d41cfde212ceb85/UnitFrame_NameLabel.png)



在我们的 LocalScript 中，我们添加一行代码来用玩家的名称填充 TextLabel。
    
    
    local player = game.Players.LocalPlayer
    local unitFrame = script.Parent
    
    unitFrame:WaitForChild("Avatar").Image = "http://www.roblox.com/Thumbs/Avatar.ashx?x=100&y=100&username=" .. player.Name
    unitFrame:WaitForChild("PlayerName").Text = player.Name
    

### 玩家生命值

我们需要做的最后一件事是为生命条和代码设置元素，以使其发生变化。在 _UnitFrame_ 中插入一个新的 **Frame** 并将其命名为 _HealthBarContainer_。将 Position 设置为 {0, 0},{0.9, 0} 并将 Size 设置为 {1, 0},{0.1, 0}。若要确保它超出 TextLabel 的边框，请将 HealthBarContainer 的 **ZIndex** 设置为 _2_。

在 _HealthBarContainer_ 中插入另一个新的 **Frame** 并将其命名为 _HealthBar_。将 size 更改为 {1, 0},{1, 0} 以便它完全填满 HealthBarContainer（注意将 Scale 设置为 1 表示父元素大小的 100%）。确保 Healthbar 的 **ZIndex** 也设置为 _2_。若要更改 HealthBar 的颜色，请单击 **BackgroundColor3** 并从选择器中选择一个颜色。

![UnitFrame_HealthBar.png](https://developer.roblox.com/assets/blt09744f39383d4d46/UnitFrame_HealthBar.png)



现在我们必须添加代码，以便在玩家的生命值发生变化时更改生命条的宽度。在我们的脚本中，为 HealthBar 添加一个变量。然后，然后，我们将一个函数绑定到玩家的 CharacterAdded 事件。每当玩家重生一个角色并将角色模型传递到绑定函数时，就会触发此事件，然后我们就可以获取该角色的人形生物。
    
    
    local player = game.Players.LocalPlayer
    local unitFrame = script.Parent
    
    unitFrame:WaitForChild("Avatar").Image = "http://www.roblox.com/Thumbs/Avatar.ashx?x=100&y=100&username=" .. player.Name
    unitFrame:WaitForChild("PlayerName").Text = player.Name
    
    local healthBar = unitFrame.HealthBarContainer.HealthBar
    
    player.CharacterAdded:connect(function(character)
    	local humanoid = character:WaitForChild(**Humanoid**)
    end)
    

现在，我们可以将一个函数绑定到该人形生物的 HealthChanged 事件。在此函数中，我们可以通过将当前生命值除以最大生命值来得出角色的生命值百分比。然后，我们可以使用该百分比作为生命条的大小，因为 Scale 组件按百分比工作。
    
    
    local player = game.Players.LocalPlayer
    local unitFrame = script.Parent
    
    unitFrame:WaitForChild("Avatar").Image = "http://www.roblox.com/Thumbs/Avatar.ashx?x=100&y=100&username=" .. player.Name
    unitFrame:WaitForChild("PlayerName").Text = player.Name
    
    local healthBar = unitFrame.HealthBarContainer.HealthBar
    
    player.CharacterAdded:connect(function(character)
    	local humanoid = character:WaitForChild(**Humanoid**)
    	humanoid.HealthChanged:connect(function(health)
    		local healthPercentage = health / character.Humanoid.MaxHealth
    		healthBar.Size = UDim2.new(healthPercentage, 0, 1, 0)
    	end)
    end)
    

最后，我们还可以禁用 Core Gui 中的默认生命条，因为我们不再需要它：
    
    
    local player = game.Players.LocalPlayer
    local unitFrame = script.Parent
    
    unitFrame:WaitForChild("Avatar").Image = "http://www.roblox.com/Thumbs/Avatar.ashx?x=100&y=100&username=" .. player.Name
    unitFrame:WaitForChild("PlayerName").Text = player.Name
    
    local healthBar = unitFrame.HealthBarContainer.HealthBar
    
    player.CharacterAdded:connect(function(character)
    	local humanoid = character:WaitForChild(**Humanoid**)
    	humanoid.HealthChanged:connect(function(health)
    		local healthPercentage = health / character.Humanoid.MaxHealth
    		healthBar.Size = UDim2.new(healthPercentage, 0, 1, 0)
    	end)
    end)
    
    game.StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Health, false)
    

现在，我们有了一个功能性的单位框架，我们可以进一步对其进行自定义，以适应我们的游戏风格！



***__Roblox官方链接__:[单元框：制作生命槽](https://developer.roblox.com/zh-cn/articles/Making-a-Unit-Frame)