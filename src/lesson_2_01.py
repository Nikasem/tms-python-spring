# #Задание 2.01
# Создать переменные firstname, lastname, age с соответствующими значениями
# Путем сложения получить строку видаПривет, меня зовут Иван Иванов, мне 35 лет
# Примечание:Переменную age задавать как строку ‘35’
firstname = "Никита"
lastname = " Семячко"
age = "26"
i = "Привет, меня  зовут " + firstname + lastname +  ", " + "мне " + age + " лет"
print(i)
print(len(i))
print(age.isdigit())
print(i.isdigit())
print(i.find("меня"))
print(firstname[3:])
k = "Hello world"
print(k[0:7:3])
print(lastname[0: 5:2])
l ="My " "{} {} {}".format("Hello","Sweet", "World" )
print(l)
