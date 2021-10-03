# 本地化非文本实例 
Time:<em>5  分钟</em>

在特殊情况下，可能需要将**非文本实例**（例如，用于商店招牌的图片或语音剪辑）本地化。在这种情况下，可以使用每种受支持语言的独特资源。

![](https://developer.roblox.com/assets/blt4b9d240f8abb0b44/Localized-Image-en.png)



![](https://developer.roblox.com/assets/blt3e240e0d7aac3e0b/Localized-Image-es.png)



![](https://developer.roblox.com/assets/blt3ef00a5b2b44a665/Localized-Image-pt.png)



## 翻译模块

以下模块从本地化门户获取所有翻译，并使用错误处理从基于 web 的 `Translator` API 捕获潜在故障。若要在游戏中使用：

  1. 在 `ReplicatedStorage` 中创建一个新的 `ModuleScript`。
  2. 将该脚本重命名为 _TranslationHelper_。
  3. 将以下代码复制到该脚本中。

```    
    
    local TranslationHelper = {}
    
    -- Roblox 服务
    local LocalizationService = game:GetService("LocalizationService")
    local Players = game:GetService("Players")
    
    -- 本地变量
    local player = Players.LocalPlayer
    local sourceLanguageCode = "en"
    
    -- 获取 Translator
    local playerTranslator, fallbackTranslator
    local foundPlayerTranslator = pcall(function()
    	playerTranslator = LocalizationService:GetTranslatorForPlayerAsync(player)
    end)
    local foundFallbackTranslator = pcall(function()
    	fallbackTranslator = LocalizationService:GetTranslatorForLocaleAsync(sourceLanguageCode)
    end)
    
    TranslationHelper.setSourceLanguage = function(languageCode)
    	if sourceLanguageCode ~= languageCode then
    		foundFallbackTranslator = pcall(function()
    			fallbackTranslator = LocalizationService:GetTranslatorForLocaleAsync(sourceLanguageCode)
    			sourceLanguageCode = languageCode
    			return true
    		end)	
    	end
    	return false
    end
    
    -- 翻译函数
    TranslationHelper.translate = function(text, object)
    	if not object then
    		object = game
    	end
    	local translation = ""
    	local foundTranslation = false
    	if foundPlayerTranslator then
    		return playerTranslator:Translate(object, text)
    	end
    	if foundFallbackTranslator then
    		return fallbackTranslator:Translate(object, text)
    	end
    	return false
    end
    
    -- 按键函数进行翻译 
    TranslationHelper.translateByKey = function(key, arguments)
    	local translation = ""
    	local foundTranslation = false
    	
    	-- 首先试图翻译至玩家语言（如果发现 Translator）
    	if foundPlayerTranslator then
    		foundTranslation = pcall(function()
    			translation = playerTranslator:FormatByKey(key, arguments)
    		end)
    	end
    	if foundFallbackTranslator and not foundTranslation then
    		foundTranslation = pcall(function()
    			translation = fallbackTranslator:FormatByKey(key, arguments)
    		end)
    	end
    	if foundTranslation then
    		return translation
    	else
    		return false
    	end
    end
    
    return TranslationHelper


```
如果你的游戏源语言不是英语，请将第 9 行的 `sourceLanguageCode` 值更改为**完全支持的**语言代码，该语言代码与本地化门户中的游戏**源语言**设置相匹配（请参阅下面的参考表）。 

##### 语言代码参考 »

下表概述了本地化门户中当前支持的语言。用黄色高亮显示的语言完全受 Roblox 平台/应用程序支持。

语言代码 语言

**de**
German
Deutsch

**en**
English
English

**es**
Spanish
Español

**fr**
French
Français

**jp**
Japanese
日本語

**ko**
Korean
한국어

**pt**
Portuguese
Português

**zh-hans**
Chinese (Simplified)
中文(简体)

**zh-hant**
Chinese (Traditional)
中文(繁體)

**bg**
Bulgarian
български

**bn**
Bengali
বাংলা

**bs**
Bosnian
босански

**cs**
Czech
Čeština

**da**
Danish
Dansk

**el**
Greek
ελληνικά

**et**
Estonian
Eesti

**fi**
Finnish
Suomi

**hi**
Hindi
हिन्दी

**hr**
Croatian
Hrvatski

**hu**
Hungarian
Magyar

**id**
Indonesian
Bahasa Indonesia

**it**
Italian
Italiano

**ka**
Georgian
ქართული

**kk**
Kazakh
қазақ тілі

**km**
Khmer
ភាសាខ្មែរ

**lt**
Lithuanian
Lietuvių

**lv**
Latvian
Latviešu

**ms**
Malay
Bahasa Melayu

**my**
Burmese
ဗမာစာ

**nb**
Bokmal
Bokmål

**nl**
Dutch
Nederlands

**fil**
Filipino
Filipino

**pl**
Polish
Polski

**ro**
Romanian
Română

**ru**
Russian
русский

**si**
Sinhala
සිංහල

**sk**
Slovak
Slovenčina

**sl**
Slovenian
Slovenski

**sq**
Albanian
Shqipe

**sr**
Serbian
српски

**sv**
Swedish
Svenska

**th**
Thai
ภาษาไทย

**tr**
Turkish
Türkçe

**uk**
Ukrainian
україньска

**vi**
Vietnamese
Tiểng Việt

  


## 收集资源 ID

若要实现本地化的资源，你应该首先收集每个版本的**资源 ID**，例如：

英语（源） 西班牙语 （es） 葡萄牙语 （pt）

rbxassetid://2957093606
rbxassetid://2957093671
rbxassetid://2957093727

![](https://developer.roblox.com/assets/blt4b9d240f8abb0b44/Localized-Image-en.png)


![](https://developer.roblox.com/assets/blt3e240e0d7aac3e0b/Localized-Image-es.png)


![](https://developer.roblox.com/assets/blt3ef00a5b2b44a665/Localized-Image-pt.png)



## 键和翻译

不要在 .csv 电子表格或本地化门户中提供字符串转换，而是输入相应资源的资源 ID。请记住，还要在 `LocalScript` 中提供用于查找的 **Key** （键）值，如以下部分所述。

A
B
C
D
E
F
G

**键**
上下文
**源**
示例
**es**
**pt**

Key_JewelsImage
2957093606
2957093671
2957093727

## 脚本实现

在继续之前，请确认：

  * **TranslationHelper** 脚本位于 `ReplicatedStorage` 中。
  * .csv 电子表格已上传到本地化门户，其中包含 “Key_JewelsImage” 键和与每个本地化图片关联的有效资源 ID。

为了进行测试，你可以 [下载](https://developer.roblox.com/assets/bltcac7145ef2354164/LocalizedImageTest.csv?disposition=attachment)包含西班牙语 (**es**) 和葡萄牙语 (**pt**) 的有效 ID 的测试电子表格，并将其上载到本地化门户，如`articles/localization portal additional features#upload-csv-file|此处`所述。 

现在将以下代码复制到一个新的 `LocalScript` 中。由于本教程涉及 GUI 图片，因此可以将脚本放在 `StarterGui` 中。

```    
    
    -- 静态变量
    local FALLBACK_IMAGE_ID = "924320031"
    
    -- Roblox 服务
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local Players = game:GetService("Players")
    
    -- 对翻译模块进行 Require
    local TranslationHelper = require(ReplicatedStorage:WaitForChild("TranslationHelper"))
    
    -- 创建新的屏幕 GUI
    local player = Players.LocalPlayer
    local playerGUI = player:WaitForChild("PlayerGui")
    local screenGUI = Instance.new("ScreenGui")
    screenGUI.Parent = playerGUI
    
    -- 创建新的图像标签
    local localizedImage = Instance.new("ImageLabel")
    localizedImage.Size = UDim2.new(0, 185, 0, 170)
    localizedImage.Position = UDim2.new(0, 40, 0, 40)
    localizedImage.BackgroundTransparency = 1
    localizedImage.Parent = screenGUI
    
    -- 从翻译模块处获取（Get）资源 ID
    local localizedImageID = TranslationHelper.translateByKey("Key_JewelsImage")
    
    -- 将资源 ID（或备用 ID）应用至图像标签
    local success, errorMessage = pcall(function()
    	localizedImage.Image = "rbxassetid://" .. localizedImageID
    end)
    if not success then
    	localizedImage.Image = "rbxassetid://" .. FALLBACK_IMAGE_ID
    	warn(errorMessage)
    end


```
在 Studio 中对你的游戏进行测试，如`articles/game testing#player-emulator|此处`所述，并为配置的语言/图片显示正确的图片。

![](https://developer.roblox.com/assets/blt186c6cc463a5a5b4/Localized-Image-Result-es.png)

 西班牙语

![](https://developer.roblox.com/assets/bltc448fd3075cd409e/Localized-Image-Result-pt.png)

 葡萄牙语



***__Roblox官方链接__:[本地化非文本实例](https://developer.roblox.com/zh-cn/articles/localizing-non-text-instances)