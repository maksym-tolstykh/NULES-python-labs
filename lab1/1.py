def is_prime(n):
    #Перевіряємо, чи є число простим.
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between(a, b):
    #Знаходимо всі прості числа між a та b.
    if a > b:
        a, b = b, a  # Міняємо місцями a та b, якщо a більше за b
    return [num for num in range(a, b + 1) if is_prime(num)]

# Зчитуємо числа a та b від користувача
a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))

# Знаходимо та виводимо прості числа між a та b
primes = find_primes_between(a, b)
print(f"Прості числа між {a} та {b}: {primes}")
