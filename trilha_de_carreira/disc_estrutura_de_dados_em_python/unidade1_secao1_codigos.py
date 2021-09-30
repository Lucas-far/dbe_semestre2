

def codigo_1():
    """
    texto = "Aprendendo Python na disciplina de linguagem de programação."

    print(f"Tamanho do texto = {len(texto)}")
    print(f"Python in texto = {'Python' in texto}")
    print(f"Quantidade de y no texto = {texto.count('y')}")
    print(f"As 5 primeiras letras são: {texto[0:6]}")
    """


def codigo_2():
    """
    texto = "Aprendendo Python na disciplina de linguagem de programação."

    print(texto.upper())
    print(texto.replace("i", 'XX'))
    """


def codigo_3():
    """
    texto = "Aprendendo Python na disciplina de linguagem de programação."
    print(f"texto = {texto}")
    print(f"Tamanho do texto = {len(texto)}\n")

    palavras = texto.split()
    print(f"palavras = {palavras}")
    print(f"Tamanho de palavras = {len(palavras)}")
    """


def codigo_4():
    """
    texto = '''Operadores de String
    Python oferece operadores para processar texto (ou seja, valores de string).
    Assim como os números, as strings podem ser comparadas usando operadores de comparação:
    ==, !=, <, > e assim por diante.
    O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
    '''

    print(f"Tamanho do texto = {len(texto)}")
    texto = texto.lower()
    texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")
    lista_palavras = texto.split()
    print(f"Tamanho da lista de palavras = {len(lista_palavras)}")

    total = lista_palavras.count("string") + lista_palavras.count("strings")

    print(f"Quantidade de vezes que string ou strings aparecem = {total}")
    """


def codigo_5():
    """
    vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

    for vogal in vogais:
        print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')
    """


def codigo_6():
    """
    # Mesmo resultado.

    vogais = []
    print(f"Tipo do objeto vogais = {type(vogais)}")

    vogais.append('a')
    vogais.append('e')
    vogais.append('i')
    vogais.append('o')
    vogais.append('u')

    for p, x in enumerate(vogais):
        print(f"Posição = {p}, valor = {x}")
    """


def codigo_7():
    """
    frutas = ["maça", "banana", "uva", "mamão", "maça"]
    notas = [8.7, 5.2, 10, 3.5]

    print("maça" in frutas) # True
    print("abacate" in frutas) # False
    print("abacate" not in frutas) # True
    print(min(frutas)) # banana
    print(max(notas)) # 10
    print(frutas.count("maça")) # 2
    print(frutas + notas)
    print(2 * frutas)
    """


def codigo_8():
    """
    lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]

    print(f"Tamanho da lista = {len(lista)}")

    for i, item in enumerate(lista):
        print(f"Posição = {i},\t valor = {item} -----------------> tipo individual = {type(item)}")

    print("\nExemplos de slices:\n")

    print("lista[1] = ", lista[1])
    print("lista[0:2] = ", lista[0:2])
    print("lista[:2] = ", lista[:2])
    print("lista[3:5] = ", lista[3:5])
    print("lista[3:6] = ", lista[3:6])
    print("lista[3:] = ", lista[3:])
    print("lista[-2] = ", lista[-2])
    print("lista[-1] = ", lista[-1])
    print("lista[4][1] = ", lista[4][1])
    """


def codigo_9():
    """
    linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
    #linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # Essa sintaxe produz o mesmo resultado que a linha 1

    print("Antes da listcomp = ", linguagens)

    linguagens = [item.lower() for item in linguagens]

    print("\nDepois da listcomp = ", linguagens)
    """


def codigo_10():
    """
    linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
    print("Antes da listcomp = ", linguagens)

    for i, item in enumerate(linguagens):
        linguagens[i] = item.lower()

    print("\nDepois da listcomp = ", linguagens)
    """


def codigo_11():
    """
    linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

    linguagens_java = [item for item in linguagens if "Java" in item]

    print(linguagens_java)
    """


def codigo_12():
    """
    linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
    linguagens_java = []

    for item in linguagens:
        if "Java" in item:
            linguagens_java.append(item)

    print(linguagens_java)
    """


def codigo_13():
    """
    # Exemplo 1
    print("Exemplo 1")
    linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

    nova_lista = map(lambda x: x.lower(), linguagens)
    print(f"A nova lista é = {nova_lista}\n")

    nova_lista = list(nova_lista)
    print(f"Agora sim, a nova lista é = {nova_lista}")


    # Exemplo 2
    print("\n\nExemplo 2")
    numeros = [0, 1, 2, 3, 4, 5]

    quadrados = list(map(lambda x: x*x, numeros))
    print(f"Lista com o número elevado a ele mesmo = {quadrados}\n")
    """


def codigo_14():
    """
    numeros  = list(range(0, 21))

    numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

    print(numeros_pares)
    """


def codigo_15():
    """
    vogais = ('a', 'e', 'i', 'o', 'u')
    print(f"Tipo do objeto vogais = {type(vogais)}")

    for p, x in enumerate(vogais):
        print(f"Posição = {p}, valor = {x}")
    """


def codigo_16():
    """
    vogais = ()

    vogais.append('a')
    """


def codigo_17():
    """
    vogais = ('a', 'e', 'i', 'o', 'u')

    for item in enumerate(vogais):
        print(item)

    # print(tuple(enumerate(vogais)))
    # print(list(enumerate(vogais)))
    """


def codigo_18():
    """
    vogais_1 = {'aeiou'} # sem uso do construtor
    print(type(vogais_1), vogais_1)

    vogais_2 = set('aeiouaaaaaa') # construtor com string
    print(type(vogais_2), vogais_2)

    vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
    print(type(vogais_3), vogais_3)

    vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
    print(type(vogais_4), vogais_4)

    print(set('banana'))
    """


def codigo_19():
    """
    def create_report():
        componentes_verificados = set(['caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub', 'impressora', 'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'])
        componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])

        qtde_componentes_verificados = len(componentes_verificados)
        qtde_componentes_com_defeito = len(componentes_com_defeito)

        componentes_ok = componentes_verificados.difference(componentes_com_defeito)

        print(f"Foram verificados {qtde_componentes_verificados} componentes.\n")
        print(f"{qtde_componentes_com_defeito} componentes apresentaram defeito.\n")

        print("Os componentes que podem ser vendidos são:")
        for item in componentes_ok:
            print(item)


    create_report()
    """


def codigo_20():
    """
    # Exemplo 1 - Criação de dicionário vazio, com atribuição posterior de chave e valor
    dici_1 = {}
    dici_1['nome'] = "João"
    dici_1['idade'] = 30

    # Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor
    dici_2 = {'nome': 'João', 'idade': 30}

    # Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor
    dici_3 = dict([('nome', "João"), ('idade', 30)])

    # Exemplo 4 - Criação de dicionário com a função built-in zip() e duas listas, uma com as chaves, outra com os valores.
    dici_4 = dict(zip(['nome', 'idade'], ["João", 30]))


    print(dici_1 == dici_2 == dici_3 == dici_4) # Testando se as diferentes construções resultamo em objetos iguais.
    """


def codigo_21():
    """
    cadastro = {
            'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
            'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
            'idade' : [25, 33, 37, 18]
            }

    print("len(cadastro) = ", len(cadastro))

    print("\n cadastro.keys() = \n", cadastro.keys())
    print("\n cadastro.values() = \n", cadastro.values())
    print("\n cadastro.items() = \n", cadastro.items())

    print("\n cadastro['nome'] = ", cadastro['nome'])
    print("\n cadastro['nome'][2] = ", cadastro['nome'][2])
    print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])
    """


def codigo_22():
    """
    print(len(cadastro['nome']))
    print(len(cadastro['cidade']))
    print(len(cadastro['idade']))

    qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])

    print(f"\n\nQuantidade de elementos no dicionário = {qtde_itens}")
    """


def codigo_23():
    """
    import numpy

    matriz_1_1 = numpy.array([1, 2, 3]) # Cria matriz 1 linha e 1 coluna
    matriz_2_2 = numpy.array([[1, 2], [3, 4]]) # Cria matriz 2 linhas e 2 colunas
    matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) # Cria matriz 3 linhas e 2 colunas
    matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]]) # Cria matriz 2 linhas e 3 colunas

    print(type(matriz_1_1))

    print('\n matriz_1_1 = ', matriz_1_1)
    print('\n matriz_2_2 = \n', matriz_2_2)
    print('\n matriz_3_2 = \n', matriz_3_2)
    print('\n matriz_2_3 = \n', matriz_2_3)
    """


def codigo_24():
    """
    m1 = numpy.zeros((3, 3)) # Cria matriz 3 x 3 somente com zero
    m2 = numpy.ones((2,2)) # Cria matriz 2 x 2 somente com um
    m3 = numpy.eye(4) # Cria matriz 4 x 4 identidade
    m4 = numpy.random.randint(low=0, high=100, size=10).reshape(2, 5) # Cria matriz 2 X 5 com números inteiros

    print('\n numpy.zeros((3, 3)) = \n', numpy.zeros((3, 3)))
    print('\n numpy.ones((2,2)) = \n', numpy.ones((2,2)))
    print('\n numpy.eye(4) = \n', numpy.eye(4))
    print('\n m4 = \n', m4)

    print(f"Soma dos valores em m4 = {m4.sum()}")
    print(f"Valor mínimo em m4 = {m4.min()}")
    print(f"Valor máximo em m4 = {m4.max()}")
    print(f"Média dos valores em m4 = {m4.mean()}")
    """
