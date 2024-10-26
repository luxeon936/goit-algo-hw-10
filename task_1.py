from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem(name="production-optimization", sense=LpMaximize)

x1 = LpVariable(name="Лемонад", lowBound=0, cat="Integer")
x2 = LpVariable(name="Фруктовий сік", lowBound=0, cat="Integer")

model += x1 + x2, "Загальна кількость продуктів"
model += (2 * x1 + 1 * x2 <= 100), "Обмеження води"
model += (1 * x1 <= 50), "Обмеження цукру"
model += (1 * x1 <= 30), "Обмеження лимонного соку"
model += (2 * x2 <= 40), "Обмеження фруктового пюре"
model.solve()

lemonade_count = value(x1)
fruit_juice_count = value(x2)
total_products = value(model.objective)

print(f"Кількість Лимонаду: {lemonade_count}")
print(f"Кількість Фруктового соку: {fruit_juice_count}")
print(f"Загальна кількість продуктів: {total_products}")