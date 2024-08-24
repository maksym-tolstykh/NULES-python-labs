def fib(n):
    # Функція для обчислення n-го числа Фібоначчі
    if n < 0:
        return "Введіть значення більше 0"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def generate_fib_list(k):
    # Генерує список з k чисел Фібоначчі
    return [fib(i) for i in range(k)]

# Зчитуємо число k від користувача
k = int(input("Введіть кількість чисел Фібоначчі: "))

# Генеруємо та виводимо список чисел Фібоначчі
fib_list = generate_fib_list(k)
print(f"Перші {k} чисел Фібоначчі: {fib_list}")
