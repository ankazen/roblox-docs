# 插件简介 
Time:<em>10  分钟</em>

**Plugin**（插件）为 Studio 的自定义加载项，用于添加一般情况下未包含的新行为与功能。开发者可以安装 Roblox 社区创作的插件，也可以自行创作插件使用。

## 查找和管理插件

开发者可以在 Studio 的 [Toolbox](/resources/studio/Toolbox)（工具箱）中查找新的 Studio 插件。安装插件后，可以通过 **Plugins** （插件）选项卡中的 **Manage Plugins（管理插件）**按钮对已安装的插件进行管理与更新。

![](https://developer.roblox.com/assets/bltea914415df398088/Plugin-Manage-Plugins-1.png)

 ![](https://developer.roblox.com/assets/bltcd91725bac69494c/Plugin-Manage-Plugins.png)



**A**

**Update（更新）**— 获取最新版本的插件。 

**B**

**激活状态**— 切换插件是否处于激活状态。 

**C**

**详细信息与移除**— 打开用来查看插件详细信息或卸载插件的菜单。 

## 创建新插件

开发者不仅能够使用预建插件，更可以根据自身需求创建用于各种目的的插件。在此段落中，我们将创建一个简单的插件，该插件不会运行默认的 “Hello world!” 打印函数，但可以将新的脚本插入到 `ServerScriptService` 中。

  1. 创建新插件时需要创建新的 `Script`。请在 `ServerStorage` 内创建新脚本实例。
  2. 将脚本命名为 **EmptyScriptAdder**。
![](https://developer.roblox.com/assets/blt73ad22e9667cbfd0/Plugin-Empty-Script-Adder.png)



  3. 右键单击脚本并选择 **Save as Local Plugin（另存为本地插件）**。
![](https://developer.roblox.com/assets/blt18d7324025e3f2ec/Save-Local-Plugin.png)



  4. 单击 **Save（保存）**，将插件放入插件文件夹中。

此时，**Output**（输出）窗口将显示已成功保存插件的消息，注意 "Hello world!" 也将显示在窗口中： ![](https://developer.roblox.com/assets/blt7f64617cff9bae7d/Plugin-Hello-World-Output.png)



这实际上就是插件的第一次运行。每当使用这种方式保存插件时，插件都会刷新并运行。

### 添加工具栏按钮

通常情况下，为插件设置 Studio 工具栏按钮能够使其运行更为方便。为此，我们将需要使用 `Plugin/CreateToolbar|Plugin:CreateToolbar()` 和 `PluginToolbar/CreateButton|PluginToolbar:CreateButton()` 函数。

  1. 打开 **EmptyScriptAdder** 脚本并删除 `print("Hello world!")`。
  2. 将以下代码复制并粘贴到脚本中：

```    
    
    -- 创建名为 "Custom Script Tools" 的工具栏区域
    local toolbar = plugin:CreateToolbar("Custom Script Tools")
    
    -- 添加名为 "Create Empty Script" 的工具栏按钮
    local newScriptButton = toolbar:CreateButton("Create Empty Script", "Create an empty script", "rbxassetid://4458901886")


```
  3. 按照前述步骤保存插件（右键单击脚本并选择 **Save as Local Plugin（另存为本地插件）**）。完成后，新的按钮将会出现在 Studio 的 **Plugins（插件）**选项卡中。
![](https://developer.roblox.com/assets/blta9a06ee7c5a3bd18/Plugin-Toolbar-Button.png)



### 修改插件行为

之前创建的插件目前还没有任何功能，需要对其添加代码，使其能够创建 `Script` 实例且将示例的 `Script/Source` 属性设置为空字符串：

```    
    
    -- 创建名为 "Custom Script Tools" 的工具栏部分
    local toolbar = plugin:CreateToolbar("Custom Script Tools")
    
    -- 添加名为 "Create Empty Script" 的工具栏按钮
    local newScriptButton = toolbar:CreateButton("Create Empty Script", "Create an empty script", "rbxassetid://4458901886")
    
    local function onNewScriptButtonClicked()
    	local newScript = Instance.new("Script")
    	newScript.Source = ""
    	newScript.Parent = game:GetService("ServerScriptService")
    end
    newScriptButton.Click:Connect(onNewScriptButtonClicked)


```
再次通过 **Save as Local Plugin（另存为本地插件）**来保存插件。如果现在单击 **Create Empty Script（创建空脚本）**插件按钮，就可以将新建 `Script` 插入到 **ServerScriptService** 中。

![](https://developer.roblox.com/assets/bltd9dd1fcdc0e69a37/Plugin-Inserted-Script.png)



### 支持撤销/重做

Studio 中的撤销和重做由 `ChangeHistoryService` 中的 **Waypoint**（航点）进行管理。在 Studio 中执行每个操作之后（例入用户拖动部件或插入新对象后），Studio 会自动添加新航点。对操作进行撤销后，Studio 会返回到上一个航点并撤消该航点之后发生的所有操作。

需要注意的是，在默认情况下使用插件将**不会**添加任何新航点。如果用户在插件对场景进行更改后单击 **Undo（撤销）**，则 Studio 将会撤销上一个非插件操作**以及**其后插件所执行的所有操作。

为了确保 Studio 可以只撤销插件的操作，请参考下列步骤：

  1. 添加名为 `ChangeHistoryService` 的 `ChangeHistoryService` 本地变量。
  2. 在 `onNewScriptButtonClicked()` 函数的最后一行中调用 `ChangeHistoryService/SetWaypoint|SetWaypoint()`。

```    
    
    local ChangeHistoryService = game:GetService("ChangeHistoryService")
    
    -- 创建名为 "Custom Script Tools" 的工具栏部分
    local toolbar = plugin:CreateToolbar("Custom Script Tools")
    
    -- 添加名为 "Create Empty Script" 的工具栏按钮
    local newScriptButton = toolbar:CreateButton("Create Empty Script", "Create an empty script", "rbxassetid://4458901886")
    
    local function onNewScriptButtonClicked()
    	local newScript = Instance.new("Script")
    	newScript.Source = ""
    	newScript.Parent = game:GetService("ServerScriptService")
    	ChangeHistoryService:SetWaypoint("Added new empty script")
    end
    newScriptButton.Click:Connect(onNewScriptButtonClicked)


```
需要时开发者可以设置多个航点，让插件逐步撤回改动。为此，只需在每个允许用户撤销的步骤后调用 `ChangeHistoryService/SetWaypoint|SetWaypoint()` 即可。 

## 共享插件

有两种方式可与其他人共享插件：向其发送 Lua 脚本文件或将插件发布到 Roblox。

### 本地共享

通过 **Save as Local Plugin（另存为本地插件）**来保存插件时，Studio 会自动将其保存至 **Plugins**（插件）文件夹。单击 **Plugins Folder**（插件文件夹）按钮，即可访问该文件夹：

![](https://developer.roblox.com/assets/blt69975887711dde53/Plugin-Plugins-Folder.png)



打开文件夹后，开发者可以复制插件的脚本文件并进行分享。获取脚本文件后，将其置于本地 **Plugins** 文件夹中即可使用。

### 发布至 Roblox

开发者可以将插件发布至 Roblox（和场景与模型一样），以便轻松共享和安装。要发布插件，请执行以下操作：

  1. 右键单击 Studio 中的插件脚本并选择 **Publish as Plugin（发布为插件）**。
![](https://developer.roblox.com/assets/blt294f75c47ef1b021/Publish-As-Plugin.png)



  2. 发布到新栏位或更新现有插件之一。
  3. 输入插件的名称和描述。
  4. 单击 **Finish（完成）**。完成发布后，开发者将会获取该插件的链接，以便与想要使用插件的其他开发者分享。

## 其他插件示例

### 插入空文件夹

插件可以使用 `Selection` 服务找到用户所选中的对象。以下脚本引入了一个新的工具栏按钮，该按钮可检查用户是否选中任何对象，若是则将新的 `Folder`（文件夹）添加至该对象。

```    
    
    local ChangeHistoryService = game:GetService("ChangeHistoryService")
    local Selection = game:GetService("Selection")
    
    local toolbar = plugin:CreateToolbar("Folder Tools")
    local createFolderButton = toolbar:CreateButton("Create Folder", "Create a new folder", "rbxassetid://4459262762")
    
    local function onCreateFolder()
    	local selectedObjects = Selection:Get()
    	local parent = workspace
    	if #selectedObjects > 0 then
    		local firstSelection = selectedObjects[1]
    		parent = firstSelection
    	end
    
    	local newFolder = Instance.new("Folder")
    	newFolder.Parent = parent
    
    	Selection:Set({newFolder})
    
    	ChangeHistoryService:SetWaypoint("Added new folder")
    end
    createFolderButton.Click:Connect(onCreateFolder)


```


***__Roblox官方链接__:[插件简介](https://developer.roblox.com/zh-cn/articles/Intro-to-Plugins)