# Exemplo 2

qtEstoque = int(input("Estoque: "))
qtSolicitada = int(input("Quantos pacotes:"))
pesoPct = float(input("Peso do pacote: "))

PESO_LIMITE = 50

if qtEstoque >= qtSolicitada and PESO_LIMITE > pesoPct:
    print("O pedido pode ser liberado!")
else:
    print("Revisar as condições de estoque e transporte")