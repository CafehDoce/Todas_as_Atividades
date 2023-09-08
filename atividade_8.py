#A ATIVIDADE 8 /SÃO 3 COMANDOS PYTHON DIFERENTE!

#COMANDO 1 - Esta função imprime uma mensagem simples na tela.
def saudacao():
    print("Olá, mundo!")

# Chamando a função para exibir a saudação.
saudacao()


#COMANDO 2 - Esta função recebe dois números e os adiciona, mas não retorna o resultado.
def somar(a, b):
    resultado = a + b
    print(f"A soma de {a} e {b} é igual a {resultado}")

# Chamando a função para somar dois números.
somar(5, 3)


#COMANDO 3 - Esta função recebe uma lista de números e retorna a média.
def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

# Chamando a função para calcular a média de uma lista de números.
lista_numeros = [10, 20, 30, 40, 50]
media_resultante = calcular_media(lista_numeros)
print(f"A média dos números na lista é {media_resultante}")