from draw3d import *
from math import sqrt


def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    return tuple(coordinate_sums)


def add1(*vectors):
    return tuple(map(sum, zip(*vectors)))


def length(v):
    return sqrt(sum([coords ** 2 for coords in v]))


if __name__ == '__main__':

    # extracts x, y and z coordinates
    print(list(zip(*[(1, 1, 3), (2, 4, -4), (4, 2, -2)])))

    # sum x, y and z coordinates values
    print([sum(coords) for coords in [(1, 2, 4), (1, 4, 2), (3, -4, -2)]])
    
    # do the same with add
    print(add((1, 1, 3), (2, 4, -4), (4, 2, -2)))
    print(add1((1, 1, 3), (2, 4, -4), (4, 2, -2)))
    
    # get length of 3d vector
    print(length((3, 4, 12)))

    """
    Exercise-1
    Draw (4, 0, 3) and (–1, 0, 1) as Arrow3D objects, such that they
    are placed tip-to-tail in both orders in 3D. What is their vector sum?
    """
    print(add((4, 0, 3), (-1, 0, 1)))
    draw3d(
        Arrow3D((4, 0, 3), color=red),
        Arrow3D((-1, 0, 1), color=blue),
        Arrow3D((3, 0, 4), (4, 0, 3), color=blue),
        Arrow3D((-1, 0, 1), (3, 0, 4), color=red),
        Arrow3D((3, 0, 4), color=purple),
    )
