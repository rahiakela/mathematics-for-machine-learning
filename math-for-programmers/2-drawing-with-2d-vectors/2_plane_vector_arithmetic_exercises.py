from vector_drawing import *
from math import sqrt
from random import uniform


def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


def length(v):
    return sqrt(v[0] ** 2 + v[1] ** 2)


def sum_cordinate(**vectors):
    """
    It adds any number of vectors together by summing all of their x-coordinates
    and all of their y-coordinates
    """
    return sum([v[0] for v in vectors]), sum([v[1] for v in vectors])


def translate(translation, vectors):
    """
    It takes a translation vector and a list of input vectors, and returns a list of the
    input vectors all translated by the translation vector.
    """
    return [add(translation, v) for v in vectors]


def scale(scaler, v):
    return scaler * v[0], scaler * v[1]


def subtract(v1, v2):
    return v1[0] - v2[0], v1[1] - v2[1]


def distance(v1, v2):
    return length(subtract(v1, v2))


def perimeter(vectors):
    distances = [
        distance(vectors[i], vectors[(i + 1) % len(vectors)])
        for i in range(0, len(vectors))
    ]
    return sum(distances)


def hundred_dinos():
    translations = [
        (12 * x, 10 * y)
        for x in range(-5, 5)
        for y in range(-5, 5)
    ]
    dinos = [
        Polygon(*translate(t, dino_vectors), color=blue)
        for t in translations
    ]
    draw(*dinos, grid=None, axes=None, origin=None)


if __name__ == '__main__':
    # we can draw the points outlining the dinosaur
    dino_vectors = [
        (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
        (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
        (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
    ]

    dino_vectors2 = [add((-2.5, -3.5), v) for v in dino_vectors]
    draw(
        Points(*dino_vectors, color=blue),
        Polygon(*dino_vectors, color=blue),
        Points(*dino_vectors2, color=red),
        Polygon(*dino_vectors2, color=red)
    )

    # draw a segment
    # draw(Points((2, 2), (-1, 3)), Segment((2, 2), (-1, 3), color=red))

    # show 100 simultaneous and non-overlapping copies of the dinosaur
    # hundred_dinos()

    # Which is longer, the x or y component of (3, –2) + (1, 1) + (–2, –2)?
    # print(sum_cordinate(([3, -2], [1, 1], [-2, -2])))
    
    # What are the components and lengths of the vectors (–6, –6) and (5, –12)?
    print(length((-6, -6)), length((5, -12)))
    
    # What vector in the dino_vectors list has the longest length?
    print(max(dino_vectors, key=length))

    # adding and scaling
    u = (-1, 1)
    v = (1, 1)
    possibilities = [
        add(scale(uniform(-3, 3), u), scale(uniform(-1, 1), v))
        for i in range(0, 500)
    ]
    # draw(Points(*possibilities))

    # use a square with side length of one as a sanity check
    print(perimeter([(1, 0), (1, 1), (0, 1), (0, 0)]))
    # Then we can calculate the perimeter of the dinosaur
    print(perimeter(dino_vectors))

