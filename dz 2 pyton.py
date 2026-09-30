import random
p = {}
u = set()
def gid():
    while True:
        i = random.randint(10000, 99999)
        if i not in u:
            u.add(i)
            return i
n = int(input("Введите количество человек: "))
for _ in range(n):
    name = input("Имя: ")
    sur = input("Фамилия: ")
    birth = input("Дата рождения: ")
    i = gid()
    p[i] = [name, sur, birth]
print("\n--- Результат ---")
for i, d in p.items():
    print(f"ID {i}: {d[0]} {d[1]}, {d[2]}")
