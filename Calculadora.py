num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite a opção: ")

if operacao == "1":
    resultado = num1 + num2
elif operacao == "2":
    resultado = num1 - num2
elif operacao == "3":
    resultado = num1 * num2
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        resultado = None
else:
    print("Operação inválida")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)
