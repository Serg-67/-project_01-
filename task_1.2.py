# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
print(3.03 + 3.03 + 3.40)
# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
primes = [3.03, 3.03, 3.40]
capitals = {}
capitals['3.03'] = 'Waste a WMoment'
capitals['3.03'] = 'Out of Touch'
capitals['3.40'] = 'Staying' 'Alive'

capitals = {'Waste a WMoment', 'Out of Touch', 'Staying' 'Alive'}
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# random = ('Waste a WMoment', 'Out of Touch', 'Staying' 'Alive')
# import random
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте мод
import datetime 
n= 9.459999999999999 
time_format = str(datetime.timedelta(seconds = n)) 
print("Time in preferred format :-",time_format) 