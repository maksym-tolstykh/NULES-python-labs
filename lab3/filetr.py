import os
from testModul.deeptr import TransLate as deeptr_TransLate, LangDetect as deeptr_LangDetect, CodeLang as deeptr_CodeLang, LanguageList as deeptr_LanguageList
from testModul.gtrans import TransLate as gtrans_TransLate, LangDetect as gtrans_LangDetect, CodeLang as gtrans_CodeLang, LanguageList as gtrans_LanguageList




def load_config(config_file: str) -> dict:
    config = {}
    try:
        if not os.path.exists(config_file):
            print(f"Файл конфігурації {config_file} не знайдено.")
            return config
        
        with open(config_file, 'r', encoding='utf-8') as file:
            text = file.read().strip().split('\n')
          
            for line in text:
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()
                print(f"Завантажено: {key.strip()} = {value.strip()}")
                
    except FileNotFoundError:
        print(f"Файл конфігурації {config_file} не знайдено.")
    except Exception as e:
        print(f"Помилка завантаження конфігурації: {str(e)}")
    return config

def read_file_with_limits(file_path: str, config: dict):
    max_chars = int(config.get('max_chars', 0))
    max_words = int(config.get('max_words', 0))
    max_sentences = int(config.get('max_sentences', 0))
    
    char_count = 0
    word_count = 0
    sentence_count = 0
    result_text = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                sentences = line.split('.')
                
                char_count += len(line)
                word_count += len(words)
                sentence_count += len(sentences) - 1
                
                result_text.append(line.strip())
                
                if max_chars and char_count > max_chars:
                    print("Досягнуто ліміту символів")
                    break
                if max_words and word_count > max_words:
                    print("Досягнуто ліміту слів")
                    break
                if max_sentences and sentence_count > max_sentences:
                    print("Досягнуто ліміту речень")
                    break
    
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    
    return '\n'.join(result_text)

print("***Завдання 1")
# Завантажуємо конфігурацію
config = load_config(os.path.join(os.path.dirname(__file__), 'config.txt'))
print("***Завдання 2")
# Читаємо файл із заданими лімітами
text = read_file_with_limits(os.path.join(os.path.dirname(__file__), 'text.txt'), config)

print("***Завдання 3")
# Визначаємо мову тексту
detected_lang = gtrans_LangDetect(text)
print(f"Визначена мова: {detected_lang}")
# Отримуємо цільову мову з конфігурації
target_lang = config.get('dest_lang')
print(f"Мова з конфігу:{target_lang}")

# Перекладаємо текст на цільову мову
translated_text = gtrans_TransLate(text, src=detected_lang, dest=target_lang)
# print(f"Перекладений текст:\n{translated_text}")

# Перевіряємо параметр `output` і виводимо відповідно до конфігурації
output = config.get('output')  # Отримуємо значення параметра output

if output is None:
    print("Параметр 'output' не знайдено в конфігурації. Встановіть його в конфігураційному файлі.")
else:
    if output == 'screen':
        print(f"Перекладено на мову: {gtrans_CodeLang(target_lang)}")
        print(f"Перекладений текст:\n{translated_text}")
    elif output == 'file':
        output_file = f'translated_text_{target_lang}.txt'  # Ім'я файлу для збереження перекладеного тексту
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(f"Перекладено на мову: {gtrans_CodeLang(target_lang)}\n")
                file.write(f"Перекладений текст:\n{translated_text}\n")
            print(f"Перекладений текст збережено у файл: {output_file}")
        except Exception as e:
            print(f"Помилка запису у файл: {str(e)}")
    else:
        print("Невідомий параметр 'output'. Підтримуються тільки 'screen' і 'file'.")

# Використання функцій з deeptr.py
detected_lang2 = deeptr_LangDetect(text)
# translated_text = deeptr_TransLate(text, src='uk', dest='en')
lang_list= deeptr_LanguageList('screen', "Добрий день")

print(f"Detected Language: {detected_lang2}")
print(lang_list)
# print(f"Translated Text: {translated_text}")