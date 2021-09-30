

from sys import getsizeof as _


# RESPOSTA: B
def pergunta_1():
    """
    1) Segundo Manzano(2019), na construção de algoritmos, os condicionais são amplamente utilizados. “Do ponto de vista
       computacional, uma condição é uma expressão booleana cujo resultado é um valor lógico falso ou verdadeiro".

    Uma expressão booleana como condição é conseguida a partir de:

    a) apenas proposições.
    b) uma relação lógica entre dois elementos e um operador relacional. **********************************************
    c) apenas de proposições dedutivas.
    d) conectivos lógicos e perguntas.
    e) proposições booleanas.
    """


# RESPOSTA: B
def pergunta_2():
    """
    2) As proposições podem ser simples ou compostas. Ela será simples quando existir uma única afirmação na frase; e
       composta, quando existir, ao menos, duas proposições simples interligadas.

    Nesse sentido, analise as afirmativas, a seguir:

    I.   Palavras usadas para separar proposições simples são chamados de conectivos lógicos. (F)
    II.  São conectivos lógicos: E, OU, NÃO, SE...ENTÃO, SE, E SOMENTE SE. (V)
    III. O conectivo lógico E é usado na operação lógica de disjunção. (F)
    IV.  O conectivo lógico OU é representado pelo símbolo v. (V)

    É correto o que se afirma em:

    a) I
    b) II e IV *********************************************************************************************************
    c) II
    d) I e III
    e) III e IV
    """


# RESPOSTA: C
def pergunta_3():
    """
    3) Um argumento é elaborado através das proposições, buscando sempre uma conclusão que seja sustentada por uma ou
       mais premissas. Portanto, argumentar significa garantir uma conclusão verdadeira, baseada em premissas
       verdadeiras. Nesse sentido, analise a frase, a seguir:

    Os carros fabricados no Brasil são taxados de impostos, que são caros. Logo, se o imposto é caro, os carros
    brasileiros também são.

    Assinale a alternativa que contém a afirmação correta:

    a) A frase é um argumento composto por duas premissas e duas conclusões.
    b) A frase é um argumento composto por uma premissa e uma conclusão.
    c) A frase é um argumento composto por duas premissas e uma conclusão. ********************************************
    d) A frase é um argumento composto por uma premissa e duas conclusões.
    e) A frase não é um argumento.
    """


# RESPOSTA: A
def pergunta_4():
    """
    4) O cálculo proposicional ajuda a validar argumentos através da utilização de proposições. As proposições podem ser
       simples ou compostas. As proposições compostas são formadas por um encadeamento de proposições simples, unidas
       por conectivos lógicos. Na tabela 1, a seguir, são relacionados alguns conectivos e suas funções:

    Tabela 1 – Conectivos lógicos

    Operador lógico    Definição              Conectivo de
    A. ()              1. Não                 a. Disjunção
    B. v               2. Se...então          b. Bicondicional
    C. <--             3. E                   c. Negação
    D. ()              4. Se, e somente se    d. Conjunção
    E. ()              5. Ou                  e. Condicional

    a) A-3-d || B-5-a || C-1-c || D-2-e || E-4-b. **********************************************************************
    b) A-1-c || B-3-e || C-5-b || D-2-a || E-4-d.
    c) A-5-e || B-1-d || C-2-c || D-4-b || E-3-a.
    d) A-4-d || B-2-c || C-5-a || D-3-e || E-1-b.
    e) A-2-e || B-4-a || C-1-d || D-5-b || E-3-c.
    """


if __name__ == '__main':
    print(_(pergunta_1()))
