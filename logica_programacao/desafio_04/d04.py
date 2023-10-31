frase = input('Digite uma frase: ').lower().strip()
fraseTratada = frase.replace(' ', '')
palindromo = fraseTratada == fraseTratada[::-1]
caracteres = len(fraseTratada)
print('A frase "{}" tem {} caracteres. É um palíndromo? {}'.format(frase, caracteres, palindromo))