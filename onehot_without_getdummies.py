# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит 
# всего из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


# Для перевода этого DataFrame в one hot формат без использования функции get_dummies 
# я использую методы pandas для создания новых столбцов, представляющих каждое 
# уникальное значение в столбце 'whoAmI' в виде бинарных флагов.

# В данном случае использован цикл for для итерации по уникальным значениям в столбце 
# и создания новых столбцов с бинарными значениями для каждого уникального значения. 
# Затем заполнили эти столбцы соответствующими бинарными значениями 
# в зависимости от того, совпадает ли значение в исходном столбце с 
# текущим уникальным значением или нет.

# Получаем таблицу, которая представляет собой двумерную структуру данных, 
# где строки и столбцы формируют сетку. В данном случае, у нас есть два столбца: 
# "human" и "robot", а каждая строка представляет собой отдельное наблюдение или объект.
# В каждой строке таблицы представлено одно наблюдение.
# В столбцах "human" и "robot" используется бинарное представление (one hot encoding), 
# где 1 обозначает присутствие соответствующей категории, а 0 - отсутствие.

import pandas as pd

# Генерируем исходные данные
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Создаем словарь, содержащий уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Для каждого уникального значения создаем новый столбец и заполняем его бинарными флагами
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец 'whoAmI'
data.drop('whoAmI', axis=1, inplace=True)

# Выводим результат
print(data.head())
