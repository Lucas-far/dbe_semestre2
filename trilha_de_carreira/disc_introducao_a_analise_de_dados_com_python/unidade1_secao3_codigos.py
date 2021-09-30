

def codigo_1():
    """
    import pandas as pd
    """


def codigo_2():
    """
    pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()
    """


def codigo_3():
    """
    pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv").head()
    """


def codigo_4():
    """
    df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

    print(df_selic.info())
    """


def codigo_5():
    """
    df_selic.drop_duplicates(keep='last', inplace=True)
    """


def codigo_6():
    """
    from datetime import date
    from datetime import datetime as dt

    data_extracao = date.today()

    df_selic['data_extracao'] = data_extracao
    df_selic['responsavel'] = "Autora"

    print(df_selic.info())
    df_selic.head()
    """


def codigo_7():
    """
    df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
    df_selic['data_extracao'] = df_selic['data_extracao'].astype('datetime64[ns]')

    print(df_selic.info())
    df_selic.head()
    """


def codigo_8():
    """
    df_selic['responsavel'] = df_selic['responsavel'].str.upper()

    df_selic.head()
    """


def codigo_9():
    """
    df_selic.sort_values(by='data', ascending=False, inplace=True)

    df_selic.head()
    """


def codigo_10():
    """
    df_selic.reset_index(drop=True, inplace=True)

    df_selic.head()
    """


def codigo_11():
    """
    lista_novo_indice = [f'selic_{indice}' for indice in df_selic.index]

    print(lista_novo_indice[:5])
    """


def codigo_12():
    """
    df_selic.set_index(keys=[lista_novo_indice], inplace=True)

    df_selic.head()
    """


def codigo_13():
    """
    print(df_selic['valor'].idxmin())
    print(df_selic['valor'].idxmax())
    """


def codigo_14():
    """
    df_selic.loc['selic_0']
    """


def codigo_15():
    """
    df_selic.loc[['selic_0', 'selic_4', 'selic_200']]
    """


def codigo_16():
    """
    df_selic.loc[:'selic_5']
    """


def codigo_17():
    """
    df_selic.loc[['selic_0', 'selic_4', 'selic_200'], 'valor']
    """


def codigo_18():
    """
    df_selic.loc[['selic_0', 'selic_4', 'selic_200'], ['valor', 'data_extracao']]
    """


def codigo_19():
    """
    df_selic.iloc[:5]
    """


def codigo_20():
    """
    teste = df_selic['valor'] < 0.01

    print(type(teste))
    teste[:5]
    """


def codigo_21():
    """
    teste2 = df_selic['data'] >= pd.to_datetime('2020-01-01')

    print(type(teste2))
    teste2[:5]
    """


def codigo_22():
    """
    teste3 = (df_selic['valor'] < 0.01) & (df_selic['data'] >= pd.to_datetime('2020-01-01'))

    teste4 = (df_selic['valor'] < 0.01) | (df_selic['data'] >= pd.to_datetime('2020-01-01'))

    print("Resultado do AND:\n")
    print(teste3[:3])

    print("Resultado do OR:\n")
    print(teste4[:3])
    """


def codigo_23():
    """
    filtro1 = df_selic['valor'] < 0.01

    df_selic.loc[filtro1]
    """


def codigo_24():
    """
    data1 = pd.to_datetime('2020-01-01')
    data2 = pd.to_datetime('2020-01-31')

    filtro_janeiro_2020 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)

    df_janeiro_2020 = df_selic.loc[filtro_janeiro_2020]
    df_janeiro_2020.head()
    """


def codigo_25():
    """
    data1 = pd.to_datetime('2019-01-01')
    data2 = pd.to_datetime('2019-01-31')

    filtro_janeiro_2019 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)

    df_janeiro_2019 = df_selic.loc[filtro_janeiro_2019]
    df_janeiro_2019.head()
    """


def codigo_26():
    """
    print('Mínimo geral = ', df_selic['valor'].min())
    print('Mínimo janeiro de 2019 = ', df_janeiro_2019['valor'].min())
    print('Mínimo janeiro de 2020 = ',df_janeiro_2020['valor'].min(), '\n')

    print('Máximo geral = ', df_selic['valor'].max())
    print('Máximo janeiro de 2019 = ', df_janeiro_2019['valor'].max())
    print('Máximo janeiro de 2020 = ',df_janeiro_2020['valor'].max(), '\n')

    print('Média geral = ', df_selic['valor'].mean())
    print('Média janeiro de 2019 = ', df_janeiro_2019['valor'].mean())
    print('Média janeiro de 2020 = ',df_janeiro_2020['valor'].mean(), '\n')
    """


def codigo_27():
    """
    df_selic.to_csv('dados_selic.csv')
    """


def codigo_28():
    """
    import psycopg2

    host = 'XXXXX'
    port = 'XXXXX'
    database = 'XXXXX'
    username = 'XXXXX'
    password = 'XXXXX'

    conn_str = fr"dbname='{database}' user='{username}' host='{host}' password='{password}' port='{port}'"
    conn = psycopg2.connect(conn_str)

    query = "select * from XXX.YYYY"
    df = pd.read_sql(query, conn)import mysql.connector

    host = 'XXXXX'
    port = 'XXXXX'
    database = 'XXXXX'
    username = 'XXXXX'
    password = 'XXXXX'

    conn_str = fr"host={host}, user={username}, passwd={password}, database={database}"
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")

    query = "select * from XXX.YYYY"
    df = pd.read_sql(query, conn)
    """
