cat > task_3-14_score.sh << 'EOF'
#!/bin/bash
echo "=== Задание 2: Фильтрация по оценкам ==="
echo "1. Студенты с оценкой выше 80:"
awk '$2 > 80 {print $0}' students.txt

echo -e "\n2. Студенты с оценкой ниже 70:"
awk '$2 < 70 {print $0}' students.txt

echo -e "\n3. Только первая строка файла:"
awk 'NR==1 {print $0}' students.txt
EOF