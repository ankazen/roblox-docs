# Virtual Reality – Best Practices 
Time:<em></em>

Developing games and experiences in VR provides unique opportunities and challenges. While standard practices in terms of game balance, level design, narrative structure can all be considered when creating a VR experience, there are several other considerations to take into account. This article will discuss the various principles that Roblox and other VR designers have learned. It will also cover some of the more speculative concepts that are still being worked out as this new technology is explored and developed.

**Comfort**: The first and most important factor to consider when designing for a VR experience is comfort. If not designed well, a VR experience can cause motion sickness. The mechanics and design of your game should take great care to make sure the player has a good experience and is not uncomfortable. Comfort mainly has to do with how the camera is controlled, but there are other things that contribute. 

**Presence**: The other thing you should focus on during development is maintaining your players’ belief that they are actually in the experience rather than watching it. VR is at its core an immersive experience, and the more you increase the immersion of your game the more you will take advantage of the platform. 

## Comfort

Roblox as a platform is always working to do whatever it can on the engine and platform side to ensure a comfortable experience. This includes creating good default camera and movement controls, including comfort as a sort parameter, and removing core 2D GUI elements. But there are many things that you, as a developer, can do beyond the platform to provide a comfortable experience.

### Movement

Camera motion can be a big contributor towards motion and simulator sickness. Some of the best experiences in VR involve little to no camera motion outside tracking the player’s head motions. That said, if you do need the camera to move beyond head tracking, there are a few practices that you can follow to ensure a more comfortable experience.

Make sure any motion is slow and at a constant velocity. Accelerations in general can cause motion sickness. Keep in mind acceleration does not just mean acceleration forward. Falling, turning, swinging, all of these motions fundamentally involve acceleration. Jumping for instance can be quite uncomfortable in VR, even if it is explicitly controlled by the player.

Backward and lateral motion, like acceleration, can also be uncomfortable. In general, try to keep motion along the axis that the player is looking.

Motion is also more comfortable in VR if the player has some control over it. Unexpected motion that are outside the player’s control, such as head bobbing, camera shaking, etc, is uncomfortable in VR and should be avoided. Similarly, removing control, such as disabling head tracking will also be uncomfortable. Even if nothing is happening in the game, the player should still be able to look around naturally.

**Using 3rd Person for Faster Avatar Motion**  
For first person experiences, users tend to prefer slower movement (around a walking pace). If your game need to feature fast turns, acceleration, and jumping, consider switching the perspective to a 3rd person camera that smoothly follows the character. Do not attach the camera to an offset from the character, but rather let the camera float and move at a constant speed to keep up with the character. In this mode it is also important to still let the player freely move their head. 

### Teleporting

Another solution to motion is to not provide any interpolated movement at all but instead teleport the player from location to location. Keep in mind this technique has not yet been thoroughly explored, so it is not yet clear if players generally find this solution more comfortable.

**Using Vehicles**  
Vehicles make a nice setting for a VR experience as the player will often be sitting in real life while playing. Vehicles can also create motion sickness though, so as with character motion you have to be careful with how the vehicle moves. One great rule to follow when adding a vehicle, always make sure some part of the vehicle is visible regardless of where the player looks. This will give the player a static reference they can use to ground themselves. 

### Performance

Performance is a critical and foundational element of comfort. If a game jitters or lags, players will likely feel discomfort. It is important to make sure that you develop within the current capabilities of the Roblox platform. While developing a VR experience, you will have to be very careful about performance heavy elements, such as player and part count, along with general script overhead.

## Presence

After comfort, presence is the most important consideration in developing a great VR experience. Presence refers to how much the player feels like they are immersed and engaged with their environment. There are several key things that break presence:

  * Lack of comfort
  * Confusion - what to do, where to go, what’s happening
  * Shallow object interactions - players expect drawers to open, door knobs to work, etc
  * Unintuitive interactions - everyday interactions that work differently in VR than expected
  * Too intense - anything that makes someone want to rip off the headset
  * Unrealistic audio - not spatially distributed, no distance attenuation
  * Proprioceptive disconnect - you are sitting down and your avatar is running

### Engagement

Taken to the extreme, the above ideas suggest that everything in the environment should be fully realized and interactive. While this is a great ambition to strive for, there are many practical considerations that will likely limit your scope (performance, design, engineering hours).

Instead of simply trying to make everything interactive to the extreme, be very deliberate when designing the actions the player can take. If a game is mostly about combat, the player’s attention will likely be focused on relevant actions, and not on mundane interactions they might expect the environment to have.

[Google’s Cardboard Design Lab](https://play.google.com/store/apps/details?id=com.google.vr.cardboard.apps.designlab&hl=en) has some great examples of how you can use visual signals to direct players towards engaging parts of a space. These signals can be subtle (people generally walk towards the light and away from darkness) or more direct (a flashing neon “Open” sign). The proper signaling can lead the player towards engaging activities with interactive 3D objects, and away from visual set pieces that simply create ambiance.

### Audio

Audio cues can be a subtle yet powerful tool to draw players into a VR experience. The key here though is to make use of Roblox’s positional audio. If an interaction or object makes a sound, the sound should be positioned at the point of interaction. For example, if a player opens a drawer, the Sound instance should be place inside the drawer model.

Try to make ambient noises (such as birds singing, water dripping, generators humming) positioned as well. Even if you don’t have specific models for these objects, simply giving them some presence in the environment that changes as the player moves will further the sense of immersion.

### GUIs and Text

2D GUIs drawn directly to the screen should not be used in VR. These both break presence and are uncomfortable. Instead, try to integrate interface elements into the 3D space in your world. The simplest approach is to simply place 2D GUIs on 3D objects like billboards, but there are many creative ways to convey information to your player. Here are some examples:

  * Make ammo utilization a gauge on a 3D weapon rather than a 2D HUD
  * Replace 2D text boxes with 3D text annotations on objects
  * Use a virtual tablet for menu selection rather than a 2D HUD
  * Replace a 2D gun target with a 3D laser and reticle projected on the interested object

### Intensity

If a VR experience is very immersive, the intensity of actions and events can be increased. This should be considered when designing a VR experience. A monster jumping at a player in VR will be more pronounced in a VR experience if that experience is very immersive. A developer should carefully test and tune their experience and make sure that if the presence in their game is high that they scale back the intensity to preserve player comfort.

### Scale

When building an experience in VR special attention should be given to the scale of buildings and objects. Games in 3rd person typically feature wide spaces and high ceilings to accommodate the camera. In 1st person, these types of spaces can seem unrealistic which can diminish presence. Unless your experience needs to play with scale for narrative or stylistic effects, try to make sure that objects in the experience are scaled to the size of the player’s character.

The default Roblox character model does not follow standard human proportions, so figuring out scale can be tricky at first glance. It is recommended to start with the vertical size of objects with the height of the character. Then, adjust the horizontal size to balance realism while still accommodating the width of the character. For default sized Roblox characters, 1 stud should be treated as 30 centimeters.

## Sample Places

The RobloxVR account has many open-sourced VR places you can edit for inspiration and reference. Click [here](https://www.roblox.com/users/118201647/profile#!/creations) to see all of these sample places.

## Further Reading

  * [Oculus Published Best Practices](https://developer.oculus.com/documentation/intro-vr/latest/concepts/book-bp/)
  * [Cardboard Design Lab App](https://play.google.com/store/apps/details?id=com.google.vr.cardboard.apps.designlab&hl=en)
  * [Talk by Kimberly Vol about Presence, Comfort, and Intensity](http://www.gamesindustry.biz/articles/2016-03-15-our-brains-essentially-are-always-screwing-with-us)
  * **[I Expect you to Die** VGDC Presentation](http://www.gdcvault.com/play/1023671/Lessons-Learned-from-I-Expect)



***__Roblox官方链接__:[Virtual Reality – Best Practices](https://developer.roblox.com/zh-cn/articles/Virtual-Reality-Best-Practices)