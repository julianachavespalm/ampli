# Função para validar entrada de dados numéricos nos campos peso e altura
def validar_dado(mensagem):
        while True:
                entrada = input(mensagem + " ou 'sair' para encerrar: ").strip().replace(",", ".")
                if entrada.lower() == "sair":
                        print("Agradecemos por utilizar a calculadora Adeps!")
                        print("Programa encerrado.")
                        quit()
                elif entrada.replace(".", "").isdigit() and float(entrada) > 0:
                        return float(entrada)
                else:
                        print("Entrada inválida. Insira apenas números maiores do que zero.")


#Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / pow(altura, 2)
    return round(imc, 2)


# Apresentação do programa
print(f"Adeps: calculadora de Índice de Massa Corporal (IMC)\n")

# Solicitação de entrada do valor do peso
peso = validar_dado('Digite o peso (em quilos)')

# Solicitação de entrada do valor da altura
altura = validar_dado('Digite sua altura (em metros)')

# Chamada da função do IMC, com os dados inseridos de peso e altura
imc = calcular_imc(peso, altura)

# Exibição do resultao do IMC e sua classificação
print(f"Seu IMC é {imc:.2f}".replace('.', ',') + ".")

# Mensagem de encerramento da calculadora Adeps
print("Agradecemos por utilizar a calculadora Adeps.")
print("Não recomendamos para o cálculo de IMC de gestantes e menores de 18 anos.")
print("Casos tenha dúvidas ou preocupações, consulte um profissional de saúde.")
print("Programa encerrado.")
