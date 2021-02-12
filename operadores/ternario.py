lock = True
grana = 130
status = 'Em casa' if lock and grana <= 130 else 'Partiu Festas'
print(status)
# print(f'seu saldo {grana} e o status é: {status}')
