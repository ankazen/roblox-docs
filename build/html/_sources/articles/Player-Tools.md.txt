# 玩家工具 
Time:<em>15  分钟</em>

Tool（工具）是用于在 Roblox 中实现武器、魔杖和其他交互式对象的特殊实例。在本文中您将学到如何创建工具、如何让玩家能够装备工具，以及如何赋予工具能力和技能。

## 创建一个新的工具

工具是一个容器示例，就像 Model（模型）一样。要创建一个新的工具，请在 **Workspace**（工作区）中右键单击，选择 **Insert Object**（插入对象），然后选择 **Tool**（工具）。

![Tool_Image01.png](https://developer.roblox.com/assets/blt42c7cc38f5a4a41e/Tool_Image01.png)



再次提醒您，工具只是一个容器，所以如果它是空的，就不会显示在 3D 视图中。右键单击该工具并插入新的**部件**。该工具现在将显示在 3D 视图中。为了能被拾取，工具里需要有一个叫做 _Handle_（手柄）的部件。将工具中的部件重命名为 “Handle”。现在，如果您运行游戏，您的角色将能够拿起该工具。

![Tool_Image09.png](https://developer.roblox.com/assets/bltfc64f6e99bf1fd31/Tool_Image09.png)



## 自定义工具几何

一个工具可以包含任意多个部件。但请记住，只有一个部件能被命名为 Handle，因为该部件是工具将附加到角色的手的位置。这里有几个构建工具的小贴士：

  * 当您完成构建时，请确保所有部件都没有锚固。如果工具的任何部分被锚固，工具将无法移动，角色在拿起它时将被卡住。
  * 只命名一个部件为 _Handle_。如果有多个称为 Handle 的部件，工具将随意选择其中一个作为与手的连接点。
  * 在创建工具时，请不要使用 Surface（表面）接合，这一点非常重要。用表面接合构造的工具在装备时会散开。当您将具有兼容表面（例如 Smooth/Weld 或 Inlet/Stud）的两个部件合并在一起时，会创建表面接合。您应将连接行为更改为 **Always**（始终），并确保所有部件的表面是 **Smooth** 或 **SmoothNoOutlines**。

![Tool_Image07.png](https://developer.roblox.com/assets/blt99e2639bbb0079b7/Tool_Image07.png)

![Tool_Image06.png](https://developer.roblox.com/assets/blt13eae73cbbf73ab5/Tool_Image06.png)



由多个部件构建的工具示例：

![Tool_Image02.png](https://developer.roblox.com/assets/blte89e54e43c2656dd/Tool_Image02.png)



在上面的示例中，白色部分是 Handle，其他部件使用接合连接在一起。

## 无手柄工具

您可以制作没有手柄或任何几何体的工具。在这种情况下，该工具就成为玩家输入的接口，而没有 3D 视图中的任何视觉表示。要制作这样的工具，只需关闭该工具的 **RequiresHandle** 属性。例如一个魔法物品，当它被拥有时，会给玩家一个通过键盘输入激活的特殊能力。

![Tool_Image05.png](https://developer.roblox.com/assets/blta8237906d5679c00/Tool_Image05.png)



## 装备工具

工具可以通过多种方式装备。最简单的方法是将该工具放在工作区中，并在玩家与其发生碰撞时装备该工具。当这种情况发生时，该工具会自动添加到玩家的背包中。如果玩家当前没有任何装备，该工具将自动装备自己。请注意，这仅在工具的 **RequiresHandle** 属性设置为 true 时才有效。

![Tool_Image04.png](https://developer.roblox.com/assets/bltcf11873bbc170628/Tool_Image04.png)



您也可以使用 **StarterPack** 给玩家工具。每当玩家出生时，StarterPack 的所有内容都会被复制到玩家的背包中。如果您想确保所有玩家都使用相同的装备开始游戏，StarterPack 是实现此目的的最佳方式。

您还可以使用 Script（脚本）将工具提供给某个玩家，该脚本可以将该工具（或该工具的副本）放入玩家的背包中。
    
    
    local copy = game.Workspace.Tool:Clone()
    copy.Parent = game.Players.Player1.Backpack
    

您还可以通过将工具设置为玩家角色的子对象来强制玩家装备工具。
    
    
    local copy = game.Workspace.Tool:Clone()
    copy.Parent = game.Players.Player1.Character
    

使用脚本将工具给予角色时要小心！如果一个玩家已经装备了一个工具，而你强迫他们装备另一个，则两个工具可能会同时被装备，或许会导致意想不到的行为。

## 丢弃工具

默认情况下，玩家可以按 ← Backspace 键（在 OSX 上为 Delete）丢弃工具。 您可以将工具的 **CanBeDropped** 设为 false 来禁用此行为。

![Tools_Image00.png](https://developer.roblox.com/assets/bltfda1da60a66d248f/Tools_Image00.png)



## 动作栏外观

当一个工具在玩家的背包里时，同时会出现在玩家屏幕底部的动作栏中。您可以自定义此栏中工具的工具提示和图标。可以通过编辑工具的 **Tooltip** 属性来设置工具提示。

![Tool_Image08.png](https://developer.roblox.com/assets/blte3682b69958c834e/Tool_Image08.png)



您可以使用 **TextureId** 属性设置该工具的图标，可以像为贴花设置图像一样设置此属性的图像。

## 工具脚本基础知识

技术层面上，工具的目的是为玩家输入提供接口，因此有许多与它们相关的函数和事件可供开发人员与之交互。工具也是独一无二的，因为它们既可以运行常规脚本，也可以运行本地脚本。但是，由于它们与脚本的复杂关系，了解如何使用工具编写脚本的基础知识非常重要。

### Script 对 LocalScript

Script 和 LocalScript 都可以监听相同的事件并调用工具上的相同函数。那么什么时候该使用哪一种呢？以下是一些一般指导原则：

代码符合下列条件时，应该使用 **Script**：

  * 导致游戏世界发生变化（例如更改玩家健康状况、创建部件等)

代码符合下列条件时，应该使用 **LocalScript**：

  * 依赖玩家输入（如鼠标或触摸输入）
  * 需要只向拿着工具的玩家展示一些东西

### 事件

脚本可以监听四个工具特有的事件：

  * **Activated**：当玩家开始激活工具时（单击、触摸或按游戏手柄上的 A 键）。
  * **Deactivated**：玩家释放激活输入时。
  * **Equipped**：玩家从背包中选择工具。
  * **Unequipped**：玩家丢弃或切换工具时。

请记住，Script 和 LocalScript 都可以监听这些事件。下面是两个脚本连接到这些事件的代码：
    
    
    -- 此代码假定脚本直接位于工具内部。如果脚本位于其他位置，则必须更改下一个变量所指向的路径。
    local tool = script.Parent
    
    local function onEquip()  
    end
    
    local function onUnequip()
    end
    
    local function onActivate()
    end
    
    local function onDeactivate()
    end
    
    tool.Equipped:connect(onEquip)
    tool.Unequipped:connect(onUnequip)
    tool.Activated:connect(onActivate)
    tool.Deactivated:connect(onDeactivate)
    

## 创建魔杖工具

在本例中，我们将演示如何制作一个简单的工具，该工具在持有者单击鼠标时会创建部件。我们将同时使用 Script 和 LocalScript 来说明它们分别的职责。

### 获取鼠标输入

每当用户单击鼠标时，都会触发 **Activated** 事件，但它不包含有关鼠标的信息。我们希望工具在用户单击的地方创建一个部件，因此知道该单击发生在空间中的哪个位置对我们来说很重要。要获得鼠标位置，我们需要使用 LocalScript，因为常规 Script 在服务器上运行，而服务器不知道任何有关用户鼠标的信息。
    
    
    -- 本地 Script
    local tool = script.Parent
    local player = game.Players.LocalPlayer
    local mouse = player:GetMouse()
    
    local function onActivate()
      local clickLocation = mouse.Hit
    end
    
    tool.Activated:connect(onActivate)
    

我们先为工具、玩家和玩家的鼠标创建了变量，然后在 _onActivate_ 函数中，我们将单击的位置存储在了一个变量中。

### 创建部件

现在我们知道了玩家单击的位置，我们需要创建一个部件。哪个脚本应该处理此问题？在获得 LocalScript 中的位置后立即创建部件似乎是最简单的，然而这样做的问题是，LocalScript 仅在玩家的机器上运行，如果游戏中的 Experimental Mode（实验模式）处于关闭状态（这是默认设置），则由该 LocalScript 创建的任何部件都不会复制到服务器，则其他人不会看到您创建的部件！我们希望所有其他玩家都能够看到这些新的部件并与之交互，因此我们必须使用 Script 在服务器上创建该部件。
    
    
    -- 服务器端 Script
    local function createPart(location)
      local part = Instance.new("Part")
      part.CFrame = location
      part.Parent = workspace
    end
    

### 在 Script 和 LocalScript 之间通信

我们现在可以获取鼠标单击的位置，也可以在任意位置创建新部件，但是这些是用不同的脚本写的！我们需要让Script 和 LocalScript 之间能互相通信，以便其协同工作。为此，我们将使用前面创建的 RemoteEvent。

RemoteEvent 是可用于在 Script 和 LocalScript 之间发送信息的特殊对象。每个脚本都有一个事件侦听器，注册后就可以在事件触发时调用函数。我们也有一些函数可用于触发事件。

让我们从服务器 Script 上的侦听器开始。
    
    
    -- 服务器端 Script
    local tool = script.Parent
    local clickEvent = tool.ClickEvent
    local clickEventConnection
     
    local function createPart(location)
      local part = Instance.new("Part")
      part.CFrame = location
      part.Parent = workspace
    end
     
    local function onClick(player, clickLocation)
      createPart(clickLocation)
    end
     
    local function onEquip()
      clickEventConnection = clickEvent.OnServerEvent:connect(onClick)
    end
     
    local function onUnequip()
      clickEventConnection:disconnect()
    end
     
    tool.Equipped:connect(onEquip)
    tool.Unequipped:connect(onUnequip)
    

我们已经添加了相当多的内容，下面将进行逐步分解。首先，我们为工具和 RemoteEvent 声明了变量。我们还创建了变量 _clickEventConnection_，将使用它来存储事件连接。

然后，我们声明了函数 _onClick_，当侦听器听到事件触发时将调用该函数。该函数有两个参数，触发事件的玩家和玩家单击的位置（稍后将从 LocalScript 传入）。

在 _onEquip_ 函数中，我们将 _onClick_ 函数连接到 RemoteEvent 的 OnServerEvent 事件。这样，每当 RemoteEvent 触发时，它都会调用 _onclick_。最后，我们在 _onUnequip_ 函数中的 _clickEventConnection_ 上调用 disconnect，这样当玩家没有拿出工具时就不会触发该事件。

您可能已经注意到，我们将玩家传入了 *onClick* 函数，但我们从未实际使用过该变量。当您将函数绑定到 OnServerEvent 时，总是首先传入玩家参数，因此我们需要确保为它准备一个变量。

现在我们已经设置了 Script，我们只需要稍微修改一下 LocalScript，让它触发 RemoteEvent 即可。
    
    
    -- 本地 Script
    local tool = script.Parent
    local player = game.Players.LocalPlayer
    local mouse = player:GetMouse()
    local clickEvent = tool.ClickEvent
     
    local function onActivate()
      local clickLocation = mouse.Hit
      clickEvent:FireServer(clickLocation)
    end
     
    tool.Activated:connect(onActivate)
    

为了让 LocalScript 触发 RemoteEvent，我们调用 `FireServer`。此函数可以接受我们想要的任意数量的参数。在本例中，我们只想传递玩家单击的位置。

现在，当我们装备好工具时，就可以通过单击来创建部件了！

![Tool_Image10.png](https://developer.roblox.com/assets/blt7fa963a29b7e1a0d/Tool_Image10.png)





***__Roblox官方链接__:[玩家工具](https://developer.roblox.com/zh-cn/articles/Player-Tools)