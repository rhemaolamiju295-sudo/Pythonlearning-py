from deep_translator import GoogleTranslator

text = input("Enter text: ")

translation = GoogleTranslator(
    source="auto",
    target="fr"
).translate(text)

print("Translation:", translation)