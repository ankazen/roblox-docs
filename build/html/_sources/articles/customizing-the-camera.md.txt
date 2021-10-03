# Customizing the Camera 
Time:<em>built-in</em>

Roblox offers several built-in options for configuring the game’s camera, along with the ability to script a more `/articles/Camera manipulation|customized camera system`.

## Built-In Settings

Common camera settings can be configured directly within Roblox Studio:

  1. In the **Explorer** window, select the **StarterPlayer** object.
![](https://developer.roblox.com/assets/blt07d7b5344faf62e3/Explorer-StarterPlayer.png)



  2. In the **Properties** window, scroll down to locate the **Camera** section. Using these options, you can easily configure your game’s camera.
![](https://developer.roblox.com/assets/bltd3366ce3170b487b/Properties-Camera.png)



### Zoom Distance

Together, **CameraMaxZoomDistance** and **CameraMinZoomDistance** set the span in which players can zoom the camera in respect to their player character. Setting a very high maximum like 500 will let players zoom the camera far out in space.

![](https://developer.roblox.com/assets/blt88811648a16aa3e0/Camera-Zoom-Range.svg)

If you want to lock the camera to a specific distance away from the player, set both of these properties to the same value. 

### Camera Mode

The **CameraMode** property sets the overall behavior of the camera:

Setting Description

**Classic**
The classic Roblox camera which allows players to zoom in and out (unless zoom is locked) and rotate the camera around the player.

**LockFirstPerson**
Locks the camera to first-person mode. When in this mode, all parts/elements of the player's character are invisible to them, except for equipped `articles/intro to player tools|tools`.

### Occlusion Mode

The **DevCameraOcclusionMode** property controls camera behavior when the player cannot see their character:

Setting Description

**Zoom**
If the player's character moves behind an object with `BasePart/Transparency|Transparency` lower than **0.25**, the camera zooms in very close to the character so that he/she can be seen. Once the character moves back into a viewable position, the camera zooms back out.

**Invisicam**
If the character moves behind an object (opaque or transparent), the camera remains in position but the object becomes semi-transparent so that the character can be seen. Once the character moves back into a viewable position, the object returns to its normal opacity.

Uh oh! Your browser doesn't appear to support embedded videos! Here is a [direct link]() to the video instead. 

### Movement Mode

The **DevComputerCameraMovementMode** (computer) and **DevTouchCameraMovementMode** (phone/tablet) determine how the player can move the camera around.

Setting Description

**Classic**
The camera remains at its zoom distance between the player's view and their character, tracking the character as it moves around the world. The camera can also be pitched up/down and rotated in an orbit around the character.

**Follow**
Similar to "Classic" but the camera will rotate to face the player's character if it's moving in any direction that isn't parallel to the direction the camera is facing.

**Orbital**
The camera remains at its zoom distance and tracks the character as it moves around the world. It can be rotated in an orbit around the character, but it can **not** be pitched up/down.

**UserChoice**
Allows players to choose their desired camera movement mode from the in-game **Settings** menu. Note that "Orbital" is not an option through the menu.

## Full Customization

If you prefer to script your own camera system, see the related articles below for guidance.



***__Roblox官方链接__:[Customizing the Camera](https://developer.roblox.com/zh-cn/articles/customizing-the-camera)