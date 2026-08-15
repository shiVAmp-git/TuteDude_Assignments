import pandas as pd
students = {'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
            'Marks':[78,85,90,66,72],
            'Subject':['Math','Math','Science','Science','Math']}
students = pd.DataFrame(students)
print("Info: ",students.info())
print("Describe: ",students.describe())
print("Head: ",students.head())
print("Tail: ",students.tail())
print("Sorted Values: \n",students.sort_values('Marks' , ascending=False))
print("Unsorted Values: \n",students.sort_index())