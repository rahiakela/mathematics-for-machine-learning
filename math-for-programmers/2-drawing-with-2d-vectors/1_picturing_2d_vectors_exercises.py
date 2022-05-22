from vector_drawing import *


if __name__ == '__main__':
    # we can draw the points outlining the dinosaur
    dino_vectors = [
        (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
        (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
        (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
    ]

    # 1-Draw the point in the plane and the arrow corresponding to the point (2, –2).
    draw(Points((2, -2)), Segment((0, 0), (2, -2)))

    # 2-Draw the dinosaur with the dots connected by constructing a Polygon object with the dino_vectors as its vertices.
    draw(Points(*dino_vectors), Polygon(*dino_vectors))

    # 3-Draw the vectors (x,x**2) for x in the range from x = –10 tox = 11) as points (dots) using the draw function.
    draw(Points(*[(x, x ** 2) for x in range(-10, 11)]), grid=(1, 10), nice_aspect_ratio=True)
