def analyze_packets():
    packets = input("Введите последовательность пакетов (только 0 и 1, мин. длина 5): ")
    if len(packets) < 5 or not all(char in '01' for char in packets):
        print("Неверный ввод. Убедитесь, что длина строки не менее 5 и используются только символы 0 и 1.")
        return
    total_packets = len(packets)
    lost_packets = packets.count('0')
    max_lost_streak = 0
    current_streak = 0
    for packet in packets:
        if packet == '0':
            current_streak += 1
            if current_streak > max_lost_streak:
                max_lost_streak = current_streak
        else:
            current_streak = 0
    loss_percentage = (lost_packets / total_packets) * 100
    if loss_percentage <= 1:
        quality = "Отличное качество"
    elif loss_percentage <= 5:
        quality = "Хорошее качество"
    elif loss_percentage <= 10:
        quality = "Удовлетворительное качество"
    elif loss_percentage <= 20:
        quality = "Плохое качество"
    else:
        quality = "Критическое состояние сети"
    print("\nВывод:")
    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_lost_streak}")
    print(f"Процент потерь: {loss_percentage:.1f}%")
    print(f"Качество связи: {quality}")
if __name__ == "__main__":
    analyze_packets()