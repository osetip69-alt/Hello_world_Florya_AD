#!/bin/bash

for i in {1..10}; do
   touch "test$i.txt"
   echo "Создал файл test$i.txt"
done

for j in {10..1..1}; do
    while [ -e "test$j.txt" ]; do
    rm "test$j.txt"
    echo "Удалил файл test$j.txt"
    done
done

echo "Все файлы удалены"
