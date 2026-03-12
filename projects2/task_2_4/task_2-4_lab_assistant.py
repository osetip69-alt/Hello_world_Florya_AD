volume = float(input("Введите нужный объем раствора (мл): "))

salt_mass = volume * 0.009

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем:\t{volume:.2f} мл\n")
    file.write(f"Масса соли:\t{salt_mass:.2f} г\n")
    file.write(f"Объем воды:\t{volume:.2f} мл\n")

print("Рецепт успешно сохранен в файл recipe.txt")
