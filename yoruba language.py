# English to Yoruba dictionary (20 words)
yoruba = {
    "hello": "pẹ̀lẹ́",
    "goodbye": "ọ̀dàbọ̀",
    "thank you": "ẹ ṣé",
    "yes": "bẹ́ẹ̀ni",
    "no": "rárá",
    "man": "ọkùnrin",
    "woman": "obìnrin",
    "child": "ọmọ",
    "food": "oúnjẹ",
    "water": "omi",
    "house": "ilé",
    "school": "ilé-ẹ̀kọ́",
    "book": "ìwé",
    "money": "owó",
    "love": "ìfẹ́",
    "friend": "ọ̀rẹ́",
    "morning": "àárọ̀",
    "night": "alẹ́",
    "work": "iṣẹ́",
    "God": "Ọlọ́run"
}

print("Choose a language:")
print("1. Yoruba")

choice = input("Enter 1 : ")

word = input("Enter an English word: ").lower()

if choice == "1":
    if word in yoruba:
        print("Yoruba translation:", yoruba[word])
    else:
        print("Word not found in Yoruba dictionary.")

else:
    print("Invalid choice.")