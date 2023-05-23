import os
clear = lambda: os.system('cls')

# Menu de Saldo Geral
def mostra_menu_saldo():
    print("\n")
    print("=======================")
    print("||    SALDO GERAL    ||")
    print("=======================")


def calcular_saldo(entradas, saidas):
    total_entradas = sum(entrada["valor"] for entrada in entradas)
    total_saidas = sum(saida["valor"] for saida in saidas)
    saldo_geral = total_entradas - total_saidas
    return saldo_geral