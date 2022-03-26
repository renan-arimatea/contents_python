"""
O que são Variáveis?
- São um modo de rotular ou nomear todos os dados pertencentes ao seu programa

O que são dados?
- São todas as informações que serão utilizadas ao longo do seu código. Podendo ser números, palavras, frases, textos, entre outros.

Existem 2 tipos de variáveis:
- Variável Global: São variáveis que podem ser manipuladas ao longo de todo código.
- Variável Local: São variáveis que podem ser manipuladas apenas em uma determinada parte do programa.

como declarar variáveis?
 nome = dado
    Ex:
    idadeSilvioSantos = 85
    a = 85

É necessário algumas regras para nomear suas variáveis:
- Em nomes compostos devemos separar por underline ou camelCase
    Ex: idade_joao = 17
        idadeJoao = 17
        IDADE_JOAO  = 17

- Variáveis não devem possuir nenhum tipo de caracter especial (%, acento, ç, dentre outros).
    Ex:
        Modo certo:
        fracao = 100
        Modo Errado:
        fração = 100

- Variáveis não devem possuir apenas números em seu nome.
    Ex:
        Modo errado:
        123 = 17 # Irá acusar erro
        Modo Certo:
        a123 = 17
        OBS: Ao utilizar numeros na nomeclatura de variaveis devem sempre vir no minimo uma letra antes dos numeros.

Tipos de Dados:

- Inteiros: Não possui casas decimais.
    Ex:
        idadeJoao = 17
        print(type(idadeJoao)) # Para utilizar a função type faça: type(nome da variavel).

- Flutuantes (float) = Números que possuem casas decimais. UTLIZA-SE PONTO (.) PARA SEPARAR OS NÚMEROS
    Ex:
        precoBanana = 5.59
        print(type(precoBanana))

- Complexo: Se um dado possuir a letra j é um número complexo, lembrando que precisa haver um número junto a ele.
    Ex:
        num_complexo = 1j
        print(type(num_complexo))

-Boolean: O valor 1  representa treu (Verdadeiro), enquanto o valor 0  representa False (Falso)
    Ex:
        var_bool = True
        print(type(var_bool))

- String: Todos os dados que estão entre aspas simples '', aspas duplas "" ou aspas simples triplas '''
    - Podem conter numeros e letras dentro dela.
    - Para inverter o conteudo presente na string basta adicionar [::-1]
    Ex:
        var_string = '12345'
        print(type(var_string))

        var_string = "Tom cruise"
        print(type(var_string))

        var_string = '''Tom cruise'''
        print(type(var_string))

        var_string = 'Tom cruise'
        print(var_string[::-1])

        # Tom Cruise
        # 0123456789

        var_string = 'Tom cruise'
        print(var_string[4:10]) # Estou pegando a posição 4(c) até a posição 9(e)

        var_String = "turquia god of war"
        print(var_String[6:13]) # Estou pegando a posição 6(a) até a posição 12(o)

- Por fim, é possível declarar varias variaveis dentro de uma mesma linha.
    Ex:
        a1,a2,a3,a4,a5 = 1,2.5,True,2j,'sim'
    - Caso haja mais dados ou variaveis em algum dos lados irá dar erro.
"""

idadeSilvioSantos = 85
a = 85

idade_joao = 17
idadeJoao = 17
IDADE_JOAO = 17

fracao = 100

a123 = 17

idadeJoao = 17
print(type(idadeJoao)) # Para utilizar a função type faça: type(nome da variavel).

precoBanana = 5.59
print(type(precoBanana))

num_complexo = 1j
print(type(num_complexo))

var_bool = True
print(type(var_bool))

var_string = '12345'
print(type(var_string))

var_string = "Tom cruise"
print(type(var_string))

var_string = '''Tom cruise'''
print(type(var_string))

var_string = 'Tom cruise'
print(var_string[::-1])

var_string = 'Tom cruise'
print(var_string[4:10]) # Estou pegando a posição 4(c) até a posição 9(e)

var_String = "turquia god of war"
print(var_String[6:13]) # Estou pegando a posição 6(a) até a posição 12(o)

a1,a2,a3,a4,a5 = 1,2.5,True,2j,'sim'
