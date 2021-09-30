

from random import choice
from time import sleep


def ink(label: str):

    x: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[1:37m',
        '\033[1:38m',
    )

    return f"{choice(x)}{label}{x[-1]}"


simbolo_ponto = '•'
autor = 'Vanessa Cadan Scheffer'

secao_1 = f"""
    [ item 1 ] ------------------------------------------- Python (criação) -------------------------------------------
        • Guido van Rossum    • Stichting Mathematisch Centrum (CWI)    • Holanda    • 1990;
    
    [ item 2 ] ---------------------------------- Python (coorporações relacionadas) ----------------------------------
        • CNRI (Corporação para Iniciativas Nacionais de Pesquisa) (Virginía) (1995)
        • BeOpen PythonLabs (2000)    • Digital Creations    • Zope Corporation
        • Python Software Foundation (PSF) (2001);
    
    [ item 3 ] ----------------------------- Python (similaridades com outras linguagens) -----------------------------
        • Perl    • Ruby    • Scheme    • Java;
    
    [ item 4 ] --------------------------------------- Python (características) ---------------------------------------
        • Sintaxe elegante
        • Desenvolvimento de protótipos e outras tarefas de programação ad-hoc, sem comprometer a manutenção
        • Múltiplas bibliotecas (conexão com servidores web) 
                                (pesquisa de texto com expressões regulares)
                                (leitura e modificação de arquivos)
        • Linguagem interpretada (sem necessidade de compilação)
        • Atribuição múltipla;
    
    [ item 5 ] ------------------------------------------- Python (sintaxe) -------------------------------------------
        • PEP 8 (Python enhancement proposal) Style Guide for Python Code    • Código pythônico (pythonic code)
        • Formatação, identação, parâmetros das funções
    ;
    
    [ item 6 ] ---------------------------------------- Python (interpretador) ----------------------------------------
        • Unicode (presença de caracteres especiais) (porém, não recomendado);
    
    [ item 7 ] --------------------- Python (IDE) (1. significado) (2. ferramentas) (3. exemplos) ---------------------
        • Integrated Development Environment    
        • Integração com sistemas de versionamento de código, refatoração de código, debug
        • Pycharm    • Spyder    • Visual Studio Code;
    
    [ item 8 ] ------------------------------------ Python (ferramenta de trabalho) ------------------------------------
        • Anaconda    • https://www.anaconda.com/products/individual;
    
    [ item 9 ] -------------------------------- Python (sistemas de controle de versão) --------------------------------
        • Git    • Github;
    
    [ item 10 ] ------------------------------------------ Python (navegação) ------------------------------------------
        • COLAB (Google Colaboratoy)    
        • Escrita e execução de código Python através do navegador
        • Acesso gratuito a recursos de computação, incluindo GPUs;
        
    [ item 11 ] ------------------------------------------ Python (variáveis) ------------------------------------------
        • Espaços alocados na memória RAM temporários    
        • Não necessitam tipagem (tipagem dinâmica)    
        • Tipo de dado com base no valor (var = True) (tipo = bool);
    
    [ item 12 ] ------------------------------------------- Python (detalhe) -------------------------------------------
        • Tudo em Python é objeto, que é o equivalente à classe;
    
    [ item 13 ] ------------------------------- Python (inserção de entrada em strings) -------------------------------
        • [ Formatador de caracteres ] [ %s e % ()            ] 
        • [ Método format()          ] [ chave & .format(var) ]
        • [ String formatada         ] [ f'' & chave          ] [ a partir do Python 3.6 ];
    
    [ item 14 ] ------------------------------------ Python (operações matemáticas) ------------------------------------
        • x + y    • x - y    • x * y    • x / y    • x // y    • x % y    • abs(x)    • pow(x, y)    • x ** y;
    
    [ item 1 ] - -;
    """.split(';')

if __name__ == '__main__':

    s1 = 'Seção 1 - A linguagem Python'

    parada = 'Com relação às operações matemáticas, seja na programação, seja na resolução analítica, o mais importante'
