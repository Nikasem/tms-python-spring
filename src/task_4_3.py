# 3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()(подсказка: создается новый ключ
# с цифрой в конце, старый удаляется)
dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_keys = list(dict.keys())
for key in list_keys:
    key_new = key + str(len(key))
    dict[key_new] = dict.pop(key)
print(dict)

dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_1_keys = list(dict_1.keys())
list_1_values = list(dict_1.values())
dict_1.clear()
i = 0
while i < len(list_1_keys):
    keys_new = list_1_keys[i] + str(len(list_1_keys[i]))
    dict_1.update({keys_new: list_1_values[i]})
    i += 1
print(dict_1)