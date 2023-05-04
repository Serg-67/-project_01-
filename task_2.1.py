# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!
from datetime import datetime

arr = [[4,6,2,1,9,63,-134,566], [-52, 56, 30, 29, -54, 0, -110], [42, 54, 65, 87, 0], [5]]
n = len(arr)
print(n)
print (arr)

def insertion(data):
  for i in range(n):
    print (i)
    j = i - 1
    val = arr[j]
  while arr[j] > val and j >= 0:
      data[j+1] = data[j]
      j -= 1
      data[j+1] = val
      
  return data
    
def maximum(arr):
  print("максимальные значения")
  print("Метод сортировки вставка")
  start_time = datetime.now()
  for data in arr:
    print("Максимальное значение из массива", data, insertion(data)[len(data)-1])
  end_time = datetime.now()
  print("Продолжительность: {}".format(end_time - start_time))

def minimum(arr):
  print("минимальные значения")
  print("Метод сортировки вставка")
  start_time = datetime.now()
  for data in arr:
    print("Минимальное значение из массива", data, insertion(data)[0])
  end_time = datetime.now()
  print("Продолжительность: {}".format(end_time - start_time))
  
def main():
  print(maximum(arr))
  print(minimum(arr))

print(main()) 