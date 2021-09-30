

from webbrowser import open


def disciplinas():
    """
    Lógica Computacional
    Modelagem de Dados
    Algoritmos e Programação Estruturada
    Análise e Modelagem de Sistemas
    """


# Lógica computacional
def tarefa_1():
    """
    A GlobalTecnol S.A fará alguns testes com tabelas verdade. Lembrando que a tabela Verdade é um mecanismo que permite
    valorar fórmulas de forma genérica, a partir de entradas binárias e conectores lógicos. Visando testar seus
    conhecimentos no assunto, preencha as seguintes tabelas verdade corretamente: Só relembrando, o conectivo Não
    pode ser representado por ¬ ou ~

    CONCLUSÃO: RESOLVER AS TABELAS VERDADE
    """


# Modelagem de dados
def tarefa_2():
    """
    A GlobalTecnol S.A irá implantar futuramente soluções envolvendo sensores e Internet das Coisas em um ambiente
    hospitalar. Para isso, ela irá desenvolver um banco de dados adequado para o uso em um hospital.

    Sabendo que a implementação de um banco de dados depende de um projeto bem detalhado e eficiente, e visando testar
    seus conhecimentos em modelagem de dados, sua tarefa será:

    Criar um Modelo Entidade-Relacionamento (MER) ou um Diagrama Entidade-Relacionamento (DER) para o banco de dados de
    um hospital, onde os principais tipos de dados que o banco deverá armazenar inicialmente são: informações de
    pacientes, médicos, consultas, enfermeiros(as), prescrições, entre outros. Ficará a seu critério a definição das
    entidades, dos relacionamentos (com suas respectivas cardinalidades) e atributos, desde que se enquadre para a
    utilização em um hospital. Como é apenas uma tarefa de seleção e não uma aplicação real, o modelo pode ser reduzido,
    devendo conter pelo menos 3 entidades com relacionamentos entre si.

    CONCLUSÃO: Criar um modelo/diagrama Entidade-relacionamento (MER/DER) (um dos dois)

    CAMPOS:
    Informações de pacientes || médicos || consultas || enfermeiros(as) || prescrições || outros

    OPCIONAL
    Definição das: Entidades || Relacionamentos (cardinalidades) || Atributos

    DETALHE
    O modelo deve conter pelo menos 3 entidades relacionadas
    """


# Algoritmos e programação estruturada
def tarefa_3():
    """
    Um dos seus desafios para conseguir a vaga do estágio na GlobalTecnol S.A, é realizar a implementação de um
    problema, utilizando a estrutura de dados vetor. O vetor deve ter tamanho 3, e os valores deverão ser inseridos pelo
    usuário. Outro ponto pedido no desafio é que você imprima os valores que foram adicionados. Para este problema,
    utilize a Linguagem C.

    CONCLUSÃO: Implementação de um problema
               Linguagem C -> estrutura de dados vetor (tamanho = 3)
               Valores inseridos pelo usuário
               Impressão dos valores adicionados
    """


# Análise e modelagem de sistemas
def tarefa_4():
    """
    Um dos desafios para alcançar a tão sonhada vaga de estágio é saber desenvolver modelos para o sistema. Neste caso,
    foi proposto a você, que desenvolvesse um modelo de caso de uso para o seguinte cenário:

    - Um cinema pode ter muitas salas, sendo necessário, portanto, registrar informações a respeito de cada uma.
    - O cinema apresenta muitos filmes, sendo necessário, portanto, registrar as informações sobre os filmes.
    - Um mesmo filme pode ser apresentado em diferentes salas e em horários. Portanto, deve-se registrar as sessões dos
      filmes.
    - Os clientes do cinema podem comprar ingressos para assistir a uma sessão. O funcionário deve intermediar a compra
      de ingresso.

    (Adaptado de: Guedes, Gilleanes TA. UML 2-Uma abordagem prática. Novatec Editora, 2018.)
    """


def normas():
    """
    ------------------------------- NORMAS PARA ELABORAÇÃO E ENTREGA DA PRODUÇÃO TEXTUAL -------------------------------

    1. Em páginas de formato A4;
    2. Margens esquerda e superior de 3cm, direita e inferior de 2cm;
    3. Fonte Times New Roman ou Arial tamanho 12, cor preta;
    4. Espaçamento de 1,5 entre linhas;
    5. Se houver citações com mais de três linhas, devem ser em fonte tamanho 10, com um recuo de 4cm da margem esquerda
       e espaçamento simples entre linhas;
    6. Capa, contendo:
        6.1. Nome de sua Unidade de Ensino, Curso e Disciplinas;
        6.2. Nome completo do (a) aluno (a);
        6.3. Título da atividade;
        6.4. Nome do Tutor (a) a Distância (EAD);
        6.5. Cidade e data da entrega, apresentação ou publicação.
    """


simbolo = ''


def pdf_picker(the_input_text: str, the_list_file_format: list, main_location: str, start: int, closure: int):

    space = '    '
    giant_arrow = '--------------->'

    official_list_file_format = []

    for item in the_list_file_format:
        official_list_file_format.append(item)

    # subjects = (
    #     None,
    #     'atividade_interdisciplinar.pdf',
    #     'disc_logica_computacional.pdf',
    #     'disc_modelagem_banco_de_dados.pdf',
    #     'disc_algoritmos_e_programacao_estruturada.pdf',
    #     'disc_analise_e_modelagem_de_sistemas.pdf'
    # )

    this_error = f'Tipo de dado é inválido. A função aceita somente números de {start} a {closure}'
    this_message = f'Números permitidos: Entre {start} a {closure}'

    # actions = {
    #     0: f'{main_location}{official_list_file_format[0]}',
    #     1: f'{main_location}{official_list_file_format[1]}',
    #     2: f'{main_location}{official_list_file_format[2]}',
    #     3: f'{main_location}{official_list_file_format[3]}',
    #     4: f'{main_location}{official_list_file_format[4]}',
    # }

    actions = {}
    x = start
    y = closure
    counter = 0
    this_range = list(range(x, y + 1))
    while x < y + 1:
        actions[this_range[counter]] = f'{main_location}{official_list_file_format[counter]}'
        x += 1
        counter += 1

    while True:
        try:
            number = int(input(the_input_text))

            if start <= number <= closure:

                for key in actions:
                    if number == key:
                        return open(actions[key])

            else:
                print('\n', space, giant_arrow, this_message)

        except ValueError:
            print('\n', space, giant_arrow, this_error)


if __name__ == '__main__':

    frame = f"""
    ---------------------------------------- Qual o documento deve ser aberto? ----------------------------------------
    0 - Atividades Interdiciplinares (pdf)
    1 - Projeto Integrado 2 (pdf)
    2 - Lógica Computacional (pdf)
    3 - Modelagem de dados (pdf)
    4 - Algoritmos e Programação Estruturada (pdf)
    5 - Análise e Modelagem de Sistemas (pdf)

    Digite de 1 a 5 após a seta -> """

    list_ = [
        'atividade_interdisciplinar.pdf',
        'disc_projeto_integrado2.pdf',
        'disc_logica_computacional.pdf',
        'disc_modelagem_banco_de_dados.pdf',
        'disc_algoritmos_e_programacao_estruturada.pdf',
        'disc_analise_e_modelagem_de_sistemas.pdf'
    ]

    print(pdf_picker(the_input_text=frame,
                     the_list_file_format=list_,
                     main_location='C:\\Users\\Conta secundária\\Downloads\\dbe\\dbe_semestre2\\',
                     start=0, closure=5))
