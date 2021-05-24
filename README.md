# Maths

Notes and experiments in maths.

## Vectors

Vector arithmetic is implemented in [vector.py](./vector.py). Usage and notes are in [the vector notebook](./vectors.ipynb).

## Angles and Trig

### The Trigonometric functions

The mnemonic: `SOH CAH TOA`

$\sin(\theta) = opposite / hypotenuse$

$\cos(\theta) = adjacent / hypotenuse$

$\tan(\theta) = opposite / adjacent$

The result of each function is a ratio. The *tangent* of an angle is the vertical distance covered divided by the horizontal. In comparison, the *sine* and *cosine* is the vertical and horizontal distance covered relative to the overall distance (hypotenuse).

Given an 37° angle:



For every 5 units traveled at 37°, 3 vertical units are covered: $\sin(37°) = 3 / 5$

For every 5 units traveled at 37°, 4 horizontal units are covered: $\cos(37°) = 4 / 5$

#### Polar to cartesian

Given a known angle $\theta$ and distance $r$ (hypotenuse) the cartesian components are:

$x = r * \cos(\theta)$

$y = r * \sin(\theta)$

![](./images/trig.png)