# 合作式开发 
Time:<em>10  分钟</em>

**Team Create**（组队创作）为 Roblox Studio 中的工具之一，可以让多个开发者群组同时对场景和脚本进行编辑。启用组队创作后，拥有相应权限的开发者可以邀请其他人进行共同编辑，且每个编辑者都可以在工作过程中清楚地看到他人所做出的改动。

## 启用组队创作

要开始与其他开发者共同编辑场景时，请在 **View**（视图）选项卡中单击 **Team Create**（组队创作）：

![](https://developer.roblox.com/assets/blt184b664e309a7ddf/Team-Create-Button.png)



打开窗口后，按下 **Turn ON**（开启）按钮：

![](https://developer.roblox.com/assets/blta48f059e911dbde7/Enable-Team-Create.png)



组队创作启用后，此窗口会显示一个用户列表，包括了所有拥有场景编辑权限的用户。每个用户会被自动分配一个用户颜色（也就是用户虚拟形象图像背后的颜色）用来在编辑时进行标识。

![](https://developer.roblox.com/assets/bltf76bd37687e32a2a/Team-Create-User-List.png)



##### 聊天窗口

A useful tool while collaborating is the **Chat** panel, accessible via **View** → **Chat**.

![](https://developer.roblox.com/assets/blt67bd7828004d8a3d/Team-Create-Chat-Button.png)



To start chatting, click on the text box, type a message, and press Enter to send it. Messages in the chat window will be labeled by the user’s color outlined above.

  


## 管理编辑成员

### 群组游戏

如果你正在对`articles/Group Games|群组游戏`进行开发工作且拥有正确的`articles/Group Games#editing-roles|权限`，就可以依照下列步骤对编辑成员进行管理：

  1. 从 **Home**（主页）选项卡中进入 **Game Settings**（游戏设置）。
![](https://developer.roblox.com/assets/bltd6af44e38b951d0a/Game-Settings.png)



  2. 选中 **Permissions**（权限）选项卡。
  3. 在 **Game Owner**（游戏所有者）部分中，展开群组图标旁边的树型图。
![](https://developer.roblox.com/assets/blt3b24ef7811555348/Group-Permissions-Expand.png)



  4. 找到你想要添加编辑权限的每一个群组角色，从权限菜单中选择 **Edit**（编辑）。
![](https://developer.roblox.com/assets/blt1be093989a8ecf8e/Group-Permissions-Set.png)



  5. 点击 **Save**（保存）按钮来保留更改。

### 独立游戏

如果想和其他人一起合作但游戏并没有以`articles/Group Games|群组游戏`的方式发布，仍然可以按下列步骤添加编辑者：

  1. 从 **Home**（主页）选项卡中进入 **Game Settings**（游戏设置）。
![](https://developer.roblox.com/assets/bltd6af44e38b951d0a/Game-Settings.png)



  2. 选择 **Permissions**（权限）选项卡。
  3. 在 **Collaborators**（合作者）部分，按照 Roblox 用户名搜索一名编辑者并对其单击，将其添加为合作者。
![](https://developer.roblox.com/assets/blt0cac85b0ea18265a/Game-Collaborators-Find-User.png)



  4. 从权限菜单中选择 **Edit**（编辑）：
![](https://developer.roblox.com/assets/blt39102d055c00a06d/Game-Collaborators-User-Permission-Edit.png)



  5. 单击 **Save**（保存）按钮来保留变动的内容。

## 进入工作环节

被邀请对场景进行编辑的开发者可以按照以下步骤加入组队创作的工作环节：

  1. 在 Studio 中关闭所有当前已打开的场景（或者关闭并重新打开 Studio）。
  2. 选择 **Group Games**（群组游戏）选项卡（当游戏为`/articles/Group Games|群组游戏`时）或者 **Shared With Me**（与我共享）选项卡。
![](https://developer.roblox.com/assets/blt29827fa3542d7240/Team-Create-Select-Sorting-Tab.png)



  3. 找到并打开场景，开始编辑。

## 合作式构建

在组队创作的工作环节中，所有编辑者都可以操控对象，但其工作流程与单独编辑还是有细微差别的，请查阅以下章节详述：

### 用户颜色

之前提到过，环节中的每个编辑者都被分配了一种颜色，该颜色会成为在编辑者组队创作窗口中虚拟形象的背景，当一名编辑者选择对象时，一个有着自己颜色的选择框就会以 3D 视图的形式出现在对象周围：

![](https://developer.roblox.com/assets/bltdbfa5838f8046dcc/Team-Create-User-Color-Parts.jpg)

同理，管理器窗口中的对象也会显示出对应的颜色点，用来指明对其进行选中的编辑者。

![](https://developer.roblox.com/assets/bltcba06a170cecfc4b/Team-Create-User-Color-Explorer.png)



### Undo（撤销）/ Redo（重做）

撤销和重做基本上和它们在单人模式中的使用方式一样，但有一些小差异，如果有多个开发者对一个部件或者实例进行了编辑，那么当你对该对象进行 **Undo** （撤销）时，此对象将会撤回至你未对其做变更之前的状态，**同时**还会撤销你最后一次编辑后的其他编辑者所做出的修改。

## 合作式编辑脚本

在组队创作工作环节中，游戏脚本被存储在中央云存储 仓库里，该仓库可以由所有合作者访问。因此，合作者将得以进行以下操作：

  * 对其他开发者正在编辑的同一脚本进行独立处理。
  * 准确获悉其他开发者对脚本进行编辑的时间段。
  * 先在本地测试变动的内容，然后再提交给云端。
  * 将本地脚本提交至云端前对其进行比对。

在默认情况下合作式编辑脚本是启用的，若想对其进行禁用，选择**Game Settings（游戏设置）** → **Options（选项）**，然后关闭 **Enable Collaborative Editing（启用合作式编辑）**。若希望设置更改立即生效，需要关闭组队创作，然后对其重新启用来重启工作环节。 

### 编辑和测试

在组队创作环境中即使是其他用户正在对脚本进行编辑，开发者仍然可以按常规操作打开该脚本。对脚本做出改动后，该脚本将会被添加到 **Drafts**（草稿）窗口中。草稿会进行自动保存，且在同一机器上不会因为多次进入与退出 Studio 工作环节而丢失。

![](https://developer.roblox.com/assets/blt6a6285642469f6c2/Team-Create-Drafts-Window.png)



如果草稿窗口没有打开，可以通过点击 **View**（视图）选项卡中的 **Drafts**（草稿）按钮进行开启。 

在本地进行的游戏测试会使用**草稿**版本（而非服务器版本）的脚本。开发者可以籍此测试变动内容，而不影响其他合作者的工作进度。在进行**团队测试**环节时将会使用服务器版本脚本，具体说明详见`articles/game testing|游戏测试模式`。

### 脚本对照

开发者随时可以将草稿与对应的云端版本进行对照，只需右键单击草稿然后选择**Compare with server**（与服务器端对照）。

![](https://developer.roblox.com/assets/blt05990c9be27b6b77/Team-Create-Drafts-Compare.png)



此操作将会打开 **Diff Result**（差异结果）窗口。红色部分表示服务器端被改动或者删除的代码；绿色部分表示更新后的代码。开发者可以通过对比行号来决定该保留的内容。

![](https://developer.roblox.com/assets/bltecba0021f2ab9f9b/Team-Create-Diff-Result.png)



### 将编辑后的内容应用到服务器端

若想将更改后的内容应用至云端版本，请在 **Draft**（草稿）窗口中选择一个或多个草稿，右键单击后选择 **Commit**（提交）。

![](https://developer.roblox.com/assets/bltc1ebf2beafe4c237/Team-Create-Drafts-Commit.png)



### 合并更改内容

若开发者在对脚本进行编辑时有另外一名合作者对同一脚本提交了改动，**Draft**（草稿）窗口中此脚本的旁边将会显示绿色的 ![](https://developer.roblox.com/assets/bltb5160a07ace432d7/Team-Create-Updated-Icon.png)

 图标。

![](https://developer.roblox.com/assets/blt45b836a3f3771786/Team-Create-Script-Updated.png)



此时开发者可选择一个或者更多脚本，右键单击然后选择 **Merge from server**（从服务器端合并）打开合并工具窗口。在此窗口中可以看到和本地开发者编辑内容有关的最新编辑条目。如果有任何改动出现内容冲突，开发者可以选择希望保留的代码，也可以进行手动编辑。

![](https://developer.roblox.com/assets/blta555ce479e9a3873/Team-Create-Merge-Options.png)



  * 勾选 **Draft**（草稿）保留本地更改，未勾选时将会删除本地更改。
  * 勾选 **Server**（服务器）将更改合并至草稿中，未勾选时将会忽略所有服务器端更改。
  * 勾选 **Other**（其它）对脚本进行手动编辑，然后将更改保存至草稿。

勾选所需选项后，可以切换 **Preview Resolution**（预览解决方案）开关，预览脚本的变更情况。

![](https://developer.roblox.com/assets/blt70c0bf68f791584a/Team-Create-Merge-Preview.png)



### 恢复被删除的脚本

当本地开发者正在编辑脚本时，如果出现另一合作者删除当前脚本的情况，将会在 **Drafts**（草稿）窗口显示带有红色 ![](https://developer.roblox.com/assets/bltf61c0a8ce69aad48/Team-Create-Deleted-Icon.png)

 的图标：

![](https://developer.roblox.com/assets/bltaf78232b137b4613/Team-Create-Script-Deleted.png)



若想将本地脚本版本放回游戏中，请在 **Drafts**（草稿）窗口选中一个或更多草稿，对其右键单击后选择**Restore Script**（恢复脚本）。

注意：被恢复的脚本将会被放置回场景的 **Workspace** 中，因此需要将其父项重新设置为原有位置。 

## 发布和保存

在使用组队创作时对已变动的内容进行保存的过程与单人 Studio 下有些差异。启用组队创作时，Studio 将会以自动保存的方式每隔 5 分钟将内容投射到云端。在多个自动保存之间做出的变动将不会被发布，因此更新已发布游戏时，仍然需要通过**File（文件）** → **Publish to Roblox（发布至 Roblox）**来进行单独发布。

## 撤销改动

所有者可以将改动的内容恢复原样，与在单人模式下开发游戏时相同：

  1. 在游戏页面上单击 ![](https://developer.roblox.com/assets/blt738fe32bb9c285f9/Config-Dots.png)

 按钮。
  2. 选择 **Configure this Place（配置此场景）**。
  3. 单击 **Version History（版本历史）**。
  4. 选择更早的版本并单击 **Revert to this version（恢复至此版本）**来进行改动撤销。

用这种方式将改动内容恢复时一定要小心，如果目前有人在用组队创作编辑游戏，其工作环节将仍然能够进行自动保存并覆盖恢复操作。在进行版本恢复前，一定要确保目前没有人正在编辑游戏，或者直接关闭组队创作。 

## 关闭组队创作

游戏所有者或拥有正确`articles/Group Games#editing-roles|权限`的开发者可以关闭场景的组队创作功能。单击位于组队创作窗口最底端的 ![](https://developer.roblox.com/assets/bltc0570ac67590e30e/Team-Create-Menu-Dots.png)

 按钮并选择 **Disable Team Create（禁用组队创作）**后，工作环节中的任何其他用户都会被踢出，且在组队创作被重新启用前都将无法加入。

![](https://developer.roblox.com/assets/blt9e83d5dc6a9b9ae5/Disable-Team-Create.png)





***__Roblox官方链接__:[合作式开发](https://developer.roblox.com/zh-cn/articles/Team-Create)