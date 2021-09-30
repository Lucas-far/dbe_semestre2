

def codigo_22():
    """
    from datetime import datetime
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    """


def codigo_23():
    """
    texto_string = requests.get('https://globoesporte.globo.com/').text
    hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    bsp_texto = BeautifulSoup(texto_string, 'html.parser')
    lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})
    print("Quantidade de manchetes = ", len(lista_noticias))
    lista_noticias[0].contents
    """


def codigo_24():
    """
    lista_noticias[0].contents[1].text.replace('"',"")
    """


def codigo_25():
    """
    lista_noticias[0].find('a').get('href')
    """


def codigo_26():
    """
    descricao = lista_noticias[0].contents[2].text
    if not descricao:
        descricao = noticia.find('div', attrs={'class': 'bstn-related'})
        descricao = descricao.text if descricao else None # Somente acessará a propriedade text caso tenha encontrado ("find")
    descricao
    """


def codigo_27():
    """
    metadados = lista_noticias[0].find('div', attrs={'class':'feed-post-metadata'})

    time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
    secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

    time_delta = time_delta.text if time_delta else None
    secao = secao.text if secao else None

    print('time_delta = ', time_delta)
    print('seção = ', secao)
    """


def codigo_28():
    """
    dados = []

    for noticia in lista_noticias:
        manchete = noticia.contents[1].text.replace('"',"")
        link = noticia.find('a').get('href')

        descricao = noticia.contents[2].text
        if not descricao:
            descricao = noticia.find('div', attrs={'class': 'bstn-related'})
            descricao = descricao.text if descricao else None

        metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
        time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
        secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

        time_delta = time_delta.text if time_delta else None
        secao = secao.text if secao else None

        dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))

    df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
    df.head()
    """


def codigo_29():
    """
    from datetime import datetime

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

    class ExtracaoPortal:
        def __init__(self):
            self.portal = None

        def extrair(self, portal):
            self.portal = portal
            texto_string = requests.get('https://globoesporte.globo.com/').text
            hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            bsp_texto = BeautifulSoup(texto_string, 'html.parser')
            lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})

            dados = []

            for noticia in lista_noticias:
                manchete = noticia.contents[1].text.replace('"',"")
                link = noticia.find('a').get('href')

                descricao = noticia.contents[2].text
                if not descricao:
                    descricao = noticia.find('div', attrs={'class': 'bstn-related'})
                    descricao = descricao.text if descricao else None

                metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
                time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
                secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

                time_delta = time_delta.text if time_delta else None
                secao = secao.text if secao else None

                dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))

            df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
            return df
    """


def codigo_30():
    """
    df = ExtracaoPortal().extrair("https://globoesporte.globo.com/")
    df.head()
    """