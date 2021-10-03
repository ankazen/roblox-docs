# 粒子发射器 
Time:<em>5  分钟</em>

**粒子发射器**通过结合使用 2D 图像以及颜色、尺寸等属性来创建例如火焰、烟雾和火花等特殊效果。

![](https://developer.roblox.com/assets/blt6991707a4e36929e/Particle-Hero.jpg)

## 创建粒子发射器

所有粒子发射器的父项都必须为 `BasePart` 类对象，例如 `Part` 或 `MeshPart` 等。

若希望创造粒子发射器，请遵循以下步骤：

在 Explorer（管理器）窗口中选中对象，并使用 ![](https://developer.roblox.com/assets/blt0dd97240c2a0db2a/Explorer-Plus-Icon.png)

 图标插入一个 **ParticleEmitter**。

![](https://developer.roblox.com/assets/bltd43b6a485fbbc039/Insert-Emitter.png)



创建完毕后，粒子发射器将在该部件的区域中发射粒子。发射器的父对象决定了其发射的方向和旋转度。

![](https://developer.roblox.com/assets/blt4fbfddc496139cd8/Emitter-Small-Area.png)

 小面积压实颗粒

![](https://developer.roblox.com/assets/blta9d4206b80ade0ab/Emitter-Large-Area.png)

 大面积散布颗粒

![](https://developer.roblox.com/assets/blt4ac07eb4e38017b0/Emitter-Part-Rotation.png)

 部件旋转改变方向

  2. 如果希望更改粒子效果的方向而不重新定位其父部件，请使用发射器的 **EmissionDirection** 属性。

![](https://developer.roblox.com/assets/bltfd0976c6ec655fcc/Emission-Direction-Front.png)

 **前方** EmissionDirection

![](https://developer.roblox.com/assets/blt85d42ebf7a240424/Emission-Direction-Bottom.png)

 **下方** EmissionDirection

## 自定义粒子

添加发射器后，你可以通过其属性修改粒子发射效果。以下是粒子发射器的一些常见属性：

### Texture（纹理）

更改粒子使用的图像。若要导入粒子图像，请参阅`/articles/game assets#images|游戏资源`一文。

![](https://developer.roblox.com/assets/blt31fac640c3547982/Emitter-Texture.jpg) 具有不同纹理的相同粒子设置

建议使用具有透明度的 PNG 图像。如果你的纹理是没有 Alpha 通道的灰度图像，请尝试将发射器的 **LightEmission** 属性设置为 **1** 以隐藏较暗的区域。 

### 颜色

此属性将粒子纹理着色为特定的颜色。可以通过三种方式选择颜色：

![](https://developer.roblox.com/assets/bltfc52c3e1b3c2a119/Emitter-Color-Options.png)



**A**

单击颜色方块，打开颜色选择器。 

**B**

输入代表 RGB 颜色值的三个数字。 

**C**

创建颜色序列，让粒子颜色随时间变化而变色。 

![](https://developer.roblox.com/assets/blt47f0892faf4cec8a/Emitter-Color-Single.jpg) 单一颜色

![](https://developer.roblox.com/assets/blt124f0cd1fbec118c/Emitter-Color-Sequence.jpg) 颜色序列

##### 创建颜色序列 »

若要修改某个序列：

  * 单击现有的标记箭头以选择该序列中的一个点。
![](https://developer.roblox.com/assets/bltb5c22e501d9ba16e/Emitter-Color-Sequence-1.png)



  * 选择标记后，即可更改颜色。
![](https://developer.roblox.com/assets/blt204f5a8babe31396/Emitter-Color-Sequence-2.png)



  * 可以通过单击时间轴上的一个点来插入其他标记。可以通过左右拖动来移动这些标记，也可以通过单击 **Delete（删除）**按钮将其删除。
![](https://developer.roblox.com/assets/bltf9f296113c018a09/Emitter-Color-Sequence-3.png)



  


### Size（尺寸）

粒子的尺寸以格为单位。开发者可以通过两种方式定义粒子尺寸：

![](https://developer.roblox.com/assets/bltc52998a7fe52f122/Emitter-Size-Options.png)



**A**

输入代表恒定尺寸的数字。 

**B**

创建一个尺寸序列，使粒子尺寸随时间流逝进行改变。 

##### 创建尺寸序列 »

使用序列，粒子尺寸可以随时间变化。序列从 0 开始，即发射开始，到 1 发射结束，1 就是粒子的生存时间。

  * 若要更改某个点处的尺寸，请单击标记并将其向上或向下拖动。也可以在 **Value（值）**字段中输入值来指定该标记处的尺寸。
![](https://developer.roblox.com/assets/blt7d4dcafc7e48cc45/Emitter-Size-Sequence-1.png)



  * 若要插入新标记，请单击图形中的任意一点。
![](https://developer.roblox.com/assets/blt0596a9e7001a36ad/Emitter-Size-Sequence-2.png)



  * 若要增加尺寸的随机范围，请单击任意标记并上下拖动包络线。届时，粒子尺寸将成为红色包络线之间的随机尺寸。
![](https://developer.roblox.com/assets/blt5fbf8c9d1b3148bf/Emitter-Size-Sequence-3.png)



  


### Lifetime（持续时间）

粒子的持续时间以秒为单位进行定义。该持续时间可以是一个恒定值，也可以是格式为 **Min** （最小值）、**Max** （最大值）的最小值/最大值范围。粒子的最长持续时间为 20 秒。

### Rate（速率）

此属性指定了每秒创建的粒子数。一个发射器每秒可以产生多达 500 个粒子。

为了在 PC 和移动设备上获得最佳性能，请尝试将粒子速率保持在尽可能低的水平。对粒子纹理的大小、发射粒子的大小和其他属性进行实验，以最大程度减少粒子的数量，同时仍能达到所需的视觉效果。 

### 其他属性

下面是一些用于进一步自定义粒子的属性。

属性 描述

`ParticleEmitter/Acceleration|Acceleration`（加速）
确定粒子的加速方向。这可以用于创建诸如受风影响的粒子的效果。

`ParticleEmitter/Drag|Drag`（阻碍）
粒子损失一半速度的速率（以秒为单位）。

`ParticleEmitter/Rotation|Rotation`（旋转）
新创建的粒子的旋转角度。单个数字将以该角度创建粒子。使用两个数字（最小值和最大值）将为每个粒子设置随机旋转。

`ParticleEmitter/RotSpeed|RotSpeed`（旋转速度）
创建时粒子的旋转速度。这可以是单个数字，也可以是代表随机速度的数字范围。负值会导致粒子逆时针旋转。

`ParticleEmitter/Speed|Speed`（速度）
粒子运动的速度（以格为单位）。这可以是单个数字，也可以是代表随机速度的数字范围。负值会导致粒子反向移动。

`ParticleEmitter/Transparency|Transparency`（透明度）
所有活动粒子在其各自生存时间中的透明度。这可以是介于 0 和 1 之间的数字，也可以是类似于尺寸序列的某个定义序列。

`ParticleEmitter/ZOffset|ZOffset`（Z 偏移）
控制粒子渲染方式的向前/向后位置（以格为单位）。这对于同一区域中有多个粒子发射器的情况非常有用。

有关发射器属性的完整列表，请参见 `ParticleEmitter` API 页面。 

## 发射器示例

可以通过创建新的 `ParticleEmitter` 并将列出的属性更改为突出显示的值来实现以下发射器。

![](https://developer.roblox.com/assets/bltb68c79a706d0ee35/Emitter-Example-Book.jpg)

属性 - ParticleEmitter "ParticleEmitter"

LightEmission（发光）
0.5

Texture（纹理）
rbxhttp://asset/?id=3909691881

Drag（阻碍）
1

Lifetime（持续时间）
5

RotSpeed（旋转速度）
-100, 100

![](https://developer.roblox.com/assets/blt521f52c08be9f0b3/Emitter-Example-Barrel.jpg)

属性 - ParticleEmitter "ParticleEmitter"

Color（颜色）
![](https://developer.roblox.com/assets/bltfdef723117a1c35f/Studio-Color-Box-Sequence1.png)



<ColorSequence>（颜色序列）![](https://developer.roblox.com/assets/blt96267d1d59a99d09/Emitter-Example-Graph-Color.png)



LightEmission（发光）
0.7

Size（尺寸）

<NumberSequence>![](https://developer.roblox.com/assets/blt91df64ef5cc05e0a/Emitter-Example-Graph-Size.png)



Texture（纹理）
rbxhttp://asset/?id=3916143220

Transparency（透明度）

<NumberSequence>（数字序列）![](https://developer.roblox.com/assets/blt9e9bad80c5db9abe/Emitter-Example-Graph-Transparency-2.png)



Lifetime（持续时间）
3

Rate（速率）
10

![](https://developer.roblox.com/assets/blt3bf45668559ebecb/Emitter-Example-Portal.jpg)

属性 - ParticleEmitter "ParticleEmitter"

Color（颜色）
![](https://developer.roblox.com/assets/blt0dfc85cdbdd2c9fe/Studio-Color-Box-Scarlet.png)

 [255, 74, 29]

LightEmission（发光）
0.8

Size（尺寸）
5

Texture（纹理）
rbxhttp://asset/?id=3916186365

Transparency（透明度）

<NumberSequence>（数字序列）![](https://developer.roblox.com/assets/blt555dd00adb22f329/Emitter-Example-Graph-Transparency.png)



Lifetime（持续时间）
2

Rate（速率）
5

Rotation（旋转）
0, 360

RotSpeed（旋转速度）
100

Speed（速度）
0



***__Roblox官方链接__:[粒子发射器](https://developer.roblox.com/zh-cn/articles/Particle-Emitters)