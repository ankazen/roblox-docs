# 通过事件让部件着火 
Time:<em>10  分钟</em>

在本教程中，我们将会学习如何通过事件和函数在游戏中创建可以点燃及熄火部件的区域。

![Scripting5_Final.png](https://developer.roblox.com/assets/blt666b8215be36d9f7/Scripting5_Final.png)



## 初始设置

让我们从向游戏中放入两个部件开始。第一个部件将被用来点燃所有与其触碰的部件；第二个部件将被用来熄灭已经点燃的火焰。请确保两个部件在 Explorer（管理器）中的名称分别为 _FirePart_（点燃用部件）和 _WaterPart_（熄灭用部件）。

![Scripting5_Parts.png](https://developer.roblox.com/assets/bltc8e1fb5a1c07f64b/Scripting5_Parts.png)



接下来，我们需要在 `ServerScriptService` 中创建一个 `Script`（脚本）。右键单击 **ServerScriptService**，将鼠标悬停在 Insert Object（插入对象）上方，然后选择 **Script（脚本）**。

## 点燃火焰

我们现在应该已经对函数的使用有了一定的经验：_print_ 和 _wait_ 函数可以在任何 Roblox 脚本中运行，而 _SetMinutesAfterMidnight_ 是 Lighting 服务的成员函数。虽然上述函数都是由 Roblox 事先定义好的，但开发者也可以根据需要在脚本中创建各种自定义函数。

首先，我们需要创建一个能够点燃部件的函数。就从下面的几行代码开始吧：

部件上玩家的触碰检测 - 点燃部件：代码示例 1 ```    
    
    function lightOnFire()
    	print("着火了！")
    end


```
创建函数时，我们需要确保包括几个重要的组成部分：第一行代码的开头必须使用关键字 **function**。紧跟其后的单词将会成为函数的名称。为函数命名的规则与为变量命名的规则相同（无空格、不得以数字开头等）。在函数名称的后面需要添加括号 ()。在下面一行中，我们将会添加当函数被调用时运行的代码。在上述示例中，调用 lightOnFire 函数后，代码 print(“着火了！”) 将会运行。当添加所有需要运行的代码后，使用关键字 **end** 来结束函数的编写。

目前我们的函数还远远没有完成，但让我们先对其进行调用，稍微测试一下吧。如果现在对游戏进行 **Run**（运行），你会发现什么都不会发生。我们之前所编写的 print 语句并不会显示在 Output（输出）中。这是因为虽然我们对函数调用后的操作进行了编写，但并没有对函数进行调用。自定义函数的调用方式与其他普通函数相同：使用函数名称，后跟括号。请参照下列示例：

部件上玩家的触碰检测 - 点燃部件：代码示例 2 ```    
    
    function lightOnFire()
    	print("着火了！")
    end
    
    lightOnFire()
    
    
    "Lighting on fire!"

```
如果我们现在运行游戏，*着火了！*将显示在 Output（输出）中。

当创建自定义函数时，请务必确保在使用函数前对其先进行定义。在上述示例中，我们先对函数进行了定义，然后才对其进行调用。如果反而行之，则函数将不会正确运行：

部件上玩家的触碰检测 - 点燃部件：代码示例 3 ```    
    
    lightOnFire()
    
    function lightOnFire()
    	print("着火了！")
    end


```
上述代码示例将不会正常运行。我们在代码的第一行就调用了 _lightOnFire()_，但由于没有事先定义函数的内容，将会导致 Script（脚本）出错。

让我们继续编写函数吧。现在的函数只能打印至输出窗口，这离我们“点燃一切”的需求还差得很远！我们希望能够通过这个函数将特定部件点燃，那么接下来就需要确保函数知道需要点燃的是哪个部件。让我们通过向函数添加 _Parameter_（参数）来完成这一步骤吧。在函数定义中的括号内添加关键字 part，如下所示：

部件上玩家的触碰检测 - 点燃部件：代码示例 4 ```    
    
    function lightOnFire(part)
    	print("将要点燃这个部件：")
    	print(part.Name)
    end


```
上述代码中的关键字 _part_ 是函数的参数。之前我们曾经在其他函数中使用过一些参数：使用 _wait_ 函数时，需要提供一个数字作为参数；使用 _print_ 函数时，需要提供一个字符串或数字作为参数。在这个代码示例中，我们需要提供的是希望点燃的 Part（部件）。在函数内部，我们将可以像普通变量一样使用 part。

接下来，让我们添加点燃后出现的火焰。添加火焰最为简单的方式就是在代码中创建新的 **Fire** 实例，并将其父项设置为传递进来的部件。创建火焰实例的方法与创建新部件的方法一致：只需将 **Instance.new(“Part”)** 修改为 _Instance.new(“Fire”)_ 即可。同时，我们需要确保将火焰保存在变量中，以便设置其 Parent（父项）属性。

部件上玩家的触碰检测 - 点燃部件：代码示例 5 ```    
    
    function lightOnFire(part)
    	print("将要点燃这个部件：")
    	print(part.Name)
    	
    	fire = Instance.new("Fire")
    	fire.Parent = part
    end


```
最后，我们需要确保每当部件触碰我们在教程开头创建的 _FirePart_ 时，都会调用此函数。让我们通过使用 **Event**（事件）来达成这个目标。事件用于在游戏中出现指定状况时对函数进行调用。事件可以包括以下状况：部件碰撞、玩家加入游戏、玩家按下按钮等。当事件发生时，我们可以在多处调用自定义函数。本示例中使用的事件为 **Touched**，与部件相关联：

部件上玩家的触碰检测 - 点燃部件：代码示例 6 ```    
    
    function lightOnFire(part)
    	print("将要点燃这个部件：")
    	print(part.Name)
    	
    	fire = Instance.new("Fire")
    	fire.Parent = part
    end
    
    firePart = game.Workspace.FirePart
    firePart.Touched:Connect(lightOnFire)


```
接下来，让我们进行游戏测试！点击 **Play（开始游戏）**后，将会生成游戏角色。控制角色走向 _FirePart_。当角色触碰到该部件时，其双腿将会燃烧起来！

![Scripting5_Final.png](https://developer.roblox.com/assets/blt666b8215be36d9f7/Scripting5_Final.png)



## 熄灭火焰

让我们为玩家们提供一个熄灭火焰的方法：触碰 _WaterPart_。如点燃火焰时相同，我们将需要创建一个能够熄灭火焰的函数，并将其连接至 **WaterPart** 的 Touched 事件。

部件上玩家的触碰检测 - 点燃部件：代码示例 7 ```    
    
    function putOutFire(part)
    	print("要灭掉这个部件上的火：")
    	print(part.Name)
    end
    
    waterPart = game.Workspace.WaterPart
    waterPart.Touched:Connect(putOutFire)


```
为了熄灭火焰，我们将会使用名为 _Destroy_ 的函数。对 Roblox 中的任何对象使用此函数后，都将导致该对象被移除。或许你会想要像下面这样编写熄灭火焰的代码：

部件上玩家的触碰检测 - 点燃部件：代码示例 8 ```    
    
    function putOutFire(part)
    	print("要灭掉这个部件上的火：")
    	print(part.Name)
    	
    	part.Fire:Destroy()
    end
    
    waterPart = game.Workspace.WaterPart
    waterPart.Touched:Connect(putOutFire)


```
虽然上面的代码可用于扑灭火焰，但当角色没有着火并触碰 WaterPart 时，又会发生什么情况呢？

![Scripting5_Error.png](https://developer.roblox.com/assets/blt1276cf0f0275fc18/Scripting5_Error.png)



没错，在这种情况下，之前的代码将会导致错误。在为游戏进行代码编写时，最理想的状况是不出现任何错误。为了修正这个情况，我们首先需要检查试图进行灭火的部件中是否存在火焰实例。该操作可以通过名为 _FindFirstChild_ 的函数轻松完成：该函数可以查看指定名称的部件是否存在于其他对象中。函数的结果甚至可以被储存在变量中。让我们立即执行这一操作吧：

部件上玩家的触碰检测 - 点燃部件：代码示例 9 ```    
    
    function putOutFire(part)
    	print("将要灭掉这个部件上的火：")
    	print(part.Name)
    	
    	fire = part:FindFirstChild("Fire")
    	if fire then
    		fire:Destroy()
    	end
    end
    
    waterPart = game.Workspace.WaterPart
    waterPart.Touched:Connect(putOutFire)


```
在刚刚创建的函数中，我们会在打印输出语句后创建名为 **fire** 的变量，并在该变量中存储 _FindFirstChild(“Fire”)_ 的结果。下一行 **if fire then** 是条件性检查，用于查看 fire 中是否已存储任何内容。如果 FindFirstChild 成功存储 fire 变量中的内容，则将调用下一行 _fire:Destroy()_。否则，在未找到任何内容时，函数将不会执行任何操作。如此一来，在调用函数时就不会产生任何错误。

下面，让我们使用 **Play（开始游戏）**对游戏进行测试。在游戏中，我们将可以通过触碰 FirePart 点燃角色，然后触碰 WaterPart 来熄灭火焰。

## 后续步骤

让我们将这段新的代码与地形结合使用吧！使用地形后，玩家踩到火山熔岩时将会着火，而跳入水中后就可以熄灭身上的火焰。这种体验将会比普通的砖块要有趣逼真得多。首先，我们将会使用 **Add（添加）**地形工具来添加地形：

![Scripting5_Terrain.png](https://developer.roblox.com/assets/blt9052bdb90d586afe/Scripting5_Terrain.png)



移动并缩放之前创建的火部件和水部件，使其与刚刚添加的地形完全重叠。确保这两个部件都处于 *Anchored（锚固）*状态，且其 _`BasePart/CanCollide`_ 属性处于关闭状态。另外，你还可以将其 _Transparency_ 属性将其设为半透明，以便更为精确地为部件定位。

![Scripting5_TerrainAndParts.png](https://developer.roblox.com/assets/blt71975783c3b1e88e/Scripting5_TerrainAndParts.png)



在脚本末尾，我们会将这两个部件设为完全透明，使其不显示在游戏成品中：
    
    
    firePart.Transparency = 1
    waterPart.Transparency = 1
    

这样一来，代码就完成了！在开始游戏时，玩家可以跳到熔岩上点燃自己，也可以跳到水中将火灭掉！

![Scripting5_TerrainFinished.png](https://developer.roblox.com/assets/bltf9123e3441e2ad23/Scripting5_TerrainFinished.png)



下面是我们刚刚编写的所有代码：

部件上玩家的触碰检测 - 点燃部件：代码示例 10 ```    
    
    function lightOnFire(part)
    	print("将要点燃这个部件：")
    	print(part.Name)
    	
    	fire = Instance.new("Fire")
    	fire.Parent = part
    end
    
    firePart = game.Workspace.FirePart
    
    firePart.Touched:Connect(lightOnFire)
    
    function putOutFire(part)
    	print("将要灭掉这个部件上的火：")
    	print(part.Name)
    	
    	fire = part:FindFirstChild("Fire")
    	if fire then
    		fire:Destroy()
    	end
    end
    
    waterPart = game.Workspace.WaterPart
    waterPart.Touched:Connect(putOutFire)
    
    firePart.Transparency = 1
    waterPart.Transparency = 1


```


***__Roblox官方链接__:[通过事件让部件着火](https://developer.roblox.com/zh-cn/articles/Setting-Parts-on-Fire-with-Events)