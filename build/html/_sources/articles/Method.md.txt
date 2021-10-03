# Method（方法） 
Time:<em>2  分钟</em>

方法为属于指定对象的特殊函数。常见的 Roblox 方法包括 `Instance/Destroy|Instance:Destroy()`、`Instance/Clone|Instance:Clone()` 和 `Instance/FindFirstChild|Instance:FindFirstChild()` 等。

方法的作用类似于存储在对象中的函数，其访问方式与表中函数的访问方式相同。但方法的调用方式受其某项特殊属性的影响。

下面两行代码效果相同，都使用了参数 `testObject` 对函数 `testFunction()` 进行调用。请注意示例中**点式**标记法（`.`）与**冒号**标记法（`:`）的不同之处。

```    
    
    testObject.testFunction(testObject)
    testObject:testFunction()


```
以上示例中，第二行代码（方法调用）由于不需要重新输入变量名称而在使用方面更为简洁。

## 自定义方法

开发者可以通过创建自定义方法来保持代码的整洁，并使代码中的表更具动态性。如果希望创建自定义方法，首先需要添加应用该方法的表。请参考以下示例：

```    
    
    local testButton = {
    	enabled = true,
    	imageActivated = "rbxgameasset://Images/ImageButtonActivated",
    	imageNormal = "rbxgameasset://Images/ImageButtonNormal"
    }


```
当向 `testButton` 表添加方法时，请在表中包含相应键值对，其中**键**为自定义方法的名称，而**值**为方法函数。请看下列示例：

```    
    
    local testButton = {
    	enabled = true,
    	imageActivated = "rbxgameasset://Images/ImageButtonActivated",
    	imageNormal = "rbxgameasset://Images/ImageButtonNormal",
    	changeEnabled = function(self)
    		self.enabled = not self.enabled
    	end
    }


```
### 调用方法

当将函数作为方法调用时，开发者将自动传递一个参数作为**表本身**，如上例代码示例中一般由 `self` 引用。若希望对此进行证明，可以直接输出 `testButton.enabled` 的值，且在方法中输出 `self.enabled` 的值：

```    
    
    local testButton = {
    	enabled = true,
    	imageActivated = "rbxgameasset://Images/ImageButtonActivated",
    	imageNormal = "rbxgameasset://Images/ImageButtonNormal",
    	changeEnabled = function(self)
    		print(self.enabled)
    		self.enabled = not self.enabled
    	end
    }
    print(testButton.enabled)
    -- Call the method
    testButton:changeEnabled()
    
    
    true
    true

```
### 附加参数

开发者可以如使用其他函数般向方法函数传递参数。但需要注意的是：由于 `self` 为方法的父表，增添的附加参数需要在该 `self` 参数**后面**列出。

```    
    
    local testButton = {
    	enabled = true,
    	imageActivated = "rbxgameasset://Images/ImageButtonActivated",
    	imageNormal = "rbxgameasset://Images/ImageButtonNormal",
    	changeEnabled = function(self, isEnabled)
    		self.enabled = isEnabled
    		print(self.enabled)
    	end
    }
    print(testButton.enabled)
    -- Call the method with an additional argument
    testButton:changeEnabled(false)
    
    
    true
    false

```


***__Roblox官方链接__:[Method（方法）](https://developer.roblox.com/zh-cn/articles/Method)