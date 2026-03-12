print("🧪 ПРИЁМКА ЛАБОРАТОРНЫХ РЕАКТИВОВ 🧪")
print("=" * 50)

name = input("Наименование реактива: ")
cas = input("CAS номер: ")
grade = input("Квалификация (осч/хч/чда/тех): ")
quantity = int(input("Количество (единиц): "))
package = input("Тип упаковки (флакон/канистра/мешок): ")
volume = input("Объём/масса: ")
manufacturer = input("Производитель: ")
lot = input("Номер партии: ")
expiry = input("Срок годности: ")
condition = input("Состояние упаковки (норма/повреждена): ")
location = input("Место хранения: ")
received_by = input("Принял (ФИО): ")

print("\n" + "=" * 60)
print("АКТ ПРИЁМКИ РЕАКТИВА")
print("=" * 60)

print(f"Наименование:    {name}")
print(f"CAS:             {cas}")
print(f"Квалификация:    {grade}")
print(f"Партия:          {lot}")
print(f"Производитель:   {manufacturer}")
print(f"Фасовка:         {quantity} x {package} ({volume})")
print(f"Годен до:        {expiry}")
print(f"Состояние:       {condition}")
print(f"Место:           {location}")
print(f"Принял:          {received_by}")
print(f"Дата:            25.02.2026")

print("=" * 60)

report = f"""
============================================================
               АКТ ПРИЁМКИ РЕАКТИВА
============================================================
Наименование:    {name}
CAS:             {cas}
Квалификация:    {grade}
Партия:          {lot}
Производитель:   {manufacturer}
Фасовка:         {quantity} x {package} ({volume})
Годен до:        {expiry}
Состояние:       {condition}
Место:           {location}
Принял:          {received_by}
Дата:            25.02.2026
============================================================
"""

with open("inventory.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("✅ Акт сохранён в inventory.txt")