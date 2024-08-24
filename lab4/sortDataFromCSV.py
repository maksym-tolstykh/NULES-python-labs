import pandas as pd

filePath = "./lab4/Employees.csv"
outputPath = './lab4/sorted_data.xlsx'

try:
    df = pd.read_csv(filePath)

    # Перетворення стовпця "Дата народження" на тип datetime
    df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%d-%m-%Y')
    today = pd.Timestamp.today()
    # Додав нову колонку ВІК, для наглядного порівняння
    df['Вік'] = (today - df['Дата народження']).dt.days // 365

    # Створення різних вікових груп
    df_all = df
    df_younger_18 = df[df['Вік'] < 18]
    df_18_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]
    df_45_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)]
    df_older_70 = df[df['Вік'] > 70]

    try:
        # Зписати дані в Excel файл
        with pd.ExcelWriter(outputPath, engine='openpyxl') as writer:
            df_all.to_excel(writer, sheet_name='all', index=False)
            df_younger_18.to_excel(writer, sheet_name='younger_18', index=False)
            df_18_45.to_excel(writer, sheet_name='18-45', index=False)
            df_45_70.to_excel(writer, sheet_name='45-70', index=False)
            df_older_70.to_excel(writer, sheet_name='older_70', index=False)

        print("Ok, файл записано")
    
    except Exception as e:
        print("Неможливо створити XLSX файл:", e)

except FileNotFoundError:
    print("Проблеми при відкритті файлу CSV.")
except pd.errors.EmptyDataError:
    print("Відсутні дані у файлі CSV.")
except pd.errors.ParserError:
    print("Помилка при обробці файлу CSV.")
except Exception as e:
    print("Непередбачувана помилка:", e)
