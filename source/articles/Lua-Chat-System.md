# Lua 聊天系统 
Time:<em>20  分钟</em>

通过 **Lua 聊天系统**，玩家可以使用桌面和移动平台上的文本快速轻松地进行通信。该系统可完全自定义来满足任何游戏的文本通信要求。

## API

  * 服务器端 
    * [ChatService](/articles/Lua-Chat-System/API/ChatService)：用于管理 ChatSpeaker 和 ChatChannel 的单一实例（传递到 ChatModule）
    * [ChatSpeaker](/articles/Lua-Chat-System/API/ChatSpeaker)：可在 ChatChannel 中创建消息的实体；每个 `Player` 将自动获得 ChatSpeaker，机器人可以通过创建 ChatSpeaker 进行聊天。
    * [ChatMessage](/articles/Lua-Chat-System/API/ChatMessage)：ChatSpeaker 发送到 ChatChannel 的内容的容器；包含用于格式化消息或将额外功能添加到命令的元数据
    * [ChatChannel](/articles/Lua-Chat-System/API/ChatChannel)：ChatSpeaker 可用来交换 ChatMessage 的方式；每个玩家的 ChatSpeaker 都添加到“全部”和“系统”；还用于群聊和私聊。
  * 客户端 
    * [ChatWindow](/articles/Lua-Chat-System/API/ChatWindow)
    * [ChatChannelsBar](/articles/Lua-Chat-System/API/ChatChannelsBar)
    * [ChatBar](/articles/Lua-Chat-System/API/ChatBar)
    * [ChatChannelUI](/articles/Lua-Chat-System/API/ChatChannelUI)
    * [ChatMessageLogDisplay](/articles/Lua-Chat-System/API/ChatMessageLogDisplay)
    * [ChatCustomState](/articles/Lua-Chat-System/API/ChatCustomState)
    * [ChatSettings](/articles/Lua-Chat-System/API/ChatSettings)

## 层次结构

聊天系统旨在利用客户端-服务器模型。[ChatChannel](/articles/Lua-Chat-System/API/ChatChannel) 和 [ChatSpeaker](/articles/Lua-Chat-System/API/ChatSpeaker) 管理是由服务器上的 [ChatService](/articles/Lua-Chat-System/API/ChatService) 处理的，而客户端负责输入和显示消息。服务器和客户端之间的通信是使用 `RemoteEvent` 自动处理的。

`Chat` 游戏服务本身是聊天系统的基本存储单元：当 Roblox 场景加载时（在客户端或 Studio 中运行或开始游戏时），聊天系统的所有组件都会自动加载到 `Chat` 游戏服务中（如果 `Chat/LoadDefaultChat` 为 true）。Lua 聊天系统会加载以下层次结构：

![Chat Hierarchy](https://developer.roblox.com/assets/blt150228c94a3feea1/Chat.png)



  * **ChatModules** \- 此 `Folder` 是 ChatServiceRunner 所需的模块的集合。此文件夹的所有内容都是脚本必需的，并且用于在服务器上创建自定义行为。*
  * **ClientChatModules** \- 此文件夹包含 ChatScript 所需的各种 `ModuleScript`。 
    * **CommandModules** \- 包含用于实现客户端聊天命令的模块。
    * **MessageCreatorModules** \- 包含用于处理和格式化消息的模块
    * **ChatConstants** \- 包含服务器和客户端共享的常量
    * **ChatSettings** \- 存储用于配置 [ChatWindow](/articles/Lua-Chat-System/API/ChatWindow) 的不同方面的各种设置
  * **ChatLocalization** \- 用于存储文本翻译的数据结构
  * **ChatServiceRunner** \- 此 `Script` 运行聊天的服务器组件。通常，无需对其进行修改即可创建自定义聊天行为和功能。运行游戏时，会自动克隆到 `ServerScriptService` 中。  
“InsertDefaultModules”（值为 true，将 ChatModules 文件夹添加到游戏）将自动禁用私聊和彩色名称。
  * **BubbleChat** \- 显示游戏内虚拟形象之上的玩家聊天消息（如果已启用）
  * **ChatScript** \- 此 `LocalScript` 运行聊天的客户端组件。与 ChatServiceRunner 一样，无需对其进行修改即可自定义聊天。运行游戏时，会自动克隆到 `StarterPlayerScripts` 中。

**注意：**如果 “ChatModules” 文件夹已存在于 `Chat` 游戏服务中，则不会插入默认聊天模块（除了其他功能之外，还实现了私聊和彩色名称）。要强制插入默认聊天模块，请将名为 “InsertDefaultModules” 的 `BoolValue`（`BoolValue/Value|Value` （值）为 true）插入到文件夹中。

## 修改 Lua 聊天系统（创建分支）

要修改或自定义聊天系统，必须先创建上述层次结构的副本。

  1. 使用 **Play** （开始游戏）按钮 (F5) 运行游戏。
  2. **选择并复制** (Ctrl+C) 已添加到 `Chat` 游戏服务的对象（请参见上文）。
  3. 使用 **Stop** （停止）按钮 (Shift+F5) 停止游戏。
  4. 选择 `Chat` 游戏服务并**粘贴到** (Ctrl+Shift+V) 已复制的对象（这些对象必须是 `Chat` 服务的父项，像运行游戏时一样）中。
  5. 禁用 `Chat/LoadDefaultChat`。

**警告：**以这种方式创建当前 Lua 聊天系统版本的副本（“分支”）时，如果系统已由 Roblox 更新，则不再更改你的版本。这样可以严格控制游戏聊天，但你的版本不会进行错误修复或其他更新。

## 聊天工作流程

在创建模块以自定义聊天之前，请务必了解聊天消息的整个工作流程。除了发送文本消息之外，聊天系统中还内置了各种命令，因此必须检查每条消息才能确定是将其解释为命令还是文本消息。即使是文本消息，也可以在该过程中进行修改和过滤。

玩家对聊天输入框进行聚焦并输入字符之后，立即会在客户端上进行多项检查。如果字符为“Escape”，则会关闭输入框，并且不执行任何操作。如果字符为除“Enter”以外的任何字符，则文本会通过“正在进行”命令处理器进行传递。这些命令处理器用于评估文本来确定是否需要执行操作。例如，当用户开始使用 /whisper 命令进行私聊时，一旦在该命令之后输入玩家姓名，输入框就会更改为指示玩家现在正在私聊频道中进行输入。

玩家完成输入并点击“Enter”后，将通过多个命令处理器发送他们输入的文本。如果正在进行命令创建了自定义聊天状态，则聊天会检查该状态以确定是否应执行最后一个命令以及消息是否应继续。如果允许消息继续，则将通过名为“已完成”处理器的另一组处理器发送文本。如果所有这些处理器返回 true，则将停止发送消息。否则，会将消息发送到服务器。

在聊天的客户端上，有两种类型的处理器：“正在进行”和“已完成”。“正在进行”将在输入每个字符后进行评估，“已完成”仅在玩家完成输入并点击“Enter”后进行评估。 

消息到达服务器后，它会通过另一组命令处理器进行传递。就像客户端上的“已完成”处理器一样，如果所有这些处理器返回 true，则将停止执行消息。否则，消息会通过一组过滤器（包括默认的 Roblox 聊天过滤器）进行传递。全部完成后，会将消息发送到所有频道和相应扬声器。

![Chat Workflow](https://developer.roblox.com/assets/bltac68edb91ce6e2f6/ChatWorkflow.png)



## 服务器模块

置于 ChatModules 中的模块具有多种用途。这些模块可用于管理聊天频道和扬声器、添加过滤器和命令函数、运行聊天机器人或执行需要在服务器上处理的任何操作。要与聊天系统进行交互，每个模块都将传递到 ChatService 对象。

启动 ChatServiceRunner 后，需要将每个模块置于 ChatModules 中。它要求每个模块返回函数，随即调用每个模块，从而将 ChatService 对象传递到每个函数。无论模块有何用途（运行机器人、添加过滤器函数等），都需要遵循以下形式才能正常工作。
    
    
    -- 模块框架示例
    local function Run(ChatService)
    	-- 在这里添加您的代码
    end
    
    return Run
    

### 添加频道

ChatModule 可执行的最简单操作之一是管理频道。可以使用 ChatService 的 AddChannel 函数创建频道对象。请注意，仅当调用该频道的成员（例如，属性和函数）时才需要使用频道对象。从 ChatService 或 Speakers 的上下文中参考频道时，频道名称用于引用它。
    
    
    local function Run(ChatService)
    	local myChannel = ChatService:AddChannel("MyChannel")
    end
    
    return Run
    

### 基本频道配置

频道具有多个可用于进行轻微修改的属性。例如，此模块会创建一个频道，设置欢迎消息并在玩家进入游戏时自动加入该频道。
    
    
    local function Run(ChatService)
    	local myChannel = ChatService:AddChannel("MyChannel")
    
    -- 设置用户进入频道时对其显示的消息 
    	myChannel.WelcomeMessage = "Welcome to my channel!"
    	-- 使玩家进入游戏时自动加入频道
    	myChannel.AutoJoin = true
    end
    
    return Run
    

### 频道事件

频道具有多个可供订阅的事件。将消息发布到频道、扬声器离开或加入，或者扬声器静音或取消静音时，都会触发这些事件。例如，此模块会创建一个名为 “MyChannel” 的频道。每当扬声器加入或离开频道时，都会向频道中的所有扬声器发送系统消息，告知它们所发生的事件。
    
    
    local function Run(ChatService)
    	local myChannel = ChatService:AddChannel("MyChannel")
    	
    	local function onSpeakerJoined(speakerName)
    		myChannel:SendSystemMessage(speakerName .. " has joined the channel.")
    	end
    	
    	local function onSpeakerLeft(speakerName)
    		myChannel:SendSystemMessage(speakerName .. " has left the channel.")
    	end
    	
    	myChannel.SpeakerJoined:Connect(onSpeakerJoined)
    	myChannel.SpeakerLeft:Connect(onSpeakerLeft)
    end
    
    return Run
    

### 命令函数

ChatModules 可执行的另一个强大操作是聊天命令。将消息发送到服务器时，聊天会通过已注册到 ChatService 和相关频道的每个命令函数发送消息。这些函数会发送到扬声器、消息以及将消息发送到的频道。函数可以执行任何所需操作，然后返回 true 或 false。如果函数返回 true，则聊天系统会停止处理消息。不再发送到任何命令函数，也不会显示在聊天窗口中。如果函数返回 false，则消息继续通过所有其他命令函数。如果没有命令函数返回 true，则会通过过滤器发送消息，然后显示消息。

命令函数通常用于实现所谓的“管理员命令”- 某些用户可用于通过聊天中的特定文本操纵游戏状态的文本命令。 

在此示例中，如果玩家在聊天中输入 “/part”，则 ChatModule 用于创建部件。请注意，如果已创建部件，则此函数返回 true，从而阻止消息继续且不显示任何消息。如果未创建部件，则此函数必须返回 false，消息才能继续通过系统。
    
    
    local function Run(ChatService)
    	local function createPart(speakerName, message, channelName)
    		if string.sub(message, 1, 5) == "/part" then
    			local newPart = Instance.new("Part")
    			newPart.Parent = game.Workspace
    			return true
    		end
    		return false
    	end
    
    	ChatService:RegisterProcessCommandsFunction("createPart", createPart)
    end
    
    return Run
    

频道和 ChatService 本身可以有聊天命令。将对发送到服务器的每条消息运行 ChatService 命令处理器，而仅当消息发送到注册命令的频道时，才会运行频道命令。 

### 过滤器函数

未由命令函数停止的消息会通过已注册到 ChatService 和相关频道的所有过滤器函数发送。每个过滤器函数都会传递扬声器、消息对象和频道名称。对消息对象所做的任何更改都将保留，并且以下每个过滤器函数都会看到更新后的消息。请注意，与命令函数不同，过滤器函数不需要返回值。

在此示例中，注册了简单的过滤器函数，使每条消息以小写形式显示。
    
    
    local function Run(ChatService)
    	local function makeLowercase(sender, messageObject, channelName)
    		messageObject.Message = string.lower(messageObject.Message)
    	end
    	
    	ChatService:RegisterFilterMessageFunction("makeLowercase", makeLowercase)
    end
    
    return Run
    

## 客户端模块

置于 ClientChatModules 中的模块可用于为客户端创建自定义行为。这些模块分为两个不同的文件夹：CommandModules 和 MessageCreatorModules。

### 命令模块

CommandModules 的工作方式与服务器上注册命令函数的模块的工作方式非常相似。这些模块定义将在玩家输入文本后触发的函数。该文本可以读取，并且命令可以将消息传递到服务器或停止处理消息。主要区别在于可以在用户点击“Enter”后或在输入每个字符后对 CommandModules 进行评估。在消息末尾评估的命令标记为 **COMPLETED_MESSAGE_PROCESSOR**，在每个字符之后评估的命令标记为 **IN_PROGRESS_MESSAGE_PROCESSOR**。

在这两种类型的命令中，模块必须返回指示命令应使用哪种类型的处理器，以及调用处理器时要执行哪个函数的字典。例如，已完成消息处理器应采用以下形式：
    
    
    local util = require(script.Parent:WaitForChild("Util"))
    
    function ProcessMessage(message, ChatWindow, ChatSettings)
    	
    end
    
    return {
    	[util.KEY_COMMAND_PROCESSOR_TYPE] = util.COMPLETED_MESSAGE_PROCESSOR,
    	[util.KEY_PROCESSOR_FUNCTION] = ProcessMessage
    }
    

请注意，**KEY_COMMAND_PROCESSOR_TYPE** enum 是在 CommandModules 文件夹的 Util ModuleScript 内定义的。建议始终将此模块包含在命令模块中。

#### 已完成消息命令

已完成消息命令在用户完成输入并点击“Enter”后进行评估。该处理器的函数会传递 `ChatMessage` 对象、客户端的 `ChatWindow` 和 `ChatSettings` 表。如果函数返回 true，则消息会停止处理，并且不会发送到服务器。否则，它会通过所有其他处理器发送，最终到达服务器（如果没有任何其他处理器阻止它）。

例如，如果用户输入命令 “/last”，以下处理器将删除当前频道中最早的消息。
    
    
    local util = require(script.Parent:WaitForChild("Util"))
    
    function ProcessMessage(message, ChatWindow, ChatSettings)
    	if string.sub(message, 1, 5) == "/last" then
    		local currentChannel = ChatWindow:GetCurrentChannel()
    		if (currentChannel) then
    			currentChannel:RemoveLastMessageFromChannel()
    		end
    		return true
    	end
    	return false
    end
    
    return {
    	[util.KEY_COMMAND_PROCESSOR_TYPE] = util.COMPLETED_MESSAGE_PROCESSOR,
    	[util.KEY_PROCESSOR_FUNCTION] = ProcessMessage
    }
    

#### 正在进行命令

正在进行命令在玩家将字符输入到聊天输入框中时进行评估。例如，以下代码在每次按键后发出啪嗒声，使其听起来就像玩家正在打字机上打字：
    
    
    local util = require(script.Parent:WaitForChild("Util"))
    local keyEffect = Instance.new("Sound")
    keyEffect.SoundId = "rbxassetid://12221976"
    keyEffect.Parent = script
    
    function ProcessMessage(message, ChatWindow, ChatBar, ChatSettings)
    	keyEffect:Play()
    end
    
    return {
    	[util.KEY_COMMAND_PROCESSOR_TYPE] = util.IN_PROGRESS_MESSAGE_PROCESSOR,
    	[util.KEY_PROCESSOR_FUNCTION] = ProcessMessage
    }
    

##### 自定义状态

正在进行命令通常用于创建聊天的自定义状态以将消息发送到特定玩家，而不只是当前频道。例如，私聊系统和群聊系统使用正在进行命令来确定玩家是否已分别输入 “/whisper” 或 “/team”，并且会将已完成的消息仅发送到相应的玩家。

自定义聊天状态会覆盖所有其他命令（正在进行或已完成）。在调用 ChatBar.ResetCustomState（将删除自定义状态并还原到正常聊天行为）之前，该状态保持不变。

自定义状态应为具有以下函数的表：

  * TextUpdated - 输入框中的文本发生更改时调用
  * GetMessage - 玩家输入完消息并点击“Enter”后调用。此函数应返回字符串。
  * ProcessCompletedMessage - 处理消息时调用。自定义状态处理器将始终在已完成消息处理器之前触发。与其他处理器一样，如果停止发送消息，则此函数应返回 true，否则应返回 false。
  * Destroy - 发送消息后调用。应用于清除自定义状态设置的任何内容

为了使用自定义状态，命令模块的 ProcessMessage 函数必须返回该状态。基本自定义状态将采用以下形式：
    
    
    local util = require(script.Parent:WaitForChild("Util"))
    
    local customState = {}
    customState.__index = customState
    
    function customState:TextUpdated()
    	print("text updated")
    end
    
    function customState:GetMessage()
    	print("get message")
    	return self.TextBox.Text
    end
    
    function customState:ProcessCompletedMessage()
    	print("process message")
    	return false
    end
    
    function customState:Destroy()
    	print("destroy custom state")
    	self.Destroyed = true
    end
    
    function customState.new(ChatWindow, ChatBar, ChatSettings)
    	local obj = {}
    	setmetatable(obj, customState)
    	
    	obj.Destroyed = false
    	obj.ChatWindow = ChatWindow
    	obj.ChatBar = ChatBar
    	obj.ChatSettings = ChatSettings
    	obj.TextBox = ChatBar:GetTextBox()
    	obj.MessageModeLabel = ChatBar:GetMessageModeTextLabel()	
    	
    	return obj
    end
    
    local function ProcessMessage(message, ChatWindow, ChatBar, ChatSettings)
    	return customState.new(ChatWindow, ChatBar, ChatSettings)
    end
    
    return {
    	[util.KEY_COMMAND_PROCESSOR_TYPE] = util.IN_PROGRESS_MESSAGE_PROCESSOR,
    	[util.KEY_PROCESSOR_FUNCTION] = ProcessMessage
    }
    

使用自定义状态的主要优点之一是模块可以在玩家就函数和外观方面进行输入的同时编辑聊吧及其所含文本，然后轻松对其进行重置（发送消息后，就会自动删除自定义状态，并且全部重置回正常）。例如，此代码会设置一次仅允许在文本框中显示 20 个字符的自定义状态。如果玩家继续输入，则会暂时删除字符串开头的字符。玩家发送消息后，所有已删除的字符将添加回消息。
    
    
    local util = require(script.Parent:WaitForChild("Util"))
    
    local oneLineState = {}
    oneLineState.__index = oneLineState
    
    function oneLineState:TextUpdated()
    	local text = self.TextBox.Text
    	local length = string.len(text)
    	if length > 20 then
    		local chopLength = length - 20
    		local addToPrefix = string.sub(text, 1, chopLength)
    		self.Prefix = self.Prefix .. addToPrefix
    		self.TextBox.Text = string.sub(text, chopLength + 1)
    	end
    end
    
    function oneLineState:GetMessage()
    	local fullString = self.Prefix .. self.TextBox.Text
    	return fullString
    end
    
    function oneLineState:ProcessCompletedMessage()
    	return false
    end
    
    function oneLineState:Destroy()
    	self.Destroyed = true
    end
    
    function oneLineState.new(ChatWindow, ChatBar, ChatSettings)
    	local obj = {}
    	setmetatable(obj, oneLineState)
    	
    	obj.Destroyed = false
    	obj.ChatWindow = ChatWindow
    	obj.ChatBar = ChatBar
    	obj.ChatSettings = ChatSettings
    	obj.TextBox = ChatBar:GetTextBox()
    	obj.MessageModeLabel = ChatBar:GetMessageModeTextLabel()	
    	
    	obj.Prefix = ""	
    	
    	return obj
    end
    
    local function ProcessMessage(message, ChatWindow, ChatBar, ChatSettings)
    	return oneLineState.new(ChatWindow, ChatBar, ChatSettings)
    end
    
    return {
    	[util.KEY_COMMAND_PROCESSOR_TYPE] = util.IN_PROGRESS_MESSAGE_PROCESSOR,
    	[util.KEY_PROCESSOR_FUNCTION] = ProcessMessage
    }
    

如上所述，发送消息后，就会删除任何自定义状态，并且聊天恢复为正常。如果需要在发送消息之前重置自定义状态，则可以使用 ChatBar:ResetCustomState() 重置状态。请注意，这也会取消对聊吧的文本框的聚焦。

### 消息创建者模块

可用于聊天的客户端组件的模块的其他类型是消息创建者模块。此类型的模块用于在聊天窗口中创建 GUI 元素以显示消息。每种类型的消息创建者都会定义新的消息类型，以便可以使用不同格式创建不同消息。此外，还可以将更多 GUI 元素添加到消息显示（允许使用图像、按钮等）。

消息模块需要在多个不同的位置进行设置。对于每种消息类型，必须将 ModuleScript 包含在 MessageCreatorModules 中。此外，需要编辑 ModuleScript ChatConstants 才能包括新的消息类型。最后，仅当聊天的服务器组件创建具有给定消息类型的新消息时才使用消息创建者。这意味着，通常还会创建 ChatModule（或编辑现有 ChatModule）以使用新的消息创建者。

要说明消息创建者的结构和设置，以下示例将指导创建每隔 5 秒报时的机器人，并且已发送的消息将变为红色背景。

开始之前，ChatConstants ModuleScript 必须为新的消息类型添加字段。
    
    
    -- ChatConstants
    local module = {}
    
    ---[[ 消息种类 ]]
    module.MessageTypeDefault = "Message"
    module.MessageTypeSystem = "System"
    module.MessageTypeMeCommand = "MeCommand"
    module.MessageTypeWelcome = "Welcome"
    module.MessageTypeSetCore = "SetCore"
    module.MessageTypeWhisper = "Whisper"
    module.MessageTypeTime = "Time"
    
    module.MajorVersion = 0
    module.MinorVersion = 2
    
    return module
    

机器人本身是在服务器上的新 ChatModule 中创建的。请注意，过滤器函数用于将新的消息类型添加到机器人发送的消息。
    
    
    -- 将放入 ChatModules 的新 ModuleScript
    local Chat = game:GetService("Chat")
    local ReplicatedModules = Chat:WaitForChild("ClientChatModules")
    local ChatConstants = require(ReplicatedModules:WaitForChild("ChatConstants"))
    
    local function Run(ChatService)
    	local timeBot = ChatService:AddSpeaker("TimeBot")
    	timeBot:JoinChannel("All")
    	
    	local function addMessageType(speaker, messageObject, channelName)
    		if speaker == "TimeBot" then
    			messageObject.MessageType = ChatConstants.MessageTypeTime
    		end
    	end
    	
    	ChatService:RegisterFilterMessageFunction("TimeBotFilter", addMessageType)	
    	
    	spawn(function()
    		while wait(5) do
    			timeBot:SayMessage("The current time is: " .. os.time(), "All", {})
    		end
    	end)
    end
    
    return Run
    

最后，必须创建消息创建者模块。此模块必须返回具有以下两个元素的字典：消息类型（使用 **KEY_MESSAGE_TYPE** 编制索引），以及创建消息 GUI 元素时要调用的函数（使用 **KEY_CREATOR_FUNCTION** 编制索引）。

**KEY_CREATOR_FUNCTION** 存储的函数需要返回具有多个组件的字典。首先，需要包括将显示在聊天窗口中的 Frame 和 TextLabel。它们可以使用函数 util:CreateBaseMessage 进行创建。该字典还需要包括要在更新消息文本时运行的函数。当消息先显示在客户端中时，如果正在处理和过滤消息，则会显示空占位符文本，因而此类消息对象需要处理调用更新时所发生的情况。接下来，字典需要包括用于确定框高度的函数。此函数通常调用 util:GetMessageHeight 函数。最后，字典需要包括多个用于定义窗口淡化时元素的淡化方式的函数。对此，还有其他实用工具函数：util:CreateFadeFunctions。
    
    
    -- 将被包含至 MessageCreatorModules 的新 ModuleScript
    local messageCreatorModules = script.Parent
    local util = require(messageCreatorModules:WaitForChild("Util"))
    local clientChatModules = messageCreatorModules.Parent
    
    local ChatSettings = require(clientChatModules:WaitForChild("ChatSettings"))
    local ChatConstants = require(clientChatModules:WaitForChild("ChatConstants"))
    
    
    local function CreateMessageLabel(messageData, channelName)
    	-- 为 Frame 和 TextLabel 创建 GUI 对象，用以放置消息
    	local BaseFrame, BaseMessage = util:CreateBaseMessage("", ChatSettings.DefaultFont, ChatSettings.ChatWindowTextSize, ChatSettings.DefaultMessageColor)
    	
    	-- 将 Frame 的背景改为红色
    	BaseFrame.BackgroundColor3 = Color3.new(1,0,0)
    	BaseFrame.BackgroundTransparency = 0
    	
    	-- 处理更新占位消息文本
    	local function UpdateTextFunction(messageObject)
            if messageObject.IsFiltered then
    		   BaseMessage.Text = messageObject.Message
            end
    	end
    	UpdateTextFunction(messageData)
    	
    	-- 使用 util 函数决定文本框的高度
    	local function GetHeightFunction(xSize)
    		return util:GetMessageHeight(BaseMessage, BaseFrame, xSize)
    	end
    
    	-- 创建当聊天窗口淡出时调用的淡出函数
    	local FadeParameters = {}
    	FadeParameters[BaseMessage] = {
    		TextTransparency = {FadedIn = 0, FadedOut = 1},
    		TextStrokeTransparency = {FadedIn = 0.75, FadedOut = 1}
    	}
    	local FadeInFunction, FadeOutFunction, UpdateAnimFunction = util:CreateFadeFunctions(FadeParameters)
    	
    	-- 返回定义了消息标签的字典
    	return {
    		[util.KEY_BASE_FRAME] = BaseFrame,
    		[util.KEY_BASE_MESSAGE] = BaseMessage,
    		[util.KEY_UPDATE_TEXT_FUNC] = UpdateTextFunction,
    		[util.KEY_GET_HEIGHT] = GetHeightFunction,
    		[util.KEY_FADE_IN] = FadeInFunction,
    		[util.KEY_FADE_OUT] = FadeOutFunction,
    		[util.KEY_UPDATE_ANIMATION] = UpdateAnimFunction
    	}
    end
    
    return {
    	[util.KEY_MESSAGE_TYPE] = ChatConstants.MessageTypeTime,
    	[util.KEY_CREATOR_FUNCTION] = CreateMessageLabel
    }
    



***__Roblox官方链接__:[Lua 聊天系统](https://developer.roblox.com/zh-cn/articles/Lua-Chat-System)