# 镜头操控 
Time:<em>15  分钟</em>

除了基本的`articles/customizing the camera|镜头自定义`之外，开发者还可以通过操控游戏镜头达成如创建特定玩家（角色）视图系统、锁定镜头至世界特定位置及创建独特镜头效果等目的。

## 镜头属性

Roblox 的 `Camera` 有若干 内置 属性，其中包括：

属性 描述

`Camera/CFrame`
镜头的 `BasePart/CFrame|CFrame` 。在放置或移动游戏镜头时常会用到这一属性。

`Camera/Focus`
镜头在 3D 空间中所朝向的点。如果把镜头朝向某个特定的方向，则需要更新这一属性，因为部分视觉效果会根据其距离焦点的距离来变更细致程度。

`Camera/FieldOfView`
在屏幕上可观察到的游戏世界的范围，其范围在垂直方向的 1 至 120 度之间(默认值为 70)。

## 为镜头编写脚本

每个玩家的镜头都处于其本地设备上，因此应当将自定义镜头代码放置至 **StarterPlayer** → **StarterPlayerScripts** 下的 `LocalScript` 中。在此类脚本中，可以通过 `Workspace/CurrentCamera|CurrentCamera` 对象来访问摄像头。

获取当前镜头 ```    
    
    local camera = workspace.CurrentCamera


```
### 越肩视角

基本的越肩视角 镜头，常见于 第三人称 射击游戏当中，可以通过下列脚本来实现。此镜头将会锁定在角色的背后，玩家可通过鼠标来转动视角（非方向输入）。

越肩镜头视角 ```    
    
    local Players = game:GetService("Players")
    local ContextActionService = game:GetService("ContextActionService")
    local UserInputService = game:GetService("UserInputService")
    local RunService = game:GetService("RunService")
    
    local camera = workspace.CurrentCamera
    local cameraOffset = Vector3.new(2, 2, 8)
    local player = Players.LocalPlayer
    
    player.CharacterAdded:Connect(function(character)
    
    	local humanoid = character:WaitForChild("Humanoid")
    	local rootPart = character:WaitForChild("HumanoidRootPart")
    	humanoid.AutoRotate = false
    
    	local cameraAngleX = 0
    	local cameraAngleY = 0
    
    	local function playerInput(actionName, inputState, inputObject)
    		-- 根据输入变化计算镜头/玩家的旋转
    		if inputState == Enum.UserInputState.Change then
    			cameraAngleX = cameraAngleX - inputObject.Delta.X
    			-- 减少垂直方向鼠标/触控灵敏度并夹住垂直轴
    			cameraAngleY = math.clamp(cameraAngleY-inputObject.Delta.Y*0.4, -75, 75)
    			-- 以 X delta 来旋转根部件 CFrame
    			rootPart.CFrame = rootPart.CFrame * CFrame.Angles(0, math.rad(-inputObject.Delta.X), 0)
    		end
    	end
    	ContextActionService:BindAction("PlayerInput", playerInput, false, Enum.UserInputType.MouseMovement, Enum.UserInputType.Touch)
    
    	RunService.RenderStepped:Connect(function()
    		if camera.CameraType ~= Enum.CameraType.Scriptable then
    			camera.CameraType = Enum.CameraType.Scriptable
    		end
    		local startCFrame = CFrame.new((rootPart.CFrame.Position)) * CFrame.Angles(0, math.rad(cameraAngleX), 0) * CFrame.Angles(math.rad(cameraAngleY), 0, 0)
    		local cameraCFrame = startCFrame:ToWorldSpace(CFrame.new(cameraOffset.X, cameraOffset.Y, cameraOffset.Z))
    		local cameraFocus = startCFrame:ToWorldSpace(CFrame.new(cameraOffset.X, cameraOffset.Y, -10000))
    		camera.CFrame = CFrame.new(cameraCFrame.Position, cameraFocus.Position)
    	end)
    end)
    
    local function focusControl(actionName, inputState, inputObject)
    	-- 在输入开始时锁定并隐藏鼠标图标
    	if inputState == Enum.UserInputState.Begin then
    		UserInputService.MouseBehavior = Enum.MouseBehavior.LockCenter
    		UserInputService.MouseIconEnabled = false
    		ContextActionService:UnbindAction("FocusControl", focusControl, false, Enum.UserInputType.MouseButton1, Enum.UserInputType.Touch, Enum.UserInputType.Focus)
    	end
    end
    ContextActionService:BindAction("FocusControl", focusControl, false, Enum.UserInputType.MouseButton1, Enum.UserInputType.Touch, Enum.UserInputType.Focus)


```
注意：可以通过调整第 7 行上的镜头偏移值改变镜头相对于角色的位置。例如，将其放在角色的左肩膀上 (`-2, 2, 8`) 或者是将镜头拉到离玩家更远的位置 (`2, 2, 15`)。 

### 缩近/拉远

使用下面的脚本可以实现一种简单的缩近/拉远镜头系统。本例中使用鼠标中间来进行放大和缩小，使用 `ContextActionService` 来在移动设备上创建虚拟的缩放按钮。

缩近/拉远 ```    
    
    local Players = game:GetService("Players")
    local ContextActionService = game:GetService("ContextActionService")
    local UserInputService = game:GetService("UserInputService")
    local TweenService = game:GetService("TweenService")
    
    local camera = workspace.CurrentCamera
    local player = Players.LocalPlayer
    
    local tweenInfo = TweenInfo.new(0.5, Enum.EasingStyle.Quint, Enum.EasingDirection.Out)
    local initialFieldOfView = camera.FieldOfView
    local initialCameraPosition = camera.CFrame
    local isZoomed = false
    local inTween = false
    local target
    
    player.CharacterAdded:Connect(function(character)
    
    	local humanoid = character:WaitForChild("Humanoid")
    	local rootPart = character:WaitForChild("HumanoidRootPart")
    	local initialWalkSpeed = humanoid.WalkSpeed
    	local initialJumpPower = humanoid.JumpPower
    
    	local cameraAngleX = 0
    	local cameraAngleY = 0
    
    	local function moveInput(actionName, inputState, inputObject)
    		if not isZoomed then return end
    		if inputState == Enum.UserInputState.Change then
    			cameraAngleX = math.clamp(cameraAngleX-inputObject.Delta.X*0.4, -90, 90)
    			cameraAngleY = math.clamp(cameraAngleY-inputObject.Delta.Y*0.4, -75, 75)
    			local camPosition = rootPart.CFrame:ToWorldSpace(CFrame.new(0, 2, -2))
    			local camRotation = camPosition * CFrame.Angles(0, math.rad(cameraAngleX), 0) * CFrame.Angles(math.rad(cameraAngleY), 0, 0)
    			target = camRotation:ToWorldSpace(CFrame.new(0, 0, -20))
    			camera.CFrame = CFrame.new(camRotation.Position, target.Position)
    			camera.Focus = CFrame.new(target.Position)
    		end
    	end
    
    	local function scopeInOut(actionName, inputState, inputObject)
    		if inTween == true then return end
    		if (inputObject.UserInputType == Enum.UserInputType.MouseButton3 and (inputState == Enum.UserInputState.Begin or inputState == Enum.UserInputState.End))
    			or (inputObject.UserInputType == Enum.UserInputType.Touch and inputState == Enum.UserInputState.End) then
    			inTween = true
    			-- 缩近
    			if isZoomed == false then
    				initialCameraPosition = camera.CFrame
    				camera.CameraType = Enum.CameraType.Scriptable
    				UserInputService.MouseBehavior = Enum.MouseBehavior.LockCenter
    				UserInputService.MouseIconEnabled = false
    				-- 根据镜头方向来旋转根部件 CFrame
    				local faceToward = camera.CFrame:Lerp(rootPart.CFrame, 1.1)
    				rootPart.CFrame = CFrame.new(rootPart.CFrame.Position, Vector3.new(faceToward.Position.X, rootPart.Position.Y, faceToward.Position.Z))
    				target = rootPart.CFrame:ToWorldSpace(CFrame.new(0, 2, -20))
    				cameraAngleX, cameraAngleY = 0, 0
    				humanoid.WalkSpeed = 0
    				humanoid.JumpPower = 0
    				wait(0.05)
    				local camPosition = rootPart.CFrame:ToWorldSpace(CFrame.new(0, 2, -2))
    				camera.CFrame = CFrame.new(camera.CFrame.Position, target.Position)
    				local tween = TweenService:Create(camera, tweenInfo, {CFrame=camPosition, FieldOfView=12})
    				tween.Completed:Connect(function()
    					ContextActionService:BindAction("MoveInput", moveInput, false, Enum.UserInputType.MouseMovement, Enum.UserInputType.Touch)
    					ContextActionService:SetTitle("ScopeInOut", "–")
    					camera.Focus = CFrame.new(target.Position)
    					isZoomed = true
    					inTween = false
    				end)
    				tween:Play()
    			-- 拉远
    			elseif isZoomed == true then
    				ContextActionService:UnbindAction("MoveInput", moveInput, false, Enum.UserInputType.MouseMovement, Enum.UserInputType.Touch)
    				UserInputService.MouseBehavior = Enum.MouseBehavior.Default
    				UserInputService.MouseIconEnabled = true
    				local tween = TweenService:Create(camera, tweenInfo, {CFrame=initialCameraPosition, FieldOfView=initialFieldOfView})
    				tween.Completed:Connect(function()
    					ContextActionService:SetTitle("ScopeInOut", "+")
    					camera.CameraType = Enum.CameraType.Custom
    					humanoid.WalkSpeed = initialWalkSpeed
    					humanoid.JumpPower = initialJumpPower
    					isZoomed = false
    					inTween = false
    				end)
    				tween:Play()
    			end	
    		end
    	end
    	ContextActionService:BindAction("ScopeInOut", scopeInOut, true, Enum.UserInputType.MouseButton3)
    	ContextActionService:SetPosition("ScopeInOut", UDim2.new(0.65, 0, 0.1, 0))
    	ContextActionService:SetTitle("ScopeInOut", "+")
    end)


```
缩近与拉远的速度可以通过第 9 行上 `TweenInfo.new()` 的第一个参数进行调整，并且作用域缩放力可以使用第 60 行上的 `FieldOfView` 值（介于 10 和 20 之间最佳）进行调整。 

### 绕着对象旋转

若要让镜头全部或部分围绕镜头旋转，请尝试使用以下脚本。该脚本具有可调整镜头偏移、旋转时间、重复计数、过渡类型等功能。

绕对象旋转 ```    
    
    local TweenService = game:GetService("TweenService")
    local RunService = game:GetService("RunService")
    
    local target = workspace.Part  -- 想要绕着旋转的对象
    local camera = workspace.CurrentCamera
    camera.CameraType = Enum.CameraType.Scriptable
    camera.Focus = target.CFrame
    local rotationAngle = Instance.new("NumberValue")
    local tweenComplete = false
    
    local cameraOffset = Vector3.new(0, 10, 12)
    local rotationTime = 15  -- 时间，以秒计
    local rotationDegrees = 360
    local rotationRepeatCount = -1  -- 使用 -1 以无限次重复
    local lookAtTarget = true  -- 镜头是否倾斜以直接指向目标
    
    local function updateCamera()
    	local rotatedCFrame = CFrame.Angles(0, math.rad(rotationAngle.Value), 0)
    	camera.CFrame = rotatedCFrame:ToWorldSpace(CFrame.new(cameraOffset))
    	if lookAtTarget == true then
    		camera.CFrame = CFrame.new(camera.CFrame.Position, target.Position)
    	end
    end
    
    -- 设置并开始旋转过渡
    local tweenInfo = TweenInfo.new(rotationTime, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut, rotationRepeatCount)
    local tween = TweenService:Create(rotationAngle, tweenInfo, {Value=rotationDegrees})
    tween.Completed:Connect(function()
    	tweenComplete = true
    end)
    tween:Play()
    
    -- 在过渡运行时更新镜头位置
    RunService.RenderStepped:Connect(function()
    	if tweenComplete == false then
    		updateCamera()
    	end
    end)


```
调整第 11 至 15 行上的变量可以控制脚本的行为表现。举例来说，如果镜头位于目标对象上方比较高的位置，如 `cameraOffset` 矢量值为 `0, 30, 12`，则 `lookAtTarget` 设置控制是否向下倾斜镜头来直接观察对象。 

### 横向卷轴镜头

通过下列脚本可以实现常用的横向卷轴镜头系统。此示例的镜头锁定在了 **X** 面上，此外 **Z** 偏移可以根据玩家调整。

若想确保该脚本正常运行， **必须** 通过将 **DevTouchMovementMode** 设置为 **Thumbstick** 来在移动设备上启用传统的拇指摇杆控制模式。详情请参阅`articles/customizing game controls|自定义游戏控制` 一文。 

横向卷轴镜头系统 ```    
    
    local Players = game:GetService("Players")
    local ContextActionService = game:GetService("ContextActionService")
    local UserInputService = game:GetService("UserInputService")
    local RunService = game:GetService("RunService")
    
    local cameraChase = {left=10, right=10, up=5, down=0}
    local cameraDistance = 200
    
    local camera = workspace.CurrentCamera
    camera.CameraType = Enum.CameraType.Scriptable
    camera.FieldOfView = 10
    
    local player = Players.LocalPlayer
    local leftValue, rightValue, initialTouchPos, jumpTouchInput, thumbstickMinPush, cameraPosZ = 0, 0, 0, nil, 15, 0
    local humanoid, rootPart
    
    local function handleMovement(actionName, inputState)
    	if inputState == Enum.UserInputState.Begin then
    		if actionName == "Left" then
    			leftValue, rightValue = 1, 0
    		elseif actionName == "Right" then
    			rightValue, leftValue = 1, 0
    		end
    	elseif inputState == Enum.UserInputState.End then
    		if actionName == "Left" or actionName == "Stop" then
    			leftValue = 0
    		end
    		if actionName == "Right" or actionName == "Stop" then
    			rightValue = 0
    		end
    	end
    end
    
    local function onMove()
    	if humanoid then
    		local moveDirection = rightValue - leftValue
    		humanoid:Move(Vector3.new(moveDirection, 0, 0), false)
    	end
    end
    
    local function updateCamera()
    	if camera.CameraType ~= Enum.CameraType.Scriptable then
    		camera.CameraType = Enum.CameraType.Scriptable
    	end
    
    	if rootPart then
    		-- 负责处理水平方向镜头追踪
    		if rootPart.Position.X < camera.CFrame.Position.X - cameraChase["left"] then
    			camera.CFrame = CFrame.new(Vector3.new(rootPart.Position.X+cameraChase["left"], camera.CFrame.Position.Y, cameraPosZ))
    		elseif rootPart.Position.X > camera.CFrame.Position.X + cameraChase["right"] then
    			camera.CFrame = CFrame.new(Vector3.new(rootPart.Position.X-cameraChase["right"], camera.CFrame.Position.Y, cameraPosZ))
    		end
    		-- 负责处理垂直方向镜头追踪
    		if rootPart.Position.Y < camera.CFrame.Position.Y - cameraChase["down"] then
    			camera.CFrame = CFrame.new(Vector3.new(camera.CFrame.Position.X, rootPart.Position.Y+cameraChase["down"], cameraPosZ))
    		elseif rootPart.Position.Y > camera.CFrame.Position.Y + cameraChase["up"] then
    			camera.CFrame = CFrame.new(Vector3.new(camera.CFrame.Position.X, rootPart.Position.Y-cameraChase["up"], cameraPosZ))
    		end
    	end
    end
    
    local function handleTouchInput(input, gameProcessed)
    	if input.UserInputState == Enum.UserInputState.Begin and gameProcessed == true then
    		-- 如果触控起始于 jump 按钮，则追踪该按钮
    		if humanoid.Jump == true then
    			jumpTouchInput = input
    		-- 或者触控起始于拇指摇杆，设置初始位置
    		else
    			initialTouchPos = input.Position.X
    		end
    	elseif input.UserInputState == Enum.UserInputState.Change and gameProcessed == true then
    		-- 在玩家移动方面忽略起始于 jump 按钮的触控操作
    		if jumpTouchInput == input then return end
    		-- 只有当拇指摇杆被推动一定程度之后才会处理移动动作
    		if input.Position.X < initialTouchPos - thumbstickMinPush then
    			handleMovement("Left", Enum.UserInputState.Begin)
    		elseif input.Position.X > initialTouchPos + thumbstickMinPush then
    			handleMovement("Right", Enum.UserInputState.Begin)
    		end
    	elseif input.UserInputState == Enum.UserInputState.End then
    		-- 如果触控操作在 jump 按钮上结束，停止追踪触控
    		if jumpTouchInput == input then
    			jumpTouchInput = nil
    		-- 或者触控操作在拇指摇杆上结束，停止所有移动动作
    		else
    			handleMovement("Stop", input.UserInputState)
    			initialTouchPos = 0
    		end
    	end
    end
    
    player.CharacterAdded:Connect(function(character)
    
    	humanoid = player.Character:WaitForChild("Humanoid")
    	rootPart = player.Character:WaitForChild("HumanoidRootPart")
    	-- 设置初始镜头位置
    	camera.CFrame = CFrame.new(Vector3.new(rootPart.Position.X, rootPart.Position.Y, rootPart.Position.Z+cameraDistance))
    	cameraPosZ = camera.CFrame.Position.Z
    	-- 如果触控启用，则连接触控处理函数
    	if UserInputService.TouchEnabled == true then
    		UserInputService.TouchStarted:Connect(handleTouchInput)
    		UserInputService.TouchMoved:Connect(handleTouchInput)
    		UserInputService.TouchEnded:Connect(handleTouchInput)
    	end
    end)
    
    RunService:BindToRenderStep("Input", Enum.RenderPriority.Input.Value, onMove)
    RunService:BindToRenderStep("Camera", Enum.RenderPriority.Camera.Value, updateCamera)
    ContextActionService:BindAction("Left", handleMovement, false, "a", Enum.KeyCode.Left)
    ContextActionService:BindAction("Right", handleMovement, false, "d", Enum.KeyCode.Right)


```
第 6 行上的 `cameraChase` 值控制在镜头开始追随玩家之前，玩家可以移离“屏幕中心”的格数。在 `cameraDistance` 值（第 7 行）的基础上每个方向值都可以调整，以便适配您的游戏设计，达到心中最好的观感效果。



***__Roblox官方链接__:[镜头操控](https://developer.roblox.com/zh-cn/articles/Camera-manipulation)