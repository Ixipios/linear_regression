from math import sqrt
from random import randint

points1 = [(2, 23), (4, 37.5), (8, 80.34), (9, 98)]  # couples (x,y)
points2 = [(1, 3), (3, 9), (4, 12), (6, 18), (7, 21)]


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


def gradient_descent1(f, leap, precision):
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


# Algorithms for multivariables functions
def partial_derivative(f, var_index, h, args):
    vars_h = []
    for i in range(len(args)):
        if i == var_index:
            vars_h.append(args[i] + h)
        else:
            vars_h.append(args[i])
    return (f(*vars_h)-f(*args))/h


def norm(grad):
    return sqrt(sum([i**2 for i in grad]))


def normalize(vector):
    vec_norm = norm(vector)
    return tuple([i/vec_norm for i in vector])


def gradient_descent2(f, precision, n_vars, leap):
    """

    :param leap: A sort of leap (it's a coefficient the gradient is multiply by)
    :param f: the function
    :param precision:
    :param n_vars: the number of variables the function takes in
    :return:
    """
    point = [2]*n_vars  # the starting point
    # print(point)
    grad = [10**2]*n_vars  # the gradiant of the function
    # a loop that will stop when the gradiant norm (length) of the function is really close to zero
    while norm(grad) > precision:
        # calculates the gradiant which each coordinate is the partial derivative with respect to each variable of f
        for i in range(n_vars):
            grad[i] = partial_derivative(f, i, 0.0001, point)
        # print("point", point)
        # we take the opposite of the gradient which "points" to the local minimum of the cost func
        # hoping it is the global one
        grad = [-i for i in grad]
        # print("grad", grad)
        for i in range(n_vars):
            point[i] += leap*(grad[i])
    return point


# print(cost_func(points1, lambda x: 3*x))
a1 = gradient_descent1(lambda a: cost_func(points1, lambda x: a*x), 0.01, 1)
# print(a1, round(a1))
# lambda a: cost_func(points1, lambda x: a*x)
# a --> le coefficient de la fonction linéaire ax
# en gros: je cherche le minimum de la fonction de coût en fonction du coefficient directeur a
# print(gradient_descent(lambda a: cost_func(points1, lambda x: a*x), 0.01, 0.001))


print(gradient_descent2(lambda a, b: cost_func(points2, lambda x: a*x+b), 0.0001, 2, 0.01))
# print(gradient_descent2(lambda x, y: x**2+y**2, 0.1, 2))
