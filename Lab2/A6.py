total_seconds = int(input("Введите секунды: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print("{}:{:02d}:{:02d}".format(hours, minutes, seconds))