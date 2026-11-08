import math
input_filename = input("Введите имя файла с данными (например, 1.WCData.txt): ")
output_filename = "WindChillReport.txt"
file = open(input_filename, "r", encoding="utf-8")
lines = file.readlines()
file.close()
output_file = open(output_filename, "w", encoding="utf-8")
output_file.write("Time        | WC temp     | WC Effect\n")
total_wc_temp = 0
count = 0
for line in lines:
    parts = line.replace("|", " ").split()
    if len(parts) >= 3:
        if parts[0] == "Time" or parts[0] == "02:15:00" and count == 0:
            pass
        if ":" in parts[0]:
            time_str = parts[0]
            temp_f = float(parts[1])
            wind_v = float(parts[2])
            wc_temp = 35.74 + 0.6125 * temp_f + (0.4275 * temp_f - 35.75) * (wind_v ** 0.16)
            wc_effect = wc_temp - temp_f
            total_wc_temp += wc_temp
            count += 1
            output_file.write("{:<11} | {:<11.1f} | {:.1f}\n".format(time_str, wc_temp, wc_effect))
if count > 0:
    average_wc = total_wc_temp / count
    output_file.write("\nThe average adjusted temperature, based on {} observations, was {:.1f}\n".format(count, average_wc))
else:
    output_file.write("\nNo observations found.\n")
output_file.close()
print("Готово! Отчет записан в файл:", output_filename)