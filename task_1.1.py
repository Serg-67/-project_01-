# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# W a s t e   a   M o m e n t   S t a y i n g  \  A l i v e  A  S o r t a  F a i r y t a l e   S t a r t  M e  U p   N e w  S a l v a t i o n  
# 0 1 2 3 4 5 6 7 8 9
print(len(my_favorite_songs))                                                                                                                                    

my_favorite_songs[:13]
my_favorite_songs[-13:]
my_favorite_songs[15:30]
my_favorite_songs[50:62]
print(my_favorite_songs[:13], my_favorite_songs[-13:], my_favorite_songs[15:30], my_favorite_songs[50:62])
