#English to Igbo Dictionary

english_to_igbo = {
    "water": "mmiri",
    "fire": "oku",
    "house": "ulo",
    "food": "nri",
    "child": "nwa",
    "man": "nwoke",
    "woman": "nwanyi",
    "book": "akwukwo",
    "sun": "anyanwu",
    "moon": "onwa",
    "God": "chukwu",
    "road": "uzo",
    "friend": "Enyi",
    "tree": "osisi",
    "rain": "Okpo mmiri",
    "market": "ahia",
    "body": "ahu",
    "head": "isi",
    "hand": "aka",
    "love": "ihunanya"
}

#Search loop
while True:
    word = input("\nEnter and English word (or 'exit' to quit): "). lower()

    if word == "exit":
        print("Goodbye!")
        break

    if word in english_to_igbo:
        print(f"Igbo: {english_to_igbo[word]}")

    else:
        print("Word not found!")