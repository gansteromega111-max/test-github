x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
same_color = (x1 + y1 + x2 + y2) % 2 == 0
if same_color:
    print("YES")
    is_white = (x1 + y1) % 2 == 0
    print("White" if is_white else "Black")
else:
    print("NO")