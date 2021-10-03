# Roblox Input Bindings 
Time:<em>5  分钟</em>

When choosing `enum/KeyCode|KeyCode` values for `ContextActionService`/`UserInputService` or detecting `Mouse` events, be aware that some bindings are reserved by Roblox, are mapped to a built-in feature, or are mapped to default controls. Unless you take precautions to avoid binding conflicts, these inputs should **not** be assigned to your game’s custom control bindings.

## Roblox-Reserved Bindings

The following bindings are **reserved by Roblox** and cannot be changed, disabled, or overridden.

Key Codes and Events Action

**Escape** `Enum.KeyCode.Escape`

Roblox menu

**F9** `Enum.KeyCode.F9`

`articles/Developer Console|Developer Console`

**F11** `Enum.KeyCode.F11`

Fullscreen mode

**F12** `Enum.KeyCode.F12`

Record video (Windows only)

**Control** \+ **Shift** \+ **F7** (Windows) `Enum.KeyCode.LeftControl`/`Enum.KeyCode.RightControl`  
+  
`Enum.KeyCode.LeftShift`/`Enum.KeyCode.RightShift`  
+  
`Enum.KeyCode.F7`

  


**Control** \+ **Alt** \+ **F7** (Mac) `Enum.KeyCode.LeftControl`/`Enum.KeyCode.RightControl`  
+  
`Enum.KeyCode.LeftAlt`/`Enum.KeyCode.RightAlt`  
+  
`Enum.KeyCode.F7`

Performance stats

**Control** \+ **F6** `Enum.KeyCode.LeftControl`/`Enum.KeyCode.RightControl`  
+  
`Enum.KeyCode.F6`

Show Microprofiler

**Control** \+ **P** `Enum.KeyCode.LeftControl`/`Enum.KeyCode.RightControl`  
+  
`Enum.KeyCode.P`

Pause Microprofiler, if showing

**PrintScreen** (Windows) `Enum.KeyCode.Print`

  


**Control** \+ **Shift** \+ **3** (Mac) `Enum.KeyCode.LeftControl`/`Enum.KeyCode.RightControl`  
+  
`Enum.KeyCode.LeftShift`/`Enum.KeyCode.RightShift`  
+  
`Enum.KeyCode.Three`

Take screenshot

## Default Player Bindings

These bindings are **Roblox defaults**, but you can override them via control scripts or `articles/Camera manipulation|camera scripts`. Note, however, that most Roblox players are accustomed to and familiar with these controls, so you should only override them in specific cases.

Key Codes and Events Action

**W** / **Up** `Enum.KeyCode.W`  
`Enum.KeyCode.Up`

Move forward

**S** / **Down** `Enum.KeyCode.S`  
`Enum.KeyCode.Down`

Move backward

**A** `Enum.KeyCode.A`

Move left

**D** `Enum.KeyCode.D`

Move right

**Space** `Enum.KeyCode.Space`

Jump

**Left** `Enum.KeyCode.Left`

Rotate camera left

**Right** `Enum.KeyCode.Right`

Rotate camera right

`Mouse/Button2Down`
Turn camera

**Shift** `Enum.KeyCode.LeftShift`/`Enum.KeyCode.RightShift`

Toggle mouselock (player setting if `StarterPlayer/EnableMouseLockOption|EnableMouseLockOption` is enabled)

`Mouse/WheelForward` / `Mouse/WheelBackward`
Zoom in/out

**I** `Enum.KeyCode.I`

Zoom in

**O** `Enum.KeyCode.O`

Zoom out

## Feature-Specific Bindings

These bindings are reserved unless you **disable the respective feature** via `StarterGui/SetCoreGuiEnabled|SetCoreGuiEnabled()`:

  * The **Backpack** bindings can be freed by setting `enum/CoreGuiType|Enum.CoreGuiType.Backpack` to `false`.
  * The **Chat** binding can be freed by setting `enum/CoreGuiType|Enum.CoreGuiType.Chat` to `false`.
  * The **Playerlist** binding can be freed by setting `enum/CoreGuiType|Enum.CoreGuiType.PlayerList` to `false`.

Key Codes and Events Feature Action

**Backquote** `Enum.KeyCode.Backquote`

Backpack
Backpack

**0** / **1** / **2** / **3** / **4** / **5** / **6** / **7** / **8** / **9** `Enum.KeyCode.Zero`  
`Enum.KeyCode.One`  
`Enum.KeyCode.Two`  
`Enum.KeyCode.Three`  
`Enum.KeyCode.Four`  
`Enum.KeyCode.Five`  
`Enum.KeyCode.Six`  
`Enum.KeyCode.Seven`  
`Enum.KeyCode.Eight`  
`Enum.KeyCode.Nine`

Backpack
Equip/unequip tools

`Mouse/Button1Down`
Backpack
Use tool

**Backspace** `Enum.KeyCode.Backspace`

Backpack
Drop tool

**Slash** `Enum.KeyCode.Slash`

Chat
Chat

**Tab** `Enum.KeyCode.Tab`

Playerlist
Show/hide player list



***__Roblox官方链接__:[Roblox Input Bindings](https://developer.roblox.com/zh-cn/articles/input-bindings)