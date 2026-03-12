# task_2-3_lab_journal.py

name = input("Введите ФИО исследователя: ")
date = input("Введите дату: ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write("+" + "-" * 50 + "+\n")
    file.write("| Электронный лабораторный журнал                  |\n")
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"| ФИО исследователя : {name:<32} |\n")
    file.write(f"| Дата             : {date:<32} |\n")
    file.write(f"| Эксперимент      : {experiment_name:<32} |\n")
    file.write("+" + "-" * 50 + "+\n")
    file.write("| Вывод:                                           |\n")
    
    words = conclusion.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= 48:
            if line:
                line += " " + word
            else:
                line = word
        else:
            file.write(f"| {line:<48} |\n")
            line = word
    if line:
        file.write(f"| {line:<48} |\n")
    
    file.write("+" + "-" * 50 + "+\n")

print("Данные успешно сохранены в journal.txt")