import numpy as np
sales = np.array([1200,1500,900,2000,1800,1700,1600])
print("Total Weekly sales: ",np.sum(sales))
print("Average Daily sales: ",np.average(sales))
print("Highest sales day: ")
max_sale = np.max(sales)
max_index = np.where(sales == max_sale)[0][0]
print(f"it is on day {max_index+1}")
print("Lwowest sales day: ")
min_sale = np.min(sales)
min_index = np.where(sales == min_sale)[0][0]
print(f"it is on day {min_index+1}")
print("Standard deviation of sales: ",np.std(sales))
index = []
avg_sale = np.average(sales)
for i,sale in enumerate(sales):
    if sale > avg_sale:
        index.append(i+1)
days = ", ".join(map(str, index))
print(f"Days with above-average sales: {days}")