import matplotlib.pyplot as plt
import pandas as pd
sales = {
    'Day':['Mon','Tue','Wed','Thu','Fri'],
    'Revenue':[1200,1500,900,2000,1800]
}
sales = pd.DataFrame(sales)
print("Total Revenue: ",sales['Revenue'].sum())
print("Average Daily Revenue: ",sales['Revenue'].mean())
print("Highest Revenue Day: \n",sales[sales['Revenue']==sales['Revenue'].max()])
print("Day where sales are above average: \n",sales[sales['Revenue']>sales['Revenue'].mean()])
sales.plot(x='Day',y='Revenue',kind='bar')
plt.show()