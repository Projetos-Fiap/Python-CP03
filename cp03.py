# CP03 - Python - Turma 1ESPW
# Membros do grupo: André Lambert (RM99148), Alessandra Vaiano (RM551497), 
# Bryan William (RM551305), Lucas Feijó (RM99727) e Vitor Maia (RM99658).

import funcoes.entradas as entradas
import funcoes.saidas as saidas
import funcoes.saldo as saldo

import os
# criando função para limpar o terminal
limpa_a_tela = lambda: os.system('clear')

########### DEFINIÇÃO DE BASES INICIAIS ###############

# Registro inicial de entradas (vendas da vinheria, associadas a uma NF)
entradasDB = [
    {
        "itens": [
            {"nf": "000000001", "nome": "ANDRÉ LAMBERT", "cpf": 44146254833, "descricao": "2 vinho tinto", "valor": 60},
            {"nf": "000000002","nome": "VITOR MAIA", "cpf": 12345678912, "descricao": "2 vinho branco", "valor": 70}
        ],
    }  
]

# Registro inicial de saídas (compras/contas da vinheria, associadas a uma NF)
saidasDB = [
    {
        "itens": [
            {"nf": "100000001", "fornecedor": "ANDRÉ LAMBERT", "cnpj": 44146254833, "descricao": "10 rolhas", "valor": 20},
            {"nf": "100000002","fornecedor": "VITOR MAIA", "cnpj": 12345678912, "descricao": "10 garrafas", "valor": 30}
        ],
    }  
]

# Mostrar menu principal
def mostra_menu_principal():
    print("\n")
    print("=========================")
    print("||    CONTABILIDADE    ||")
    print("=========================")
    print("1. ENTRADAS")
    print("2. SAÍDAS")
    print("3. SALDO GERAL")
    print("0. FINALIZAR PROGRAMA")

########### DEFINIÇÃO DO PROGRAMA ###############

# O programa roda até que a opção de sair seja escolhida
while True:
    mostra_menu_principal()
    opcaoMenuPrincipal = input("DIGITE A OPÇÃO DESEJADA: ") 
    match opcaoMenuPrincipal:
        case "1": #ENTRADAS
            limpa_a_tela()
            while True: 
                entradas.mostra_menu_entradas()
                opcaoEntrada = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoEntrada:
                    case "1": # ENTRADAS > CADASTRAR NOVA ENTRADA
                        limpa_a_tela()
                        while True:
                            entradas.cadastrar_entrada()
                    case "2": # ENTRADAS > VER TODAS AS NF
                        limpa_a_tela()
                        while True:
                            entradas.listar_entradas()
                    case "0": # VOLTAR
                        limpa_a_tela()
                        break
                    case _ :
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        
        case "2": # SAÍDAS
            limpa_a_tela()
            while True: 
                saidas.mostra_menu_saidas()
                opcaoSaida = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoSaida:
                    case "1": # SAÍDAS > CADASTRAR NOVA SAÍDA
                        limpa_a_tela()
                        while True:
                            saidas.cadastrar_saida()
                    case "2": # SAÍDAS > VER TODAS AS SAÍDAS
                        limpa_a_tela()
                        while True:
                            saidas.cadastrar_saida()
                    case "0": # VOLTAR
                        limpa_a_tela()
                        break
                    case _ :
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        
        case "3": # SALDO
            limpa_a_tela()
            while True:
                saldo.mostra_menu_saldo()
        
        case "0": # FINALIZAR O PROGRAMA
            break
        case _:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
            continue


        


