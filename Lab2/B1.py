filename = input("Введите имя файла с картой (например, inmap0.dat): ")
file = open(filename, "r", encoding="utf-8")
lines = file.readlines()
file.close()
first_line = lines[0].split()
num_locations = int(first_line[0])
scale = float(first_line[1])
print("Даниель Якимчик")
print("Simple Map Distance Computations")
print("Map Scale Factor: {:.2f} miles per inch".format(scale))
print("{:<8} | {:<10} | {:<10}".format("Map", "Mileage", "Measure"))
print("{:<8} | {:<10} | {:<10}".format("#", "Distance", "Distance"))
total_distance = 0
for i in range(1, num_locations + 1):
    inches = float(lines[i])
    miles = inches * scale
    total_distance += miles
    print("{:<8} | {:<10.1f} | {:<10.1f}".format(i, inches, miles))
print("Total Distance: {:.1f} miles".format(total_distance))