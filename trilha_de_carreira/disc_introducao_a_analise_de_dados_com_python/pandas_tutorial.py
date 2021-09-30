

import pandas as pd

# dependência = pip install pandas
# pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)  # Objeto pandas padrão Series

_ = '------------------------------------------------------------------------------------------------------------------'

nome = 'Lucas Farias Santos de Sousa'

dados_dict = {
    'nome': 'Lucas',
    'sobrenome': 'Farias',
    'complemento': 'Santos de Sousa'
}

dados_tpl = ('Lucas', 'masculino', 'Brasil')

objeto = pd.Series(data=5)                 # Objeto Series inteiro
objeto2 = pd.Series(data=0.5)              # Objeto Series flutuante
objeto3 = pd.Series(data=nome)             # Objeto Series string
objeto4 = pd.Series(data=nome.split(' '))  # Objeto Series lista
objeto5 = pd.Series(data=dados_tpl)        # Objeto Series tupla
objeto6 = pd.Series(data=dados_dict)       # Objeto Series dicionário


print([1], _)
print(objeto)
print([2], _)
print(objeto2)
print([3], _)
print(objeto3)
print([4], _)
print(objeto4)
print([5], _)
print(objeto5)
print([6], _)
print(objeto6)

# --------------------- Criação de rótulos (parâmetro index) (equivalência de índices mandatória) ---------------------
pessoas = 'Ana Ena Ina Ona Una'.split(' ')  # 5 índices
idades = [*range(16, 21)]                   # 5 índices

print([7], _)
print(pessoas_idades := pd.Series(data=pessoas, index=idades))

# --------------------------------- Método (loc) (achar um valor através de um rótulo) ---------------------------------
print([8], _)
print(pessoas_idades.loc[16])
print(pessoas_idades.loc[20])

# TODO Parada: EXTRAINDO INFORMAÇÕES DE UMA SERIES
