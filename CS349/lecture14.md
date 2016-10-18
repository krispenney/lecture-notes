# Lecture 14 - October 14, 2016

## Assignment 1 Review

### CatsEyes
Key Problem:
* Have an event queue, take off queue and handle it.
* On X, client generating at full speed (without Thread Sleep) would cause glitches on server.
* After Sleep, Eyes can't keep up --> Event buildup.
* Just put in a while loop causes problems
  * With a lot of events, stays in the while loop
  * painting and sleep don't happen.
* **Solution**: handle events until sleep / dynamic sleeping.
``` Java
  long targetRepaintTime = now() + 1000/FPS;
  while(true){
    if(now() > targetRepaintTime){
      paint
      targetRepaintTime = now() + 1000/FPS;
    }

    if(is an event){
      handle it
    }else{
      sleep(now() - 1000/FPS);
    }
  }
```

## Visual Perception

### Temporal Resolution
* How we see over time.
* **Critical Flicker Frequency**: light changes from flickering to continuous light.
