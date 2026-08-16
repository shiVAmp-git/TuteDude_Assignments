import pandas as pd
students = {'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
            'Marks':[78,85,90,66,72],
            'Subject':['Math','Math','Science','Science','Math']}
students = pd.DataFrame(students)
print("Avg Marks grouped: \n",students.groupby('Subject')['Marks'].mean())
print("Avg Marks grouped: \n",students.groupby('Subject').size())
print("Avg Marks grouped: \n",students.groupby('Subject').max())
