from vector_drawing import *
from math import sqrt, pi
from random import uniform
from vectors import *


if __name__ == '__main__':
    # we can draw the points outlining the dinosaur
    dino_vectors = [
        (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
        (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
        (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
    ]
    # rotate the dinosaur
    rotation_angle = pi / 4
    dino_polar = [to_polar(v) for v in dino_vectors]
    dino_rotated_polar = [(l, angle + rotation_angle) for l, angle in dino_polar]
    dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]
    draw(Polygon(*dino_vectors, color=gray), Polygon(*dino_rotated, color=red))

    # we could first rotate and then translate the dinosaur.
    new_dino = translate((8, 8), rotate(5 * pi / 3, dino_vectors))
    draw(Polygon(*dino_vectors, color=gray), Polygon(*new_dino, color=red))

