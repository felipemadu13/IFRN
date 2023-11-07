dinheiro = 0

while dinheiro < 1:
  print('Informe um valor inteiro maior ou igual a 1 real.')
  dinheiro = int(input('Qual valor você deseja sacar? '))

cedulasMax = int(input('Valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100)? '))

notasDisponiveis = cedulasMax == 1 or cedulasMax == 2 or cedulasMax == 5 or cedulasMax == 10 or cedulasMax == 20 or cedulasMax == 50 or cedulasMax == 100

if (notasDisponiveis and dinheiro >= cedulasMax):
   while dinheiro != 0:
    notas = dinheiro // cedulasMax
    dinheiro = dinheiro % cedulasMax
    if (notas != 0):
      print(f"{notas} de R$ {cedulasMax}")

    if (cedulasMax == 100):
      cedulasMax = 50
    elif (cedulasMax == 50):
      cedulasMax = 20
    elif (cedulasMax == 20):
      cedulasMax = 10
    elif (cedulasMax == 10): 
      cedulasMax = 5
    elif (cedulasMax == 5):
      cedulasMax = 2
    else:
      cedulasMax = 1
else:
   print('condições não atendidas')
    