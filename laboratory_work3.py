import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

print("--- 1. Завантаження даних ---")
data = pd.read_csv('seattle-weather.csv')

print("\nПеревірка на пропущені значення:")
print(data.isnull().sum())

# 2. аналіз характеристик 
print("\n--- 2. Статистичні характеристики ---")
column_name = 'temp_max'

mean_value = data[column_name].mean()
median_value = data[column_name].median()
mode_value = data[column_name].mode()[0]
variance_value = data[column_name].var()
std_deviation = data[column_name].std()

print(f"Аналіз параметра: {column_name}")
print(f"Середнє значення: {mean_value:.2f}")
print(f"Медіана: {median_value:.2f}")
print(f"Мода: {mode_value:.2f}")
print(f"Дисперсія: {variance_value:.2f}")
print(f"Стандартне відхилення: {std_deviation:.2f}")

# 3. візуалізація
print("\n--- 3. Візуалізація даних ---")
print("Генеруємо графіки... (закрийте вікно графіка, щоб код продовжив роботу)")

# 3.1. гістограма
plt.figure(figsize=(10, 6))
sns.histplot(data[column_name], bins=30, kde=True, color='skyblue')
plt.title('Гістограма розподілу максимальної температури')
plt.xlabel('Максимальна температура (temp_max)')
plt.ylabel('Частота')
plt.savefig('histogram.png')
plt.show()

# 3.2. діаграма розсіювання
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['temp_max'], y=data['temp_min'], color='orange')
plt.title('Залежність між максимальною та мінімальною температурами')
plt.xlabel('Максимальна температура (temp_max)')
plt.ylabel('Мінімальна температура (temp_min)')
plt.savefig('scatter.png')
plt.show()

# 4. довірчі інтервали
print("\n--- 4. Довірчі інтервали ---")
sample = data[column_name]
n = len(sample)
confidence = 0.95

sem = stats.sem(sample)
h = sem * stats.t.ppf((1 + confidence) / 2, n - 1)
lower_bound = mean_value - h
upper_bound = mean_value + h

print(f"Довірчий інтервал для середнього з рівнем довіри {confidence*100}%:")
print(f"[{lower_bound:.2f}; {upper_bound:.2f}]")

# 5. експорт в excel
print("\n--- 5. Експорт в Excel ---")
# Створення DataFrame з результатами
results = pd.DataFrame({
    'Показник': ['Середнє значення', 'Медіана', 'Мода', 'Дисперсія', 'Стандартне відхилення'],
    'Значення': [mean_value, median_value, mode_value, variance_value, std_deviation]
})

# збереження в Excel
with pd.ExcelWriter('results.xlsx') as writer:
    results.to_excel(writer, sheet_name='Статистика', index=False)

print("Дані успішно збережено у файл 'results.xlsx'. Графіки збережено як 'histogram.png' та 'scatter.png'.")

# коефіцієнт кореляції Пірсона
correlation, p_value_pearson = stats.pearsonr(data['temp_max'], data['temp_min'])
print(f"Коефіцієнт кореляції Пірсона (temp_max та temp_min): {correlation:.3f}")

# перевірка на нормальність
stat, p_value_shapiro = stats.shapiro(data[column_name])
print(f"p-value для тесту Шапіро-Уїлка: {p_value_shapiro:.5f}")

alpha = 0.05
if p_value_shapiro > alpha:
    print('Висновок: Розподіл нормальний (не відхиляємо нульову гіпотезу)')
else:
    print('Висновок: Розподіл відрізняється від нормального (відхиляємо нульову гіпотезу)')