numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
positive = []
for number in numbers:
    if number > 0:
        positive.append(number)
print("Додатні:", positive)
negative = []
for number in numbers:
    if number < 0:
        negative.append(number)
print("Від'ємні:", negative)
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
print("Парні:", even)
div3 = []
for number in numbers:
    if number % 3 == 0:
        div3.append(number)
print("Кратні 3:", div3)
print("Мінімум:", min(numbers))
print("Максимум:", max(numbers))
print("Сума:", sum(numbers))
print("Середнє:", sum(numbers) / len(numbers))

