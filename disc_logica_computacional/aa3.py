

from sys import getsizeof as _


# RESPOSTA: A
def pergunta_1():
    """
    1) Proposição é uma sentença declarativa que pode ser classificada como verdadeira ou falsa, jamais ambas ao mesmo
       tempo. Ou seja, não pode haver dúvida quanto à classificação da sentença. Também podemos dizer que trata-se de
       uma classificação binária, pois só existem dois resultados possíveis: V ou F, ou ainda 1 ou 0.

    Uma premissa é um ponto ou ideia de que se parte para armar um raciocínio.

    Exemplo de Premissas:

    - Maria é inteligente.    - Maria não estudar muito.    - Todos os alunos inteligentes ou estudiosos são aprovados.

    Com base no exemplo de Premissas acima e usando a Lógica Proposicional, podemos chegar a seguinte conclusão

    a) Maria será aprovada. ********************************************************************************************
    b) Maria não será aprovada.
    c) Maria é inteligente.
    d) Maria é estudante.
    e) Maria é inteligente sem estudar.
    """


# RESPOSTA: E
def pergunta_2():
    """
    2) No estudo da lógica, além de distinguir se uma frase é ou não um argumento, também é importante distinguirmos se
       uma sentença pode ou não ser classificada como verdadeira ou falsa (não ambas ao mesmo tempo).

    Aponte qual frase não pode ser classificada (valorada) em verdadeira (V) ou falso (F):

    a) O Paraguai é um pais da América Latina.
    b) Mato Grosso é uma Cidade do Brasil.
    c) São Paulo é a capital do Brasil.
    d) Cinco mais um é igual a sete.
    e) Que show! *******************************************************************************************************
    """


# RESPOSTA: A
def pergunta_3():
    """
    3) Proposição é uma sentença declarativa que pode ser classificada como verdadeira ou falsa, jamais ambas ao mesmo
       tempo. Ou seja, não pode haver dúvida quanto à classificação da sentença.

    De acordo com as informações apresentadas na tabela a seguir, faça a associação dos três princípios básicos de uma
    proposição contidos na COLUNA A com seus respectivos significados contidos na COLUNA B.

    COLUNA A
    I.   Princípio da Identidade
    II.  Princípio da Não Contradição
    III. Princípio do Terceiro excluído

    COLUNA B
    1. Toda proposição ou é verdadeira ou é falsa, não existindo um terceiro valor que ela possa assumir. Sendo P uma
       proposição tem-se: P ou não P.
    2. Toda proposição é idêntica a si mesma. Ou seja, sendo P uma proposição: P é P
    3. Uma proposição não pode ser verdadeira e falsa ao mesmo tempo. Sendo P uma proposição tem-se: não (P e não P).

    a) I - 2, II - 3, III - 1. *****************************************************************************************
    b) I - 2, II - 1, III - 3.
    c) I - 3, II - 2, III - 1.
    d) I - 3, II - 1, III - 2.
    e) I - 1, II - 2, III - 3.
    """


# RESPOSTA: B
def pergunta_4():
    """
    4) Uma proposição composta pode ser criada fazendo a conjunção de duas proposições simples, nesse caso, são
       utilizadas as palavras “e”, “mas”, “no entanto”, dentre outras para fazer a conexão. Também podemos criar uma
       proposição composta fazendo a disjunção de duas proposições simples, nesse caso, usamos a palavra “ou” para a
       conexão. A disjunção possui uma particularidade, ela pode ser inclusiva ou exclusiva.

    Considere o contexto e avalie as seguintes proposições:

    I.   Rodrigo é estudante ou é trabalhador. Essa é uma proposição inclusiva. (V)
    II.  Maria é Paulista ou é Carioca. Essa é uma proposição inclusiva. (F)
    III. Felipe é gordo ou é magro. Essa é uma proposição exclusiva. (V)
    IV.  Arthur é baixo ou é alto. Essa é uma proposição exclusiva. (V)

    Agora, assinale a alternativa que apresenta a correta:

    (F) a) II, III e IV
    (V) b) I, III e IV *************************************************************************************************
    (F) c) I, II e III
    (F) d) I, II e IV
    (F) e) I, II, III e IV
    """


if __name__ == '__main':
    print(_(pergunta_1()))
