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
nomes_dos_restaurantes = [{'nome': "Sabor & Arte" , 'categoria' : 'Caseira', 'ativo': False,'senha':"senha de teste"},{'nome': "Rosa Gastronômica" , 'categoria' : 'Italiano', 'ativo': True,'senha':"senha de teste2"},{'nome': "Cantinho dos Sabores" , 'categoria' : 'Japonesa', 'ativo': False,'senha':"senha de teste3"}]
def Cadastrar_Novo_Restaurante():
    limpar_tela("Cadastro de um novo restaurante")
    nome_do_restaurante = str(input("Qual é o nome desse restaurante que deseja cadastrar:  "))
    categoria_do_restaurante = str(input(f"Qual é a categoria do restaurante {nome_do_restaurante}:  "))
    senha_do_restaurante = input("Digite sua senha: ")
    dados_do_novo_restaurante = {'nome': nome_do_restaurante , 'categoria' : categoria_do_restaurante, 'ativo': False, 'senha': senha_do_restaurante}
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
            print("Para Ativar ou Desativar digite Ativar\nPara mudar o nome digite Nome\nPara mudar a categoria digite Categoria\nPara ver ou mudar a senha digite Senha\nPara apagar digite Apagar")
            o_que_alternar = str(input("O quê deseja fazer :  ")).upper()
            if o_que_alternar == "ATIVAR":
                y['ativo'] = not y['ativo']
                mensagem = "Ativado" if y['ativo'] else "Desativo"
                print(f"O {y['nome']} foi {mensagem} com sucesso")
            elif o_que_alternar == "NOME":
                limpar_tela("Mudando o Nome")
                nome_novo = str(input(f"Digite um novo para o restaurante {y['nome']} : "))
                print(f"Mudar de {y['nome']} para {nome_novo}\n")
                confirmar_o_novo_nome = str(input("Deseja confirmar o novo nome [Sim || Nao] :  ")).upper()
                if confirmar_o_novo_nome == "SIM" or confirmar_o_novo_nome == "S":
                    nome_antigo = y['nome']
                    y['nome'] = nome_novo
                    print(f"O nome do restaurante {nome_antigo} mudou para {nome_novo} com sucesso")
            elif o_que_alternar == "CATEGORIA":
                limpar_tela("Mudando a Categoria")
                categoria_nova = str(input(f"O restaurante {y['nome']} é de comida {y['categoria']}, qual será a nova categoria de comida do {y['nome']}: "))
                print(f"Mudar de comida {y['categoria']} para {categoria_nova}\n")
                confirmar_a_nova_categoria = str(input("Deseja confirmar a nova categoria [Sim || Nao] :  ")).upper()
                if confirmar_a_nova_categoria == "SIM" or confirmar_a_nova_categoria == "S":
                    categoria_antiga = y['categoria']
                    y['categoria'] = categoria_nova
                    print(f"O restaurante {y['nome']} mudou de comida {categoria_antiga} para comida {categoria_nova} com sucesso")
            elif o_que_alternar == "SENHA":
                limpar_tela("Configurando a senha")
                print("Para ver a Senha digite Ver\nPara mudar a senha digite Mudar")
                o_que_fazer_senha = str(input("O que você deseja fazer: ")).upper()
                if o_que_fazer_senha == "VER":
                    print(f"A senha atual do {y['nome']} é : {y['senha']}")
                elif o_que_fazer_senha == "MUDAR":
                    limpar_tela("Mudando a senha")
                    senha_nova = input("Digite uma nova Senha: ")
                    y['senha'] = senha_nova
                    print(f"A senha do {y['nome']} mudou para nova senha com sucesso")
            elif o_que_alternar == "APAGAR":
                limpar_tela("Apagar o Restaurante")
                confirmar_que_vai_apagar = str(input("Deseja Apagar [Sim || Nao] :  ")).upper()
                if confirmar_que_vai_apagar == "SIM" or confirmar_que_vai_apagar == "S":
                    contador = 0
                    while (contador < 3):
                        verificar_senha = input("Digite a Senha para apagar: ")
                        if verificar_senha == y['senha']:
                            print(f"Você apagou o restaurante {y['nome']} com sucesso")
                            nomes_dos_restaurantes.remove(y)
                            contador = 3
                        else:
                            print("Você digitou a senha errada")
                            contador+=1
                


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
                senha = "*"*len(x['senha'])
                print(f"{posicao_do_restaurane_na_lista}.{nome.ljust(20)} || Sua Categoria é de comida {categoria.ljust(20)} || {ativo.ljust(20)} || Sua senha é: {senha} ")
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