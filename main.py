import numpy as np
import matplotlib.pyplot as plt
def f(x):
    conds = [
        (x >= 0) & (x < 1),
        (x >= 1) & (x <= 2)
    ]
    funcs = [
        -1.0,
        3 * x - 4
    ]
    return np.select(conds, funcs, default=np.nan)

def common(x, N):
    s = -0.25
    for n in range(1, N + 1):
        an = (3 / (n * np.pi) ** 2) * (1 - (-1) ** n)
        bn = -3 / (n * np.pi)
        s += an * np.cos(n * np.pi * x) + bn * np.sin(n * np.pi * x)
    return s


def cos(x, N):
    s = -0.25
    for n in range(1, N + 1):
        an = (12 / (n * np.pi) ** 2) * ((-1) ** n - np.cos(n * np.pi / 2))
        s += an * np.cos(n * np.pi * x / 2)
    return s


def sin(x, N):
    s = 0
    for n in range(1, N + 1):
        bn = -(2 + 4 * (-1) ** n) / (n * np.pi) - (12 / (n * np.pi) ** 2) * np.sin(n * np.pi / 2)
        s += bn * np.sin(n * np.pi * x / 2)
    return s

x_vals = np.linspace(-4, 4, 2000)
x_orig = np.linspace(0, 2, 500)
f_orig_vals = f(x_orig)
N_list = [3, 10, 30]

methods = [
    (common, 'Общий ряд Фурье'),
    (cos, 'Ряд по косинусам (четное продолжение)'),
    (sin, 'Ряд по синусам (нечетное продолжение)')
]

for func, title in methods:
    plt.figure(figsize=(10, 6))
    plt.plot(x_orig, f_orig_vals, 'red', label='f(x) на [0, 2]', zorder=10)

    for N in N_list:
        plt.plot(x_vals, func(x_vals, N), label=f'N={N}')

    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlim(-4, 4)
    plt.ylim(-5, 5)
    plt.grid(True)
    plt.legend()
    plt.show()
