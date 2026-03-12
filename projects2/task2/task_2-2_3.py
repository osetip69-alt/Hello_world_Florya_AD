print("🔬 СИСТЕМА УЧЁТА ЛАБОРАТОРНОГО ОБОРУДОВАНИЯ 🔬")
print("=" * 70)

device_name = input("Название прибора: ")
inventory_number = input("Инвентарный номер: ")
manufacturer = input("Производитель: ")
model = input("Модель: ")
year = input("Год выпуска: ")

while True:
    status_input = input("Состояние (работает/ремонт/списан): ").lower()
    if status_input in ["работает", "ремонт", "списан"]:
        device_status = status_input
        break
    else:
        print("Введите: работает, ремонт или списан")

while True:
    calibration_input = input("Требуется калибровка? (да/нет): ").lower()
    if calibration_input in ["да", "нет"]:
        needs_calibration = "Да" if calibration_input == "да" else "Нет"
        break
    else:
        print("Введите да или нет")

quantity = int(input("Количество: "))
last_maintenance = input("Дата последнего ТО (ДД.ММ.ГГГГ): ")

print("\n" * 2)
print("📊 ПАСПОРТ ОБОРУДОВАНИЯ 📊")
print("=" * 90)

print(f"🔹 Название:          {device_name}")
print(f"🔹 Инв. номер:        {inventory_number}")
print(f"🔹 Производитель:     {manufacturer}")
print(f"🔹 Модель:            {model}")
print(f"🔹 Год выпуска:       {year}")
print(f"🔹 Состояние:         {device_status}")
print(f"🔹 Калибровка:        {needs_calibration}")
print(f"🔹 Количество:        {quantity} шт.")
print(f"🔹 Последнее ТО:      {last_maintenance}")

print("=" * 90)

if device_status == "работает" and needs_calibration == "Нет":
    print("✅ Прибор готов к работе")
elif device_status == "работает" and needs_calibration == "Да":
    print("⚠️ Требуется калибровка перед использованием")
elif device_status == "ремонт":
    print("🔧 Прибор в ремонте")
else:
    print("❌ Прибор списан")