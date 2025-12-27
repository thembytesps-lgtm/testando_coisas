top_Filmes = ['Interestellar', 'About fate', 'The Dark Knight',
              'Avengers: Ultimato', 'Bastardos Inglorious']

print(top_Filmes)
print(top_Filmes[0])
print(top_Filmes[-1])
print(top_Filmes[1:4])
print(len(top_Filmes))

top_Filmes.append('Joker')
top_Filmes.remove('About fate')
print(top_Filmes)

top_Filmes_Copy = top_Filmes.copy()
top_Filmes_Copy.append('Frozen')
top_Filmes_Copy.sort()

print(top_Filmes_Copy)
print(top_Filmes_Copy.index('Frozen'))
print(top_Filmes.index('Avengers: Ultimato'))

top_Filmes.clear()
top_Filmes_Copy.clear()

print(top_Filmes)
print(top_Filmes_Copy)

""" top_filmes = []

while len(top_filmes) < 10:
    top_filmes.append(input('Diga um filme bom: '))

print(top_filmes) """