# JSON 格式 
Time:<em>2  分钟</em>

**JSON** 是一种数据存储格式。在 Roblox 中，`HttpService` 提供了两个用于处理 JSON 数据的函数：

  * `HttpService/JSONEncode|HttpService:JSONEncode()` 将变量转换为其 JSON 等效变量。
  * `HttpService/JSONDecode|HttpService:JSONDecode()` 将 JSON 值转换为其 Lua 表示形式。

## 编码

此代码片段将 `characterStats` 编码为 JSON 字符串并将其打印到输出。

JSON: Code Sample 1 ```    
    
    local HttpService = game:GetService("HttpService")
    
    local characterStats = {
    	money = 123456,
    	title = "1337 h4x04",
    	is_epic = true,
    	awards = {
    		kills10 = true,
    		died20 = false,
    	}
    }
    
    local json = HttpService:JSONEncode(characterStats)
    print(json)
    
    
    {"awards":{"died20":false,"kills10":true},"title":"1337 h4x04","is_epic":true,"money":123456}

```
`HttpService/JSONEncode|HttpService:JSONEncode()` 不能对字符串、数字、表和布尔值以外的任何内容进行编码；传递任何其他内容都将出错。 

## 解码

此代码片段将上面创建的JSON值转换回其表表示形式，然后将其 `money` 值打印到输出。

JSON: Code Sample 2 ```    
    
    local HttpService = game:GetService("HttpService")
    
    local jsonData = '{"awards":{"died20":false,"kills10":true},"title":"1337 h4x04","is_epic":true,"money":123456}'
    local characterStats = HttpService:JSONDecode(jsonData)
    print(characterStats.money)
    
    
    123456

```


***__Roblox官方链接__:[JSON 格式](https://developer.roblox.com/zh-cn/articles/JSON-Storage-Format)