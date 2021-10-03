# 设置文本动画 
Time:<em>5  分钟</em>

可以通过以下效果在视觉上增强输出 NPC 对话、玩家指令和提示等游戏内文本的效果：

Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link]() to the video instead. 

## 打字机模块

以下模块模仿了上述效果，几乎可以在任何 `TextLabel` 或 `TextButton` 上使用。若要在游戏中使用，你需要：

  1. 在 `ReplicatedStorage` 中创建一个新的 `ModuleScript`。
  2. 将这个新脚本重命名为 _TypeWriter_。
  3. 将以下代码复制到该脚本中。

```    
    
    local SOURCE_LOCALE = "en"
    
    local LocalizationService = game:GetService("LocalizationService")
    local Players = game:GetService("Players")
    
    local player = Players.LocalPlayer
    
    local translator = nil
    pcall(function()
    	translator = LocalizationService:GetTranslatorForPlayerAsync(player)
    end)
    if not translator then
    	pcall(function()
    		translator = LocalizationService:GetTranslatorForLocaleAsync(SOURCE_LOCALE)
    	end)
    end
    
    local TypeWriter = {}
    
    local defaultConfigurations = {
    	delayTime = 0.2,
    	extraDelayOnSpace = true
    }
    
    function TypeWriter.configure(configurations)
    	for key, value in pairs(defaultConfigurations) do
    		local newValue = configurations[key]
    		if newValue ~= nil then
    			defaultConfigurations[key] = newValue
    		else
    			warn(key .. " is not a valid configuration for TypeWriter module")
    		end
    	end
    end
    
    function TypeWriter.typeWrite(guiObject, text)
    	guiObject.AutoLocalize = false
    	guiObject.Text = ""
    	local displayText = text
    	if translator then
    		displayText = translator:Translate(guiObject, text)
    	end
    	for first, last in utf8.graphemes(displayText) do
    		local grapheme = string.sub(displayText, first, last)
    		guiObject.Text = guiObject.Text .. grapheme
    		if defaultConfigurations.extraDelayOnSpace and grapheme == " " then
    			wait(defaultConfigurations.delayTime)
    		end
    		wait(defaultConfigurations.delayTime)
    	end
    end
    
    return TypeWriter


```
如果你的游戏的源语言不是英语，请更改第 1 行上`articles/localization portal additional features#locale-code-reference|区域设置代码` (`en`) 以匹配本地化门户中的游戏源语言设置。 

该模块的主要功能包括：

  * 支持采用你在`articles/Introduction to Localization on Roblox|本地化门户`中配置的语言对输出文本进行**本地化翻译**。
  * 轻松自定义选项，如文本输出速度和句子中断词之间是否存在自然延迟。
  * 在输出非拉丁字符（如中文或朝鲜语）时完全支持 UTF-8 编码。

## 脚本实现

若要使用该模块显示打出的文本，需要一个能够显示文本的 GUI 对象，例如 `TextLabel`。如果你不熟悉文本标签及其基本选项，请参阅 `articles/Intro to GUIs|GUI 简介`。

  1. 创建一个 `TextLabel`。为了进行测试，合适的位置应位于以 `StarterGui` 为父系的 `ScreenGui` 中。
  2. 创建一个新的 `LocalScript` 作为 `TextLabel` 的直接子系。
  3. 将以下代码复制到新的 `LocalScript` 中。随意将第 7 行引号中的文本更改为所需的任何文本。

```    
    
    -- Roblox services
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    -- Require module
    local TypeWriter = require(ReplicatedStorage:WaitForChild("TypeWriter"))
    
    TypeWriter.typeWrite(script.Parent, "Beyond this door is the Great Zorgoth...")


```
  4. 在 Studio 中对你的游戏进行测试，文本应该在 `TextLabel` 中逐字输出。

### 配置选项

为了方便起见，该模块包含一个接受以下参数的配置函数：

参数 描述 默认值

**delayTime**
每个文本字符输出之间的延迟时间（秒）。
0.2

**extraDelayOnSpace**
在遇到文本字符串中有空格时是否添加自然延迟。
true

若要更改这些设置，只需调用该模块的 `configure()` 函数，例如：

```    
    
    -- Roblox services
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    -- Require module
    local TypeWriter = require(ReplicatedStorage:WaitForChild("TypeWriter"))
    
    TypeWriter.configure({
    	delayTime = 0.05,
    	extraDelayOnSpace = false
    })
    
    TypeWriter.typeWrite(script.Parent, "Beyond this door is the Great Zorgoth...")


```


***__Roblox官方链接__:[设置文本动画](https://developer.roblox.com/zh-cn/articles/animating-text)