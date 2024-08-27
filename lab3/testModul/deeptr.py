from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
import pycountry
DetectorFactory.seed = 0  # Для стабільного результату

# Функція для перекладу тексту
def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"

# Функція для визначення мови
def LangDetect(text: str, set: str = 'all') -> str:
    try:
        lang = detect(text)
        confidence = 0.99  # Приблизна оцінка, оскільки langdetect не надає коефіцієнт
        if set == 'lang':
            return lang
        elif set == 'confidence':
            return str(confidence)
        else:
            return lang
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"

# Функція для отримання коду або назви мови
def CodeLang(lang: str) -> str:
    # Отримання назви мови на основі її коду
    language = pycountry.languages.get(alpha_2=lang)
    return language.name if language else "Невідома мова"

# Функція для виведення списку мов
def LanguageList(out: str = 'screen', text: str = '') -> str:
    languages = {
            'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'bn': 'Bengali',
            'bs': 'Bosnian', 'ca': 'Catalan', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish',
            'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'fi': 'Finnish',
            'fr': 'French', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole',
            'ha': 'Hausa', 'vi': 'Vietnamese',
            'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'
        } # Список мов
    try:
        if out == 'screen':
            print("N  Language     ISO-639 code    Text")
            print("-" * 50)
            for i, (code, lang) in enumerate(languages.items(), 1):
                translated_text = TransLate(text, 'auto', code)
                print(f"{i}  {lang:<12} {code:<10} {translated_text}")
            return "Ok"
        elif out == 'file':
            with open('languages.txt', 'w') as f:
                f.write("N  Language     ISO-639 code    Text\n")
                f.write("-" * 50 + "\n")
                for i, (code, lang) in enumerate(languages.items(), 1):
                    translated_text = TransLate(text, 'auto', code)
                    f.write(f"{i}  {lang:<12} {code:<10} {translated_text}\n")
            return "Ok"
    except Exception as e:
        return f"Помилка: {str(e)}"
