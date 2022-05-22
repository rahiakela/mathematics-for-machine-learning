from math import sqrt, sin, cos, pi, atan2


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


def to_cartesian(polar_vector):
    lengths, theta = polar_vector[0], polar_vector[1]
    return lengths * cos(theta), lengths * sin(theta)


def to_polar(vector):
    x, y = vector[0], vector[1]
    theta = atan2(y, x)
    return length(vector), theta


def rotate(angle, vectors):
    polors = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a + angle)) for l, a in polors]
