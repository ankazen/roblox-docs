# 构建篝火 
Time:<em>5 分钟</em>

在本教程中，我们将使用碰撞开关、粒子和自定义光来制作篝火。

首先，为篝火构建一个基座。切记，如果你希望降低部件的厚度，就必须将 Studio 工具的递增量从 _1 格_更改为 _1/5 格_。

![CampfireBase1.png](https://developer.roblox.com/assets/blt9fe72cbd8cb74659/CampfireBase1.png)

 ![CampfireBase2.png](https://developer.roblox.com/assets/blt3fe297456843f05d/CampfireBase2.png)



我们现在会添加一个部件作为我们篝火的第一根木柴。插入一个新的 **Part（部件）**作为木柴并确保其 **Anchored（已锚固）**。

![CampfireInsertLog.png](https://developer.roblox.com/assets/blt812093ef50e39d1b/CampfireInsertLog.png)



我们需要旋转木柴，使其以一定的角度伸出基座。默认情况下，Studio 会阻止部件在旋转或移动时穿过其他部件。我们可以通过确保关闭碰撞开关来禁用此功能。

![CollisionsOn.png](https://developer.roblox.com/assets/blt16a653ec23bbd84a/CollisionsOn.png)

 ![CollisionsOff.png](https://developer.roblox.com/assets/bltdc8779b2fa10542c/CollisionsOff.png)



旋转木柴，使其以一定角度指向篝火的中心。

![CampfireRotateLog1.png](https://developer.roblox.com/assets/blt25841b2073a2909e/CampfireRotateLog1.png)

 ![CampfireRotateLog2.png](https://developer.roblox.com/assets/blt32e90c43d2d74e66/CampfireRotateLog2.png)

 ![CampfireRotateLog3.png](https://developer.roblox.com/assets/bltf6ee8def55ada545/CampfireRotateLog3.png)



用 **Duplicate（复制）**命令制作木柴的副本。请注意，在碰撞关闭的情况下，复制的木柴与第一根木柴处于完全相同的位置。使用“Rotate（旋转）”和“Move（移动）”工具来移动复制的木柴。

![CampfireLogDuplicate1.png](https://developer.roblox.com/assets/blteaceac6c36d3e418/CampfireLogDuplicate1.png)



再次复制木柴，并重新摆放副本。

![CampfireLogDuplicate2.png](https://developer.roblox.com/assets/blt7f6f4f495abb21b9/CampfireLogDuplicate2.png)



接着，我们必须添加火焰效果。选择木柴下的基座部件，单击“Model（模型）”选项卡，单击 **Effects（效果）**按钮，然后选择 **Fire（火焰）**。

![CampfireSelectFire.png](https://developer.roblox.com/assets/blt40ede16ebfc033d8/CampfireSelectFire.png)



![CampfireSmallFire.png](https://developer.roblox.com/assets/bltb98fa312f5c63f65/CampfireSmallFire.png)



默认的火焰大小可能不足以覆盖所有木柴。要使火焰效果变得更大，先打开 **Explorer（管理器）**和 **Properties（属性）**窗口。从 Workspace 中（可能位于你的其中一个部件内）选择 _Fire（火焰）_。将 _火焰_的 **Size** 属性更改为较大的值。在本示例中，10 用来覆盖木柴已绰绰有余。

![CampfireSizeProperty.png](https://developer.roblox.com/assets/blt79cc897ebb453c30/CampfireSizeProperty.png)



![CampfireLargeFire.png](https://developer.roblox.com/assets/blt532e15c02efb4217/CampfireLargeFire.png)



现在火焰看起来效果已经很不错了，但是还没有照亮周围的任何区域。要创建照明效果，我们就必须添加一个 **PointLight**。再次选择篝火的基座（即盛放火焰的部件），单击“Model（模型）”选项卡，接着单击 **Effects（效果）**，然后单击 **PointLight**。

![CampfireInsertPointLight.png](https://developer.roblox.com/assets/blt3f4731eef82f02b9/CampfireInsertPointLight.png)



![CampfireDimLight.png](https://developer.roblox.com/assets/blt37cf0805fdc1f69f/CampfireDimLight.png)



最后，让我们再将光源调亮一些，并让它发出近似火焰颜色的光芒。在“Explorer（管理器）”窗口中选择 _PointLight_。将 **Brightness** 属性更改为 10，将 **Range** 更改为 15，并为 **Color** 属性选择橙色。

![CampfirePointLightProperties.png](https://developer.roblox.com/assets/blt990e11997aa55b1b/CampfirePointLightProperties.png)



![CampfireFinished.png](https://developer.roblox.com/assets/blt9a7dcdfee9ab8923/CampfireFinished.png)



这样，我们就得到欢乐喜庆的篝火了！



***__Roblox官方链接__:[构建篝火](https://developer.roblox.com/zh-cn/articles/Building-a-Campfire)