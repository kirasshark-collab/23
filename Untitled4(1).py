group_info = ('10-ІТ', '2026/2027')
students = {
    "Anna":[ 10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9]
}
for name, grades in students.items():
    grades_str = " ".join(map(str, grades))
    print(f"{name}: {grades_str}")
print(f"{group_info[0]} — {group_info[1]}")
averages = {}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg
    print(f"{name} — {avg:.1f}")
best_student = max(averages, key=averages.get)
print(f"Найкращий результат: {best_student} — {averages[best_student]:.1f}")