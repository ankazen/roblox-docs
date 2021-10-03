# MicroProfiler 
Time:<em>2  分钟</em>

MicroProfiler 是一个高级工具，开发人员可以在移动设备和台式机上使用该工具分析和调试客户端性能问题。

![MicroProfiler.png](https://developer.roblox.com/assets/blt8902fe9a81b5de4b/MicroProfiler.png)



## 在移动设备上使用 MicroProfiler

  1. 点击左上角的汉堡包菜单
  2. 点击设置选项卡
  3. 向上滑动并打开 Micro Profiler 选项
  4. 再次向上滑动，找到 IP 和端口
  5. 在使用相同网络的台式计算机上，在浏览器中访问该 URL。该 URL 看起来可能像这样（但可能有所不同）：<http://172.16.24.107:1338>

## 在 PC 上使用 MicroProfiler

  1. 在 Studio 或 Roblox 客户端中，按 Ctrl+F6 打开 MicroProfiler 视图。
  2. 按 Ctrl+P 暂停并查看过去几帧的数据。

## 添加自定义分析标签

可以使用 [debug.profilebegin](http://wiki.roblox.com/index.php?title=Global_namespace/Basic_functions&redirect=no#debug.profilebegin) API 从 lua 向 Microprofiler 中添加自定义标签。

## 有趣的视频



***__Roblox官方链接__:[MicroProfiler](https://developer.roblox.com/zh-cn/articles/MicroProfiler)