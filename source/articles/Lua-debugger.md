# 使用 Lua 调试器 
Time:<em>10  分钟</em>

**Lua 调试器**为 Lua 环境下的调试工具，旨在为 Roblox 开发者提供任何 IDE（集成开发环境）中应有的实用工具。默认情况下，调试器处于启用状态。开发者可以通过 Roblox Studio 的 **Settings（设置）**菜单对其进行启用或禁用。

![](https://developer.roblox.com/assets/bltf5d60f4defe65691/Enable-Lua-Debugger.png)



## 调试器的作用

调试器能够帮助开发者检查其代码是否正常运行，是十分有用的工具。部分调试器功能可以使用 `print()` 语句（执行特定代码时验证）进行复制，但开发者可以在不修改代码的前提下通过调试器将 **Breakpoint**（断点）置于其脚本中。拥有断点的应用程序将在断点处停止，以便开发者检查程序状态或断点处特定变量的值。

## 断点

断点是脚本内的“保存点”。为代码行设置断点后，运行中的 Roblox 游戏在尝试执行该代码行时将会暂停。

要设置脚本内的断点，请执行以下操作：

  1. 在 Roblox Studio 内打开脚本。
  2. 单击脚本内需要暂停执行的代码行左侧，创建指示断点的红点。
![](https://developer.roblox.com/assets/bltc8e67419d22afb9f/Create-Breakpoint.png)



需要移除断点时，单击该行左侧红点即可。 

### 检查断点

单击 **View（视图）**选项卡中的 **Breakpoints（断点）**后，开发者可以浏览其所设置过的所有断点。此操作将会打开 **Breakpoints（断点）**窗口，该窗口的功能包括对特定断点或所有断点进行启用与禁用、移除断点，以及查看每个断点所在的脚本。

### 逐步执行代码

脚本在断点处暂停后，开发者可以选择逐行继续执行脚本，以便密切监视变量更改以及函数调用。逐步执行代码的方式共有三种，均位于 **Script Menu（脚本菜单）**选项卡中：

按钮 操作 描述

![](https://developer.roblox.com/assets/blt1d4efb493e0111b8/Step-In.png)


**Step Into（单步跳入）**
**单步跳入**按钮可将调试器移动到当前行上的函数中。如果当前行上没有函数，调试器将移动到下一行。

![](https://developer.roblox.com/assets/blt16bc1bc580d6c5f2/Step-Over.png)


**Step Over（单步跳过）**
**单步跳过**按钮可将调试器移动到下一行代码，而**不是**移动到函数中。

![](https://developer.roblox.com/assets/bltbbfdf1cb53d5475f/Step-Out.png)


**Step Out（单步跳出）**
**单步跳出**按钮可将调试器移出当前函数并移动到起始函数调用的下一行代码。如果当前行不在函数内，此按钮将移动到下一行。

Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link](/zh-cn/assets/bltc3e1ecac6b6f7667/CodeStepVideo2.mp4) to the video instead. 

## 监视变量

除了设置断点之外，开发者还可以指示调试器对变量进行“监视”变量，从而在遇到断点时检查变量的值。要将变量添加到监视列表，只需使其高亮显示后单击 **Script Menu（脚本菜单）**选项卡中的 **Add Watch（添加监视）**按钮即可。此操作将会打开 **Watch（监视）**窗口，开发者在逐步执行断点时可以从该窗口中监视变量值。

![](https://developer.roblox.com/assets/bltc234fe9996f15cc9/Watch-Variable.png)



同时，开发者还可以通过单击 **Add Watch（添加监视）**按钮并输入变量名称来对其值进行监视。 

## 调用堆栈

**View（视图）**选项卡中的 **Call Stack（调用堆栈）**窗口可以告知开发者游戏当前在代码中的确切位置（当暂停或位于在断点处时）。如果当前代码行存在于从其他函数调用的某个函数中，堆栈将显示函数的调用顺序以及进行调用的行号。

![](https://developer.roblox.com/assets/blt16377ea05a08669d/Call-Stack.png)





***__Roblox官方链接__:[使用 Lua 调试器](https://developer.roblox.com/zh-cn/articles/Lua-debugger)