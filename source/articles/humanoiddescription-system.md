# HumanoidDescription 系统 
Time:<em>预期输出</em>

`HumanoidDescription` 是一个 `Instance` ，可以被放置于管理器的任意层级之中，它的作用是让开发者动态的更改 `Humanoid` 的特征，比如身体部件的颜色、身体的缩放、饰品、衣物以及默认动画等。

##### 最佳实践/告诫

使用 `HumanoidDescription` 系统时，请注意以下几个要点：

  * 该系统默认角色的当前 `HumanoidDescription` 无法手动编辑，并在角色上反映当前资源。
  * 在使用 `HumanoidDescription` 系统的同时更改角色资源可能会导致不确定的行为。

  


## HumanoidDescription 属性

Accessories（饰品）

**BackAccessory（后背饰品）**

**FaceAccessory（面部饰品）**

**FrontAccessory（前身饰品）**

**HairAccessory（头发饰品）**

**HatAccessory（头帽饰品）**

**NeckAccessory（脖颈饰品）**

**ShouldersAccessory（肩膀饰品）**

**WaistAccessory（腰部饰品）**

Scale（缩放）

**BodyTypeScale（身体类型缩放）**
0.3

**DepthScale（深度缩放）**
1

**HeadScale（头部缩放）**
1

**HeightScale（高度缩放）**
1

**ProportionScale（比例缩放）**
1

**WidthScale（宽度缩放）**
1

Animation（动画）

**ClimbAnimation（攀爬动画）**
0

**FallAnimation（坠落动画）**
0

**IdleAnimation（闲置动画）**
0

**JumpAnimation（跳跃动画）**
0

**RunAnimation（奔跑动画）**
0

**SwimAnimation（游泳动画）**
0

**WalkAnimation（行走动画）**
0

Body Parts（身体部件）

**Face（脸）**
0

**Head（头）**
0

**LeftArm（左臂）**
0

**LeftLeg（左腿）**
0

**RightArm（右臂）**
0

**RightLeg（右腿）**
0

**Torso（躯干）**
0

Clothes（衣物）

**GraphicTShirt（图案T恤）**
0

**Pants（裤子）**
0

**Shirt（衬衫）**
0

Body Colors（身体颜色）

**HeadColor（头部颜色）**
[0, 0, 0]

**LeftArmColor（左臂颜色）**
[0, 0, 0]

**LeftLegColor（左腿颜色）**
[0, 0, 0]

**RightArmColor（右臂颜色）**
[0, 0, 0]

**RightLegColor（右腿颜色）**
[0, 0, 0]

**TorsoColor（躯干颜色）**
[0, 0, 0]

## 创建一个 HumanoidDescription

开发者可以在管理器层级中直接创建一个新的 `HumanoidDescription` 实例：

![](https://developer.roblox.com/assets/blt908228a5122f4f89/HumanoidDescription.png)



还可以在`Script`内部创建该实例：

```    
    
    local humanoidDescription = Instance.new("HumanoidDescription")


```
## 脚本示例

下列示例展示了该如何在脚本中使用 `HumanoidDescription`。

### 编辑属性

在 `HumanoidDescription` 实例中，不同属性群组的类型也不同：

  * **Accessories** （饰品）的属性为字符串类型，是由 逗号分隔开 的资源标识符的集合，比如`“2551510151,2535600138”`。
  * **Scale** （缩放）属性为数值型。
  * 每个 **Animation** （动画）、 **Body Parts** （身体部件）和 **Clothes** （衣物）属性都是一个单独的资源标识符。
  * 每个 **Body Colors** （身体颜色）属性都是一个`datatype/Color3|Color3`类型。

要对这些属性进行自定义，只需要在 `HumanoidDescription` 实例上直接设置即可。

```    
    
    local humanoidDescription = Instance.new("HumanoidDescription")
    humanoidDescription.HatAccessory = "2551510151,2535600138"
    humanoidDescription.BodyTypeScale = 0.1
    humanoidDescription.ClimbAnimation = 619521311
    humanoidDescription.Face = 86487700
    humanoidDescription.GraphicTShirt = 1711661
    humanoidDescription.HeadColor = Color3.new(0, 1, 0)


```
### 重新生成那些带有 HumanoidDescription 的角色

要创建一个 `HumanoidDescription` 然后重新生成一个带有此描述角色的方法是往 workspace 添加一个 `Script` （注意，不是`LocalScript`），然后把这段代码添加进去：

```    
    
    -- 停止自动生成，以便在 “PlayerAdded” 回调中执行
    game.Players.CharacterAutoLoads = false
    
    local function onPlayerAdded(player)
    	-- 创建 HumanoidDescription
    	local humanoidDescription = Instance.new("HumanoidDescription")
    	humanoidDescription.HatAccessory = "2551510151,2535600138"
    	humanoidDescription.BodyTypeScale = 0.1
    	humanoidDescription.ClimbAnimation = 619521311
    	humanoidDescription.Face = 86487700
    	humanoidDescription.GraphicTShirt = 1711661
    	humanoidDescription.HeadColor = Color3.new(0, 1, 0)
    	-- 生成带有 HumanoidDescription 的角色
    	player:LoadCharacterWithHumanoidDescription(humanoidDescription)
    end
    
    -- 将 “PlayerAdded” 事件与 “onPlayerAdded()” 函数进行连接
    game.Players.PlayerAdded:Connect(onPlayerAdded)


```
如果想试验这段编码，请下载 [HumanoidDescriptionCreateAndSpawn.rbxlx](https://developer.roblox.com/assets/blt2048c0a48967d9ec/HumanoidDescriptionCreateAndSpawn.rbxlx)。 

如果开发者在 Studio 中创建了一个 `HumanoidDescription` 并将其设置成 workspace 的子项，就可以将一个 `Script` （注意，不是 `LocalScript` ） 添加到 workspace 中并把这段编码加进去：

```    
    
    -- 停止自动生成，以便在 “PlayerAdded” 回调中执行
    game.Players.CharacterAutoLoads = false
    
    local function onPlayerAdded(player)
    	-- 生成带有 "game.Workspace.StudioHumanoidDescription" 的角色
    	player:LoadCharacterWithHumanoidDescription(game.Workspace.StudioHumanoidDescription)
    end
    
    -- 将 "PlayerAdded" 事件与 "onPlayerAdded()" 函数连接
    game.Players.PlayerAdded:Connect(onPlayerAdded)


```
要试验这段编码，请下载 [HumanoidDescriptionSpawnFromHierarchy.rbxlx](https://developer.roblox.com/assets/bltfa11561457767eca/HumanoidDescriptionSpawnFromHierarchy.rbxlx)。 

### 应用到所有角色上

下列编码被放置在一个 `Script` 中，作用是将一个位于 workspace 中的 `HumanoidDescription` 应用到当前游戏中的所有角色身上：

```    
    
    for _, player in pairs(game.Players:GetChildren()) do
    	local humanoid = player.Character and player.Character:FindFirstChild("Humanoid")
    	if humanoid then
    		-- 将 “game.Workspace.StudioHumanoidDescription” 应用到 “humanoid”
    		humanoid:ApplyDescription(game.Workspace.StudioHumanoidDescription)
    	end
    end


```
如果想查看这段编码的结果，请下载 [HumanoidDescriptionApplyDescription.rbxlx](https://developer.roblox.com/assets/blt25b99d5f6bb645b5/HumanoidDescriptionApplyDescription.rbxlx)，运行该场景，然后点击屏幕左上方的 **红色** 按钮。 

### 将角色还原为默认状态

如果要将一名角色还原到没有用虚拟形象编辑器应用任何资源的状态，请将下列编码放入一个`Script`中。注意，即使这样做也仍然会从默认的 `HumanoidDescription` 中应用身体颜色和缩放比例等。

```    
    
    local humanoid = player.Character and player.Character:FindFirstChild("Humanoid")
    if humanoid then
    	local defaultHumanoidDescription = Instance.new("HumanoidDescription")
    	humanoid:ApplyDescription(defaultHumanoidDescription)
    end


```
要查看此编码的结果，请下载 [HumanoidDescriptionApplyDescription.rbxlx](https://developer.roblox.com/assets/blt25b99d5f6bb645b5/HumanoidDescriptionApplyDescription.rbxlx)，运行该场景，然后点击屏幕左上方的 **绿色** 按钮。 

### 更改已存在的角色资源

如果要给角色添加一副新的墨镜和一个新的躯干（其他的都不做改动），请将这段编码放入一个 `Script` 之中：

```    
    
    local humanoid = player.Character and player.Character:FindFirstChild("Humanoid")
    if humanoid then
    	local descriptionClone = humanoid:GetAppliedDescription()
    	-- 只能有一具躯干
    	descriptionClone.Torso = 86500008
    	-- 在一个用逗号分隔的字符串中允许有多个面部饰品资源
    	descriptionClone.FaceAccessory = descriptionClone.FaceAccessory .. ",2535420239"
    	-- 将改动后的 “descriptionClone” 应用于人形对象
    	humanoid:ApplyDescription(descriptionClone)
    end


```
要查看此编码的结果，请下载 [HumanoidDescriptionApplyDescription.rbxlx](https://developer.roblox.com/assets/blt25b99d5f6bb645b5/HumanoidDescriptionApplyDescription.rbxlx)，运行该场景，然后点击屏幕左上方的 **蓝色** 按钮。 

如果要还原至块状躯干并移除所有当前的脸部饰品（其他的不做改动），请将下列编码放入 `Script` 之中：

```    
    
    local humanoid = player.Character and player.Character:FindFirstChild("Humanoid")
    if humanoid then
    	local descriptionClone = humanoid:GetAppliedDescription()
    	-- 还原至默认的躯干
    	descriptionClone.Torso = 0
    	-- 移除所有的面部饰品
    	descriptionClone.FaceAccessory = ""
    	-- 将改动后的 “descriptionClone” 应用于人形对象
    	humanoid:ApplyDescription(descriptionClone)
    end


```
要查看此代码的结果，请下载 [HumanoidDescriptionApplyDescription.rbxlx](https://developer.roblox.com/assets/blt25b99d5f6bb645b5/HumanoidDescriptionApplyDescription.rbxlx)，运行该场景，然后点击屏幕左上方的**白色** 按钮。 

### 更换一名已有角色的颜色

如果要让一名角色的左臂变成紫红色，（其他地方不做改动），请将这个编码放入 `Script` 中：

```    
    
    local humanoid = player.Character and player.Character:FindFirstChild("Humanoid")
    if humanoid then
    	local descriptionClone = humanoid:GetAppliedDescription()
    	descriptionClone.LeftArmColor = Color3.new(1, 0, 1)
    	-- 将改动后的 “descriptionClone” 应用于人形对象
    	humanoid:ApplyDescription(descriptionClone)
    end


```
要查看此代码的结果，请下载 [HumanoidDescriptionApplyDescription.rbxlx](https://developer.roblox.com/assets/blt25b99d5f6bb645b5/HumanoidDescriptionApplyDescription.rbxlx)，运行该场景，然后点击屏幕左上角的**紫红色**按钮。 

### 更改现有角色的身体比例

如果要让角色身高加倍（其他地方不做改动），请将此代码放入 `Script` 中：

```    
    
    local humanoid = player.Character and player.Character:FindFirstChild("Humanoid")
    if humanoid then
    	local descriptionClone = humanoid:GetAppliedDescription()
    	descriptionClone.HeightScale = descriptionClone.HeightScale*2
    	-- 将改动后的 “descriptionClone” 应用于人形对象
    	humanoid:ApplyDescription(descriptionClone)
    end


```
要查看此代码的结果，请下载 [HumanoidDescriptionApplyDescription.rbxlx](https://developer.roblox.com/assets/blt25b99d5f6bb645b5/HumanoidDescriptionApplyDescription.rbxlx)，运行场景，然后点击屏幕左上角的 **黄色**按钮。 

### 更改一名已有角色的动画

如果要更改一名角色的“闲置”动画（其他地方不做改动），请将下列内容放入 `Script` 中：

```    
    
    local humanoid = player.Character and player.Character:FindFirstChild("Humanoid")
    if humanoid then
    	local descriptionClone = humanoid:GetAppliedDescription()
    	descriptionClone.IdleAnimation = 754637456
    	-- 将改动后的 “descriptionClone” 应用于人形对象
    	humanoid:ApplyDescription(descriptionClone)
    end


```
要查看此代码的结果，请下载 [HumanoidDescriptionApplyDescription.rbxlx](https://developer.roblox.com/assets/blt25b99d5f6bb645b5/HumanoidDescriptionApplyDescription.rbxlx)，运行该场景，然后点击屏幕左上角的**蓝绿色**按钮。 

### 根据用户规范生成角色

如果要使所有生成的角色与 ID 为 **491243243** 的虚拟角色编辑器设置相匹配，请在 workspace 内的 `Scrip` 中放置以下内容：

```    
    
    -- 停止自动生成，以便在 “PlayerAdded” 回调中执行
    game.Players.CharacterAutoLoads = false
    
    local function onPlayerAdded(player)
    	local humanoidDescriptionForUser = game.Players:GetHumanoidDescriptionFromUserId(491243243)
    	-- 生成带有 HumanoidDescription 的角色
    	player:LoadCharacterWithHumanoidDescription(humanoidDescriptionForUser)
    end
    
    -- 将 “PlayerAdded” 事件连接到 “onPlayerAdded()” 函数上
    game.Players.PlayerAdded:Connect(onPlayerAdded)


```
要试验这段编码，请下载 [HumanoidDescriptionSpawnMatchingUser.rbxlx](https://developer.roblox.com/assets/bltf5b7df1111de5a87/HumanoidDescriptionSpawnMatchingUser.rbxlx)。 

### 根据装备规范生成角色

要使所有生成的角色与 ID 为 **480059254** 的装扮设置相匹配，请将以下内容放在 workspace 内的 `Script` 中：

```    
    
    -- 停止自动生成，以便其在 “PlayerAdded” 回调中执行
    game.Players.CharacterAutoLoads = false
     
    local function onPlayerAdded(player)
    	local humanoidDescriptionForOutfit = game.Players:GetHumanoidDescriptionFromOutfitId(480059254)
    	-- 生成带有 HumanoidDescription 的角色
    	player:LoadCharacterWithHumanoidDescription(humanoidDescriptionForOutfit)
    end
    
    -- 将 “PlayerAdded” 事件连接到 “onPlayerAdded()” 函数
    game.Players.PlayerAdded:Connect(onPlayerAdded)


```
要试验这段编码，请下载 [HumanoidDescriptionSpawnMatchingOutfit.rbxlx](https://developer.roblox.com/assets/blt96149b15fbf12d49/HumanoidDescriptionSpawnMatchingOutfit.rbxlx)。 



***__Roblox官方链接__:[HumanoidDescription 系统](https://developer.roblox.com/zh-cn/articles/humanoiddescription-system)