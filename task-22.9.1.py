#!/usr/bin/python

# def quick_sort() - быстрый поиск
# def bin_search_m() - модифицированный под условия задачи двоичный поиск

def main():
    init_list = []

    init_string = input('Введите последовательность чисел через пробел: ')
    init_num_str = input('Введите любое число: ')
    
    init_list_str = init_string.split()
    init_num = int(init_num_str)

    for i in init_list_str:
        init_list.append(int(i))
    
    left = 0
    right = len(init_list)-1
    quick_sort(init_list, left, right)
    print("Осортированный список: ", init_list)

    if init_num < init_list[0] or init_num > init_list[-1]:
        print('Введённое вами число не присутствует в списке.')
    else:
        idx = bin_search_m(init_list, init_num, left, right)
        print('Индекс элемента, такого, что, он меньше введённого вами числа, но следующий за ним элемент больше или равен этому числу (индекс считается с 0): ', idx)

def quick_sort(ilist, left, right):
    middle = (left+right) // 2
    
    p = ilist[middle]
    i,j = left, right
    while i <= j:
        while ilist[i] < p:
            i += 1
        while ilist[j] > p:
            j -= 1
        if i <= j:
            ilist[i], ilist[j] = ilist[j], ilist[i]
            i += 1
            j -= 1
        
    if j > left:
        quick_sort(ilist, left, j)
    if right > i:
        quick_sort(ilist, i, right)
        
def bin_search_m(ilist, element, left, right): 
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует
            
    middle = (right+left) // 2 # находим середину
    if ilist[middle] < element and ilist[middle+1] >= element: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < ilist[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return bin_search_m(ilist, element, left, middle-1)
    else: # иначе в правой
        return bin_search_m(ilist, element, middle+1, right)

if __name__ == "__main__":
    main()
