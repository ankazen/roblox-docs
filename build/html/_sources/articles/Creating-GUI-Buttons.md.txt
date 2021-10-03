# 创建 GUI 按钮 
Time:<em>10  分钟</em>

本文将拓展`articles/Using Images in GUIs|在 GUI 中使用图像`的教程，并演示如何制作可以在菜单、游戏内操作等内容中使用的屏显按钮。

## 按钮类型

### 文本按钮

`TextButton` 与 `TextLabel` 非常相似，区别在于玩家可以点击或触碰来激活它。它在内部也与文本标签有许多相同的视觉属性：字体，背景颜色，描边颜色等等。

![](https://developer.roblox.com/assets/blt3b41c5fcae887a74/Text-Button-Example.png)



### 图像按钮

同样，`ImageButton` 也像是 `ImageLabel` 对象的互动版本，使用您上传至 Roblox 的一张自定义图像。它也与其非按钮版本共享许多同样的属性。

![](https://developer.roblox.com/assets/blt57ed7bcddba87667/Image-Button-Example.png)



## 创建按钮

本文其余的部分将演示如何在屏幕上添加一个 `ImageButton`，并根据玩家的互动来切换三种不同的外观。

### 添加一个 ImageButton

  1. 在 Explorer（管理器）窗口中，将鼠标悬停在 **StarterGui** 对象上，点击圆形 ![](https://developer.roblox.com/assets/blt0dd97240c2a0db2a/Explorer-Plus-Icon.png)

 按钮，然后插入一个 **ScreenGui** 对象。
  2. 选择新的 **ScreenGui** 对象，然后以类似的方式插入一个 **ImageButton**。
![](https://developer.roblox.com/assets/blt4e313d906cf97b91/Add-ImageButton-1.png)



这将在游戏视图的角落添加一个空白的图像按钮。

![](https://developer.roblox.com/assets/blt6c2524e15ef4f7de/New-ImageButton-1.png)



### 上传图像

此按钮需要三张自定义图像：它在屏幕上的正常外观，鼠标悬停时的外观，以及玩家按下按钮时的外观。

![](https://developer.roblox.com/assets/bltceee05c433f1fc16/ImgButtonNormal.png)

 ImgButtonNormal

![](https://developer.roblox.com/assets/blt6a44e16ed2ae1f88/ImgButtonHover.png)

 ImgButtonHover

![](https://developer.roblox.com/assets/blt4cecb613af7f0574/ImgButtonPressed.png)

 ImgButtonPressed

您可以用这些菜单按钮来测试，只需右键点击每个按钮并选择 **Save Image As...（另存图像为...）**来保存至您的电脑中。 

与其单独上传每张图像，您可以用 [Asset Manager（资源管理器）](/resources/studio/Asset-Manager)一次上传多张图像：

  1. 如果尚未打开，点击 **View** （视图）选项卡的 **Asset Manager** （资源管理器）。
![](https://developer.roblox.com/assets/blt920c84884e646d5b/Toggle-Game-Explorer.png)



  2. 点击窗口顶部附近的 **Import** （导入）按钮。
![](https://developer.roblox.com/assets/blt6d000574d5048053/Asset-Manager-Import-Button.png)



  3. 找到您电脑中的三张图像，选择并确认上传。
  4. 上传完成后，双击 **Images** （图像）文件夹或从树状图菜单中选择 **Images**。

![](https://developer.roblox.com/assets/blt1e6408581c921750/Asset-Manager-Images-Folder-1.png)



![](https://developer.roblox.com/assets/bltdb3624d3b5c2d132/Asset-Manager-Images-Folder-2.png)



在文件夹中，您应该可以看见新的图像：

![](https://developer.roblox.com/assets/bltedad54c26573042e/Add-Images-2.png)



### 设置外观

通过 `ImageButton` 对象可设置按钮的三种外观。

  1. 在管理器窗口中，选择 **ImageButton** 对象。
![](https://developer.roblox.com/assets/blt4e313d906cf97b91/Add-ImageButton-1.png)



  2. 在 **Properties** （属性）窗口中，点击 **Image** （图像）属性并选择 **ImgButtonNormal** 资源。
![](https://developer.roblox.com/assets/blt3a3905103d9fb913/Set-Buttton-Images-Normal.png)



  3. 点击 **HoverImage** 属性并选择 **ImgButtonHover** 资源。
![](https://developer.roblox.com/assets/bltd86feaebec02bf02/Set-Buttton-Images-Hover.png)



  4. 点击 **PressedImage** 属性并选择 **ImgButtonPressed** 资源。
![](https://developer.roblox.com/assets/blt8cbd63c80a9b055b/Set-Buttton-Images-Pressed.png)



### 调整按钮

要决定按钮在屏幕上的最终外观，请做出如下调整：

  1. 在属性窗口中，将 **BackgroundTransparency** 的值设为 **1**，使背景变为透明。
![](https://developer.roblox.com/assets/bltf03bf5b70d762219/Add-ImageButton-2.png)



  2. 将 **Position** → **X** → **Offset** 和 **Position** → **Y** → **Offset** 都设为大约 50，使按钮从角落中移开。
![](https://developer.roblox.com/assets/blt5e75340fa9a34bb7/Add-ImageButton-3.png)



### 附加 LocalScript

最后的工作是连接基本的按钮功能。

  1. 在“Explorer（管理器）”窗口中，将鼠标悬停在 **ImageButton** 对象上，点击圆形 ![](https://developer.roblox.com/assets/blt0dd97240c2a0db2a/Explorer-Plus-Icon.png)

 按钮，然后插入一个 **LocalScript** 对象。这将创建一个新的 `LocalScript` 并显示它。
![](https://developer.roblox.com/assets/blt3d663d50e2c756a4/ImageButton-LocalScript.png)



  2. 在脚本中，复制并粘贴以下新行：

基本按钮激活（LocalScript） ```    
    
    local button = script.Parent
    
    local function onButtonActivated()
    	print("按钮已激活！")
    	-- 在这里执行按钮对应的操作
    
    end
    
    button.Activated:Connect(onButtonActivated)


```
这是一个基本按钮脚本，其作用如下：

  * 第一行设置一个变量 `button`，让脚本明白它连接的是哪个对象。这里它连接的是 `ImageButton`，即脚本的父项。

  * `onButtonActivated()` 函数是按钮激活的主处理函数。您可以在里面执行按钮的操作，例如开启游戏的主菜单。

  * 最后一行**连接** `onButtonActivated()` 函数和 `GuiButton/Activated|Activated` （已激活）事件。这将使函数在玩家每次于游戏中激活按钮时运行。

虽然有许多种不同的事件可以连接至按钮，`GuiButton/Activated|Activated` 是基本按钮最可靠的选择，可在电脑、手机、平板电脑以及主机等各种平台上提供标准按钮行为。 

##### 按钮错误排查

If the button doesn’t work as expected, check the following:

  * Make sure you used a client-side `LocalScript`, not a server-side `Script`.
  * Ensure that the `LocalScript` is a **direct child** of the `ImageButton` object (not the top-level `ScreenGui` parent).
  * Confirm that your `ImageButton` object's **Image**, **HoverImage**, and **PressedImage** properties are set to the appropriate image assets.

  




***__Roblox官方链接__:[创建 GUI 按钮](https://developer.roblox.com/zh-cn/articles/Creating-GUI-Buttons)