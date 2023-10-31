aluno = input("Informe o nome do aluno: ")
nota1 = int(input("Informe a nota do 1º bimestre (0 a 100): "))
nota2 = int(input("Informe a nota do 2º bimestre (0 a 100): "))
nota3 = int(input("Informe a nota do 3º bimestre (0 a 100): "))
nota4 = int(input("Informe a nota do 4º bimestre (0 a 100): "))

soma = nota1 * 2 + nota2 * 2 + nota3 * 3 + nota4 * 3
media = round(soma / 10)

if media >= 60:
    situacao = "Aprovado"
    cor = "\033[97;42m" 
elif 20 <= media < 60:
    situacao = "Em Recuperação"
    cor = "\033[31;43m" 
else:
    situacao = "Reprovado"
    cor = "\033[7;31m" 

print("{} O aluno {} obteve a média {} e está {}.\033[m".format(cor, aluno, media, situacao))
