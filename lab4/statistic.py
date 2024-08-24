import pandas as pd

filePath = "./lab4/Employees.csv"
outputPath = './lab4/sorted_data.xlsx'

try:
    df = pd.read_csv(filePath)

    all_Male = len(df[df["Стать"] == "Чоловік"])
    all_Female = len(df[df["Стать"] == "Жінка"])

     # Перетворення стовпця "Дата народження" на тип datetime
    df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%d-%m-%Y')
    today = pd.Timestamp.today()
    # Додав нову колонку ВІК, для наглядного порівняння
    df['Вік'] = (today - df['Дата народження']).dt.days // 365

    df_younger_18 = len(df[df['Вік'] < 18])
    df_18_45 = len(df[(df['Вік'] >= 18) & (df['Вік'] <= 45)])
    df_45_70 = len(df[(df['Вік'] > 45) & (df['Вік'] <= 70)])
    df_older_70 = len(df[df['Вік'] > 70])

    df_younger_18f = len(df[(df['Вік'] < 18) & (df["Стать"] == "Жінка")])
    df_18_45f = len(df[(df['Вік'] >= 18) & (df['Вік'] <= 45) & (df["Стать"] == "Жінка")])
    df_45_70f = len(df[(df['Вік'] > 45) & (df['Вік'] <= 70) & (df["Стать"] == "Жінка")])
    df_older_70f = len(df[df['Вік'] > 70 & (df["Стать"] == "Жінка")] )

    df_younger_18m = len(df[(df['Вік'] < 18) & (df["Стать"] == "Чоловік")])
    df_18_45m = len(df[(df['Вік'] >= 18) & (df['Вік'] <= 45) & (df["Стать"] == "Чоловік")])
    df_45_70m = len(df[(df['Вік'] > 45) & (df['Вік'] <= 70) & (df["Стать"] == "Чоловік")])
    df_older_70m = len(df[df['Вік'] > 70 & (df["Стать"] == "Чоловік")] )

    print("Кількість співробітників чоловічої статі:",all_Male)
    print("Кількість співробітників жіночої статі:",all_Female)
    print(f"Менше 18: {df_younger_18}, 18-45 : {df_18_45}, 45-70 : {df_45_70}, більше 70: {df_older_70}")
    print(f"Менше 18: {df_younger_18f}ж, 18-45 : {df_18_45f}ж, 45-70 : {df_45_70f}ж, більше 70: {df_older_70f}ж")
    print(f"Менше 18: {df_younger_18m}м, 18-45 : {df_18_45m}м, 45-70 : {df_45_70m}м, більше 70: {df_older_70m}м")


except FileNotFoundError:
    print("Проблеми при відкритті файлу CSV.")