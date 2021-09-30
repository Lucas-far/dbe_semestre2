

from sys import getsizeof as _


# RESPOSTA: B ou D (acho que é B)
def pergunta_1():
    """
    1) Na lógica formal, proposições são combinadas através do uso de conectivos, como AND (representado pelo conectivo
       ^) e OR (representado pelo conectivo v), respectivamente E e OU. Considere a seguinte proposição: ¬p ^ q.

    Considerando o contexto, analise as afirmativas.

    I.   A proposição é equivalente a p v q. (F)
    II.  A proposição é equivalente a q ^ ¬p. (V)
    III. A tabela verdade resulta em 3 saídas verdadeiras e 1 saída falsa. (F)

    Considerando o contexto apresentado, é correto o que se afirma em:

    a) I
    b) II **************************************************************************************************************
    c) I e II
    d) II e III
    e) I, II e III

    P    Q <-- P <-- P ^ Q
    V    V    F    F
    V    F    F    F
    F    V    V    V
    F    F    V    F
    """


# RESPOSTA: D
def pergunta_2():
    """
    2) GERSTING (2017) afirma que os conectivos lógicos são classificados em conectivos binários, quando unem duas
       expressões, assim como o conectivo E e o conectivo OU, e conectivos unários, como a negação, são aplicados em uma
       única expressão. Considere a seguinte proposição: ¬¬(¬p ^ ¬¬q)

    Considerando o contexto, analise as afirmativas.

    I.   A proposição é equivalente a ¬p v q. (V)
    II.  A proposição é equivalente a ¬q ^ p. (F)
    III. A dupla negação pode ser cancelada. (V)

    Considerando o contexto, assinale a alternativa correta.

    a) I
    b) III
    c) I e II
    d) I e III  ********************************************************************************************************
    e) I, II e III
    """


# RESPOSTA: A
def pergunta_3():
    """
    3) Em circuitos digitais, visando facilitar o desenvolvimento de projetos digitais, o uso de símbolos é comum e tem
       o mesmo efeito da lógica formal. Na representação de circuitos digitais, os conectivos AND (a) e OR (b) são
       representados conforme a figura a seguir.

    Agora, analise a figura a seguir, onde há três entradas A, B e C e uma saída S.

    Considerando o contexto, assinale a alternativa que representa corretamente o circuito digital exemplificado na
    Figura 2.

    a) S = A v (B ^ C) ************************************************************************************************
    b) S = (A v B) ^ C
    c) S = A v B ^ C
    d) S = C v (A ^ B)
    e) S = A ^ B v C
    """


# RESPOSTA: C
def pergunta_4():
    """
    4) A lógica proposicional é um sistema formal que utiliza fórmulas bem formadas para representar proposições
       formadas de proposições atômicas e conectivos lógicos. Tais fórmulas podem ser derivadas. A implicação lógica
       (representada utilizando o símbolo ¿) pode ser entendida como "se proposição 1, então proposição 2”. Considere a
       proposição s ¿ (p ^ ¬r).

    Considerando o contexto, analise as afirmativas.

    I.   A proposição é uma tautologia.
    II.  A proposição é logicamente equivalente a ¬s v (p ^ ¬r).
    III. A proposição é logicamente equivalente a (s ¿ p) ^ ¬r.

    Considerando o contexto apresentado, é correto o que se afirma em:

    a) I
    b) II
    c) III ************************************************************************************************************
    d) I e III
    e) II e III
    """


if __name__ == '__main':
    print(_(pergunta_1()))
