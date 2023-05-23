import os
clear = lambda: os.system('clear')

# Menu de Saídas
def mostra_menu_saidas():
    print("\n")
    print("==================")
    print("||    SAÍDAS    ||")
    print("==================")
    print("1. CADASTRAR NOVA SAÍDA")
    print("2. VER TODAS AS SAÍDAS") 
    print("0. VOLTAR")
            
# 1. Cadastrar NFs de saídas (contas da vinheria)
def cadastrar_saida(saidas):
    print("\n")
    print("=========================")
    print("||   CADASTRAR SAÍDA   ||")
    print("=========================")
    nfSaida = input("DIGITE O NÚMERO DA NF: ")
    if len (nfSaida) != 8:
        print("NÚMERO INVÁLIDO! A NF TEM QUE TER 8 CARACTERES")
    else:
        nomeFornecedor = input("DIGITE O NOME DO FORNECEDOR: ") 
        cnpjFornecedor = input("DIGITE O CNPJ DO FORNECEDOR: ")
        if len (cnpjFornecedor) != 14:
            print("NÚMERO INVÁLIDO! O CNPJ TEM QUE TER 14 CARACTERES")
        else: 
            descricao = input("DIGITE UMA DESCRIÇÃO: ")
            valor = float(input("DIGITE O VALOR DA NF: "))
            if (valor <= 0):
                print("VALOR INVÁLIDO! TENTE NOVAMENTE")    
            else:
                nova_nf = {"nf": nfSaida, "fornecedor": nomeFornecedor, "cnpj": cnpjFornecedor, "descricao": descricao, "valor": valor}
                saidas.append(nova_nf)
                clear()
                print("NF CADASTRADA COM SUCESSO!")
            

# 2. Mostra todas as saídas na tela
def listar_saidas(saidas):
    if len(saidas) == 0:
        print('\n\n >>NENHUMA SAÍDA REGISTRADA.<<')
    else:
        print('\n')
        print("===============================")
        print("||    HISTÓRICO DE SAÍDAS    ||")
        print("===============================")
        for saida in saidas:
            print('')
            print(f"NF:      : {saida['nf']}")
            print(f"FORNECEDOR: {saida['fornecedor']}")
            print(f"CNPJ: {saida['cnpj']}")
            print(f"DESCRIÇÃO: {saida['descricao']}")
            print(f"VALOR: {saida['valor']}")
            print('')
            print('-----------------------------------')
            