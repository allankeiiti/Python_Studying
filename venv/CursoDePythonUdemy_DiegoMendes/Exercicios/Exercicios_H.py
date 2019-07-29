'''
Ex:1
Crie um script para aprovar um empréstimo bancário. Devemos perguntar para o usuário: o valor do imovel; salario;
em quantos anos será realizado o pagamento
Então devemos calcular a prestação mensal, sabendo que ela não pode ser maior que 30% do salário, que neste caso, o
empréstimo não será aprovado


estateValue = float(input('\033[0;20;41mDigite o valor do imóvel: \033[m'))
payment = float(input('Digite o salário: '))
yearsForPay = int(input('Digite em quantos anos sera realizado o pagamento: '))

#CALCULANDO PRESTAÇÃO MENSAL
monthPrice = estateValue/int((yearsForPay*12))
if (payment*0.3) > monthPrice:
    print('Pagamento mensal: {:.2f}.'.format(monthPrice))
    print('Empréstimo aprovado')
else:
    print('Pagamento mensal: {:.2f}.'.format(monthPrice))
    print('Empréstimo reprovado')
'''
