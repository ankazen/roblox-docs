# 音效与音乐 
Time:<em>10  分钟</em>

当构建游戏时，经常会有开发者忽略掉游戏中声音与音乐的重要性。如果能对这两方面进行创造性地运用，则可以为你的游戏奠定感人肺腑或激动人心的基调、增添游戏悬念、更能让游戏中的角色栩栩如生。

## Audio Marketplace（音频市场）

在 [Toolbox](/resources/studio/Toolbox)（工具箱）窗口中单击 **Marketplace**（市场）选项卡，从菜单中选择 **Audio**（音频）即可在大量音频中进行搜索。

![](https://developer.roblox.com/assets/bltc40a4f446019c115/Toolbox-Marketplace-Audio.png)



在此视图中，可以通过名称搜寻音频，也可以单击 ![](https://developer.roblox.com/assets/blt9d572a0193f40209/Toolbox-Sort-Icon.png)

 按钮进行：

  * 通过 **Creator**（创造者）的搜寻（也就是发布该音频文件的 Roblox 用户）。
  * 通过 **Sound Length** （声音长度）的搜寻，可以籍此分辨较短的声音效果与较长的音乐。
  * 对音频文件进行 **Sort**（排序）。排序种类分为按相关程度排序（最为常用）、按获取 “favorite”（收藏）票数排序、按最近更新排序、以及按评分高低排序。

在 Studio 中可以直接对音频文件进行预览，只需单击音频项角落的 **play** （播放）按钮即可。找到想要使用的音频文件后，右击音频项，选择 **Copy Asset ID** （复制资源 ID）即可（在下文中的回放测试中将会需要该 ID）。

![](https://developer.roblox.com/assets/blta9affb74e78ec98f/Audio-Item-Play-Button.png)

 1\. 预览

![](https://developer.roblox.com/assets/blte2d2f653ecf00317/Audio-Item-Copy-ID.png)

 2\. 右击复制 ID

## 上传自定义音频

在 Roblox 中上传音频文件时需要花费少量 Robux —— 这是因为我们需要花费时间对用户上传的每个声音文件进行审核。

请注意：如果你对该声音文件没有所有权或使用权，则将其上传和/或使用的行为是对 Roblox 服务条款的违背。 

将音频上传至 Roblox 网站：

  1. 访问 [Create Audio](https://www.roblox.com/develop?View=3)（创建音频）页面后，系统将会 提示你上传本地文件并为其命名。音频文件的格式必须为 **.mp3** 或 **.ogg**、时长需要小于 7 分钟、且大小不能超过 19.5 MB。
  2. 单击 **Estimate Price** （预估价格）按钮。音频文件的上传费用率取决于以下定价结构：

时长 价格

0 – 10 秒
![](https://developer.roblox.com/assets/blt0fffb3baccc585f5/Robux-Icon-Small.png)

20

10 – 30 秒
![](https://developer.roblox.com/assets/blt0fffb3baccc585f5/Robux-Icon-Small.png)

35

30 秒– 2 分钟
![](https://developer.roblox.com/assets/blt0fffb3baccc585f5/Robux-Icon-Small.png)

70

2 – 7 分钟
![](https://developer.roblox.com/assets/blt0fffb3baccc585f5/Robux-Icon-Small.png)

350

  3. 单击 **Purchase** （购买）按钮，上传音频文件。
  4. 上传完毕后，音频文件将会显示在页面列表中。点击文件名称打开其独立页面，并从浏览器窗口 URL 中复制或记录其数字 ID（在下文中的回放测试中将会需要该 ID）。

https://www.roblox.com/library/1837103530/Lucid-Dream

## 播放音乐

通过编写脚本，开发者可以在游戏中播放背景音乐。方法如下：

  1. 在 Studio 的管理器窗口中向 **ReplicatedStorage** 添加新的 `ModuleScript`。
![](https://developer.roblox.com/assets/blt03909b07be91ea1d/ReplicatedStorage-ModuleScript.png)



  2. 将新的脚本重命名为 **AudioPlayer**。
![](https://developer.roblox.com/assets/blt9cc3935af7f9fa0a/Rename-Script-AudioPlayer.png)



  3. 删除脚本中所有现存行后，粘贴下列代码：

```    
    
    local AudioPlayer = {}
    
    -- Roblox 服务
    local ContentProvider = game:GetService("ContentProvider")
    
    -- 预加载音频资源的函数
    AudioPlayer.preloadAudio = function(assetArray)
    	local audioAssets = {}
    
    	-- 将新的 “Sound” 资源添加至 “audioAssets” 数组
    	for name, audioID in pairs(assetArray) do
    		local audioInstance = Instance.new("Sound")
    		audioInstance.SoundId = "rbxassetid://" .. audioID
    		audioInstance.Name = name
    		audioInstance.Parent = game.Workspace
    		table.insert(audioAssets, audioInstance)
    	end
    
    	local success, assets = pcall(function()
    		ContentProvider:PreloadAsync(audioAssets)
    	end)
    end
    
    -- 播放音频资源的函数
    AudioPlayer.playAudio = function(assetName)
    	local audio = game.Workspace:FindFirstChild(assetName)
    	if not audio then
    		warn("Could not find audio asset: " .. assetName)
    		return
    	end
    	if not audio.IsLoaded then
    		audio.Loaded:wait()
    	end
    	audio:Play()
    end
    
    return AudioPlayer


```
为了能够播放音频文件，必须先将其下载到客户端（Roblox 应用程序）并加载。视文件大小不同，这可能需要一些时间。因此，建议通过模块的 `preloadAudio()` 函数 （第 7 至 22 行）和 `ContentProvider/PreloadAsync|ContentProvider:PreloadAsync()`（第 20 行）来预加载音频文件。 

  4. 在 **StarterPlayerScripts**（**StarterPlayer** 的子项）内创建一个新的 `LocalScript`。
![](https://developer.roblox.com/assets/bltc1618e724ad60ee8/StarterPlayerScripts-LocalScript.png)



  5. 删除脚本中所有现存行，然后粘贴以下代码。如有需要，从第 9 行开始输入其他音轨名称和音频 ID（请参阅上文中的音频市场或上传自定义音频）。

```    
    
    -- Roblox 服务
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    -- 对模块进行 Require
    local AudioPlayerModule = require(ReplicatedStorage:WaitForChild("AudioPlayer"))
    
    -- 预加载音乐音轨
    AudioPlayerModule.preloadAudio({
    	["Lucid_Dream"] = 1837103530,
    	["Desert_Sands"] = 1848350335
    })
    
    -- 播放音乐音轨
    AudioPlayerModule.playAudio("Lucid_Dream")


```
  6. 测试游戏，你会听到背景中播放第 14 行中所指定名称的音轨。

```    
    
    -- 播放音乐音轨
    AudioPlayerModule.playAudio("Lucid_Dream")


```
## 播放音效

不同于背景音乐，音效通常源自于游戏中的特定场景或对象——例如车辆的引擎轰鸣声、战场上敌人的怒吼声等。不过，这些音效也能以“环境”音效的形式播放，例如风声或雨声等。

### 3D 音效

放置在 `BasePart` 或 `Attachment` 中的音效会从部件的 `BasePart/Position|Position` （位置）或附件的 `Attachment/WorldPosition|WorldPosition` 处发出声音。这些音效被称作 **3D 音效**，而且都具备下列几种共同特征：

  * **音量** — 3D 音效的音量会随着玩家接近声源而提高。
  * **立体声** — 如果玩家的一侧距离声源较近，对应方向的扬声器音量就会较大。
  * **多普勒效应** — 如果 3D 音效的声源正在逼近玩家，声调就会升高。同样地，如果声源正在远离玩家，声调就会降低。

如果 3D 声效的源部件/附件已存在于某一场景中，则可直接在 Studio 内对其进行添加：

  1. 在 Explorer（管理器）窗口中，插入一个新的 `Sound` 对象作为源对象的子项。
![](https://developer.roblox.com/assets/blt6409bd6e49534acf/Insert-3D-Sound.png)



  2. 选中新的音效对象，在其 Properties（属性）窗口中找到其 **SoundId** 属性。输入 rbxassetid://，后面填写有效的音频 ID。例：rbxassetid://1847352423。
![](https://developer.roblox.com/assets/blt4f90c628f603e1b2/Specify-Sound-ID.png)



  3. 切换其 **Playing** 属性至开启（音效不会自动播放，需要明确指示其开始播放）。
![](https://developer.roblox.com/assets/blt6c0e7520534801dd/Toggle-Sound-Playing.png)



  4. 测试游戏，根据角色与声源的距离观测 3D 音效的音质。

### 环境音效

风声和雷鸣等环境音效无需附加至部件，因为这些音效将会充斥整个场景。正因如此，此类音效可以使用上文播放音乐中所示的相同脚本来进行播放。

### GUI 音效

用于交互式 GUI 对象的音效可以使用上文播放音乐中所示的相同 `ModuleScript` 来播放。但这样将会立即播放音效，因此可以将其连接至相关按钮的 `GuiButton/Activated|Activated` （已激活）事件监听器。

  1. 在 **StarterGui** 中添加新的 **ScreenGui**，然后在其中创建新的 **TextButton**。如果你对按钮及其基本选项并不熟悉，请参阅 `articles/Creating GUI Buttons|创建 GUI 按钮`一文。

  2. 选中新的按钮，对其插入 `LocalScript`。

![](https://developer.roblox.com/assets/blta51533314e36660b/TextButton-LocalScript.png)



  3. 删除脚本中所有现存行，粘贴以下代码。如有需要，在第 9 行输入其他音效名称和音频 ID。

```    
    
    -- Roblox 服务
    local ReplicatedStorage= game:GetService("ReplicatedStorage")
    
    -- 对模块进行 Require
    local AudioPlayerModule = require(ReplicatedStorage:WaitForChild("AudioPlayer"))
    
    -- 预加载音效
    AudioPlayerModule.preloadAudio({
    	["Simple_Click"] = 3061551819
    })
    
    -- 对按钮进行引用
    local textButton = script.Parent
    
    -- 当按钮被按下时激活的函数
    local function onButtonActivated()
    	AudioPlayerModule.playAudio("Simple_Click")
    end
    textButton.Activated:Connect(onButtonActivated)


```
  4. 测试游戏，激活按钮后，你会听到第 17 行中所指定名称的音效。

```    
    
    -- 当按钮被按下时激活的函数
    local function onButtonActivated()
    	AudioPlayerModule.playAudio("Simple_Click")
    end
    textButton.Activated:Connect(onButtonActivated)


```


***__Roblox官方链接__:[音效与音乐](https://developer.roblox.com/zh-cn/articles/sounds-and-music)