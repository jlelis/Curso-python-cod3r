from functools import reduce


# def mais_um_meio(nota):
#     return nota + 1.5
def somar_nota(delta):
    def somar(nota):
        return nota + delta

    return somar


notas = [6.4, 7.2, 5.8, 8.4]
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)


def somar(a, b):
    return a + b


total = reduce(somar, notas, 0)
print(total)

# for i, nota in enumerate(notas):
#     # print(i, nota)
#     notas[i] = nota + 1.5
# print(notas)

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
# print(notas)
