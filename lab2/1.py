from langdetect import detect
from googletrans import Translator
import pycountry

def LangDetect(txt):
    # Виявлення мови тексту
    lang_code = detect(txt)
    return f"Виявленна мова(lang={lang_code})"  

def TransLate(txt, lang):
    # Переклад тексту
    translator = Translator()
    translated = translator.translate(txt, dest=lang)
    return translated.text

def CodeLang(lang):
    # Отримання назви мови на основі її коду
    language = pycountry.languages.get(alpha_2=lang)
    return language.name if language else "Невідома мова"

# Вхідні дані
txt = "Слава Україні!"
lang = "en"

# Виконання функцій
print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang(lang))
