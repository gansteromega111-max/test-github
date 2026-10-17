spisok = ['123e', '91.4', '42', -12.12]
for item in spisok:
    try:
        res = int(item)
        print("Успех:", item, "->", res)
    except:
        print("Ошибка для:", item)