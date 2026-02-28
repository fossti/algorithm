import time
import matplotlib.pyplot as plt

def measure_execution_time(func, *args, **kw):
    start_time = time.time()
    result = func(*args, **kw)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    return result, execution_time
def arr(size):
    array = []
    for i in range(size):
        array.append(1)
    return array
sizes = [10, 100, 1000, 10000, 100000, 1000000, 1000000, 5000000, 10000000, 50000000]
times = []

for i in range(len(sizes)):
    array, t = measure_execution_time(arr, sizes[i])
    times.append(t)
    print(f"Элементов: {sizes[i]} | Время: {t:>12.2f} мс")
    del array

plt.figure(figsize=(10, 8))
plt.plot(sizes, times, marker='o')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (мс)')
plt.title('Зависимость времени заполнения массива от его размера')
plt.grid(True)
plt.tight_layout()
plt.show()