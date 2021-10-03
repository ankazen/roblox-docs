# 枚举值 
Time:<em>2  分钟</em>

**enumeration** （枚举）的常见缩写为 “enum”，是可以接受成组值中单一值的特殊数据类型。举例来说，`enum/Material` 枚举表示了部件的材质类型。

有关 Roblox 中枚举类型的完整列表，请参见[枚举值索引](/api-reference/enum)。 

在脚本中，开发者可以通过名为 `datatype/Enum` 的全局对象对枚举进行访问。若希望获取枚举值可用的所有 `datatype/EnumItem|EnumItem` 选项，请对指定枚举类型调用 `GetEnumItems()` 方法：

```    
    
    local inputStates = Enum.UserInputState:GetEnumItems()
    
    for i, v in ipairs(inputStates) do
    	print(v)
    end
    
    
    Enum.UserInputState.Begin
    Enum.UserInputState.Change
    Enum.UserInputState.End
    Enum.UserInputState.Cancel
    Enum.UserInputState.None

```
了解 `datatype/EnumItem|EnumItem` 的可用选项后，开发者可以通过 3 种不同的方式为对象设置枚举属性：

```    
    
    workspace.Part.Material = Enum.Material.Concrete  -- By full enum (preferred method)
    workspace.Part.Material = 816  -- By enum value
    workspace.Part.Material = "Concrete"  -- By enum name


```


***__Roblox官方链接__:[枚举值](https://developer.roblox.com/zh-cn/articles/Enumeration)