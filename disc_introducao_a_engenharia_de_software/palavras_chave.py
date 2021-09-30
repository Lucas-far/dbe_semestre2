

from metodos_bdd.bdd import mtd_paint_random as _

#todo Iniciar a unidade 2 - seção 3

meaning = 'conceito'
separator = '*-*-*-*-*-*'

u2_s1 = f'UNIDADE 2 / SEÇÃO 1 {_(label=f"{separator}")} '
pressman = 'Pressman (2006)'
sommerville = 'Sommerville (2011)'
zanin = 'Zanin et al. (2018)'
three_authors_1977 = 'Boehn, Brown e Lipow (1977)'


u2_s2 = f'UNIDADE 2 / SEÇÃO 2 {_(label=f"{separator}")} '
mello = 'Mello (2010)'
wazlawick = 'Wazlawick (2013)'
abnt = '(ABNT, 2015)'
two_authors_2019 = 'Carpinetti e Gerolamo (2019)'

u2_s3 = f'UNIDADE 2 / SEÇÃO 3 {_(label=f"{separator}")} '
couto = 'Couto (2007)'
two_authors_2006 = 'Koscianski e Soares (2006)'
valls = 'Valls (2003)'
rocha = 'Rocha (2005)'

u3_s1 = f'UNIDADE 3 / SEÇÃO 1 {_(label=f"{separator}")} '

summary = {

    'ebook': {

        # -------------------------------------------- UNIDADE 2 / SEÇÃO 1 --------------------------------------------
        1: {'título': u2_s1 + 'Qualidade de software', 'ref': zanin, 'det': meaning},
        2: {'título': u2_s1 + 'Requisitos funcionais', 'ref': None, 'det': meaning},
        3: {'título': u2_s1 + 'Requisitos não funcionais', 'ref': None, 'det': meaning},
        4: {'título': u2_s1 + 'Ciclo de desenvolvimento de um software', 'ref': pressman, 'det': '6 etapas'},
        5: {'título': u2_s1 + 'Qualidade de software', 'ref': pressman, 'det': meaning},
        6: {'título': u2_s1 + 'Qualidade nas atividades de desenvolvimento de software', 'ref': sommerville, 'det': '3 níveis'},
        7: {'título': u2_s1 + 'Falha de software', 'ref': zanin, 'det': 'aspecto antagônico à qualidade'},
        8: {'título': u2_s1 + 'Desenvolvedor', 'ref': None, 'det': 'tratamento de falha de softwares / 3 meios'},
        9: {'título': u2_s1 + 'Erros de software', 'ref': zanin, 'det': meaning},
        10: {'título': u2_s1 + 'Defeito de software', 'ref': zanin, 'det': meaning},
        11: {'título': u2_s1 + 'Bugs', 'ref': zanin, 'det': meaning},
        12: {'título': u2_s1 + 'Garantia de qualidade', 'ref': sommerville, 'det': 'Software Quality Assurance (SQA) / 5 deveres'},
        13: {'título': u2_s1 + 'Garantia de qualidade', 'ref': pressman, 'det': meaning},
        14: {'título': u2_s1 + 'Funcionalidades para medição da qualidade de software', 'ref': three_authors_1977, 'det': '3 funcionalidades com várias características'},
        15: {'título': u2_s1 + 'Checklists', 'ref': None, 'det': '3 características'},
        16: {'título': u2_s1 + 'Processos de qualidade', 'ref': sommerville, 'det': '5 processos'},

        # -------------------------------------------- UNIDADE 2 / SEÇÃO 2 --------------------------------------------
        17: {'título': u2_s2 + 'Setor de desenvolvimento vs manufatura', 'ref': mello, 'det': 'software é produto'},
        18: {'título': u2_s2 + 'Modelos de qualidade de produto (software)', 'ref': wazlawick, 'det': '4 normas'},
        19: {'título': u2_s2 + 'ISO 9126 (funcionalidade)', 'ref': wazlawick, 'det': '5 subcaracterísticas'},
        20: {'título': u2_s2 + 'ISO 9126 (confiabilidade)', 'ref': wazlawick, 'det': '3 subcaracterísticas'},
        21: {'título': u2_s2 + 'ISO 9126 (usabilidade)', 'ref': wazlawick, 'det': '3 subcaracterísticas'},
        22: {'título': u2_s2 + 'ISO 9126 (eficiência)', 'ref': wazlawick, 'det': '2 subcaracterísticas'},
        23: {'título': u2_s2 + 'ISO 9126 (manutenibilidade)', 'ref': wazlawick, 'det': '3 subcaracterísticas'},
        24: {'título': u2_s2 + 'ISO 9126 (portabilidade)', 'ref': wazlawick, 'det': '3 subcaracterísticas'},
        25: {'título': u2_s2 + 'ISO 9126 (métricas) (conjuntos)', 'ref': wazlawick, 'det': '3 métricas'},
        26: {'título': u2_s2 + 'ISO 9000', 'ref': abnt, 'det': 'funções'},
        27: {'título': u2_s2 + 'ISO 9000', 'ref': two_authors_2019, 'det': '8 princípios de gestão de qualidade'},
        28: {'título': u2_s2 + 'ISO 9001', 'ref': abnt, 'det': 'atua no sistema de gestão da qualidade (SGQ) / 6 objetivos'},

        # -------------------------------------------- UNIDADE 2 / SEÇÃO 3 --------------------------------------------
        29: {'título': u2_s3 + 'Mapeamento de processos', 'ref': sommerville, 'det': '5 benefícios'},
        30: {'título': u2_s3 + 'Níveis de detalhamento de processos', 'ref': sommerville, 'det': '3 níveis'},
        31: {'título': u2_s3 + 'Modelos de maturidade', 'ref': None, 'det': '2 modelos'},
        32: {'título': u2_s3 + 'Capability Maturity Model', 'ref': couto, 'det': '5 níveis'},
        33: {'título': u2_s3 + 'Capability Maturity Model Integration', 'ref': two_authors_2006, 'det': 'importância'},
        34: {'título': u2_s3 + 'Capability Maturity Model Integration', 'ref': None, 'det': '5 níveis (início no 0)'},
        35: {'título': u2_s3 + 'ISO 9001', 'ref': valls, 'det': 'objetivos e características'},
        36: {'título': u2_s3 + 'ISO 9001', 'ref': two_authors_2006, 'det': '8 princípios da qualidade'},
        37: {'título': u2_s3 + 'ISO 9001', 'ref': valls, 'det': 'procedimentos após implantação'},
        38: {'título': u2_s3 + 'Melhoria de processos', 'ref': valls, 'det': '6 pontos'},
        39: {'título': u2_s3 + 'PSP (Personal Software Process)', 'ref': two_authors_2006, 'det': meaning},
        40: {'título': u2_s3 + 'PSP (Kloc)', 'ref': two_authors_2006, 'det': meaning + ' operacionalizar PSP'},
        41: {'título': u2_s3 + 'Softex', 'ref': None, 'det': 'gestão de MPS.BR (Melhoria de procedimentos de software)'},
        42: {'título': u2_s3 + 'MPS.BR', 'ref': None, 'det': 'Tutorial para uma empresa poder ser avaliada quanto ao nível de maturidade'},
        43: {'título': u2_s3 + 'MPS.BR', 'ref': rocha, 'det': '3 ténicas constitutivas (modelos) / MR MA MN'},
        44: {'título': u2_s3 + 'MPS.BR (modelos)', 'ref': rocha, 'det': '3 modelos e seus formulários'},
        45: {'título': u2_s3 + 'MPS.BR e NBR ISO/IEC', 'ref': rocha, 'det': 'composição = 3 itens'},

        # -------------------------------------------- UNIDADE 3 / SEÇÃO 1 --------------------------------------------
        46: {}
    }
}

# 20: {'título': '', 'ref': None, 'det': None},
keys = list(summary['ebook'].keys())
thread = '-------------------------------------------------------------------------------------------------------------'
# print(keys)
index = 1
while index < keys[-1]:
    print(thread)
    print(f" Título:    || {summary['ebook'][index]['título']}")
    print(f" Referência || {summary['ebook'][index]['ref']}")
    print(f" Detalhe    || {summary['ebook'][index]['det']}")
    index += 1
