# BodyMovers 
Time:<em>BodyMover: Code Sample 1</em>

Objects that inherit from the BodyMovers structure are used to move Parts against `gravity` and other forces.

## Shared properties

### Force, MaxTorque, and MaxForce

All BodyMovers objects have either a `Force`, `MaxTorque` or **MaxForce** property which function the same. These are Vector3 properties and depending on the amount of each axis (X,Y,Z) will be the maximum amount of force that can be applied to that axis.

BodyMover: Code Sample 1 ```    
    
    BodyPosition.MaxForce = Vector3.new(0, 1000, 0)--no movement on any axis but the Y-axis.
    
    
    0

```
### P

`P` is the amount of power used to reach a goal. The higher the P value, the faster it will move towards its goal and sometimes even surpass the goal. If set too low, the object might not even move.

### D

`D` is the amount of damping that will be used. Damping will stop the object from surpassing its goal and having to turn around. By setting a good D, it will start to slow down as it reaches its goal so that it does not go past it. The higher the D value, the more it will slow down.

## BodyAngularVelocity

`BodyAngularVelocity` is used to set a constant rotational velocity. This means it can be used to turn your part even without other forces acting upon it.

The `BodyAngularVelocity/AngularVelocity` property controls rotation. Its direction is the axis which the part rotates around, and the magnitude is the speed in radians per second at which it does it.  
![Angularvelocitydiagram.png](https://developer.roblox.com/assets/blt82602c5878a38942/Angularvelocitydiagram.png)



## BodyVelocity

`BodyVelocity` is used to set a constant velocity. This means that it can be used to move your part at a constant speed despite gravity.

The `BodyVelocity/Velocity` property is the maximum _speed_ at which an object can go while being pushed by the BodyVelocity object.

BodyMover: Code Sample 2 ```    
    
    BodyVelocity.Velocity = Vector3.new(0, 1000, 0)--sends the part at a constant speed upward
    
    
    0

```
## BodyForce

`BodyForce` will push a part with the magnitude and direction of the `BodyForce/Force` property, in world coordinates.

BodyMover: Code Sample 3 ```    
    
    -- push a 4,1.2,2 part upward, regardless of orientation
    BodyForce.Force = Vector3.new(0, 1915.52, 0)
    
    
    0

```
## BodyThrust

`BodyThrust` is similar to BodyForce, however, its force works in relation to the object. The `BodyThrust/Force` property defines the direction and magnitude the part should be pushed, in object coordinates. The `BodyThrust/Location` property defines the position where the thrust is being applied, once again in object coordinates.

BodyMover: Code Sample 4 ```    
    
    -- push a 4,1.2,2 part upward, with the center of thrust at the underside of the part
    BodyThrust.Location = Vector3.new(0, -0.6, 0)
    BodyThrust.Force = Vector3.new(0, 1915.52, 0)
    
    
    0

```
## BodyPosition

`BodyPosition` moves a brick towards a certain Vector3 point ignoring gravity. The `BodyPosition/Position` property defines the spot in which the part will attempt to move towards.

BodyMover: Code Sample 5 ```    
    
    --Moves part towards center of the world
    BodyPosition.Position = Vector3.new(0, 0, 0)
    
    
    0

```
## BodyGyro

`BodyGyro` attempts to keep a fixed orientation of the part relative to its `BodyGyro/CFrame` property. This means it will try to rotate the brick to match the rotation of the CFrame.

BodyMover: Code Sample 6 ```    
    
    --Rotates the brick to stay at a rotation of CFrame.Angles(math.pi / 2, 0, 0)
    BodyGyro.CFrame = CFrame.Angles(math.pi / 2, 0, 0)
    
    
    0

```
## RocketPropulsion

`RocketPropulsion` is used to mimic the movement of a projectile. RocketPropulsion has a lot of unique properties that can be used for maximum results.

  * `RocketPropulsion/Target` is the Part that the RocketPropulsion is shooting at.
  * `RocketPropulsion/TargetRadius` is the distance the part must be from its target to trigger its `RocketPropulsion/ReachedTarget` event.
  * `RocketPropulsion/TargetOffset` is how far from the target to shoot.
  * `RocketPropulsion/CartoonFactor` is how much the part points towards its target. 0 is pointing straight up away from the target, 1 is directly at the target. The default is 0.7 in order to counter the force of gravity.
  * `RocketPropulsion/MaxSpeed` is a number that defines the maximum speed that the part is allowed to reach.
  * `RocketPropulsion/TurnP` and `RocketPropulsion/TurnD` are the `P` and `D` properties that signify the turning Power and Dampening of the projectile.
  * `RocketPropulsion/ThrustP` and `RocketPropulsion/ThrustD` are the `P` and `D` properties that signify the movement Power and Dampening of the projectile.

BodyMover: Code Sample 7 ```    
    
    --shoots the projectile in the direction that the object is moving.
    RocketPropulsion.TargetOffset = RocketPropulsion.Target.Velocity
    
    
    0

```


***__Roblox官方链接__:[BodyMovers](https://developer.roblox.com/zh-cn/articles/BodyMovers)