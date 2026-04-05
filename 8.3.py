# 8.3.py
students = {
    "Иванов": {"английский", "немецкий", "китайский"},
    "Петров": {"английский", "французский"},
    "Сидоров": {"испанский", "итальянский", "китайский"},
    "Кузнецов": {"английский", "японский"},
    "Смирнов": {"немецкий", "французский", "китайский"}
}

all_languages = set()
for languages in students.values():
    all_languages.update(languages)

print(f"Различные языки ({len(all_languages)} шт.): {sorted(all_languages)}")

chinese_speakers = [name for name, langs in students.items() if "китайский" in langs]
print(f"Студенты, знающие китайский язык: {', '.join(chinese_speakers)}")
