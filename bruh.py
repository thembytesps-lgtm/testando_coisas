"""texto = 'I love programar demais, entretanto... há uns cursos muito peba por ai'
print(' '.join(texto[::-1].split()))


user_word = input('Irei dizer se sua palavra é palindroma: ').lower().replace(' ', '')

palindroma = user_word == user_word[::-1]

print(f'É Palindroma: {palindroma}') """

lista = [1, 1, 2, 4, 6, 7, 1, 2, 2]

lista_copy = lista.copy()
lista_copy.sort()

print(lista)
print(lista_copy)