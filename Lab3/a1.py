x1 = float(input("Введите x1: "))
y1 = float(input("Введите y2: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
q1 = 0
if x1 > 0 and y1 > 0:
    q1 = 1
elif x1 < 0 and y1 > 0:
    q1 = 2
elif x1 < 0 and y1 < 0:
    q1 = 3
elif x1 > 0 and y1 < 0:
    q1 = 4
q2 = 0
if x2 > 0 and y2 > 0:
    q2 = 1
elif x2 < 0 and y2 > 0:
    q2 = 2
elif x2 < 0 and y2 < 0:
    q2 = 3
elif x2 > 0 and y2 < 0:
    q2 = 4
if q1 == q2:
    roman = {1: "I", 2: "II", 3: "III", 4: "IV"}
    print(f"Yes, {roman[q1]}")
else:
    print("No")