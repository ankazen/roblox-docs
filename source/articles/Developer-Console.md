# 开发者控制台 
Time:<em>5  分钟</em>

测试游戏时，查看游戏产生的输出和错误非常有用。在 Roblox Studio 中运行时，**输出**窗口会显示这些消息，但在测试游戏的实时运行版本时，应使用**开发者控制台**访问输出消息和许多其他详细信息。

## 打开控制台

根据平台的不同，可以按如下方式打开开发者控制台：

平台 方法

Windows / Mac
按 F9 键。

移动设备（手机或平板电脑）
在聊天中输入 `/console` 或从游戏中的 **Settings（设置）** 菜单打开控制台。

## 控制台部分

控制台顶部是一个快捷栏，显示严重错误和警告的数量、客户端内存使用情况以及平均 ping 的时间。单击这些项目中的任何一个都将在控制台中显示相关的详细信息。

![](https://developer.roblox.com/assets/bltb17e790bf8d5e8a1/Console-Summary-Bar.png)



快捷栏下方有一系列选项卡，其中信息最丰富的是 **Log** （日志）、**Memory** （内存）和 **Network** （网络）。

### 日志

**Log** （日志）部分显示游戏中的脚本的诊断消息，按 **Client** （客户端）或 **Server** （服务器）分类。

![](https://developer.roblox.com/assets/blt0dd4dfd7840168b0/Console-Log-Client-Server-Toggle.png)



  * 客户端上运行的 `LocalScript|LocalScripts` 的输出将显示在控制台的 **Log** （日志）→ **Client** （客户端）部分。运行游戏的任何人都可以查看这些本地输出消息。
  * Roblox 的服务器上运行的 `Script|Scripts` （脚本）输出将显示在控制台的 **Log** （日志）→ **Server** （服务器）部分。只有游戏的所有者或具有编辑权限的团队成员才能访问此部分。

通过切换以下复选框，还可以筛选日志中的输出消息：

![](https://developer.roblox.com/assets/bltb3529923660dd862/Console-Filter-Options.png)



**输出**
通过在游戏的脚本中调用 `print()` 语句生成的消息。

**信息**
游戏生成的非错误或自定义输出语句的消息。

**警告**
表示是潜在问题但不是关键问题的消息。

**错误**
表示发生了严重事件的消息。

最后，**Log** （日志）→ **Server** （服务器）部分包含一个**命令栏**，允许游戏的编辑器运行任意 Lua 代码。请注意，此命令栏具有与 `Script|Scripts` （脚本）和 `LocalScript|LocalScripts` 相同的安全限制，这意味着它与 Studio 中的命令栏不同，它无法运行受保护的函数。

![](https://developer.roblox.com/assets/blt30a926434d64eac9/Console-Command-Bar.png)



### 内存

模型、地形、部件、视觉效果、脚本、物理设备、音频等都会影响总内存使用。控制台的 **Memory** （内存）部分显示有关游戏内存使用情况的指标。

在视图中，总内存分为三类：

  * **CoreMemory** — 由 Roblox 引擎内置的进程（如网络、虚拟角色、GUI 元素等）使用的内存。
  * **PlaceMemory** — 构建游戏时由于直接选择而扩展的内存。
  * **UntrackedMemory** — 未标记的任意内存分配。

##### 内存管理提示 »

**PlaceMemory** 分为几个子类别。下表提供了每个子类别的简要描述和减少内存使用的提示。

类别 描述 内存管理提示

**HttpCache**
从 Roblox 服务器加载的资源（图像、网格等）现在保存在内存的缓存中。
加载更少或更小的资源。

**Instances**
场景中的 `Instances`。
如果可能，请减少 Instances（管理器窗口中的对象）的总数。

**Signals**
在 Instances 之间触发的信号（在一个 Instance 上触发事件以在另一个 Instance 上触发事件）。
在 Instances 之间使用较少的事件连接。

**LuaHeap**
核心脚本（Roblox 客户端附带的脚本）和自定义脚本的堆内存。
编写节省内存的脚本。

**Script**
Lua 脚本。
使用更少或更短的脚本。

**PhysicsCollision**
物理模拟的碰撞数据。
如果部件不需要移动，请将 `BasePart/Anchored|Anchored` 设置为 **true**。如果不需要与任何东西（包括玩家）碰撞，请将 `BasePart/CanCollide|CanCollide` 设置为 **false**。

**PhysicsParts**
物理几何学和动力学。
使用更简单、更小或更少的部件。

**GraphicsSolidModels**
要呈现`articles/3D Modeling with Parts|实体模型`的物理数据
使用更少/更简单的实体模型，或将它们的 `enum/RenderFidelity` 设置为**自动**。

**GraphicsMeshParts**
`MeshPart|MeshParts` 的图形。
使用更少/更简单的`articles/Mesh Parts|网格`。

**GraphicsParticles**
粒子系统的图形。
使用更少的粒子系统或产生更少的寿命较短的粒子。

**GraphicsParts**
部件的图形。
使用更少/更简单的部件。

**GraphicsSpatialHash**
常规渲染。
使用更少的部件、粒子和灯光（本质上是任何有助于渲染的内容）。

**GraphicsTerrain**
地形的图形。
使用更少的地形。

**GraphicsTexture**
纹理内存。
使用更少或更小的纹理。

**GraphicsTextureCharacter**
角色的纹理内存。
使用更少的独特角色外观。

**Sounds**
内存中的声音。
使用更少或更小的声音。

**StreamingSounds**
流媒体声音。
使用更少的流媒体声音。

**TerrainVoxels**
地形体素。
使用更少的地形。

**TerrainPhysics**
地形物理学。
对于靠近地形的对象，将 `BasePart/CanCollide|CanCollide` 设置为 **false** 和/或将 `BasePart/Anchored|Anchored` 设置为 **true**。

**Gui**
通用 GUI 元素使用的内存。
减少或优化你的 GUI 实例使用。

**Animation**
用于动画数据的内存（姿势和 `KeyframeSequence` 缓存的数据），通常是虚拟角色动画。
尽可能少使用不同的动画并优化动画。

**Navigation**
`PathfindingService` 的支持结构使用的内存。
优化使用并减少对 `PathfindingService` 的调用

  


### 网络

本部分揭示了游戏在运行时进行了多少次网络调用，包括通过 `HttpService` 进行的显式调用和由 Roblox 服务（如 DataStoreService）进行的网络请求。

顶部附近是按类型分类的游戏网络调用 **Summary（摘要）**。每种类型都包含有关请求次数、请求失败次数和时间统计信息的详细信息。

摘要下方是 **Details（详细信息）**部分，其中列出了每个单独的网络调用。每行显示 HTTP 方法（GET、POST 等） 以及状态代码、执行的时间、请求类型和请求 URL。单击列表中的任何行都会显示响应详细信息，例如：

![](https://developer.roblox.com/assets/blt5fda94fb79527d74/Console-Network-Response-Detail.png)





***__Roblox官方链接__:[开发者控制台](https://developer.roblox.com/zh-cn/articles/Developer-Console)