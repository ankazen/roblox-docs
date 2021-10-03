# For 循环 
Time:<em>5  分钟</em>

**泛型 for**循环是一种利用迭代器函数的 `for 循环`。在学习此循环之前，你应该了解基本的 for 循环。

## 有状态迭代器

首先，让我们看看迭代器。通俗地说，迭代器是一个函数，每次调用它时都返回下一组值。下面是一个生成简单迭代器的函数：
    
    
    -- 返回一个迭代器，该迭代器计算首尾之间的字母
    function letterIterator(first, last)   
        -- 存储迭代器所在的位置
        local index = first 
        -- 返回迭代器——一个函数！
        return function()
            if index <= last then
                -- 移至下一个角色
                index = index + 1  
                -- 返回 index plus 95 的 ascii 表示形式（一个字母）
                -- 请注意，仅返回一个值
                return string.char(index + 95)
            end
        end
    end
    

下面是我们如何使用它：
    
    
    local iterator = letterIterator(1, 4)
    local letter
     
    letter = iterator()
    print(letter) -- **a**
     
    letter = iterator()
    print(letter) -- **b**
     
    letter = iterator()
    print(letter) -- **c**
     
    letter = iterator()
    print(letter) -- **d**
     
    letter = iterator()
    print(letter) -- nil
     
    letter = iterator()
    print(letter) -- nil
    

如你所见，迭代器返回第一个、第二个、第三个和第四个字母，然后停止返回任何内容。此时，没有任何要迭代的内容，因此你应该停止调用迭代器。这就是泛型 for 循环的来源。我们可以这样编写前面的代码：

Generic For Code Sample 1 ```    
    
    for letter in letterIterator(1, 4) do
    	print(letter)
    end
    
    
    a
    b
    c
    d

```
## 说明

迭代器是跟踪记录 _for_ 循环应该运行多少次的对象。这与`Articles/Roblox Coding Basics Loops|循环`中的数字 **for** 循环**不同**，因为数字 for 循环只是一个索引：
    
    
    for i = 20, 1, -2 do
    	print(i)
    end
    

但是，在泛型 for 循环中，我们得到迭代器函数返回的值。在上面 `letterIterator()` 返回的迭代器中，我们看到返回的是 `string.char(index + 95)`，而不是 `index` 本身。下面是一个使用多个返回值的示例：

### 标准库迭代器

两个常用的标准库迭代器函数是 `pairs` 和 `ipairs`。这些函数返回表键及其对应的 `values`。pairs 遍历整个表，即使键是非数字的（例如“Hi”），也将其视为 `dictionary`（请参见`Articles/Table|表`）。ipairs 像数组一样遍历表，从 1 开始，计算连续的整数索引。一旦达到 nil 值，它将停止在表中循环。另外，请注意，pairs 不按任何特定顺序遍历表。下面是展示两者不同之处的示例：
    
    
    local sampleTable = {
    	[1] = "A",
    	[2] = 2,
    	[3] = "B",
    	[5] = 5,
    	Hi = "C"
    }
    

Generic For Code Sample 3 ```    
    
    for i, v in ipairs(sampleTable) do
    	print(i, v)
    end
    
    
    1	A
    2	2
    3	B

```
Generic For Code Sample 4 ```    
    
    for k, v in pairs(sampleTable) do
    	print(k, v)
    end
    
    
    2	2
    3	B
    1	A
    5	5
    Hi	C

```
由于 pairs 使用 `next` 作为迭代器函数，有些人更喜欢直接调用它：

Generic For Code Sample 5 ```    
    
    for k, v in next, sampleTable do
    	print(k, v)
    end
    
    
    2	2
    3	B
    1	A
    5	5
    Hi	C

```
## 自定义迭代器

你也可以自己编写迭代器！以下是两个有用的示例：

#### string.gfind

此示例返回多个值：

Generic For Code Sample 6 ```    
    
    string = {}
    string.gfind = function(stringToSearch, pattern, start)
    	local start = start or 1 -- Default value is 1
    	return function()
    		local beginning, ending = stringToSearch:find(pattern, start) -- Start searching at the specified location
    		if beginning and ending then -- Check to make sure that the match is there
    			start = ending + 1 -- Add one to the ending so the pattern will start to look after the last match
    			return beginning, ending, stringToSearch:sub(beginning, ending) -- return the 3 values
    		end
    	end
    end
    
    local stringToSearch = "Hello! My name is merlin1188!"
    
    for start, finish, value in string.gfind(stringToSearch, "%a+") do
    	print("The match starts at " .. start ..", finishes at " .. finish .. ", and is " .. value)
    end
    
    
    he match starts at 1, finishes at 5, and is Hello
    The match starts at 8, finishes at 9, and is My
    The match starts at 11, finishes at 14, and is name
    The match starts at 16, finishes at 17, and is is
    The match starts at 19, finishes at 24, and is merlin

```
#### 后代

此示例遍历 `Instance|Instance` （实例）的所有`Instance/GetChildren|children` （子级）：
    
    
    function descendants(obj, depth)
    	assert(obj and obj.GetChildren, "object parameter is missing or is not an instance")
    
    	local function yieldtree(obj, level)
    		if depth and level > depth then
    			return
    		end
    		for _, o in ipairs(obj:GetChildren()) do
    			coroutine.yield(o, level)
    			yieldtree(o, level+1)
    		end
    	end
    
    	return coroutine.wrap(function() yieldtree(obj, 1) end)
    

## 供进一步参考：

  * [无状态迭代器](http://www.lua.org/pil/7.3.html)



***__Roblox官方链接__:[For 循环](https://developer.roblox.com/zh-cn/articles/For-Loops)