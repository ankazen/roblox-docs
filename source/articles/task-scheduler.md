# 任务计划程序 
Time:<em>10  分钟</em>

**任务计划程序**负责在游戏运行时协调每帧中所有需要进行的工作，即使在游戏暂停时也不例外。其所协调的工作中包含侦测玩家输入、应用角色动画、 更新物理模拟及恢复处于 `wait()` 状态的脚本运行等。请一定要注意不要让任务计划程序超载，尤其是进行以下操作时：

  * 使用自定义人物模型或输入方案时
  * 自行为部件添加动画效果时（不使用 `Animator` 的情况下）
  * 大量使用精准物理时
  * 频繁复制对象时

## Frame（帧）

**帧**是游戏逻辑中的传输单元，每一帧中都会完成一定量的工作。在游戏中每秒内可发生多个帧，通常来讲，**每秒帧数**（FPS）越高，游戏性能也就越好。每帧内完成工作的效率越高，每秒内能够发生的帧数也就越多，而玩家体验也会因此提升。

## RunService

向游戏添加每帧任务最直接的方法为使用 `RunService` 的下列成员：

  * `RunService/BindToRenderStep|RunService:BindToRenderStep()`
  * `RunService/RenderStepped`
  * `RunService/Stepped`
  * `RunService/Heartbeat`

在选择需要使用的成员时，一定要多加斟酌。

## 计划程序的优先级

任务计划程序将任务通过下列顺序进行分类与完成。有的任务在一帧中可能不会完成任何工作，而其它任务可能会在一帧中多次完成工作：

  1. **用户输入** — 输入（`UserInputService`）事件和绑定函数（`ContextActionService/BindAction|ContextActionService:BindAction()`）将被优先处理。例：按下键盘键、鼠标移动、屏幕触控、手柄震动等。 
  2. **渲染**
    1. `RunService/BindToRenderStep|RunService:BindToRenderStep()` — 所有以这种方式进行绑定的函数将会以优先级顺序被调用。在内置 PlayerModule 中，镜头与角色控制脚本将按照 `enum/RenderPriority` 决定的优先级顺序对回调进行绑定。
    2. `RunService/RenderStepped` 事件被触发后，将会和所有事件一样调用连接函数，从最新连接的回调起开始运行。
    3. **屏幕绘制** — 此时，游戏状态将会进行并行渲染。此后的更改将在下一帧进行渲染。
  3. **复制对象获取任务** — 对传入属性变更与事件触发进行应用。
  4. **恢复等待状态** — 此时，任何当前处于 `wait()` 状态的运行中脚本将会在等待时间结束后进行恢复。等待恢复时间的下限为 0.03 秒，就是三十分之一秒。传递至 `spawn()` 与 `delay()` 的函数也会在此处运行。如果有线程需要在 0.1 秒后恢复，则会在之后的帧中进行恢复。
  5. **Lua 垃圾收集器**
  6. **模拟任务**（如果游戏暂停则略过此步） 
    1. **内部旧版步骤**
      1. `Explosion|Explosion` 可造成地形破坏、击退及关节破坏。
      2. `BodyMover|BodyMover` 例：`BodyPosition`、`RocketPropulsion`、`BodyGyro`等。
      3. `Humanoid` 发生状态更新，例：移动或死亡。
      4. **Internal Animation Step** — Animator 对 `Motor6D/Transform` 进行更新。将不会移动部件或更新已应用的关节偏移。
    2. `RunService/Stepped` 事件被触发。
    3. **内部物理步骤**
      1. **Motor6D** — 对使用 `Motor6D` 连接部件的相对位置进行更新。
      2. **世界步骤** — 更新部件接触并解决接触与约束。由于物理效果每 240 Hz 进行更新，所以每帧中可能会多次发生此步骤。所有世界步骤完成后，将会触发 `BasePart/Touched` 及相关物理事件。
      3. **插值网络集合** — 对无所有者的体位置进行插值。例：`BasePart/SetNetworkOwner|BasePart:SetNetworkOwner()`。
  7. `RunService/Heartbeat` 事件被触发。
  8. **复制对象发送任务** — 对传出属性变更与事件触发进行发送。不会每帧执行。

## 指南规则

如果想要创建高性能效率的游戏，请参照以下准则：

  * 除非必要，不要将函数绑定至渲染步骤（`BindToRenderStep/RenderStepped`）。此种行为将会延迟渲染线程，从而减少游戏的 FPS。只有输入后渲染前需要进行的任务才应该放置于此，例如镜头移动等。如果想要对顺序进行更为严格的控制，请使用 `RunService/BindToRenderStep|BindToRenderStep()` 而非 `RunService/RenderStepped|RenderStepped`。
  * 无论任何时刻，尽量减少使用 `wait()` 的脚本数量。请避免使用 `while wait() do end` 或 `while true do wait() end`，因为此两种构造并不能确保每帧或每个游戏步骤都会运行。可以使用 `RunService/Stepped|Stepped` 或 `RunService/Heartbeat|Heartbeat` 等事件进行替代，这些事件会对核心任务计划程序循环进行严格遵循。同理，请避免使用 `spawn()` 或 `delay()`，因为其所使用的内部机制与 `wait()` 相同（使用 `spawn()` 时与[协同程序](/api-reference/lua-docs/coroutine)库中的 `coroutine.wrap()` 与 `coroutine.resume()` 结合，效果更好）。
  * `RunService/Stepped|Stepped` 在物理效果**前**发生，而 `RunService/Heartbeat|Heartbeat` 在物理效果**后**发生。因此，对物理状态产生**影响**的游戏逻辑应该在 `RunService/Stepped|Stepped` 中完成，例如设置部件的`BasePart/Velocity|速度`等。与此相反，对物理状态进行**依赖**或**反应**的游戏逻辑应该在 `RunService/Heartbeat|Heartbeat` 中进行处理，例如读取部件`BasePart/Position|位置`以侦测其是否进入定义区域等。
  * 如果想要更改 `Motor6D/Transform` ，则需在 `RunService/Stepped|Stepped` 对此进行处理。如果放置至其它步骤，则下一帧的 `Animator|Animator` 将会对更改进行覆盖。即使 `Animator`不存在时，`RunService/Stepped|Stepped` 也是 `Motor6D/Transform` 应用至部件位置前最后触发的 Lua 事件。



***__Roblox官方链接__:[任务计划程序](https://developer.roblox.com/zh-cn/articles/task-scheduler)