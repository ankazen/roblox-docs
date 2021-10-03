# 文本与聊天过滤 
Time:<em>20  分钟</em>

保证玩家与游戏环境安全的重要方法之一就是使用恰当的**文本过滤**功能。Roblox 内置的文本过滤功能不仅可以防止用户看到污言秽语等不当消息，还可以屏蔽相关个人信息，防止身份泄露。由于 Roblox 拥有大量年轻用户群，防止其分享或阅读不当内容是极有必要的。

由于关键词过滤对于营造安全环境极为重要，Roblox 会对游戏内容进行主动监控，确保其符合特定标准。如果游戏被举报或自动检测到未应用过滤功能，我们将会暂时对其进行关闭，直至开发人员采取适当措施应用过滤功能。

## 如何过滤文本

通过 `TextService` 的 `TextService/FilterStringAsync|FilterStringAsync()` 函数可以对文本进行过滤。此函数会提取文本字符串（作为输入）及文本创建玩家的 ID，然后返回可用于发布过滤后字符串的 `TextFilterResult` 对象。
    
    
    local TextService = game:GetService("TextService")
    local filteredTextResult = TextService:FilterStringAsync(text, fromPlayerId)
    

`TextService/FilterStringAsync|FilterStringAsync()` 应在服务器上调用。在客户端上对其调用时会失败。 

此函数可用于过滤聊天和非聊天情景中特定用户或全部用户的字符串。此函数所返回的对象 `TextFilterResult` 有三种调用方法：`TextFilterResult/GetChatForUserAsync|GetChatForUserAsync()`、`TextFilterResult/GetNonChatStringForBroadcastAsync|GetNonChatStringForBroadcastAsync()` 和 `TextFilterResult/GetNonChatStringForUserAsync|GetNonChatStringForUserAsync()`。
    
    
    local TextService = game:GetService("TextService")
    local filteredText = ""
    local success, errorMessage = pcall(function()
    	filteredTextResult = TextService:FilterStringAsync(text, fromPlayerId)
    end)
    if not success then
    	warn("Error filtering text:", text, ":", errorMessage)
    	-- 在此处放置代码以处理过滤失败
    end
    

请注意，`TextService/FilterStringAsync|FilterStringAsync()` 和所有 `TextFilterResult` 函数都会进行内部 web 调用，因此偶尔会发生调用失败的情况。所以，上述函数应当始终被封装在 `pcall` 中。如果包含过滤器函数的 `pcall` 调用失败，请**切勿**按预期继续使用此文本（即使发布空文本字段也不要发布未过滤文本）。

### 示例 1

此示例设置了一个小组件，可让玩家向其他玩家发送消息。此类小组件需要至少两个脚本：一个用于处理输入信息和显示消息的 `LocalScript` 和一个用于过滤服务器上消息的 `Script` 。由于示例模拟了一名玩家向另一名特定玩家发送消息的情景，应使用函数 `TextFilterResult/GetChatForUserAsync|GetChatForUserAsync()`。可沿用此[实用示例](https://www.roblox.com/games/3618543227/Message-Passing-WIth-Filtering)。

#### LocalScript
    
    
    -- LocalScript
    
    local Players = game:GetService("Players")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    local player = Players.LocalPlayer
    local playerGui = player:WaitForChild("PlayerGui")
    local screen = playerGui:WaitForChild("MessageScreen")
    local sendMessageEvent = ReplicatedStorage:WaitForChild("SendPrivateMessage")
    
    -- sendFrame（发送框）的 GUI 元素
    local sendFrame = screen:WaitForChild("SendFrame")
    local recipientField = sendFrame:WaitForChild("Recipient")
    local writeMessageField = sendFrame:WaitForChild("Message")
    local sendButton = sendFrame:WaitForChild("Send")
    
    -- receiveFrame（接收框）的 GUI 元素
    local receiveFrame = screen:WaitForChild("ReceiveFrame")
    local senderField = receiveFrame:WaitForChild("From")
    local readMessageField = receiveFrame:WaitForChild("Message")
    
    -- 点击发送按钮时将会调用
    local function onSendClicked()
    	-- 尝试寻找接收消息的玩家，如果该玩家存在才会发送消息
    	local recipient = Players:FindFirstChild(recipientField.Text)
    	local message = writeMessageField.Text
    	if recipient and message ~= "" then
    		-- 发送消息
    		sendMessageEvent:FireServer(recipient, message)
    		-- 清理 send frame（发送框）
    		recipientField.Text = ""
    		writeMessageField.Text = ""
    	end 
    end
    
    -- 当发送信息事件触发时被调用，也就是说此客户端收到了消息
    local function onReceiveMessage(sender, message)
    	-- 将发送者和消息本身填写至接收框的字段中
    	senderField.Text = sender.Name
    	readMessageField.Text = message
    end
    
    -- 绑定事件函数
    sendButton.MouseButton1Click:Connect(onSendClicked)
    sendMessageEvent.OnClientEvent:Connect(onReceiveMessage)
    

#### Script
    
    
    -- 脚本
    
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local TextService = game:GetService("TextService")
    
    local sendMessageEvent = ReplicatedStorage.SendPrivateMessage
    
    local function getTextObject(message, fromPlayerId)
    	local textObject
    	local success, errorMessage = pcall(function()
    		textObject = TextService:FilterStringAsync(message, fromPlayerId)
    	end)
    	if success then
    		return textObject
    	end
    	return false
    end
    
    local function getFilteredMessage(textObject, toPlayerId)
    	local filteredMessage
    	local success, errorMessage = pcall(function()
    		filteredMessage = textObject:GetChatForUserAsync(toPlayerId)
    	end)
    	if success then
    		return filteredMessage
    	end
    	return false
    end
    
    -- 当客户端发送消息时进行调用
    local function onSendMessage(sender, recipient, message)
    	if message ~= "" then
    		-- 对输入的消息进行过滤并发送过滤后的消息
    		local messageObject = getTextObject(message, sender.UserId)
    
    		if messageObject then
    			local filteredMessage = getFilteredMessage(messageObject, recipient.UserId)
    			sendMessageEvent:FireClient(recipient, sender, filteredMessage)
    		end
    	end
    end
    
    sendMessageEvent.OnServerEvent:Connect(onSendMessage)
    

### 示例 2

本示例设置了一个对话框，可让玩家在标牌上撰写消息。由于服务器中的所有人（包括在撰写消息玩家离开后加入游戏的玩家）都可查阅此消息，因此必须使用 `TextFilterResult/GetNonChatStringForBroadcastAsync|GetNonChatStringForBroadcastAsync()` 对消息文本进行过滤。可沿用此[实用示例](https://www.roblox.com/games/3618537258/Broadcast-Text-Filtering)。

#### LocalScript
    
    
    -- LocalScript
    local Players = game:GetService("Players")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    local player = Players.LocalPlayer
    local playerGui = player:WaitForChild("PlayerGui")
    local screen = playerGui:WaitForChild("MessageScreen")
    
    -- 对话框的 GUI 元素
    local frame = screen:WaitForChild("Frame")
    local messageInput = frame:WaitForChild("Message")
    local sendButton = frame:WaitForChild("Send")
    
    -- RemoteEvent，用于向服务器发送需要过滤与显示的文本 
    local setSignText = ReplicatedStorage:WaitForChild("SetSignText")
    
    -- 按下按钮后进行调用
    local function onClick()
    	local message = messageInput.Text
    	if message ~= "" then
    		setSignText:FireServer(message)
    		frame.Visible = false
    	end
    end
    
    sendButton.MouseButton1Click:Connect(onClick)
    

#### Script
    
    
    -- 脚本
    
    local TextService = game:GetService("TextService")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    local sign = game.Workspace.Sign
    local signTop = sign.Top
    local signSurfaceGui = signTop.SurfaceGui
    local signLabel = signSurfaceGui.SignLabel
    
    local setSignText = ReplicatedStorage.SetSignText
    
    local function getTextObject(message, fromPlayerId)
    	local textObject
    	local success, errorMessage = pcall(function()
    		textObject = TextService:FilterStringAsync(message, fromPlayerId)
    	end)
    	if success then
    		return textObject
    	elseif errorMessage then
    		print("生成 TextFilterResult 时出现错误", errorMessage)
    	end
    	return false
    end
    
    local function getFilteredMessage(textObject)
    	local filteredMessage
    	local success, errorMessage = pcall(function()
    		filteredMessage = textObject:GetNonChatStringForBroadcastAsync()
    	end)
    	if success then
    		return filteredMessage
    	elseif errorMessage then
    		print("过滤消息时出现错误：", errorMessage)
    	end
    	return false
    end
    
    -- 当客户端发送撰写标牌的请求时触发
    local function onSetSignText(player, text)
    	if text ~= "" then
    		-- 过滤输入消息并发送过滤后的消息
    		local messageObject = getTextObject(text, player.UserId)
    		local filteredText = ""
    		filteredText = getFilteredMessage(messageObject)
    		signLabel.Text = filteredText
    	end
    end
    
    setSignText.OnServerEvent:Connect(onSetSignText)
    

## 需要过滤的文本

任何开发人员无法专门控制且将会在屏幕上显示的文本都应当被过滤。这通常涵盖了玩家所控制的各种文本，但如果想要确保游戏符合 Roblox 的过滤规则，请务必考虑下述其它几种情况：

### 玩家输入信息

无论文本的输入与显示方法，任何玩家撰写的拟显示文本都必须经过过滤。最常见的输入文本方式是通过 `TextBox`，但获取玩家文本输入的方式并不仅限于此，例如带有角色按钮的自定义 GUI 和 3D 空间中的交互式键盘模型等。

![AlternateInput0.png](https://developer.roblox.com/assets/blt1b2d106c5fad5144/AlternateInput0.png)



![AlternateInput1.png](https://developer.roblox.com/assets/bltc124255c68413f55/AlternateInput1.png)



除了非传统的新颖输入方法之外，还有许多显示文本的方法。例如，单词可以用 3D 部件拼写，`Humanoid|Humanoid` （人形对象）的 `Model|Model` （模型）可以显示其名称。如果此类显示内容可以被除作者外的其他玩家看到，则该文本在过滤后方可显示。

![AlternateDisplay0.png](https://developer.roblox.com/assets/bltcdd21b59162f5a68/AlternateDisplay0.png)



![AlternateDisplay1.png](https://developer.roblox.com/assets/bltd84c4c4e43b806d7/AlternateDisplay1.png)



### 随机字词

某些游戏可能会用到以随机字符生成字词后显示给玩家的机制，但也有可能在过程中生成不当用语。在此类情况下，随机文字的显示结果应通过服务器中的过滤器发送，并可在 `TextService/FilterStringAsync|FilterStringAsync()` 中使用将查看这些字词的玩家用户 ID。

举例来说，下列代码会在玩家加入游戏时向其发送一个稍后会进行显示的随机字词。代码将在循环中生成随机字词，直至发现没有被过滤器更改的字词为止。可沿用此[实用示例](https://www.roblox.com/games/3618540254/Random-Text-Filtering)。
    
    
    local TextService = game:GetService("TextService")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    local sendRandomWordEvent = ReplicatedStorage.RandomWordEvent
    local ALPHABET= "abcdefghijklmnopqrstuvwxyz"
    local MIN_LENGTH = 3
    local MAX_LENGTH = 8
    -- 生成随机词的函数
    local function generateRandomWord()
    	local length = math.random(MIN_LENGTH, MAX_LENGTH)
    	local text = ""
    	for index = 1, length do
    		local randomLetterIndex = math.random(1, string.len(alphabet))
    		text = text .. string.sub(ALPHABET, randomLetterIndex, randomLetterIndex)
    	end
    	return text
    end
    
    local function getTextObject(message, fromPlayerId)
    	local textObject
    	local success, errorMessage = pcall(function()
    		textObject = TextService:FilterStringAsync(message, fromPlayerId)
    	end)
    	if success then
    		return textObject
    	elseif errorMessage then
    		print("生成文本对象时出现错误")
    	end
    	return false
    end
    
    local function getFilteredMessage(textObject, toPlayerId)
    	local filteredMessage
    	local success, errorMessage = pcall(function()
    		filteredMessage = textObject:GetNonChatStringForUserAsync(toPlayerId)
    	end)
    	if success then
    		return filteredMessage
    	elseif errorMessage then
    		print("过滤消息时出现错误：", errorMessage)
    	end
    	return false
    end
    
    -- 当玩家加入游戏时进行调用
    local function onPlayerJoined(player)
    	local text = ""
    	local filteredText = ""
    	-- 生成随机词，直到生成的词能够通过过滤为止
    	repeat
    		filteredText = ""
    		text = generateRandomWord()
    		-- 过滤输出消息并发送过滤后的消息
    		local messageObject = getTextObject(text, player.UserId)
    		filteredText = getFilteredMessage(messageObject, player.UserId)
    	until text == filteredText
    	if text == filteredText then
    		print("消息为", text, "过滤消息为", filteredText)
    	end
    	-- 将生成的随机词发送至客户端
    	sendRandomWordEvent:FireClient(player, text)
    end
    game.Players.PlayerAdded:Connect(onPlayerJoined)
    

### 外部源

一些游戏会与外部 Web 服务器相连。在某些情况下，这种连接将用于获取游戏中显示的信息内容。如果外部站点的内容不在开发人员完全控制之下，且第三方可能会对站点内容进行修改，则在显示此内容前应对其进行过滤。
    
    
    local TextService = game:GetService("TextService")
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local HttpService = game:GetService("HttpService")
    
    local sendRandomName = ReplicatedStorage.SendRandomName
    local randomNameWebsiteAddress = "http://www.roblox.com/randomname"
    local nameTable = nil
    
    local function initializeNameTable()
    	local nameTableJSON = nil
    	local success, message = pcall(function()
    		nameTableJSON = HttpService:GetAsync(randomNameWebsiteAddress)
    	end)
    	if success then
    		nameTable = HttpService:JSONDecode(nameTableJSON)
    		print("nameTable 为：", nameTable)
    	end
    end
    
    local function onPlayerJoin(player)
    	if nameTable then
    		local randomName = ""
    		local filteredName = ""
    		local filteredNameObject
    		repeat
    			randomName = nameTable[math.random(#nameTable)]
    			local success, errorMessage = pcall(function()
    				filteredNameObject = TextService:FilterStringAsync(randomName, player.UserId)
    			end)
    			if success then
    				print("过滤对象创建成功")
    			elseif errorMessage then
    				print("创建过滤对象时发生错误")
    			end
    			local success, errorMessage = pcall(function()
    				filteredName = filteredNameObject.GetNonChatStringForUserAsync(player.UserId)
    			end)
    			if success then
    				print("过滤名称创建成功")
    			elseif errorMessage then
    				print("创建过滤名称时发生错误")
    			end
    		until randomName == filteredName
    		sendRandomName:FireClient(sendRandomName)
    	end
    end
    
    initializeNameTable()
    game.Players.PlayerAdded:Connect(onPlayerJoin)
    

### 已储存文本

很多游戏都会使用`articles/Data store|数据储存`来存储文本。例如，游戏可能会存储聊天日志或玩家昵称等。在这些情况下，如果需要过滤储存内的文本，建议在检索文本时对其进行过滤。可籍此确保文本将会使用最新版本的过滤器。
    
    
    local TextService = game:GetService("TextService")
    local DataStoreService = game:GetService("DataStoreService")
    
    local petData = nil
    local petCreator = require(game.ServerStorage.PetCreator)
    
    local function onPlayerJoin(player)
    	local data = {}
    	local success, message = pcall(function()
    		data = petData:GetAsync(player.UserId)
    	end)
    	if success then
    		local petName = data.Name
    		local petType = data.PetType
    		local filteredName = ""
    		local filteredNameObject
    		local success, message = pcall(function()
    			filteredNameObject = TextService:FilterStringAsync(petName, player.UserId)
    		end)
    		if success then
    			local worked, errorMessage = pcall(function()
    				filteredName = filteredNameObject:GetNonChatStringForBroadcastAsync()
    			end)
    			if worked then
    				petCreator:MakePet(player, petType, filteredName)
    			end
    		end
    	end
    end
    
    local success, message = pcall(function()
    	petData = DataStoreService:GetDataStore("PetData")
    end)
    if success then
    	game.Players.PlayerAdded:Connect(onPlayerJoin)
    end
    

### 例外情况

文本过滤中的一个例外情况是在向玩家显示他们自己编写的文本时无需对其进行过滤，但对此类情况仍然需要加以考虑。

使用聊天过滤器功能过滤文本需耗费少量时间。举例来说，假设玩家输入了想要显示的消息。该文本必须发送到服务器，经过滤后发送回客户端，其中每个阶段都需要一定量的时间。当使用此过程时，输入消息与返回过滤消息之间可能会出现明显延迟。

![FilterPath0.png](https://developer.roblox.com/assets/blt55058062a35b5ff0/FilterPath0.png)



向其他玩家发送消息时，这一流程是必要的（由于其他玩家所看到的文本需要经过过滤）。但撰写消息的玩家应可在聊天记录中即刻看到自己的消息。为了便于聊天进行，Roblox 对此特殊情况内置了特别的处理办法：如果玩家仅使用 `TextBox` 输入文本，则生成的文本不必针对该玩家进行过滤，且将会在此玩家屏幕上立即显示。

![FilterPath1.png](https://developer.roblox.com/assets/blt867454c593a298d8/FilterPath1.png)



重要提醒：此除外情况在检索已存储的消息时不适用。Roblox 用于检测过滤是否正确进行的自动检查会忽略键入 `TextBox` 中的文本，但仅限于使用 `TextBox` 的同一会话中。如果玩家的文本已被保存，之后在玩家重新加入游戏时被进行检索，则需要在过滤后才会进行显示（其对象包括撰写该文本的玩家）。



***__Roblox官方链接__:[文本与聊天过滤](https://developer.roblox.com/zh-cn/articles/Text-and-Chat-Filtering)