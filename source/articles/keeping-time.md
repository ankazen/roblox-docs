# 游戏计时 
Time:<em>10  分钟</em>

几乎所有游戏都需要以某种方式计时。在 Roblox 中，脚本有多种计时以及等待的方法，又名 **yielding（暂停）**。

使用 wait 的简单暂停 ```    
    
    print("我们来玩等待游戏吧。")
    wait(5)
    print("你赢了！")


```
## 简单暂停

最简单的暂停可以使用 `wait` 函数实现，这将暂停指定的秒数。它的用法非常直截了当：

当 `wait` 被调用时，Roblox 的内部计划程序会让线程暂停尽可能地接近给定时间，然后发出信号让线程再次恢复。

### 与 Unity 的 StartCoroutine/IEnumerator 对比

下面的示例取自 [Unity 脚本编写 API：WaitForSeconds](https://docs.unity3d.com/ScriptReference/WaitForSeconds.html).
    
    
    using UnityEngine;
    using System.Collections;
    
    public class WaitForSecondsExample : MonoBehaviour
    {
        void Start()
        {
            StartCoroutine(Example());
        }
    
        IEnumerator Example()
        {
            print(Time.time);
            yield return new WaitForSeconds(5);
            print(Time.time);
        }
    }
    

在 Roblox 中，与之作用类似的代码如下：

Roblox Lua Comparison 与 Unity 的 WaitForSeconds 的比较 ```    
    
    local function Start()
    	-- 这里 `spawn` 的作用与 MonoBehaviour 的 `StartCoroutine` 类似。
    	-- 注意：我们以函数名称对其进行引用而不是调用！
    	spawn(Example)
    end
    
    local function Example()
    	print(time())
    	wait(5)
    	print(time())
    end
    
    Start()
    
    
    0
    5

```
## 用函数暂停

有时定义一个函数并在给定的秒数后运行更加容易。‘delay’ 函数在这方面是完美的选择：以秒为单位指定等待时间，并在指定时间过后运行一个函数：

延迟示例 ```    
    
    local function explode()
    	print("轰隆！")
    end
    delay(5, explode)
    
    
    Kaboom!

```
### 与 Unity 中 MonoBehavior 的 Invoke 对比

下面是一段 Unity C# 脚本示例，它将在两秒后运行 `Explode` 方法。这是为了展示 Unity 中 MonoBehavior 的 [Invoke]（[https://docs.unity3d.com/ScriptReference/MonoBehaviour.Invoke.html）与](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Invoke.html%EF%BC%89%E4%B8%8E) Roblox 中的 `delay` 函数的相似性。
    
    
    using UnityEngine;
    
    public class ExampleScript : MonoBehaviour
    {
        void Start()
        {
            Invoke("Explode", 2);
        }
    
        void Explode()
        {
        	print("轰隆！");
        }
    }
    

上面的示例类似 Roblox 中的以下代码：

Roblox Lua Comparison 与 Unity C# 中 MonoBehavior 的 Invoke 的比较# ```    
    
    local function Start()
    	-- 注意：这里我们将 Explode 函数作为参考而不是字符串传递。
    	delay(2, Explode)
    end
    
    local function Explode()
    	print("轰隆！")
    end
    
    Start()
    
    
    Kaboom!

```
`Invoke` 和 `delay` 都不会暂停当前线程。换句话说，脚本将在计划函数调用后立即继续运行。

## 每帧计时

更常见情况的是，脚本会有必须尽可能频繁地运行的逻辑。`RunService/Stepped` 事件会在游戏运行时的每帧触发，差不多每秒 60 帧。在 Studio 中，这是在点击 “Run（运行）”或 “Play Solo（单人游戏）”之后开始。该事件以当前游戏时间触发，然后是自上一帧以来的时间（增量时间）。

RunService Stepped 示例 ```    
    
    local RunService = game:GetService("RunService")
    
    local function onStepped(t, dt)
    	-- 此函数每帧运行。
    	-- t: 游戏运行的时间，以秒为单位
    	-- dt: 自上次 Stepped 触发后经过的时间，以秒为单位
    	print("自上一帧之后的秒数： " .. dt)
    end
    RunService.Stepped:Connect(onStepped)
    
    
    Seconds since last frame: 0.015212

```
有时已经无需再每帧运行这样的函数。为此，可以保存一个由 `Connect` 返回的 Connection 对象的引用，之后再调用 `Disconnect`。下面的示例是“简单的暂停”示例中基于事件的实现。

用 RunService Stepped 等待 ```    
    
    local RunService = game:GetService("RunService")
    
    local connection
    local countedTime = 0
    local goalTime = 5
    
    local function onStepped(t, dt)
    	countedTime = countedTime + dt
    	if countedTime >= goalTime then
    		print("You win!")
    		-- 我们不再需要计时，因此这里断开连接：
    		connection:Disconnect()
    		-- 如果我们要数 `goalTime` 的每一秒，可以从 `countedTime` 删减而不是断开连接：
    		countedTime = countedTime - goalTime
    	end
    end
    print("我们来玩等待游戏吧。")
    connection = RunService.Stepped:Connect(onStepped)
    
    
    Let's play the waiting game.
    You win!

```
基于事件的方法有利于保持代码简洁。有关事件的更多信息，请参见关于[事件](/articles/events)的文章。

### 与 Unity C# 中 MonoBehavior 的 Update 对比

在 Roblox 中连接至 `RunService/Stepped` 与在 Unity 中的 [MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html) 定义 `Update` 函数非常相似。
    
    
    using UnityEngine;
    using System.Collections;
    
    public class ExampleClass : MonoBehaviour
    {
    	void Update()
    	{
    		print(Time.time);
    	}
    }
    

上面的示例类似于 Roblox 中的以下代码：
    
    
    local RunService = game:GetService("RunService")
    
    local function Update(t, dt)
    	print(time())
    end
    
    RunService.Stepped:Connect(Update)
    

## 渲染函数步骤

有时 `LocalScript` 需要负责处理视觉效果。例如，让箭头指向某个对象。这种视觉效果应该在屏幕渲染之前更新。在 Roblox 中，您可以使用 `RunService/BindToRenderStep` 函数来实现：

RunService BindToRenderStep 示例 ```    
    
    local RunService = game:GetService("RunService")
    local function runEveryRenderStep()
    	-- 此函数在屏幕显示时允许
    end
    RunService:BindToRenderStep("renderStepDemo", 1, runEveryRenderStep)
    -- 之后您可能需要解绑此函数。为此，请使用：
    RunService:UnbindFromRenderStep("renderStepDemo")


```


***__Roblox官方链接__:[游戏计时](https://developer.roblox.com/zh-cn/articles/keeping-time)