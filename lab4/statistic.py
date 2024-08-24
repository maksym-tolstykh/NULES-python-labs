import pandas as pd
import matplotlib.pyplot as plt

filePath = "./lab4/Employees.csv"
outputPath = './lab4/sorted_data.xlsx'

try:
    # Завантаження даних
    df = pd.read_csv(filePath)

    # Підрахунок кількості чоловіків і жінок
    gender_counts = df["Стать"].value_counts()
    all_Male = gender_counts.get("Чоловік", 0)
    all_Female = gender_counts.get("Жінка", 0)

    # Перетворення стовпця "Дата народження" на тип datetime
    df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%d-%m-%Y')
    today = pd.Timestamp.today()
    df['Вік'] = (today - df['Дата народження']).dt.days // 365

    # Функція для підрахунку вікових категорій
    def count_age_groups(df, gender=None):
        if gender:
            df = df[df["Стать"] == gender]
        return {
            "менше 18": len(df[df['Вік'] < 18]),
            "18-45": len(df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]),
            "45-70": len(df[(df['Вік'] > 45) & (df['Вік'] <= 70)]),
            "більше 70": len(df[df['Вік'] > 70])
        }

    # Підрахунок вікових категорій
    age_groups_total = count_age_groups(df)
    age_groups_female = count_age_groups(df, gender="Жінка")
    age_groups_male = count_age_groups(df, gender="Чоловік")

    # Виведення результатів
    print("Кількість співробітників чоловічої статі:", all_Male)
    print("Кількість співробітників жіночої статі:", all_Female)
    print(f"Менше 18: {age_groups_total['менше 18']}, 18-45 : {age_groups_total['18-45']}, 45-70 : {age_groups_total['45-70']}, більше 70: {age_groups_total['більше 70']}")
    print(f"Менше 18: {age_groups_female['менше 18']}ж, 18-45 : {age_groups_female['18-45']}ж, 45-70 : {age_groups_female['45-70']}ж, більше 70: {age_groups_female['більше 70']}ж")
    print(f"Менше 18: {age_groups_male['менше 18']}м, 18-45 : {age_groups_male['18-45']}м, 45-70 : {age_groups_male['45-70']}м, більше 70: {age_groups_male['більше 70']}м")

   # Створення графіків
    # Графік кількості чоловіків та жінок
    plt.figure(figsize=(10, 6))
    gender_counts.plot(kind='bar', color=['blue', 'pink'])
    plt.title('Кількість співробітників за статтю')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('./lab4/gender_counts.png')
    plt.show()

       # Графіки вікових категорій
    age_groups_df = pd.DataFrame({
        'Вікова категорія': list(age_groups_total.keys()),
        'Загальна кількість': list(age_groups_total.values()),
        'Жінки': list(age_groups_female.values()),
        'Чоловіки': list(age_groups_male.values())
    })

    age_groups_df.set_index('Вікова категорія').plot(kind='bar', figsize=(12, 8))
    plt.title('Розподіл за віком')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('./lab4/age_groups.png')
    plt.show()

except FileNotFoundError:
    print("Проблеми при відкритті файлу CSV.")
