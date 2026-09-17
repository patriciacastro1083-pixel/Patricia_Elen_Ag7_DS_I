# Campanha de Conscientização Ambiental

# Entrada

print("Bem-vindo à Campanha de Conscientização Ambiental!")

opcao = input("Digite seu tipo de imóvel ( 1 - comercial, 2 - apartamento, 3 -casa): ")

match opcao:
    case '1':
        print("Você selecionou a opção comercial.")
    case '2':
        print("Você selecionou a opção apartamento.")
    case '3':
        print('Você selecionou a opção casa.')

consumo = int(input("Digite seu consumo de água mensal em metros cúbicos (m3): "))

# condições de consumo 

match opcao:
    case '1':
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    case '2' if consumo < 10:
        print("Consumo econômico – excelente controle de água!")
    case '2' if consumo >10 and consumo<=25:
        print("Consumo moderado – dentro do padrão residencial.")
    case '3' if consumo<=25:    
        print("Consumo moderado - dentro do padrão residencial.")
    case '2'|'3' if consumo>25:
        print("Consumo excessio – adote medidas de economia e verifique vazamentos.")





     















