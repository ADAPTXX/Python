a = 10
b = 5

# User iteraction
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o seguindo valor: '))
print(type(a))
print(type(b))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print('soma: {}'.format(soma)) # like strFmt
resultado =('Soma: {soma} \nSubtração: {sub}'
      '\nMultiplicação: {mult}'
      '\nDivisão: {divisao}'
      '\nResto: {resto}'
      .format(soma=soma,
              sub=subtracao,
              mult=multiplicacao,
              divisao=divisao,
              resto=resto)) # like strFmt and alias in soma= sub= \n = enter
print(resultado)
print(type(soma))
soma = str(soma)
print(type(soma))

#print('soma: ' + soma)
print('soma:' + soma)
print(subtracao)
print(multiplicacao)
print(type(divisao)) # busca o tipo específico
print(int(divisao)) # função de casting
print(resto)

# x = '1'
# soma2 = int(x) + 1
# print(soma2)
# CTRL + Barra invertida comenta bloco





