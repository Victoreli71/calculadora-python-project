#FUNÇÃO DA OPERAÇÃO ESCOLHIDA E O QUE IRÁ FAZER 
def operacao_total(operacao_sinal, valor, valor2):
    if operacao_sinal == "+" :
       resultado =  valor + valor2
    elif operacao_sinal == "-" :
        resultado = valor - valor2
    elif operacao_sinal == "*" :
        resultado = (valor * valor2)
    elif operacao_sinal == "/" :
        resultado = (valor / valor2)
    else :
        print ("não se encaixa nos parametros")
      
    return resultado
#PEDINDO PARA O USUÁRIO DIGITAR 2 NUMEROS 
valor = float(input("digite o valor 1 :"))
valor2 = float(input("digite o valor 2 :"))
operacao_sinal =str(input("digite qual conta que voce quer realizar : "))
#PRINT PARA EXIBIR O RESULTADO DA FUNCTION DE OPERAÇÕES
resul = operacao_total(operacao_sinal, valor, valor2)
print(f'resultado é {resul}')
