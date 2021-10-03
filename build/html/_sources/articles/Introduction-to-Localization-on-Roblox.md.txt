# 本地化简介 
Time:<em>10  分钟</em>

Roblox 致力于促进我们玩家和开发者群体的成长。随着全球玩家数量的不断增长，**本地化**将更有助这些玩家理解和享受您的游戏作品。

## 本地化的目的

从核心上来说，本地化的目的就是让游戏的含义更加明确，并提高其对特定玩家群体的吸引力。世界上的每个地区都有其自己的文化、语言和习俗，所以您游戏中的按钮、说明、角色对话等内容，最好都能显示为地区特有的语言。

![](https://developer.roblox.com/assets/blt49b3373f6fe58022/Multilingual-Robot-Dance.jpg)

本地化不只是最基本的翻译，还意味着要在你的游戏当中使用**最贴切**的译文。你尽可以直接上网查找直白的逐字翻译，但是每一种文化都会有自己独特的辞藻能用来表达你真正想要传达的意思。 

## 本地化入门

在 Roblox 当中，本地化一款游戏涉及以下三个主要阶段：

**文本的采集和存储**
![](https://developer.roblox.com/assets/blt4e539ce26d011f16/r-arrow-blue.png)


**添加和管理译文**
![](https://developer.roblox.com/assets/blt4e539ce26d011f16/r-arrow-blue.png)


**使用译文**

如果您是初次接触本地化，请继续阅读探索基于云**的本地化平台**，即推荐的译文存储、管理和使用方法。

## 文本的采集和存储

要访问本地化平台，请导航至您的游戏主页，单击 ![](https://developer.roblox.com/assets/blt738fe32bb9c285f9/Config-Dots.png)

 按钮，然后从快捷菜单中选择 **Configure Localization（配置本地化）**。

![](https://developer.roblox.com/assets/bltc26a047d5f63e31c/Configure-Localization.png)



进入平台后，单击 **Settings（设置）** 选项卡并打开 **Automatic Text Capture（ATC - 自动文本捕捉）**。这样当任何人在 Roblox 上玩您的游戏时，就会对游戏内的字符串进行捕捉和存储。

![](https://developer.roblox.com/assets/bltf2271e5731d23224/LP-Enable-ATC.png)



##### ATC 使用准则

For ATC to detect in-game text and add it to the localization portal, note the following:

  * The game must be played in the **Roblox application**, not within Roblox Studio.
  * If the game is played from your account, it may take 1–2 minutes for ATC to inject text into the localization portal.

  


##### 逐个对象禁用 ATC

对于某些游戏内内容，你应当**禁用**自动文本捕捉。例如，ATC 无需追踪名为“Diva Dragonslayer”（角色名）的 NPC 上方 `BillboardGui` 上的 `TextLabel`，因为她的名字不会随语言的不同而改变。

要禁用特定 `GuiBase2d|GUI` 对象上的自动文本捕捉，请在 Studio 中取消选中其 `GuiBase2d/AutoLocalize|AutoLocalize` 属性，或是在脚本中将其设为 `false`。

  


## 添加和管理译文

你应当先在 **Languages** （语言）部分中将 **Game Source Language（游戏源语言）**设为 Roblox 上完全支持的语言之一。

![](https://developer.roblox.com/assets/blt12a20377bc49c831/LP-Source-Language.png)



下面，在紧接着的 **Translated Languages** （翻译语言）部分中，单击 **Add Language（添加语言）**字段并从菜单中选择一种语言。

![](https://developer.roblox.com/assets/blt6053dac5e5eff0c8/LP-Select-Language.png)



添加到列表后，单击特定语言后会打开 **Manage Translations（管理译文）**页面，可以在其中管理你的译文。

![](https://developer.roblox.com/assets/blt259ed0336e964470/LP-Translation-Manager.png)



**A**

通过自动文本捕捉或手工输入采集的游戏内**源文本字符串**列表。绿色指示表示已经为选定语言添加了一条译文，而灰色指示则表示不存在译文。 

**B**

将要用于所选定语言的本地化译文。 

**C**

在其中找到了字符串的游戏内 GUI 对象列表。 

**D**

对特定项目进行的更改日志（历史）。若您使用所选语言的自动翻译，机器翻译的记录会出现在此。 

## 自动翻译

目前，**自动机器翻译**已面向指定测试人员开放，届时此功能将向所有开发者开放。根据您之前选择的**游戏源语言**，启用支持语言的自动翻译的开关会显示：

![](https://developer.roblox.com/assets/blt560255811afec38f/Auto-Translation-Toggle.png)



目前有以下自动翻译可用：

源语言 目标语言

**英语**
简体中文
法语
日语
葡萄牙语

繁体中文
德语
韩语
西班牙语

请注意，自动翻译永远不会覆盖人工翻译。任何已有的人工翻译都将保持不变，只有尚无翻译的条目会被填充。 

## 使用译文

当你准备好在自己的游戏当中使用翻译好的内容后，返回平台的 **Settings** （设置）部分并启用 **Use Translated Content（使用翻译内容）**。

![](https://developer.roblox.com/assets/bltec06ab0a13ebd01f/LP-Use-Translated-Content.png)



启用后，你就可以直接在 Roblox Studio 内按`articles/game testing#player-emulator|游戏测试模式`中的叙述测试译文了。

请注意，如果您在此时发布游戏，译文将会应用到游戏的发行中版本。 

* * *

从这里开始，如需设置游戏标题和描述翻译、或让其他翻译者协助翻译工作等，请参阅`articles/localization portal additional features|本地化平台 – 其他功能`一文。



***__Roblox官方链接__:[本地化简介](https://developer.roblox.com/zh-cn/articles/Introduction-to-Localization-on-Roblox)