print("=== Анализ последовательности ДНК ===\n")

dna = input("Введите последовательность ДНК: ").upper()

print(f"\nПоследовательность в верхнем регистре: {dna}\n")

count_a = dna.count('A')
count_t = dna.count('T')
count_g = dna.count('G')
count_c = dna.count('C')
total_length = len(dna)

print("Подсчёт нуклеотидов:")
print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"G: {count_g}")
print(f"C: {count_c}")

print(f"\nОбщая длина: {total_length} нуклеотидов")

if total_length > 0:
    print(f"\nПроцентное содержание:")
    print(f"A: {(count_a/total_length*100):.1f}%")
    print(f"T: {(count_t/total_length*100):.1f}%")
    print(f"G: {(count_g/total_length*100):.1f}%")
    print(f"C: {(count_c/total_length*100):.1f}%")
