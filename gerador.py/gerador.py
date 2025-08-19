import random


# Lista de símbolos possíveis
simbolos = '!@#$%^&*()-_=+[]{};:,.<>?/|\\'

# Solicita ao usuário a quantidade de símbolos
quantidade = int(input("Quantos símbolos aleatórios você quer? "))

# Gera os símbolos aleatórios
simbolos_aleatorios = ''.join(random.choices(simbolos, k=quantidade))


 # Gera letras maiúsculas aleatórias
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_maiusculas_aleatorias = ''.join(random.choices(letras_maiusculas, k=quantidade))

# Gera letras minúsculas aleatórias
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_minusculas_aleatorias = ''.join(random.choices(letras_minusculas, k=quantidade))

# Gera a senha final
senha = ''.join(random.choices(letras_maiusculas + letras_minusculas + simbolos, k=quantidade))
print("Senha gerada:", senha)


#builde by DEV_daniel