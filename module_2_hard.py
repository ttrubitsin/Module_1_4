def generate_password(n):
    result_pass = ""
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0:
                result_pass += str(i) + str(j)
    return result_pass

# Пример
n = 5

result = generate_password(n)
print(f'Число первой вставки: {n}', f'пароль: {result}')

