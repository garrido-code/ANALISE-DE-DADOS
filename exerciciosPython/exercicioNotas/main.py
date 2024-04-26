print("NOTA ALUNO")

#pegar as informações
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a Sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))


#somar as notas e mutipliacar as que tem peso
notaAluno = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5))/10
    
if notaAluno >= 6 and notaAluno <= 10:
    print("PARABÉNS VOCÊ PASSOU 🥳 🎉")
else:
    print("INFELIZMENTE VOCÊ NÃO PASSOU 😰")
    print(f"O valor das notas {nota1}, {nota2}, {nota3} é igual a {notaAluno}")