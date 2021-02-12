nota = float(input('Informe a nota: '))

if nota >= 9:
    print('Duas palavras: para bens! :P')
elif nota >= 7:
    print('aprovado!')
elif nota > 4 and nota < 7:
    print('recuperação!')
else:
    print('Reprovado!')

print(nota)
