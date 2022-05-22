from vector_drawing import *
from vectors import *


if __name__ == '__main__':
    # verify that 5 units at an angle of 37° gets us close to the point (4, 3)
    angle = 37 * pi / 180
    print(to_cartesian((5, angle)))

    # verify some simple examples
    print(to_polar((1, 0)))
    print(to_polar((-2, 3)))

    # Confirm that the vector given by Cartesian coordinates (–1.34, 2.68) has a length of approximately 3 as expected
    print(length((-1.34, 2.68)))

    # convert these to Cartesian coordinates and connect them in a
    # closed loop with line segments to draw a picture
    polar_coords = [(cos(x * pi / 100.0), 2 * pi * x / 1000.0) for x in range(0, 1000)]
    vectors = [to_cartesian(p) for p in polar_coords]
    draw(Polygon(*vectors, color=green))


