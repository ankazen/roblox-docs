# Avatar Emotes 
Time:<em>opt-in</em>

In addition to the default `articles/Lua Chat System|chat` and opt-in `articles/Avatar Context Menu|Avatar Context Menu`, Roblox players can express what they’re feeling through **emotes**.

Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link](/zh-cn/assets/blt51bf60023e6396b7/Emotes.mp4) to the video instead. 

Depending on the platform, the emote menu can be opened as follows:

Platform Method

PC / Mobile
Click/tap the ![](https://developer.roblox.com/assets/blt2ee60d0984800c91/Emotes-Menu-Icon.png)

 button from the top menu bar.

Console
Access it from the radial menu.

## Controlling the Emotes Menu

### Customizing the Menu

The emotes menu can be customized by loading and “equipping” emotes from the [catalog](https://www.roblox.com/catalog/?Category=12&Subcategory=39). In a script, this can be done by calling `HumanoidDescription/SetEmotes|SetEmotes()` on a player’s `HumanoidDescription` object. Once set, specific emotes can be equipped via the `HumanoidDescription/SetEquippedEmotes|SetEquippedEmotes()` API.

Consider the following example which may be placed in a `LocalScript` within `StarterCharacterScripts`:

```    
    
    local Players = game:GetService("Players")
    local humanoid = Players.LocalPlayer.Character.Humanoid
    local humanoidDescription = humanoid.HumanoidDescription
    
    -- 加载自定义表情
    local emoteTable = {
    	["Hello"] = {3576686446},
    	["Stadium"] = {3360686498},
    	["Tilt"] = {3360692915},
    	["Shrug"] = {3576968026},
    	["Salute"] = {3360689775},
    	["Point"] = {3576823880}
    }
    humanoidDescription:SetEmotes(emoteTable)
    
    -- 以指定顺序装备表情
    local equippedEmotes = {"Hello", "Stadium", "Tilt", "Shrug", "Salute", "Point"}
    humanoidDescription:SetEquippedEmotes(equippedEmotes)


```
##### 设置说明

  * `emoteTable` 内的 `["Shrug"]` 或 `["Salute"]` 等键名称是可以自定义的。当玩家浏览菜单选项时，这些键名称将出现在表情菜单的中心。
  * `equippedEmotes` 表中键名称的顺序定义了菜单中表情的显示顺序，从第一个位置（轮盘顶部）开始按顺时针顺序排列。
  * 表情菜单包含 8 个位置。如果您没有 8 个要加载的自定义表情，请考虑重复一些键，用总共 8 个条目填充 `equippedEmotes` 表，以确保菜单中没有空位。

  


### Opening/Closing the Menu

To forcibly open or close the emotes menu, call `GuiService/SetEmotesMenuOpen|GuiService:SetEmotesMenuOpen()` with a boolean value of `true` or `false`.

```    
    
    -- 打开表情菜单
    local GuiService = game:GetService("GuiService")
    GuiService:SetEmotesMenuOpen(true)


```
If you need to detect whether the emotes menu is open, call `GuiService/GetEmotesMenuOpen|GuiService:GetEmotesMenuOpen()`. This will return a boolean indicating the menu's current state. 

### Disabling the Menu

The emotes menu can be disabled via the `StarterGui/SetCoreGuiEnabled|StarterGui:SetCoreGuiEnabled()` API. Note, however, that disabling the menu will **not** prevent emotes from being performed with an `articles/Lua Chat System|admin command`.

```    
    
    local StarterGui = game:GetService("StarterGui")
    StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.EmotesMenu, false)


```
##### 禁用用户表情

除了禁用菜单外，您还可以通过关闭 **StarterPlayer** → **Character** 中的 **UserEmotesEnabled** 选项来禁用**用户已拥有**表情的加载。请注意，此属性只能在 Studio 中设置，不能在运行时由脚本设置，但它可以由脚本读取。

  


## Playing Emotes

To explicitly play an emote that a character has in its `HumanoidDescription`, call the `Humanoid/PlayEmote|Humanoid:PlayEmote()` API, passing the string name of the emote. This call will return `true` to indicate that the emote was played successfully, or `false` otherwise.

```    
    
    local Players = game:GetService("Players")
    local humanoid = Players.LocalPlayer.Character.Humanoid
    
    humanoid:PlayEmote("Shrug")


```


***__Roblox官方链接__:[Avatar Emotes](https://developer.roblox.com/zh-cn/articles/avatar-emotes)