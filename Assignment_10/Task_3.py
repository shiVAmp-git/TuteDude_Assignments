import pandas as pd
sr = pd.Series([78,85,90,66,72])
print("maximum marks: ",sr.max())
print("minimum marks: ",sr.min())
print("sum of marks: ",sr.sum())
print("mean of marks: ",sr.mean())
result = lambda mark:1 if mark>70 else 0
result_list = pd.Series(map(result,sr))
print("passed_students",result_list.sum())
