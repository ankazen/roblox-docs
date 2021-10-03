# 实体建模：使用部件进行 3D 建模 
Time:<em>10  分钟</em>

通过实体建模，开发者可以使用最为简单的部件（例如块状体、球体、楔状体及柱状体等）来创建十分复杂的游戏模型。对模型进行联合操作后，也可以大大减少游戏中的总部件数目，从而间接提升游戏性能。

![](https://developer.roblox.com/assets/blt7f953d87b4d85cb3/CSG-Door.jpg)

![](https://developer.roblox.com/assets/bltf6aa49515b1c492d/CSG-Potion.jpg)

![](https://developer.roblox.com/assets/bltbc68386edd12aa09/CSG-Gear.jpg)

## 建模操作

### Union（联合）

**Union**（联合）为实体建模中的主要操作。选中希望组合的部件后，单击 **Model**（模型）选项卡中的 **Union**（联合）选项，即可执行这一操作。组合完毕的部件将被转化为名为 **Union** 的新部件。

![](https://developer.roblox.com/assets/blt12f1f9b92d9773ec/CSG-Union-Button.png)



**联合**只能用于基础部件（块状体、球体、楔状体及柱状体），且这些部件下**不能**含有任何子项（如脚本或表面 GUI 等）。当试图对拥有子项的部件进行结合时，其子项将会从 `DataModel` 中隐藏。

### Negate（抵消）

实体建模的功能不仅是组合连接部件。通过 **Negate（抵消）**按钮可以将部件的一部分进行去除。若要使用该按钮，请选中一个部件，然后单击 **Model（模型）**选项卡中的 **Negate（抵消）**按钮。

![](https://developer.roblox.com/assets/blt7dc16d2d629426a6/CSG-Negate-Button.png)



此操作会将该部件转化为“抵消部件”（negative part），其外观将呈红色半透明状，以便区分。当使用**联合**工具组合抵消部件与正常部件时，抵消部件与正常部件重叠的部分将被切除。

注意：选中抵消部件后再次单击 **Negate（抵消）**即可回撤部件切除操作。 

### Separate（分离）

当希望对联合模型进行回撤（撤销操作）时，选中该模型并单击 **Separate（分离）**即可达到此目标。该操作将会分解已形成的联合，以便开发者对联合的大小和构造进行调整。

![](https://developer.roblox.com/assets/bltfcba9af76703c621/CSG-Separate-Button.png)



##### 实体建模的限制

  * If a union operation would result in a part with more than 5000 triangles, it will fail and Studio will alert you to the error in the **Output** window.
  * A unioned or negated part can only be scaled uniformly (all of the dimensions must be scaled at the same proportion). If you need to change just one part in a solid model, separate the model, transform the specific part, and redo the union process.

  


## 模型属性

### 细节等级

默认情况下，不管实体建模部件离镜头有多远，都将始终以精确保真度显示。虽然此特性可以改善从任何距离观察时的部件外观，但当场景中具有大量高细节实体建模部件时，可能会降低整体`articles/Improving Performance|游戏性能`。

若需要对实体建模部件的显示细节等级进行动态控制，请将其 `enum/RenderFidelity|RenderFidelity` 属性更改为 **Automatic**（自动）。此操作将导致部件根据其与镜头的距离以不同的细节等级进行渲染：

与镜头的距离 渲染保真度

低于 250 格
最高

250 至 500 格
中等

500 格或以上
最低

### 平滑操作

`PartOperation/SmoothingAngle|SmoothingAngle` 属性代表了实体建模部件上各面法线之间阈值的一个角度（单位为度）。当法线差异值小于此属性的值时将对相关法线进行调整，也就是对差异值进行平滑。通常来说，如果想要获取较好的结果，应当将此属性设为 30 至 70 度之间的一个值。将其设为 0 度时，模型边缘将会极为锐利；而将其设为 90 至 180 度时会在拥有锐利边缘的联合模型上产生一种“阴影”效果（虽然可以将属性设于此区间，但并不推荐其所产生的效果）。

![](https://developer.roblox.com/assets/blt53ff07ce0d5f1cf7/CSG-SmoothingAngle-0.png)

 SmoothingAngle : **0**

![](https://developer.roblox.com/assets/bltc1f5f51600953267/CSG-SmoothingAngle-50.png)

 SmoothingAngle : **50**

注意：当法线拥有不同材质或颜色时，将不会受到表面平滑的影响。 



***__Roblox官方链接__:[实体建模：使用部件进行 3D 建模](https://developer.roblox.com/zh-cn/articles/3D-Modeling-with-Parts)