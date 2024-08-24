import pandas as pd
from faker import Faker

fake = Faker('uk-UA')

headers = ["Прізвище","Ім’я","По батькові","Стать","Дата народження","Посада","Місто проживання","Адреса проживання","Телефон","Email"]

# Генеруємо дані
def generate_fake_data(num_rows):
    data = []
    for _ in range(num_rows):
        gender = fake.random_element(elements=('Чоловік', 'Жінка'))
        # Генерація імені відповідно до статі
        if gender == 'Чоловік':
            first_name = fake.first_name_male()
            middle_name = fake.middle_name_male()
        else:
            first_name = fake.first_name_female()
            middle_name = fake.middle_name_female()
        row = [
            fake.last_name(),            # Прізвище
            first_name ,           # Ім’я
            middle_name,          # По батькові
            gender,  # Стать
            fake.date_of_birth(minimum_age=16, maximum_age=86).strftime('%d-%m-%Y'),  # Дата народження
            fake.job(),                  # Посада
            fake.city(),                 # Місто проживання
            fake.address().replace('\n', ', '),  # Адреса проживання
            fake.phone_number(),         # Телефон
            fake.email()                 # Email
        ]
        data.append(row)
    return data

# Генеруємо фейкові дані
fake_data = generate_fake_data(2000)

# Створюємо DataFrame
df = pd.DataFrame(fake_data, columns=headers)
# Записуємо DataFrame у CSV файл
df.to_csv('./lab4/Employees.csv', index=False, encoding='utf-8-sig')
print("Файл створено")