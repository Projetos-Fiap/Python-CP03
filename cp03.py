# CP03 - Python - Turma 1ESPW
# Membros do grupo: André Lambert (RM99148), Alessandra Vaiano (RM551497), 
# Bryan William (RM551305), Lucas Feijó (RM99727) e Vitor Maia (RM99658).

import funcoes.compras as compras
import funcoes.entradas as entradas
import funcoes.estoque as estoque
import funcoes.fornecedor as fornecedor
import funcoes.saidas as saidas
import funcoes.suprimento as suprimento
import os
# criando função para limpar o terminal
limpa_a_tela = lambda: os.system('cls')

########### DEFINIÇÃO DE BASES INICIAIS ###############

# Registro inicial de entradas (vendas da vinheria)
entradasDB = [
    {
        "itens": [
            {"suprimento": "VINHO TINTO", "valor": 50, "CPF_CLIENTE": "080.412.990-83", "quantidade": 2},
            {"suprimento": "VINHO BRANCO", "valor": 60, "CPF_CLIENTE": "511.262.840-50", "quantidade": 2},
            {"suprimento": "VINHO ROSÉ", "valor": 70, "CPF_CLIENTE": "427.073.250-40", "quantidade": 1},
            {"suprimento": "ESPUMANTE", "valor": 80, "CPF_CLIENTE": "166.299.580-63", "quantidade": 1}
        ],
        "data": "02:43 - 22/5/2023",
        "descricao": "Compra inicial"
    }  
]

# Registro inicial de saídas (compras da vinheria)
saidasDB = [
    {
        "itens": [
            {"suprimento": "ROLHAS", "valor": 3.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 1},
            {"suprimento": "GARRAFAS", "valor": 5.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 1}
        ],
        "data": "02:48 - 22/05/2023",
        "descricao": "Saída inicial"
    }
]

# Registro inicial de estoque
estoqueDB = [
    {"suprimento": "ROLHAS", "valor": 3.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 1},
    {"suprimento": "GARRAFAS", "valor": 5.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 1},
    {"suprimento": "CAIXAS", "valor": 4.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1},
    {"suprimento": "RÓTULOS", "valor": 2.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1}
]

# Registro inicial de fornecedores
fornecedoresDB = [
    {"fornecedor": "FULANO", "cnpj": "60.718.835/0001-03"},
    {"fornecedor": "CICLANO", "cnpj": "49.548.348/0001-07"}
]

# mostrar menu principal
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
                opcaoCompra = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoCompra:
                    case "1": # COMPRAS > MENU DE FORNECEDORES
                        limpa_a_tela()
                        while True:
                            fornecedor.mostra_lista_de_fornecedores(fornecedoresDB)
                            opcaoFornecedor = input('DIGITE A OPÇÃO DESEJADA: ')
                            match opcaoFornecedor:
                                case "9": # COMPRAS > MENU DE FORNECEDORES > CADASTRAR NOVO FORNECEDOR
                                    limpa_a_tela()
                                    fornecedor.cadastrar_fornecedor(fornecedoresDB)
                                    continue
                                case "0": # VOLTAR
                                    limpa_a_tela()
                                    break
                                case _:
                                    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                                    continue
                    case "2": # COMPRAS > MENU DE SUPRIMENTOS
                        limpa_a_tela()
                        while True:
                            suprimento.mostra_menu_comprar_suprimentos(suprimentosDB)
                            opcaoSuprimento = input('DIGITE A OPÇÃO DESEJADA: ')
                            match opcaoSuprimento:
                                case "1": # COMPRAS > MENU DE SUPRIMENTOS > COMPRAR SUPRIMENTO
                                    limpa_a_tela()
                                    suprimento.comprar_suprimento(suprimentosDB, estoqueDB, comprasDB)
                                    continue
                                case "2":# COMPRAS > MENU DE SUPRIMENTOS > CADASTRAR NOVO SUPRIMENTO
                                    limpa_a_tela()
                                    suprimento.cadastrar_suprimento(suprimentosDB, estoqueDB)
                                    continue
                                case "0": # VOLTAR
                                    limpa_a_tela()
                                    break
                                case _:
                                    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                                    continue
                    case "3": # COMPRAS > VER TODAS AS COMPRAS
                        limpa_a_tela()
                        compras.ver_compras(comprasDB)
                        continue
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
                estoque.mostra_menu_estoque()
                opcaoEstoque = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoEstoque:
                    case "1": # ESTOQUE > MOSTRAR ENTRADAS
                        limpa_a_tela()
                        entradas.listar_entradas(comprasDB)
                        continue
                    case "2": # ESTOQUE > MENU SAÍDAS
                        limpa_a_tela()
                        while True:
                            saidas.mostra_menu_saidas()
                            opcaoSaida = input("DIGITE A OPÇÃO DESEJADA: ")
                            match opcaoSaida:
                                case "1": # ESTOQUE > MENU SAÍDAS > LISTAR SAÍDAS
                                    limpa_a_tela()
                                    saidas.listar_saidas(saidasDB)
                                    continue
                                case "2": # ESTOQUE > MENU SAÍDAS > CADASTRAR SAÍDAS
                                    limpa_a_tela()
                                    saidas.cadastrar_saida(saidasDB, estoqueDB)
                                    continue
                                case "0": # VOLTAR
                                    limpa_a_tela()
                                    break
                                case _ :
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n")
                                    continue
                        continue
                    case "3": # ESTOQUE > MOSTRAR ESTOQUE
                        limpa_a_tela()
                        estoque.mostra_estoque(estoqueDB)
                        continue
                    case "0": # VOLTAR
                        limpa_a_tela()
                        break
                    case _:
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        case "0": # FINALIZAR O PROGRAMA
            break
        case _:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
            continue


        


