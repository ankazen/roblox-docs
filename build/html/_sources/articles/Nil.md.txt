# Nil 值 
Time:<em>2  分钟</em>

在 Lua 中，**nil** 表示不存在或虚无。它通常用于移除表中的值或销毁脚本中的变量。例如：

Blanking out the value of a table ```    
    
    local dictionaryTable = {
    	Monday = 1,
    	Tuesday = 2,
    	Wednesday = 3
    }
    -- Output value of 'Tuesday' key
    print(dictionaryTable.Tuesday)
    -- Clear 'Tuesday' key
    dictionaryTable.Tuesday = nil
    -- Output value of key again
    print(dictionaryTable.Tuesday)
    
    
    2
    nil

```
在 Roblox 中，`nil` 还可用于清除 `Instance` 对象的 `Instance/Parent|Parent` （父项）值并有效地将其从游戏中移除，但这可能会使该对象重生。考虑以下示例：

Sample use of "nil" ```    
    
    -- Create a new brick
    local part = Instance.new("Part")
    -- Parent new part to the workspace, making it viewable
    part.Parent = workspace 
    wait(1)
    -- Remove the part from view, but not from memory
    part.Parent = nil
    wait(1)
    -- Part still exists because it's referenced by the variable 'part', so it can be returned to view
    part.Parent = workspace 
    wait(1)
    -- Remove the part from view again
    part.Parent = nil
    -- Clear part reference so it gets picked up by the garbage collector
    part = nil
    
    
    0

```


***__Roblox官方链接__:[Nil 值](https://developer.roblox.com/zh-cn/articles/Nil)