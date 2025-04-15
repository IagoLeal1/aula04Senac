compraVl = float(input("insira o valor da compra:  "))

if compraVl > 250:
    desconto = compraVl * 0.16
    compraDesconto = compraVl - desconto
    print("Valor da compra foi:", compraVl, "e com desconto:", compraDesconto)
else:
    print("Você não obteve o desconto, o valor de sua compra foi:", compraVl)