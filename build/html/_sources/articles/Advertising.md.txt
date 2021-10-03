# 游戏与物品广告 
Time:<em>5  分钟</em>

Roblox 允许开发人员为游戏、目录物品、`articles/Group Games|群组`等项目上传自定义图像广告。用户单击广告后，将会被导向你所宣传的项目页面。

## 竞价系统

开发人员并不能直接在 Roblox 购买广告空间，而是需要以**拍卖**的形式为空间进行竞价。由于可用的广告空间有限，竞拍成交价格越高的广告曝光率（显示次数）也就越高。

举例来说，目前系统中共有 3 条广告（实际情况下常会有数百条广告共同存在）：

广告 竞拍价格 结果

**A**
![](https://developer.roblox.com/assets/blt0fffb3baccc585f5/Robux-Icon-Small.png)

300
此广告的出现率将会是 **B** 的 3 倍，同时会是 **C** 的 6 倍。

**B**
![](https://developer.roblox.com/assets/blt0fffb3baccc585f5/Robux-Icon-Small.png)

100
此广告的出现率将会是 **C** 的 2 倍。

**C**
![](https://developer.roblox.com/assets/blt0fffb3baccc585f5/Robux-Icon-Small.png)

50
—

## 广告类型

广告的展示类型共有三种：**banners**（横幅）、**skyscrapers**（竖幅）、以及 **rectangles**（矩形）。由于其形状不同，横幅广告不能占用竖幅广告的位置，反之亦然。因此，每个不同的广告类型都拥有其独立的竞拍系统，也就是说上面示例的竞拍系统共有 3 个之多。

种类 尺寸 位置

**Banner（横幅）**
728×90
Roblox 网站页面的顶部或底部。

**Skyscraper（竖幅）**
160×600
Roblox 网站页面的左侧或右侧。

**Rectangle（矩形）**
300×250
Roblox 网站页面的右侧或底部。

## 创建广告

若想开始创建广告，请前往 [Create（创建）](https://www.roblox.com/develop)页面，找到想要宣传的项目并单击其右边的齿轮图标，选择 **Advertise**（广告）进入新的页面。开发人员将可以在此处获取广告模板并上传自己的广告。

![](https://developer.roblox.com/assets/blt3463a25683b83c6f/Create-User-Ad.png)



如果浏览器中正在运行广告拦截程序，在上传广告前需将其暂时关闭。 

上传广告时，请遵循以下步骤：

  1. 填写广告名称（当用户将鼠标光标悬停至广告上时将会显示此名称）。
  2. 在上传区域拖拽或上传图像文件。
  3. 单击 **Upload**（上传）按钮。

## 投放广告

创建并上传至少一个广告后，就可以按照下列步骤开始一轮广告投放了：

  1. 返回 [Create（创建）](https://www.roblox.com/develop)页面，点击 **User Ads**（用户广告）选项卡。
  2. 点击右侧齿轮图标，在弹出式菜单中选择 **Run Ad**（投放广告）。
  3. 输入以 Robux 为单位的竞价数目。
  4. 点击 **Run**（投放）开始此轮广告投放。

每一轮广告投放时长为 24 小时，广告出现概率将会由该时段竞价系统决定。 



***__Roblox官方链接__:[游戏与物品广告](https://developer.roblox.com/zh-cn/articles/Advertising)