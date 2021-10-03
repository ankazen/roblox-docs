# Roblox 虚拟形象 
Time:<em>如玩具般</em>

Roblox 的每个玩家都会自动获取属于自己的人形 **avatar**（虚拟形象），且默认设置为所有 Roblox 游戏中玩家的角色外形。

![](https://developer.roblox.com/assets/blt6a63b94b291e70ec/Roblox-Avatars-Rthro-Lineup.jpg)

玩家可以通过大量身体部件、饰品、服装、皮肤颜色、动画效果等选项对其虚拟形象进行自定义。虽然玩家可以通过无穷的搭配来表达其独特的个人风格，但游戏中虚拟形象的控制权最终在于开发者手中，开发者可以为游戏中的所有虚拟形象指定特定外观。

## 虚拟形象类型

Roblox 虚拟形象可以分为两类：**R6** 和 **R15**。

![](https://developer.roblox.com/assets/blt5b0824ec37238468/Avatar-Type-R6.jpg) R6

![](https://developer.roblox.com/assets/blt9bbf4f91c34a24da/Avatar-Type-Rthro.jpg) R15

### 构成

如其名称所示，**R6** 虚拟形象仅由 6 个部件所构成，因此其动画动作十分有限。**R15** 则由 15 个部件组成，其动作范围也被扩大了很多。

R6
R15

头部
头部

身体
上半身

下半身

左臂
左大臂

左小臂

左手

右臂
右大臂

右小臂

右手

左腿
左大腿

左小腿

左脚

右腿
右大腿

右小腿

右脚

### 身体比例与 Rthro

除了身体部件、饰品和皮肤颜色之外，R15 虚拟形象的身体类型、高度、宽度、头部尺寸及比例都可以进行自定义。

选项 描述

**身体类型**
值的范围为 0%（身材短粗、如玩具般的角色）到 100%（高大、如真人般的角色）。身体类型值为 100% 时也被称为 **Rthro**。装备在[目录](https://www.roblox.com/catalog/?Category=4&Subcategory=37&Direction=2)中被标记为 ![](https://developer.roblox.com/assets/bltc604d13bcf308703/Rthro-Label-Small.png)

 的角色包时，身体类型值将会设置为 100%，但其仍然能和任何身体类型以及任何其他虚拟形象部件共同使用。

**高度与宽度**
虚拟形象的相对高度和宽度，高度的值区间在 90% 到 105% 之间，宽度的值区间在 70% 到 100% 之间。

**头部**
虚拟形象头部相对于其身体的比例，其值区间在 95% 到 100% 之间。

**比例**
当被设置为 0% 时，总体身体形态会显得更高更宽，带有宽厚的肩膀。当被设置为 100% 时，身体形态会显得更窄更矮，带有纤细的肩膀。

Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link](/zh-cn/assets/blt8aed6666fb2796f8/Rthro-Scaling-640x360.mp4) to the video instead. 

### 类型侦测

如果有必要的话，可以使用 `Humanoid/RigType` 属性来侦测某玩家的虚拟形象类型。举例来说，下列示例在 `LocalScript` 之中进行了上述操作：

```    
    
    local Players = game:GetService("Players")
    local player = Players.LocalPlayer
    
    local function getRigType(player)
    	local character = player.Character
    	if not character or not character.Parent then
    		character = player.CharacterAdded:wait()
    	end
    
    	local humanoid = character:WaitForChild("Humanoid")
    	return humanoid.RigType
    end
    
    local rigType = getRigType(player)
    print(rigType)


```
## 基础自定义

如果你想为游戏中的虚拟形象制定一个更具体且玩家设置度较低的外表，可以通过 Roblox Studio 或运行时脚本来对玩家虚拟形象进行自定义。

### Roblox Studio

开发者在 Studio 中 **Game Settings**（游戏设置）窗口的 **Avatar**（虚拟形象）部分对虚拟形象的种类、身体部件、身体比例及着装进行强制规定（详情请见 `/articles/game settings|Roblox 游戏设置`一文）。需要注意的是，如果将 **Body Type**（身体类型）设置为 0%，虚拟形象将拥有经典的 R15 虚拟形象比例；如果被设置为 100%，虚拟形象的属性就会和 Rthro 类似。

### 运行时脚本

开发者可以通过在脚本中使用 `HumanoidDescription` 实例来改变虚拟形象的属性，更多详情及编码示例请参考 `/articles/humanoiddescription system|HumanoidDescription 系统`一文。



***__Roblox官方链接__:[Roblox 虚拟形象](https://developer.roblox.com/zh-cn/articles/roblox-avatars)