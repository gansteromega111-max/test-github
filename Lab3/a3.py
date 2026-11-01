prev_val = int(input())
curr_val = int(input())
if curr_val >= prev_val:
    used = curr_val - prev_val
else:
    used = (9999 - prev_val + 1) + curr_val
cost = 0.0
if used <= 300:
    cost = 21.0
elif used <= 600:
    cost = 21.0 + (used - 300) * 0.06
elif used <= 800:
    cost = 21.0 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21.0 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
avg_price = cost / used if used > 0 else 0.0
print(f"Предыдущее\t{prev_val}")
print(f"Текущее\t\t{curr_val}")
print(f"Использовано\t{used}")
print(f"К оплате\t{cost:.2f}")
print(f"Ср. цена м^3\t{avg_price:.2f}")