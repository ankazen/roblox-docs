# 回复用拾取物品 
Time:<em>10  分钟</em>

在本文中，我们将探讨碰撞处理和玩家统计信息，以创建玩家可以走过去给自己治疗的医疗包。

## 创建医疗包

医疗包本身可以是`articles/Mesh Parts|网格`、一组部件 (`Model`)、`articles/3D Modeling with Parts|实体建模`的对象，甚至可以是一个简单的 `Part`。无论选择哪种类型都要做到：

  1. 锚固对象以便玩家无法踢到。
  2. 插入一个 `Script` 作为对象的直接子项（如果使用一组部件，则插入脚本作为医疗包 “case” 的子项，因为我们将用它来进行碰撞检测）。
![](https://developer.roblox.com/assets/blt64329419f2ab18cf/HealthPack-Script.png)



## 接触事件

作为一个基本的医疗包，需要能够治疗任何接触它的玩家，因此脚本需要一个 `BasePart/Touched|Touched` （触碰）事件。在此事件触发的函数中，我们需要确认接触到医疗包的任何内容都是玩家角色（否则医疗包将会尝试治疗其接触到的任何内容）。为了实现这一点，我们将检查接触医疗包的父对象是否包含一个 `Humanoid`，它是一个特殊的 `Instance`，是所有玩家角色的一部分。

```    
    
    local healthPack = script.Parent
    
    local function onPartTouch(otherPart)
    	local partParent = otherPart.Parent
    	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
    	if humanoid then
    		-- 玩家的角色触碰了医疗包
    
    	end
    end
    healthPack.Touched:Connect(onPartTouch)


```
## 治疗代码

默认情况下，Roblox 角色的生命值为 100，因此让我们创建一个设置为 30 的 `healAmount` 变量。然后，我们便可以使用 `Humanoid/Health` 属性给接触医疗包的玩家回复生命值。

```    
    
    local healthPack = script.Parent
    local healAmount = 30
    
    local function onPartTouch(otherPart)
    	local partParent = otherPart.Parent
    	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
    	if humanoid then
    		-- 玩家的角色碰触了医疗包
    		local currentHealth = humanoid.Health
    		local newHealth = currentHealth + healAmount
    		humanoid.Health = newHealth
    	end
    end
    healthPack.Touched:Connect(onPartTouch)


```
## 技能冷却

此时，当角色的脚、手、腿等的**任何部分**接触到医疗包时，将继续触发 `BasePart/Touched|Touched` （触碰）事件，从而有可能将玩家的生命值提高 30 以上。为了解决此问题，首先创建一个表示医疗包“技能冷却”将持续多少秒的 `cooldown` 变量，并将 `canHeal` 以布尔值的形式来表示该医疗包是否可以治疗：

```    
    
    local healthPack = script.Parent
    local healAmount = 30
    local cooldown = 10
    local canHeal = true


```
现在，在检查 `Humanoid` 的条件语句中，测试 `canHeal` 是否为 `true`。如果为 `true`，则将其设置为 `false`，这样治疗代码就不会立即再次执行。角色得到治疗后，等待 `cooldown` 的持续时间，然后将 `canHeal` 设置回 `true`：

```    
    
    local function onPartTouch(otherPart)
    	local partParent = otherPart.Parent
    	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
    	if humanoid and canHeal == true then
    		-- 玩家的角色碰触了医疗包
    		canHeal = false
    		local currentHealth = humanoid.Health
    		local newHealth = currentHealth + healAmount
    		humanoid.Health = newHealth
    		wait(cooldown)
    		canHeal = true
    	end
    end
    healthPack.Touched:Connect(onPartTouch)


```
## 最后修整

现在已经可以使用医疗包了，不过再添加一些东西会使它变得更好。

### 最大生命值检查

医疗包不应治疗已经完全健康的角色，因此让我们添加另一个条件来检查玩家的生命值是否低于最大值：

```    
    
    local function onPartTouch(otherPart)
    	local partParent = otherPart.Parent
    	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
    	if humanoid and canHeal == true and humanoid.Health < humanoid.MaxHealth then
    		-- 玩家的角色触碰到了医疗包
    		canHeal = false


```
### 技能冷却指示

医疗包冷却期间的视觉指示将通知玩家当前无法收集。如果医疗包为单个网格或对象（而不是一组对象），则只需在冷却期间提高其`BasePart/Transparency|Transparency` （透明度），之后再将其重置：

```    
    
    local function onPartTouch(otherPart)
    	local partParent = otherPart.Parent
    	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
    	if humanoid and canHeal == true and humanoid.Health < humanoid.MaxHealth then
    		-- 玩家的角色碰触了医疗包
    		canHeal = false
    		local currentHealth = humanoid.Health
    		local newHealth = currentHealth + healAmount
    		humanoid.Health = newHealth
    		healthPack.Transparency = 0.6
    		wait(cooldown)
    		healthPack.Transparency = 0
    		canHeal = true
    	end
    end
    healthPack.Touched:Connect(onPartTouch)


```
### 单次使用医疗包

如果你不想要多次使用的医疗包，例如，如果你想将医疗包存储在 `ServerStorage` 中并将副本克隆到游戏世界以供单次使用，则只需移除所有冷却逻辑并在治疗代码之后添加一个 `Instance/Destroy|Destroy()` 命令：

```    
    
    local healthPack = script.Parent
    local healAmount = 30
    
    local function onPartTouch(otherPart)
    	local partParent = otherPart.Parent
    	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
    	if humanoid and humanoid.Health < humanoid.MaxHealth then
    		-- 玩家的角色碰触了医疗包
    		local currentHealth = humanoid.Health
    		local newHealth = currentHealth + healAmount
    		humanoid.Health = newHealth
    		healthPack:Destroy()
    	end
    end
    healthPack.Touched:Connect(onPartTouch)


```


***__Roblox官方链接__:[回复用拾取物品](https://developer.roblox.com/zh-cn/articles/Health-Pickups)