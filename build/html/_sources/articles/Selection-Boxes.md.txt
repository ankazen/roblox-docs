# 选择框 
Time:<em>5  分钟</em>

本教程介绍如何使用 SelectionBox 以及它的一些用例。

和所有对象一样，`SelectionBox` 需要一个父对象和一个 `PVAdornment/Adornee`。你可以将 SelectionBox 放在任何需要的位置作为其父级，但必须设置其装饰对象。装饰对象将显示在部件上面，因此它基本上会覆盖该部件。下面是一个如何创建 SelectionBox 以及如何设置其装饰对象的示例：
    
    
    local part = Instance.new("Part",workspace)
    part.Anchored = true
    part.Size = Vector3.new(5,5,5)
    
    local selectionBox = Instance.new("SelectionBox")
    selectionBox.Adornee = part
    selectionBox.Color3 = Color3.new(1,0,0)
    selectionBox.Parent = part
    

![SelectionBoxExample.jpg](https://developer.roblox.com/assets/blt1ef83c85311f20db/SelectionBoxExample.jpg)

### 使用鼠标选择部件

为此，你只需向 StarterGui 中插入一个 LocalScript，该脚本将复制到该玩家的 PlayerGui 并且当他们将其鼠标放置在部件上时，会在其鼠标经过的部件上出现 SelectionBox。该脚本很容易作为基础脚本使用，开发者可以轻易将其转换成执行某些操作的工具，但因此其也只是一个基本脚本，可供开发者填充扩展任何想要的内容。

How to Use a Selection Box: Code Sample 1 ```    
    
    local modelMode = false  -- if true, select models rather than parts
    
    local player = game.Players.LocalPlayer
    local mouse = player:GetMouse() --Getting the player's mouse
    
    local selection = Instance.new("SelectionBox")
    selection.Color3 = Color3.new(0.6,0.6,0,6)
    selection.Parent = player.PlayerGui
    
    mouse.Move:Connect(function() --When the mouse moves
    	local target = mouse.Target
    
    	if not target then
    		-- nothing selected
    		selection.Adornee = nil
    	elseif modelMode then
    		-- when in model mode, try and select the parents first
    		if target.Parent:IsA("Model") then
    			selection.Adornee = target.Parent
    		elseif target.Parent.Parent:IsA("Accoutrement") then
    			selection.Adornee = target.Parent.Parent
    		elseif target:IsA("BasePart") then
    			selection.Adornee = target
    		else
    			selection.Adornee = nil
    		end
    	else
    		if target:IsA("BasePart") then
    			selection.Adornee = target
    		else
    			selection.Adornee = nil
    		end
    	end
    end)
    
    
    0

```


***__Roblox官方链接__:[选择框](https://developer.roblox.com/zh-cn/articles/Selection-Boxes)