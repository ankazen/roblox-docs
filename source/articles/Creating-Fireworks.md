# Creating Fireworks 
Time:<em></em>

Particle effects come in two varieties: continuous particles like snow or burst particles like fireworks. In this tutorial, we’ll create a fireworks particle effect using several ParticleEmitters and the Emit method. Below a preview of the effect you’ll create in following these steps:

![An animation of the Fireworks burst particle effect](https://developer.roblox.com/assets/blt2a03389914b8185e/fireworks.gif)

## A Note About Creating Burst Particle Effects

This tutorial creates a burst particle effect, which means at the end we’ll need to use `ParticleEmitter/Emit` to spawn many particles at the same time. We can use the Command Bar to call the method while working, but the default `ParticleEmitter/Rate` of emission will suffice for previewing particles. At a certain point, we’ll turn this off (set `ParticleEmitter/Rate` to 0) in favor of using the Emit method. At the moment, there’s no native Studio tool to emit a burst of particles, but you can create or [install a Roblox Studio plugin](https://www.roblox.com/library/303835976/ParticleEmitter-Emit-n) to allow this.

# Steps

  1. Under the Home tab in the Insert section, insert a `Part`.  
![Inserting a Part](https://developer.roblox.com/assets/blt9d8d6a8b75616bbd/InsertPart.png)

![The newly inserted Part](https://developer.roblox.com/assets/blt594ca29a5b53c870/SelectedPart.png)


  2. Under the Model tab in the Constraints section, select `Attachment`. With that tool selected, click once in the game view to create an Attachment object. In the Explorer window, notice how the object has been parented to the Part.  
![Creating a new Attachment](https://developer.roblox.com/assets/blta997e49199217d1f/CreateAttachment.png)

![The new Attachment viewed in the Explorer](https://developer.roblox.com/assets/bltda778cdc5cce9854/ExplorerAttachment.png)


  3. In the Properties window, set the Attachment’s Position to 0, 15, 0. This is the position of the Attachment relative to the parent Part. We want the attachment somewhat high off the ground.  
![The Attachment's Position property](https://developer.roblox.com/assets/blt845025e49f8b244e/AttachmentPosition.png)


  4. Next, add a `ParticleEmitter` to the Attachment. Select the Attachment, then press CTRL+I to open the Advanced Objects menu. Type “particle” and find ParticleEmitter to insert it. Since the ParticleEmitter is within the Attachment, the particles will be emit from the attachment point.  
![The newly inserted ParticleEmitter](https://developer.roblox.com/assets/blt91f958744112caa8/NewParticleEmitter.png)


  5. Fireworks are short-lived particles. We begin editing the ParticleEmitter by change its `ParticleEmitter/Lifetime` to 2, 3 so particles last somewhere between 2 and 3 seconds.
  6. When a firework charge explodes, it sends colorful flares in all directions. To send particles in all directions, we need to set the ParticleEmitter’s SpreadAngle. This property is a bit confusing, so try the following values at first: 
    1. By default, this property is 0, 0 so there is no variation in direction. The particles should shoot straight upward.
    2. Try setting it to 90, 0. This will cause particles to emit in a half-circle shape. Notice how the angle applies in both directions (90 creates a total angle of 180)  
![Setting the SpreadAngle to 90, 0](https://developer.roblox.com/assets/blt4f71c44941e47645/ParticleSpreadAngle90_0.png)


    3. Setting it to 90, 90 will create a half-sphere shape, as it will apply the spread on both angles.
    4. For creating a firework charge, set it to 135, 135. This almost completely random in direction save for a few downward directions. In 2D, this is what is happening:  
![Setting the SpreadAngle to 135, 135](https://developer.roblox.com/assets/bltb56c29500b12eb2e/ParticleSpreadAngle135_135.png)


  7. Next, set the ParticleEmitter’s `ParticleEmitter/Speed` to 30 and `ParticleEmitter/Drag` to 5. This will cause the particles to fly out fast then decelerate quickly. To simulate gravity, set `ParticleEmitter/Acceleration` to 0, -5, 0.
  8. Next let’s decide on how the particles are to look. Start by setting the ParticleEmitter’s `ParticleEmitter/LightEmission` to 1 so the particles’ colors blend additively. Also set the `ParticleEmitter/LightInfluence` to 0 so the particles aren’t made dark by the night sky!
  9. Particles should fade out only toward the end of the particles’ lifetimes. Select the ParticleEmitter’s `ParticleEmitter/Transparency` then press the […] button to open a graph. Add a stop at Time = 0.5 in the center by clicking. Set its value to 0. Raise the end stop (at Time = 1) to 1.  
![The Transparency graph for the ParticleEmitter](https://developer.roblox.com/assets/blt0412e4c89f1441f8/FireworkTransparencyGraph.png)


  10. Next, let’s decide on the color of the particles. Since fireworks often have multiple colors, we’ll have to create multiple ParticleEmitters. Press CTRL+D a few times (1 for each with the ParticleEmitter selected to duplicate it. On each particle emitter, set the Color property to a unique color. You should also rename each emitter to its color. Try the following colors: 
    1. Red: 255, 63, 63
    2. Yellow: 63, 255, 255
    3. Green: 63, 255, 63
    4. Blue: 63, 63, 255
    5. Orange: 255, 127, 63
    6. Purple: 255, 63, 255
  11. Since this is a burst particle effect, set `ParticleEmitter/Enabled` to false on each ParticleEmitter. You can also set Rate to 0.  
**Tip:** You can select all the ParticleEmitters by holding CTRL and left clicking each emitter in the Explorer.
  12. To preview the result, you’ll need to emit particles on all the emitters at once. To do this, type (or copy and paste) the following command in the Command Bar and press enter.
    
    
    local emitters = workspace.Part.Attachment:GetChildren(); for _, emitter in pairs(emitters) do emitter:Emit(10) end
    

When all is said and done, you should have a nice exciting firework effect!

![An animation of the Fireworks burst particle effect](https://developer.roblox.com/assets/blt2a03389914b8185e/fireworks.gif)



***__Roblox官方链接__:[Creating Fireworks](https://developer.roblox.com/zh-cn/articles/Creating-Fireworks)