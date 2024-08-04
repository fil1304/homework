first = int(input('Введите первое число: '))
print(first)
second = int(input('Введите второе число: '))
print(second)
third = int(input('Введите третье число: '))
print(third)
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif not first == second == third:
    print(0)


