Classes-in-Python---testing
===========================

In this project I explore how to create a class to store 2D world data for modelling and animation with Visual Python.

I am also testing GitHub as a way to store my code, and I am curious about the collaborative aspects of using GitHub.

My idea is to define a very simple 2D world of say 10 x 10 elements, arranged in a vertical matrix. Then I would 
like to explore what happens when an object x is released at top row and allowed to fall and collide with say 
water-like objects, 8, that are in the bottom rows. Except for the x and 8 objects there are no other physical 
objects in the world. The 0 objects are just empty space.

00123456789<br>
100000x0000<br>
20000000000<br>
30000000000<br>
40000000000<br>
50000000000<br>
60000000000<br>
78888888888<br>
88888888888<br>
98888888888<br>

Some data for the world could be:
-gravity: g<br>
-size: x, y<br>

For each element I plan to store information about the initial condition, like:
-position: x0, y0<br>
-velocity: vx0, vy0<br>
-acceleration: ax0, ay0<br>
-mass: m0<br>
-color: c0  #three values: r, g, b<br>

Some information about boundary conditions should be stored for each element. In my simple world I will start with the 
following assumptions:<br>
-the world is vertical. That is, one row of elements is on the ground, then the next row is placed right on top of it and so on.<br>
-the elements on the edge can not move. (Or should I allow them to move away and leave the world?)<br>
-the bottom row of elements sits firmly on "the ground".<br>
-the mass of the elements <br>

I think I will include member variables in the element class to store the dynamical values that vil be created and 
used during the animation. These will in the general case include many of the same physical parameters that are stored for definition of the initial conditions:<br>
-x,y<br>
-vx, vy<br>
-ax, ay<br>
-m<br>
-c<br>

Then I think I will need some rules to calculate the new velocity after collision of two elements. I will start with:<br>
-movement can only be in the x or y directions (this is very limiting, will produce uninteresting animations, I think)<br>
-when an element falls on and collides with another element, then 80% of the impuls energy is transfered to the element
below the element and 10% to the elements that are on each side of it. If there are no elements adjacent then the 
energy disappears.<br>

Ok, these are my first thoughts on the problem.
