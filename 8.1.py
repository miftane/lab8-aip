# 8.1.py
countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Испания": "Мадрид",
    "Япония": "Токио",
    "Китай": "Пекин"
}

print("Все страны и столицы:")
for country, capital in countries.items():
    print(f"{country} - {capital}")

country_name = input("\nВведите название страны: ")
if country_name in countries:
    print(f"Столица {country_name}: {countries[country_name]}")
else:
    print("Страна не найдена")

print("\nСтраны в алфавитном порядке:")
for country in sorted(countries.keys()):
    print(f"{country} - {countries[country]}")
