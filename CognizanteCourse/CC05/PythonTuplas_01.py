# Tuplas are immutables
lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

# [?] get or update especific element from list
lista_animal[0] = 'macaco'
print(lista_animal)

# Tuplas
tupla = (1, 10, 2, 14)
print(tupla)
print(tupla[1])

# Below function gets error, because tuplas are immutable
# tupla[0] = 12

# len gets the quantity of elements in tuplas
print(len(tupla))

# Tuple function converts list to tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

# List function converts list to tupla
lista_numerica = list(tupla)
lista_numerica[0] = 100
print(type(lista_numerica))
print(lista_numerica)

# # Lists and Tuplas
# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante']
#
# print(lista)
# print(type(lista_animal))
#
# # The first element from a list is the number '0'
# print(lista_animal[1])
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
#
# # sum is used to sum all elements from list
# # max gets the bigest element from list
# # min gets the lowest element from list
# print(sum(lista))
# print(max(lista))
# print(min(lista))
#
# # 'In' function valid se has a value in list
# # append adds elements to list
# if 'lobo' in lista_animal:
#     print('Existe um gato na lista')
# else:
#     print('Não existe um lobo na lista')
#     lista_animal.append('lobo')
#
# # you can make calcs with list
# nova_lista = lista_animal * 3
# print(nova_lista)
#
# # pop delete last element from list or with position
# # remove delete element by name
# lista_animal.pop()
# lista_animal.pop(0)
# lista_animal.remove('elefante')
# print(lista_animal)
#
# lista = [12, 10, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
#
# # Sort puts list in ordem
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
#
# # Revert sort elements in reverse order
# lista.reverse()
# lista_animal.reverse()
# print(lista)
# print(lista_animal)
#
#
#
