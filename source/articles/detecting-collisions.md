# 检测碰撞 
Time:<em>5  分钟</em>

Collision（碰撞）是游戏世界中虚拟形状出现交集时所产生的结果。这些虚拟形状在 Roblox 中被称为 `BasePart` 对象，而其出现交集时的行为取决于开发者对碰撞现象的**脚本编写**。

在进行碰撞处理时，请注意以下几点：

  * Roblox 中的碰撞会导致对象进行位移。当不希望对象位置受碰撞影响时，请禁用碰撞中涉及双方对象或其中之一的 `BasePart/CanCollide|CanCollide` 属性。禁用后，`BasePart/Touched|Touched` （已触碰）和 `BasePart/TouchEnded|TouchEnded` 事件仍然会触发，但碰撞对象的动量状态将不会受到影响。
  * 当需要隐藏碰撞检测部件（如大门前能够检测玩家进入建筑物的区域等）时，请将其 `BasePart/Transparency|Transparency`（透明度）属性设置为 **1**。
  * `BasePart|BasePart` 同时也可以使用自定义网格。关于如何针对自定义网格为碰撞检测进行微调，请查看 `Enum/CollisionFidelity|CollisionFidelity` 一文。

## Touched 事件

即使部件设置为不发生物理碰撞（也就是当 `BasePart/CanCollide|CanCollide` 设置为 `false` 时），Roblox 也会触发部件接触或相交的 `BasePart/Touched|Touched` （触碰）事件。此功能对触发游戏中的特定事件非常有用，例如打开活板门、在障碍赛中通过保存点保存游戏进度、以及依照玩家位置不同更改其区域天空盒等情况。

### 部件触发的碰撞

任何部件都可以用来触发 `BasePart/Touched|Touched` （触碰）事件。当需要在游戏中使用该事件时，必须通过 `Connect()` 为其连接一个函数。将下列 `Script`（脚本）放置在部件内，即可显示如何使用 `BasePart/Touched|Touched` （触碰）事件检测该部件与其他部件的碰撞。

```    
    
    local part = script.Parent
    
    local function onPartTouched(otherPart)
    	print(part.Name .. " 触碰了 " .. otherPart.Name)
    end
    
    part.Touched:Connect(onPartTouched)


```
### 角色触发的碰撞

若要检测玩家的**角色**是否触碰了任何部件，请找到碰撞部件的父项，并检查其是否包含 `Humanoid` 对象。该脚本必须放在检测碰撞的部件中。

```    
    
    local part = script.Parent
    
    local function onPartTouched(otherPart)
    	-- 获取另一个部件的父项
    	local partParent = otherPart.Parent
    	-- 在父项中寻找 Humanoid 对象
    	local humanoid = partParent:FindFirstChildWhichIsA("Humanoid")
    	if humanoid then
    		-- 对 Humanoid 对象进行操作（例：将其生命值设为 0）
    		humanoid.Health = 0
    	end
    end
    
    part.Touched:Connect(onPartTouched)


```
当发生角色与其他模型间多次触发 `BasePart/Touched|Touched` 事件的情况时，其原因可能是角色的每个部件（脚、小腿等）都分别触发了不同的事件。为了防止这种情况，开发者可以在脚本中添加`articles/Debounce|防抖动`系统。 

## TouchEnded 事件

Roblox 同时也提供了在碰撞结束时触发的 `BasePart/TouchEnded|TouchEnded` 事件，可以用来检测两个对象之间停止接触的时间。

```    
    
    local part = script.Parent
    
    local function onPartTouchEnded(otherPart)
    	print(part.Name .. " 不再触碰 " .. otherPart.Name)
    end
    
    part.TouchEnded:Connect(onPartTouchEnded)


```


***__Roblox官方链接__:[检测碰撞](https://developer.roblox.com/zh-cn/articles/detecting-collisions)