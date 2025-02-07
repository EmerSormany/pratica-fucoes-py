"""
Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, [nome]!".
"""

def saudacao (nome: str):
    return f"Olá, {nome}!"

"""
Crie uma função dobro que aceita um número como argumento e retorna o dobro desse número.
"""

def dobro(num):
    return num*2

"""
Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos. 
O idioma é opcional e padrão para "inglês". 
A função deve retornar uma saudação no idioma especificado.
"""

def saudacao_personalizada(nome, idioma = "inglês"):
    if idioma == "inglês":
        return f"Hello, {nome}!"
    elif idioma == "espanhol":
        return f"Hola, {nome}!"
    else:
        return f"Bonjour, {nome}!"


"""
Escreva uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) e retorna a base elevada ao expoente


"""
"""
Defina uma função chamada potencia que calcula a potência de um número elevado a uma potência especificada. 
Forneça uma documentação que explique como usar a função e inclua exemplos de uso.
"""

def potencia(base, expo = 2): 
    """
    Calcula um número elevado a uma potência. Usa 2 parâmetros 'base' e 'expo'. 
    O primeiro parâmetro é a base e o segundo parâmetro é o valor da potência.
    Se não for passado valor para o segundo parâmetro, ele será usado com valor 2 e o número de base será elevado ao quadrado.
    Ex.: potencia(2) retornará 4.
    potencia(2, 3) retornará 8.
    """
    return base**expo


"""
Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150.
"""
def idade_valida(idade):
    if idade - int(idade) == 0:
        if idade >= 0 and idade <=150:
            return True
        else:
            return False
    else:
        return False

"""
Implemente uma função validar_email que verifica se uma string fornecida como argumento representa um endereço de e-mail válido. 
Considere que um email válido não deve ter espaços, deve conter 01 arroba e terminar com .com
"""

import re

def validar_email(email):
    if email.find('@') == -1:
        return False   

    if email[-4:] != '.com':
        return False

    t = re.compile(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$')
    resultado = t.match(email)

    print(resultado)
    
    if len(email.split(' ')) > 1:
        return False
    
    return True

print(validar_email('invalido@.com'))