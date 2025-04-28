f = open("DZ.txt", "w")
f.write("Замена строки в текстовом файле; \nзаписать список в файл; \nизменить строку в списке;\n")
f.close()

f = open("DZ.txt", "r")
print(f.read())
f.close()

try:
    pos1 = int(input("Введите номер строки: "))
    pos2 = int(input("Введите номер строки для замены: "))
    if 0 < pos1 <= 3 and 0 < pos2 <= 3:
        pos1 = pos1 - 1
        pos2 = pos2 - 1
        f = open("DZ.txt", "r")
        read_file = f.readlines()
        read_file[pos1], read_file[pos2] = read_file[pos2], read_file[pos1]
        f.close()
        f = open("DZ.txt", "w")
        f.writelines(read_file)
        f.close()
    else:
        print("Не верное число")
except ValueError:
    print("Значение некорректно. Введите число")

print()
f = open("DZ.txt", "r")
print(f.read())




