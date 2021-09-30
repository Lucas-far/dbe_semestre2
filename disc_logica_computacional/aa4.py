

from sys import getsizeof as _


# RESPOSTA: E
def pergunta_1():
    """
    1) Na tabela estão apresentadas algumas operações. Observe atentamente cada uma delas.

          A    B    A    (A B)
    L1    F    F         V
    L2    V    V    F
    L3         F    F    F
    L4    F         V    F

    Assinale a alternativa que completa corretamente o resultado de cada linha.

    a) L1 - V; L2 – F; L3 – F; L4 – V
    b) L1 - F; L2 – F; L3 – F; L4 - V
    c) L1 - V; L2 – F; L3 – F; L4 - F
    d) L1 - F; L2 – V; L3 – F; L4 - F
    e) L1 - V; L2 – V; L3 – V; L4 - V **********************************************************************************
    """


# RESPOSTA: D
def pergunta_2():
    """
    2) O conectivo lógico da _________ é utilizado quando desejamos obter um resultado falso, se e somente se, as duas
       proposições forem falsas. Do mesmo modo, o conectivo lógico da _________ é utilizado quando desejamos obter um
       resultado verdadeiro, se e somente se, as duas forem verdadeiras. E, por fim, o conectivo lógico da _________
       é utilizado quando desejamos inverter um resultado.

    Assinale a alternativa que completa corretamente as lacunas da frase.

    a) disjunção, negação e conjunção
    b) conjunção, disjunção e negação
    c) negação, disjunção e conjunção
    d) disjunção, conjunção e negação **********************************************************************************
    e) conjunção, negação e disjunção
    """


# RESPOSTA: B
def pergunta_3():
    """
    3) Considere os conectivos lógicos de conjunção, disjunção e negação. Além disso, considere também o valor lógico de
       uma proposição P como falso e o valor lógico de uma proposição Q como verdadeira. Julgue as afirmativas a seguir
       em (C) Corretas ou (I) Incorretas.

    (I) a disjunção entre as duas é falsa.                                                       [ P v Q    F v V    V ]
    (  ) a negação de P operado com a conjunção de Q é verdadeira.
    (I) a conjunção entre as duas é verdadeira                                                  [ P ^ Q    F ^ V    F ]
    (  ) a negação de Q operado com a disjunção de P é verdadeira
    (C) a disjunção entre as duas é verdadeira                                                   [ P v Q    F v V    V ]

    Assinale a alternativa que apresenta a sequência CORRETA.

    a) I C I I I
    b) I C I I C *******************************************************************************************************
    c) I I C I C
    d) C I C C I
    e) C C C I I
    """


# RESPOSTA: D
def pergunta_4():
    """
    4) A Tabela Verdade é utilizada como um método exaustivo de extração de resultados (SILVA, FINGER, MELO, 2017). Em
       outras palavras, construímos uma Tabela Verdade para testarmos todos os resultados possíveis para uma combinação
       de entradas em uma determinada fórmula.

    Faça associações das proposições na Coluna A com os seus respectivos significados, apresentados na Coluna B.

    Coluna A
    I   - Tautologia   || 1. É quando o resultado de uma fórmula obtém somente F como respostas.
    II  - Condicional  || 2. Quando uma Tabela Verdade não é uma tautologia e não é uma contradição.
    III - Contingência || 3. É uma proposição que independentemente das entradas, todas as respostas são verdadeiras.
    IV  - Contradição  || 4. Dada uma sequência de proposições, a partir da operação condicional é possível chegar a uma
                             conclusão (um resultado) que é uma nova proposição.

    Assinale a alternativa que apresenta a associação CORRETA entre as colunas.

    a) I - 3; II - 2; III - 4; IV - 1.
    b) I - 2; II - 1; III - 4; IV - 3.
    c) I - 4; II - 1; III - 2; IV - 3.
    d) I - 3; II - 4; III - 2; IV - 1. *********************************************************************************
    e) I - 1; II - 3; III - 2; IV - 4.
    """


if __name__ == '__main':
    print(_(pergunta_1()))
