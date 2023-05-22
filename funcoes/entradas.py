# Menu de Entradas
def mostra_menu_entradas():
    print("\n")
    print("====================")
    print("||    ENTRADAS    ||")
    print("====================")
    print("1. CADASTRAR NF DE ENTRADA")
    print("2. VER TODAS AS NF DE ENTRADAS") 
    print("0. VOLTAR")

# Mostra na tela todas as compras
def ver_compras(compras):
    if len(compras) == 0:
        print("\n\n>>NENHUMA COMPRA REALIZADA.<<")
    else:
        print('\n')
        print("================================")
        print("||    Histórico de compras    ||")
        print("================================")
        for compra in compras:
            valorTotalCompra = 0
            print('')
            print(f"DATA     : {compra['data']}")
            print(f"DESCRICAO: {compra['descricao']}")
            print("ITENS:")
            for item in compra['itens']:
                valorTotalItem = item['valor'] * float(item['quantidade'])
                valorTotalCompra += valorTotalItem
                print(f"{item['quantidade']} * {item['suprimento']} =", end= " ")
                print('R$ %.2f' % valorTotalItem)
            print('')
            print('VALOR TOTAL DA COMPRA: R$ %.2f' % valorTotalCompra)
            print('-----------------------------------')
            