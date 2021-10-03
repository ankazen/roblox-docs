# 根部件：概述与理解 
Time:<em>10  分钟</em>

## Root Part（根部件）是什么？

`Weld|Weld`（接合）与 `Motor6D|Motor6D` 等刚性 `JointInstance|joint`（关节）可将多个部件结合为一个“**集合**”。如果集合中的所有部件均未被锚固，则该集合将形成一个刚体。每个集合都将拥有一个根部件，可以通过调用 `BasePart/GetRootPart` 来进行获取。

Weld 和 Motor6D 关节均无方向定义。当更改 C0/C1 或为 Motor6D 添加动画效果时，Part0 和 Part1 的具体定义部件并不能决定将要移动的部件。如果希望了解各部件的移动情况，我们首先需要对根部件进行指定。

**集合的 Root Part（根部件）为当刚性关节的 `DataType/CFrame|CFrame` 进行更新时仍然不会移动的部件。**

在使用 Weld（接合）时，开发者无需对此问题过于纠结：只需使用 `WeldConstraint|WeldConstraint` 或在进行接合前将部件移动到指定位置即可避免这一问题。但在使用 Motor6D 制作动画效果时，则需了解会进行移动的具体部件。

进行内部处理时，我们首先需要根据下文所述的部件排序规则决定根部件，然后使用从根部件逐步扩展的刚性关节构建扩展型的树状结构。当某个刚性关节的 CFrame 更新后，关节中距离根部件最近的部件将会静止不动，而其子部件及子部件的各子项将会进行移动。简而言之，我们将会为每个集合构建一个内部的变换层次结构（Transform Hierarchy）。

下图左边为基础的 R15 `Humanoid|Humanoid`（人形对象）角色模型中树状结构的视觉化效果，而右边为此树状结构中部件与部件之间的移动关系。

![Humanoid rig in Workspace](https://developer.roblox.com/assets/blt9abeebfde015986e/Root-Parts-Thumbnail.jpeg)

![Humanoid rig in explorer](https://developer.roblox.com/assets/bltc252f9f5b103c805/Humanoid-Rig-Explorer.png)



普通的 Humanoid（人形对象）角色模型为使用 Motor6D 进行连接的单一集合。其根部件通常为 `HumanoidRootPart`，原因如下：集合中的 `Accessory|Accessory` （饰品）通常为“**无质量**”部件；另外，将部件取名为 “HumanoidRootPart” 时，会使其在根据 `BasePart/Size|Size`（尺寸）进行排序的根部件排序规则中获取 10 倍尺寸值加成（这条规则来源于 Roblox 中添加 `BasePart/RootPriority|RootPriority` 前的时期）。

根部件在物理效果复制（Physics Replication）方面也有着重要作用。只有在所有客户端拥有相同根部件的前提下，物理效果复制才能够正常运行；当涉及到约束时，同时也将需要对机制结构进行统一，以保证网络所有权的正常分配。

## 根部件排序规则

在选择集合根部件时，集合中的部件将会按照此规则表顺序进行比较：

  1. 部件锚固（锚固部件将始终为其所在集合的根部件）
  2. 非 `BasePart/Massless|massless`（无质量）部件
  3. RootPriority
  4. 旧版尺寸排序。根据以 Size（尺寸）定义的对象边界框所拥有的的最大表面区域进行排序。其中 Seat（座位）部件将获取 20 倍加成；名为 “Torso”（躯干）及 “HumanoidRootPart” 的部件将分别获取 5 倍和 10 倍加成：`floor(maxPlanarSize() * 50.0) * specialMultiplier`

此规则表中的最后一条规则已经过时，但仍有许多游戏在不知情的情况下运用了这条规则。为了避免这种情况的发生，开发者应当通过提升特定部件 RootPriority 值等方法对表中的其他规则进行利用，以便更为准确地决定集合的根部件。



***__Roblox官方链接__:[根部件：概述与理解](https://developer.roblox.com/zh-cn/articles/understanding-root-parts)