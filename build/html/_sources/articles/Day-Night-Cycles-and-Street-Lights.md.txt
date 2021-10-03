# 昼夜循环和路灯 
Time:<em>5  分钟</em>

在此教程中，我们将会向游戏内添加一个通过 Loop（循环）进行日夜更替的脚本和一盏通过条件语句定时进行开关的街灯。

## 更改游戏内时间

在默认情况下，Roblox 游戏并不会进行日夜更替。但若有需要，开发者可以通过脚本达成这一效果。首先，让我们来看看如何通过名为 `Lighting/SetMinutesAfterMidnight` 的函数来改变游戏内的时间：
    
    
    game.Lighting:SetMinutesAfterMidnight(5 * 60)
    

正如我们之前在关于函数的教程中所提到的，函数乃是开发者可以在代码中使用的特殊指令。举例来说，我们所常用的 _print_ 就是一个全局函数，可以供开发者随时进行调用。同时，也有一部分函数是与特定类型实例相关联的。比如这次用到的 `Lighting/SetMinutesAfterMidnight` 函数就是与 `Lighting` 实例相关联的。当使用这类函数时，同时需要指定与之一起使用的实例，其在代码中的格式与更改实例属性相似。需要注意的是，在更改属性时我们会用点号（.）分隔实例与函数，而在指定实例时应当使用冒号（:）。

函数 SetMinutesAfterMidnight 的使用方法非常直接：在该函数括号内填入的数字就是当前世界午夜过后的分钟数。举例来说，上述代码示例会将游戏内时间设为凌晨 5 点（5 个 60 分钟也就是 5 个小时）。

通过这个函数，我们可以多次持续地更改游戏内的时间：
    
    
    game.Lighting:SetMinutesAfterMidnight(5 * 60)
    game.Lighting:SetMinutesAfterMidnight(6 * 60)
    game.Lighting:SetMinutesAfterMidnight(7 * 60)
    game.Lighting:SetMinutesAfterMidnight(8 * 60)
    game.Lighting:SetMinutesAfterMidnight(9 * 60)
    

上述代码会将时间逐步从凌晨 5 点更改至上午 9 点，但若此时进入游戏，玩家会看到游戏时间立刻变为上午 9 点。这又是怎么回事呢？为什么时间没有进行逐步变更呢？

虽然游戏程序的确按照我们的指令对游戏内时间进行了逐步变更，但其运行速度过快，导致我们无法观测到时间变更的结果。由于游戏在运行脚本时会使用其最快速度，导致绝大多数指令都会在瞬间完成，无法观察其运行过程。为了让玩家真正体验到游戏内时间的流逝，我们需要让脚本在每次进行变更后暂停一段时间。在本示例中，我们将会使用 “wait” 全局函数达成这一目标：
    
    
    game.Lighting:SetMinutesAfterMidnight(5 * 60)
    wait(1)
    game.Lighting:SetMinutesAfterMidnight(6 * 60)
    wait(1)
    game.Lighting:SetMinutesAfterMidnight(7 * 60)
    wait(1)
    game.Lighting:SetMinutesAfterMidnight(8 * 60)
    wait(1)
    game.Lighting:SetMinutesAfterMidnight(9 * 60)
    

在脚本中调用 _wait_ 时，指令就会按照我们所指定的时长进行暂停（以秒为单位）。在上述代码中，每次时间变更之后脚本都会暂停 1 秒钟，以便我们观察游戏内时间的流逝。

## Loop（循环）

虽然上述代码可以在短时间内正常运行，但如果我们希望游戏内的时间一直不停流逝，又应该怎么办呢？难道说要写下成千上万行相似的代码吗？在这里，我们可以使用一个名为 Loop（循环）的功能。这个十分简单易行的功能可以替我们完成这项艰巨的任务。

循环是一段可以不断重复执行的代码，只有在满足特定条件后循环才会结束。有些循环甚至可以无限运行，直到游戏本身结束为止。我们此次将会使用这些无限循环中的一种，名为 while 循环。请看下列示例代码：
    
    
    number = 0
    while true do
    	number = number + 1
    	print(number)
    	wait(1)
    end
    

脚本的第一行创建了一个名为 _number_ 的变量，并将一个为 0 的值储存在其中。脚本第二行设置了类型为 _while_ 的循环，而其后面的 _true_ 为循环重复执行的条件。由于我们并不像让这个循环结束，此处只需将条件设置为 _true_ 即可让循环无限运行下去（我们将在后面的课程中详细解释循环的停止方法）。_do_ 和 _end_ 之间的代码片段就是我们想要其进行重复的操作了。在本代码示例中，每循环一次，脚本就会对 **number** 变量内储存的值添加 1，而添加后的结果又将被储存进 _number_ 变量中去。之后我们将会输出 _number_ 的值，并命令脚本暂停 1 秒钟。之后循环将会再次运行，为 _number_ 内储存的值再次添加 1，以此类推。

类似上述示例中能够不停运行下去的循环被我们称为无限循环。虽然无限循环的用途十分广泛，但在使用时需要格外注意：一定要在循环所重复的代码块中添加一个 *wait* 函数，否则游戏将会崩溃。 

你或许已经注意到，上述示例 while 循环中的代码都向右移动了一段距离。这种格式叫做缩进，是代码编写时的常用规则。缩进并不会影响到代码的运行速度，而是通过改变其格式让代码更为清晰易读。当在循环、条件语句或函数内部存在代码块时，请对其如上述示例般进行缩进，以便你或其他编程者对代码进行阅读。需要进行缩进时请使用此按键 

接下来，就让我们运用 while 循环实现游戏内的日夜更替吧。
    
    
    minutesAfterMidnight = 0
    while true do
    	minutesAfterMidnight = minutesAfterMidnight + 1
    	game.Lighting:SetMinutesAfterMidnight(minutesAfterMidnight)
    	wait(.1)
    end
    

在这段代码中，我们通过变量 _minutesAfterMidnight_ 对游戏时间进行跟踪。每次进行循环，我们都会向 _minutesAfterMidnight_ 中储存的值添加 1，然后通过 _SetMinutesAfterMidnight_ 来更新游戏时间。更新后，我们会让脚本暂停十分之一秒，然后继续下一次循环。向游戏中加入此脚本并让其运行一段时间后，就可以观察到非常明显的日夜更替现象。

开发者可以通过改变循环中每次向 *minutesAfterMidnight* 值所添加的数目来更改昼夜交替的速度。添加的值越大，时间过得也就越快。反之亦然。 

## 向游戏添加路灯

接下来，我们将会向游戏中添加一盏夜晚开启白天关闭的路灯。首先，让我们创建路灯结构：

![Scripting4Lamp.png](https://developer.roblox.com/assets/blt2180282c6a283c91/Scripting4Lamp.png)



将希望发光的部件命名为 _LightPart_。此部件的材质应为 Neon（霓虹），以便其展现发光的视觉效果。同时，我们需要向此部件中插入 **PointLight**， 使其发出光能够照亮周围的部件。开发者可以随意设置 PointLight 的 Color（颜色）、Brightness（亮度）和 Range（距离）等属性，打造出自己想要的效果。

![Scripting4LampExplorer.png](https://developer.roblox.com/assets/blt464003f3751cda4f/Scripting4LampExplorer.png)



接下来，我们将对上一部分所演示的脚本进行更改，使路灯在早上 6 点关闭。同时我们也将会提升游戏内日夜更替的速度，以便开发者可以更为快速地对代码进行测试。
    
    
    lightPart = game.Workspace.LightPart
    minutesAfterMidnight = 0
    while true do
    	minutesAfterMidnight = minutesAfterMidnight + 10
    	game.Lighting:SetMinutesAfterMidnight(minutesAfterMidnight)
    
    	if game.Lighting:GetMinutesAfterMidnight() == 6 * 60 then
    		lightPart.Material = Enum.Material.Plastic
    		lightPart.PointLight.Enabled = false
    	end
    
    	wait(0.1)
    end
    

首先，让我们为 **LightPart** 创建一个变量。在此次的循环中，我们添加了名为 if 语句的组成部分。if 语句只会在满足特定条件后才会执行指定代码。在本示例中，我们需要查看时间是否为早上 6 点。需要在 Lua 语言中确认两个对象是否相等，则需要使用两个连着的等号（也就是 ==）。位于 **then** 和 **else** 之间的编码只有当 MinutesAfterMidnight（午夜过后的分钟数）为 6 * 60 （也就是 6 个小时）时才会运行。当此时运行代码时，我们将会发现作为路灯灯泡的部分将会变为塑料材质，而其中的 PointLight 也会随之停止发光。

若希望在白天结束时重新开启路灯，只需再增添一个 If 语句即可：
    
    
    lightPart = game.Workspace.LightPart
    minutesAfterMidnight = 0
    
    while true do
    	minutesAfterMidnight = minutesAfterMidnight + 10
    	game.Lighting:SetMinutesAfterMidnight(minutesAfterMidnight)
    	wait(0.1)
    	
    	if game.Lighting:GetMinutesAfterMidnight() == 6 * 60 then		-- 检查时间是否为早上 6 点
    		lightPart.Material = Enum.Material.Plastic
    		lightPart.PointLight.Enabled = false
    	end
    	if game.Lighting:GetMinutesAfterMidnight() == 18 * 60 then		-- 检查时间是否为晚上 6 点
    		lightPart.Material = Enum.Material.Neon
    		lightPart.PointLight.Enabled = true
    	end
    end
    

学习本教程后，开发者即可顺利地为游戏增添日夜更替，也可以构建自动开启关闭的路灯了！



***__Roblox官方链接__:[昼夜循环和路灯](https://developer.roblox.com/zh-cn/articles/Day-Night-Cycles-and-Street-Lights)