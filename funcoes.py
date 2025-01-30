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

def potencia(base, expo = 2):
    return base**expo


"""
Defina uma função chamada potencia que calcula a potência de um número elevado a uma potência especificada. 
Forneça uma documentação que explique como usar a função e inclua exemplos de uso.
"""

def 
