# 防抖动：使用时机及原因说明 
Time:<em>5  分钟</em>

简而言之，**Debounce（防抖动）**系统就是一个用来防止函数运行次数过多的代码集合。这个概念来自于电子元件开关的接点弹跳现象，也就是开关开启时接点在多次弹跳后才能稳定下来，导致多个信号产生。该问题在 Roblox 中主要体现于 `BasePart/Touched` 事件：在两个部件短时间内多次触碰时会产生类似问题。不过，防抖动系统在其他情况下也能够派上用场。

### 理论应用

假设地板上有一个按钮。每当玩家角色跳到按钮上时，按钮就会输出一条讯息。为此情况编写的代码可能会是这样的：
    
    
    game.Workspace.Button.Touched:Connect(function(hit)
        print("按钮被按下") --打印讯息
        wait(1)                 --等待 1 秒
        print("Hi :D")          --打印另一条讯息
    end)
    

上述代码将会在输出窗口中产生下列讯息：
    
    
    按钮被按下
    Hi :D
    

但物理引擎处理碰撞的方式使其不会只记录一次碰撞，而是可能触发多次 Touched 事件。因此，刚才代码的实际输出效果可能更接近下面所示：
    
    
    按钮被按下
    按钮被按下
    按钮被按下
    按钮被按下
    按钮被按下
    Hi :D
    Hi :D
    Hi :D
    Hi :D
    Hi :D
    

所有的事件处理函数会同时执行，而非按顺序单个执行。

下面是开发者可能会遇到的情况：

当希望使用按钮进行 `Articles/How to Make a Model Regenerate`（模型再次生成）时，很可能会导致每按一次按钮都会生成 5 个模型。由于这 5 个模型都会处于_相同位置_，可能会导致多种问题发生。在代码中加入简单的防抖动系统后，就可以轻易避免这些问题。当然，在上述情况中也可以为按钮添加 `ClickDetector` 来解决重复问题。但在许多无法使用 ClickDetector 的情况下，防抖动系统将会十分有用。

基本的防抖动系统工作原理如下：

当特定动作发生时（例如当玩家跳上之前所提到的地板按钮上时），脚本会**封锁**所有对函数的再次调用，直到指定时长后或者动作完成后为止。

### 使用示例

为已有脚本添加防抖动功能其实并不困难。下面就让我们以之前的脚本为例：只需添加几行代码，就能够为这个脚本添加函数能够再次运行前需要等待的时长限制。
    
    
    local buttonPressed = false
    --将按钮是否被按下的状态储存在局部变量中
    
    Workspace.Button.Touched:Connect(function(hit)
        if not buttonPressed then
        -- 状态是否为“未按下”？
    
            buttonPressed = true
            -- 若是，则将其标记为“已按下”，防止函数多次运行
    
            print("按钮被按下")
            wait(1)
            print("Hi :D")
            -- 执行操作
    
            buttonPressed = false
            -- 执行操作后将其标记为“未按下”，以便再次执行函数
        end
    end)
    

进行调整后，输出应该是这样的：
    
    
    按钮被按下
    Hi :D
    

这样就达到我们最开始的目的了！这四行代码可以被添加至大多数带有函数的脚本中，以达成同样的效果。其也适用于非互相触碰对象的使用情况，如：用来阻止玩家过于频繁地按下按钮或发射武器，或者用来阻止新事件在当前事件完成前触发等。请参考下列示例：

### 实际应用

下列代码为火箭发射器工具的本地 GUI 脚本：
    
    
    enabled = true
    mouse.Button1Down:Connect(function()
        if not enabled then
            return
        end
    
        enabled = false
        mouse.Icon = "rbxasset://textures\\GunWaitCursor.png"
    
        wait(12)
        mouse.Icon = "rbxasset://textures\\GunCursor.png"
        enabled = true
    
    end)
    

发射火箭发射器后，脚本会显示装填图标，并让函数等待 12 秒。在此期间 enabled 值将为 false，因此当玩家尝试再次使用发射器时，函数会立即返回，导致脚本不会运行。装填图标将会在 12 秒后消失，且 enabled 值将重新设为 true，以便玩家再次使用火箭发射器。

### 进阶符号用法

在熟悉防抖动的使用方法后，开发者不需要为每个事件处理程序定义不同的防抖动变量，可转为编写防抖动函数，用来返回事件处理函数的防抖动拷贝。该函数将会使用 `...` 符号来[传递参数](https://developer.roblox.com/en-us/articles/Variadic-Functions#argument-forwarding)。
    
    
    function debounce(func)
        local isRunning = false    -- 创建局部防抖动变量
        return function(...)       -- 返回新函数
            if not isRunning then
                isRunning = true
    
                func(...)          -- 用原始参数进行调用
    
                isRunning = false
            end
        end
    end
    

将其应用至原始代码：
    
    
    Workspace.Button.Touched:Connect(debounce(function(hit)
        print("按钮被按下") --打印讯息
        wait(1)                 --等候 1 秒
        print("Hi :D")          --打印另一条讯息
    end))
    

#### 练习实践

制作一个被玩家触碰时使玩家生命值减少 5 的部件。通过防抖动功能确保此效果每 3 秒只能触发一次。 

显示/隐藏
    
    
    --将按钮是否被按下的状态储存在局部变量中
    local buttonPressed = false
    script.Parent.Touched:connect(function(hit)
        -- 状态是否为“未按下”？
        if not buttonPressed then
            -- 若是，则将其标记为“已按下”，防止函数多次运行
            buttonPressed = true
            if hit.Parent then
                hum = hit.Parent:FindFirstChild("Humanoid")
                hum.Health = hum.Health - 5
            end
            wait(3)
            -- 执行操作后将其标记为“未按下”，以便再次执行函数
            buttonPressed = false
        end
    end)
    



***__Roblox官方链接__:[防抖动：使用时机及原因说明](https://developer.roblox.com/zh-cn/articles/Debounce)