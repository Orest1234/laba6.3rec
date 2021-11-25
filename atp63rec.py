# atp63rec.py
# Хімчинський Орест
# Лабораторна робота No 6.3
# Пошук елементів одновимірного масиву
# Варіант 15
import random


# створення масиву
def create(size, p=[]):
    if size <= 0:

        return p
    else:

        p.append(int(random.random() * 10))
        size -= 1
        return create(size)


# визначення парних чисел
def search_double(p, list_double=[]):
    if p == []:
        return list_double

    else:
        if p[0] % 2 == 0:
            list_double.append(p[0])
            p = p[1:]
        else:
            p = p[1:]
        return search_double(p, list_double)




# розрахунки
def calculation(list_double, res=0):
    if list_double == []:
        return res
    else:
        number = list_double[0]
        if number != None:

            res += 1
            list_double = list_double[1:]
            return calculation(list_double,res)


# головна функція
def main():
    p = create(10)
    print('Масив: ', p)
    list_double = search_double(p)
    summ = calculation(list_double)
    print('Кількість парних елементів масиву: ', summ)


main()