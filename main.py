from math import sqrt
from random import randint

points1 = [(2, 23), (4, 37.5), (8, 80.34), (9, 98)]  # couples (x,y)


def gradient(f, x):
    precision = 0.1
    a = x-precision
    b = x+precision
    return (f(a)-f(b))/(a-b)


def cost_func(points, f):
    quadratic_sum = 0
    for point in points:
        y1 = f(point[0])
        quadratic_sum += (y1-point[1])**2
    return quadratic_sum/len(points)


def gradient_descent(f, leap, precision):
    """
    The gradient descent algorithm: searches the minimum of the given function f
    :param f: the function
    :param leap: the leap or step taken at each turn
    :param precision: the precision of the result
    :return: the minimum of f
    """
    x = 2
    grad = old_grad = gradient(f, x)
    signe = (1, -1)[randint(0, 1)]
    while abs(grad) > precision:
        x += leap * signe
        grad = gradient(f, x)
        if abs(grad) > abs(old_grad):
            signe *= -1
        old_grad = grad
    return x


print(cost_func(points1, lambda x: 3*x))
a1 = gradient_descent(lambda a: cost_func(points1, lambda x: a*x), 0.01, 1)
print(a1, round(a1))
# lambda a: cost_func(points1, lambda x: a*x)
# a --> le coefficient de la fonction linéaire ax
# en gros: je cherche le minimum de la fonction de coût en fonction du coefficient directeur a
# print(gradient_descent(lambda a: cost_func(points1, lambda x: a*x), 0.01, 0.001))
