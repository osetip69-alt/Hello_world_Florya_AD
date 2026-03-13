cat > task_3-14_students.sh << 'EOF'
#!/bin/bash
echo "=== Задание 1: students.txt ==="
echo "1. Только имена студентов:"
awk '{print $1}' students.txt

echo -e "\n2. Только оценки:"
awk '{print $2}' students.txt

echo -e "\n3. Номер строки и имя:"
awk '{print NR, $1}' students.txt
EOF