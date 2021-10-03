# Bézier Curves 
Time:<em></em>

Game development often requires using curves, such as drawing curvy shapes or travelling along a non-linear path. However, computers require a function in order to perform calculations. For lines, equations are quite simple (y = mx +b). Curves, on the other hand, tend to be a bit more complicated. A **Bézier curve** is an easier type of curve that is useful in a wide variety of places in game design. You’ll need to be somewhat comfortable with the following math topics in order to get started:

  * Algebra
  * Linear interpolation
  * Vectors

## Quadratic Bézier curves

A **quadratic Bézier curve** is a curve created using **three points**. The first and the third point define the start and the end of the curve. The intermediate point influences the curvature of the line, and is most of the time not on the curve.  
Here’s what one quadratic Bézier looks like:

![bezier1.png](https://developer.roblox.com/assets/blt6f28a20d3417e288/Bezier1.png)



This may seem confusing at first, but it’s simpler than it appears: the function is lerping along the line between between p0 and p1 while simultaneously lerping along the line between p1 and p2. We’re then taking the two points created by those two lerp functions and then lerping along that value to get our point on the curve. This looks something like this:

![bezier2.gif](https://developer.roblox.com/assets/blt6bac53c6c6f16b7b/Bezier2.gif)

We can write it in code form as such:
    
    
    function lerp(a, b, c)
    	return a + (b - a) * c
    end
    
    function quadBezier(t, p0, p1, p2)
    	local l1 = lerp(p0, p1, t)
    	local l2 = lerp(p1, p2, t)
    	local quad = lerp(l1, l2, t)
    	return quad
    end
    

This function is alright and there’s nothing wrong with it, but there’s a more formal equation that’s commonly used for quadratic Bézier curves.

![beziereq1.png](https://developer.roblox.com/assets/blte9e328e234646be2/Beziereq1.png)



To understand why this equation works we have to first think about how we would create a linear Bézier curve (not really a curve now is it?). If you’re up to date on the prerequisites of the article then you already know how to do this in the form of a linear interpolation between two points!

![beziereq2.png](https://developer.roblox.com/assets/blt3e7f7e13dc09fbd3/Beziereq2.png)



We already know how to do a quadratic Bezier using three linear interpolations like we did in the code above so let’s try writing that out with our linear B(t) function:

![beziereq3.png](https://developer.roblox.com/assets/blt592536ac50554d85/Beziereq3.png)



Sure enough we’re left with the formal quadratic Bézier curve equation!
    
    
    function quadBezier(t, p0, p1, p2)
    	return (1 - t)^2 * p0 + 2 * (1 - t) * t * p1 + t^2 * p2
    end
    

![](https://developer.roblox.com/assets/blt8a1bc7e1b6272ca7/Bezier3.gif)

## Cubic Bézier curves

A cubic Bézier curve is a curve that’s created with four points. The first and the fourth point define the start and the end of the curve. The intermediates point once again just like the quadratic curve influence the curvature of the line.

Here’s what a cubic Bézier might look like:

![bezier4.png](https://developer.roblox.com/assets/blt6dbdfe4e78afd162/Bezier4.png)



Once again, this might seem a little confusing to wrap your head around but it’s a very similar process to what we were doing with the quadratic Bézier curves. What we’re actually doing is lerping along the line between between p0 and p1 while simultaneously lerping along the line between p1 and p2 while also simultaneously lerping along the line between p2 and p3. We’re then taking the two points created by those the first and second lerp functions and then lerping along that value to get yet another point which we’ll call “a”. Then we’re taking two points created by the second and third lerp functions and lerping along the line created by those two points to get a point which we’ll call “b”. Finally, we lerp between “a” and “b” to get our point along the curve.

![bezier5.gif](https://developer.roblox.com/assets/blt0e3d6247bf78730f/Bezier5.gif)

We can write this in function form:
    
    
    function lerp(a, b, c)
    	return a + (b - a) * c
    end
    
    function cubicBezier(t, p0, p1, p2, p3)
    	local l1 = lerp(p0, p1, t)
    	local l2 = lerp(p1, p2, t)
    	local l3 = lerp(p2, p3, t)
    	local a = lerp(l1, l2, t)
    	local b = lerp(l2, l3, t)
    	local cubic = lerp(a, b, t)
    	return cubic
    end
    

Yet again, there’s a more formal equation for a cubic Bézier:

![beziereq4.png](https://developer.roblox.com/assets/blt8edacc997ebcbbc2/Beziereq4.png)



In a similar sense we can pull apart the code from above to find why this equation works:

![beziereq5.png](https://developer.roblox.com/assets/blt7d7cc1c551a785d0/Beziereq5.png)



Sure enough, we’re left with the cubic Bézier function!
    
    
    function cubicBezier(t, p0, p1, p2, p3)
    	return (1 - t)^3*p0 + 3*(1 - t)^2*t*p1 + 3*(1 - t)*t^2*p2 + t^3*p3
    end
    

![](https://developer.roblox.com/assets/blt39e5771948c7202b/Bezier6.gif)

It is possible to have Bézier curves of higher degrees by following a similar pattern but for the purpose of this article we’ll stop here at cubic.

## Arc-length parameterization

So now that we know a bit about how to calculate points along Bézier curves let’s talk about some current issues we might face with them. To start, let’s see what happens when we try to interpolate along our curve at a fixed speed.

![bezier7.gif](https://developer.roblox.com/assets/blt36c3b5fb39d66d62/Bezier7.gif)
    
    
    -- function for drawing a 2D line between two points
    function drawLine(p1, p2)
    	local v = (p2 - p1)
    	local f = Instance.new("Frame")
    	f.Size = UDim2.new(0, v.magnitude + 1, 0, 2)
    	f.Position = UDim2.new(0,(p1.x + v.x/2) - f.Size.X.Offset * 0.5, 0, (p1.y + v.y/2) - f.Size.Y.Offset * 0.5)
    	f.Rotation = math.deg(math.atan2(v.y, v.x))
    	f.BorderSizePixel = 0
    	f.BackgroundColor3 = Color3.new()
    	return f
    end
    
    function update(p0, p1, p2, p3, canvas)
    	local last
    	canvas:ClearAllChildren() -- clear any previous drawings
    	for t = 0, 1, 0.01 do -- 0 <= t <= 1
    		local p = cubicBezier(t, p0, p1, p2, p3)
    		if last then drawLine(last, p).Parent = canvas end
    		last = p
    	end
    end
    
    function travelCurve(p0, p1, p2, p3, moving)
    	for t = 0, 1, 0.01 do -- 0 <= t <= 1
    		local p = cubicBezier(t, p0, p1, p2, p3)
    		moving.Position = UDim2.new(0, p.x - mp.AbsoluteSize.x/2, 0, p.y - mp.AbsoluteSize.y/2)
    		game:GetService("RunService").RenderStepped:wait()
    	end
    end
    

Hmm, that doesn’t look like it’s traveling at a linear rate does it? Turns out the reason for this is because by nature of a Bézier curve doesn’t produce points that are evenly distributed. To see this let’s just draw points along the curve.

![bezier8.gif](https://developer.roblox.com/assets/bltcdd5fd2ce9185675/Bezier8.gif)
    
    
    -- function for drawing a 2D point
    function drawPoint(p1)
    	local f = Instance.new("Frame")
    	f.Size = UDim2.new(0, 2, 0, 2)
    	f.Position = UDim2.new(0, p1.x - f.Size.X.Offset * 0.5, 0, p1.y - f.Size.Y.Offset * 0.5)
    	f.BorderSizePixel = 0
    	f.BackgroundColor3 = Color3.new()
    	return f
    end
    
    function update(p0, p1, p2, p3, canvas)
    	local last
    	canvas:ClearAllChildren() -- clear any previous drawings
    	for t = 0, 1, 0.01 do -- 0 <= t <= 1
    		local p = cubicBezier(t, p0, p1, p2, p3)
    		drawPoint(p).Parent = world
    		last = p
    	end
    end
    

As shown in the gif above, the points near the middle are more tightly packed together and the points closer to the start and end of the curve are further apart. This creates an effect of slowing down in the middle and getting faster near the start and end. So what can we do to fix this problem? In other words, how can we make it so that t = 0.25 is guaranteed to be 25% along the curve’s distance?

Turns out the simplest way to do this is a best guess method which isn’t perfect, but it’s so close that unless you’re working for NASA you won’t even notice it. To be clear, there are other ways to do this that are more accurate, but they require calculus which is out of the scope of this article.

Here’s how the process works:
    
    
    -- n is the number of points
    -- func is the bezier curve function
    -- ... are the points used in the bezier curve function
    function length(n, func, ...)
    	local sum, ranges, sums = 0, {}, {}
    	for i = 0, n-1 do
    		-- calculate the current point and the next point
    		local p1, p2 = func(i/n, ...), func((i+1)/n, ...)
    		-- get the distance between them
    		local dist = (p2 - p1).magnitude
    		-- store the information we gathered in a table that's indexed by the current distance
    		ranges[sum] = {dist, p1, p2}
    		-- store the current sum so we can easily sort through it later
    		table.insert(sums, sum)
    		-- update the sum
    		sum = sum + dist
    	end
    	-- return values
    	return sum, ranges, sums
    end
    

With that in mind we can use that function in tandem with another to get a pretty good guess of the actual linear position t would represent along the Bezier curve:
    
    
    function fixedBezier(n, t, func, ...)
    	-- gather values from length function
    	local length, ranges, sums = length(n, func, ...)
    	-- find how far along the length we should be
    	local T, near = t * length, 0
    	-- get the nearest point we calculated
    	for _, n in next, sums do
    		if (T - n) < 0 then break end
    		near = n
    	end
    	local set = ranges[near]
    	-- linearly interpolate between that point and its neighbor
    	local percent = (T - near)/set[1]
    	return set[2] + (set[3] - set[2]) * percent
    end
    

Here’s the problem, when our current function is used consecutively this causes a lot of lag! We’re using the length function which has to do a ton of point calculations every time for just one single point! Here’s the good news though, if we use a bit of object oriented programming we can store the values the length function and make sure to update it only when the points that create the Bézier change!

Here’s a nice little Bézier module that should work with any degree of Bézier function:

![bezier9.gif](https://developer.roblox.com/assets/blt2ee53c6a18bb5ec1/Bezier9.gif)
    
    
    local bezier = {}
    
    function length(n, func, ...)
    	local sum, ranges, sums = 0, {}, {}
    	for i = 0, n-1 do
    		local p1, p2 = func(i/n, ...), func((i+1)/n, ...)
    		local dist = (p2 - p1).magnitude
    		ranges[sum] = {dist, p1, p2}
    		table.insert(sums, sum)
    		sum = sum + dist
    	end
    	return sum, ranges, sums
    end
    
    function bezier.new(func, n, ...)
    	local self = setmetatable({}, {__index = bezier})
    	local sum, ranges, sums = length(n, func, ...)
    	self.func = func
    	self.n = n
    	self.points = {...}
    	self.length = sum
    	self.ranges = ranges
    	self.sums = sums
    	return self
    end
    
    function bezier:setPoints(...)
    	-- only update the length when the control points are changed
    	local sum, ranges, sums = length(self.n, self.func, ...)
    	self.points = {...}
    	self.length = sum
    	self.ranges = ranges
    	self.sums = sums
    end
    
    function bezier:calc(t)
    	-- if you don't need t to be a percentage of distance
    	return self.func(t, unpack(self.points))
    end
    
    function bezier:calcFixed(t)
    	local T, near = t * self.length, 0
    	for _, n in next, self.sums do
    		if (T - n) < 0 then break end
    		near = n
    	end
    	local set = self.ranges[near]
    	local percent = (T - near)/set[1]
    	return set[2], set[3], percent
    end
    
    return bezier
    

## Bézier paths

The last thing this article will cover is the idea of connecting multiple Bézier curves together. For visual purposes the concept is easy. Just make sure that the start point of your next Bézier curve is the same as the last point on the previous Bézier curve. What becomes more difficult is making these curves into a single interpolation function. Luckily for us, it’s a similar process to Arc-length parameterization except we already have all the values we need!

For example let’s assume we’re using the module from above:
    
    
    -- bzs is table with bezier urves in it in order traveled
    function travelPath(t, bzs)
    	local totalLength, sums = 0, {}
    	-- get total length of all curves, also order sums for sorting
    	for _, bz in next, bzs do
    		table.insert(sums, totalLength)
    		totalLength = totalLength + bz.length
    	end
    	-- get percentage of total distance and find the bezier curve we're on
    	local T, near, bz = t * totalLength, 0, bzs[1]
    	for i, n in ipairs(sums) do
    		if (T - n) < 0 then break end
    		near, bz = n, bzs[i]
    	end
    	-- get relative percentage traveled on given bezier curve
    	local percent = (T - near)/bz.length
    	-- lerp across curve by percentage
    	local a, b, c = bz:calcFixed(percent)
    	return a + (b - a) * c
    end
    

That’s all there is to it! We can also use Bézier curves in 3D since lerping with 3D and 2D vectors is the same.

![bezier10.gif](https://developer.roblox.com/assets/blt1098a20ff5999294/Bezier10.gif)



***__Roblox官方链接__:[Bézier Curves](https://developer.roblox.com/zh-cn/articles/Bezier-curves)