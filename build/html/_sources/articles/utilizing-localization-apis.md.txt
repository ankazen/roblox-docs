# 使用本地化 API 
Time:<em>5  分钟</em>

在必要时，开发者可以使用脚本来获取那些添加到`articles/Introduction to Localization on Roblox|本地化门户`中的翻译并将其格式化。

## 加载一个翻译器

当开发者准备使用 API 来进行翻译时，应该先要获取一个 `Translator` 实例。

### 玩家区域设置

当 `LocalizationService/GetTranslatorForPlayerAsync|GetTranslatorForPlayerAsync()` API 针对 `Players/LocalPlayer|LocalPlayer` 属性进行调用时，会得到一个用于玩家 Roblox 账户所设置语言的 `Translator` 。

```    
    
    local LocalizationService = game:GetService("LocalizationService")
    
    local success, translator = pcall(function()
    	return LocalizationService:GetTranslatorForPlayerAsync(game.Players.LocalPlayer)
    end)
    
    if success then
    
    else
    	warn("无法为玩家加载翻译器！")
    end


```
### 特定区域设置

如果开发者实现了一个自定义游戏选项来让玩家选择他们最喜欢的语言，那么就能通过 `LocalizationService/GetTranslatorForLocaleAsync|GetTranslatorForLocaleAsync()` 来为Roblox 所支持的语言码获取一个 `Translator` 。

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

  


```    
    
    local LocalizationService = game:GetService("LocalizationService")
    
    local success, translator = pcall(function()
    	return LocalizationService:GetTranslatorForLocaleAsync("es")
    end)
    
    if success then
    
    else
    	warn("无法为玩家加载翻译器！")
    end


```
注意 `LocalizationService/GetTranslatorForPlayerAsync|GetTranslatorForPlayerAsync()` 和 `LocalizationService/GetTranslatorForLocaleAsync|GetTranslatorForLocaleAsync()` 都是异步运行，所以可能会因为连接不稳定或者其他原因而导致运行失败，因此一定要将它们和 `pcall` 嵌套并实现错误处理功能，如下所示。 

## Translate()

当一个合法的 `Translator` 加载完毕后，`Translator/Translate|Translate()` 函数就可以从本地化门户中基于其 **Source** 字符串和一个游戏内 `Instance` 来取回翻译。注意 `Instance` 参数可能是任意参数，除非开发者要求进行[上下文 覆盖](/api-reference/function/Translator/Translate#translate-context-overrides)。

A
B
C
D
E

Key（键）
Context（上下文）
**Source（原文）**
Example（示例）
**es**

Screen
Pantalla

```    
    
    if success then
    	local translation = translator:Translate(game, "Screen")
    	print(translation)
    else
    	warn("无法为玩家加载翻译器！")
    end
    
    
    Pantalla

```
如果开发者用一个**不**存在于本地化门户中的源文本字符串去调用 `Translator/Translate|Translate()` ，那么该字符串就会自动被添加到门户（以及可下载的 .csv 电子表格）中，翻译人员就可以找到它并进行翻译。 

## FormatByKey()

当 `Translator/FormatByKey|FormatByKey()` 对一个有效合法的 `Translator` 进行调用时，它会从本地化门户中基于一个针对源项的标识符 **key** （键）来获取翻译。标识符键只能被输入到可下载的电子表格 **Key** 列中或者输入到门户中的直接条目里，无法通过 Roblox 应用中的自动文本捕捉来进行侦测或添加。

##### 输入键 »

如果你更喜欢使用 .csv `articles/localization portal additional features#localizing-with-csv-files|电子表格`管理译文，则可以在 **Key** 列输入标识符键：

A
B
C
D
E

**键**
上下文
原文
示例
es

Key_StartButton
Start
Iniciar

Key_OptionsButton
Options
Opciones

或者，你可以通过以下步骤，直接在本地化门户中输入基于键的条目：

  1. 在门户中的 **Manage Translations（管理译文）**页面上，单击 **Add New Entry（添加新条目）**按钮。
![](https://developer.roblox.com/assets/bltb96d211b1f744953/LP-Add-New-Entry.png)



  2. 指定 **Text to Translate（待译文字）**（将成为电子表单中的**原文**）和**键**值。
  3. 单击 **Save（保存）**按钮将条目添加至门户。

  


如果要在一个脚本中使用 `Translator/FormatByKey|FormatByKey()` ，用一个从本地化门户中获取到的有效的键名称来调用 API 。比如下列编码示例的第 9 行的 `print()` 语句将在开发者在西班牙语环境中进行`articles/game testing#player-emulator|游戏测试`时输出对应键为 “Key_Prize” 的西班牙语翻译 “joyas”。

A
B
C
D
E

**Key（键）**
Context（上下文）
Source（原文）
Example（示例）
**es**

Key_Prize
jewels
joyas

```    
    
    if success then
    	local keyTranslation = translator:FormatByKey("Key_Prize")
    	print(keyTranslation)
    else
    	warn("无法为玩家加载 translator ！")
    end
    
    
    joyas

```
## 使用格式化字符串

本地化 API 可以和`/articles/localization format strings|格式化字符串`一起使用来返回带有变量数据的翻译内容。此方法仅取决于格式化字符串为**已编号**还是**已命名**。

### 已编号格式化字符串

下列翻译数据中含有**已编号**的格式化字符串，比如 **{1:int}**：

A
B
C
D
E

**Key（键）**
Context（上下文）
**Source（原文）**
Example（示例）
**es**

Key_Prize_1
{1:int} jewels
{1:int} joyas

Key_Prize_2
${1:fixed} cash and {2:int} jewels
${1:fixed} dinero y {2:int} joyas

要将这些数据格式化为带有变量金额的现金和/或珠宝，请将数量传入一个以逗号分隔的 Lua 数组之中，以该数组作为 `Translator/FormatByKey|FormatByKey()` 的第二个参数。再使用西班牙语进行`articles/game testing#player-emulator|游戏测试`时，`print()` 语句就会输出正确的翻译。

```    
    
    if success then
    	local keyTranslation1 = translator:FormatByKey("Key_Prize_1", {100})
    	print(keyTranslation1)
    	local keyTranslation2 = translator:FormatByKey("Key_Prize_2", {500, 100})
    	print(keyTranslation2)
    else
    
    
    100 joyas
    $500.00 dinero y 100 joyas

```
### 已命名的格式化字符串

在处理**已命名**格式化字符串（比如 **{NumJewels:int}** ）时，将一个含有多个键值对的表格作为第二个参数传入 `Translator/FormatByKey|FormatByKey()`，每个键值对中是一个格式化字符串的名称和要替换的值。

A
B
C
D
E

**Key（键）**
Context（上下文）
**Source（原文）**
Example（示例）
**es**

Key_Prize_1
{NumJewels:int} jewels
{NumJewels:int} joyas

Key_Prize_2
{AmountCash:fixed} cash and {NumJewels:int} jewels
{AmountCash:fixed} dinero y {NumJewels:int} joyas

```    
    
    if success then
    	local keyTranslation1 = translator:FormatByKey("Key_Prize_1", {NumJewels=100})
    	print(keyTranslation1)
    	local keyTranslation2 = translator:FormatByKey("Key_Prize_2", {AmountCash=500, NumJewels=100})
    	print(keyTranslation2)
    else
    
    
    100 joyas
    $500.00 dinero y 100 joyas

```
## 最佳做法

### 禁用 AutoLocalize

在使用本地化 API 时，最好禁用使用译文对象的 `GuiBase2d/AutoLocalize|AutoLocalize`。例如：

情景 禁用 AutoLocalize 的原因

在 NPC 头顶上方的 `BillboardGui` 中显示 NPC 专有名称。
NPC 的名字在各国语言中保持不变，因此 Studio's 的自动文本捕捉功能无法捕获 NPC 名字。

从门户中获取一段译文并用“打字机”效果以逐字母的方式显示。
防止 Studio 的自动文本捕捉功能捕捉不完整的词语并将其添加至门户。

要禁用某个特定 GUI 对象的 自动本地化功能，需要在 Studio 中取消选中它的 `GuiBase2d/AutoLocalize|AutoLocalize` 属性或者在一段脚本中将其设置为 `false` 。

### 错误处理

下面的帮助模块可以捕获到开发者本地化条目中可能存在的问题并处理基于网络的函数在获取 `Translator` 时可能会引发的错误。 要在游戏中使用此功能，请执行以下操作：

  1. 在 `ReplicatedStorage` 中创建新的 `ModuleScript`。
  2. 将新脚本重命名为 _TranslationHelper_。
  3. 将下列编码复制到脚本中。

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
如果游戏的原文并非英文，请将第 9 行的 `sourceLanguageCode` 值更改为**获得充分支持的**语言码，该语言码与本地化门户中游戏的**原文 语言**设置必须一致。请参阅上方的游戏码参考 表，了解可接受选项。 

将模块放入 `ReplicatedStorage` 后，就可以从 `LocalScript` 中进行 `require()` 处理，如下面第 5 行所示。之后如有需要，可随时调用模块的 `translate()` 函数（等效于 `Translator/Translate|Translate()` ）或者 `translateByKey()` 函数（等效于 `Translator/FormatByKey|FormatByKey()`）。

```    
    
    -- Roblox 服务
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    
    -- 对翻译模块进行 Require
    local TranslationHelper = require(ReplicatedStorage:WaitForChild("TranslationHelper"))
    
    local sourceTranslation = TranslationHelper.translate("Source_String")
    local keyTranslation = TranslationHelper.translateByKey("Key_Name")


```


***__Roblox官方链接__:[使用本地化 API](https://developer.roblox.com/zh-cn/articles/utilizing-localization-apis)