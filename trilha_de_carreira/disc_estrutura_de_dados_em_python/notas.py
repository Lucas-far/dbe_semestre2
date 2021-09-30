
from random import choice
from time import sleep


def ink(label: str):

    x: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[1:37m',
        '\033[1:38m',
    )

    return f"{choice(x)}{label}{x[-1]}"


simbolo_ponto = '•'
autor = 'Vanessa Cadan Scheffer'

secao_1 = f"""
    [ item 1 ] ------------------------------------------- Python (detalhe) -------------------------------------------
        •  Um programa Python é representado por objetos ou pela relação entre objetos, ou seja, tudo é um objeto;
    
    [ item 2 ] ------------------------------------------ Python (detalhe 2) ------------------------------------------
        • O objeto do tipo (int) possui limite determinado ao espaço disponível na memória RAM;
    
    [ item 3 ] ------------------------------------ Estruturas de dados (conceito) ------------------------------------
        • Objetos que armazenam mais de um valor dentro de si, e sua escolha varia de acordo com o tipo do problema;
    
    [ item 4 ] --------------------------------- Estruturas de dados (objetos) (tipos) ---------------------------------
        • Array NumPy    • Mapping (dict)   • Set (set)    • Sequência (str, list, tuple); 
    
    [ item 5 ] ------------------------- Estruturas de dados (objetos) (sequência) (operações) -------------------------
        • [ + ] [ * ] [int] [int:int] [int:int:int] [ in ] [ len() ] [ min() ] [ max() ] [ count() ]
        • Estr. de dados que armazenam + de 1 valor e representam seq. finitas indexadas por números não negativos;
         
    [ item 6 ] ------------------------------------------------- FONTE -------------------------------------------------
        • PERKOVIC, Ljubomir. Introdução à computação usando Python: um foco no desenvolvimento de aplicações. RJ: LTC,
          2016;
    
    [ item 7 ] ------------------------------- Estruturas de dados (sequência) (String) -------------------------------
        • Tipo de sequência cujos objetos não podem ter um novo valor atribuido numa posição específica
        • NÃO PERMITIDO    var = 'Lucas'    var[2] = 'v'
        • PERMITIDO        var = 'Lucas'    var.replace(var[2], 'v');
        
    [ item 8 ] -------------------------------- Estruturas de dados (sequência) (Lista) --------------------------------
        • Tipo de sequência cujos objetos são mutáveis
        • Construção: lista vazia, lista com vírgulas separadoras, list comprehension, contrutor
        • Características: suporta várias classes de dados, fatiamento proveitoso; 
    
    [ item 9 ] ---------------------------- Estrutura de dados (Lista) (List comprehension) ----------------------------
        • Forma pythônica de criar uma lista com base em um objeto iterável, ou escrever um  loop for
        • Utilizada quando deseja-se criar uma nova sequência a partir de uma já existente, porém com alguma alteração,
          por exemplo, filtragem;
    
    [ item 10 ] ---------------------------- Estruturas de dados (Lista) (funções built-in) ----------------------------
        • map() = Utilizada para transformar cada item de um objeto iterável
                  Sua sintaxe requer dois parâmetros: a função e o objeto iterável 
                  A visualização do seu resultado requer o uso de construtor, convertendo o objeto para um iterável
                  Construtores: dict() list() set() tuple()  
                  EX: var = list(range(1, 11))
                      print(list(map(lambda def_: not def_ % 2, var)))
                      [False, True, False, True, False, True, False, True, False, True]
        
        • filter = Utilizada para filtrar cada item de um objeto iterável
                   Sua sintaxe requer dois parâmetros: a função e o objeto iterável 
                   A visualização do seu resultado requer o uso de construtor, convertendo o objeto para um iterável
                   Construtores: dict() list() set() tuple() 
                   EX: var = list(range(1, 11))
                       print(list(filter(lambda def_: not def_ % 2, var)))
                       [2, 4, 6, 8, 10];
    
    [ item 11 ] ------------------------------- Estruturas de dados (Sequência) (Tupla) -------------------------------
        • Tipo de sequência cujos objetos são imutáveis
        • Tupla vazia [ () ou dado, ]    • Parênteses [ (dado,) ]    • Construtor [ tuple() ];
   
   [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •
    """.split(';')

secao_2 = f"""
    [ item 1 ] -  -
        •
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •
    """.split(';')

secao_3 = f"""
    [ item 1 ] -  -
        •
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •
    """.split(';')

secao_4 = f"""
    [ item 1 ] -  -
        •
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •
    """.split(';')

if __name__ == '__main__':

    s1 = 'Seção 1 - A linguagem Python'

    parada = """
    Observe o codigo a seguir, no qual criamos uma tupla chamada de "vogais" e, por meio da estrutura de repetição,
    imprimos cada elemento da tupla. Usamos, ainda, uma variável auxiliar p para indicar a posição que o elemento ocupa
    na tupla.
    """
