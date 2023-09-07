"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal, e condição de
pagamento:
> à vista dinheiro/cheque: 10% de desconto
> à vista no cartao: 5% de desconto
> em até 2x no cartão: preço normal
> 3x ou mais no cartão: 20% de juros
"""

print('{:=^40}'.format(' \33[0;31mLU COSTUMIZA\33[0m '))
preco = float(input('Valor das compras: R$'))
print('''\33[0;49;90mFORMAS DE PAGAMENTOS\33[0m
[\33[0;31m 1 \33[0m] à vista dinheiro / cheque
[\33[0;31m 2 \33[0m] à vista cartão
[\33[0;31m 3 \33[0m] 2x no cartão
[\33[0;31m 4 \33[0m] 3x ou mais no cartão
''')
opcao = int(input('\33[0;49;34mQual forma de pagamento\33[0m? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em \33[0;49;93m2\33[0m x de R$\33[0;49;92m{:.2f}\33[0m reais \33[0;49;92m'
          'SEM JUROS\33[0m'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcela = int(input('\33[0;49;34mQuantas parcelas\33[0m? '))
    parcela = total / totalParcela
    print('Sua compra parcelada em \33[0;49;33m{}X\33[0m vai custar \33[0;49;31m{:.2f}\33[0m com JUROS'
          .format(totalParcela, parcela))
    print('Sua compra de R$\33[0;49;92m{:.2f}\33[0m vai custar R$\33[0;49;92m{:.2f}\33[0m no final'
          .format(preco, total))
else:
    total = preco
    print('\33[0;49;31mOPÇÃO INVALIDA\33[0m! tente novamente')
