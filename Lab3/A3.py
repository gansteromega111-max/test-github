def main():
  try:
    prev_reading = int(input("Предыдущее: "))
    curr_reading = int(input("Текущее: "))
    if curr_reading >= prev_reading:
      consumed = curr_reading - prev_reading
    else:
      consumed = (10000 - prev_reading) + curr_reading
    cost = 0.0
    if consumed <= 300:
      cost = 21.0
    elif consumed <= 600:
      cost = 21.0 + (consumed - 300) * 0.06
    elif consumed <= 800:
      cost = 21.0 + 300 * 0.06 + (consumed - 600) * 0.04
    else:
      cost = 21.0 + 300 * 0.06 + 200 * 0.04 + (consumed - 800) * 0.025
    avg_price = cost / consumed if consumed > 0 else 0.0
    print("Предыдущее", prev_reading)
    print("Текущее", curr_reading)
    print("Использовано", consumed)
    print(f"К оплате\n{cost:.2f}")
    print(f"Ср. цена т^3\n{avg_price:.2f}")
  except ValueError:
    print("Ошибка ввода")
if __name__ == "__main__":
  main()