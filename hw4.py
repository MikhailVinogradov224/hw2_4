from ntpath import join
import numbers


N = int(input("Введите размер списка: "))
numbers = list(range(-N, N+1))
data = open('file.txt','w')
data.writelines(','.join(map(str,numbers)))
path = 'file.txt'
data = open(path,'r')
for line in data:
    j = int(input("Введите индекс первой переменной:"))
    k = int(input("Введите индекс второй переменной:"))
    s = numbers [k]*numbers[j]
    print(line)
    print(s)