catalog = {
    "bread": 35,
    "milk": 48,
    "cheese": 120,
    "tea": 75
}
catalog["juice"] = 60
catalog["milk"] = 52
name = input("Введіть назву товару для пошуку: ")
price = catalog.get(name)
if price is not None:
    print(f"Ціна товару {name}: {price} грн")
else:
    print("Товар не знайдено")
low = 40
high = 100
print(f"\nТовари в ціновому діапазоні {low}–{high} грн:")
count = 0
for name, price in catalog.items():
    if low <= price <= high:
        print(f"{name} — {price} грн")
        count += 1
print(f"Кількість знайдених товарів: {count}")

