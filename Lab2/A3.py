import sys
bytes_from_task = 1921000
megabytes = bytes_from_task / 1024 / 1024
print("Результат перевода из условия:")
print("Мегабайты:", round(megabytes, 2))
huge_number = 3 ** 9090001
real_bytes = sys.getsizeof(huge_number)
real_mb = real_bytes / 1024 / 1024
print("Реальный размер числа в памяти (байты):", real_bytes)
print("Реальный размер числа в памяти (мегабайты):", round(real_mb, 2))