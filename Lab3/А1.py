def get_quarter(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"
    return None
def main():
    try:
        x1 = float(input("Введите x1: "))
        y1 = float(input("Введите y1: "))
        x2 = float(input("Введите x2: "))
        y2 = float(input("Введите y2: "))

        q1 = get_quarter(x1, y1)
        q2 = get_quarter(x2, y2)

        if q1 and q2 and q1 == q2:
            print(f"Yes, {q1}")
        else:
            print("No")
    except ValueError:
        print("Ошибка ввода")
if __name__ == "__main__":
    main()