import string

def process_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Розділити текст на речення
            sentences = text.split('.')
            first_sentence = sentences[0].strip() + '.' if sentences else 'Речення не знайдено'

            # Вивести перше речення
            print(f"Перше речення: {first_sentence}")

            # Вилучити пунктуацію та розділити текст на слова
            translator = str.maketrans('', '', string.punctuation)
            words = text.translate(translator).split()
            
            # Розділити слова на українські та англійські
            ukrainian_words = [word for word in words if any('\u0400' <= char <= '\u04FF' for char in word)]
            english_words = [word for word in words if any('a' <= char.lower() <= 'z' for char in word)]
            
            # Сортувати слова
            ukrainian_words_sorted = sorted(set(ukrainian_words))
            english_words_sorted = sorted(set(english_words))

            # Вивести слова в алфавітному порядку
            print("\nУкраїнські слова в алфавітному порядку:")
            print('\n'.join(ukrainian_words_sorted))

            print("\nАнглійські слова в алфавітному порядку:")
            print('\n'.join(english_words_sorted))
            
            # Вивести кількість слів
            print(f"\nЗагальна кількість слів: {len(words)}")

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except IOError:
        print("Помилка: Не вдалося прочитати файл.")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")

# Вказати шлях до вашого текстового файлу
file_path = './lab5/text.txt'
process_text_file(file_path)
