
# Statistik Dasar untuk AI Engineer

## Latihan 1: Measure of Central Tendency
```python
import numpy as np
from scipy import stats

data = [12, 15, 13, 20, 18, 17, 16, 14, 22]

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=True).mode[0])
```

---

## Latihan 2: Measure of Spread
```python
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
```

---

## Latihan 3: Visualisasi Distribusi
```python
import matplotlib.pyplot as plt

plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title("Distribusi Data")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.grid(True)
plt.show()
```

---

## Latihan 4: Korelasi Antar Variabel
```python
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]  # Korelasi negatif

corr = np.corrcoef(x, y)[0, 1]
print("Korelasi Pearson x dan y:", corr)
```
