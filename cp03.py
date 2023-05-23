# CP03 - Python - Turma 1ESPW
# Membros do grupo: André Lambert (RM99148), Alessandra Vaiano (RM551497), 
# Bryan William (RM551305), Lucas Feijó (RM99727) e Vitor Maia (RM99658).

import funcoes.entradas as entradas
import funcoes.saidas as saidas
import funcoes.saldo as saldo

import os
# criando função para limpar o terminal
limpa_a_tela = lambda: os.system('cls')

########### DEFINIÇÃO DE BASES INICIAIS ###############

# Registro inicial de entradas (vendas da vinheria, associadas a uma NF)
entradasDB = [
    {"nf": "000000001", "cliente": "André", "cpf": "12345678900", "descricao": "1 Tinto", "valor": 50.0},
    {"nf": "000000002", "cliente": "Vitor", "cpf": "98765432100", "descricao": "1 Branco", "valor": 60.0},
    # Adicione mais registros conforme necessário
]

# Registro inicial de saídas (compras/contas da vinheria, associadas a uma NF)
saidasDB = [
    {"nf": "100000001", "fornecedor": "Fulano", "cnpj": "35250222000108", "descricao": "100 Garrafas", "valor": 500.0},
    {"nf": "200000002", "fornecedor": "Ciclano", "cnpj": "98765432000199", "descricao": "100 Rolhas", "valor": 200.0},
    # Adicione mais registros conforme necessário
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
                        entradas.cadastrar_entrada(entradasDB)
                    case "2": # ENTRADAS > VER TODAS AS NF
                        limpa_a_tela()
                        entradas.listar_entradas(entradasDB)
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
                        saidas.cadastrar_saida(saidasDB)
                    case "2": # SAÍDAS > VER TODAS AS SAÍDAS
                        limpa_a_tela()
                        saidas.listar_saidas(saidasDB)
                    case "0": # VOLTAR
                        limpa_a_tela()
                        break
                    case _ :
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        
        case "3": # SALDO
            while True:
                limpa_a_tela()
                saldo.mostra_menu_saldo(entradasDB, saidasDB)
                opcaoSaldo = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoSaldo: 
                    case "0": #VOLTAR
                        limpa_a_tela
                        break
                    case _ :
                        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n")
                        continue

        case "0": # FINALIZAR O PROGRAMA
            break
        case _:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
            continue


        


