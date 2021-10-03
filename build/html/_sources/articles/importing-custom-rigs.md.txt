# 导入自定义模型 
Time:<em>10  分钟</em>

本文概述了 Roblox 从 Autodesk Maya 或 Blender 导入自定义模型的流程（包括带有动画的模型），可作为非玩家角色与机械对象等使用。

## 关于模型的指导原则

### 常规准则

在 Maya 或 Blender 中构建角色模型时，请遵循以下常规准则：

  * 确保将单位设置为 **Centimeter（厘米）**。
  * 几何体网格应仅具有转换值。这些值应相对于其父关节。举例来说，如果从其关节取消网格的父项，则应将转换值清零 (**0**, **0**, **0**)。

如果没有看到此情况，请取消几何体网格的父项，冻结其变换，然后将其父项设置回各自关节。现在，它们应该具有本地转换值，并且如果取消父项，则将它们清零。 

  * 所有关节均应正确放置且任何轴均不得旋转，它们应该都为 (**0**, **0**, **0**)。同样，每个关节的比例应保持默认值，并设置为 (**1**, **1**, **1**)。

### 模型层次结构

对于总体上的模型层次结构，请确保：

  * 具有名为 **Root**（区分大小写）的最高级关节。
  * **Root** 的每个子代关节都有一个名称相同、或名称带有 **_Geo** 后缀的匹配的几何体。比如，如果关节名为 **Torso**，那几何体的名称应为 **Torso** 或 **Torso_Geo**。

Root

![](https://developer.roblox.com/assets/blt0e5b38e8e28b4dee/Hierarchy-Tree-End.png)



Torso

![](https://developer.roblox.com/assets/blt070fe939a497b781/Hierarchy-Tree-Split.png)



Torso_Geo

![](https://developer.roblox.com/assets/blt070fe939a497b781/Hierarchy-Tree-Split.png)



RightUpperLeg

![](https://developer.roblox.com/assets/blt9817f6f24bade38d/Hierarchy-Tree-Connect.png)



![](https://developer.roblox.com/assets/blt070fe939a497b781/Hierarchy-Tree-Split.png)



RightUpperLeg_Geo

![](https://developer.roblox.com/assets/blt9817f6f24bade38d/Hierarchy-Tree-Connect.png)



![](https://developer.roblox.com/assets/blt0e5b38e8e28b4dee/Hierarchy-Tree-End.png)



RightLowerLeg

![](https://developer.roblox.com/assets/blt9817f6f24bade38d/Hierarchy-Tree-Connect.png)



![](https://developer.roblox.com/assets/blt0e5b38e8e28b4dee/Hierarchy-Tree-End.png)



RightLowerLeg_Geo

![](https://developer.roblox.com/assets/blt0e5b38e8e28b4dee/Hierarchy-Tree-End.png)



LeftUpperLeg

![](https://developer.roblox.com/assets/blt070fe939a497b781/Hierarchy-Tree-Split.png)



LeftUpperLeg_Geo

![](https://developer.roblox.com/assets/blt0e5b38e8e28b4dee/Hierarchy-Tree-End.png)



LeftLowerLeg

![](https://developer.roblox.com/assets/blt0e5b38e8e28b4dee/Hierarchy-Tree-End.png)



LeftLowerLeg_Geo

## 导出模型

请参阅下列指导，具体取决于您正在从哪一软件导出（Maya 或 Blender）。

##### 从 Maya 导出 »

从 Maya 导出角色之前，确保将单位设置为 **Centimeters（厘米）**。然后使用 **File（文件）** → **Export All（全部导出）**并对默认设置进行以下更改：

设置 值

几何体

**平滑网格**
已启用

**参考资产内容**
已启用

单位

**自动**
已启用

轴转换

**上轴**
Y

FBX 文件格式

**类型**
二进制

**版本**
FBX 2014/2015

如果还要导出纹理，请打开 **Embed Media（嵌入媒体）**部分并确保选中 **Embed Media（嵌入媒体）**。 

  


##### 从 Blender 导出 »

从 Blender 导出角色之前，请确保将单位设置为 **Centimeters（厘米）**。然后在 **Export FBX（导出 FBX）**面板中，对默认设置进行以下更改：

设置 值

**Camera（镜头）**按钮
已禁用

**Lamp（灯具）**按钮
已禁用

如果要将纹理导出为嵌入媒体，请将 **Path Mode（路径模式）**设置为 **Copy（复制）**并单击其右侧的框，这样看来好像正在弹出纸张。请注意，这只适用于**二进制** FBX 导出，而不适用于 ASCII。 

  


## 导入至 Roblox Studio

想要了解导入自定义模型的流程，可下载[本示例](?disposition=attachment)（SimpleDog.fbx）。

[下载](?disposition=attachment)

下载好 FBX 文件后，请按如下步骤操作：

  1. 从 Studio 的 **Plugins** 选项卡中，点击 **Avatar Importer**（角色导入）按钮。
  2. 点击四个选项中的 **Custom**（自定义）选项。
![](https://developer.roblox.com/assets/bltf5f0388ec7393a4b/Avatar-Importer-Choices-Custom.png)



  3. 浏览下载好的文件（SimpleDog.fbx）。导入 Studio 中后应为此模型。

(_IMAGE_)

![]()

## 导入/导出动画

如果您使用 Maya 或 Blender 直接进行了模型的动画制作，您可以通过 Roblox 的内置 `/articles/using animation editor|动画编辑器`来导入及上传动画。

### 导入动画

若想从 FBX 文件中导入动画：

  1. 在 **Plugins** 选项卡中，点击 **Animation Editor**（动画编辑器） 。
  2. 选择模型（**ImportedCustomRig**）并点击 **Create** （如果可以的话）。如有关于 R15 虚拟角色的警告信息，直接忽略即可。
  3. 从动画编辑器的 **File** 菜单中（非 Studio 的 File 文件菜单）选择 **Import FBX Animation**（导入 FBX 动画）。
  4. 浏览并选择同一 FBX 文件（SimpleDog.fbx）。

##### 计算髋高 »

任何通过 Avatar Importer 虚拟角色导入器导入的模型都会被分配为 `Humanoid` 人型生物对象，即使他们看上去并非如此。人型生物包括有若干随模型设计和高度而变化的属性，如 `Humanoid/HipHeight|HipHeight` 。

确定大致的 `Humanoid/HipHeight|HipHeight` 值的方式如下：

  1. 移动模型以使其脚部/底座的 **Y** 位置为 **0** ，如待在默认的 **Baseplate** 上的对象。
  2. 在 Studio 的命令栏（**View** → **Command Bar**）中，粘贴下面的代码。
  3. 从 Output 输出窗口中（**View** → **Output**）复制或记录下显示的值；后面测试自定义模型时会用到。
    
    
    local hrp = workspace.ImportedCustomRig.HumanoidRootPart
    print(hrp.Position.Y - (0.5 * hrp.Size.Y))
    

  


### 导出动画

当您将动画顺利导入之后，还需要将其上传到 Roblox 。

  1. 动画编辑器的 **File** 菜单中（而不是 Studio 的 File 文件菜单）选择 **Export**（导出） 。
  2. 选择新栏位或者已有栏位。
  3. 上传完成后，**复制或记录动画的 ID**，随后在测试自定义模型时会用到。

https://www.roblox.com/catalog/2350495664

  4. 从对话窗口退出；此时，您可以把动画编辑器窗口也一并关闭。

## 在 Studio 中进行测试

最后一个环节：您可以按如下方式来测试模型：

  1. 在管理器窗口中，将 **ImportedCustomRig** 移动到 **ServerStorage** 中。
![](https://developer.roblox.com/assets/bltf70acefa9a82c0bc/Avatar-Importer-Custom-Testing-1.png)



  2. 将鼠标放在 **ServerScriptService** 上，点击 ![](https://developer.roblox.com/assets/blt0dd97240c2a0db2a/Explorer-Plus-Icon.png)

 按钮，并插入一个新的 **Script** 。
![](https://developer.roblox.com/assets/blta9c6e12716caec27/Avatar-Importer-Custom-Testing-2.png)



  3. 将刚才创建的新脚本重命名为 _CreateObjectFromRig_。
  4. 将下列代码粘贴到该脚本中。

```    
    
    local ServerStorage = game:GetService("ServerStorage")
    
    local animationID = 0000000000
    
    -- 将模型复制到 workspace 工作区并设置各属性
    local template = ServerStorage.ImportedCustomRig
    local object = template:Clone()
    local humanoidObject = object.Humanoid
    humanoidObject.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.None
    humanoidObject.HipHeight = 2.45
    object.Parent = workspace
    
    -- 设置模型位置
    object:MoveTo(Vector3.new(20, 4, 0))
    
    -- 创建自定义动画
    local animation = Instance.new("Animation")
    animation.AnimationId = "rbxassetid://" .. animationID
    animation.Parent = ServerStorage
    
    -- 播放自定义动画
    local animationTrack = object.Humanoid:LoadAnimation(animation)
    animationTrack:Play()


```
  5. 在第 3 行，将 `animationID` 值改为您之前在导出动画部分记下的 ID。

```    
    
    local ServerStorage = game:GetService("ServerStorage")
    
    local animationID = 2350495664
    
    -- 将模型复制到 workspace 工作区并设置各属性


```
  6. 在第 10 行，将 `humanoidObject.HipHeight` 值改为您在 Hip Height 部分计算所得的数字。

```    
    
    -- 将模型复制到 workspace 工作区中并设置各属性
    local template = ServerStorage.ImportedCustomRig
    local object = template:Clone()
    local humanoidObject = object.Humanoid
    humanoidObject.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.None
    humanoidObject.HipHeight = 2.9460468292236
    object.Parent = workspace


```
  7. 进行游戏，您应该会在游戏中看到狗了。它会以在 FBX 文件中事先配置的简单动作来进行移动。

(_VIDEO_)



***__Roblox官方链接__:[导入自定义模型](https://developer.roblox.com/zh-cn/articles/importing-custom-rigs)