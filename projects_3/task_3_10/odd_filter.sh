#!/bin/bash

#Вывод на экран чётных чисел
for i in {1..20}; do
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi

echo "$i"

#Остановка работы после 15
    if (( i==15 )); then
       echo "Цикл дошёл до 15"
       break
    fi

done
