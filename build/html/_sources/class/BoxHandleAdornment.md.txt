# BoxHandleAdornment
为使句柄具备交互能力，必须将玩家的 PlayerGui 或 CoreGui 设为其父项。
BoxHandleAdornment 是一种能够装饰到 BasePart 上的矩形棱柱。这种装饰物能够侦听输入事件，常用于制作拖曳工具。

属性
Vector3
Size
装饰物的尺寸。

继承自 HandleAdornment:
隐藏
bool
AlwaysOnTop
强制该对象在 Workspace 进行渲染时出现在所有 3D 对象的顶部。

CFrame
CFrame
对象相对于其 PVAdornment.Adornee 的位置和旋转。

Vector3
SizeRelativeOffset
基于 adornee（被装饰物）BasePart.Size 的装饰物位置偏移。

int
ZIndex
ZIndex 属性决定 HandleAdornment 的绘制顺序。

继承自 PVAdornment:
隐藏
PVInstance
Adornee
与 PVAdornment 相连的 PVInstance 。

继承自 GuiBase3d:
隐藏
Color3
Color3
设置一个 GUI 对象的颜色。

float
Transparency
设置 GUI 对象的透明度，1 表示不可见，0 表示完全可见。

bool
Visible
决定对象和其子项是否会被显示。

继承自 Instance:
隐藏
bool
Archivable
Determines if an Instance can be cloned using Instance:Clone or saved to file.

string
ClassName
 [readonly]  [notreplicated]
A read-only string representing the class this Instance belongs to

string
Name
Instance的非唯一标识符

Instance
Parent
决定 Instance 的分层式父项

bool
RobloxLocked
当为 true 时，Instance 及其子项将无法被 Script 或 LocalScript 进行索引或者编辑，并在尝试对其进行上述操作时报错

函数
继承自 Instance:
隐藏
void
ClearAllChildren ( )
此函数将摧毁 Instance 的所有子项。

Instance
Clone ( )
Create a deep copy of a Roblox instance and descendants where Archivable = true.

void
Destroy ( )
Sets the Instance.Parent property to nil, locks the Instance.Parent property, disconnects all connections and calls Destroy on all children.

Instance
FindFirstAncestor ( string  name )
返回 Instance 的第一父项，其 Instance.Name 与给定名称一致。

Instance
FindFirstAncestorOfClass ( string  className )
返回 Instance.ClassName 等于给定 className 的 Instance 的第一个父项。

Instance
FindFirstAncestorWhichIsA ( string  className )
返回 Instance 的第一个父项，此父项的 Instance:IsA 对于给定 className 会返回 true。

Instance
FindFirstChild ( string  name , bool  recursive )
Returns the first child of the Instance found with the given name.

Instance
FindFirstChildOfClass ( string  className )
返回 Instance.ClassName 等于给定 className 的第一个 Instance 子项。

Instance
FindFirstChildWhichIsA ( string  className , bool  recursive )
返回 Instance 的第一个子项，此子项的 Instance:IsA 对于给定 className 会返回 true。

Variant
GetAttribute ( string  attribute )
RBXScriptSignal
GetAttributeChangedSignal ( string  attribute )
Dictionary
GetAttributes ( )
Objects
GetChildren ( )
Returns an array containing all of the Instance's children.

string
GetDebugId ( int  scopeLength )
 [notbrowsable]
返回供 Roblox 内部使用的 Instance DebugId 的编码字符串。

Array
GetDescendants ( )
 [customluastate]
返回含有实例所有子项的数组

string
GetFullName ( )
返回一个描述 Instance 父项的字符串。

RBXScriptSignal
GetPropertyChangedSignal ( string  property )
获取一个在对象给定属性更改时触发的事件。

bool
IsA ( string  className )
 [customluastate]
Returns true if an Instance's class matches or inherits from a given class

bool
IsAncestorOf ( Instance  descendant )
当 Instance 为给定子项的父项时返回 true。

bool
IsDescendantOf ( Instance  ancestor )
Returns true if an Instance is a descendant of the given ancestor.

void
SetAttribute ( string  attribute , Variant  value )
Instance
WaitForChild ( string  childName , double  timeOut )
 [customluastate]  [canyield]
返回拥有给定名称的 Instance 子项。若无满足条件的子项存在，则函数将会暂停当前线程，直到子项出现为止。

事件
继承自 HandleAdornment:
隐藏
RBXScriptSignal
MouseButton1Down ( )
当用户在装饰物上按下鼠标左键时触发。

RBXScriptSignal
MouseButton1Up ( )
当用户在装饰物上松开鼠标左键时触发。

RBXScriptSignal
MouseEnter ( )
当用户将光标移到装饰物上时触发。

RBXScriptSignal
MouseLeave ( )
当用户将光标从装饰物上移开时触发。

继承自 Instance:
隐藏
RBXScriptSignal
AncestryChanged ( Instance  child , Instance  parent )
当对象或其父项之一的 Instance.Parent 属性发生改变时即会触发。

RBXScriptSignal
AttributeChanged ( string  attribute )
RBXScriptSignal
Changed ( string  property )
 [detectingpropertychanges]
在对象的属性发生更改后立即触发。

RBXScriptSignal
ChildAdded ( Instance  child )
Fires when an object is parented to this Instance.

RBXScriptSignal
ChildRemoved ( Instance  child )
从该 Instance 中移除某一子项时触发。

RBXScriptSignal
DescendantAdded ( Instance  descendant )
向 Instance 中添加子项时触发。

RBXScriptSignal
DescendantRemoving ( Instance  descendant )
在 Instance 的子项即将被移除前触发。