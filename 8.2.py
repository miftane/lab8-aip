# 8.2.py
points = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}

letter_ustal_value = {}
for value_ya_ustal, letters in points.items():
    for letter in letters:
        letter_ustal_value[letter] = value_ya_ustal

word = input("Введите слово (заглавными буквами): ").upper()
total = 0

for letter in word:
    if letter in letter_ustal_value:
        total += letter_ustal_value[letter]

print(f"Стоимость слова '{word}': {total} очков")
