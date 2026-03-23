import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


data_1 = np.array([10, 12, 15, 14, 10, 20, 25, 18, 22, 17, 19, 21, 13, 14, 16])

mean_1 = np.mean(data_1)
median_1 = np.median(data_1)
variance_1 = np.var(data_1, ddof=1)
n = len(data_1)

confidence = 0.95
t_value = stats.t.ppf((1 + confidence) / 2, n - 1)
margin_error = t_value * (np.sqrt(variance_1) / np.sqrt(n))
ci_mean = (mean_1 - margin_error, mean_1 + margin_error)

chi2_lower = stats.chi2.ppf((1 - confidence) / 2, n - 1)
chi2_upper = stats.chi2.ppf((1 + confidence) / 2, n - 1)
ci_variance = ((n - 1) * variance_1 / chi2_upper, (n - 1) * variance_1 / chi2_lower)

print("--- ЗАВДАННЯ 1 ---")
print(f"Середнє: {mean_1:.2f}")
print(f"Медіана: {median_1:.2f}")
print(f"Дисперсія: {variance_1:.2f}")
print(f"Довірчий інтервал (середнє): від {ci_mean[0]:.2f} до {ci_mean[1]:.2f}")
print(f"Довірчий інтервал (дисперсія): від {ci_variance[0]:.2f} до {ci_variance[1]:.2f}\n")

plt.figure(figsize=(8, 4))
plt.hist(data_1, bins=7, color='skyblue', edgecolor='black')
plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Гістограма вибірки (Завдання 1)')
plt.show()

group_a = np.array([85, 92, 78, 81, 89, 85, 91, 77, 84, 88])
group_b = np.array([79, 82, 85, 88, 75, 83, 90, 80, 87, 84])

mean_a, mean_b = np.mean(group_a), np.mean(group_b)
var_a, var_b = np.var(group_a, ddof=1), np.var(group_b, ddof=1)
std_a, std_b = np.std(group_a, ddof=1), np.std(group_b, ddof=1)

t_stat, p_value = stats.ttest_ind(group_a, group_b)

print("--- ЗАВДАННЯ 2 ---")
print(f"Група А -> Середнє: {mean_a:.2f}, Дисперсія: {var_a:.2f}, Відхилення: {std_a:.2f}")
print(f"Група В -> Середнє: {mean_b:.2f}, Дисперсія: {var_b:.2f}, Відхилення: {std_b:.2f}")
print(f"p-value для порівняння: {p_value:.3f}")

plt.figure(figsize=(8, 4))
plt.hist([group_a, group_b], bins=5, color=['blue', 'orange'], label=['Група А', 'Група В'], edgecolor='black')
plt.xlabel('Бали')
plt.ylabel('Кількість студентів')
plt.title('Розподіл балів: Група А vs Група В')
plt.legend()
plt.show()