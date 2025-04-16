# Exemplo 3

anoFili = int(input("Insira o tempo de filiação(em anos): "))
vlMovimentado = float(input("Valor movimentado nos últimos 6 meses (R$): "))

VL_ANO_FILI = 3
VL_MOVIMENTADO = 5000

if anoFili >= VL_ANO_FILI or vlMovimentado > VL_MOVIMENTADO: 
    print("Você tem direito ao benefício especial")
else:
    print("Você ainda não atende aos critérios para o benefício")