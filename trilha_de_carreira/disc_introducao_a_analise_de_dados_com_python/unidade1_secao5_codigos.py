

def codigo_1():
    """
    from matplotlib import pyplot as plt

    %matplotlib inline
    """


def codigo_2():
    """
    import random

    dados1 = random.sample(range(100), k=20)
    dados2 = random.sample(range(100), k=20)

    plt.plot(dados1, dados2) # pyplot gerencia a figura e o eixo
    """


def codigo_3():
    """
    import numpy as np

    x = range(5)
    x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.

    fig, ax = plt.subplots(1, 2, figsize=(12, 5)) # Cria figura com subplots: 1 linha, 2 colunas e eixos

    print("Tipo de ax = ", type(ax))
    print("Conteúdo de ax[0] = ", ax[0])
    print("Conteúdo de ax[1] = ", ax[1])

    ax[0].plot(x, x, label='eq_1') # cria gráfico sobre eixo 0
    ax[0].plot(x, x**2, label='eq_2') # cria gráfico sobre eixo 0
    ax[0].plot(x, x**3, label='eq_3') # cria gráfico sobre eixo 0
    ax[0].set_xlabel('Eixo x')
    ax[0].set_ylabel('Eixo y')
    ax[0].set_title("Gráfico 1")
    ax[0].legend()

    ax[1].plot(x, x, 'r--', label='eq_1') # cria gráfico sobre eixo 1
    ax[1].plot(x**2, x, 'b--', label='eq_2') # cria gráfico sobre eixo 1
    ax[1].plot(x**3, x, 'g--', label='eq_3') # cria gráfico sobre eixo 1
    ax[1].set_xlabel('Novo Eixo x')
    ax[1].set_ylabel('Novo Eixo y')
    ax[1].set_title("Gráfico 2")
    ax[1].legend()
    """


def codigo_4():
    """
    x = range(5)
    x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.

    fig = plt.subplots(figsize=(12, 5)) # Cria figura sem eixo
    plt.subplot(121) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 1
    plt.plot(x, x, label='eq_1')
    plt.plot(x, x**2, label='eq_2')
    plt.plot(x, x**3, label='eq_3')
    plt.title("Gráfico 1")
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.legend()

    plt.subplot(122) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 2
    plt.plot(x, x, 'r--', label='eq_1')
    plt.plot(x**2, x, 'b--', label='eq_2')
    plt.plot(x**3, x, 'g--', label='eq_3')
    plt.title("Gráfico 2")
    plt.xlabel('Novo eixo x')
    plt.ylabel('Novo eixo y')
    plt.legend()
    """


def codigo_5():
    """
    import pandas as pd

    dados = {
        'turma':['A', 'B', 'C'],
        'qtde_alunos':[33, 50, 45]
        }
    df = pd.DataFrame(dados)

    df
    """


def codigo_6():
    """
    df.plot(x='turma', y='qtde_alunos', kind='bar')
    """


def codigo_7():
    """
    df.plot(x='turma', y='qtde_alunos', kind='barh')
    """


def codigo_8():
    """
    df.plot(x='turma', y='qtde_alunos', kind='line')
    """


def codigo_9():
    """
    df.set_index('turma').plot(y='qtde_alunos', kind='pie')
    """


def codigo_10():
    """
    df_etanol = pd.read_csv('exportacao-etanol-hidratado-2012-2020-bep.csv', sep=';', encoding="ISO-8859-1")

    # Apaga colunas que não usaremos
    df_etanol.drop(columns=['PRODUTO', 'MOVIMENTO COMERCIAL', 'UNIDADE'], inplace=True)

    # Substitui a vírgula por ponto em cada coluna
    for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ TOTAL'.split():
        df_etanol[mes] = df_etanol[mes].str.replace(',', '.')

    # Converte os valores para float
    df_etanol = df_etanol.astype(float)

    # Converte o ano para inteiro
    df_etanol['ANO'] = df_etanol['ANO'].astype(int)

    df_etanol.head(2)
    """


def codigo_11():
    """
    df_etanol.plot(x='ANO',
               y='JAN',
               kind='bar',
               figsize=(10, 5),
               rot=0,
               fontsize=12,
               legend=False)

    df_etanol.plot(x='ANO',
                   y='JAN',
                   kind='line',
                   figsize=(10, 5),
                   rot=0,
                   fontsize=12,
                   legend=False)
    """


def codigo_12():
    """
    df_etanol[['ANO', 'JAN', 'FEV']].plot(x='ANO', kind='bar', figsize=(10, 5), rot=0, fontsize=12)
    """


def codigo_13():
    """
    import seaborn as sns

    # Configurando o visual do gráfico. Leia mais em https://seaborn.pydata.org/generated/seaborn.set.html#seaborn.set
    sns.set(style="whitegrid") # opções: darkgrid, whitegrid, dark, white, ticks

    df_tips = sns.load_dataset('tips')

    print(df_tips.info())
    df_tips.head()
    """


def codigo_14():
    """
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
    """


def codigo_15():
    """
    plt.figure(figsize=(10, 5))

    ax = sns.barplot(x="day", y="total_bill", data=df_tips)

    ax.axes.set_title("Venda média diária", fontsize=14)
    ax.set_xlabel("Dia", fontsize=14)
    ax.set_ylabel("Venda média ", fontsize=14)
    ax.tick_params(labelsize=14)
    """


def codigo_16():
    """
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_tips, x="day")
    """


def codigo_17():
    """
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_tips, x="day", hue="sex")
    """


def codigo_18():
    """
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df_tips, x="total_bill", y="tip")
    """
