for i in range(10):
    print(i)
for i in range(1, 11):
    print(i)
for i in range(0, 100, 2):
    print(i)
for i in range(20, 0, -3):
    print(i)
nums = [1, 2, 3, 4, 5]

for n in nums:
    print(n, end=',')
texto = 'Python eh fera'
for letra in texto:
    print(letra, end=' ')
for n in {1, 2, 3, 4, 5, 6, 6, 4, 3}:
    print(n, end=' ')

produto = {
    'nome': 'Caneta',
    'preco': 8.90,
    'desc': 0.5,
}

for atrib in produto:
    print(atrib, '==>', produto[atrib])

for atrib, valor in produto.items():
    print(atrib, '=>', valor)

for valor in produto.values():
    print(valor, end=' ')
for atrib in produto.keys():
    print(atrib, end=' ')

