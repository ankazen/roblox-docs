# 闪烁的动态光源 
Time:<em>5  分钟</em>

开发者可以通过动态照明打造更具有真实感的游戏世界。但需要注意的是，现实生活中的光源并不是纹丝不动的。无论是野营时的篝火或是明暗交替的灯光，我们身边的各种光源都是持续移动着的。在本教程中，我们将会学习一种让灯光变亮或变暗的简单方法，并通过其构建更为真实的光源效果。

## 创建光源

在学习关于光源的设置方法时，首要任务自然是构建动态照明对象。本教程将会使用 `PointLight` 对象，但其与 `SpotLight` 的工作方式完全相同。同时，我们还需要一个脚本来控制发光效果。

**营火示例：**

![ExampleCampFire](https://developer.roblox.com/assets/blt8a04b6034780c8ea/campFireExplorer.jpg)

## 编写代码

本示例中的一大部分内容都涉及到了`Articles/Roblox Coding Basics Loops|循环`。对循环（特别是`Articles/For 循环`）尚未掌握的开发者应当对这部分内容进行理解与回顾，然后再学习本教程中的内容。

让我们开始编写代码！首先，我们需要创造带有一长串参数的一个函数。可不要认为这些参数过于冗长：这里的每一个参数对于整个函数（特别是主循环）的正常运转都是不可或缺的。下面就让我们来详细了解一下代码的形态与各参数的作用吧！
    
    
    function AdjustLights(Start, End, Interval, Time, Table_of_lights)
    	for Index = Start, End, Interval do
    		wait(Time)
    	end
    end
    

  * **Start**：主循环的起始数字。
  * **End**：主循环的结束数字。
  * **Interval**：这将是主循环计数用的数字。需要注意的是，主循环计数时可以进行正向或负向计数。
  * **Time**：循环每个周期之间的时长。
  * **Table_of_lights**：此函数将控制所有灯光的列表。

仔细观察上述代码后，你可能会发现这段代码根本不会执行任何可见操作。下面让我们来对其进行进一步分析：在主循环中， `Index` 值代表了 for 循环的当前值，且与我们之前所提到的各个参数息息相关。因此，这个函数也拥有极大的灵活性，只需对其稍加修改，就能改变其功能。下面让我们来看一个示例：

Glowing dynamic lights Code Sample 1 ```    
    
    function AdjustLights(Start, End, Interval, Time, Table_of_lights)
    	for Index = Start, End, Interval do
    		print(Index) -- This will print the current value of Index.
    		wait(Time)
    	end
    end
    
    AdjustLights(0, 3, 1, 0.1, Table_of_lights)
    print("The next loop is about to run.")
    AdjustLights(6, 2, -2, 0.4, Table_of_lights)
    
    
    1
    2
    3
    The next loop is about to run.
    6
    4
    2

```
让我们来回想刚才发生的事。第一个循环从 0 到 3，每隔 0.1 秒加 1。第二个循环从 6 到 2，每隔 0.4 秒减 2。如果你仍然感到有些困惑，不如通过对参数进行修改来继续进行观测。你所看到的示例越多，循环的功能也就越为易懂。

理解函数的功能以及 `Index` 所代表的含义之后，我们就可以利用该值对动态光源的 `PointLight/Range|Range`（光照距离）或 `Lighting/Brightness`（光照强度）进行逐步更改了。若希望达成此效果，只需使用另外一个循环将 `Table_of_lights` 的所有值进行收集，并将其 Range（范围）或 Brightness（亮度）属性设置为 `Index`。
    
    
    function AdjustLights(Start, End, Interval, Time, Table_of_lights)
    	for Index = Start, End, Interval do
    		for Light_Index = 1, #Table_of_lights do
    			Table_of_lights[Light_Index].Range = Index -- 或 Table_of_lights[Light_Index].Brightness = Index
    		end
    		wait(Time)
    	end
    end
    

下面我们只需添加一个无线循环，让对象持续发光即可。

**回忆一下营火的例子和脚本的位置。**
    
    
    function AdjustLights(Start, End, Interval, Time, Table_of_lights)
    	for Index = Start, End, Interval do
    		for Light_Index = 1, #Table_of_lights do
    			Table_of_lights[Light_Index].Range = Index -- 或 Table_of_lights[Light_Index].Brightness = Index
    		end
    		wait(Time)
    	end
    end
    
    while true do
    	AdjustLights(14, 4, -0.5, 0.1, {script.Parent.PointLight})
    	AdjustLights(4, 14, 0.5, 0.1, {script.Parent.PointLight})
    end
    

欣赏一下自己构建的光源吧！对了，不要忘记打开 `Lighting/GlobalShadows` 选项喔。

![Glowing_Campfire.gif](https://developer.roblox.com/assets/blt31b80a1ffab56a11/Glowing_Campfire.gif)

### 另请参阅

`Roblox Coding Basics Loops|Loop`（循环）  
`PointLight`  
`SpotLight`  
`Table`



***__Roblox官方链接__:[闪烁的动态光源](https://developer.roblox.com/zh-cn/articles/Glowing-dynamic-lights)