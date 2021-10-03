# 布尔值 
Time:<em>10  分钟</em>

**Boolean**（布尔值）是一种非常简单的数据类型，其值为 **true** 或 **false**。布尔值常用于例如下列代码的`Articles/Conditional Statements in Lua|条件语句`中：

Boolean: Code Sample 1 ```    
    
    local testBoolean = true
    
    if testBoolean == true then
    	-- Value of 'testBoolean' is true, so this condition is executed
    else
    	-- If value of 'testBoolean' is false, this condition is executed
    end
    
    
    0

```
## Lua 估算

在 Lua 中，如果某个值**不是** false 或 `nil`，则在条件语句中使用时会将其视为 “true”。下面的代码仅输出 Lua 解释为 true 的值：

Boolean: Code Sample 2 ```    
    
    -- These values are all "true"
    if true then
    	print("true")
    end
    if 1 then
    	print("1")
    end
    if "text" then
    	print('"text"')
    end
    if {1, 2, 3} then
    	print("{1, 2, 3}")
    end
    if workspace then
    	print("workspace")
    end
    if "" then
    	print('""')
    end
    
    -- But these values are not...
    if false then
    	print("false")
    end
    if nil then
    	print("nil")
    end
    
    
    true
    1
    "text"
    {1, 2, 3}
    workspace
    ""

```
## 运算符

根据上述估算规则，带有 Lua `/articles/Operators|operators` （运算符）的条件语句工作方式如下所示：

### And

如果为 `false` 或 `nil`，`and` 运算符返回**第一个**参数，否则返回第二个参数。

Boolean: Code Samples 5 ```    
    
    print(4 and 5)
    print(nil and 12)
    print(false and 12)
    print(true and true)
    print(true and false)
    print(false and true)
    print(false and false)
    
    
    5
    nil
    false
    true
    false
    false
    false

```
### Or

`or` 运算符对两个值进行运算。如果第一个值 **既不是 `false` 也不是 `nil`**，则 `or` 运算符返回第一个值。如果第一个值**是 `false` 或 `nil`**，则该运算符返回第二个值。例如：

Boolean: Code Samples 8 ```    
    
    local y = x or 1
    print(y)
    
    
    1

```
之所以输出 `1`，是因为 `x` 不存在，因此为 `nil`。实际上，`or` 运算符是让我们选择 `1` 而不是 `nil`。

Boolean: Code Samples 9 ```    
    
    local x = false
    local y = x or 1
    print(y)
    
    
    1

```
之所以也输出 `1`，是因为尽管 `x` 存在，但其值为 `false`。如果 `x` 为 `true`，则 `or` 运算符将选择 `x` 而不是 `1`。

### Not

如果参数为 `false` 或 `nil`，则 `not` 运算符返回 `true`，否则返回 `false`。

Boolean: Code Sample 3 ```    
    
    print(not true)
    print(not false)
    print(not nil)
    print(not "text")
    print(not 0)
    
    
    false
    true
    true
    false
    false

```


***__Roblox官方链接__:[布尔值](https://developer.roblox.com/zh-cn/articles/Boolean)