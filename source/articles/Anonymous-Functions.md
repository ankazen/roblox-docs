# 匿名函数 
Time:<em>2  分钟</em>

**匿名函数**是没有直接标识符的函数文本。它们用于缩短代码。这些函数的缺点是只能在它们形成的表达式中使用。

### 示例

与 `DataType/RBXScriptSignal` Connect 函数一起使用的匿名函数。
    
    
    local brick = script.Parent
    brick.Touched:Connect(function (part)
    	--这里是匿名函数中的注释！
    	print("Beep")
    end)
    

上述代码比定义一个命名的函数要短，比如：
    
    
    local brick = script.Parent
    
    local function onTouch(part)
    	--这里是命名函数中的注释！
    	print("Beep")
    end
    
    brick.Touched:connect(onTouch)
    

#### 关闭

匿名函数最常用于聊天脚本或复合事件脚本。使用匿名函数是为了使当前函数的参数仍然可访问。

#### 示例
    
    
    game.Players.PlayerAdded:connect(function(player)
    	player.Chatted:connect(function (msg)
    	--如果此匿名函数转换为 PlayerAdded 连接外的命名函数
    	--则将无法访问 `player` 变量。
    	end)
    end)
    

如果你希望在 Chatted 连接中使该函数具有名称，则仍然必须使用匿名函数。不过，它不需要和实际的消息处理代码一样长：
    
    
    function onPlayerChatted(player, msg)
    --由于下面的匿名函数，本函数中存在 **player** 参数
    end
    
    game.Players.PlayerAdded:connect(function (player)
    	player.Chatted:connect(function(msg)
    	--消息处理被移至 onPlayerChatted 函数，而不是此处
    		onPlayerChatted(player, msg)
    		--该函数比长消息处理代码要定义得更快
    	end)
    end)
    

这对于缩短代码很有用，但是在多次运行的代码中应避免这种情况。这是因为该函数被定义了多次，这是不必要的，因为它是不变的文本函数。这些函数应按语义命名和使用。



***__Roblox官方链接__:[匿名函数](https://developer.roblox.com/zh-cn/articles/Anonymous-Functions)