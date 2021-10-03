# GUI 简介 
Time:<em>20  分钟</em>

![](https://developer.roblox.com/assets/bltbbc45a3d1bd83a89/Intro-GUI-Banner.jpg) [Hexaria](https://www.roblox.com/games/913614076/Hexaria-Beta-V0-70) 标题屏幕（经 [Biostream ](https://www.roblox.com/users/15683535/profile))许可使用）

**GUI** 表示图形用户界面（**G**raphical **U**ser **I**nterface），用于向玩家显示游戏相关的信息。GUI 可用于向玩家显示其角色的等级、生命值和金币数量，也可以为菜单和物品栏系统创建按钮。在下图中，[Hexaria](https://www.roblox.com/games/913614076/Hexaria-Beta-V0-70) 的游戏开发人员使用 GUI 显示了关于玩家的信息并创建了游戏内菜单。

## 添加 GUI 到游戏中

最常见的 GUI 类型是**屏幕 GUI**，其行为类似于将贴纸放在玩家屏幕上的 2D 区域。当玩家移动镜头或探索游戏世界时，屏幕 GUI 会保持在相同区域中（位于屏幕上）。

当您制作新的 Roblox 游戏时，此屏幕 GUI 区域开始并不存在 — 您需要添加它。最简便的方法是将其添加到 StarterGui 服务，以便在玩家加入游戏时将其复制到玩家的本地游戏会话中。

  1. 在**管理器**窗口中，找到 **StarterGui** 对象。
![](https://developer.roblox.com/assets/bltec4b9d5dab192eae/Select-StarterGui-1.png)



  2. 将鼠标悬停在该对象上并单击圆圈 ⊕ 按钮。
![](https://developer.roblox.com/assets/blt25db36987baaf715/Select-StarterGui-2.png)



  3. 在弹出菜单中找到 **ScreenGui** 并选择它，这将在您的 3D 游戏世界上方创建一个新的 2D 屏幕区域。
![](https://developer.roblox.com/assets/blt097a958fc708fa79/Select-ScreenGui.png)



## 添加项目至屏幕 GUI

这个新的屏幕 GUI 当前为空 — 它只是一幅覆盖整个玩家屏幕宽度和高度的空白画布。

### 添加文本标签

各种内容都可添加至屏幕 GUI。我们先从基本的文本标签开始。

  1. 在管理器窗口中将鼠标悬停在作为 **StarterGui** 子项的新 **ScreenGui** 对象上，并单击其圆圈 ⊕ 按钮。
![](https://developer.roblox.com/assets/bltf0201a77763d92e6/Add-TextLabel-1.png)



  2. 在弹出菜单中找到 **TextLabel** 并选择它。请注意，通过在 “Search object（搜索对象）”输入字段中键入对象名称的前几个字母，可以更轻松地找到该对象。
![](https://developer.roblox.com/assets/blt7bbac02d7dbebeeb/Add-TextLabel-2.png)



这将在游戏视图的左上角添加一个非常基本的文本标签。

![](https://developer.roblox.com/assets/blt333958352b9224ba/Add-TextLabel-3.png)



这些步骤创建的新文本标签将作为** StarterGui **的子项** ScreenGui **的子项。由于这些对象都不存在于 3D 工作区中，因此您无法像选择常规部件一样使用** Select（选择）**工具选择它们。要选择任何这些与 GUI 相关的对象，您必须在创建它们的管理器窗口树中进行选择。 

### 自定义标签

现在我们在屏幕中有了一个文本标签，但是一个写了 **Label** 的白色框用处不大。让我们将其改为一个显示”版本号“的 GUI，这是通常出现在菜单/简介屏幕上的显示元素，用于显示游戏的当前版本。

  1. 在管理器窗口中，选择新的 **TextLabel** 对象。
![](https://developer.roblox.com/assets/blta40a63b51f80c3d9/Select-TextLabel.png)



  2. 通过选择 **View（视图）**选项卡并单击 **Properties（属性）**按钮，打开 **Properties（属性）**窗口。
![](https://developer.roblox.com/assets/bltc8a7d157bd64a3f3/Toggle-Properties.png)



  3. 对于 Font 属性（位于** Text（文本）** 部分中），单击字体名称的右侧并从下拉菜单中选择** Highway**。
![](https://developer.roblox.com/assets/blte49f6473348dca94/Intro-GUI-Font-Changed.png)



  4. 在 **Text** 属性字段中，键入如 **Version 1.0（版本 1.0）** 的新名称。
![](https://developer.roblox.com/assets/bltb8fef8a1ac67cb69/Intro-GUI-Text-Changed.png)



  5. 在 **TextSize** 属性字段中，键入 **35**。
![](https://developer.roblox.com/assets/blt7475d7316092b82e/Intro-GUI-TextSize-Changed.png)



  6. 现在展开 **Data（数据）** 部分（如果它尚未展开）。
![](https://developer.roblox.com/assets/blt1ab5ba1391304a69/Data-Section-Expand.png)



  7. 对于 **BorderSizePixel** 值，输入类似于 **8** 的新值。
![](https://developer.roblox.com/assets/blt41709aa769b867be/Intro-GUI-BorderSizePixel-Changed.png)



很不错！GUI 对象现在看起来好多了！如果希望更具创意，可尝试更改如 **TextColor3**、**BackgroundColor3** 和 **BackgroundTransparency** 等属性。

## 在屏幕 GUI 中定位项目

现在屏幕上有了一个基本的文本对象，让我们将其移动到新的位置。Roblox 中的每个 2D 对象都具有 ** Position** 属性，可用于根据其父对象确定将它绘制于何处。此位置由 ** X** 和 ** Y** 坐标设置，其中 ** X** 是水平位置，** Y** 是垂直位置。

![](https://developer.roblox.com/assets/blt37b4ff76a6df2492/XY-Axes.png)



在首次创建时，所有 2D 对象都从屏幕左上角 **0** 的 **X** 和 **Y** 位置开始，但是如何移动它？ 让我们来看一下文本标签的 **Position** 属性并了解如何移动！

  1. 如果未选择 **TextLabel** 对象，请在管理器窗口中单击它。
![](https://developer.roblox.com/assets/blta40a63b51f80c3d9/Select-TextLabel.png)



  2. 找到** Position** 属性并单击小箭头展开它。
![](https://developer.roblox.com/assets/bltede64106156ac48c/Expand-Position.png)



  3. 现在，直接展开其下方的 **X** 和 **Y** 分支。请注意，每个分支都具有唯一的 **Scale（缩放）** 和 **Offset（偏移）** 属性 — 可使用这些值为屏幕 GUI 中的文本标签定位。
![](https://developer.roblox.com/assets/bltf438813ac9679d6a/Expand-XY-Position.png)



### Scale 属性

**Scale** 属性表示父对象的宽度或高度的**百分比**。请记住，屏幕 GUI“画布”覆盖 3D 游戏视图的全宽和全高 — 这意味着 **Scale** 属性可用于根据屏幕全宽或全高的百分比将对象直接定位于视图的中心、紧靠左边缘或右边缘或者两者之间的任何位置。

虽然 **Scale** 表示百分比，但是您输入的值范围通常应介于 **0** 和 **1** 之间，其中 0 等于 0%，1 等于 100%。例如：

![](https://developer.roblox.com/assets/blt0f9c1447a2a5a11a/Scale-10.png)

 **Scale** = **0.1**  
全宽或全高的 10%

![](https://developer.roblox.com/assets/bltb754008fd7c8994c/Scale-50.png)

 **Scale** = **0.5**  
全宽或全高的 50%

![](https://developer.roblox.com/assets/bltcd65d1c9a68b5b20/Scale-95.png)

 **Scale** = **0.95**  
全宽或全高的 95%

现在，让我们将文本标签移至屏幕的水平中心。只需为 **X** 的 **Scale** 值输入** 0.5**，然后按 Enter/Return 键确认。

![](https://developer.roblox.com/assets/blt4673d0bcb8aac69a/Change-X-Scale-Position.png)



文本标签现在应该更靠近游戏视图的中心。

![](https://developer.roblox.com/assets/bltef4c7697cd252ce1/TextLabel-X-Scale-Position.jpg)

请记住，您的游戏将在不同宽高的屏幕上进行。例如，手机屏幕可能比 PC 或主机屏幕略宽（且略短）。**Scale** 是将对象定位在视图中心的最佳选择，在不同的屏幕上它将始终保持在中心。 

### Offset 属性

每组中的第二个属性称为 **Offset**。此属性不是按父项大小的百分比，而是按**像素**来移动元素的。如果要将 GUI 元素放在靠近游戏视图边缘的位置，您可以使用此属性。

让我们将文本标签放在靠近屏幕顶部边缘的地方。为 **Y** 的 **Offset** 值输入 50，然后按 Enter/Return 键确认。

![](https://developer.roblox.com/assets/bltbee4d513dbe033ac/Change-Y-Offset-Position.png)



现在文本标签应在靠近屏幕顶部边缘的地方。

![](https://developer.roblox.com/assets/bltf68fee05960513b0/TextLabel-Y-Offset-Position.jpg)

**Offset** 是将对象定位于视图**边缘**附近的最佳选择。使用此选项将确保对象在 PC、主机、平板电脑和手机上都保持在相同的基本屏幕位置。 

### 锚点

如果您仔细看 GUI 对象的当前位置，您将注意到：它并非位于左右方向的正中心位置，即使将 **Position** → **X** → **Scale** 设置为 0.5 (50%) 也是如此。

![](https://developer.roblox.com/assets/bltc7407dcf58619379/Anchor-Intro.jpg)

这是因为对象具有默认**锚点**。锚点是**对象上**用于与您设置的屏幕位置对齐的特定点。想象锚点如一根针穿过一张纸 — 针可以穿过纸上的任何位置，并且 Roblox 会使该针与您为对象设置的 **Position** 值保持一致。

在游戏编辑器窗口中，锚点由对象（在选中它时）上的**小正方形轮廓**显示。在创建新 GUI 对象时，锚点默认在其左上角 — 这就是为什么对象上的该点与之前设置的 **X** 和 **Y** 位置值保持一致。

![](https://developer.roblox.com/assets/blte4d6af9a014b49ef/Anchor-Point-Comparison.png)



锚点基于的 **X** 和 **Y** 值是对象大小的百分比：**0** 等于 0%，**1** 等于 100%。

![](https://developer.roblox.com/assets/blt89bbeb2323d5ff16/Anchor-Diagram.png)



您可以使用此概念将 GUI 对象置于屏幕的正中心。

  1. 如果未选择 **TextLabel** 对象，请在管理器窗口中单击它。
  2. 找到 **AnchorPoint** 属性并单击小箭头展开它。
![](https://developer.roblox.com/assets/blt6983e77005485224/Expand-AnchorPoint.png)



  3. 将 **X** 值设置为 **0.5**，然后按 Enter/Return 键确认。
![](https://developer.roblox.com/assets/blta266e5ec84b755b8/Anchor-X-Changed.png)



文本标签现在应该精确定位在游戏视图的中心。

![](https://developer.roblox.com/assets/blt9b8066a6815f8c12/Anchor-Centered.jpg)

锚点值并非限制为 **0**、**0.5** 或 **1** — 您可以输入介于这些值之间的任何值，如 **0.25** 或 **0.8** 等，但是无法设置小于 **0** 或大于 **1** 的锚点。 

## 调整屏幕 GUI 中项目的大小

如您所见，**Position** 和 **AnchorPoint** 属性可用于将元素放置在屏幕 GUI 中的任何位置。我们还可以更改任何元素的大小，方法是使用其 **Size** 属性。

  1. 如果未选择 **TextLabel** 对象，请在管理器窗口中单击它。
  2. 找到 **Size** 属性并单击小箭头展开它。
![](https://developer.roblox.com/assets/blt37f8a3b492a513e3/Expand-Size.png)



  3. 现在，展开其下方的 **X** 和 **Y** 分支。与 **Position** 类似，每个分支都具有唯一的 **Scale** 和 **Offset** 属性。
![](https://developer.roblox.com/assets/blt46435a2a520926d3/Expand-XY-Size.png)



### Scale 属性

在设置 GUI 对象的尺寸时，**Scale** 属性与位置的工作原理相同，即表示父对象的宽度或高度的百分比。如果将 **Size** → **X** → **Scale** 设置为 0.5 (50%)，该对象将正好为屏幕宽度的一半。

让我们测试一下！

  1. 为 **X** 的 **Scale** 值输入 **0.75**，然后按 Enter/Return 键确认。
![](https://developer.roblox.com/assets/bltcf36ffcb589f6543/Change-X-Scale-Size.png)



  2. 为 **X** 的 **Offset** 值输入 **0**，然后按 Enter/Return 键。
![](https://developer.roblox.com/assets/blt8e5bd54715a9e2d7/Change-X-Offset-Size.png)



文本标签现在应该正好占据屏幕宽度的 75%。

![](https://developer.roblox.com/assets/blt83371ee45d40f3c6/TextLabel-X-Scale-Size.jpg)

### Offset 属性

正如上文所述，**Size** 也具有称为 **Offset** 的属性。如果希望所创建的按钮、标签或其他对象无论在哪个屏幕上显示时都保持相同数量的**像素**（宽度或高度），那么您可以使用 Offset 来定义尺寸。

要增加文本标签的高度，只需为 **Y** 的 **Offset** 值输入 **150**，然后按 Enter/Return 键确认。

![](https://developer.roblox.com/assets/blt227a606f25663b41/Change-Y-Offset-Size.png)



现在，文本标签应该比以前高很多了！

![](https://developer.roblox.com/assets/bltf4b864a55db49b04/TextLabel-Y-Offset-Size.jpg)

## 使用负偏移值

某些 GUI 布局只能使用 **Scale** 和 **Offset** 值的创意组合实现，您可以通过将 **TextLabel** 对象填充整个屏幕然后四条边全部都留出 20 像素的边距来一探究竟。

  1. 将 **Position** → **Y** → **Offset** 设置为 **20**。这应该会略微向上提升对象。
![](https://developer.roblox.com/assets/blt733ae73915ef92b0/Position-Size-Combo-1.jpg)

  2. 将 S**Size** → **X** → **Scale** 设置为 **1**（100% 的屏幕宽度）。
  3. 将 **Size** → **X** → **Offset** 设置为 **-40** — 这会使对象比整个屏幕宽度_少_ 40 像素，让两边都留出所需的 20 像素边距。
![](https://developer.roblox.com/assets/blt888ff380f80f3261/Position-Size-Combo-2.jpg)

  4. 将 **Size** → **Y** → **Scale** 设置为 **1**（100% 的屏幕高度）。
  5. 将 **Size** → **Y** → **Offset** 设置为 **-40**。正如以上所示，这会使对象比屏幕全高少 40 像素，让顶部和底部都留出 20 像素的边距。
![](https://developer.roblox.com/assets/blt3e0c50f4c4b6ea5c/Position-Size-Combo-3.png)



#### 挑战

至少还有一种其他设置组合将产生上面相同的 GUI 对象，您能想到吗？这里有一个提示：将**锚点**设置为 **TextLabel** 对象的_中心_，然后根据需要调整 **Scale** 和 **Offset** 值。 

显示/隐藏

AnchorPoint 值

X 0.5

Y 0.5

Position 值

X Scale 0.5

Offset 0

Y Scale 0.5

Offset 0

Size 值

X Scale 1

Offset -40

Y Scale 1

Offset -40

* * *

好极了！这样我们就介绍完了 GUI 的基础知识、如何为玩家创建屏幕 GUI 画布，以及如何对屏幕上的 GUI 对象进行定位和大小调整。



***__Roblox官方链接__:[GUI 简介](https://developer.roblox.com/zh-cn/articles/Intro-to-GUIs)