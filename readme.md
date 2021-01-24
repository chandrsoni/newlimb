create a 2 bone arm that touches or leads to a point in the 3d space
1 point fixed
2nd point pointing towards target

initial idea:
- 2-5 servo motors
- 1st (very sure) on (0,0)
- 2nd for 2 dimensional moving on (0,0)
- 3rd on 1st and 2nd bone

First method(direct compute)
y = l* sin(a) + l * sin(b)
x = l * cos(a) + l * cos(b)
 0 < b < 180

 Second method(gradient change):
 derivatives of x and y with a and b
 move delta in the direction of the final point
 delta would be constant(might rethink this)