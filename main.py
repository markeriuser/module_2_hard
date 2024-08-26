def get_password(n):
    result = ""
    for i in range(1, n//2 + 1):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result
for i in range(3, 20):
    n = int(input("Введите число от 3 до 20: "))
    print(get_password(n))
