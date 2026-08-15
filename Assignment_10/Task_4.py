import pandas as pd
students = {'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
            'Marks':[78,85,90,66,72],
            'Subject':['Math','Math','Science','Science','Math']}
students = pd.DataFrame(students)
print("First 3 rows: \n",students.iloc[0:3])
print("Last 2 rows: \n",students.iloc[3:])
print("Shape of dataframe: ",students.shape)
print("Columns of dataframe: ",students.columns)