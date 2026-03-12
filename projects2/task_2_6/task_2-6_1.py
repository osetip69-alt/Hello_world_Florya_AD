pH = float(input("Введите значение pH: "))

if pH < 7.0:
    print("Кислая среда")
elif pH == 7.0:
    print("Нейтральная среда")
else:
    print("Щелочная среда")