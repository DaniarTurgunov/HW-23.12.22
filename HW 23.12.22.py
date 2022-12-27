# 1. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

import random 
def create_equation():
    n = int(input('Введите максимльную степень: '))
    equation = {}
    for m in range(n, -1, -1):
        equation[m] = random.randint(-5, 5)
    return(equation)
equation = create_equation()                 # Для 2 задачи надо закомментировать
# equation1 = create_equation()
# equation2 = create_equation()
# print(equation1)
# print(equation2)
print(equation)                              # Для 2 задачи надо закомментировать

def create_func(equation: dict) -> str:
    new_equation = []
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' ' + ' + '.join(new_equation) + ' = 0' 
    new_equation = new_equation.replace('+ -', '- ').replace('*x**1', '*x')\
        .replace('*x**0', '').replace(' 0*x**', '').replace('1*x', 'x')
    return new_equation 
new_equation = create_func(equation)         # Для 2 задачи надо закомментировать
print(new_equation)                          # Для 2 задачи надо закомментировать


def transf_equ(equation: str) -> dict:       # Для 2 задачи надо закомментировать весь блок
    equation = equation.replace('+ ','').replace(' - ',' -')\
        .replace(' x', ' 1*x').replace(' -x', ' -1*x').replace('*x ', '*x**1 ').split()[:-2]
    dict_equation = {}
    for item in equation:
        i = item.split('*x**')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        elif len(i) == 1:
            dict_equation[0] = int(i[0])
    return dict_equation
dict_equation = transf_equ(new_equation) 
print(dict_equation) 

#  2:

# def summ_equation(first_equ: dict, second_equ: dict):
#     final_equ = {}
#     final_equ.update(first_equ)
#     final_equ.update(second_equ)
#     for key in final_equ:
#         final_equ[key] = first_equ.get(key, 0) + second_equ.get(key, 0)
#     return final_equ
# print(create_func(summ_equation(equation1, equation2)))