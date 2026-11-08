def draw_rectangle(rows, columns, char):
    print(f"\nПРЯМОУГОЛЬНИК {rows}x{columns}:")
    for i in range(rows):
        for j in range(columns):
            print(char, end="")
        print()
def draw_frame(rows, columns, char):
    print(f"\nРАМКА {rows}x{columns}:")
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(char, end="")
            else:
                print(" ", end="")
        print()
def draw_right_triangle(rows, char):
    print(f"\nПРАВЫЙ ТРЕУГОЛЬНИК (высота {rows}):")
    for i in range(1, rows + 1):
        for j in range(i):
            print(char, end="")
        print()
if __name__ == "__main__":
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))
    ch = input("Введите символ для отрисовки: ")
    draw_rectangle(n, m, ch)
    draw_frame(n, m, ch)
    draw_right_triangle(n, ch)