# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
cqlquery = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY,
Student_Name TEXT NOT NULL,
School_id INTEGER NOT NULL
);"""
cursor.execute(cqlquery)
connection.commit()
connection.close()

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
cqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_id)
VALUES
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);"""
cursor.execute(cqlquery)
connection.commit()
connection.close()


import sqlite3
import pandas as pd

connection = sqlite3.connect("teachers.db")
query = "SELECT * FROM Students"
df = pd.read_sql(query,connection)
print(df)

df.to_excel('teachers.xlsx', index = False)


import sqlite3

def get_student(student_id):
  connection = sqlite3.connect("teachers.db")
  cursor = connection.cursor()
  query = "SELECT * FROM School JOIN Students ON School.School_id = Students.School_id WHERE Students.Student_id = ?"
  cursor.execute(query,(student_id,))
  records = cursor.fetchall()
  print(records)
  for rom in records:
    print()

x = int(input("Введи ID:"))

get_student(x)