

from sys import getsizeof as _


# RESPOSTA: D
def pergunta_1():
    """
    1) As expressões lógicas, também chamadas de fórmulas, são como fórmulas matemáticas. Assim, se existem regras para
       escrever uma fórmula matemática, também existem para escrever fórmulas do cálculo proposicional. Quando uma
       fórmula proposicional é escrita corretamente, ela é chamada de fórmula bem-formulada.

    Nesse contexto, analise as proposições a seguir:

    I.   A --> (B ^ C ~)
    II.  (A ^ ~B) --> D
    III. C ^ B --> ~C
    IV.  B --> (~A) ^ C

    É correto o que se afirma em:

    a) I e II
    b) III
    c) IV
    d) II, III e IV
    e) I
    """


# RESPOSTA: E
def pergunta_2():
    """
    2) Através de valores lógicos de entrada para as proposições, uma fbf pode ser valorada em verdadeira ou falsa.
       Nesse contexto, associe os itens da figura 1, a seguir:

        V    F
        A    B
       ________
       ~ V ^ ~ F
       1   3   2

    (3) F ^ V = F
    (1) ~ V = F
    (2) ~ F = V

    Assinale a alternativa que contém a associação correta entre a figura 1 e a valoração:

    a) 1-2-3.
    b) 3-2-1.
    c) 2-3-1.
    d) 1-3-2.
    e) 3-1-2.
    """


# RESPOSTA: C
def pergunta_3():
    """
    3) A lógica proposicional é composta por proposições e conectivos lógicos que permitem criar uma série de fórmulas,
       que quando escritas corretamente são chamadas de fbfs (fórmula bem formulada). Uma fbf é valorada em verdadeira
       (V) ou falsa (F), a partir da valoração das proposições com o conectivo lógico em questão, respeitando a ordem de
       precedência dos operadores lógicos. A valoração de uma fórmula também depende dos valores lógicos de entrada para
       cada uma das proposições.

    Com base em seu conhecimento à respeito de lógica proposicional, analise as afirmativas a seguir.

    I.   Quando uma fórmula apresenta um conjunto de proposições, das quais uma delas é uma conclusão, dizemos que tal
         fórmula é um argumento. (V - página 120)
    II.  Uma sequência de demonstração é uma sequência de fbfs nas quais cada fbf é uma hipótese ou o resultado de se
         aplicar uma das regras de dedução do sistema formal a fbfs anteriores na sequência (V - página 122)
    III. As regras de inferência serão usadas quando uma fbf (que pode ser uma hipótese ou resultado de uma regra) pode
         ser substituída por outra fbf, mantendo o resultado lógico. (F - Página 123)

    Neste contexto, é correto o que se afirma em:

    a) I           ||
    b) II          || x
    c) I e II      || OK
    d) II e III    || x
    e) I, II e III ||
    """


# RESPOSTA: B
def pergunta_4():
    """
    4) Além das regras de equivalência, o processo de dedução lógica também possui as regras de inferência. Na
       inferência, dada uma determinada fbf, ela poderá ser substituída por outra que atenda a regra de inferência. Há
       três regras de inferência principais: Modus Ponens (MP), Modus Tollens (MT) e Silogismo Hipotético (SH).

    De acordo com as informações apresentadas na tabela a seguir, faça a associação das regras de inferência na Coluna A
    com as respectivas estruturas apresentados na Coluna B.

    I. Modus Ponens (MP)           || 1. (P => Q) ^ ~Q => ~P
    II. Modus Tollens (MT)         || 2. (P => Q) ^ P => Q
    III. Silogismo Hipotético (SH) || 3. (P => Q) ^ (Q => R) => (P => R)

    Assinale a alternativa que apresenta a associação CORRETA entre as colunas. (I = 2) (II = 1) (III = 3)

    a) I - 1; II - 3; III - 2 || x
    b) I - 2; II - 1; III - 3 ||
    c) I - 3; II - 1; III - 2 || x
    d) I - 3; II - 2; III - 1 || x
    e) I - 1; II - 2; III - 3 ||
    """


# RESPOSTA: B
def pergunta_5():
    """
    5) Quando uma fórmula apresenta um conjunto de proposições, das quais uma delas é uma conclusão, dizemos que tal
       fórmula é um argumento. “Um argumento e´ um conjunto de proposições, ou de fórmulas, nas quais uma delas
       (conclusão) deriva, ou e´ consequência, das outras (premissas).”

    Com relação à temática apresentada, avalie as seguintes asserções e a relação proposta entre elas.

    I. A ligação entre as hipóteses e a conclusão é feita por meio do conectivo condicional
    PORQUE
    II. No argumento, as proposições são ligadas logicamente pelo conectivo de conjunção (e), as quais implicam
        logicamente a conclusão.

    A respeito dessas asserções, assinale a alternativa correta.

    a) As asserções I e II são proposições verdadeiras, mas a II não justifica a I. || OK
    b) As asserções I e II são proposições verdadeiras e a II justifica a I.        ||
    c) A asserção I é uma proposição verdadeira e a II, falsa.                      ||
    d) A asserção I é uma proposição falsa e a II, verdadeira.                      || x
    e) As asserções I e II são proposições falsas.                                  || x
    """


if __name__ == '__main__':
    print(quadro := f"""
    ---------- TAMANHOS DAS PERGUNTAS ----------
    Pergunta 1: {_(pergunta_1())}
    Pergunta 2: {_(pergunta_2())}
    Pergunta 3: {_(pergunta_3())}
    Pergunta 4: {_(pergunta_4())}
    Pergunta 5: {_(pergunta_5())}""")
