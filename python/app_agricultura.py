import csv

culturas = []

# Funções auxiliares
def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

def calcular_insumo(area, qtd_por_metro):
    return area * qtd_por_metro

def salvar_dados_csv():
    with open('dados_agricultura.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Cultura', 'Area_m2', 'Insumo', 'Qtd_total_insumo'])
        for cultura in culturas:
            writer.writerow([cultura['nome'], cultura['area'], cultura['insumo'], cultura['qtd_insumo']])

# Menu de opções
def menu():
    print("""
    FarmTech Solutions - Agricultura Digital

    1. Entrada de Dados
    2. Exibir Dados
    3. Atualizar Dados
    4. Deletar Dados
    5. Salvar Dados em CSV (para uso em R)
    6. Sair
    """)

# Loop principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome da cultura: ")
        comprimento = float(input("Comprimento da área (m): "))
        largura = float(input("Largura da área (m): "))
        area = calcular_area_retangulo(comprimento, largura)

        insumo = input("Nome do insumo: ")
        qtd_por_metro = float(input("Quantidade do insumo por metro quadrado: "))
        qtd_insumo = calcular_insumo(area, qtd_por_metro)

        culturas.append({
            'nome': nome,
            'area': area,
            'insumo': insumo,
            'qtd_insumo': qtd_insumo
        })
        print("Dados inseridos com sucesso.")

    elif opcao == '2':
        for idx, cultura in enumerate(culturas):
            print(f"[{idx}] Cultura: {cultura['nome']}, Área: {cultura['area']} m², Insumo: {cultura['insumo']}, Qtd: {cultura['qtd_insumo']} unidades")

    elif opcao == '3':
        idx = int(input("Digite o índice do dado que deseja atualizar: "))
        if 0 <= idx < len(culturas):
            culturas[idx]['nome'] = input("Novo nome da cultura: ")
            culturas[idx]['area'] = float(input("Nova área (m²): "))
            culturas[idx]['insumo'] = input("Novo nome do insumo: ")
            culturas[idx]['qtd_insumo'] = float(input("Nova quantidade total do insumo: "))
            print("Dados atualizados com sucesso.")
        else:
            print("Índice inválido.")

    elif opcao == '4':
        idx = int(input("Digite o índice do dado que deseja deletar: "))
        if 0 <= idx < len(culturas):
            culturas.pop(idx)
            print("Dados deletados com sucesso.")
        else:
            print("Índice inválido.")

    elif opcao == '5':
        salvar_dados_csv()
        print("Dados salvos em CSV com sucesso (dados_agricultura.csv).")

    elif opcao == '6':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, tente novamente.")

