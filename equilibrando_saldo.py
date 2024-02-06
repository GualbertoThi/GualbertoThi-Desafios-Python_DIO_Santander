saldo_atual = float(input("Informe o saldo atual:"))
valor_deposito = float(input("Informe o valor do depósito:"))
valor_retirada = float(input("Informe o valor da retirada:"))

saldo_atualizado = saldo_atual + valor_deposito - valor_retirada

print ("O seu saldo atualizado é de " , saldo_atualizado)