# Table（表） 
Time:<em>10 分钟</em>

**Table**（表）为可以储存多个值的 Lua 数据类型，其中包括`/articles/Numbers|数字`、`/articles/Boolean|布尔值`、`/articles/String|字符串`、`/articles/Function|函数`等多种类型。表的构造使用中括号（`{}`），如下所示：

```    
    
    -- Construct an empty table assigned to variable "t"
    local t = {}
    print(t)
    
    
    table: 0035AE18

```
表格在构建后即可用作**数组**或**字典**，如以下各部分中所述。

## 数组

数组是一组简单的有序值，可用于存储数据集合，例如一组拥有特殊权限的玩家。

### 创建数组

要使用 Lua 表格创建数组，只需按顺序存储各个值，并用逗号分隔这些值即可。数组值可以是任何非 `nil` 类型（布尔值、数字、字符串、函数、用户数据，甚至是另一个表格）。

```    
    
    -- Construct an array with three items
    local testArray = {"A string", 3.14159, workspace.Part}


```
### 从数组读取数据

要从数组中读取数据，请在其引用后添加一对方括号，并指定其中元素的索引号 (`[pos]`)：

```    
    
    -- Construct an array with three items
    local testArray = {"A string", 3.14159, workspace.Part}
    
    print(testArray[1])
    print(testArray[2])
    print(testArray[3])
    
    
    A string
    3.14159
    Part

```
与某些语言不同，Lua 对数组使用**以 1 为基数的索引**，这意味着数组中的第一项是 `[1]`，而不是 `[0]`。 

### 向数组写入数据

可以通过在方括号 (`[pos]`) 中指示索引号，并后跟 `=` 和值来定义或重写数组索引值：

```    
    
    local testArray = {"A string", 3.14159, workspace.Part}
    
    testArray[2] = 12345
    testArray[4] = "New string"
    
    print(testArray[2])
    print(testArray[4])
    
    
    12345
    New string

```
### 循环访问数组

可以通过以下两种方式循环访问（循环遍历）数组：

  * 在 `for` 循环中使用内置的 `ipairs()` 函数。
  * 使用 `#` 运算符获取数组的长度，并从 **1** 一直循环到该长度值。

```    
    
    local testArray = {"A string", 3.14159, workspace.Part, "New string"}
    
    -- Loop using "ipairs()"
    for index, value in ipairs(testArray) do
      print(index, value)
    end
    
    -- Iterate using the array length operator (#)
    for index = 1, #testArray do
      print(index, testArray[index])
    end
    
    
    1 A string
    2 3.14159
    3 Part
    4 New string
    1 A string
    2 3.14159
    3 Part
    4 New string

```
### 插入项目

可以通过以下两种方法之一向数组**末尾**插入项目：

  * 将数组引用和项目值传递给 Lua 的 `table.insert()` 函数。
  * 使用 `t[#t+1]` 语法将新项目添加到数组。

```    
    
    local testArray = {"A string", 3.14159}
    
    table.insert(testArray, "New string")
    testArray[#testArray+1] = "Another new string"
    
    print(testArray[3])
    print(testArray[4])
    
    
    New string
    Another new string

```
此外，也可以通过将位置值作为 `table.insert()` 的第二个参数，在开头和结尾之间插入项目。此方法将插入新项目，并将随后的项目上移一个索引位置。

```    
    
    local testArray = {"First item", "Next item"}
    
    table.insert(testArray, 2, "NEW ITEM #2")
    
    print(testArray[1])
    print(testArray[2])
    print(testArray[3])
    
    
    First item
    NEW ITEM #2
    Next item

```
### 移除项目

可以使用 Lua 的 `table.remove()` 函数从数组中移除项目。此方法将移除指定位置处的项目，并将随后的所有项目下移一个索引位置。

```    
    
    local testArray = {"First item", "Next item", "Last item"}
    
    table.remove(testArray, 2)
    
    print(testArray[1])
    print(testArray[2])
    
    
    First item
    Last item

```
有关上述函数和其他特定于数组的方法的详细信息，请参阅 Lua [表格库](/api-reference/lua-docs/table)文档。 

## 字典

字典是对数组的扩展。数组存储一组有序的项目，而字典存储一组**键值对**。

键 值

FruitName
Lemon

FruitColor
Yellow

Sour
true

### 创建字典

要创建字典表，请定义每个**键**，并后跟 `=` 和**值**。请记得用逗号分隔每个键值对：

```    
    
    local testDictionary = {
      FruitName = "Lemon",
      FruitColor = "Yellow",
      Sour = true
    }


```
在创建字典时，键不仅限于字符串名称（如 `FruitColor`）；例如，键也可以是 `Instance`。在这种情况下，必须用方括号 (`[key]`) 声明键：

```    
    
    local part = Instance.new("Part")
    
    local testDictionary = {
      PartType = "Block",
      [part] = true
    }


```
### 从字典中读取数据

要从字典中读取数据，请在其引用后添加一对方括号并指定键名称：

```    
    
    local part = Instance.new("Part")
    
    local testDictionary = {
      PartType = "Block",
      [part] = true
    }
    
    print(testDictionary["PartType"])  -- Include quotes for string keys
    print(testDictionary[part])  -- Omit quotes for non-string keys
    
    
    Block
    true

```
如上面的代码注释中所述，请注意以下几点： 

  * 必须用引号将**字符串**键（例如 `PartType`）引起来，如 `testDictionary["PartType"]` 中的情况。
  * **不**应使用引号将**非字符串**键（例如 `[part]`）引起来。

### 向字典写入数据

可以通过在方括号 (`[key]`) 中指示键名称并后跟 `=` 和值来定义新的或现有的字典键的值：

```    
    
    local testDictionary = {
      FruitName = "Lemon",
      Sour = true
    }
    
    -- Change value of existing keys
    testDictionary["FruitName"] = "Cherry"
    testDictionary["Sour"] = false
    
    -- Insert new key-value pair
    testDictionary["FruitCount"] = 10
    
    print(testDictionary["FruitName"])
    print(testDictionary["Sour"])
    print(testDictionary["FruitCount"])
    
    
    Cherry
    false
    10

```
### 循环访问字典

可以在 `for` 循环中使用内置的 `pairs()` 函数对字典进行循环访问：

```    
    
    local testDictionary = {
      FruitName = "Lemon",
      FruitColor = "Yellow",
      Sour = true
    }
    
    for key, value in pairs(testDictionary) do
      print(key, value)
    end
    
    
    FruitName Lemon
    Sour true
    FruitColor Yellow

```
与对数组使用 `ipairs()` 不同，通过 `pairs()` 循环访问字典时不一定会按照项目在字典中的相同声明顺序返回这些项目。 

### 移除键值对

要从字典中移除键值对，只需将其值设置为 `nil` 即可，这会从字典中完全删除键值对，如下面的 `pairs()` 循环输出中所示：

```    
    
    local testDictionary = {
      FruitName = "Lemon",
      FruitColor = "Yellow",
      Sour = true
    }
    
    testDictionary["Sour"] = nil
    
    for key, value in pairs(testDictionary) do
      print(key, value)
    end
    
    
    FruitName Lemon
    FruitColor Yellow

```
## 将表作为引用

如果将表存储在新变量中，则不会创建该表的副本。该变量将成为原始表的**引用**（指针）。这意味着对原始表的任何更改都将反映在任何引用中：

```    
    
    local originalArray = {10, 20}
    
    local arrayReference = originalArray
    
    print("Original:", originalArray[1], originalArray[2])
    print("Reference:", arrayReference[1], arrayReference[2])
    
    -- Change values in original array
    originalArray[1] = 1000
    originalArray[2] = 2000
    
    print("Reference:", arrayReference[1], arrayReference[2])
    
    
    Original: 10 20
    Reference: 10 20
    Reference: 1000 2000

```


***__Roblox官方链接__:[Table（表）](https://developer.roblox.com/zh-cn/articles/Table)