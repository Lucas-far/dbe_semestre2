

from random import choice
from time import sleep


def ink(label: str):

    x: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[1:37m',
        '\033[1:38m',
    )

    return f"{choice(x)}{label}{x[-1]}"


simbolo_ponto = '•'

secao1 = f"""
    [ item 1 ] ------------------------------------------- Pandas (conceito) -------------------------------------------
        • Pacote Python que fornece estruturas de dados projetadas para facilitar o trabalho com dados estruturados
          (tabelas) e de séries temporais;
          
    [ item 2 ] ----------------------------------------- Pandas (documentação) -----------------------------------------
        • https://pandas.pydata.org/docs/getting_started/overview.html;
        
    [ item 3 ] ------------------------------------------- Panda (objetivo) -------------------------------------------    
        • Pretende ser o alicerce de alto nível fundamental p/ uma análise prática, a dos dados do mundo real em Python;
        
    [ item 4 ] ------------------------------------------ Pandas (instalção) ------------------------------------------
        • pip install pandas;
        
    [ item 5 ] ------------------------------------- Pandas (estruturas de dados) -------------------------------------
        • Series    || vetor de dados (unidimencional), capaz de armazenar diferentes tipos de dados  
        • Dataframe || conjunto de Series, um contêiner para Series;
        
    [ item 6 ] ---------------------------- Pandas (estruturas de dados) (características) ----------------------------
        • Indexação das linhas, por rótulo (str, int, float, date);
        
    [ item 7 ] ------------------------ Pandas (1. exemplo de Series) (2. exemplo de Dataframe) ------------------------
        
        [ Series ] (índice, dados)         
            a     Howard                         
            b     Ian                           
            c     Peter  
        
        [ DataFrame ] (índices, colunas, dados) (planilha de Excel)
            Nome   Cidade    Idade
        0   Howard New York  32
        1   Ian    Chicago   22
        2   Peter  San Diego 25;
    
    [ item 8 ] ----------------------------------------- Pandas (cheat sheet) -----------------------------------------
        • https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf;
        
    [ item 9 ] ------------------------------------- Pandas (importação via alias) -------------------------------------
        • import pandas as pd; 
    
    [ item 10 ] --------------------------------- Pandas (instância de objeto Series) ---------------------------------                    
        • pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
        • Parâmetro mandatório [ data ]
        • Para saber mais informações, ver o módulo [ pandas_tutorial.py ];
    """.split(';')

if __name__ == '__main__':

    s1 = 'INTRODUÇÃO A BIBLIOTECA PANDAS (Vanessa Cadan Scheffer)'
