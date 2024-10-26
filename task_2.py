import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def f(x):
    return x**4

a = -2  # Нижня межа
b = 2  # Верхня межа

N = 1000 # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

# Точки під кривою
under_curve = np.sum(y_rand < f(x_rand))

# Площа
rect_area = (b - a) * f(b)

# Оцінка площі під кривою (значення інтеграла)
monte_carlo_result = (under_curve / N) * rect_area

# Аналітичне обчислення інтеграла за допомогою SciPy функція quad
quad_result, quad_error = spi.quad(f, a, b)

print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Аналітичний інтеграл (quad): {quad_result} ± {quad_error}")

# Створення діапазону значень для x
x = np.linspace(-2.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Додавання точок Монте-Карло на графік (приклад 500 точок)
ax.scatter(x_rand[:500], y_rand[:500], c=(y_rand[:500] < f(x_rand[:500])), cmap='coolwarm', s=1)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^4 від {a} до {b}')
plt.grid()
plt.show()