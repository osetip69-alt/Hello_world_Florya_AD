cat > task_3-14_stat.sh << 'EOF'
#!/bin/bash
echo "=== Задание 3: Статистика по оценкам ==="
echo -n "1. Сумма всех оценок: "
awk '{sum += $2} END {print sum}' students.txt

echo -n "2. Средняя оценка: "
awk '{sum += $2; count++} END {print sum/count}' students.txt

echo -n "3. Максимальная оценка: "
awk 'NR==1 {max=$2} $2 > max {max=$2} END {print max}' students.txt
EOF