

def codigo_28():
    """
    import pandas as pd

    df_etanol = pd.read_csv('exportacao-etanol-hidratado-2012-2020-bep.csv', sep=';', encoding="ISO-8859-1")

    print(df_etanol.info())
    df_etanol.head(2)
    """


def codigo_29():
    """
    df_etanol.drop(columns=['PRODUTO', 'MOVIMENTO COMERCIAL', 'UNIDADE'], inplace=True)

    df_etanol.head(2)
    """


def codigo_30():
    """
    df_etanol.set_index(keys='ANO', drop=True, inplace=True)

    df_etanol.head(2)
    """


def codigo_31():
    """
    for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ TOTAL'.split():
        df_etanol[mes] = df_etanol[mes].str.replace(',', '.')

    print(df_etanol.dtypes)
    df_etanol.head(2)
    """


def codigo_32():
    """
    df_etanol = df_etanol.astype(float)
    print(df_etanol.dtypes)

    df_etanol.head(2)
    """


def codigo_33():
    """
    # Em cada ano, qual o menor e o maior valor arrecadado da exportação?

    for ano in range(2012, 2021):
        ano_info = df_etanol.loc[ano]
        minimo = ano_info.min()
        maximo = ano_info.max()
        print(f"Ano = {ano}")
        print(f"Menor valor = {minimo:,.0f}".replace(',', '.'))
        print(f"Maior valor = {maximo:,.0f}".replace(',', '.'))
        print("--------------")
    """


def codigo_34():
    """
    # Considerando o período de 2012 a 2019, qual a média mensal de arrecadamento com a exportação

    print("Média mensal de rendimentos:")
    for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split():
        media = df_etanol.loc[2012:2019, mes].mean()
        print(f"{mes} = {media:,.0f}".replace(',', '.'))
    """


def codigo_35():
    """
    # Considerando o período de 2012 a 2019, qual ano teve o menor arrecadamento? E o menor?

    ano_menor_arrecadacao = df_etanol.loc[2012:2019, 'TOTAL'].idxmin()
    ano_maior_arrecadacao = df_etanol.loc[2012:2019, 'TOTAL'].idxmax()

    print(f"Ano com menor arrecadação = {ano_menor_arrecadacao}")
    print(f"Ano com maior arrecadação = {ano_maior_arrecadacao}")
    """
