import os
def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")
def exibir_opcoes():
    print("1- Cadastrar Restaurante")
    print("2- Listar Restaurante")
    print("3- Alternar Restaurante")
    print("4- Sair")
def finalizar_app():
    os.system("cls")
    print("Finalizar o programa\n")
def Opcao_Invalida():
    os.system("cls")
    print("Opção Inválida ❗❗❗❗\n")
    input("Digite qualquer tecla para voltar ao menu principal")
    main()
nomes_dos_restaurantes = [{'nome': "Sabor & Arte" , 'categoria' : 'Caseira', 'ativo': False},{'nome': "Rosa Gastronômica" , 'categoria' : 'Italiano', 'ativo': True},{'nome': "Cantinho dos Sabores" , 'categoria' : 'Japonesa', 'ativo': False}]
def Cadastrar_Novo_Restaurante():
    limpar_tela("Cadastro de um novo restaurante")
    nome_do_restaurante = str(input("Qual é o nome desse restaurante que deseja cadastrar:  "))
    categoria_do_restaurante = str(input(f"Qual é a categoria do restaurante {nome_do_restaurante}:  "))
    dados_do_novo_restaurante = {'nome': nome_do_restaurante , 'categoria' : categoria_do_restaurante, 'ativo': False}
    nomes_dos_restaurantes.append(dados_do_novo_restaurante)
    input(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\nDigite qualquer tecla para voltar ao menu principal")
    main()
def limpar_tela(texto):
    os.system('cls')
    print("="*len(texto))
    print(f'{texto}')
    print("="*len(texto)+"\n")
def voltar_ao_menu():
        input("Digite qualquer tecla para voltar ao menu principal:    ")
        main()
def alternar_estado_do_restaurante():
    limpar_tela('Alterando estado do restaurante')
    nome_do_restaurante_busca = str(input("Digite o nome do restaurante que deseja alterar o estado:  "))
    restaurante_encontrado = False
    for y in nomes_dos_restaurantes:
        if nome_do_restaurante_busca == y['nome']:
            restaurante_encontrado = True
            print("Para Ativar ou Desativar digite Ativar\nPara mudar o nome digite Nome\nPara mudar a categoria digite Categoria")
            o_que_alternar = str(input("O quê deseja fazer :  ")).upper()
            if o_que_alternar == "ATIVAR":
                y['ativo'] = not y['ativo']
                mensagem = "Ativado" if y['ativo'] else "Desativo"
                print(f"O {y['nome']} foi {mensagem} com sucesso")
            elif o_que_alternar == "NOME":
                nome_novo = str(input(f"Digite um novo para o restaurante {y['nome']} : "))
                os.system("cls")
                print(f"Mudar de {y['nome']} para {nome_novo}\n")
                confirmar_o_novo_nome = str(input("Deseja confirmar o novo nome [Sim || Nao] :  ")).upper()
                if confirmar_o_novo_nome == "SIM" or confirmar_o_novo_nome == "S":
                    nome_antigo = y['nome']
                    y['nome'] = nome_novo
                    print(f"O nome do restaurante {nome_antigo} mudou para {nome_novo} com sucesso")
            elif o_que_alternar == "CATEGORIA":
                categoria_nova = str(input(f"O restaurante {y['nome']} é de comida {y['categoria']}, qual será a nova categoria de comida do {y['nome']}: "))
                os.system("cls")
                print(f"Mudar de comida {y['categoria']} para {categoria_nova}\n")
                confirmar_a_nova_categoria = str(input("Deseja confirmar a nova categoria [Sim || Nao] :  ")).upper()
                if confirmar_a_nova_categoria == "SIM" or confirmar_a_nova_categoria == "S":
                    categoria_antiga = y['categoria']
                    y['categoria'] = categoria_nova
                    print(f"O restaurante {y['nome']} mudou de comida {categoria_antiga} para comida {categoria_nova} com sucesso")


    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_ao_menu()



def verificar_opcao():
    try:
        opcao_escolhida = int(input("\nEscolha uma opção: "))
        if opcao_escolhida == 1:
            Cadastrar_Novo_Restaurante()
        elif opcao_escolhida == 2 :
            limpar_tela("Listando os Restaurantes")
            posicao_do_restaurane_na_lista=1
            for x in nomes_dos_restaurantes:
                if x['ativo']:
                    texto_ativo_ou_nao = "Ativo"
                else:
                    texto_ativo_ou_nao = "Desativo"
                nome = x ['nome']
                categoria = x ['categoria']
                ativo = f"Situação atual é de {texto_ativo_ou_nao}"
                print(f"{posicao_do_restaurane_na_lista}.{nome.ljust(20)} || Sua Categoria é de comida {categoria.ljust(20)} || {ativo.ljust(20)} ")
                posicao_do_restaurane_na_lista+=1
            input(f"\nDigite qualquer tecla para voltar ao menu principal")
            main()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            Opcao_Invalida()
    except:
        Opcao_Invalida()
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    verificar_opcao()
if __name__ == '__main__':
    main()