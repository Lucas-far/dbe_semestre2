

from sys import getsizeof as _


# RESPOSTA: D
def pergunta_1():
    """
    1) Um problema recorrente envolvendo subconjuntos diz respeito à determinação do número de subconjuntos de um
       determinado conjunto. Deste modo, há um teorema para contabilizar o número de subconjuntos de um conjunto
       qualquer, conhecendo-se a sua cardinalidade.

    Seja A um conjunto com cardinalidade igual a 8. Quantos subconjuntos de A poderiam ser contabilizados? Assinale a
    alternativa que apresenta o número correto de subconjuntos de A.

    a) 1024
    b) 2048
    c) 1025
    d) 256 *************************************************************************************************************
    e) 121

    CÁLCULO = 2 elevado a n    2 ** 8    256
    """


# RESPOSTA: E
def pergunta_2():
    """
    2) Usualmente, um conjunto é descrito pelas suas propriedades. Por exemplo, se o conjunto é de números pares
       positivos, ao invés de escrever {2, 4, 6, 8, 10, 12...}, podemos representar esse conjunto como {X E oval N; 2X}.

       Assinale a alternativa que apresenta o conjunto definido por C = {X E oval Z; -2 <= x < 8}

    a) C = {-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8}
    b) C = {-2, 8}
    c) C = {0, 1, 2, 3, 4, 5, 6, 7}
    d) C = {-2, 0, 2, 4, 6}
    e) C = {-2, -1, 0, 1, 2, 3, 4, 5, 6, 7} ****************************************************************************
    """


# RESPOSTA: C
def pergunta_3():
    """
    3) Na teoria dos conjuntos, há notações específicas para denotar a relação entre dois conjuntos. Para que qualquer
       pessoa tenha um entendimento correto, é necessário ter o domínio do uso das notações.

    Considere os conjuntos M = {x E oval Z; x = 5n, n E oval N} e N = {x E oval N; x = 10n, n E oval N}. Pode-se
    verificar que M e N possuem uma relação entre si.

    Assinale a alternativa que apresenta a relação existente entre M e N.

    a) N E oval M
    b) M E oval corte N
    c) N C sublinhado M ************************************************************************************************
    d) M C oval N
    e) N E espelhado M
    """


# RESPOSTA: B
def pergunta_4():
    """
    4) Mesmo não conhecendo quais são os elementos dos conjuntos, se souber a cardinalidade da união, interseção ou de
       um conjunto, pode-se calcular a cardinalidade deo conjunto desconhecido.

    Considere o seguinte: Sejam os conjuntos A e B tal que |A| = 20, |A n B| = 12 e |A ? invertido B| = 60

    Assinale a alternativa com o valor correto de |B|.

    a) 43
    b) 52 **************************************************************************************************************
    c) 34
    d) 79
    e) 12

    • CÁLCULO: |A ∪ B| = |A| + |B| − |A ∩ B|    60 = 20 + |B| - 12    60 - 20 + 12 = |B|    |B| = 52
    """


if __name__ == '__main':
    print(_(pergunta_1()))
