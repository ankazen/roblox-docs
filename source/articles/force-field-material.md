# 力场材质 
Time:<em></em>

力场材质可以被用来创建各种特殊效果，不管是闪闪发光的护盾还是光芒刺眼的利刃都不在话下。

## 力场边框

如果立场材质的部件与其它部件出现了重叠，那么重叠的边框将会被显示出来。

![](https://developer.roblox.com/assets/blt430f480bd0925c04/forceFieldSeperate.jpg) ![](https://developer.roblox.com/assets/blt435245970bc26809/forceFieldOverlapping.jpg)

## 纹理动画

通过同时应用力场与纹理，可以创造各种各样的视觉效果。只有使用自定义纹理的 MeshPart 才能添加动画效果。当设计纹理时，纹理图像 **RGB** 通道的**红色**分量决定了所显示的重叠部分。具体的移动动画为随机决定，无法直接进行操控。

下面列举了部分示例纹理以及其所导致的力场：

RGB 纹理 红色分量 动画

![](https://developer.roblox.com/assets/blt9ed5a981465c401d/forceField-textureExamples-hexColor.jpg)
![](https://developer.roblox.com/assets/bltb4aee6c67663d12f/forceField-textureExamples-hexR.jpg)
![](https://developer.roblox.com/assets/blt417b2efe41cd980b/forceField-hexPattern.gif)

![](https://developer.roblox.com/assets/blt1dcab1ce4e5777bf/forceField-textureExamples-gradientColor.jpg)
![](https://developer.roblox.com/assets/blt9a17b4ea4c8765ad/forceField-textureExamples-gradientR.jpg)
![](https://developer.roblox.com/assets/blt727aea95e2edfbe6/forceField-gradient.gif)

![](https://developer.roblox.com/assets/blt600362fb6366eb42/forceField-textureExamples-symbolColor.jpg)
![](https://developer.roblox.com/assets/blt41f5f3ad89706763/forceField-textureExamples-symbolR.jpg)
![](https://developer.roblox.com/assets/bltea4b68ca60a488fc/forceField-unique.gif)

## 顶点绘制

通过使用 3D 建模应用程序改变网格的顶点 Alpha 轮廓，可以修改力场的边框。顶点颜色的 Alpha 通道控制了边框的不透明度。值为 1 时无强制着色，为 0 时为全强制着色。

![](https://developer.roblox.com/assets/blte1f38428ee96a496/forceField_texturePaint_setup.jpg)

![](https://developer.roblox.com/assets/bltf010950c6ebed4b3/forceField_texturePaint_example.jpg)

同时，顶点颜色染色可以用来影响力场上所显示的颜色。

![](https://developer.roblox.com/assets/bltde577e9c37fcb949/forceField_paintColor_setup.jpg)

![](https://developer.roblox.com/assets/blt438a56657a6a823c/forceField_paintColor_example.jpg)



***__Roblox官方链接__:[力场材质](https://developer.roblox.com/zh-cn/articles/force-field-material)