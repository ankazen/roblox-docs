# Studio 控件中的拖放 
Time:<em>10  分钟</em>

使用插件中的拖放交互是一种改进插件中数据流的简易方式。在阅读之前请好好熟悉下 studio 控件，可以先参考一下 `articles/Building Studio Widgets` 这篇文章！

## 创建一个拖拽源

当用户在 UI 元素（比如控件中的 `TextButton` 或者 `ImageButton`）上按鼠标键时，就需要调用 `Plugin/StartDrag` 来开始一个拖拽动作。先用常规方式创建一个控件：下列代码示例会创建出一个包含按钮的简单窗口。
    
    
    -- 先创建控件
    local widgetInfo = DockWidgetPluginGuiInfo.new(Enum.InitialDockState.Float, true, true, 300, 200)
    local dragSourceWidget = plugin:CreateDockWidgetPluginGui("Drag Source", widgetInfo)
    dragSourceWidget.Title = "Drag Source"
    
    -- 创建一个将会初始化拖拽的 TextButton
    local dragButton = Instance.new("TextButton")
    dragButton.Size = UDim2.new(1, 0, 1, 0)
    dragButton.Text = "Drag me!"
    dragButton.Parent = dragSourceWidget
    

### 初始化拖拽

我们希望当用户用鼠标点击 TextButton 时，拖拽动作就会立刻开始。一般情况下按钮上会使用 `GuiButton/Activated|Activated` 事件，但我们选择使用 `GuiButton/MouseButton1Down|MouseButton1Down`，因为它会在鼠标键被按下的时候就立刻开始，而不是等鼠标键被松开后再开始。
    
    
    local function onButton1Down()
    	local dragInfo = {
    		Data = "Hello, world",      -- 数据正在被拖拽
    		MimeType = "text/plain",    -- 描述数据的 MIME 类型
    		Sender = "SomeDragSource",  -- 描述数据起源于何处
    		MouseIcon = "",             -- 提供给光标使用的图像
    		DragIcon = "",              -- 在拖拽时光标下面显示的图像
    		HotSpot = Vector2.new(0, 0) -- 在 DragIcon 的哪个位置居中光标
    	}
    	plugin:StartDrag(dragInfo)
    end
    
    dragButton.MouseButton1Down:Connect(onButton1Down)
    

在这个函数中必须决定被拖拽的数据详情：其类型由 `MimeType` 键来反映，拖拽内容应该在 `Data` 键中，发送者则由 `Sender`键描述。详情参考 `Plugin/StartDrag` 页面。

## 创建一个释放的目标

当用户在拖拽窗口过程中松开鼠标键时，`PluginGui/PluginDragDropped|PluginDragDropped` 事件就会启动，我们需要一个释放的目标，创建带有 `TextLabel` 的第二个控件来侦测拖拽动作后的释放：
    
    
    local dragTargetWidget = plugin:CreateDockWidgetPluginGui("Drop Target", widgetInfo)
    dragTargetWidget.Title = "Drop Target"
    
    -- 此 TextLabel 将会显示被释放的东西
    local textLabel = Instance.new("TextLabel")
    textLabel.Size = UDim2.new(1, 0, 1, 0)
    textLabel.Text = "Drop here..."
    textLabel.Parent = dragTargetWidget
    

### 处理释放的动作

然后将 `PluginGui/PluginDragDropped|PluginDragDropped` 事件与释放的目标的控件相连接：
    
    
    local function onDragDrop(dragData)
    	print("PluginDragDropped")
    	if dragData.MimeType == "text/plain" then
    		textLabel.Text = dragData.Data
    	else
    		textLabel.Text = dragData.MimeType
    	end
    end
    dragTargetWidget.PluginDragDropped:connect(onDragDrop)
    

当一个拖拽动作仍在进行中时，当用户将鼠标移过一个控件时，下面三个事件会启动：

— `PluginGui/PluginDragEntered|PluginDragEntered` – 当用户光标悬停于窗口上时  
— `PluginGui/PluginDragMoved|PluginDragMoved` – 当用户光标移动到窗口上时会不断地启动，非常适合显示“就放在这里吧！”的讯息。  
— `PluginGui/PluginDragLeft|PluginDragLeft` – 当用户的光标离开窗口后启动，非常适合隐藏“就放在这里吧！”的讯息。



***__Roblox官方链接__:[Studio 控件中的拖放](https://developer.roblox.com/zh-cn/articles/drag-and-drop-in-studio-widgets)