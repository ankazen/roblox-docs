# 在 GUI 中使用图像 
Time:<em>10  分钟</em>

在 `Articles/Intro to GUIs` 指南中，开发者学习了GUI 的基础知识、如何为所有进入自己游戏的玩家创建 Screen GUI 画布，以及如何在屏幕上放置一个 `TextLabel` GUI 对象并对其大小进行调整。如果开发者还没有完整阅读过 `Articles/Intro to GUIs` 指南，请先阅读该指南！

接下来我们将详细展开这些概念并探索如何在 Screen GUI 区域插入**图像**。这对于在屏幕上展示图标、标识、背景图像以及其他酷炫的设计是一个绝佳途径！

## 向一个 Screen GUI 中添加图像

将一张图像添加到 Screen GUI 的过程与添加一个文本标签非常相似。

  1. 在管理器窗口中找到 **ScreenGui** 对象（开发者可以使用在 `Articles/Intro to GUIs` 指南中创建的对象）
  2. 插入一个 `ImageLabel` 对象。记住，开发者可以通过在搜索字段中输入对象名称的前几个字母来快速查找。
![](https://developer.roblox.com/assets/blt7cee6a4552533a46/Add-ImageLabel-2.png)



这一操作会在游戏视图的左上角添加一个空白的图像标签。

![](https://developer.roblox.com/assets/blt7bf6f81219465500/Add-ImageLabel-3.png)



### 上传一张图像

有了这个空白图像标签，事情就基本上搞定了一半。但我们还需要在屏幕上放置一个真实的图像，现在就开始上传吧。

游戏必须被**发布到 Roblox** ，然后才能上传图像。如果开发者需要关于游戏发布的相关帮助，请 点击 这里。 

  1. 在 Roblox Studio 中，选择 **文件** → **发布到 Roblox**。
  2. 点击**新场景**。
  3. 键入名称和描述。
  4. 点击**创建场景**。
  5. 当进度条满格且为“100% 完成”时，点击蓝色的**下一步**按钮。
  6. 下一个屏幕界面上会显示游戏附加功能的有关信息。开发者可以选择跳过这些步骤 — 只需要点击**完成**按钮即可。 

  1. 在管理器窗口中选择新的 **ImageLabel** 对象。
![](https://developer.roblox.com/assets/blt9afe50926c654b85/Select-ImageLabel.png)



  2. 在属性窗口的 **图像**区域内，点击 **图像**属性。
![](https://developer.roblox.com/assets/blt1480ab6345145332/Click-Image-Field.png)



  3. 在弹出窗口中点击**添加图像…**。
![](https://developer.roblox.com/assets/blt53925f335a7f8e2e/Click-Add-Image.png)



如果开发者没有看到窗口弹出，那么就说明游戏可能还未**发布**。记住，必须要先确认游戏已 发布后才能上传图像。 

  4. 在下一对话框中单击 **选择文件**按钮。在电脑上找到并选中一张自己想要上传的图像。

![](https://developer.roblox.com/assets/blt79e4a8e82857168a/PlayIcon.png)

 开发者可以使用这个小图标 “play” 来进行测试 — 只需要右键点击这个小图标然后选择**将图像另存为...**，将它保存至一个便捷的位置，然后根据指示导航至此图像。 

如果想在菜单界面或类似的彩色背景界面上放置图像，开发者可以在图像编辑程序中对图像可见部分周围的像素进行**透明化**处理，这样背景或后面其他的游戏对象就能显示出来。 

  5. 开发者还可以在较小的 **名称**输入字段中键入另一个不同的名称。输入完毕后点击 **创建**按钮。
  6. 上传完成后，就能看到 **ImageLabel** 对象已更新为所选图像啦！
![](https://developer.roblox.com/assets/bltc4918e0967c903e4/ImageLabel-Image.png)



### 更改标签属性

目前图像已经上传并应用于 **ImageLabel** 对象，但我们还可以更改一些属性让它看起来更好！

  1. 如果属性窗口中的 **数据**区域没有展开的话，则将其展开。
  2. 在 **BackgroundTransparency** 值中输入 **1**，这样图像标签的背景就会完全透明化，图像背景后的所有内容都会显示出来。
![](https://developer.roblox.com/assets/blt0b74f4dd9bfee77c/Images-GUI-BackgroundTransparency-Changed.png)



  3. 开发者可以通过 **Size**属性设置图像标签的大小。首先，将 **Size** → **X** → **Offset（偏移）**更改为 **80**。
![](https://developer.roblox.com/assets/blt7da291e7e73568ec/Images-GUI-ImageLabel-X-Offset-Size-Changed.png)



  4. 同样地，将 **Size** → **Y** → **Offset（偏移）**也更改为 **80**，以保持图像比例不变。
![](https://developer.roblox.com/assets/blt2541e6f0b11e386d/Images-GUI-ImageLabel-Y-Offset-Size-Changed.png)



  5. 开发者还可以通过 **Position（位置）**属性来设置图像标签的位置。首先，将 **Position（位置）** → **X** → **Offset（偏移）**更改为 **40**。
![](https://developer.roblox.com/assets/bltf4bd36e9347c9c70/Images-GUI-ImageLabel-X-Offset-Position-Changed.png)



  6. 再将 **Position（位置）** → **Y** → **Offset（偏移）**更改至 **20**来使标签略微下移。
![](https://developer.roblox.com/assets/blt5723e66f752bab31/Images-GUI-ImageLabel-Y-Offset-Position-Changed.png)



  7. 最后，将 **Rotation（旋转）**值设置为 **-8**，使标签向逆时针方向稍微旋转一些。
![](https://developer.roblox.com/assets/bltb08bf69df1cb3102/Images-GUI-ImageLabel-Rotation-Changed.png)



## 在 Screen GUI 中进行图像分层

太棒了！现在开发者已经知道了如何将图像上传至 Roblox 并将它们放置到屏幕上。不过当开发者想要添加多个图像时，可能就需要考虑**分层**了。

在 Screen GUI 区域进行对象分层就像是在一张纸上贴多个贴纸。如果开发者将一个贴纸贴在另一个贴纸上，那该贴纸将会遮住后面的贴纸。但有时开发者可能会想以不同的方式来排列这些贴纸，比如把后面的贴纸移到最前面。

### 创建第二个图像标签

让我们将另一个图像放置到屏幕上以便展示如何进行分层操作。

  1. 向 **ScreenGui** 添加一个新的 **ImageLabel** 对象。



***__Roblox官方链接__:[在 GUI 中使用图像](https://developer.roblox.com/zh-cn/articles/Using-Images-in-GUIs)