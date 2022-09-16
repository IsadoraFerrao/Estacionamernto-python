mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
codigo_letra = ''
palavra = ''

for codigo in mensagem_criptografada:
    if codigo == '-1':
        palavra += chr(int(codigo_letra))
        codigo_letra = ''
        continue

    codigo_letra += codigo

print(f'A palavra é: {palavra}')
