#!/bin/bash

check_root() {
    if [ $EUID -ne 0 ]; then
        echo "Ошибка!!! Зайдите от имени суперпользователя!"
        exit 1
    fi
]

check_root

echo "Скрипт запущен"
