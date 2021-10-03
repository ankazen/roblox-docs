# 线程计划程序 
Time:<em>5  分钟</em>

Roblox 使用线程计划程序以允许多个脚本并行执行。你可以利用此功能，在同一脚本中并行运行两段代码。Roblox 的线程计划程序可通过 `spawn`、`wait` 和 `delay` 函数体现。

在本文的剩余部分，“任务”一词用于表示由线程计划程序管理的协同程序。

### 列队任务

有两种方法可以将任务列队至线程计划程序中：

### 任务切换

Roblox 运行 wait 函数（或任何其他 YieldFunction）时，会暂停当前任务，使其列队等待稍后处理，然后查找其他等待任务（即另一个脚本或事件处理程序），并恢复下一个最重要的任务。没有其他方法可用于切换任务 - 如果你已使用 Spawn 使任务列队，则必须使用 wait() 才能使其运行：

此外，当列队任务终止时，可运行新任务 - 无需使用上述代码中的 wait()：

### ypcall

`ypcall` 可将任务列队，然后暂停当前任务，直到列队任务完成或出现错误

### 实施详情

以下代码显示了以 lua 编写的 Roblox 线程计划程序，其行为（看上去）与内置程序相同：

此代码不含：

  * 与 `wait` 行为类似的基本 `coroutine.yield()`
  * `pcall`

### 另请参阅

  * `Articles/Beginners Guide to Coroutines` \- 由线程计划程序在内部使用



***__Roblox官方链接__:[线程计划程序](https://developer.roblox.com/zh-cn/articles/Thread-Scheduler)