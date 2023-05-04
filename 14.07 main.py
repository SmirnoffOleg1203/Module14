first_year = int(input("Введите первый год: "))
second_year = int(input("Введите второй год: "))

print(f"Года от {first_year} до {second_year} с тремя одинаковыми цифрами:")

for i in range(first_year, second_year +1 ):
    first = i // 1000
    second = (i // 100) % 10
    match_1 = 0
    match_2 = 0
    for j in str(i):
        if int(j) == first:
            match_1 += 1
        if int(j) == second:
            match_2 += 1
    if match_1 == 3 or match_2 == 3:
        print(i)
