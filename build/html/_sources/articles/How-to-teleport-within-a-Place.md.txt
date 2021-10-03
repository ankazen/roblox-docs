# 场景内玩家传送 
Time:<em>5  分钟</em>

“传送”一词用于描述将一组部件（通常是玩家的角色）移至某一坐标的动作。在 Roblox 中，设置一个部件的 `Position` 属性会断开该部件与任何其他相连部件的连接，从而破坏模型。因此，不可使用以下方法传送玩家，因为这会将躯干与头部断开。
    
    
    game.Workspace.Player.Torso.Position = Vector3.new(0, 50, 0)
    

要在不消灭玩家的情况下正确传送玩家，必须使用 Cframe 属性并改用 `Articles/Understanding CFrame|CFrame` 数据类型。
    
    
    game.Workspace.Player.HumanoidRootPart.CFrame = CFrame.new(Vector3.new(0, 50, 0))
    

## Cframe 对 MoveTo

`Humanoid/MoveTo|MoveTo` 可用于设置模型中的一块砖的 Cframe。仅当 Parent 属性为 Workspace 时，MoveTo 才会更改模型中部件的 Position/CFrame。

## 传送全部玩家

可通过迭代每一玩家角色并相应设置 Cframe 传送游戏中的全部玩家。

同时传送一组玩家时要小心：偏移目标位置，以免各玩家躯干重叠。
    
    
    target = CFrame.new(0, 50, 0) --可能会是在砖块旁边或新的区域内
    for i, player in ipairs(game.Players:GetChildren()) do
       --确保角色及其 HumanoidRootPart 存在
       if player.Character and player.Character:FindFirstChild("HumanoidRootPart") then
           --为每个角色添加值为 5 的偏移
          player.Character.HumanoidRootPart.CFrame = target + Vector3.new(0, i * 5, 0)
       end
    end
    

上述代码会将每个玩家传送至位置（0,50,0），为其提供最大为 5 的偏移，以免其重叠。显然，将玩家向上偏移有助于避免相互碰撞，但如果玩家正在被传送至建筑物或房间中，则可能最终会将玩家放置于天花板或房顶上。在创建传送逻辑时要耐心谨慎，以免出现此类逾越边界情况。

## 传送效果

可使用 `Articles/For Loops|for 循环` 逐步增加肢体的透明度，从而加入淡出效果。
    
    
    player = game.Players.Player --或许需要在这里进行改变……
    target = Vector3.new(20, 10, 20) --……还有这里
    
    function fadeTo(a, b, c)
        for transparency = a, b, c do
        --从 a 到 b，以 c 为计
            for _, part in pairs(player.Character:GetChildren()) do
            --对于此角色中的每一个对象
    
                if part:IsA("BasePart") then
                --都需要检查其是否为部件
    
                    part.Transparency = transparency
                    --若是则设置其透明度
                end
            end
            wait(0.1)
        end
    end
    
    fadeTo(0, 1, 0.1) --淡出
    player.Character.HumanoidRootPart.CFrame = target --传送玩家
    fadeTo(1, 0, -0.1) --淡入
    

其他效果可包括：更改 `BasePart/Reflectance` 以让玩家从地面腾空而起、闪闪发光，或使用 `BodyAngularVelocity` 让玩家旋转。



***__Roblox官方链接__:[场景内玩家传送](https://developer.roblox.com/zh-cn/articles/How-to-teleport-within-a-Place)