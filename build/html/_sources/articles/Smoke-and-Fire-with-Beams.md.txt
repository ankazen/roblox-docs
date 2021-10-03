# 使用光束创建冒烟和起火的效果 
Time:<em>15  分钟</em>

在本教程中，你将学习：

  * 如何使用 `Beam` 对象创建自己的火焰效果
  * 如何在 `Part` 上创建 `Attachment` 并设置其位置
  * 如何在整个光束上设置光束的 `Beam/Color` 和 `Beam/Transparency`。
  * `Beam/LightEmission` 如何在两个 Beam 对象上起作用

![Tutorial final product](https://developer.roblox.com/assets/blt4217e95f14c2b6ca/FireBeamFinal.png)



# 步骤

  1. 在“Insert（插入）”部分的“Home（主页）”选项卡下，插入一个 `Part`。  
![Inserting a Part](https://developer.roblox.com/assets/blt9d8d6a8b75616bbd/InsertPart.png)

![Selected part](https://developer.roblox.com/assets/blt594ca29a5b53c870/SelectedPart.png)


  2. 在“Constraints（约束）”部分的“Model（模型）”选项卡下，选择 `Attachment`。在选中该工具的情况下，在游戏视图中两个不同的位置上单击你的 Part（部件）两次，可创建两个 Attachment（附件）对象。在“Explorer（管理器）”窗口中，观察这两个对象如何成为该 Part（部件）的父对象。  
![Creating an Attachment](https://developer.roblox.com/assets/blta997e49199217d1f/CreateAttachment.png)

![Created Attachments](https://developer.roblox.com/assets/blt36124a435b8fc831/NewAttachments.png)

![Attachments in the Explorer Window](https://developer.roblox.com/assets/bltdc2a7a19e7bfe406/AttachmentsExplorer.png)


  3. 将这两个附件重命名为 “Center” 和 “Top”。完成此操作的方法是，在“Explorer（管理器）”窗口中右键单击这两个附件，然后选择“Rename（重命名）”或按 F2。  
![Renamed Attachments in Explorer](https://developer.roblox.com/assets/bltd5bac421c190dd61/PartCenterTopAttachments.png)


  4. 选择 Center Attachment（中央附件）。在“Properties（属性）”窗口中，将其 `Attachment/Position` 设置为 0, 0, 0。将 Top Attachment （顶部附件）的 Position 设置为 0, 10, 0。Position（位置）会相对于 Part（部件）重定位附件。  
![Attachment Position in the Properties Window](https://developer.roblox.com/assets/blt845025e49f8b244e/AttachmentPosition.png)


  5. 选择该 Part（部件）。在“Effects（效果）”下拉列表中“Gameplay（游戏）”部分的“Model（模型）”选项卡下，插入一个 `Beam` 对象。  
![Inserting a Beam effect](https://developer.roblox.com/assets/blt6b3526fa8e24c5aa/InsertBeam.png)

![Beam in the Explorer window](https://developer.roblox.com/assets/blt42707ed26a9d7b4c/Beam.png)


  6. 这个新的 Beam 将在插入时被选中。在“Properties（属性）”窗口中，在这个新的 Beam 被选中的情况下，将 `Beam/Attachment0` 属性设置为 Center Attachment（中央附件）并且将 `Beam/Attachment1` 属性设置为 Top Attachment（顶部附件）。  
**提示：** 若要设置对象引用属性（例如 Attachment0 和 Attachment1），请单击该属性右侧的空格。然后，单击“Explorer（管理器）”窗口中的对象，或单击 X 以清除该属性。  
设置这两个属性后，光束将在游戏视图中的部件上渲染。应该如下所示：  
![Beam preview - step 6](https://developer.roblox.com/assets/bltbb8337d1c91fdd12/FireBeam0.png)


  7. 将 Beam 的 `Beam/Texture` 属性设置为以下值：  
`rbxassetid://1849531275` ([Preview](https://i.imgur.com/I54FaUj.png)

)  
此纹理是 128 × 1024 重复的透明白色烟雾纹理。  
**提示：** 你只需粘贴数字部分（资源 ID），Roblox Studio 会填写前缀。  
设置后，光束将立即渲染纹理。由于 Beam 的 TextureSpeed 属性（默认情况下是，设置为 1），因此它还会向上移动。  
![Beam preview - step 7](https://developer.roblox.com/assets/blt6cec1fd894f5f40f/FireBeam1.png)


  8. 将 Beam 的 `Beam/Width0` 属性设置为 4，并将 `Beam/Width1` 属性设置为 8。这将使光束呈圆锥形渲染，在底部变细，在顶部变宽。  
![Beam preview - step 8](https://developer.roblox.com/assets/blt7287dcbef2a54652/FireBeam2.png)


  9. 接下来，在“Properties（属性）”窗口中选择 Beam 的 `Beam/Transparency` 属性。单击该属性，当你要输入数字时，请改为单击出现在字段右侧的 […]。  
![Beam Transparency Field](https://developer.roblox.com/assets/blt18e0c039589bf4a0/BeamTransparencyField.png)

  
此时将出现一个折线图。这是用于 `DataType/NumberSequence` 类型字段的编辑器。对于 Transparency（透明度），X 轴代表从 Attachment0 到 Attachment1 渲染的光束中的位置。 Y 轴代表该位置处光束的 Transparency（透明度）。默认情况下，在整个 Beam 中该值为 0.5，如 0.5 处的水平线显示。  
![Beam Transparency Graph - Constant](https://developer.roblox.com/assets/blt19c8e68c4a4c96bc/BeamTransparencyGraphConstant.png)

  
将鼠标悬停在左侧点（Time = 0 处）以将其选中。通过将它拖动到折线图的底部，将它的值设置为 0。将右侧点（Time = 1 处）的值设置为 1。这将导致 Beam（光束）在 Attachment0 附近完全不透明地渲染，并在 Attachment1 附近逐渐消失。该图现在应如下所示：  
![Beam Transparency Graph - Linear](https://developer.roblox.com/assets/blt443b7094406af408/BeamTransparencyGraphLinear.png)

  
光束现在会像这样。注意 Attachment1 附近的光束顶部没有硬边。  
![Beam preview - step 9](https://developer.roblox.com/assets/blt5c580e0ff7fbd0da/FireBeam3.png)


  10. 选择光束的 `Beam/Color` 属性。与透明度非常相似，你可以在编辑时单击 […] 打开 `DataType/ColorSequence` 编辑器。与透明度类似，此图根据位置确定光束的 `Beam/Texture` 的颜色。  
![Beam Color Graph](https://developer.roblox.com/assets/blt77eb559373dabcaa/BeamColorWhite.png)

  
我们希望光束从白色渐变为橙色再到红色。单击右侧的色块（Time = 1 处）以将其选中，然后单击 Color（颜色）将颜色更改为红色。对左侧的色块（Time = 0 处）进行相同的操作，将颜色更改为黄色。  
![Beam Color Graph - Gradient](https://developer.roblox.com/assets/blt409036ff45b2fab6/BeamColorGradient.png)

  
现在，光束将从 Attachment0 到 Attachment1 从黄色混合为红色，中间为橙色。它看起来像这样：  
![Beam preview - step 10](https://developer.roblox.com/assets/blt464640f2aa2b8250/FireBeam4.png)


  11. 启用光束的 `Beam/FaceCamera` 属性。这将导致在 Attachment0-Attachment1 行上旋转光束的 2D 面，以使光束始终面向 `Camera`。尝试从不同的镜头角度查看光束，以了解此属性的工作方式。
  12. 将光束的 `Beam/LightEmission` 属性更改为 1。光束会显得稍微亮一些，因为 LightEmission 导致光束使用 [加法混合] (<https://en.wikipedia.org/wiki/Blend_modes#Addition>) 进行渲染。  
![Beam LightEmission and TextureSpeed in Properties window](https://developer.roblox.com/assets/blt9c1947391da0330f/BeamLightEmissionTextureSpeed.png)


  13. 将光束的 `Beam/TextureSpeed` 更改为 0.4 并将光束重命名为 BeamA。按 CTRL+D 复制该光束并将副本重命名为 BeamB。将 BeamB 的 TextureSpeed 更改为 0.8。现在，该部件的外观将明显变亮，因为有两个使用了加法混合的光束。BeamB 的纹理移动速度比 BeamA 的快，因此当纹理的颜色混合时，它们会产生一种烟雾效果。  
![Beam preview - Step 13](https://developer.roblox.com/assets/bltbbc54333c259be9c/FireBeam5.png)


  14. 在选中该部件的情况下，添加一个 `Smoke` 对象（通过“Gameplay（游戏）”部分的“Model（模型）”选项卡下的“Effects（效果）”菜单）：  
![Inserting a Smoke object](https://developer.roblox.com/assets/blt5ab023c5d7e6b687/InsertSmoke.png)


  15. 对于 Smoke 对象，将 `Smoke/RiseVelocity` 设置为 5，将 Opacity 设置为 0.2 并将 `Smoke/Color` 设置为黑色。这将对比 Beam 对象的明亮颜色。  
![Beam preview - step 15](https://developer.roblox.com/assets/bltc17afcb031ff63ab/FireBeam6.png)


  16. 现在开始创造吧！开始摆弄在前面步骤中设置的属性。这里有一些想法。 
    1. 尝试在 0, 15, 0 处创建一个名为 Top2 的新 `Attachment` 并将 BeamB 的 Attachment1 设置为这个新附件。这将导致一些火焰升得更高。
    2. 将 Part 的 `BasePart/Transparency` 设置为 1 以便它不可见。注意底部的硬边。尝试设置 Transparency 以便光束在 Attachment0 附近消失。  
![A customized Transparency graph](https://developer.roblox.com/assets/blt0c492617d513b817/BeamTransparencyGraphCustom.png)


    3. 在选中 Center Attachment 的情况下，在“Effects（效果）”下添加一个 `PointLight` 对象。将它的 `PointLight/Color` 设置为橙色，将它的 Range 设置为 12。  
![Inserting a PointLight](https://developer.roblox.com/assets/blt11a4320b31f96251/InsertPointLight.png)


    4. 尝试不同的 `Beam/Texture`！下面是一缕透明的白色烟雾。将 BeamB 的 TextureLength 设置为 1.25，将它的 Texture 设置为以下值：  
`rbxassetid://1525327413` ([Preview](https://i.imgur.com/wZza97B.png)

)
  17. 下面是执行上述步骤时效果的免费模型链接：[Final Product](https://www.roblox.com/library/1880281999)

这是我玩了几分钟后想出的光束发射效果的一种变化。看看你是否可以重新创建它。  
**提示：** 每次你改变内容时都要复制你的效果。这样你可以回到一个更基本的效果版本。  
![Pink fire Beam effect - try recreating me!](https://developer.roblox.com/assets/blt852194554d15fe8d/PinkFireBeamExample.png)





***__Roblox官方链接__:[使用光束创建冒烟和起火的效果](https://developer.roblox.com/zh-cn/articles/Smoke-and-Fire-with-Beams)