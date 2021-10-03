# CFrame 数学运算 
Time:<em>15  分钟</em>

阅读本文章前需要具备较为深厚的向量和向量数学知识。请刚接触 CFrame 的开发者先从`articles/Understanding CFrame|了解 CFrames`一文开始阅读。 

## CFrame 的分量

每个 CFrame 都由 12 个单独的数字组成，我们称其为分量。当需要获取这些数字时，只需调用能够将其作为结果返回的 `CFrame:components()` 方法即可。
    
    
    local x, y, z, m11, m12, m13, m21, m22, m23, m31, m32, m33 = cf:components()
    

当定义 CFrame 时，开发者也可以直接输入这 12 个数字。
    
    
    local cf = CFrame.new(x, y, z, m11, m12, m13, m21, m22, m23, m31, m32, m33)
    

12 个数字中的前三个分别为 CFrame 的 x、y 和 z 分量，也就是其中包含的坐标位置。剩余的数字组成了 CFrame 的旋转方位。这些数字看上去可能有些复杂，但当我们对其换个方式稍加整理就会发现，这些数列分别代表的是 rightVector、upVector 和负 lookVector。
    
    
    local cf = CFrame.new(0, 0, 0)
    local x, y, z, m11, m12, m13, m21, m22, m23, m31, m32, m33 = cf:components()
    
    -- m11, m12, m13,
    -- m21, m22, m23,
    -- m31, m32, m33
    
    local right = Vector3.new(m11, m21, m31) -- 与 cf.rightVector 相同
    local up = Vector3.new(m12, m22, m32) -- 与 cf.upVector 相同
    local back = Vector3.new(m13, m23, m33) -- 与 -cf.lookVecto 相同
    

对这些向量进行视觉化后，我们将可以更轻易地体会 CFrame 旋转数值的实际效果。从下图中可以看到这些数字代表的是三个正交向量，它们共同描绘了一个 3D 球体状旋转范围。

![CFrame Axes](https://developer.roblox.com/assets/blt0d5070611917410a/CFrameMath_rotationVectors-compressor.gif)

## CFrame * CFrame

CFrame 实际上是采用以下形式的 4x4 矩阵：

![CFrameMath_cf4x4.png](https://developer.roblox.com/assets/blt13db5c99d3faf61f/CFrameMath_cf4x4.png)



也就是说，我们只需将两个 4x4 的矩阵相乘，就能轻松地将两个 CFrame 相乘！

![CFrameMath_cf4x4Multiply2.png](https://developer.roblox.com/assets/bltd549ef4a34baeda7/CFrameMath_cf4x4Multiply2.png)



这样我们就能编写出用于将两个 CFrame 相乘的函数！
    
    
    local function multiplyCFrame(a, b)
    	local ax, ay, az, a11, a12, a13, a21, a22, a23, a31, a32, a33 = a:components()
    	local bx, by, bz, b11, b12, b13, b21, b22, b23, b31, b32, b33 = b:components()
    	local m11 = a11*b11+a12*b21+a13*b31
    	local m12 = a11*b12+a12*b22+a13*b32
    	local m13 = a11*b13+a12*b23+a13*b33
    	local x = a11*bx+a12*by+a13*bz+ax
    	local m21 = a21*b11+a22*b21+a23*b31
    	local m22 = a21*b12+a22*b22+a23*b32
    	local m23 = a21*b13+a22*b23+a23*b33
    	local y = a21*bx+a22*by+a23*bz+ay
    	local m31 = a31*b11+a32*b21+a33*b31
    	local m32 = a31*b12+a32*b22+a33*b32
    	local m33 = a31*b13+a32*b23+a33*b33
    	local z = a31*bx+a32*by+a33*bz+az
    	return CFrame.new(x, y, z, m11, m12, m13, m21, m22, m23, m31, m32, m33)
    end
    

我们还可以通过循环到达同样的结果：
    
    
    local function multiply4x4(a, b)
    	local out = {}
    	for i = 1, 16 do
    		out[i] = 0
    		local r = math.floor((i-1)/4)+1
    		local p = i%4 == 0 and 4 or i%4
    		for j = 1, 4 do
    			local ai = (r-1)*4+j
    			local bi = p+(j-1)*4
    			out[i] = out[i] + a[ai]*b[bi]
    		end
    	end
    	return out
    end
     
    local function multiplyCFrame(a, b)
    	local ax, ay, az, a11, a12, a13, a21, a22, a23, a31, a32, a33 = a:components()
    	local bx, by, bz, b11, b12, b13, b21, b22, b23, b31, b32, b33 = b:components()
    	a = {a11, a12, a13, ax, a21, a22, a23, ay, a31, a32, a33, az, 0, 0, 0, 1}
    	b = {b11, b12, b13, bx, b21, b22, b23, by, b31, b32, b33, bz, 0, 0, 0, 1}
    	local m11, m12, m13, x, m21, m22, m23, y, m31, m32, m33, z = unpack(multiply4x4(a, b))
    	return CFrame.new(x, y, z, m11, m12, m13, m21, m22, m23, m31, m32, m33)
    end
    

最后让我们来进行验证测试
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32));
    
    print(cf*cf)
    print(multiplyCFrame(cf, cf))
    
    
    
    4.44273901, 3.34623194, 2.4210279, -0.849777162, -0.0723331869, 0.522155881, -0.316965073, 0.861586094, -0.396487743, -0.421203077, -0.502431393, -0.755083263
    4.44273901, 3.34623194, 2.4210279, -0.849777162, -0.0723331869, 0.522155941, -0.316965073, 0.861586154, -0.396487743, -0.421203077, -0.502431393, -0.755083263
    

进行 CFrame 相乘时有一点十分重要：CFrame 的乘数是不能互换的。换而言之，a * b 并不一定等于 b * a。
    
    
    local cf1 = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    local cf2 = CFrame.new(0.1, -10, 6) * CFrame.Angles(math.rad(90), math.rad(-28), math.rad(-86))
    
    print(cf1*cf2)
    print(cf2*cf1)
    
    
    
    5.09500504, -7.92827415, 7.54646206, -0.937961817, 0.220474482, -0.26761657, 0.0239842981, -0.728708208, -0.684404194, -0.345908046, -0.64836365, 0.678212643
    0.514770269, -13.618248, 5.1419487, 0.162701935, 0.975506902, -0.148035079, 0.94501543, -0.197204709, -0.260875672, -0.283679247, -0.0974504724, -0.953954697
    

这项规则也有几种例外情况，其中一种是逆运算，我们稍后再做讨论，而另一种就是我们现在要谈到的身份识别 CFrame。

身份识别 CFrame 如下所示：
    
    
    local identityCFrame = CFrame.new(0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1)
    -- note: CFrame.new(0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1) == CFrame.new()
    

如果我们自前或自后用 CFrame 乘以身份识别 CFrame，我们只会得到原来的 CFrame，就像从未进行过乘法运算一样。
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    
    print(cf*CFrame.new())
    print(CFrame.new()*cf)
    
    
    
    1, 2, 3, 0.262061268, 0.163754046, 0.95105654, -0.319058299, 0.944782019, -0.0747579709, -0.910783052, -0.283851326, 0.299837857
    1, 2, 3, 0.262061268, 0.163754046, 0.95105654, -0.319058299, 0.944782019, -0.0747579709, -0.910783052, -0.283851326, 0.299837857
    

## CFrame * Vector3

我们已经知道 CFrame 实际上是 4x4 的矩阵，那么下面就让我们来看看如何将其与向量相乘。CFrame 与 Vector3 的乘法运算用矩阵形式表现是这样的。

![CFrameMath_cfv3Multiply.png](https://developer.roblox.com/assets/bltf1a4d51278a9ac43/CFrameMath_cfv3Multiply.png)



因此我们可以编写下列函数
    
    
    local function multiplycfv3(a, b)
    	local x, y, z, m11, m12, m13, m21, m22, m23, m31, m32, m33 = a:components()
    	local vx, vy, vz = b.x, b.y, b.z
    	local nx = m11*vx+m12*vy+m13*vz+x
    	local ny = m21*vx+m22*vy+m23*vz+y
    	local nz = m31*vx+m32*vy+m33*vz+z
    	return Vector3.new(nx, ny, nz)
    end
    

下面让我们再次来进行测试。
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    local v3 = Vector3.new(5, 6, -12)
    
    print(cf*v3)
    print(multiplycfv3(cf, v3))
    
    
    
    -8.11984825, 6.97049618, -6.85507774
    -8.11984825, 6.97049618, -6.85507774
    

与 CFrame 间互乘不同，CFrame * Vector3 的乘法可以拆分为更加直观的形式。让我们来对表示法稍作调整。

![CFrameMath_cfv3Multiply2.png](https://developer.roblox.com/assets/bltf6737a3183a6d02e/CFrameMath_cfv3Multiply2.png)



是否注意到我们用来与 vx、vy 和 vz 相乘的向量？它们就是我们早些时候学习到的 right、up 和 back 向量！下面让我们来重写函数，反应这一知识。
    
    
    local function multiplycfv3(a, b)
    	return a.p + b.x*a.rightVector + b.y*a.upVector - b.z*a.lookVector
    end
    

这也有助于我们将运算的实际意义以视觉化方式呈现。

![CFrameMath_cfv3MultiplyVisual.png](https://developer.roblox.com/assets/blt7538fe0aca619bb2/CFrameMath_cfv3MultiplyVisual.png)



## CFrame + / - Vector3

在 CFrame 上加上或减去 Vector3 是十分直观的运算。我们只需在 CFrame x、y 和 z 上加/减向量 x、y 和 z，而旋转方位则保持不变。
    
    
    local function addcfv3(a, b)
    	local x, y, z, m11, m12, m13, m21, m22, m23, m31, m32, m33 = a:components()
    	return CFrame.new(x + b.x, y + b.y, z + b.z, m11, m12, m13, m21, m22, m23, m31, m32, m33);
    end;
    

当然也需要进行测试。
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    local v3 = Vector3.new(5, 6, -12)
    
    print(cf + v3)
    print(addcfv3(cf, v3))
    
    
    
    6, 8, -9, 0.262061268, 0.163754046, 0.95105654, -0.319058299, 0.944782019, -0.0747579709, -0.910783052, -0.283851326, 0.299837857
    6, 8, -9, 0.262061268, 0.163754046, 0.95105654, -0.319058299, 0.944782019, -0.0747579709, -0.910783052, -0.283851326, 0.299837857
    

#### CFrame 的逆运算

CFrame 的逆运算对于大多数人来说都有一定难度。我们将不会在本文中介绍具体如何进行逆运算，而是会着重解说逆运算的使用方法。

我们在 CFrame 互乘章节最后曾提到，乘法的乘数并非总是能够互换。对于乘以派生于自身 CFrame 的 CFrame 逆运算来说，这一条并**不**适用。无论开发者自前还是自后用 CFrame 乘以其逆运算，**始终**都会返回身份识别 CFrame！
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.pi/2, 0, 0)
    
    print(cf*cf:inverse())
    print(cf:inverse()*cf)
    
    
    
    0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1
    0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1
    

运用 CFrame 逆运算的窍门就是写出等式，然后运用我们所掌握的身份识别 CFrame 和 CFrame 乘数不可互换属性等相关知识。让我们来看几个示例。

### 还原为初始值

假设我们有两个 CFrame，并将其相乘得出一个新的 CFrame。
    
    
    local cf1 = CFrame.new(1, 2, 3) * CFrame.Angles(math.pi/3, math.pi/6, 0)
    local cf2 = CFrame.new(-4, 5, 7.2) * CFrame.Angles(0, math.pi/7, -math.pi/3)
    
    local cf = cf1 * cf2
    

假设仅给定了 cf 和 cf1，而我们希望求出 cf2。要如何才能做到？要着手解决该问题，我们就要看一下 cf 的等式。
    
    
    cf = cf1 * cf2
    

然后我们就可以应用自己掌握的逆运算知识来求得 cf2。
    
    
    cf = cf1 * cf2
    cf1:inverse() * cf = cf1:inverse() * cf1 * cf2 -- 自前以 cf1:inverse() 相乘等式两边
    cf1:inverse() * cf = CFrame.new() * cf2 -- 注意 cf:inverse() * cf = identityCFrame
    cf1:inverse() * cf = cf2 -- 注意 identityCFrame * cf = cf
    

毫无疑问，我们能通过测试验证这一结果。
    
    
    local cf1 = CFrame.new(1, 2, 3) * CFrame.Angles(math.pi/3, math.pi/6, 0)
    local cf2 = CFrame.new(-4, 5, 7.2) * CFrame.Angles(0, math.pi/7, -math.pi/3)
    
    local cf = cf1*cf2
    
    print(cf2)
    print(cf1:inverse() * cf)
    
    
    
    -4, 5, 7.19999981, 0.450484395, 0.780261934, 0.433883756, -0.866025448, 0.49999997, 0, -0.216941863, -0.375754386, 0.90096885
    -4, 5.00000143, 7.19999933, 0.450484395, 0.780261934, 0.433883697, -0.866025507, 0.5, -2.98023224e-08, -0.216941863, -0.375754386, 0.90096879
    

_请注意，输出结果中的细微变化是由于浮点数学运算的误差所导致_

假设我们已知 cf2 和 cf，但 cf1 未知。要求解该问题，我们也可以采用相似的步骤。
    
    
    cf = cf1 * cf2
    cf * cf2:inverse() = cf1 * cf2 * cf2:inverse() -- 自后以 cf2:inverse() 相乘等式两边
    cf * cf2:inverse() = cf1 * CFrame.new() -- 注意 cf * cf:inverse() = identityCFrame
    cf * cf2:inverse() = cf1 -- 注意 cf * identityCFrame = cf
    

再次进行验证测试。
    
    
    local cf1 = CFrame.new(1, 2, 3) * CFrame.Angles(math.pi/3, math.pi/6, 0)
    local cf2 = CFrame.new(-4, 5, 7.2) * CFrame.Angles(0, math.pi/7, -math.pi/3)
    
    local cf = cf1*cf2
    
    print(cf1)
    print(cf * cf2:inverse())
    
    
    
    1, 2, 3, 0.866025388, 0, 0.5, 0.433012724, 0.49999997, -0.75, -0.249999985, 0.866025448, 0.433012664
    1.00000048, 2.00000048, 3.00000095, 0.866025329, -2.98023224e-08, 0.49999997, 0.433012664, 0.5, -0.75, -0.25000003, 0.866025507, 0.433012664
    

_请注意，结果中的细微变化是由于浮点数学运算的误差所导致_

或许开发者心中会有这样的疑问：自前与自后相乘究竟为何如此重要？要得知原因所在，让我们来有意识地逐步研究 cf 自前乘以 cf2:inverse() 的整个运算过程，并观察最终的结果。
    
    
    cf = cf1 * cf2
    cf2:inverse() * cf = cf2:inverse() * cf1 * cf2
    -- 由于不知道 cf2:inverse() * cf1 = ??? 的答案，所以
    cf2:inverse() * cf = ???
    

最终的结论就是，顺序是十分重要的，而且我们对等式一侧的处理也必须应用于另一侧，不管是否自前或自后相乘都包括在内！

### 门的旋转

假设我们希望通过 CFrame 实现门的开合。这对于部分学习 CFrame 的人来说可能会十分困难，因为当我们对某一部件的 CFrame 使用 `CFrame.Angles` 函数并更新时，它会从中心开始转动。

![CFrameMath_doorRotate1.gif](https://developer.roblox.com/assets/blt68965f7f24226d28/CFrameMath_doorRotate1.gif)
    
    
    local door = game.Workspace.Door
    
    game:GetService("RunService").Heartbeat:connect(function(dt)
    	door.CFrame = door.CFrame * CFrame.Angles(0, math.rad(1)*dt*60, 0)
    end)
    

理想情况下，我们自然希望门能围绕某种铰链转动。也就是说，我们需要寻找一种方法来将我们的铰链作为旋转的中心。我们知道自己能够以类似早先旋转门的方式来旋转铰链。

![CFrameMath_doorRotate2.gif](https://developer.roblox.com/assets/blt68e0693617dbe134/CFrameMath_doorRotate2.gif)
    
    
    local door = game.Workspace.Door
    local hinge = game.Workspace.Hinge
    
    game:GetService("RunService").Heartbeat:connect(function(dt)
    	hinge.CFrame = hinge.CFrame * CFrame.Angles(0, math.rad(1)*dt*60, 0)
    end)
    

如果我们能设法计算出门相对于未旋转铰链的偏移值，就可以将该偏移值应用到旋转的铰链，并得出旋转门的 CFrame。换言之，我们必须在以下运算中求得偏移值：
    
    
    hinge.CFrame * offset = door.CFrame
    

求得偏移值的关键之处，就是使用逆运算！切记，我们对等式一侧的处理也必须应用于另一侧。
    
    
    hinge.CFrame * offset = door.CFrame -- want to get rid of hinge.CFrame on left side
    hinge.CFrame:inverse() * hinge.CFrame * offset = hinge.CFrame:inverse() * door.CFrame -- 因为乘数无法互换，进行自前相乘
    CFrame.new() * offset = hinge.CFrame:inverse() * door.CFrame -- cf:inverse() * cf = CFrame.new()
    offset = hinge.CFrame:inverse() * door.CFrame -- CFrame.new() * cf = cf
    

求出偏移值后，让我们将其应用到旋转铰链上吧！

![CFrameMath_doorRotate3-compressor.gif](https://developer.roblox.com/assets/blt6bf5320f1c4ca507/CFrameMath_doorRotate3-compressor.gif)
    
    
    local door = game.Workspace.Door
    local hinge = game.Workspace.Hinge
    
    local offset = hinge.CFrame:inverse() * door.CFrame; -- 旋转前首先进行偏移
    game:GetService("RunService").Heartbeat:connect(function(dt)
    	hinge.CFrame = hinge.CFrame * CFrame.Angles(0, math.rad(1)*dt*60, 0) -- 旋转铰链
    	door.CFrame = hinge.CFrame * offset -- 将偏移应用至旋转铰链
    end)
    

### 亲自尝试：接合

接合会受到以下条件约束。
    
    
    weld.Part0.CFrame * weld.C0 = weld.Part1.CFrame * weld.C1
    

请运用我们之前掌握的逆运算知识，尝试求出 Weld.C0 和 Weld.C1。完成自我测试前尽量不要参考答案。
    
    
    --解决方法：Weld.C0:
    weld.Part0.CFrame * weld.C0 = weld.Part1.CFrame * weld.C1 
    weld.Part0.CFrame:inverse() * weld.Part0.CFrame * weld.C0 = weld.Part0.CFrame:inverse() * weld.Part1.CFrame * weld.C1 
    CFrame.new() * weld.C0 = weld.Part0.CFrame:inverse() * weld.Part1.CFrame * weld.C1 
    weld.C0 = weld.Part0.CFrame:inverse() * weld.Part1.CFrame * weld.C1 
    
    --解决方法：C1:
    weld.Part0.CFrame * weld.C0 = weld.Part1.CFrame * weld.C1 
    weld.Part1.CFrame:inverse() * weld.Part0.CFrame * weld.C0 = weld.Part1.CFrame:inverse() * weld.Part1.CFrame * weld.C1 
    weld.Part1.CFrame:inverse() * weld.Part0.CFrame * weld.C0 = CFrame.new() * weld.C1 
    weld.Part1.CFrame:inverse() * weld.Part0.CFrame * weld.C0 = weld.C1
    

## CFrame 方法

在最后一节中，我们将探讨每种变换方法及对这些方法的部分直观理解。

### CFrame:ToObjectSpace()

等同于 `CFrame:inverse() * cf`

其实之前尝试实现门的旋转时，我们就已经从求取偏移值的过程中了解到了该方法的作用。此方法能计算出 CFrame 需要从 `CFrame` 中取得的偏移值，用以求出 `cf`

开发者可以通过以下函数轻松对其进行验证：
    
    
    CFrame * CFrame:toObjectSpace(cf)
    CFrame * CFrame:inverse() * cf
    identityCFrame * cf
    cf
    

### CFrame:ToWorldSpace()

等同于 `CFrame * cf`

此方法只是进行 CFrame 乘法，可能会让人觉得有些平凡无奇。不过，该方法的名称可能有助于我们更为直观地理解乘法运算的实际概念。我们在 `CFrame:toObjectSpace(cf)` 方法中看到，它返回的是两个 CFrame 之间的偏移值。我们还注意到，当我们用 `CFrame` 乘以偏移值后，最终结果是 `cf`。那么，我们将两个 CFrame 相乘时，实际上就是将第二个 CFrame 当做了偏移值。
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    local offset = CFrame.new(0, 0, -10) -- 向前 10 格偏移
    
    print(cf:toWorldSpace(offset)) -- 向前 10 格偏移。记住 cf 的前方为 cf.lookVector
    
    
    
    -8.51056576, 2.74757957, 0.00162148476, 0.262061268, 0.163754046, 0.95105654, -0.319058299, 0.944782019, -0.0747579709, -0.910783052, -0.283851326, 0.299837857
    

### CFrame:PointToObjectSpace()

等同于 `CFrame:inverse() * v3`

![CFrameMath_pointToObjectSpace.gif](https://developer.roblox.com/assets/bltf5bc4f61e31171d3/CFrameMath_pointToObjectSpace.gif)

此方法会在 3D 空间当中取特定点并使之与 `CFrame.p` 相对应，然后将其换算为偏移值。

此方法的替代方法为 `(CFrame - CFrame.p):inverse() * (v3 - CFrame.p)`
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    local v3 = Vector3.new(10, 10, 15)
    
    print(cf:pointToObjectSpace(v3))
    print((cf - cf.p):inverse() * (v3 - cf.p))
    
    
    
    -11.123312, 5.62582684, 11.5594997
    -11.123312, 5.62582684, 11.5594997
    

### CFrame:PointToWorldSpace()

等同于 `CFrame * v3`

由于我们早已探讨过了 `CFrame * v3` 的直观效果，因此除去已知内容外并无太多内容需要赘述。但需要再次进行提醒的是：此方法相当于在没有旋转方位的情况下应用偏移值。
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    local v3 = Vector3.new(10, 10, 15)
    
    print(cf * cf:pointToObjectSpace(v3))
    
    
    
    10.000001, 10, 15.0000019
    

_请注意，结果中的细微变化是由于浮点数学运算的误差所导致_

### CFrame:VectorToObjectSpace()

等同于 `(CFrame-CFrame.p):inverse() * v3`

此方法十分类似于 `CFrame:pointObjectSpace(v3)` 方法的替代形式。最主要的区别就是 `v3` 不再减去 `CFrame.p`。换而言之，两者步骤非常相似，唯一的区别就是不会使 `v3` 与 `CFrame.p` 相对应，而是默认之前所输入的 v3 已为相对数值。
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    
    print(cf:vectorToObjectSpace(cf.rightVector))
    
    
    
    1.00000012, 2.98023224e-08, 0
    

_请注意，结果中的细微变化是由于浮点数学运算的误差所导致_

我们可以看到，其结果等于或约等于 Vector3.new(1, 0, 0)，即 identityCFrame 的 rightVector。理想情况下，这两者完全相等，但正如上文所提到的，产生细微区别的原因是由于浮点数学运算的误差。

### CFrame:VectorToWorldSpace()

等同于 `(CFrame-CFrame.p) * v3`

此方法的替代形式是 `CFrame * v3 - CFrame.p`。也就是说，此方法其实与 `CFrame:pointWorldSpace(v3)` 相差无几，但并不会添加 CFrame.p（如我们在 CFrame * v3 一节中所学到的）。
    
    
    local cf = CFrame.new(1, 2, 3) * CFrame.Angles(math.rad(14), math.rad(72), math.rad(-32))
    
    print(cf:vectorToWorldSpace(Vector3.new(1, 0, 0)))
    print(cf * Vector3.new(1, 0, 0) - cf.p)
    print(cf.rightVector)
    
    
    
    0.262061268, -0.319058299, -0.910783052
    0.262061238, -0.319058299, -0.910783052
    0.262061268, -0.319058299, -0.910783052
    



***__Roblox官方链接__:[CFrame 数学运算](https://developer.roblox.com/zh-cn/articles/CFrame-Math-Operations)