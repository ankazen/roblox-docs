# 对象浏览器 
Time:<em>10  分钟</em>

对象浏览器显示有关 Roblox 中可用的每个对象、类和枚举的信息。

![在此处输入图像描述](https://developer.roblox.com/assets/blt8b059675ebb8dcb5/Object_Browser.png)



## 用法

你可以通过转到 Roblox Studio 中的 `Help（帮助）> Object Browser（对象浏览器）`来访问对象浏览器。

单击此项后，将打开一个名为“Object Browser（对象浏览器）”的新选项卡。这个窗口包含一些非常重要的信息，是关于可以在 Roblox 中创建的对象类型的。这个窗口有三个面板：最左边的面板是类和枚举列表，右上方的面板是成员列表，右下方的面板是详细信息列表。

### 类面板

类面板包含 Roblox 中所有可用类的列表。默认情况下，此面板列出所有可实例化的类和所有枚举类型。此列表按字母顺序排序，首先是类，然后是枚举类型。类由一个图标表示，该图标带有一个黄色的对角矩形和一个紫色和蓝色的菱形。枚举由一个带有两个黄色圆角矩形的图标表示。

#### 类

类是可以实例化的数据组。在 Roblox 中，Instance.new 函数用于创建对象。此函数可创建一个新对象，使其具有与你提供的类相同的类。此对象具有类的属性、方法和事件。这些属性、方法和事件与 Lua 脚本一起用于操作游戏。

#### 枚举

Enums（枚举）（即 `Enumeration` 的缩写）只是一个值。通常，当对象可以具有一组特定、有限的不同值时，将使用枚举。要进行比较，部件的名称可以是任意字符序列。

### 成员面板

成员面板列出类的所有属性、方法和事件，以及枚举的可用值。

### 属性、方法和事件

单击“类”面板中的类时，此面板中将显示可用属性、方法和事件的列表。这些成员按字母顺序列出并分组，首先是方法，其次是属性，最后是事件。方法用紫色菱形表示。属性用蓝色菱形表示。事件用黄色闪电球表示。

#### 枚举值

单击“类”面板中的枚举时，将显示与该枚举关联的值列表。枚举值由一个白色框表示，后面有一个黄色的圆角框。

#### 其他注意事项

如果将视图级别设置为 RobloxScript，则会看到一些项目的图标左下角有一个黄色键。这表示该方法、属性或事件不能在脚本或 LocalScript 中使用，无论是用于读取值还是分配值。

### 详细信息面板

“详细信息”面板可能是三个面板中最重要的面板。“详细信息”面板提供有关选定类、枚举、方法、属性或事件的信息。

#### 类详细信息

在“类”面板中选择类时，有关该类的某些信息将显示在此面板中。首先，你将看到所选择的类的继承（即，该类是“由什么组成的”）。你将看到的第二条信息是 Summary（摘要）。摘要是对所选类的简要说明。让我们看一下 Part。当你选择 Part 时，你看到的第一行是 `Part->BasePart->PVInstance->Instance`。这意味着 Part 继承自 BasePart 类，BasePart 类又继承自 PVInstance 类，PVInstance 类最终继承自 Instance 类。

当一个类继承另一个类时，这意味着该类包含所继承类的成员。在本例中，Part 包含 Touched 事件，它是 BasePart 类的一部分。这些“父”类在 Is-A 基础上与所选类关联。也就是说，Part Is-A BasePart、Is-A PVInstance 和 Is-A Instance。对于“Part”、“BasePart”、“PVInstance”和“Instance”这些值，对部件调用的 IsA 方法的返回值为 true。

我个人喜欢把继承看作是矩形和正方形之间的关系。正方形继承了长方形。我们也可以口头解释为“正方形总是矩形，但矩形并不总是正方形”。这同样适用于部件。Part 始终是 BasePart，但 BasePart 并不总是 Part。

继承是编程中的一个前沿课题，所以如果你现在还不理解它，也不要担心。

#### 方法详细信息

从“成员”面板中选择方法时，此面板中将显示有关该方法的一些关键信息。你看到的第一行称为方法的签名。方法的签名定义其返回类型和参数类型。第二行告诉你方法的来源（即包含此方法的类）。最后对该方法进行了简要说明。让我们仔细查看 Part 类的 IsA 方法。
    
    
    bool IsA(string className)
    Member of Instance
    
    Summary: Returns a boolean if this Instance is of type 'className' or a is a subclass of type 'className'. If 'className' is not a valid class type in Roblox, this function will always return false. More info
    

第一行 `bool IsA(string className)` 定义了方法的签名。这告诉你 IsA 方法返回 bool 值（布尔值的缩写），并在作为方法调用时将字符串作为唯一的参数。第二行是 `Member of Instance`，告诉你 `IsA` 方法实际上不属于 `Part` 类；它实际上属于 `Instance` 类。这意味着每个继承实例类的类都将包含 IsA 方法。最后，显示包含有关方法信息的摘要。

#### 属性详细信息

从“成员”面板中选择属性时，将显示有关选定属性的详细信息。属性详细信息只包含三个部分。第一部分是属性的值类型。第二部分显示属性属于哪个类，第三部分是属性的摘要。让我们仔细看下 Part 类的 Anchored 属性。
    
    
    bool Anchored
    Member of BasePart
    
    Summary: Determines whether or not physics acts upon the Part. If true, part stays Anchored in space, not moving regardless of any collision/forces acting upon it. If false, physics works normally on the part.
    

第一行告诉我们，`DescendantAdded` 事件返回一个 `Instance` 或一个对象。第二行告诉我们这个事件属于 ‘Instance’ 类（同样，不是 Part 类）。然后，摘要将说明事件的作用和触发时间。

#### 事件详细信息

当你从“成员”面板中选择一个事件时，将显示有关该事件的信息。第一行告诉你事件返回的内容。第二行告诉你事件属于哪个类，最后给出事件的摘要。让我们来看看 Part 类的 DescendantAdded 事件。
    
    
    event DescendantAdded(Instance descendant)
    Member of Instance
    
    Summary: Fired after an Instance is parented to this object, or any of this object's descendants. The descendant argument is the Instance that is being added.
    

第一行告诉我们，`DescendantAdded` 事件返回一个 `Instance` 或一个对象。第二行告诉我们这个事件属于 ‘Instance’ 类（同样，不是 Part 类）。然后，摘要将说明事件的作用和触发时间。

对于事件，返回的值将传递给调用函数。将函数连接到事件时，事件返回的任何值都将传递给连接的函数。如果我将以下函数连接到 DescendantAdded 事件：
    
    
    function a(param)
    end
    

param 将成为添加的后代对象，它是 `DescendantAdded` 事件的返回值。

#### 枚举详细信息

选择枚举时，此面板中显示的唯一内容是枚举的名称。此名称用于访问与选定枚举关联的枚举值。然后选择一个枚举值，显示的唯一内容是与该值关联的基于零的整数值和该值的名称（用冒号分隔）。如果选择 NormalId 枚举，则详细信息面板将包含 `NormalId`。如果选择 NormalId 枚举，然后选择 Top 枚举值，那么详细信息面板将包含 `1:Top`。

#### 其他注意事项

如果启用了已弃用对象的视图并将视图级别设置为 RobloxScript，则你会注意到此面板中显示的一些其他信息。如果你选择了一个用删除线表示的已弃用的项目，一些漂亮的红色文字会向你解释，你选择的成员已弃用，不应该使用。这意味着 Roblox 不再支持此方法、属性或事件的使用，并且如果将来的更新损坏了它，它将不会被修复。如果你选择的项目图标左下角有一个黑色挂锁，这意味着你选择的项目是预备性的，应仅用于测试。一些漂亮的红色文字也会告知你这些是预备对象。

## 高级

通过编辑 Roblox 附带的 `ReflectionMetadata.xml` 文件，可以在 Roblox Studio 和对象浏览器中显示一些隐藏类。



***__Roblox官方链接__:[对象浏览器](https://developer.roblox.com/zh-cn/articles/Object-browser)