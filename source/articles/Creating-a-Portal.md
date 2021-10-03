# 创建传送门 
Time:<em>10  分钟</em>

在本教程中，你将创建以下大门的粒子效果：

![并排两个蓝色的旋转门，左边旋转门向内旋转，右边旋转门向外旋转](https://developer.roblox.com/assets/blteeafe0bf37fe85bc/portal_particle2.gif.gif)

# 步骤

  1. 在 Insert（插入）部分的 Home（主页）选项卡下，插入一个 `Part`。  
![Inserting a Part](https://developer.roblox.com/assets/blt9d8d6a8b75616bbd/InsertPart.png)

![The inserted part](https://developer.roblox.com/assets/blt594ca29a5b53c870/SelectedPart.png)


  2. 在 Constraints（约束）部分的 Model（模型）选项卡下，选择 `Attachment`。选择该工具后，在游戏视图中单击一次以创建一个附件对象。在管理器窗口中，请注意该对象如何成为部件的父级。  
![Creating an Attachment](https://developer.roblox.com/assets/blta997e49199217d1f/CreateAttachment.png)

![The newly created Attachment](https://developer.roblox.com/assets/bltda778cdc5cce9854/ExplorerAttachment.png)


  3. 在 Properties（属性）窗口中，将该 Attachment 的 `Attachment/Position` 设置为 0, 5, 0。这是该 Attachment 相对于父级部件的位置。  
![The Attachment's Position property in the Properties window](https://developer.roblox.com/assets/blt845025e49f8b244e/AttachmentPosition.png)


  4. 接下来，向该 Attachment 中添加一个 `ParticleEmitter`。选择该 Attachment，然后按 CTRL+I 以打开 Advanced Objects（高级对象）菜单。输入 “particle” 并找到 ParticleEmitter 将其插入。由于 ParticleEmitter 位于该 Attachment 中，因此将从附件点发射粒子。  
![The newly inserted ParticleEmitter](https://developer.roblox.com/assets/blt91f958744112caa8/NewParticleEmitter.png)


  5. 接下来，将 ParticleEmitter 的 `ParticleEmitter/Texture` 设置为以下旋转图像：  
`rbxassetid://145532427`
  6. 我们希望粒子以我们的附件为中心。因此，将 ParticleEmitter 的 `ParticleEmitter/Speed` 设置为 0 以便它们不移动。此外，如果附件移动，粒子也应该跟着移动。启用 LockedToPart 以便发生这种情况。
  7. 接下来，我们希望旋转从随机旋转开始。将 ParticleEmitter 的 `ParticleEmitter/Rotation` 属性设置为 0, 360。该属性是 `DataType/NumberRange`；当发射粒子时，在最小值和最大值之间选择一个随机数。 粒子现在应该看起来像这样：  
![Portal particle preview - step 7](https://developer.roblox.com/assets/blt03aa2a3148f8380f/PortalParticle0.png)


  8. 接下来，将 ParticleEmitter 的 `ParticleEmitter/LightEmission` 设置为 1。这会导致粒子混合在一起。纹理的黑色部分将透明地渲染。因为大门会发光，所以不应该受到环境照明的影响。同时将 `ParticleEmitter/LightInfluence` 设置 0。  
![Portal particle preview - step 8](https://developer.roblox.com/assets/blt03e0a4b6fdab4d4d/PortalParticle1.png)


  9. 旋转会在短时间内消失。将 ParticleEmitter 的 `ParticleEmitter/Lifetime` 设置为 2 秒。选择 `ParticleEmitter/Transparency` 属性并按出现的 […]。将出现一个图形。X 轴表示粒子的寿命，Y 轴表示粒子的透明度。  
![The ParticleEmitter Transparency graph - tweened from 0 to 1](https://developer.roblox.com/assets/blteecfcb61a7c15566/ParticleTransparencyLinear.png)


  10. 随着时间的推移，这些粒子的大小会逐渐增大。选择 `ParticleEmitter/Size` 属性并单击 […]。将“大小”设置为介于 0 和 5 之间的值。我们开始得到类似大门的东西。  
![Portal particle preview - step 10](https://developer.roblox.com/assets/bltcb3fb11ee1fd6f94/PortalParticle2.png)


  11. 现在我们需要旋转成为真正的旋转。将 `ParticleEmitter/RotSpeed` 设置为 -400, -320。旋转速度为负值，因此粒子会逆时针（即旋转的方向）旋转。  
![Portal particle preview - step 11](https://developer.roblox.com/assets/bltee28c5437582cdfc/PortalParticle4.png)


  12. 将部件的 `BasePart/Transparency` 设置为 1 以将其隐藏。  
好了！通过使用螺旋纹理和旋转速度，你可以创建一些非常独特的粒子效果。我们刚才做的效果是逆时针旋转，看起来像是一个“出口”大门。按照以下步骤创建类似的“入口”大门： 
    1. 通过在选中部件的情况下按 CTRL+D，复制上述步骤中的大门。将部件移到原始部件的侧面。将原始部件命名为 “ExitPortal”，将副本命名为 “EntrancePortal”。
    2. 翻转 `ParticleEmitter/Transparency` 属性。使其介于 1 和 0 之间。  
![Inverting the Transparency tween from 1 to 0](https://developer.roblox.com/assets/blt0b68e761b10c18a1/ParticleTransparencyLinearInverse.png)


    3. 同时翻转 `ParticleEmitter/Size`。  
![Inverting the Size tween](https://developer.roblox.com/assets/blt3f1663fabc76a3f4/ParticleSizeLinearInverse.png)


    4. 最后，取反 `ParticleEmitter/RotSpeed` 属性。由于原始范围是 -400 到 -320，因此将其设置为 320 到 400（取反和交换）。  
要下载成品，请单击此链接：[Finished Portals](https://www.roblox.com/library/1881797152)



***__Roblox官方链接__:[创建传送门](https://developer.roblox.com/zh-cn/articles/Creating-a-Portal)