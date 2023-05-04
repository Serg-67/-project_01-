# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

# def quarter_of(month):
    # pass
def quarter_of(month):
    if  month != 12:
     if  month > 1 and month < 4:
        return("1 quarter_of")
      
    if  month > 3 and month < 7:
         return("2 quarter_of")
       
    if  month > 6 and month < 9:
         return("3 quarter_of")
       
    if  month > 9 and month < 12:
         return("4 quarter_of")
    
if __name__ == '__main__':
     month=int(input('Введите номер месяца: '))
print(quarter_of(month))