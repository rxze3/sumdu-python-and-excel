import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
p = np.array([0.1, 0.2, 0.3, 0.25, 0.15]) 

def expectation(values, probabilities):
    return np.sum(np.multiply(values, probabilities))

def variance(values, probabilities, exp_val):
    return np.sum(np.multiply((values - exp_val)**2, probabilities))

E_X = expectation(x, p)
Var_X = variance(x, p, E_X)
Std_X = np.sqrt(Var_X) 

print(f"Математичне сподівання (E_X): {E_X:.4f}")
print(f"Дисперсія (Var_X): {Var_X:.4f}")
print(f"Стандартне відхилення (Std_X): {Std_X:.4f}")

plt.bar(x, p, color='skyblue', edgecolor='black')
plt.xlabel('Значення дискретної випадкової величини (Х)')
plt.ylabel('Ймовірність P(X)')
plt.title('Стовпчаста діаграма розподілу дискретної випадкової величини')
plt.grid(True, axis='y')
plt.show()