import os
clear = lambda: os.system('cls')

def calcular_saldo(entradas, saidas):
    total_entradas = sum(entrada["valor"] for entrada in entradas)
    total_saidas = sum(saida["valor"] for saida in saidas)
    saldo_geral = total_entradas - total_saidas
    return saldo_geral

# Menu de Saldo Geral
def mostra_menu_saldo(entradasDB, saidasDB):
    print("\n")
    print("=======================")
    print("||    SALDO GERAL    ||")
    print("=======================")
    saldo_geral = calcular_saldo(entradasDB, saidasDB)
    print(f"Saldo Geral: R$ {saldo_geral:.2f}")
    print("0. VOLTAR")    