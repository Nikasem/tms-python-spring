"""2) Дано число. Найти сумму и произведение его цифр."""
n = int(input("Введите число:"))
s = 0
m = 1
while n > 0:
    s += n % 10
    m *= n % 10
    n = n // 10
print("Сумма:", s)
print("Произведение:", m)