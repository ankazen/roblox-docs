# 游戏手柄触觉反馈 
Time:<em>5  分钟</em>

Xbox One 控制器和其他一些 USB 游戏手柄控制器内置有提供触觉反馈的电机。增加隆隆声和振动可以极大地增强游戏的体验，并提供难以通过视觉或听觉传达的微妙反馈。Roblox 向开发者提供了一项名为 `HapticService` 的服务来处理触觉反馈。

### 检查振动支持

并非所有的控制器都支持振动，因此在尝试使用 ClassLink|HapticService 之前检查插入的控制器是否具有振动支持很重要。若要检查给定的控制器是否完全支持隆隆声，可以调用 `HapticService/IsVibrationSupported`
    
    
    local HapticService = game:GetService("HapticService")
    local isVibrationSupported = HapticService:IsVibrationSupported(Enum.UserInputType.Gamepad1)
    

检查游戏手柄是否支持振动之后，你也应该检查它是否支持你要使用的电机。在 XBox One 上，控制器有 4 个电机：

  * 大：在控制器的左侧。适合一般隆隆声。
  * 小：在控制器的右侧。适用于更细微的隆隆声（轮胎打滑、触电等）。
  * 左触发器：在左触发器下面。适用于刹车、枪械重装等。
  * 右触发器：在右触发器下面。适用于反冲、加速等。

在 PC 上，你无法保证用户拥有什么样的控制器。很多控制器仅支持大小电机（没有触发器）。你可以使用 `HapticService/IsMotorSupported` 查看用户的控制器是否支持你要使用的电机。
    
    
    local HapticService = game:GetService("HapticService")
    local isVibrationSupported = HapticService:IsVibrationSupported(Enum.UserInputType.Gamepad1)
    local largeSupported = false
    if isVibrationSupported then
    	largeSupported = HapticService:IsMotorSupported(Enum.UserInputType.Gamepad1, Enum.VibrationMotor.Large)
    end
    

### 打开电机

确认用户的游戏手柄支持振动之后，你便可以开始使用游戏手柄电机了。你可以使用 `HapticService/SetMotor` 打开游戏手柄上的特定电机。此函数将游戏手柄和振动振幅作为参数。振幅可以是 0 到 1 之间的任意值（0 表示无振动，1 表示最大振动）。
    
    
    local HapticService = game:GetService("HapticService")
    HapticService:SetMotor(Enum.UserInputType.Gamepad1, Enum.VibrationMotor.Large, .5)
    

你也可以使用 `HapticService/GetMotor` 来获取给定电机的当前振动振幅。
    
    
    local HapticService = game:GetService("HapticService")
    print(HapticService:GetMotor(Enum.UserInputType.Gamepad1, Enum.VibrationMotor.Large)
    

Vehicle Haptic Feedback ```    
    
    -- Services
    local HapticService = game:GetService("HapticService")
    local Players = game:GetService("Players")
    local RunService = game:GetService("RunService")
    
    -- Make sure we are running in a LocalScript.
    local player = Players.LocalPlayer
    assert(player,"This should be running in a LocalScript!")
    
    -- Setup Haptic Feedback Listener
    local function updateHapticFeedback()
    	-- Check if we currently have a character.
    	local character = player.Character
    	if character then
    		-- Do we have a Humanoid?
    		local humanoid = character:FindFirstChildOfClass("Humanoid")
    		if humanoid then
    			-- Are we in a vehicle seat?
    			local seatPart = humanoid.SeatPart
    			if seatPart and seatPart:IsA("VehicleSeat") then
    				-- Measure the current speed of the vehicle by taking the magnitude of the seat's velocity.
    				local speed = seatPart.Velocity.Magnitude 
    				
    				-- Measure the current throttle from the user.
    				local throttle = math.abs(seatPart.ThrottleFloat)
    				
    				-- Compute how much the controller should be vibrating.
    				local vibrationScale = math.min(1, (speed * throttle) / seatPart.MaxSpeed)
    				
    				-- Apply the vibration.
    				HapticService:SetMotor(Enum.UserInputType.Gamepad1, Enum.VibrationMotor.Small, vibrationScale)
    				
    				-- Return so the motor doesn't get reset.
    				return
    			end
    		end
    	end
    	
    	-- If nothing is happening, turn off the motor.
    	HapticService:SetMotor(Enum.UserInputType.Gamepad1, Enum.VibrationMotor.Small, 0)
    end
    
    -- Connect our haptic feedback listener to be updated 60 times a second.
    RunService.Heartbeat:Connect(updateHapticFeedback)
    
    
    0

```


***__Roblox官方链接__:[游戏手柄触觉反馈](https://developer.roblox.com/zh-cn/articles/Gamepad-Haptic-Feedback)