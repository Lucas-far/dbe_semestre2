

from sys import getsizeof as _


# RESPOSTA: A
def pergunta_1():
    """
    1) Hoje em dia, com sistemas informacionais espalhados por todos os setores da economia e em nosso dia-a-dia, uma
       das escolhas mais populares na hora de decidir qual a profissão seguir são, com certeza, profissões relacionadas
       à computação, programação ou análise de sistemas. Para ser um profissional dessa área e ter condições de
       progredir na profissão que demanda construção de sistemas que envolvem software, será necessário um conhecimento
       sólido de lógica computacional. A lógica formal começa nos estudos de Aristóteles, na Grécia Antiga.

    A lógica é dita formal quando:

    --------------------------------------------------------------------------------------------------------------------
    a) analisa e representa a forma de qualquer argumento para que possa ser considerado válido para se chegar a uma
       conclusão, em que se pode inferir alguma resposta.
    --------------------------------------------------------------------------------------------------------------------

    b) permite expressar as premissas e suas relações por meio de símbolos matemáticos, construindo equações para
       expressar argumentos.

    c) nosso conhecimento, o conhecimento humano, parte de duas fontes principais. A primeira trata da receptividade das
       impressões através de nossos sentidos.

    d) é relativa à faculdade de conhecer um objeto por representações mentais, através do pensamento.

    e) está relacionado ao que é obtido através de nossos sentidos, à observação, à experimentação, com base na presença
       real de determinado objeto.
    """


# RESPOSTA: B
def pergunta_2():
    """
    2) O estudo da lógica permite, que de forma prática, possamos entender como nosso raciocínio é formado, fundamentar
       nossos argumentos, escrever e registrar de forma organizada, nos comunicarmos melhor, além de fazer conexões
       entre diversos assuntos e entender melhor o mundo que está a nossa volta.

    De acordo com as informações apresentadas na tabela a seguir, faça a associação das nomenclaturas de alguns termos
    importantes e muito utilizados na lógica com suas respectivos definições.

    I. Conhecimento Empírico
        1. Se preocupa com argumentos que permitam chegar a conclusões gerais a partir de casos particulares.
    II. Conhecimento Puro
        2. É aquela que parte de premissas, afirmativas ou leis mais gerais, permitindo a obtenção de verdades menos
           gerais, ou particulares.
    III. Lógica Dedutiva
        3. é relativo à representação que não se mescla com a sensação, é puramente racional.
    IV. Lógica Indutiva
        4. Está relacionado ao que é obtido através de nossos sentidos, à observação, à experimentação, com base na
           presença real de determinado objeto.

    a) I - 4; II - 3; III - 1; IV - 2.
    b) I - 4; II - 3; III - 2; IV - 1. *********************************************************************************
    c) I - 4; II - 2; III - 3; IV - 1.
    d) I - 3; II - 4; III - 2; IV - 1.
    e) I - 3; II - 1; III - 4; IV - 2.
    """


# RESPOSTA: C
def pergunta_3():
    """
    3) A Lógica atualmente é fortemente estudada em matérias relacionadas a ciência da computação, tecnologia da
       informação e programação, pois é a base para a construção de algoritmos. É importante ter um forte entendimento
       desta ciência para que possamos compreender como construir algoritmos e desenvolver e analisar sistemas
       computacionais.

    Veja um exemplo de conclusão lógica:

    Bruce é uma pessoa e sabe caminhar.
    Klark é uma pessoa e sabe caminhar.
    Diana é uma pessoa e sabe caminhar.
    (...)
    Portanto, toda pessoa sabe caminhar.

    O exemplo de conclusão lógica descrita acima foi obtido através

    a) do Conhecimento Empírico.
    b) do Conhecimento Puro.
    c) da Lógica Indutiva. *********************************************************************************************
    d) da Lógica Transcendental.
    e) da Lógica Simbólica.
    """


# RESPOSTA: A
def pergunta_4():
    """
    4) Em um sentido amplo, a lógica é o estudo da estrutura e dos princípios relativos ao raciocínio, à estruturação do
       pensamento, com ênfase na argumentação, que pode ser considerada como válida ou inválida. Com base em premissas,
       ela permite a construção do raciocínio indutivo ou dedutivo, e também a realização de operações lógicas
       simbólicas e demonstrações matemáticas.

    Podemos classificar o estudo da lógica em três grandes períodos:

    a) o Período Aristotélico, o Período Booleano e o Período Atual. ***************************************************
    b) o Período do Silogismo, o Período Booleano e o Período Isaacotélico. (F)
    c) o Período Aristotélico, Período do Silogismo e o Período Atual.      (F)
    d) o Período Aristotélico, o Período Booleano e o Período do Silogismo. (F)
    e) o Período Aristotélico, o Período Booleano e o Período Isaacotélico. (F)
    """


if __name__ == '__main__':
    print(quadro := f"""
        ---------- TAMANHOS DAS PERGUNTAS ----------
        Pergunta 1: {_(pergunta_1())}
        Pergunta 2: {_(pergunta_2())}
        Pergunta 3: {_(pergunta_3())}
        Pergunta 4: {_(pergunta_4())}""")
