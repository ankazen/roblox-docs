# 创建滚动框架 GUI 
Time:<em>5  分钟</em>

![ScrollingFrameExample.gif](https://developer.roblox.com/assets/bltc4ce8d1f19ac09ae/ScrollingFrameExample.gif)

`ScrollingFrame` 的设置方式与常规 `Frame` 的设置方式相同。将 `ScreenGui` 添加到场景中的 `StarterGui` 中，然后插入一个 ScrollingFrame。

![ExplorerScrollingFrame.png](https://developer.roblox.com/assets/blt2e713b2033cdc5c7/ExplorerScrollingFrame.png)



  * ScrollingFrame 的位置通过其 Position 属性设置，该属性为 `DataType/UDim2`。
  * 同样，在 Size 属性中设置 ScrollingFrame 的大小，该属性也为 `DataType/UDim2`。请注意，ScrollingFrame 可能会有一个占用此部分尺寸的滚动条
  * 如果需要知道 ScrollingFrame 中的实际查看区域有多大，可以使用只读属性 `ScrollingFrame/AbsoluteWindowSize` 来获取。
  * 如果显示滚动条，则其厚度由 `ScrollingFrame/ScrollBarThickness` 属性确定。
  * ScrollingFrame 内的区域称为画布。CanvasSize 属性确定整个画布的大小。如果画布的某个尺寸比 ScrollingFrame 的尺寸宽，则会显示相应的滚动条。否则滚动条将隐藏。
  * CanvasPosition 定义显示框架时滚动条的默认位置（以像素为单位）。请注意，如果未显示滚动条，则此属性不会执行任何操作。

### 自定义滚动条

可以自定义 ScrollerFrame 中的滚动条。滚动条本身由三个图像组成：顶部、中间和底部。水平滚动条和垂直滚动条使用相同的图像（水平滚动条将垂直滚动条的图像逆时针旋转 90 度）。

滚动条中的图像根据 ScrollBarThickness 属性进行缩放。顶部图像和底部图像始终是正方形，其宽度和高度均等于滚动条的厚度。中间图像将始终具有滚动条的厚度，但是长度将根据框架尺寸和画布尺寸进行缩放。

滚动条可以按比例缩放，因此滚动条的长度与槽的长度之比等于画布大小与框架大小之比。

若要使用自定义图像，请上传要用作贴花的三个图像。建议使用缩放效果好的图像，尤其是需要拉伸的中间图像。然后，在 ScrollingFrame 的 Properties 中，将 BottomImage、MidImage 和 TopImage 更改为相应的 url。

![ScrollingFrameProperties.png](https://developer.roblox.com/assets/blt0c4b23339d01e492/ScrollingFrameProperties.png)



### 示例

本例将创建一个包含四个 `ImageLabel`（每个角上一个）的 ScrollingFrame。请注意，它是如何使用滚动条的自定义资源的：

ScrollingFrame Creation ```    
    
    -- In a LocalScript in StarterGui:
    
    -- Create ScreenGui
    local screenGui = Instance.new("ScreenGui")
    screenGui.Parent = script.Parent
     
    -- Create ScrollingFrame
    local scrollingFrame = Instance.new("ScrollingFrame")
    scrollingFrame.Position = UDim2.new(0.2, 0, 0.1, 0)
    scrollingFrame.Size = UDim2.new(0, 200, 0, 100)
    scrollingFrame.CanvasSize = UDim2.new(0, 600, 2, 0)
    scrollingFrame.BackgroundColor3 = BrickColor.White().Color
    scrollingFrame.BottomImage = "rbxassetid://156476249"
    scrollingFrame.MidImage = "rbxassetid://156476256"
    scrollingFrame.TopImage = "rbxassetid://156476261"
    scrollingFrame.Parent = screenGui
    
    -- Create images to put in ScrollingFrame
    local topLeftImage = Instance.new("ImageLabel")
    topLeftImage.Position = UDim2.new(0, 0, 0, 0)
    topLeftImage.Size = UDim2.new(0, 100, 0, 100)
    topLeftImage.BackgroundColor3 = Color3.new(255/255, 162/255, 116/255)
    topLeftImage.ZIndex = 2
    topLeftImage.ImageTransparency = 0.5
    topLeftImage.Image = "rbxassetid://133293265"
    topLeftImage.Parent = scrollingFrame
    
    local topRightImage = Instance.new("ImageLabel")
    topRightImage.Position = UDim2.new(1, -100, 0, 0)
    topRightImage.Size = UDim2.new(0, 100, 0, 100)
    topRightImage.BackgroundColor3 = Color3.new(255/255, 190/255, 216/255)
    topRightImage.ZIndex = 2
    topRightImage.ImageTransparency = 0.5
    topRightImage.Image = "rbxassetid://133293265"
    topRightImage.Parent = scrollingFrame
    
    local bottomLeftImage = Instance.new("ImageLabel")
    bottomLeftImage.Position = UDim2.new(0, 0, 1, -100)
    bottomLeftImage.Size = UDim2.new(0, 100, 0, 100)
    bottomLeftImage.BackgroundColor3 = Color3.new(28/255, 255/255, 180/255)
    bottomLeftImage.ZIndex = 2
    bottomLeftImage.ImageTransparency = 0.5
    bottomLeftImage.Image = "rbxassetid://133293265"
    bottomLeftImage.Parent = scrollingFrame
    
    local bottomRightImage = Instance.new("ImageLabel")
    bottomRightImage.Position = UDim2.new(1, -100, 1, -100)
    bottomRightImage.Size = UDim2.new(0, 100, 0, 100)
    bottomRightImage.BackgroundColor3 = Color3.new(28/255, 69/255, 255/255)
    bottomRightImage.ZIndex = 2
    bottomRightImage.ImageTransparency = 0.5
    bottomRightImage.Image = "rbxassetid://133293265"
    bottomRightImage.Parent = scrollingFrame
    
    
    0

```


***__Roblox官方链接__:[创建滚动框架 GUI](https://developer.roblox.com/zh-cn/articles/Creating-a-Scrolling-Frame-GUI)