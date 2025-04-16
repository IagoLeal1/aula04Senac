# Exemplo 1

vlCompra = float(input("insira o valor da compra:  "))

# Constante se usa letra maiúscula e isso é uma constante
LIMITE = 250

if vlCompra > LIMITE:
    desconto = vlCompra * 0.16
    compraDesconto = vlCompra - desconto
    print("Valor da compra foi:", vlCompra, 
          "e você obteve esse valor de desconto:", desconto, 
          "então o valor total com desconto foi:", compraDesconto)
else:
    print("Você não obteve o desconto, o valor de sua compra foi:", vlCompra)

# Exemplo 2

qtEstoque = int(input("Estoque: "))
qtSolicitada = int(input("Quantos pacotes:"))
pesoPct = float(input("Peso do pacote: "))

PESO_LIMITE = 50

if qtEstoque >= qtSolicitada and PESO_LIMITE > pesoPct:
    print("Liberado!")
else: 
    print("Revisar as condições de estoque e transporte")