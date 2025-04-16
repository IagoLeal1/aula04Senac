codigo = int(input("Digite seu codigo: "))

match codigo:
    case 1:
        print("Acesso liberado para a academia")
    case 2:
        print("Acesso liberado para a piscina")
    case 3:
        print("Acesso liberado para a Salão de Festas")
    case 4:
        print("Acesso liberado para a Cobertura Vip")
    case 5 | 6:
        print("Acesso liberado para a Estacionamento")
    case 7 | 8 | 9:
        print("Acesso liberado para a Todas as Áreas comuns")
    case 10:
        print("Acesso liberado para a Administração")
    case 11:
        print("Acesso liberado para ao Acesso Técnico")
    case _:
        print("Acesso Negado")
