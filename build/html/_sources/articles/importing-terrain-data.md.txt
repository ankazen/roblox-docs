# 导入地形数据 
Time:<em>5  分钟</em>

在`/articles/Intro To Terrain|环境与地形工具`当中，我们涉猎了手动地形生成的方法。除此之外，开发者还可以通过导入 heightmap（高度图）以及 colormap（颜色图）来创建地形。

## 导入 Heightmap（高度图）

**Heightmap（高度图）**是 3D 地形图的 2D 表示，形同于从正上方俯视。高度图上较亮的区域会在实际地形中表现为较高的地域，如山峰等。高度图中较暗则会形成诸如峡谷之类的区域。

![](https://developer.roblox.com/assets/blt08ebba3ddfaa88c6/Terrain-Heightmap.png)



![](https://developer.roblox.com/assets/blt4e539ce26d011f16/r-arrow-blue.png)



![](https://developer.roblox.com/assets/bltb0bf41ea76556bda/Terrain-Heightmap-Result.jpg)

若想在 Roblox Studio 中导入高度图，请遵循以下步骤：

  1. 在 **Home**（主页）选项卡中点击 **Terrain**（地形）部分的 **Editor**（编辑器）按钮。
![](https://developer.roblox.com/assets/blt614b8c09002f5ad2/Toggle-Terrain-Editor.png)



  2. 在 **Terrain Editor**（地形编辑器）窗口，点击 **Create**（创建）选项卡下的 **Import**（导入）按钮。
![](https://developer.roblox.com/assets/blt46fb94db6afb7c59/Terrain-Editor-Import.png)



  3. 在 **Map Settings**（地图设置）中点击 **Asset ID**（资源 ID），选择事先通过 Game Explorer（游戏管理器）上传的恰当高度图。

上传高度图时最好选择灰度图像，但是导入器仍可分辨 RGB 图像（其原理为仅使用图像中的**红色**通道来获取高度信息）。 

  4. 若有需求，可输入新的 **Position** （位置，也就是生成地形的中心）及其 **Size**（尺寸），单位以格计。需要注意的是，地形的最大范围维度没有强制的上限，系统测试时曾达到的最大格数为 16384×16384×1024 格。

最小和最大的地形高度将取决于导入期间高度图最暗和最亮的区域，最终的结果是相对于 **Y** 轴的尺寸（高度）而言的。举例来说，如果选择高度为 128，则纯黑色区域等于是中心位置



***__Roblox官方链接__:[导入地形数据](https://developer.roblox.com/zh-cn/articles/importing-terrain-data)