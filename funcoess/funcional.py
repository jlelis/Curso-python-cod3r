def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


somar = soma(3, 4)  # funcao em vairiavel
print(somar)


def operacao_aritimetica(fn, op1, op2):
    return fn(op1, op2)


resultado = operacao_aritimetica(soma, 13, 48)
print(resultado)

resultado = operacao_aritimetica(sub, 13, 48)
print(resultado)


def soma_parcial(a):
    # processameto pesado 1 - 10s
    # processameto pesado 2 - 10s
    # processameto pesado 3 - 40s
    def concluir_soma(b):
        return a + b  # 10s

    return concluir_soma


# r1 = soma_total(1,2) => 1m10s
# r2 = soma_total(1,3) => 1m10s
# r3 = soma_total(1,4) => 1m10s


# fn = soma_parcial(10)
resultado_final = soma_parcial(10)(12)
print(resultado_final)
