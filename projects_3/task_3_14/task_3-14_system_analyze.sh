cat > task_3-14_system_analyze.sh << 'EOF'
#!/bin/bash
echo "=== Задание 5: Анализ дискового пространства (df -h) ==="
echo "Файловая система и процент заполнения:"
df -h | awk 'NR>1 {
    printf "%-20s %s\n", $1, $5
    # Убираем символ % для сравнения
    usage = $5
    gsub(/%/, "", usage)
    if (usage > 90) {
        print "  ⚠️  ПРЕДУПРЕЖДЕНИЕ: Заполнено более 90%!"
    }
}'
EOF