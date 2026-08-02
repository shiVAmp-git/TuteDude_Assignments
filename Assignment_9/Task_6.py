import numpy as np 
marks = np.array([78,85,90,66,72,88,95,60])
marks.sort()
print("Sorted Array of marks: ",marks)
print("25th percentile: ",np.percentile(marks,25))
print("50th percentile: ",np.percentile(marks,50))
print("75th percentile: ",np.percentile(marks,75))
print(np.average(marks))
count = 0
avg_mark = np.average(marks)
for mark in marks:
    if mark > avg_mark:
        count += 1
print(f"from this {count} student got above average marks")