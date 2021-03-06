# 2D 碰撞检测 
Time:<em>30  分钟</em>

##### 简介

当在二维空间中制作游戏时，你可能会发现自己受到内置 API 所能创建内容的限制。本文旨在介绍几种不同的 2D 碰撞检测方法。

**先决条件**

由于本文介绍不止一种方法，所以先决条件也不同，具体取决于你处理碰撞检测问题的方式。对于第一种方法，你需要对 GUI 元素的位置及其属性有基本的了解。第二种方法需要了解点积以及如何在 2D 中旋转矢量/点（本文将讨论旋转）。

##### 方法 1：轴对齐的形状

“轴对齐的形状”是指没有旋转的形状。换句话说，它的边平行于标准的 x 轴和 y 轴。这意味着这种形式的碰撞检测只适用于那些将其旋转属性设置为 0 的 GUI 元素。

**创建算法**

这种碰撞方法的目的是查看每个形状的范围是否互相重叠。

![Collision1.png](https://developer.roblox.com/assets/blt7f74583b820e7ed4/Collision1.png)



我们可以用什么规则集来检查形状 1 和形状 2 是否重叠？

*第一个形状左上角的 x 值是否小于第二个形状右上角的 x 值。  
*第一个形状右上角的 x 值是否大于第二个形状左上角的 x 值。  
*第一个形状左上角的 y 值是否小于第二个形状左下角的 y 值。  
*第一个形状左下角的 y 值是否大于第二个形状左上角的 y 值。

_注意：这些 2D GUI 使用的 XY 网格与其它 Roblox 使用的坐标不同。(0, 0) 位置在 GUI 元素的左上角。在这个网格中，右在 X 方向为正，下在 Y 方向为正。_

建议你使用上面的图片和规则（可能还有你的手指！）来找出为什么这样做有效。

**编写代码**

好吧，有了支撑这个简单碰撞方法的理论，我们如何把它转换成代码呢？一旦我们有了角，做测试就很简单了，那么我们如何才能得到角呢？

在本教程中，我们将使用 AbsolutePosition 和 AbsoluteSize 属性，因为它们会获取 GUI 的大小和位置，并将其完全转换为像素。我们不能使用比例和偏移的组合，因为它们是两个不同的单位，不能进行比较。

考虑到这一点，我们知道，对于任何给定的轴对齐 GUI，我们可以通过函数得到角，如：
    
    
    function getCorners(gui)
    	local topLeft = gui.AbsolutePosition;
    	local size = gui.AbsoluteSize;
    
    	local corners = {
    		topLeft = topLeft;
    		topRight = topLeft + Vector2.new(size.x, 0);
    		bottomRight = topLeft + Vector2.new(size.x, size.y);
    		bottomLeft = topLeft + Vector2.new(0, size.y);
    	};
    
    	return corners;
    end;
    

因此，在理解了如何获取角后，我们现在将应用两个测试，非常好！我们有一个简单的函数，可测试轴对齐形状的碰撞：
    
    
    function collides(gui1, gui2)
    	local g1p, g1s = gui1.AbsolutePosition, gui1.AbsoluteSize;
    	local g2p, g2s = gui2.AbsolutePosition, gui2.AbsoluteSize;
    	return ((g1p.x < g2p.x + g2s.x and g1p.x + g1s.x > g2p.x) and (g1p.y < g2p.y + g2s.y and g1p.y + g1s.y > g2p.y));
    end;
    
    -- 使用的示例：
    
    local f1 = script.Parent:WaitForChild("Frame1");
    local f2 = script.Parent:WaitForChild("Frame2");
    
    game:GetService("RunService").RenderStepped:connect(function()
    	local doesCollide = collides(f1, f2);
    	f1.BorderColor3 = doesCollide and Color3.new(1, 0, 0) or Color3.new(0, 1, 0);
    	f2.BorderColor3 = doesCollide and Color3.new(1, 0, 0) or Color3.new(0, 1, 0);
    end);
    

![Collision3.gif](https://developer.roblox.com/assets/blt50951f3ef60829be/Collision3.gif)

_注意：这种碰撞方法不考虑负尺寸的 GUI_

**下一步：最小平移矢量**

如果我们想让脚本自动重新定位形状，那么我们将寻找必须移动形状以使它们不再碰撞的最小量。这个量被称为最小平移矢量（MTV），它非常有用！

对于轴向对齐的形状，计算这个最小量在逻辑上非常简单。我们只需要看看 shape1 的每条边，得到这条边与 shape2 的对边之间的距离，然后在所有这些比较中找出最小的距离并移动形状。
    
    
    function collidesMTV(gui1, gui2)
    	local g1p, g1s = gui1.AbsolutePosition, gui1.AbsoluteSize;
    	local g2p, g2s = gui2.AbsolutePosition, gui2.AbsoluteSize;
    	-- 首先检查碰撞
    	local doesCollide, mtv = ((g1p.x < g2p.x + g2s.x and g1p.x + g1s.x > g2p.x) and (g1p.y < g2p.y + g2s.y and g1p.y + g1s.y > g2p.y));
    	-- 由于我们知道其将会碰撞，找出 mtv
    	if doesCollide then
    		-- 找出 shape1 边缘和 shape2 相对边缘之间的距离
    		local edgeDifferences = {
    			Vector2.new(g1p.x - (g2p.x + g2s.x), 0); -- 左
    			Vector2.new((g1p.x + g1s.x) - g2p.x, 0); -- 右
    			Vector2.new(0, g1p.y - (g2p.y + g2s.y)); -- 上
    			Vector2.new(0, (g1p.y + g1s.y) - g2p.y); -- 下
    		};
    		-- 获取最小差值
    		table.sort(edgeDifferences, function(a, b) return a.magnitude < b.magnitude; end);
    		mtv = edgeDifferences[1];
    	end;
    	-- 提供碰撞布尔值与 mtv
    	return doesCollide, mtv or Vector2.new();
    end;
     
    -- 示例
     
    local f1 = script.Parent:WaitForChild("Frame1");
    local f2 = script.Parent:WaitForChild("Frame2");
     
    game:GetService("RunService").RenderStepped:connect(function()
    	local doesCollide, mtv = collidesMTV(f2, f1);
    	if doesCollide then
    		f1.Position = f1.Position + UDim2.new(0, mtv.x, 0, mtv.y);
    	end;
    end);
    

![Collision4.gif](https://developer.roblox.com/assets/blt9f1cf7b940ee9620/Collision4.gif)

##### 方法 2 的先决条件：旋转形状的角

是的，这种方法有一点复杂。在前一种方法中，我们只能在形状没有旋转的情况下检测碰撞。在下一种方法中，我们将能够检测旋转的形状之间的碰撞，前提是我们可以获得它们的旋转角！

**理解数学**

在获取形状的角时，我们需要考虑一些问题/事情：

  * 无论形状如何旋转，GUI 对象的大小和位置都保持不变。这意味着形状仍然从左上角定位，就像没有应用旋转一样。类似地，形状的位置属性将提供一个非旋转值。
  * 当形状旋转时，它会通过形状的中心旋转。这意味着我们有一个旋转的原点。  
幸运的是，我们有一种绕原点旋转矢量的方法。要搞明白这一点有点难，但通过基本的三角学知识以及笔和纸，你会很快弄明白的！让我们来看一个例子：

![Colllision5.png](https://developer.roblox.com/assets/blt42c624f7eb411a93/Colllision5.png)



假设我想把点 P 旋转 R 度。执行这个旋转的关键是假设点保持不动，轴旋转，然后找到点的 x 和 y 值在新的旋转轴上的位置：

![Collision6.png](https://developer.roblox.com/assets/blt50a0f1648b777cd0/Collision6.png)



让我们通过视觉辅助来回顾一下这些步骤：

请记住 SOHCAHTOA，我们可以用它来解决直角三角形缺失角度和长度的问题，只要我们至少拥有两条信息。

我们知道，旋转轴上的新 x 值 (Xb) 就是 A 到 B (AB) 与 B 到 Xb (BXb) 长度的和。我们还知道，B 到 Xb 的长度等于 Xa 到 D (XaD) 的长度。

同样地，我们知道，旋转轴上的新 y 值 (Yb) 就是 A 到 F (AF) 减去 Yb 到 F (YbF) 后的长度。我们还知道，Yb 到 F 的长度等于 G 到 Ya (GYa) 的长度。

记住这一点，我们可以使用某些基本的三角函数来解出 Xb 和 Yb：  
![Collision23.png](https://developer.roblox.com/assets/bltdc02506f9b6b0fd2/Collision23.png)

  
好了，现在我们必须找到一种方法来将这个新发现的知识应用到 GUI 中。第一个问题是，我们刚刚推导出的等式仅限于绕原点 (0,0) 旋转。这不是一个很大的问题，但我们需要考虑信息的当前形式。

如果我们像方法一那样得到了角，然后直接将旋转应用到角上，那么我们将围绕整个 2D 平面旋转形状（就像时钟上的指针一样）。更确切地说，我们要做的是用一些简单的减法得到相对于 (0, 0) 原点的角，使其作为形状的中心：

![Collision7.png](https://developer.roblox.com/assets/bltf9ad9c45f21d91ed/Collision7.png)

 ![Collision8.png](https://developer.roblox.com/assets/blt5c4634e7889e4f20/Collision8.png)



在旋转了这些经过调整的角后，我们将做一些加法以再次获得相对于形状实际中心的点。

最后要记住的一件重要的事是，vector2 中的正 x 和 y 值引用右上象限中的一个点。另一方面，UDim2 位置的正 x 和 y 值引用右下象限中的点。因为我们旋转的是 vector2 的值，我们可能认为我们需要顺时针旋转。不过，因为我们将这些点转换成了 UDim2，所以我们实际上需要逆时针旋转以获得正确的 UDim2 值。

**编写代码**

现在我们知道了要得到旋转的形状需要做什么，让我们把它放到一个通用的函数中：
    
    
    function getCorners(frame)
    	local corners, rot = {}, math.rad(frame.Rotation); -- 使用弧度（Radian）
    	local center = frame.AbsolutePosition + frame.AbsoluteSize/2; -- 中心的位置
    	-- 无旋转情况下角的位置  
    	local world_cords = {
    		Vector2.new(frame.AbsolutePosition.x, frame.AbsolutePosition.y); -- 左上
    		Vector2.new(frame.AbsolutePosition.x + frame.AbsoluteSize.x, frame.AbsolutePosition.y); -- 右上
    		Vector2.new(frame.AbsolutePosition.x + frame.AbsoluteSize.x, frame.AbsolutePosition.y + frame.AbsoluteSize.y); -- 右下
    		Vector2.new(frame.AbsolutePosition.x, frame.AbsolutePosition.y + frame.AbsoluteSize.y); -- 左下
    	};
    	-- 代入旋转进行计算
    	for i, corner in ipairs(world_cords) do
    		-- 使用之前的旋转方法，获得相对角度，然后添加至原始中心
    		local x = center.x + (corner.x - center.x) * math.cos(rot) - (corner.y - center.y) * math.sin(rot);
    		local y = center.y + (corner.x - center.x) * math.sin(rot) + (corner.y - center.y) * math.cos(rot);
    		corners[i] = Vector2.new(x, y);
    	end;
    	return corners;
    end;
    

我们可以做一个简单的测试。查看透明旋转形状上的角是否精确：

![Collision9.gif](https://developer.roblox.com/assets/blt814b785c2c039d72/Collision9.gif)

太棒了，我们可以得到我们形状的旋转角！

##### 方法 2：分离轴定理 (SAT)

既然我们有方法来获得形状的角，我们可以采用一些更先进的方法来进行 2D 碰撞。

分离轴定理是一种检测两个凸多边形是否相交的方法。凸多边形就是你绘制的任意直线都可以穿过的任何形状，而且该直线只会穿过形状两次。为了方便起见，我们只使用凸形的矩形。

**理解数学**

SAT 背后的理念是，如果你能在两个图形之间画一条线，那么就不会发生碰撞。

![Collision10.png](https://developer.roblox.com/assets/blt7d6599a196a3b395/Collision10.png)



前提很简单，任何人都可以很容易地用手实现它，但是我们如何把它转化成可以用数学方法测试的东西呢？答案是将我们的角投射到两个形状的所有唯一曲面法线上。

![Collision11.png](https://developer.roblox.com/assets/blt5d23e47422538ce3/Collision11.png)



如果我们知道蓝线和红线在粉紫色线上的位置，那么我们只需看看这些点是否重叠。如果不重叠，我们就知道没有交集。如果重叠，那么我们必须检查其他轴。

换言之，如果我把形状放在一个黑暗的房间里，绕着它们走，我是否会在房间墙壁的另一侧看到它们的阴影中有一个间隙？如果是，那么形状不会碰撞。否则它们是：

_有间隙（无碰撞）：_

![Collision12.gif](https://developer.roblox.com/assets/bltdb431402c5a07346/Collision12.gif)

_无间隙（有碰撞）：_

![Collision13.gif](https://developer.roblox.com/assets/blt9fa918aff1849033/Collision13.gif)

显然，在上面的例子中，我们看到的是从两个形状周围的各个角度投射的阴影。这不仅效率低下，而且没有必要。如上所述，我们只需要在形状的唯一曲面法线上投射阴影。

**编写代码**

首先，什么是法线？法线是垂直于曲面的单位矢量（如紫色所示）：

![Collision14.png](https://developer.roblox.com/assets/blt76c53e8ec0347d54/Collision14.png)



如何得到一个垂直的矢量？很简单，只要交换 x 和 y 的值，并将其中一个值乘以 -1。例如，我们有 Vector2.new(0, 1)，我们想要一个垂直的 vector2。只需交换 x 和 y，即可得出 Vector2.new(1, 0)，然后用 x 或 y 乘以 -1 得到 Vector2.new(-1, 0) 或 Vector2.new(1, 0)。所以采用以下函数形式：
    
    
    function getPerpendicular(vec)
        return Vector2.new(vec.y, -vec.x).unit;
    end;
    

好吧，既然我们了解了这一点，我们如何得到形状的唯一曲面法线呢？这很容易，因为我们拥有形状的角。只需减去两个相连的角，即得到垂直的单位矢量。还要记住，我们只需要唯一的轴，也就是说，我们不需要相反的同一曲面法线。这与矩形特别相关，因为每一条边都有一个具有完全相反的曲面法线的对边，我们不需要这个。因此，代码如下：
    
    
    function getAxis(shape1Corners, shape2Corners)
        local axis = {};
        axis[1] = getPerpendicular(shape1Corners[1] - shape1Corners[2]);
        axis[2] = getPerpendicular(shape1Corners[1] - shape1Corners[4]);
        axis[3] = getPerpendicular(shape2Corners[1] - shape2Corners[2]);
        axis[4] = getPerpendicular(shape2Corners[1] - shape2Corners[4]);
        return axis;
    end;
    

因为我们使用的是矩形，所以我们可以将它进一步简化。由于边矢量（采用形状顶部和底部的单位形式）与左右边的曲面法线相同，并且反之亦然，所以我们可以完全去掉 getvertical 函数：

![Collision15.png](https://developer.roblox.com/assets/blt329d7100fd2f26ac/Collision15.png)



请注意，蓝色箭头与紫色箭头的方向相同，因此我们只需减去，然后进行标准化：
    
    
    function getAxis(shape1Corners, shape2Corners)
        local axis = {};
        -- vector 的 x 和 y 值为正或负都可（只要不通过相对 vector 进行重复即可）
        axis[1] = (shape1Corners[2] - shape1Corners[1]).unit;
        axis[2] = (shape1Corners[2] - shape1Corners[3]).unit;
        axis[3] = (shape2Corners[2] - shape2Corners[1]).unit;
        axis[4] = (shape2Corners[2] - shape2Corners[3]).unit;
        return axis;
    end;
    

关于轴，我们还需要介绍一件事！之后，如果我们想计算最小平移矢量，我们需要做一些关于轴的矢量运算。因此，重要的是我们不会随意选择轴。在本文中，我们将选择的轴总是从角 1 延伸到连接的角：
    
    
    function getAxis(c1, c2)
    	local axis = {};
    	axis[1] = (c1[2] - c1[1]).unit;
    	axis[2] = (c1[4] - c1[1]).unit;
    	axis[3] = (c2[2] - c2[1]).unit;
    	axis[4] = (c2[4] - c2[1]).unit;
    	return axis;
    end;
    

太棒了！现在轴已经解决了，是时候关注投影了。

为了让这些角投影到轴上，我们只需进行循环，然后用点积投影。我们要注意的一件事是，将这个值保持为标量形式。如果我们要把它转换成矢量，那么长度的唯一度量就是量级，但是量级总是正的，这意味着我们在检查这些值是否重叠时丢失了有价值的信息。

在获得了所有的标量后，接下来我们就需要看看是否有重叠。回忆一下这张照片：

![Collision11.png](https://developer.roblox.com/assets/blt5d23e47422538ce3/Collision11.png)



所以我们需要得到每个形状最大和最小标量（因为它们一起代表形状“阴影”的端点），然后看看它们是否重叠。如果有任何间隙，我们立即会知道形状不会碰撞。但是，如果没有间隙，并且我们检查了所有轴上的重叠标量，那么我们知道这两个形状是碰撞的！
    
    
    function dot2d(a, b)
        -- vector2 的端点
        return a.x * b.x + a.y * b.y;
    end;
    
    function collide(shape1, shape2)
        local c1, c2 = getCorners(shape1), getCorners(shape2); -- 角
        local axis = getAxis(c1, c2); -- 轴
        local scalars = {};
        for i = 1, #axis do -- 遍历所有轴
            for i2, set in pairs({c1, c2}) do
                scalars[i2] = {}; -- 如果之前有轴标量则将其清空
                for _, point in pairs(set) do
                    -- 将角投射至轴并储存至表，用来区分两个形状
                    table.insert(scalars[i2], dot2d(point, axis[i]));
                end;
            end;
            -- 获取每个形状的最大及最小投射标量
            local s1max, s1min = math.max(unpack(scalars[1])), math.min(unpack(scalars[1]));
            local s2max, s2min = math.max(unpack(scalars[2])), math.min(unpack(scalars[2]));
            -- 如果没有重合，则不会发生碰撞！
            if s2min > s1max or s2max < s1min then
                return false;
            end;
        end;
        -- 结束检查所有轴，每个轴都有重合，所以一定会发生碰撞
        return true;
    end;
    
    -- 示例
    
    local f1 = script.Parent:WaitForChild("Frame1");
    local f2 = script.Parent:WaitForChild("Frame2");
    
    game:GetService("RunService").RenderStepped:connect(function()
    	f1.Rotation = f1.Rotation + 1;
    	f2.Rotation = f2.Rotation - 1;
    	local doesCollide = collide(f1, f2);
    	f1.BorderColor3 = doesCollide and Color3.new(1, 0, 0) or Color3.new(0, 1, 0);
    	f2.BorderColor3 = doesCollide and Color3.new(1, 0, 0) or Color3.new(0, 1, 0);
    end);
    

好极了！我们现在有了一种检查旋转形状是否碰撞的方法：

![Collision16.gif](https://developer.roblox.com/assets/bltf3a755a1f80a368b/Collision16.gif)

**下一步：最小平移矢量**

如果发生碰撞，我们还是希望形状会自动调整其位置。我们也可以用 SAT 碰撞计算 MTV。这个过程实际上比轴对齐的形状更容易，因为我们已经拥有了大部分信息。

我们所需要做的就是找到最小的重叠距离，然后把它应用到我们的轴（确保考虑正确的方向）。就这么简单：
    
    
    function collide(shape1, shape2)
    	local c1, c2 = getCorners(shape1), getCorners(shape2);
    	local axis = getAxis(c1, c2);
    	local scalars, mtv = {}, Vector2.new(math.huge, math.huge); -- 巨大幅度
    	local a = nil;
    	for i = 1, #axis do
    		for i2, set in pairs({c1, c2}) do
    			scalars[i2] = {};
    			for _, point in pairs(set) do
    				table.insert(scalars[i2], dot2d(point, axis[i]));
    			end;
    		end;
    		local s1max, s1min = math.max(unpack(scalars[1])), math.min(unpack(scalars[1]));
    		local s2max, s2min = math.max(unpack(scalars[2])), math.min(unpack(scalars[2]));
    		if s2min > s1max or s2max < s1min then
    			return false, Vector2.new(); -- 因为没有碰撞，所以 mtv 为极小
    		end;
    		-- 获取到 shape 1 会在 shape 2 上重合，因此将 mtv 应用至 shape 2
    		local overlap = s1max > s2max and -(s2max - s1min) or (s1max - s2min);
    		if math.abs(overlap) < mtv.magnitude then
    			-- 为了获取合适的方向，重合可能为负
    			mtv = axis[i] * overlap;
    		end;
    	end;
    	return true, mtv;
    end;
    
    -- 示例
    
    local f1 = script.Parent:WaitForChild("Frame1");
    local f2 = script.Parent:WaitForChild("Frame2");
    
    game:GetService("RunService").RenderStepped:connect(function()
    	f1.Rotation = f1.Rotation + 1;
    	f2.Rotation = f2.Rotation - 1;
    	local doesCollide, mtv = collide(f2, f1);
    	if doesCollide then
    		f1.Position = f1.Position + UDim2.new(0, mtv.x, 0, mtv.y);
    	end;
    end);
    

![Collision17.gif](https://developer.roblox.com/assets/bltd65974c4cc50de0b/Collision17.gif)

##### 补充：线段相交

好吧，最后这个算法或多或少是补充性的，因为它并不是完全适用于碰撞检测的理想算法，但如果你在进行 2D 研发，你会发现它可与本文讨论的其它方法一起使用，以获得更多关于形状周围环境的信息。

**理解数学**

![Collision18.png](https://developer.roblox.com/assets/blt55be1881c2d91540/Collision18.png)



假设我们有两行，每一行本质定义为两点之间的连接（a 到 b，c 到 d）。这种形式没问题，但由于我们正在创建矢量，我们希望以一种更加相关的形式得到所需信息。实际上，通过矢量减法很容易做到这一点：

![Collision19.png](https://developer.roblox.com/assets/bltfbcdb28c0162dca8/Collision19.png)



如果这两条线段真的相交，那么我们知道有一些标量 t 和 u，当它们分别与 r 和 s 相乘时是相等：这就是我们的交点。

![Collision20.png](https://developer.roblox.com/assets/blte7b94571020162aa/Collision20.png)



好了，我们已经建立了等式，但是我们好像遇到些难处。通常我们的目标是用代数方法求解未知数，但我们有两个未知数！那么，我们该怎么做呢？这让事情变得很棘手。我们实际上要做的是将整个产品中的 2D 定义为：
    
    
    function cross2d(a, b)
    	return a.x * b.y - a.y * b.x;
    end;
    
    -- 你可能会注意到，这实际上只是我们将这两个矢量作为 3D 矢量交叉得到的 z 值。
    function alternateCross2d(a, b)
    	-- 注意：我们所计算的交叉 x 及 y 值可能为 0
    	return Vector3.new(a.x, a.y, 0):Cross(Vector3.new(b.x, b.y, 0)).z;
    end;
    

我们要注意的一个有趣的特性是，当我们 2D 交叉任何矢量时，结果是 0。
    
    
    local v = Vector2.new(129290.31478, -342.232);
    print(cross2d(v, v)); -- result: 0
    

考虑到这一点，我们所要做的就是将这个新定义应用于我们在上面计算出的等式，并求解其中一个变量：

![Collision21_2.png](https://developer.roblox.com/assets/blt74d15baf1e684da6/Collision21_2.png)



因此，请记住这一点，我们知道，如果我们进行此计算且 t 和 u 都在 0 和 1 之间（因为我们要用加法矢量乘以它），则我们知道这两条线相交！就是这样！

**编写代码**
    
    
    function lineIntersect(a, b, c, d)
    	-- 以增量 vector 形式获取
    	local r = (b - a);
    	local s = (d - c);
    	
    	-- 仅在此使用，所以只计算一次
    	local d = r.x * s.y - r.y * s.x; 
    	local u = ((c.x - a.x) * r.y - (c.y - a.y) * r.x) / d;
    	local t = ((c.x - a.x) * s.y - (c.y - a.y) * s.x) / d;
    	
    	-- 如果有交叉，则返回位置
    	return (0 <= u and u <= 1 and 0 <= t and t <= 1) and a + t * r;
    end;
    
    print(lineIntersect(
    	Vector2.new(0, 0), -- a
    	Vector2.new(3, 3), -- b
    	Vector2.new(3, 0), -- c
    	Vector2.new(0, 3)  -- d
    )); 
    -- 结果：Vector2.new(1.5, 1.5)
    
    print(lineIntersect(
    	Vector2.new(0, 0), -- a
    	Vector2.new(3, 3), -- b
    	Vector2.new(3, 0), -- c
    	Vector2.new(6, 3)  -- d
    ));
    -- 结果：false
    

太棒了，现在只需要把它应用到我们的代码中。幸运的是，我们已经计算出了角，所以只需比较构成两个形状的线段。
    
    
    function lineIntersect(a, b, c, d)
    	-- 以增量 vector 形式获取
    	local r = (b - a);
    	local s = (d - c);
    	
    	-- 仅在此使用，所以只计算一次
    	local d = r.x * s.y - r.y * s.x; 
    	local u = ((c.x - a.x) * r.y - (c.y - a.y) * r.x) / d;
    	local t = ((c.x - a.x) * s.y - (c.y - a.y) * s.x) / d;
    	
    	-- 如果有交叉，则返回位置
    	return (0 <= u and u <= 1 and 0 <= t and t <= 1) and a + t * r;
    end;
    
    function getSegments(corners)
    	local segments = {};
    	for k, corner in pairs(corners) do
    		local ncorner = corners[k + 1 <= #corners and k + 1 or 1];
    		table.insert(segments, {corner, ncorner});
    	end;
    	return segments;
    end;
    
    function collide(shape1, shape2)
    	local s1, s2 = getSegments(getCorners(shape1)), getSegments(getCorners(shape2));
    	for _, segment in pairs(s1) do
    		for _, segment2 in pairs(s2) do
    			local v = lineIntersect(segment[2], segment[1], segment2[2], segment2[1]);
    			if v then
    				return v;
    			end;
    		end;
    	end;
    	return false;
    end;
    
    -- 示例
    
    local f1 = script.Parent:WaitForChild("Frame1");
    local f2 = script.Parent:WaitForChild("Frame2");
    
    game:GetService("RunService").RenderStepped:connect(function()
    	f1.Rotation = f1.Rotation + 1;
    	f2.Rotation = f2.Rotation - 1;
    	local doesCollide = collide(f1, f2);
    	f1.BorderColor3 = doesCollide and Color3.new(1, 0, 0) or Color3.new(0, 1, 0);
    	f2.BorderColor3 = doesCollide and Color3.new(1, 0, 0) or Color3.new(0, 1, 0);
    end);
    

![Collision22.gif](https://developer.roblox.com/assets/blt1edfacb16b55d158/Collision22.gif)

你可能会注意到，这种方法缺少一个形状比另一个形状大的情况（由于它们的边缘没有碰撞），因此作为碰撞方法，它并不是最优的。尽管这么说，调整这个方法来解决这个问题并不是不可能的，但是本文不会讨论这个问题。

##### 另请参阅

  * [Mozilla 碰撞检测文章](https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection)

  * [分离轴定理](http://www.dyn4j.org/2010/01/sat/)



***__Roblox官方链接__:[2D 碰撞检测](https://developer.roblox.com/zh-cn/articles/2D-Collision-Detection)