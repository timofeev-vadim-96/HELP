# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d. 
# Функция должна возвращать новый созданный одномерный список.
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

res_list = []
def get_line_list(input_list, arr = list(), counter = 0):
    if counter == len(input_list)-1: return arr
    else: 
        arr.append(input_list[counter])
        counter +=1
        get_line_list(input_list,arr,counter)
print(get_line_list(d))
    