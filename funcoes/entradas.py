import os
clear = lambda: os.system('cls')

# Menu de Entradas
def mostra_menu_entradas():
    print("\n")
    print("====================")
    print("||    ENTRADAS    ||")
    print("====================")
    print("1. CADASTRAR NOVA ENTRADA")
    print("2. VER TODAS AS ENTRADAS") 
    print("0. VOLTAR")
            
# 1. Cadastrar NFs de entradas (vendas da vinheria)
def cadastrar_entrada(entradas):
    print("\n")
    print("===========================")
    print("||   CADASTRAR ENTRADA   ||")
    print("===========================")
    nfEntrada = input("DIGITE O NÚMERO DA NF: ")
    if len (nfEntrada) != 8:
        print("NÚMERO INVÁLIDO! A NF TEM QUE TER 8 CARACTERES")
    else:
        nomeCliente = input("DIGITE O NOME DO CLIENTE: ") 
        cpfCliente = input("DIGITE O CPF DO CLIENTE: ")
        if len (cpfCliente) != 11:
            print("NÚMERO INVÁLIDO! O CPF TEM QUE TER 11 CARACTERES")
        else: 
            descricao = input("DIGITE UMA DESCRIÇÃO: ")
            valor = float(input("DIGITE O VALOR DA NF: "))
            if (valor <= 0):
                print("VALOR INVÁLIDO! TENTE NOVAMENTE")    
            else:
                nova_nf = {"nf": nfEntrada, "cliente": nomeCliente, "cpf": cpfCliente, "descricao": descricao, "valor": valor}
                entradas.append(nova_nf)
                clear()
                print("NF CADASTRADA COM SUCESSO!")
            

# 2. Mostra todas as entradas na tela
def listar_entradas(entradas):
    if len(entradas) == 0:
        print('\n\n >>NENHUMA ENTRADA REGISTRADA.<<')
    else:
        print('\n')
        print("=================================")
        print("||    HISTÓRICO DE ENTRADAS    ||")
        print("=================================")
        for entrada in entradas:
            print('')
            print(f"NF:      : {entrada['nf']}")
            print(f"CLIENTE: {entrada['cliente']}")
            print(f"CPF: {entrada['cpf']}")
            print(f"DESCRIÇÃO: {entrada['descricao']}")
            print(f"VALOR: {entrada['valor']}")
            print('')
            print('-----------------------------------')
            
            
            