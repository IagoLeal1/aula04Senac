# Exemplo 4

nota = float(input("Digite a nota: "))

MEDIA = 7
MEDIA_RECU = 5

if nota >= 0:
    if nota >= MEDIA:
        print("Você passou!")
    elif nota >= MEDIA_RECU:
        print("Recuperação")
    else:
        print("Reprovado")

else:
    print("Valor inválido")