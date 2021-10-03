# 减少延迟影响 
Time:<em>15  分钟</em>

网络游戏（例如 Roblox 上的游戏）都有令人沮丧的，不可避免的延迟问题。幸运的是，你可以使用两种策略来克服这种延迟，并将其优雅地集成到游戏的功能中。

## 延迟的根源

在学习一些隐藏延迟的策略之前，重要的是要有一个准确的心理模型来解释为什么延迟必须存在于远程调用的游戏中。

假设你是我们在英国的用户之一。在这个游戏中，一个本地脚本允许你按“F”键发射大炮。开发人员认为炮弹对于客户端处理来说太重要了。因此，本地脚本对服务器进行远程调用，以便服务器可以是触发的服务器。当客户端检测到“F”键被按下时，它会联系服务器，服务器会发射加农炮，并且服务器会让客户端知道结果。但是，由于你的计算机在英国，而且 Roblox 服务器在美国，因此这需要在整个大西洋上传送信号。需要发送两次信号。这需要时间，而这一次是在按下“F”键和实际看到炮火之间的恼人延迟。

## “Laggy Cannons”

为了使最后一个示例的假设少一些，本教程随附了一个简单的 Roblox 游戏，名为“Laggy Cannons”。[你可以在此处在线玩这个游戏](http://www.Roblox.com/Laggy-Cannons-place?id=174999362)，也可以根据需要自行下载 Studio 版本。

在 Laggy Cannons 中，有四门大炮对准四个移动目标。每个大炮目标对都受到相同的人为夸大的延迟时间的影响，但是每个大炮目标对都以稍微不同的方式解决了这一延迟。有些大炮目标对比其他大炮目标对更好地处理这种延迟。紫色大炮目标对比红色大炮目标对好，红色大炮目标对比橙色大炮目标对好，橙色大炮目标对比蓝色大炮目标对好。

![在此处输入图像描述](https://developer.roblox.com/assets/blt0e00ededf5cf89cc/LaggyCannons_Gameplay.png)



在阅读本教程的其余部分之前，现在是一个很好的时间去玩 Laggy Cannons 游戏，看看你是否能感觉到这四种大炮之间的差异。若要玩 Laggy Cannons 游戏，请使用重生点附近的四个传送器传送到具有相应颜色的炮台。当你站在炮台上时，你可以按“F”来发射炮弹并尝试击中该大炮的移动目标。踏上炮台的彩色区域，返回传送炮台并尝试另一门大炮。你可以通过单击重生点附近控制板上的“+”和“-”按钮来操纵人为延迟的秒数。

本教程的其余部分深入介绍了每种颜色的大炮或目标的行为方式以及原因。我们还将概括每对使用的策略，以便你可以更轻松地将它们应用于你的游戏。

### 蓝色大炮

![在此处输入图像描述](https://developer.roblox.com/assets/bltc662b5ee274f61ac/LaggyCannons_BlueCannon.png)



让我们从无法真正尝试的大炮开始：蓝色大炮。如果你按“F”键，你会立即看到和听到大炮开火的爆炸声，但你会很长一段时间看不到炮弹。以下是当你发射蓝色大炮时在本地脚本中调用的函数：
    
    
    --在本地脚本中
    local function badCannonStrategy()
        Workspace.FireCannonEvent:FireServer(activeCannon)
        createExplosion(activeCannon)
    end
    

此函数的第一行使用名为“FireCannonEvent”的一个 RemoteEvent 来请求服务器触发名为“activeCannon”的全局变量。当然，此处的 activeCannon 是蓝色大炮。FireCannonEvent 是对服务器的单向请求。在向服务器发送一条要求它发射蓝色大炮的消息后，这个本地脚本立即继续使用未显示的辅助函数“createExplosion”在屏幕上显示爆炸。

此处没有做任何工作来处理 RemoteEvent 固有的延迟。消息已发送，爆炸已制造，然后我们等待服务器发射炮弹。

## 第 1 课：小心使用你的代码

`badCannonStrategy()` 函数看起来很无辜。它发射大炮并制造爆炸，这不就是我们想要的吗？问题是它完全忽略了延迟，这很容易做到。如果你想制作出色的游戏，你必须注意到这里会有延迟。请继续读下去，了解你能对延迟做些什么。

### 橙色大炮

![在此处输入图像描述](https://developer.roblox.com/assets/blt1002ad22c65de0dd/LaggyCannons_OrangeCannon.png)



橙色大炮稍微修改了蓝色大炮的策略，以便使炮弹的发射与爆炸同步。触发橙色大炮的函数如下：
    
    
    --在本地脚本中
    local function okCannonStrategy()
        local waitForResponse = Workspace.FireCannonFunction:InvokeServer(activeCannon)
        createExplosion(activeCannon)
    end
    

你可以看到这里唯一的变化是函数的第一行。橙色大炮没有使用 RemoteEvent 来发射炮弹，而是使用一个名为“FireCannonFunction”的 RemoteFunction。你可能还记得`Articles/Remote Functions and Events|关于远程调用的教程`中讲述的内容，RemoteFunction 与 RemoteEvent 的不同之处在于它有一个返回值。RemoteEvent 只是从客户端向服务器发送的信号，而 RemoteFunction 不仅是从客户端向服务器发送的信号，而且还是从服务器向客户端返回的值。此外，由于客户端期望返回值，因此它实际上会等待该返回值出现，然后再在其本地脚本中继续。这正是橙色大炮脚本所利用的功能。这个稍微好一点的大炮发射函数等待服务器告知该大炮已经发射了一个炮弹，然后再继续创建伴随的爆炸。

## 第 2 课：同步体验

蓝色大炮没有意义，因为你在看到炮弹之前就已经看到了大炮爆炸。在现实世界中，爆炸和炮弹射击同时发生。为了让游戏充满乐趣和沉浸感，它不应该违背玩家对这类愚蠢事情的期望。遵循橙色大炮的示例，并使用 RemoteFunction 在客户端和服务器之间同步事件。

### 红色大炮

![在此处输入图像描述](https://developer.roblox.com/assets/bltbfe5032abc4c46ec/LaggyCannons_RedCannon.png)



虽然橙色大炮解决了炮弹和爆炸不同步的问题，但它实际上暴露了另一个延迟问题。当玩家按下“F”键开火时，在游戏完全响应之前会有明显的延迟。这被称为输入延迟，这是玩家最讨厌的事情之一。

有一个简单的技巧可以用来消除输入延迟。你无法加快大炮发射的时间。无论如何，这都将花费一条消息从客户端到服务器再到客户端的往返时间。但是，你可以给玩家一些其他即时反馈，使他们觉得游戏正在响应他们的命令。

红色大炮选择给的立即反馈是声音。当玩家按下“F”键时，红色大炮立即开始播放大炮引信燃烧的声音。此声音会一直播放到服务器响应 RemoteFunction。一旦服务器响应，红色大炮将关闭燃烧的引信声音，并伴随着服务器刚刚发射的炮弹产生爆炸。
    
    
    --在本地脚本中
    local function bestCannonStrategy()
        Workspace.Sounds.BurningFuse:Play() 
        local waitForResponse = Workspace.FireCannonFunction:InvokeServer(activeCannon)
        Workspace.Sounds.BurningFuse:Stop()
        createExplosion(activeCannon)
    end
    

如果使用红色大炮，应该感觉很自然。在按下“F”键和看到炮弹开火之间仍有一段延迟，但这是不可察觉的，因为大炮将这种延迟融入其工作方式中。

## 第 3 课：没有输入延迟！

玩家讨厌输入延迟。感到自己和游戏脱节是令人沮丧的。尽管可能需要对玩家输入做出延迟的响应，但你始终可以给玩家一些小的响应，以表明他们的请求已被听到。这可以是声音、变化的砖块颜色，甚至可以是任何东西。让玩家知道他们的请求已被听到，你的玩家会非常开心。

### 紫色目标

![在此处输入图像描述](https://developer.roblox.com/assets/blt506901afa31c58e8/LaggyCannons_PurpleTarget.png)



紫色大炮的工作方式和红色大炮完全一样。紫色平台和所有其他颜色的平台的区别在于移动目标的功能。

当你击中蓝色、橙色或红色目标时，你会注意到在看到目标被击中与产生的“叮”声和分数更新之间存在延迟。例如，蓝色目标的“叮”声和分数更新由以下服务器函数执行：
    
    
    --服务器端脚本
    Workspace.Blue.Target.Face.Touched:connect(function(projectile)
        wait(_G.artificialLag)    -- Laggy Cannons 游戏创造人为延迟的方法
        --播放目标命中声效
        Workspace.Sounds.TargetHit:Play()
        --更新蓝色分数
        blueScore = blueScore + 1
        Workspace.Blue.Scoreboard.SurfaceGui.ScoreLabel.Text = blueScore
    end)
    

我们知道像玩家得分这样重要的事情必须由服务器来处理。因此，更新目标分数时必须有延迟。但是击中目标的声音呢？

虽然最终由服务器决定目标是否被击中，但客户端完全能够立即播放目标击中的声音本身。最坏的情况是，如果客户端和服务器在目标是否被击中的问题上有一个罕见的分歧，玩家将体验到“叮”声和分数更新之间的差异。发生这种情况的概率是五千分之一，这是一个很值得给予玩家即时反馈的成本。因此，我们实际上可以将以前的服务器脚本拆分为服务器脚本和本地脚本：
    
    
    --服务器端脚本
    Workspace.Purple.Target.Face.Touched:connect(function(projectile)
        wait(_G.artificialLag)    -–（Laggy Cannons 游戏创造人为延迟的方法）
        --更新紫色分数
        purpleScore = purpleScore + 1
        Workspace.Purple.Scoreboard.SurfaceGui.ScoreLabel.Text = purpleScore
    end)
    
    --本地脚本
    Workspace.Purple.Target.Face.Touched:connect(function(projectile)
        --播放目标命中声效
        Workspace.Sounds.TargetHit:Play()
    end)
    

## 第 4 课：拆分脚本

有时你必须在服务器上做一半的工作，在客户机上做一半的工作。不要害怕两次检测同一事件。本地检测给玩家提供反馈，服务器检测处理重要的游戏逻辑。

## 现实世界中的延迟

Laggy Cannons 的默认人为延迟为一秒。这是你玩 Roblox 游戏时机器自然遇到的任何延迟的基础。在我们的玩家群中，我们可以看到延迟 0.1 到 1.5 秒不等的玩家。平均延迟似乎徘徊在 0.3 秒左右。幸运的是，你现在已具备处理此延迟的工具。

## 在 Studio 中测试延迟

如果要在 Roblox Studio 中模拟延迟，则可以转到“File（文件）”->“Settings（设置）” ->“Network（网络）” -> IncomingReplicationLag 并调整 Studio 在运行测试服务器时模拟的延迟秒数。



***__Roblox官方链接__:[减少延迟影响](https://developer.roblox.com/zh-cn/articles/Fighting-Against-Lag)