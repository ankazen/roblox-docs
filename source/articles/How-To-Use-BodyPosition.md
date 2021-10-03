# BodyPosition 
Time:<em>5  分钟</em>

当实践本教程时，请处于 Roblox Studio 中。一些开发者可能并不熟悉 BodyPosition（主体位置）的定义：BodyPosition 是使用 Roblox 模拟物理移动游戏中对象的一种方法。对象将会尝试移动至主体位置所指定的点，并尝试施加既定的力。在许多特定情况下可以运用主体位置的这一特性。举例来说，通过 BodyPosition 为对象在 Y 轴（上下方向）上定义较大的力，而在 X 和 Z 轴（分别为左右方向和前后方向）上定义较小的力。这样就能将该对象转变为能够自由移动的漂浮物体。当创建悬停飞行载具或船只时，主体位置将会十分有用。在对其进行利用时需要注意：虽然部件会尝试前往指定点，但并非一定会到达该位置。如果在其路径上存在锚固的其它对象，则该部件很可能无法到达目标位置。

## 起始设置

  1. 创建砖型小型部件（示例尺寸：5 x 1 x 5）。
  2. 选中该砖块，单击 **Insert（插入）** -> **Object（对象）** -> **Script（脚本）**。
  3. 双击新的脚本对象。

## 代码

双击脚本对象后，应当会显示以下内容：
    
    
    print("Hello World!")
    

由于本示例不需要这些文本，请将其进行删除。下面我们将会逐步解释放入该脚本的示例代码：
    
    
    function onTouched(hit)
    

上述代码的作用是当此对象被触碰时对触碰事件进行检测。
    
    
    local character = hit.Parent
    if character and character:findFirstChild("Humanoid") then
    

而这一段代码将会检测对砖块进行触碰的是否为 Humanoid（人形对象）。我们希望由人形对象触发主体位置，而非火箭炮或者弹弓弹丸等部件。
    
    
    local b = Instance.new("BodyPosition")
    

上述代码对 BodyPosition 对象进行了定义。但因为我们尚未定义其父项，该主体位置目前没有任何作用。
    
    
    b.position = Vector3.new(500, 500, 500)
    b.maxForce = Vector3.new(500000000, 500000000, 500000000)
    b.Parent = character.Torso
    

这几行代码将会定义 BodyPosition 的一部分属性。

  * BodyPosition 的 position 属性作用：当 BodyPosition 拥有父项时，此属性将会使父项前往 BodyPosition 的 position 属性位置。此属性的用途很多。举例来说，当希望进行传送而不使用传送功能时，即可利用该属性。
  * BodyPosition 的 maxForce 属性作用：该属性定义了向父项的每个轴上施加的力度，同时也控制了 BodyPosition 在将对象移动至其 position（位置）属性前其所能达到的最远位置。
  * BodyPosition 的 Parent（父项）作用：BodyPosition 的父项就是其所将移动的对象。在本示例中，我们将会移动游戏角色的 Torso（躯干）。

目前为止的代码应当如下所示：
    
    
    function onTouched(hit)
        local character = hit.Parent
        if character and character:findFirstChild("Humanoid") then
            local b = Instance.new("BodyPosition")
            b.position = Vector3.new(500, 500, 500)
            b.maxForce = Vector3.new(500000000, 500000000, 500000000)
            b.Parent = character.Torso
    

这段代码会让游戏角色飞行到 BodyPosition 的指定位置，但角色将不会落地。下面让我们来修复这一问题：
    
    
             wait(3)
             b.Parent = nil
    

加入上述代码后， BodyPosition 将在 3 秒钟后不复存在，而角色也将会随之落地。之后我们只需对函数进行清理，然后将其连接到 Touched 属性即可：
    
    
         end
    end
    script.Parent.Touched:connect(onTouched)
    

加入 end 后，即可结束 if 语句和函数。整个脚本现在应当如下所示：
    
    
    function onTouched(hit)
        local character = hit.Parent
        if character and character:findFirstChild("Humanoid") then
            local b = Instance.new("BodyPosition")
            b.position = Vector3.new(500, 500, 500)
            b.maxForce = Vector3.new(500000000, 500000000, 500000000)
            b.Parent = character.Torso
            wait(3)
            b.Parent = nil
        end
    end
    script.Parent.Touched:connect(onTouched)
    

若希望变更角色前往的位置，则可以更改 BodyPosition 的 position 属性。当将 wait 的时间改为 0.1 秒时（即 wait(0.1)），BodyPosition 的父项角色将会飞起来，十分有趣！

## 另请参阅

  * `BodyPosition`
  * `Datatype/Vector3`



***__Roblox官方链接__:[BodyPosition](https://developer.roblox.com/zh-cn/articles/How-To-Use-BodyPosition)