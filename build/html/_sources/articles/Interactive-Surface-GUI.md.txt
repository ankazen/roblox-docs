# 交互式表面 GUI 
Time:<em>15  分钟</em>

`Articles/Creating Surface GUI|表面 GUI`教程介绍了如何创建基本的表面 GUI。开发者可以籍此在 Roblox 游戏中展示标志、插图和其他对象。但现在我们将对其进行进一步学习，探讨如何制作能够作为游戏中按钮、键盘、面板等内容的_交互式_表面对象。

## 创建按钮列

与任何表面 GUI 一样，你需要一个基本的部件来连接它。

  1. 创建一个正好 2 个格宽和 2 个格深的块。

![](https://developer.roblox.com/assets/bltd4573db09a00d644/Create-ButtonColumn-1.png)



对于此演示，块是 2 个格宽和 2 个格深，这一点非常重要。如有必要 ，在 **Properties（属性）**窗口中，检查 **Part（部件）** → **Size（大小）**值。 

  2. 在管理器窗口中，将部件重命名为 _ButtonColumn_。
![](https://developer.roblox.com/assets/blt857e71864aec72e6/Rename-ButtonColumn.png)



## 创建表面 GUI

现在，为该列创建一个表面 GUI。这次，我们不是将其直接添加到 **ButtonColumn** 部件，而是将其添加到 **StarterGui** 对象（记住，当每个玩家加入游戏时，这会将 GUI 复制到他们的本地游戏会话中）。

  1. 在管理器窗口中，将鼠标悬停在 **StarterGui** 上，然后单击其圆形的 circle ⊕ 按钮。

  2. 从弹出菜单中选择 **SurfaceGui**。

![](https://developer.roblox.com/assets/blt0bd2675a19205554/Create-SurfaceGUI-A-2.png)



## 将 GUI 连接到该列

这个新的表面 GUI 空间是 **StarterGui** 对象的一部分，但它没有连接部件，它只是在空间中漂浮着。若要将此表面 GUI 连接到部件，你必须设置它的 **Adornee** 属性。

  1. 在管理器窗口中选择 **SurfaceGui** 对象。

  2. 在“Properties（属性）”窗口中，单击 **Adornee** 属性。这会将你在 Studio 中的光标更改为一个小的选择箭头。

![](https://developer.roblox.com/assets/blt2c20fe3985cd2143/Set-Adornee-1.png)



  3. 在 3D 游戏编辑器窗口中，单击按钮列部分，将其设置为 GUI 的装饰物。
![](https://developer.roblox.com/assets/blt2f755d99abded8aa/Set-Adornee-2.png)



## 添加图像按钮

现在，让我们向表面 GUI 中添加一个图像按钮。这些步骤与 `articles/Creating GUI Buttons` 中的步骤类似，因此如有必要，请查看该指南。

  1. 在管理器窗口中，找到要添加到 **StarterGui** 的 **SurfaceGui** 对象，然后插入一个 `ImageButton` 对象。
![](https://developer.roblox.com/assets/blt4e313d906cf97b91/Add-ImageButton-1.png)



  2. 选择该按钮并在“Properties（属性）”窗口中单击其 **Image** 属性。将下面的 `ControlButton.png` 图像上传到你的游戏中（右键单击并选择 **Save Image As…（将图像另存为…）**将其保存到你的计算机）。
![](https://developer.roblox.com/assets/blta5b1b36f74d831b0/ControlButton.png)



当图像上传完成后，你应该会在前角看到一个小按钮：

![](https://developer.roblox.com/assets/blt6939f7fb03a02d2c/Add-ImageButton-SurfaceGUI-2.png)



根据你的镜头视图，你可能没有看到 GUI 所在的列的表面。如果你看不到按钮，请移动你的镜头，直到你看到它。 

## 更改 GUI 外观

如你所见，表面 GUI 被放置在部件的_前_表面。这并不总是你想要的 GUI，所以让我们改变它。

  1. 选择 **SurfaceGui** 对象（而不是其中的图像按钮）。
  2. 在“Properties（属性）”窗口中，找到 **Face** 属性并从下拉列表中选择 **Top**。现在表面 GUI 以及其中的按钮都将位于此列的顶部。
![](https://developer.roblox.com/assets/bltb93c40199aa7e997/Interactive-Surface-GUI-Change-GUI-Face-1.png)



虽然按钮现在在顶部表面上，但它太小了，它藏在一个角落里，甚至不像图像那样完美的圆形！

请记住，将表面 GUI 的**画布大小**设置为它所在表面的相同比例。因为我们把它移到了顶部表面，所以我们需要改变画布大小来与之匹配。

  1. 确保 **SurfaceGui** 对象仍处于选中状态。
  2. 请记住，比较方便的做法是，将画布大小在每个方向上设置为表面的格长度的 100 倍。由于顶部表面是 2 × 2 格，因此将 **CanvasSize** 的 **X** 和 **Y** 更改为 200。
![](https://developer.roblox.com/assets/bltc65bb09f3316d4b3/Interactive-Surface-GUI-Change-GUI-Face-2.png)



### 自定义按钮

此时，按钮仍然不像玩家所期望的那样。它仍然藏在表面的一个角落里，没有朝着正确的方向。下面就让我们来修复所有这些以及更多问题吧！

  1. 选择图像按钮，并将 **AnchorPoint** 属性都设置为 0.5。
![](https://developer.roblox.com/assets/blt79da1b8589ced425/Customize-SurfaceGUI-TextLabel-1.png)



  2. 将 **BackgroundTransparency** 改为 1 让背景可见。

  3. 将 **Position（位置）** → **X** → **Scale（比例）**和 **Y** → **Scale（比例）**都设置为 0.5。这将使标签在表面 GUI 的边界内居中。

![](https://developer.roblox.com/assets/bltc34cb8d3c21f6141/Interactive-Surface-GUI-Customize-SurfaceGUI-TextLabel-2.png)



  4. 对于 **Size（大小）**，将 **X** → **Offset（偏移）**和 **Y** → **Offset（偏移）**都设置为 150。
![](https://developer.roblox.com/assets/blt723f9c53501cc3e7/Interactive-Surface-GUI-Customize-SurfaceGUI-TextLabel-3.png)



  5. 将 **Rotation（旋转）**设置为 -90 以使按钮朝向正确的方向（从列的前面朝向后面）。
![](https://developer.roblox.com/assets/blt9fed8377b49cd452/Interactive-Surface-GUI-Customize-SurfaceGUI-TextLabel-4.png)



### 连接本地脚本

最后一个任务是将一个函数连接到按钮的 `GuiButton/Activated|Activated` （已激活）事件。对于本指南，该函数仅用于将布尔变量设置为 `true` 或 `false`。在真正的游戏中，按下按钮可能会打开一扇密门或打开一个交互式的屏幕 GUI。

  1. 在管理器窗口中，将鼠标悬停在 **ImageButton** 对象上，然后插入 **LocalScript**。
![](https://developer.roblox.com/assets/bltfbfd37470bd9d33a/New-LocalScript.png)



  2. 在新脚本中，删除任何现有代码，然后复制并粘贴到这些新行中：
    
    
    local button = script.Parent
    local toggled = false
     
    local function onButtonActivated()
    	if toggled == false then
    		toggled = true
    		-- 当按钮开启时进行操作
    		--
    	else    
    		toggled = false
    		-- 当按钮关闭时进行操作
    		--
    	end
    end
     
    button.Activated:Connect(onButtonActivated)
    

* * *

除了一个简单的按钮，你还能想到什么其他的想法？挑战自己，创建一个打开密门的按钮，甚至是一台打开一个大型交互式 `articles/Intro to GUIs|屏幕 GUI` 显示屏的触摸屏计算机。选项无穷无尽！



***__Roblox官方链接__:[交互式表面 GUI](https://developer.roblox.com/zh-cn/articles/Interactive-Surface-GUI)