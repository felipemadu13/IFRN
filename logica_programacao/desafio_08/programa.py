# programa.py
import calcArea

print('Cálculo das áreas de figuras geométricas:')
print('1. Círculo')
print('2. Triângulo')
print('3. Retângulo')
print(' ')

try:
    escolha = int(input('Qual figura deseja calcular a área? '))
    if escolha == 1:
      raio = float(input('Qual o tamanho do raio do círculo? '))
      area = calcArea.circulo(raio)
      print(f"{area:.2f}")
    elif escolha == 2:
      base = float(input('Qual o tamanho da base do triângulo? '))
      altura = float(input('Qual o tamanho da altura do triângulo? '))
      area = calcArea.triangulo(base, altura)
      print(f"{area:.2f}")
    elif escolha == 3:
      base = float(input('Qual o tamanho da base do triângulo? '))
      altura = float(input('Qual o tamanho da altura do triângulo? '))
      area = calcArea.retangulo(base, altura)
      print(f"{area:.2f}")
    else:
      print('ERRO! Essa não é uma opção válida!')
except:
    print('ERRO! Essa não é uma opção válida!')