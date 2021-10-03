# Beam（光束）简介 
Time:<em>5  分钟</em>

Beam（光束）是一种特殊效果对象，其作用为在两个 `Attachment` 对象之间渲染纹理。开发者可以对颜色、透明度、宽度、纹理和纹理速度等光束属性进行配置。

## 创建光束

光束的起点和终点都需要附着到一个部件。开始创建光束之前，需要通过 Model（模型） > Constraints（约束） > 启用 Constraint Details（约束详细信息），以确保 Attachment 可见。启用后，它将以灰色突出显示。

  1. **创建两个部件**作为光束的起点和终点。  
![游戏视图中的两个部件](https://developer.roblox.com/assets/bltfaf266b05c588903/TwoParts.png)


  2. **将两个部件编组**为一个 `Model`（选择两个部件然后按 Ctrl+G 或 ⌘+G）。  
![在管理器窗口中由两个部件组成的模型](https://developer.roblox.com/assets/blt20244fb8adf85220/ModelWithTwoParts.png)


  3. 使用 + 按钮为每个部件**插入附件**。  
![使用 + 按钮插入附件](https://developer.roblox.com/assets/bltf6eb54e381899d02/InsertAttachment.png)

 → ![在管理器窗口中，两个部件，每个带有两个附件](https://developer.roblox.com/assets/blt458e4e0c2c61efcc/TwoPartsWithAttachments.png)


  4. 将**一个 Beam 插入**模型。  
![将一个光束插入模型](https://developer.roblox.com/assets/bltdb06522c4c942fb7/InsertBeam.png)


  5. 选择光束，然后在属性窗口中向下滚动到 Attachment0/Attachment1 属性。单击该属性，然后单击先前创建的附件来**设置附件**。注意不要将附件属性分配给同一附件！  
![点击附件后的属性分配 Attachment0](https://developer.roblox.com/assets/blte6c779fb4835eaa4/AssigningAttachment0.png)


  6. 最后结果应为这样：  
![光束连接的两个部件](https://developer.roblox.com/assets/bltb1645f18c44aeeec/TwoPartsWithABeam2.png)



移动部件或其附件也会移动光束，因为附件点决定了光束的起点/终点。现在就可以开始测试光束属性了！开发者可以通过选择模型并按 Ctrl+D 或 ⌘+D 来复制该模型。创建光束时，请经常对其进行复制，以便可以比较所做出的修改。

## 视觉属性

光束最有用的属性或许就是 `Beam/Texture|Texture` 了，它沿光束的长度渲染 Texture（纹理）。下图中，绿色/粉色的三角形纹理被渲染。Texture 属性是一个 `articles/Content` 属性，如 `rbxassetid://3259097211`（如下图所示）。

![一个绿色/粉色三角形纹理，旁边是原始光束和应用了纹理的光束](https://developer.roblox.com/assets/blt66dd94d1bf0efb5e/BeamTexture.png)



### 使用序列的颜色和透明度

在光束上，有两个视觉属性您可以使用序列来定义：透明度和颜色。在 Studio 中，您可以通过单击属性窗口中的 […] 来配置这些属性。透明度属性是一个 `datatype/NumberSequence`，需使用折线图编辑。X 轴是沿光束长度的位置，Y 轴是该位置的透明度。单击图形上的任意位置可以添加一个新的关键点，拖动现有的关键点可以编辑或删除它们，Reset（重置）按钮会将序列更改回窗口打开时的状态。

![光束的透明度序列，范围为 0 到 1](https://developer.roblox.com/assets/blt5e517927e6e939fe/Beam.Transparency.png)



`Beam/Color` 的工作原理与此类似，但使用的是色标渐变。纹理沿光束长度以与 `ImageLabel/ImageColor3` 相同的方式着色。单击序列栏可以添加更多色标，单击色标可以选择它们，以更改它们的颜色、位置或删除它们。

![一个以从红到蓝的颜色渐变着色的光束](https://developer.roblox.com/assets/blt77ef6a0658d2143f/BeamColor.png)



## 光束几何形状

3D 内容都是用三角形渲染的；光束通过在两个分段之间绘制两个三角形来渲染其纹理。分段布置在两个 `Attachment` 方向之间，因此如果附件朝向不同的方向，分段就会扭曲。默认情况下光束使用 10 个分段，但您可以通过配置 `Beam/Segments|Segments` 属性进行更改。

![具有 5 个分段的两个光束，其中前景光束由于附件的方向而扭曲](https://developer.roblox.com/assets/blta47fff4777b882ed/BeamTwist.png)



上面的屏幕截图显示了两个光束，每个光束有 5 个分段。绿色/粉色三角形纹理在 5 个分段之间渲染 4 次。前景光束由于附件的轻微扭曲而扭曲。

### FaceCamera

开启 `Beam/FaceCamera|FaceCamera` 属性后，光束会自动调整角度面向镜头。

![两个光束，背景光束面向镜头](https://developer.roblox.com/assets/blt0c7153b75ec8b135/Beam.FaceCamera.png)



### Width0 和 Width1

您可以通过配置 `Beam/Width0|Width0`/`Beam/Width1|Width1` 属性在每个端点设置光束的宽度。

![一个在每个端点有不同宽度的光束](https://developer.roblox.com/assets/bltdccfd2f57a137cd5/BeamWidth-sm.png)



### CurveSize0 和 CurveSize1

您可以使用 `Beam/CurveSize0|CurveSize0`/`Beam/CurveSize1|CurveSize1` 属性来使光束相对附件的方向向上或向下弯曲。

![一个又大又漂亮的曲线光束](https://developer.roblox.com/assets/blt1e941db48a9a3560/Beam.CurveSize.png)





***__Roblox官方链接__:[Beam（光束）简介](https://developer.roblox.com/zh-cn/articles/intro-to-beams)