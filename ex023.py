#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite qualqur numero inteiro de 0 a 9999: '))
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10
print('A casa do milhar é {} \n centena é {} \n dezena é {} \n e unidade é {}'.format(milhar, centena, dezena, unidade))

# o modulo (%) divide o numero e mostra o restante. Nesse processo ex.: pregamos os numero 1234, dividimos inteiro por
# 10, resultando em 123, ai fazemos o modulo de 10, a funcao vai dividir inteiramente por 10 e mostrar o resto, ou seja,
# pegara o 123/10 = 12, sobrando 3. Nesse caso a dezena é 3.