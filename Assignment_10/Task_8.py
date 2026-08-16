import matplotlib.pyplot as plt
import pandas as pd
students = {'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
            'Marks':[78,85,90,66,72],
            'Subject':['Math','Math','Science','Science','Math']}
students = pd.DataFrame(students)
students.plot(x='Name',y='Marks',kind='bar')
students.plot(x='Name',y='Marks',kind='line')
students.plot(x='Name',y='Marks',kind='hist')
