group1 = {"Anna", "Ivan", "Olha"}
group2 = {"Ivan", "Maksym", "Olha"}
print("Спільні для обох груп:", group1 & group2)
print("Тільки група 1:", group1 - group2)
print("Тільки група 2:", group2 - group1)
print("Всі:", group1 | group2)