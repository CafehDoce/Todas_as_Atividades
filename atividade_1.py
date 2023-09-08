#ATIVIDADE 1

nome = input ("Qual seu nome? ")
sobrenome = input ("Qual seu sobrenome? ")
altura = int(input ("Qual sua altura? "))
peso = int(input ("Qual seu peso? "))
idade = int(input ("Qual sua idade? "))
adulto = idade >= 18
print ("Seu nome é:",nome)
print ("Seu sobrenome é:",sobrenome)
print ("Sua altura é:",altura,"cm")
print ("Seu peso é :",peso,"kg")
print ("Você é maior de idade." if adulto else "Você não é maior de idade.")