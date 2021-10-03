# 本地化门户：扩展功能 
Time:<em>10  分钟</em>

除了在`articles/Introduction to Localization on Roblox|本地化简介`教程中介绍过的功能，你还能在本地化门户中设置已翻译的游戏标题/描述、上传本地化图标与缩略图、以及指定其他译者为你提供帮助等。

##### 提醒 – 访问本地化门户 »

要访问本地化门户，请导航到游戏的主页，单击 ![](https://developer.roblox.com/assets/5b96ee6b46674ff33ad964fd/Config-Dots.png)

 按钮，然后从上下文菜单中选择 **Configure Localization（配置本地化）**。

![](https://developer.roblox.com/assets/5d1675537757f569bc972d95/Configure-Localization.png)



  


## 本地化游戏信息

除了游戏内文本本地化之外，Roblox 还允许你对游戏标题及描述进行指定本地化。同时，你也可以为任何支持语言上传对应的独特`articles/Game Icons Tips|游戏图标`与`articles/Thumbnail|游戏缩略图`。只需前往 **Languages**（语言） → **Manage Translations** （管理译文）后，选择 **Game Information**（游戏信息）即可进行设置。

![](https://developer.roblox.com/assets/bltd7c5c358d9e1ee24/LP-Game-Information.png)



### 标题和描述

要设置本地化的游戏标题和描述，请执行以下操作：

  1. 在左列中点击 **Name**（名称）或 **Description**（描述），键入与在右上角下拉菜单中选择语言相符的译文。
  2. 完成修改后，点击 **Save**（保存）。
  3. 如果想要查看所做出的的修改，请向下滚动至游戏主页的最下方，找到语言选择框并选择添加本地化名称与描述的语言。
![](https://developer.roblox.com/assets/bltafe748534876b33c/Translation-Selection.png)



请注意，无法在此页面上编辑源语言名称/描述。要对其进行编辑，请在 Roblox Studio 中使用`articles/game settings|游戏设置`窗口的 **Basic Info**（基本信息）部分。 

### 游戏图标

要上传各种语言的唯一游戏图标，请执行以下操作：

  1. 在左列中点击 **Icon**（图标）。
  2. 在右上角下拉菜单中确认选择的语言正确无误。
  3. 在图标图像框中进行单击，然后从计算机中选择图像文件。
  4. 完成上传后，单击 **Save**（保存）。

### 游戏缩略图

要上传本地化过的游戏缩略图，请执行以下操作：

  1. 在左列中点击 **Thumbnails**（缩略图）。
  2. 在右上角下拉菜单中确认选择的语言正确无误。
  3. 在缩略图图像框中进行单击，然后从计算机中选择图像文件。
  4. 如果希望上传多个缩略图，可以选择最多 10 个图像文件进行上传。
  5. 完成上传后，单击 **Save**（保存）。

## 对游戏产品进行本地化

如果希望对`/articles/Badges Special Game Awards|徽章`等游戏产品进行本地化，请前往 **Languages** （语言）→ **Manage Translations** （管理译文），选择 **Game Products**（游戏产品）进行设置。

![](https://developer.roblox.com/assets/blte293785f16ce3101/LP-Game-Products.png)



在目标页面中，游戏产品应当在左列进行陈列。要对产品进行本地化，请执行以下操作：

  1. 单击产品名称，对其进行展开。
![](https://developer.roblox.com/assets/blt161bedae52241efe/LP-Expand-Game-Product.png)



  2. 在面板右方的输入框中输入翻译过的产品名称。
  3. 完成输入后，点击 **Save**（保存）。
  4. 单击 **Description**（描述）按钮，重复同样步骤。
![](https://developer.roblox.com/assets/blt0be8046d71b87aef/LP-Game-Product-Description.png)



目前只能进行徽章的本地化，但其它游戏产品将会陆续加入本地化门户，敬请期待。 

## 清除未翻译的字符串

在某些情况下，**自动文本捕获（ATC）** 将从对象（理想情况下，应已在游戏中翻译）中捕获源文本字符串，方法是禁用 `GuiBase2d/AutoLocalize|AutoLocalize` 属性并通过`articles/utilizing localization apis|本地化 API` 进行管理。

要清除没有任何有效翻译的源文本字符串，请单击门户的 **Settings**（设置）部分中的 **Clear**（清除）按钮：

![](https://developer.roblox.com/assets/blt525e2afab349d072/LP-Clear-Untranslated.png)



## 添加其他译者

翻译为不熟悉的语言时，你可能希望指定其他 Roblox 用户（允许这些用户将译文添加到游戏）。

  1. 在门户的 **Translators**（译者）部分中，选择是否要按 **Username** （用户名）、**User ID** （用户 ID）或 **Group ID** （组 ID）添加译者。

可在个人资料页面的 URL 中找到用户的 ID，例如： 

https://www.roblox.com/users/012345678/profile

同样，可在组的主页的 URL 中找到 Roblox 组 ID： 

https://www.roblox.com/groups/1234567/

  2. 输入用户名或 ID，然后单击“添加”图标。
![](https://developer.roblox.com/assets/blt4e001a32f607ed7a/LP-Add-Translator.png)



  3. 准备好后，向译者发送指向 [Translator Portal （译者门户页面）](https://www.roblox.com/translator-portal)的链接。在该页面上，译者可以查看其有权限进行翻译的所有游戏。在页面右上角的选择菜单中选择目标语言后，也可以查看当前语言的翻译进度（百分比）。
![](https://developer.roblox.com/assets/blte4be6bceadf7a1d8/Translator-Portal.png)



## 翻译分析

为了查看整个游戏的本地化进程，你可以下载两月一次的翻译报告，其中包含如下数据：

  * 源字符串总数以及已为每种语言翻译的数量/百分比。
  * 关每个译者及其贡献的信息。
  * 译者贡献的本年迄今分析。

要下载报告，请访问门户的 **Reports**（报告）部分，选择日期范围，然后单击 **Download**（下载）按钮。报告将会以 .csv 电子表格形式下载，可以使用自选应用程序查看。

## 使用 CSV 文件进行本地化

如果译者无权访问本地化门户或不想对其进行使用，可以下载 .csv 文件进行编辑，然后上传具更改完毕的文件以进行本地化。

要下载 .csv 电子表格，请执行以下操作：

  1. 在 Roblox Studio 中，单击 **Plugins**（插件）选项卡 **Localization**（本地化）部分中的 **Tools**（工具）按钮。
![](https://developer.roblox.com/assets/blt762e59f7a48df1ca/Localization-Tools-Button.png)



  2. 在本地化工具窗口的 **Cloud Localization Table**（云本地化表）下，单击 **Download table as CSV**（下载为 CSV）旁的下载按钮。

### 编辑电子表格

在电子表格中，前四列如下：

列 描述

**Key（键）**
使用`articles/utilizing localization apis|本地化 API` 实现脚本中基于键的查找的自定义键。 

**Context（上下文）**
可用于提供[上下文替代](/api-reference/function/Translator/Translate#translate-context-overrides)的 `Instance` 参考。

**Source（源）**
由自动文本捕获或手动输入收集的游戏内**源文本字符串**。

**Example（示例）**
这会被自动本地化忽略，并且可用于向人工译员提供附加注释，例如有关文本中引用的 NPC 的详细信息、不应翻译的游戏特定术语等。

A
B
C
D
E
F
G

**Key**
**Context**
**Source**
**Example**

Options

Start

要为你的游戏指定翻译，译者应添加正在翻译的语言的**语言代码列**，例如 **es** 或 **pt**（请参阅下面的语言代码参考表）。在该列中，**源**列中的源文本字符串应互相对应以便提供正确的翻译。

A
B
C
D
E
F
G

Key
Context
**Source**
Example
**es**
**pt**

Options
Opciones
Opções

Start
Iniciar
Iniciar

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

  


### 上传与测试

完成游戏所有翻译、获得完整 .csv 文件后，可以通过 Roblox Studio 对其进行上传。

  1. 在本地化工具窗口的**云本地化表**下，单击 **Update with new content from CSV**（使用 CSV 中的新内容进行更新）旁边的更新按钮。
  2. 选择 .csv 文件并查看确认窗口中的详细信息。如果所有内容看起来都正确，请单击**确认**按钮以上传更新后的电子表格。
  3. 表格上传后，你可以直接在 Roblox Studio 中对本地化后的游戏进行测试，详见`articles/game testing#player-emulator|游戏测试模式`。

请注意：如果此时发布游戏，翻译将应用于游戏的已发布版本。 



***__Roblox官方链接__:[本地化门户：扩展功能](https://developer.roblox.com/zh-cn/articles/localization-portal-additional-features)