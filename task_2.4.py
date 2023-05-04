# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

marks = "Hi! Hello!"
print(len(marks))
fvar, svar = marks[3:-1], marks[:2]
new_marks = svar + fvar
print(new_marks)

# marks = "Oh, no!!!"
# print(len(marks))
# fvar, svar = marks[1:-3], marks[:1]
# new_marks = svar + fvar
# print(new_marks)




# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# def remove_last_em(s):
    # pass

# def remove(text):
#     i = 0
#     while i < 1 and text[-1]=='!':
#         text = text[:-1]
#         i+=1
#     return text
# remove("Hi!") == 'Hi!'
# True
# print(remove("Hi!"))
# print(remove("Hi!!!"))
# print(remove("!Hi"))



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# def remove_word_with_one_em(s):
    # pass

