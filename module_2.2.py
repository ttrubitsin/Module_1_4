first = int(input("Введите 1 число: "))
second = int(input("Введите 2 число: "))
third = int(input("Введите 3 число: "))
if first == second == third:
    print(3)
elif first == second != third:
    print(2)
elif first == third != second:
    print(2)
elif second == third != first:
    print(2)
else:
    print (0)
