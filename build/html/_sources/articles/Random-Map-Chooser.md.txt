# 随机地图选择器 
Time:<em>2  分钟</em>

如果你曾经玩过 Roblox 回合游戏，那么你可能已经注意到，它们提供了多种地图，并且游戏似乎是随机选择的。你可能想知道这是如何实现的，但实际上却很简单！本文将介绍可用于循环游戏中地图的一些基本技巧，以及如何使游戏中的玩家获得流畅的体验。

## 管理器设置

典型的设置可能如下所示：

![MapChooser_Explorer.png](https://developer.roblox.com/assets/blt9051fd7f7c744ff9/MapChooser_Explorer.png)



使用此设置，游戏中可用的每个地图都存储在 `ReplicatedStorage` 中名为 **Maps** 的 `Folder` 中。  
下面是一些示例函数，你可以使用此设置将随机地图加载到世界中（之后再将其卸载）。
    
    
    local replicatedStorage = game:GetService("ReplicatedStorage")
    local maps = replicatedStorage:WaitForChild("Maps")
    
    local function pickMap()
    	local mapList = maps:GetChildren() -- Declares a table of the maps inside of the Maps folder.
    	local selectedIndex = math.random(1,#maps) -- Choose a random number between 1, and the number of maps available.
    	local map = mapList[selectedIndex]:Clone() -- Create a clone of the map we selected.
    	map.Parent = workspace -- Parent it to the workspace.
    	map.Name = "Map" -- Rename the map so that we can use the unloadMap() function later to remove it.
    	return mapList[selectedIndex].Name -- Return the name of the map we selected, in case we want to display it.
    end
    
    local function unloadMap()
    	if workspace:FindFirstChild("Map") then -- If there is a model in the Workspace named "Map"
    		workspace.Map:Destroy() -- Destroy it!
    	end
    end
    
    local h = Instance.new("Hint")
    h.Parent = workspace
    
    while true do
    	h.Text = "Picking new map..."
    	wait(3)
    	local mapName = selectMap()
    	h.Text = "Selected map: "..mapName
    	wait(3)
    	h.Text = "Unloading map..."
    	unloadMap()
    	wait(3)
    end
    

## 存储地图：ReplicatedStorage 和 ServerStorage

在上面的示例中，_Maps_ 存储在 ReplicatedStorage 中。选择将其存储在 ReplicatedStorage 中，还是存储在 ServerStorage 中，都取决于你。在决定使用哪种技巧时，需要牢记以下几点：

  * 如果你的地图是静态的并且没有更改，那么你只需在要加载地图时将其移到工作区中，然后在完成之后再将其移回到 _Maps_ 文件夹中即可。

    * 这种技巧非常有用，因为服务器只在一个时间将地图的内容发送给玩家：就是在他们加入游戏时！
  * 如果你的地图具有移动的组件，并且重复使用它可能不会很好地工作，那么你可能希望将其存储在 ServerStorage 中。

    * 与其将模型移到工作区中，不如将其`Instance/克隆`到工作区中。
    * 这样可以加快加入时间，但会导致玩家在通过网络复制地图时遇到一些延迟。



***__Roblox官方链接__:[随机地图选择器](https://developer.roblox.com/zh-cn/articles/Random-Map-Chooser)