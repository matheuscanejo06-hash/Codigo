def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media


notas = [8, 7, 9, 6, 10]
print(f"A média é: {calcular_media(notas)}")
