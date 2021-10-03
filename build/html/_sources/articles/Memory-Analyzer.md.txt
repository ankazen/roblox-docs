# 内存分析器 
Time:<em>5  分钟</em>


    local me = "Brandon"
    -- 注释可引用本地 x = 2
    function namedFunction(param)
    	print(param)
    end
    namedFunction(me)
    

如果想要你的 Roblox 游戏大获成功，就应当让其在包括移动设备及平板电脑等各种支持平台上运行顺畅。提升游戏性能的关键因素之一是对内存使用的有效管理。内存对于移动设备来说格外重要。如果游戏在手机上运行的游戏时消耗过多内存，就会导致游戏崩溃。

地形、部件、图形效果、脚本、物理模拟以及声效等各种因素都能够造成内存消耗。Studio 的 Performance（性能）控件可以显示场景的内存消耗指标。通过这些指标，我们可以识别效果过多内存的场景。

## 分析工具

如果想要对游戏的内存消耗进行监测，可以使用以下两个工具：第一个是可以在 Studio 和客户端中打开的 Developer Console（开发者控制台）。第二个是 Studio 的 Performance（性能）控件。

### 开发者控制台

开发者控制台可以在其 Memory（内存）选项卡中显示正在运行场景的当前内存消耗：

![MemoryAnalyzerDevConsole.png](https://developer.roblox.com/assets/bltad9006e34b3cb630/MemoryAnalyzerDevConsole.png)



在 Mac 和 PC 设备上（客户端和 Studio 中）按下 F9 键即可打开控制台。

平台 开发者控制台的打开方式

Mac 和 PC（Studio 和客户端中）
按 F9 键

移动设备（平板电脑和手机）
在聊天系统中键入信息 "/console" 

游戏主机
在游戏内的设置菜单中选择开发者控制台



***__Roblox官方链接__:[内存分析器](https://developer.roblox.com/zh-cn/articles/Memory-Analyzer)