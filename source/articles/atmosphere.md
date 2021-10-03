# Atmosphere（氛围）掌控 
Time:<em>5  分钟</em>

`Atmosphere`（氛围）对象可以通过调整 Density（密度）等各种空气粒子属性来改变日光等光线的发散形态，从而帮助开发者在 Roblox 中创建更为真实的游戏环境。此对象可以模拟真实世界中的“空气透视”现象，并允许开发者对天空背景与远处对象的透光性进行控制。不仅如此，通过 Atmosphere 对象还能对 Haze（雾气）与 Glare（眩光）等条件进行操控，从而打造出完美澎湃的日落或雾气朦胧的下午等各种场景。

## 设置选项

若想对氛围进行设置，需要用到 `Lighting` 服务中的 `Sky` 和 `Atmosphere` 对象。如果服务中尚未存在上述对象，请将其进行插入。

![](https://developer.roblox.com/assets/bltdd45b4547def9101/Atmosphere-Sky-Objects.png)



## Atmosphere（氛围）属性

### Density （密度）

`Atmosphere/Density|Density` （密度）定义了空气中存在粒子的数目。密度越高，粒子也就越多，游戏内的对象或地形也就会因为被这些粒子遮蔽而变得越为朦胧模糊。需要注意的是，Density（密度）并不会**直接**作用于 `articles/Custom Skyboxes|Skybox`（天空盒），而是只作用于游戏内的对象或地形，并通过对其进行操控而影响 Skybox（天空盒）的可见程度。

Density（密度）= 0 Density（密度）= 0.35

![](https://developer.roblox.com/assets/bltf99d55d704c3d0b6/Atmosphere-Density-A.jpg)

![](https://developer.roblox.com/assets/blt6b8b16519d05e550/Atmosphere-Density-B.jpg)

### Offset（偏移）

`Atmosphere/Offset|Offset`（偏移）控制了光照在镜头与天空背景间的照射方式。可以通过增加偏移值来创造日落时天边清晰可见的晚霞，也可以通过减少偏移值来将远处的对象与天空背景进行融合，创造广阔无垠的开阔世界。

Offset（偏移）= 0 Offset（偏移）= 1

![](https://developer.roblox.com/assets/blt8bcf21dadce6c222/Atmosphere-Offset-A.jpg)

![](https://developer.roblox.com/assets/blt06e241270abbf082/Atmosphere-Offset-B.jpg)

需要注意的是，在调整 Offset（偏移）属性时要与 `Atmosphere/Density|Density`（密度）属性进行平衡，并在场景中进行仔细测试。当偏移值过低时，可能会导致天空盒透过对象或地形显示。此类问题可以通过增加偏移值进行修复。虽然偏移值可以让远处的对象或地形与天空背景的对比更为清晰，但当偏移值过高时可能会出现远处地形或网格的细节层次显示不均的现象。 

### Haze（雾气）

`Atmosphere/Haze|Haze`（雾气）定义了环境氛围的雾气浓度，对地平线以上及远处的环境氛围都有影响。与 `Atmosphere/Color|Color`（颜色）属性共同使用时，可以用来创建特定的环境氛围，例如污染严重的外星星球表面的雾霾等。

Haze（雾气）= 1 Haze（雾气）= 2.8

![](https://developer.roblox.com/assets/blt9c7bbb3698988ef3/Atmosphere-Haze-A.jpg)

![](https://developer.roblox.com/assets/blt40e8e32caec63528/Atmosphere-Haze-B.jpg)

### Color（颜色）

`Atmosphere/Color|Color`（颜色）属性可以用来改变氛围色调，潜移默化地影响环境氛围。推荐将此属性与 `Atmosphere/Haze|Haze`（雾气）属性同时使用，以扩展可见效果。

Color（颜色） = [255, 255, 255] Color（颜色） = [250, 200, 255]

![](https://developer.roblox.com/assets/blt8d36b3ccf5bb8919/Atmosphere-Color-A.jpg)

![](https://developer.roblox.com/assets/bltc42075d69e827e8d/Atmosphere-Color-B.jpg)

### Glare（眩光）

`Atmosphere/Glare|Glare`（眩光）指定了太阳光源周围的氛围光或眩光。眩光值增加时，体现在天空与世界中的阳光照射强度也将会随之增加。

Glare（眩光）= 0 Glare（眩光）= 1

![](https://developer.roblox.com/assets/bltb5567a982b107e42/Atmosphere-Glare-A.jpg)

![](https://developer.roblox.com/assets/blt8c0ba9496ed24b54/Atmosphere-Glare-B.jpg)

当使用 `Atmosphere/Glare|Glare`（眩光）属性时，需要同时将 `Atmosphere/Haze|Haze`（雾气）等级设置为 0 以上才会显示眩光效果。 

### Decay（衰减）

`Atmosphere/Decay|Decay`（衰减）定义了远离太阳的气氛色调。当太阳根据 `Lighting/ClockTime|ClockTime` 或 `Lighting/TimeOfDay|TimeOfDay` 在天空中移动时，逐渐远离太阳的区域氛围将会从 `Atmosphere/Color|Color`（颜色）属性所指定的颜色向衰减值进行过渡。

Decay（衰减）= [255, 255, 255] Decay（衰减）= [255, 90, 80]

![](https://developer.roblox.com/assets/blt8c0ba9496ed24b54/Atmosphere-Glare-B.jpg)

![](https://developer.roblox.com/assets/bltb3c09e390b8fe81f/Atmosphere-Decay-B.jpg)

使用 `Atmosphere/Decay|Decay`（衰减）属性时，场景中的 `Atmosphere/Haze|Haze`（雾气）和 `Atmosphere/Glare|Glare`（眩光）程度必须要大于 0，否则衰减将不会产生任何效果。 

### 撒哈拉日落

![](https://developer.roblox.com/assets/blt3b93ef7813d00089/Atmosphere-Sahara-Sunset.jpg)

Lighting（光照） Atmosphere（氛围） Sky（天空） Color Correction（颜色修正） Sun Rays（太阳光束）

**Lighting（光照）**

OutdoorAmbient

[100, 70, 70]

ClockTime
17.7

**Atmosphere（氛围）** （**Lighting** 的子项）

Density（密度）
0.35

Color（颜色）

[250, 180, 120]

Decay（衰减）

[255, 0, 200]

Glare（眩光）
1

Haze（雾气）
2.1

**Sky（天空）** （**Lighting** 的子项）

SunAngluarSize
16

**ColorCorrection（颜色修正）** （**Lighting** 的子项）

Contrast（对比）
2

Saturation（饱和）
0.2

TintColor

[200, 150, 220]

**SunRays（太阳光束）** （**Lighting** 的子项）

Intensity（强度）
0.08

Spread（分散）
0.75



***__Roblox官方链接__:[Atmosphere（氛围）掌控](https://developer.roblox.com/zh-cn/articles/atmosphere)