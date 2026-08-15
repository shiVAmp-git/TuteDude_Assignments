import pandas as pd
students = {'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
            'Marks':[78,85,90,66,72],
            'Subject':['Math','Math','Science','Science','Math']}
students = pd.DataFrame(students)
print("Marks more then 75: \n",students[students['Marks']>75])
print("Marks more then 75: \n",students[students['Subject']=='Math']) 
print("Marks above AVG: \n",students[students['Marks']>students['Marks'].mean()])
print("Failed Students: \n",students[students['Marks']<70])
    