# 45 度镜头视角 
Time:<em>10  分钟</em>

45 度镜头是在许多 RPG 和战略游戏中使用的一种镜头视角。其特点为镜头通常在固定的高度以一定的角度向下俯视。本文介绍如何实现集成至默认 Roblox 控制的一个 45 度镜头示例。

![IsoCamExample.png](https://developer.roblox.com/assets/blt17ec54dba731659f/IsoCamExample.png)



## 插入 45 度镜头

45 度镜头脚本需要对当前镜头 PlayerScript 稍加修改才能运行。如果希望对脚本进行复制，只需启动 Studio 的新实例，单击 “Play（开始游戏）”，查看 “Players（玩家）”> “Player1（玩家 1）”> PlayerScripts，然后复制名为 CameraScript 的整个 LocalScript（包括其所有子项） 。

![DefaultCameraScript.png](https://developer.roblox.com/assets/bltfd5534b4b610df68/DefaultCameraScript.png)



停止游戏并将复制的脚本放在 StarterPlayer > StarterPlayerScripts 中：

![NewCameraPlayerScript.png](https://developer.roblox.com/assets/blt38e071594fe7a03d/NewCameraPlayerScript.png)



将以下代码插入名为 _ThreeFourthsCamera_ 的 ModuleScript 中。将此模块脚本插入到 RootScript 中。

![InsideRootScript.png](https://developer.roblox.com/assets/bltf026bb8ddea9d9d2/InsideRootScript.png)



我们需要在 CameraScript 的 LocalScript 中声明这个新镜头。在脚本顶部声明其他镜头的地方插入以下行：
    
    
    local ThreeFourthsCamera = require(RootCamera.ThreeFourthsCamera)()
    

从此处实现 45 度镜头最为简单的方法就是使 CameraScript 忽略其他镜头模式，并始终启用 45 度镜头。为此，请修改 CameraScript 中的 SetEnabledCamera 函数，如下所示：

## 自定义

45 度镜头具有多个配置选项，更改后可以自定义玩家体验。所有配置都在 CreateThreeFourthsCamera 函数中。一些关键配置如下：

配置 描述

ZoomEnabled
设置玩家是否可以缩放镜头。

PanEnabled
设置玩家是否可以平移镜头。

RotateEnabled
设置玩家是否可以旋转镜头。

useEdgeBumpPanning
设置玩家是否可以通过将鼠标移到屏幕边缘来平移镜头。

pitch
控制镜头的默认俯仰角度。

roll
控制镜头的默认横摆角度。

yaw
控制镜头的默认偏航角度。

mode
设置镜头是锁定到玩家角色还是可以自由移动。只能设置为 *"Locked"* 和 *"Free"*。



***__Roblox官方链接__:[45 度镜头视角](https://developer.roblox.com/zh-cn/articles/Three-Quarters-Camera-View)