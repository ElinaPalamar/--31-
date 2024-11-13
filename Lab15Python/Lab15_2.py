import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'])

df_2014 = df[df['Date'].dt.year == 2014]
df_2014['Month'] = df_2014['Date'].dt.month

# Розрахунок сумарних даних по місяцях
monthly_data = df_2014.drop(columns=['Date']).sum(axis=1).groupby(df_2014['Month']).sum()

# Знаходження найбільш популярного місяця
most_popular_month = monthly_data.idxmax()
month_names = {1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 5: 'Травень',
               6: 'Червень', 7: 'Липень', 8: 'Серпень', 9: 'Вересень', 10: 'Жовтень',
               11: 'Листопад', 12: 'Грудень'}
most_popular_month_name = month_names[most_popular_month]

print(f"Найбільш популярний місяць: {most_popular_month_name}")

plt.figure(figsize=(10, 6))
monthly_data.plot(kind='bar', color='skyblue')
plt.title('Використання велодоріжок у 2014 році')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=0)
plt.show()
