

from random import choice
from time import sleep
from sys import getsizeof as size

simbolo_ponto = '•'
simbolo_uniao, simbolo_intersecao = '∪', '∩'

u1_secao_1 = f"""
    [ 09 ] [ item 1 ] ---------------------------------------- Lógica (relação) ----------------------------------------
        • Construção de algoritmos    • Desenvolvimento de programas;
    
    [ 10 ] [ item 2 ] -------------------------------------- Lógica (definições) --------------------------------------
        • Formal    • Transcendental;
    
    [ 10 ] [ item 3 ] ------------------------------------ Lógica (classificações) ------------------------------------
        • Clássica    • Dedutiva    • Indutiva    • Não clássica;
    
    [ 10 ] [ item 4 ] ---------------------------------------- Lógica (conexão) ----------------------------------------
        • Análise de sistemas    • Linguagem de programação    • Sistemas computacionais;
    
    [ 10 ] [ item 5 ] ----------------------------------- Lógica Formal (pionerismo) -----------------------------------
        • Aristóteles;
    
    [ 10 ] [ item 6 ] --------------------------------- Lógica (conceito) (Forbellone) --------------------------------- 
        • Arte de bem pensar    • Ciência das formas de pensamento;
    
    [ 10 ] [ item 7 ] ------------------------------------- Raciocínio (conceito) ------------------------------------- 
        • Forma mais complexa do pensamento;
    
    [ 10 ] [ item 8 ] ---------------------------------- Lógica (objetivo principal) ----------------------------------
        • Correção do raciocínio;
    
    [ 10 ] [ item 9 ] --------------------------------- Lógica Formal (linha do tempo) ---------------------------------
        • Grécia antiga    • Aristóteles    • Matemática;
    
    [ 10 ] [ item 10 ] ---------------------------------- Lógica (objetivo) (Fajardo) ----------------------------------
        • Entender o raciocínio humano;
    
    [ 10 ] [ item 11 ] ----------------------------------- Lógica (objeto de estudo) ----------------------------------- 
        • Ciência da computação    • Tecnologia da informação    • Programação;
    
    [ 10 ] [ item 12 ] ---------------------------------------- Lógica (termos) ----------------------------------------
        • ARGUMENTO    • FALÁCIA    • PREMISA    • PROPOSIÇÃO    • SILOGISMO;
    
    [ 10 ] [ item 13 ] ---------------------------- Lógica - termo - Proposição (conceito) ----------------------------
        • Enunciado declarativo;
    
    [ 11 ] [ item 14 ] ----------------------------- Lógica - termo - Argumento (conceito) -----------------------------
        • Conjuntos de enunciados relacionados entre si;
    
    [ 11 ] [ item 15 ] ------------------------------ Lógica - termo - Falácia (conceito) ------------------------------ 
        • Argumentos logicamente errados;
    
    [ 11 ] [ item 16 ] ----------------------------- Lógica - termo - Premissa (conceito) ----------------------------- 
        • Proposições de base para o raciocínio e silogismo;
    
    [ 11 ] [ item 17 ] ----------------------------- Lógica - termo - Silogismo (conceito) -----------------------------
        • Raciocínio dedutivo em premisas p/ conclusão;
    
    [ 11 ] [ item 18 ] ----------------------------------- Lógica formal (objetivo) -----------------------------------
        • Análise e representação da forma de um argumento p/ sua validação;
    
    [ 11 ] [ item 19 ] ------------------------------------- Lógica formal (info) -------------------------------------
        • Lida com premissas e conclusões, se são V ou F;
    
    [ 11 ] [ item 20 ] ----------------------------------------- Lógica (info) -----------------------------------------
        • Não é seu papel concluir se uma proposição é V ou F
        • Se a premisa é V, pela lógica, a conclusão também é V;
    
    [ 11 ] [ item 21 ] ---------------------------------------- Premisa (info) ---------------------------------------- 
        • Varia entre V ou F, sendo passível de verificação de veracidade;
    
    [ 11 ] [ item 22 ] --------------------------------------- Argumento (info) --------------------------------------- 
        • Pode ser válido ou inválido, sendo passível de verificação da validade;
    
    
    [ 12 ] [ item 23 ] ------------------- Inferência (1. conceito) (2. tipo) (3. info) (4. exemplo) ------------------- 
        1 • Processo que permite chegar a conclusões a partir de premissas, constituindo a argumentação lógica perfeita
        2 • Indutiva e Dedutiva
        3 • Quando é inválida, recebe o nome de FALÁCIA
        4 • Todos os homens são mortais. Elias é homem. Logo, Elias é mortal;
    
    [ 12 ] [ item 24 ] ----------------------------------- Lógica formal (conclusão) -----------------------------------
        • Mostra-se incapaz de analisar argumentos;
    
    [ 12 ] [ item 25 ] ------------------------------------ Linguagem (comunicação) ------------------------------------
        • Sinais, regras e símbolos;
    
    [ 12 ] [ item 26 ] -------------------------------------- Paradoxo (conceito) --------------------------------------
        • Manipulação da linguagem, mas com conclusões lógicas e inverídicas;
    
    [ 13 ] [ item 27 ] --------------------------------- Erro de raciocínio (conceito) ---------------------------------
        • Argumentos válidos e verdadeiros que chegam à conclusões falsas;
    
    [ 13 ] [ item 28 ] -------------------------- Lógica simbólica (1. eventos) (2. objetivo) --------------------------
        1 • Origem no século XIX, com símbolos matemáticos precisos, nomeados equações
        2 • Expressar relações entre premisas;
      
    [ 13 ] [ item 29 ] ----------------------------------- Lógica matemática (info) ----------------------------------- 
        • Foi a pioneira p/ lógica computacional (sistemas digitais);
     
    [ 13 ] [ item 30 ] ------------- Lógica transcendental (1. pioneirismo) (2. ideia) (3. funcionamento) -------------
        1 • Immanuel Kant (livro: Crítica da Razão Pura
        2 • Formação do conhecimento por duas fontes: Sentido vs Pensamento 
        3 • Representações das coisas, não por suas atribuições físicas;
    
    [ 14 ] [ item 31 ] ------------------------------ Conhecimento empírico (posteriori) ------------------------------
        • Obtido pelos sentidos, pela presença real da coisa;
     
    [ 14 ] [ item 32 ] ---------------------------------- Conhecimento puro (priori) ----------------------------------
        • Obtido por representação racional, desvinculado da sensação;
     
    [ 14 ] [ item 33 ] -------------------------- Lógica dedutiva (1. conceito) (2. exemplo) --------------------------
        1 • Uso de premisas gerais p/ alcançar verdades específicas
        2 • Todo Analista de sistemas sabe programar. Mariana é analista de sistemas. Portanto, Mariana sabe programar;
      
    [ 14 ] [ item 34 ] -------------------------- Lógica indutiva (1. conceito) (2. exemplo) -------------------------- 
        1 • Uso de premisas restritas p/alcançar conclusões gerais
        2 • Ana é analista de sistemas e sabe programar. Portanto, todos os analistas de sistemas sabem programar;
    
    [ 14/15 ] [ item 35 ] --------------------------------- Lógica indutiva (problema) --------------------------------- 
        • Um contraexemplo é um fator invalidador, que quebra essa lógica;
    
    [ 15 ] [ item 36 ] ------------------------------------ Lógica clássica (dados) ------------------------------------
        • PIONERISMO || Aristóteles
        • FOCO       || veracidade das conclusões, validade dos argumentos
        • VALORES    || V ou F;
    
    [ 15/16 ] [ item 37 ] ------------------------------------ Lógica não clássica ------------------------------------
        • FUZZY [ valores = 0 ou 1 ]    • MODAL [ valores = V, F, necess. V, necess. F ];
    
    [ 16 ] [ item 38 ] ----------------------------------- Lógica modal (pionerismo) -----------------------------------
        • Lewis;
    
    [ 16 ] [ item 39 ] ----------------------------- Lógica não clássica (características) -----------------------------
        • Base em ling. ricas              (operadores de necessidade e possibilidade)
        • Base em princípios distintos     (nega princ. da identidade)
        • Admissão de semânticas distintas (operadores temporais);
    """.split(';')

u1_secao_2 = f"""
    [ 20 ] [ item 1 ] ------------------------------- Lógica de programação (pionerismo) ------------------------------- 
        • Aristóteles    • George Boole    • Gottlob Frege;
    
    [ 21 ] [ item 2 ] ----------------------------------------- Lógica (objetivos) -------------------------------------
        • Estuda o raciocínio em estrutura e princípios    • Estruturar o pensamento;
     
    [ 21 ] [ item 3 ] -------------------------------------- Lógica (construção) --------------------------------------
        • Base nas premissas    • Raciocínio dedutivo    • Raciocínio indutivo    • Operações lógicas simbólicas;
    
    [ 21 ] [ item 4 ] --------------------------------------- Lógica (períodos) ---------------------------------------
        • Aristotélico    • Booleano    • Atual;
    
    [ 21 ] [ item 5 ] ----------------- Teoria do Silogismo (1. pionerismo) (2. conceito) (3. exemplo) ----------------- 
       1 • Aristóteles    • Vulgo: inferência dedutiva    • Período: entre 390 até 1840
       2 • Argumento conclusivo que ignora a análise de premissas e proposições
       3 • (Premissa)  Todos os brasileiros torcem pelo Brasil. José é brasileiro
           (Conclusão) José torce pelo Brasil;
    
    [ 22 ] [ item 6 ] ---------------------------------------- Lógica (evento) ----------------------------------------
        • Aristóteles acreditava que deveria ser contestada;
    
    [ 22 ] [ item 7 ] --------------------------- Lógica clássica (Aristóteles) (princípios) ---------------------------
        • Identidade        || algo é idêntico a si (lógica pura)    
        • Não contradição   || algo não pode ser duas coisas por vez   
        • Terceiro excluído || algo é ou não algo, não havendo uma terceira via;
    
    [ 23 ] [ item 8 ] ---------------------------------------- Lógica (eventos) ---------------------------------------- 
        • Grécia antiga    • Declínio, ostracismo    • Resurgimento no XII e XIII    • Paradoxo semântico;
    
    [ 23 ] [ item 9 ] -------------------------------------- Paradoxo (conceito) --------------------------------------
        • Argumento com sentido, mas de conclusão contraditória;
    
    [ 24 ] [ item 10 ] -------------------------------------- Lógica (transição) --------------------------------------
        • Iluminismo (séc. XVIII)    • Transição da fé p/ razão    • Alvo da Ciência e Filosofia;
        
    [ 24 ] [ item 11 ] ----------------------------- Lógica formal/simbólica (surgimento) -----------------------------
        • Período Booleano (1840 - 1910);
    
    [ 24 ] [ item 12 ] ----------------------------------- Lógica formal (premissa) -----------------------------------
        • Símbolos computáveis substituem palavras e proposições;
    
    [ 24 ] [ item 13 ] ----------------------------------- Lógica formal (expoentes) -----------------------------------
        • George Boole (1815-64)    • Georg Cantor (1845-1918)    • Gottlob Frege (1848-1925);
        
    [ 24 ] [ item 14 ] --------------------------------- Álgebra booleana (pionerismo) ---------------------------------
        • George Boole    • Criação dos valores binários 0 e 1;
    
    [ 25 ] [ item 15 ] --------------------------------- Algebra booleana (conectivos) ---------------------------------
        • Adição [ou]    • Multiplicação [e];
        
    [ 25 ] [ item 16 ] ---------------------------------- Álgebra booleana (exemplo) ----------------------------------
        • [A] O Brasil é um continente (falso = 0)
        • [B] A África é um continente (verdade = 1)
                
        -> Conectivo [ ou ]: O Brasil é um continente ou a África é um continente = [ A ou B ] = [ 0 + 1 = 1 ] = (V)   
        -> Conectivo [ e ]:  O Brasil é um continente ou a África é um continente = [ A e B  ] = [ 0 x 1 = 0 ] = (F);
    
    [ 25 ] [ item 17 ] ------------------------------- Teoria dos Conjuntos (pionerismo) -------------------------------
        • Georg Cantor    • A teoria deu origem à Álgebra dos Conjuntos;
    
    [ 25 ] [ item 18 ] ------------------------------ Álgebra dos Conjuntos (operadores) ------------------------------
        • União [ símbolo = ∪ ]    • Interseção [ símbolo = ∩ ];
    
    [ 25 ] [ item 19 ] -------------------------------- Álgebra dos Conjuntos (suporte) --------------------------------
        • Lógica formal    • Matemática moderna;
    
    [ 25 ] [ item 20 ] ------------------------------- Lógica tradicional (reformulação) -------------------------------
        • Proposta por Gottlob Frege    • Origem ao Cálculo proposicional e de predicados;
    
    [ 26 ] [ item 21 ] ------------------------- Operadores lógicos (símbolos e significados) -------------------------
        • Negação       [ ~    ] [ não               ]
        • Conjunção     [ ^    ] [ e                 ]
        • Disjunção     [ v    ] [ ou                ]
        • Condicional   [ ->   ] [ se...então        ]
        • Bicondicional [ <--> ] [ se...e somente se ];
             
    [ 26 ] [ item 22 ] --------------------------------- Operadores lógicos (exemplo) ---------------------------------
        • [A] Ana ñ é gaúcha    • [B] Ena ñ é paulista    • [C] Ina dirigir    • [D] Ona beber
        
        SINTAXE: [ ~ A ^ ~ B  ]  TRADUÇÃO: Ana não é gaucha (E) Ena não é paulista       OPERADOR: Conjunção [ ^ ]
        SINTAXE: [ ~ C -> ~ D ]  TRADUÇÃO: (SE) Ina não dirigir, (ENTÃO) Ena não beberá  OPERADOR: Condicional [ -> ];
                
    [ 26 ] [ item 23 ] ----------------------------------- Lógica (período moderno) ----------------------------------- 
        • Início em 1910    • Bertrand Russel (1872-1970)    • Alfred North Whitehead (1861-1947);
    
    [ 26 ] [ item 24 ] --------------------------------- Sistemas formais polivalentes ---------------------------------
        • Desenvolvimento a partir da mesclagem de Lógica clássica e não clássica;
    
    [ 26/27 ] [ item 25 ] -------------------------------- Lógica não clássica (tipos) -------------------------------- 
        • FUZZY    • MODAL    • PARACOMPLETA    • PARACONSISTENTE;
    
    [ 27 ] [ item 26 ] --------------------------------- Lógica fuzzy (funcionamento) --------------------------------- 
        • Tratamento de conceitos vagos, imprecisos, ambíguos
        • Tratamento através de conversão de linguagem humana p/ numérica
        • Tratamento quando há impossibilidade de determinação de V ou F
        
        • EXEMPLO: O posto fica a ALGUNS metros   (termo vago)
                   O clima está PARCIALMENTE seco (termo vago);
    """.split(';')

u1_secao_3 = f"""
    [ 32 ] [ item 1 ] -------------------------------- Lógica (princípios matemáticos) -------------------------------- 
        • Noções de listagem    • Contagem    • Agrupamentos;
    
    [ 33 ] [ item 2 ] ---------------------------------------- Lógica (relação) ---------------------------------------- 
        • Matemática discreta/finita/combinatória;
    
    [ 33 ] [ item 3 ] --------------------------------- Matemática discreta (conceito) --------------------------------- 
        • Ramo da matemática, que estuda objetos e estruturas discretas, finitas e distintas;
             
    [ 33 ] [ item 4 ] -------------------------------- Matemática discreta (objetivos) --------------------------------
        • Contar objetos    • Estudo de relações entre conjuntos    • Análise de algoritmos;
    
    [ 33 ] [ item 5 ] ---------------------------- Matemática discreta (problemas tratados) ----------------------------
        • Contagem   || quantidade de arranjos e configurações existentes
        • Existência || arranjos satisfazendo propriedades
        • Otimização || melhor configuração;
        
    [ 33 ] [ item 6 ] -------------------------------- Matemática discreta (princípio) -------------------------------- 
        • Princípio da contagem;
    
    [ 33 ] [ item 7 ] -------------------- Matemática discreta (Princípio da contagem) (objetivos) --------------------
        • Contar recursos finitos
        • Verificar eficácia de algoritmo (consumo & runtime);
    
    [ 34 ] [ item 8 ] --------------------------------- Lista (conceito) (Scheinerman) --------------------------------- 
        • (vulgo: UPLA)    • Sequência ordenada de objetos);
    
    [ 34 ] [ item 9 ] ---------------------------------------- Lista (detalhes) ---------------------------------------- 
    SÍMBOLO: []       SEPARADOR: ,       ORDEM: importa       REPETIÇÃO: permitível;
    
    [ 34 ] [ item 10 ] ------------------------------------ Listas (nomemclaturas) ------------------------------------
        • ELEMENTOS    || dados/índices de uma lista                                
        • COMPRIMENTO  || quantidade de elementos de uma lista
        • PAR ORDENADO || quantidade equivalente à uma lista com 2 elementos;
          
    [ 34 ] [ item 11 ] ----------------------------------------- Lista (tipos) -----------------------------------------
        • Algarismos (ex: números)       • Letras (ex: nomes)       • Ambos (ex: placa de um veículo);
    
    [ 36/37 ] [ item 12 ] ---------------------------------- Scheinerman (princípio) ---------------------------------- 
        • Princípio da multiplicação para listas de par ordenados/com dois elementos;
    
    [ 36/37 ] [ item 13 ] --------------------------- Princípio da multiplicação (evolução) --------------------------- 
        • Fatorial    • Fórmula = inteiro!    • (exemplo) 3! = 3 x 2 x 1 = 6;
    
    [ 37 ] [ item 14 ] --------------------------------- Árvore de decisão (objetivos) ---------------------------------
        • Forma de ordenar objetos de lista
        • Mapear resultados por escolha
        • Tomar decisões (condução de diálogos)
        • Visualizar ramificações e consequências (mapear algoritmos)
        • Criar planos de ação;
    
    [ 37/38 ] [ item 15 ] -------------------------------- Árvore de decisão (formação) -------------------------------- 
        • Um nó raiz se divide em nós alternativos com objetivo de chegar a um resultado;
    
    [ 38 ] [ item 16 ] ---------------------------------- Árvore de decisão (tarefas) ---------------------------------- 
        • Determinar a quantidade de listas
        • Descriminar listas não otimizadas (extensas);
        
    [ 38 ] [ item 17 ] --------------------------------- Árvore de decisão (problema) ---------------------------------
        • Listas extensas podem ter um desenho complexo, sendo passível de descarte;
    
    [ 39 ] [ item 18 ] ------------------------------------------ Informação ------------------------------------------
        • O Princípio multiplicativo ou Árvore de decisão são meios de decisão de formação de um objeto de lista;
    
    [ 39 ] [ item 19 ] ------------------------------ Matemática discreta (agrupamentos) ------------------------------
        • São fórmulas    • Arranjos    • Permutações    • Combinações;
    
    [ 39 ] [ item 20 ] ------------------------------------ Agrupamento de arranjo ------------------------------------
        • Formado por 'p' elementos distintos escolhidos a partir de um conjunto de 'n' elementos
        • A ordem importa, se mudada, cria novos agrupamentos
        • SUPOSIÇÕES ||    (n = 4) (p = 2)
        • FÓRMULA    ||    An.p = n! / (n - p)! 
        • PRÁTICA    ||    A4.2 = 4! / (4 - 2)!     4! / 2!     4 x 3 x 2 x 1 / 2 x 1     24 / 2 = 12;
    
    [ 40 ] [ item 21 ] ----------------------------------- Agrupamento de permutação -----------------------------------
        • Sua fórmula original [ Pn = n! / (n - n)! ] foi simplificada para fatorial [ n! ];
        
    [ 40 ] [ item 22 ] ----------------------------------- Agrupamento de combinação -----------------------------------
        • Formado por 'p' elementos distintos escolhidos a partir de um conjunto de 'n' elementos
        • A ordem não importa, se mudada, é formado o mesmo agrupamento
        • SUPOSIÇÕES || (n = 5) (p = 2)
        • FÓRMULA    || Cn,p = n! / p!(n - p)! 
        • PRÁTICA    || C5,2 = 5! / 2!(5 - 2)!   5! / 2!3!   5x4x3x2x1 / (2x1)(3x2x1)   120 / 2.6   120/12 = 10;
    """.split(';')

# ----------------------------------------------------------------------------------------------------------------------

u2_secao_1 = f"""
    [ 49 ] [ item 1 ] ------------------------------------- Álgebra dos Conjuntos -------------------------------------
        • Linguagem clara    • Desprezo por equívocos    • Atuante na computação;
    
    [ 50 ] [ item 2 ] ---------------------------------- Teoria de Conjuntos (termos) ----------------------------------
        • Subconjunto    • Igualdade de conjuntos    • Sentenças    • Diagramas    • Quantificadores    • Pertinência
        • Continência;
    
    [ 51 ] [ item 3 ] -------------------------------------- Conjunto (conceito) --------------------------------------
        • Coleções não ordenadas de objetos que podem ser, de alguma forma, relacionados;
    
    [ 51 ] [ item 4 ] --------------------------------- Conjunto (tipos de declaração) ---------------------------------
        • A = {1, 2, 3, 4, 5}    • B = {{1, 2, 3...}}    • C = {{0 < x < 6}}    
        • Listagem completa      • Listagem reduzida     • Listagem por propriedade (melhor p/ uso em cjs. grandes;
    
    [ 52 ] [ item 5 ] ------------------------------ Conjunto (representação alternativa) ------------------------------
        • Diagramas de John Venn    • Círculos eulerianos;
    
    #i
    [ 52/53 ] [ item 6 ] ------------------------------------- Conjunto (relações) -------------------------------------
        • Pertinência     (Letra E oval)                          SIGNIFICADO: é membro, pertence, é elemento
        • Não pertinência (Letra E oval com corte transversal)    SIGNIFICADO: ñ é membro, ñ pertence, ñ é elemento;
    
    [ 53 ] [ item 7 ] ------------------------------ Conjunto (cardinalidade) (conceito) ------------------------------
        • Quantidade de elementos de um conjunto    • Símbolo: |Conjunto| = int    • Ex: A = {1, 2, 3}    |A| = 3;
    
    [ 53 ] [ item 8 ] ----------------------------------- Conjunto (tipos e exemplo) -----------------------------------
        • A = {'abril', 'junho', 'setembro', 'novembro'} (Conjunto finito)   || dados logicamente contáveis
        • B = {{1, 4, 9, 16, 25,…}}                      (Conjunto infinito) || quadrados perfeitos são infinitos
        • C = {{x > 3 e x < 4}}                          (Conjunto vazio)    || satisfação impossível;
    
    #i
    [ 53 ] [ item 9 ] ---------------------------- Conjunto (cardinalidade vazia) (símbolo) ----------------------------
        • Letra O com corte transversal;
    
    #i
    [ 53/54 ] [ item 10 ] ----------------------------------- Matemática (conjuntos) -----------------------------------
        • Não negativos (N)    • Inteiros (Z)    • Racionais (Q)    • Reais (R)    • Complexos (C);
    
    [ 54/55 ] [ item 11 ] --------------- Teoria dos Conjuntos (quantificador) (1. tipos) (2. exemplos) ---------------
        1 • Universal     • Letra A de cabeça para baixo    • para todo, qualquer que seja    
        1 • Existência    • Letra E espelhada               • há, existe 
        2 • [ Universal ]  Todo inteiro é par ou ímpar     
        2 • [ Existência ] Existe um número natural que é primo e par;
    
    [ 55 ] [ item 12 ] -------------------------- Quantificador universal (símbolo) (exemplo) --------------------------
        • A invertido    x    E oval    Z    [ TRADUÇÃO: Qualquer que seja x pertence aos inteiros ];
    
    #i
    [ 55 ] [ item 13 ] -------------- Subconjunto (1. conceito) (2. símbolo) (3. exemplo) (4. conclusão) --------------
        1 • Conjunto contido em outro
        2 • Letra C sublinhada
        3 • A = {1, 2, 3}    B = {1, 2, 3, 4, 5}    
        4 • A é subconjunto de B, pois todos os seus elementos estão em B;
    
    [ 56 ] [ item 14 ] -------------------------------- Subconjunto (contagem) (regras) --------------------------------
        • SUPOSIÇÃO              || A = {{a, b, c}}
        • SUBCONJUNTOS POSSÍVEIS || 3, sendo eles {{a, b}}, {{a, c}}, {{b, c}} 
        • LÓGICA                 || {{a, b}} & {{b, a}} não conta como diferente, assim como {{a, c}} & {{c, a}}...
        • OBSERVAÇÃO             || Em contagem de subconjunto, vazio conta como 1;
    """.split(';')

u2_secao_2 = f"""
    #i
    [ 62 ] [ item 1 ] -------------------------------- Teoria de conjuntos (operações) --------------------------------
        • União               (letra U)             [ p. 62 ]
        • Interseção          (letra U invertida)   [ p. 62 ]
        • Diferença           (traço de parágrafo)  [ p. 65 ]
        • Diferença simétrica (triângulo)           [ p. 65 ];
    
    [ 63 ] [ item 2 ] --------------------- Teoria de conjuntos (operações) (União vs Intervenção) ---------------------
        • A = {3, 4, 5, 6, 7}    B = {1, 2, 3, 4, 5} 
                    
        • A e B (união)      -> {1, 2, 3, 4, 5, 6, 7} -> junção de elementos diferentes de A e B (exclusão de repetidos)
        • A e B (interseção) -> {3, 4, 5}             -> junção de elementos iguais de A e B;
    
    [ 64 ] [ item 3 ] ----------------------- Álgebra de conjuntos (leis básicas) (propriedades) -----------------------
        • Comutativas    • Associativas    • Conjunto vazio    • Distributivas    • Idempotência;
    
    [ 65 ] [ item 4 ] --------------------- Teoria de conjuntos (operações) (Diferença) (exemplo) ---------------------
        • A = {1, 2, 3, 4, 5}    B = {4, 5, 6, 7}
                    
        • A para B (diferença) -> (A - B) = {1, 2, 3} [ existe em A, mas não em B ]
        • B para A (diferença) -> (B - A) = {6, 7}    [ existe me B, mas não em A ];
    
    [ 65 ] [ item 5 ] -------------- Teoria de conjuntos (Diferença simétrica) (1. conceito) (2. exemplo) --------------
        1 • Junção das 2 situações possíveis de diferença            
        2 • A = {1, 2, 3, 4, 5}    B = {4, 5, 6, 7}
                    
        • DIFERENÇA (A - B) = {1, 2, 3} existe em A, mas não em B 
        • DIFERENÇA (B - A) = {6, 7} existe me B, mas não em A
        • DIFERENÇA SIMÉTRICA = {1, 2, 3, 6, 7};
    
    [ 66 ] [ item 6 ] ----------------- Conjunto (operações) (método de contagem) (Inclusão-exclusão) -----------------
        • Usado em conjuntos finitos e grandes
        • Fórmula (parte 1)    • |A| + |B|    • Soma da cardinalidade de um conjunto A com um B
        • Fórmula (parte 2)    • − |A ∩ B|    • Subtração da cardinalidade da interseção de A com B 
        
        • FóRMULA: |A ∪ B| = |A| + |B| − |A ∩ B|;
        
    [ 66 ] [ item 7 ] ------------ Conjunto (operações) (método de contagem) (Inclusão-exclusão) (exemplo) ------------
        • A = 280 (empregados que usam navegador A)
        • B = 300 (empregados que usam navegador B)
        • C = 120 (empregados que usam navegador A e B)
                    
        • CÁLCULO: |A ∪ B| = |A| + |B| − |A ∩ B|    |A ∪ B| = 280 + 300 - 120    |A ∪ B| = 460;
    
    #i
    [ 68 ] [ item 8 ] Conjunto vazio é um conjunto disjunto    • SÍMBOLO: Zero com corte transversal;
    """.split(';')

u2_secao_3 = f"""
    [ 74 ] [ item 1 ] -------------------------- Teoria dos Conjuntos (operação alternativa) --------------------------
        • Complemento ou Complementar de um conjunto;

    [ 74 ] [ item 2 ] -------------------------- Teoria dos Conjuntos (complemento) (exemplo) --------------------------
        • A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}    • B = {1, 2, 3, 5, 8, 9}

        LÓGICA    || Na sintaxe de COMPLEMENTO, o segundo conjunto da sintaxe é o alvo
        EXEMPLO   || Na sintaxe [ Complemento de B para A ] o alvo é A 
        PRÁTICA   || Na sintaxe [ Complemento de B para A ] o resultado do COMPLEMENTO é {4, 6, 7, 10}
        PRÁTICA   || Todos os elementos exclusivos de A em relação ao B
        CONCLUSÃO || Na sintaxe [ Complemento de B para A ] o primeiro conjunto é sempre subconjunto do segundo;

    [ 75 ] [ item 3 ] --------------------------------- Conjuntos disjuntos (exemplo) ---------------------------------
        • A = {2, 7, 9, 13}     • B = {3, 5, 10, 12}    • Nem A ou B são subconjuntos de si, são conjuntos disjuntos;

    [ 76 ] [ item 4 ] ------------------------------- Conjunto (complemento) (símbolos) ------------------------------- 
        • Traço, vírgulas ou C (elevado)    • A = {12, 13, 14, 15, 16, 17, 18}    • B = {12, 13, 14, 15}
        • Ac = Complemento de B para A = {16, 17, 18};

    [ 77 ] [ item 5 ] ---------------------------------- Operação binária (conceito) ----------------------------------
        • Operação sobre dois números;

    [ 78 ] [ item 6 ] -------------------------------- Plano cartesiano (representação) --------------------------------
        • Ângulo de 90%, onde o eixo X é a parte horizontal e Y é a parte vertical;

    [ 79 ] [ item 7 ] ----------------------------- Plano cartesiano (produto cartesiano) ----------------------------- 
        • A = {4, 5, 6}     • B = {6, 7, 8}

        • Produto cartesiano A x B = {(4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8), (6, 6), (6, 7), (6, 8)}      
        • Produto cartesiano B x A = {(6, 4), (6, 5), (6, 6), (7, 4), (7, 5), (7, 6), (8, 4), (8, 5), (8, 6)};

    [ 79 ] [ item 8 ] ----------------------------------- Produto cartesiano (info) -----------------------------------
        • Não é uma operação comutativa;

    [ 79 ] [ item 9 ] --------------------- Plano cartesiano (produto cartesiano vs cardinalidade) ---------------------     
        • A = {4, 5, 6}     • B = {6, 7, 8}

        • |A x B|      • Representação da cardinalidade do plano cartesiano de A X B
        • |A| x |B|    • Representação da cardinalidade de A x B

        • |A x B|      • |(4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8), (6, 6), (6, 7), (6, 8)| = |9|
        • |A| x |B|    • |{4, 5, 6}| x |{6, 7, 8}| = |3| x |3|                                    = |9|;

    [ 79 ] [ item 10 ] ---------------------- Plano cartesiano (Diagrama de Venn) (representação) ----------------------
        • A = {2, 3}     • B = {4, 5}

        PLANO CARTESIANO DE A X B           || {(2, 4), (2, 5), (3, 4), (3, 5)}
        REPRESENTAÇÃO DO DIAGRAMA (parte 1) || Dois balões, representando respectivamente os conjunto A e B, separados
        REPRESENTAÇÃO DO DIAGRAMA (parte 2) || Os elementos do conjunto A apontando setas aos elementos do conjunto B; 

    [ 80 ] [ item 11 ] -------------------------------------- (CONTEÚDO DO LIVRO) --------------------------------------
       • Vamos aqui utilizar um Diagrama de Venn para demonstrar uma relação arbitrária entre dois conjuntos A e B;
    """.split(';')

# ----------------------------------------------------------------------------------------------------------------------

u3_secao_1 = f"""
    [ 92/93 ] [ item 1 ] ------------------------------ Premissas e conclusões (exemplo) ------------------------------
        • “É lógico que Pedro será aprovado nos exames, pois ele é inteligente e estuda muito e todos os alunos
           inteligentes e estudiosos são aprovados”
         
        Premissa 1 || Pedro é inteligente           
        Premissa 2 || Pedro estuda muito
        Premissa 3 || Todos os alunos inteligentes e estudiosos são aprovados
        Conclusão  || Pedro será aprovado;
    
    [ 93 ] [ item 2 ] ---------------------------------- Argumento (características) ----------------------------------
        • Nem sempre está numa frase    • Sempre possui uma conclusão;
    
    [ 93 ] [ item 3 ] ------------------------------------- Argumento (inválidos) -------------------------------------
        • Quando não há conclusividade    • EX: perguntas, exclamações;
    
    [ 93 ] [ item 4 ] ---------------------------------- Lógica (objetivo de análise) ----------------------------------
        • Se a sentença é argumento    • Se a sentença pode ser classificada em V ou F;
    
    [ 94 ] [ item 5 ] ----------------------------- Proposição (1. conceito) (2. detalhe) -----------------------------
        • Sentença declarativa que pode ser classificada em V ou F (não ao mesmo tempo)
        • Também pode ser classificada como proposição binária (0 ou 1);
    
    [ 94 ] [ item 6 ] ------------------------------- Sentença (condição da proposição) -------------------------------
        • Não haver dúvida sobre o resultado ser V ou F;
    
    [ 94 ] [ item 7 ] ------------------------------------- Proposição (objetivo) -------------------------------------
        • Sustentar um argumento e sua conclusão;
    
    [ 94 ] [ item 8 ] -------------------------------------- (CONTEÚDO DO LIVRO) --------------------------------------  
        • Diagramas de Euler;
    
    [ 95 ] [ item 9 ] ------------------------------------ Proposição (observação) ------------------------------------
        • Proposições devem seguir os princípios:    • Identidade    • Não contradição    • Terceiro exlcuído;
    
    [ 95 ] [ item 10 ] -------------------------- Proposição (1. classificação) (2. exemplos) --------------------------
        1 • Simples      • possui somente uma afirmação
        1 • Composta     • possui pelo menos duas proposições simples (ligadas por um conectivo lógico)
        
        2 • [ proposição simples  ]    • A = 11 é um número ímpar         
        2 • [ proposição simples  ]    • B = 11 é um número primo         
        2 • [ proposição composta ]    • C = 11 é um número ímpar e primo [ conector lógico E ];
    
    [ 96/97 ] [ item 11 ] -------------------- Proposição (relação) (conectores/conectivos lógicos) --------------------
        • e                [ conjunção     ] [ AND ] [ ^        ] [ OBS: Todas as proposições envolvidas devem ser V ]
        • ou               [ disjunção     ] [ OR  ] [ v        ] [ OBS: Se 1 entre outras proposições for V ] (p. 98)
        • não              [ negação       ] [ NOT ] [ ~, <-, ‘ ] [ OBS: inversão de uma proposição ]          (p. 99)
        • se...então       [ condicional   ] [     ] [ ->       ]                                              (p. 106)
        • se, e somente se [ bicondicional ] [     ] [ <->      ]                                              (p. 108);
    
    [ 97 ] [ item 12 ] -------------------- Proposição (sintaxes alternativas p/ conector lógico E) --------------------
        • Mas    • todavia    • contudo    • no entanto    • visto que    • enquanto    • além disso    • embora;
    """.split(';')

u3_secao_2 = f"""
    #i
    [ 105/106 ] [ item 1 ] ---------------- Conectivo lógico de disjunção (ou) (inclusivo & exclusivo) ----------------
        • [A] João é estudante    • [B] João é trabalhador    • [C] João é paulista    • [D] João é carioca
                     
        PROPOSIÇÃO DE DISJUNÇÃO INCLUSIVA || João é estudante ou é trabalhador [ 1 ou ambas podem ser V ]
        PROPOSIÇÃO DE DISJUNÇÃO EXCLUSIVA || João é paulista ou é carioca      [ 1 é V ou a outra, não ambas ]
        
        PROPOSIÇÃO DE DISJUNÇÃO INCLUSIVA || O símbolo é: [ v ]
        PROPOSIÇÃO DE DISJUNÇÃO EXCLUSIVA || O símbolo é: [ v sublinhado ];
    
    [ 106 ] [ item 2 ] ----------------- Conectivo condicional (se...então) (proposição) (categorias) -----------------
        • [A] = João estuda para a prova (antecedente)     • [B] = João passa de ano (consequente)
                  
        • LÓGICA   || A proposição CONSEQUENTE é condicionada pelo proposição ANTECEDENTE
        • SINTAXE  || A -> B
        • OBS      || A proposição CONSEQUENTE não pode ser falsa, apenas a ANTECEDENTE;
    
    [ 108 ] [ item 3 ] ------------------ Conectivo condicional (se...então) (sintaxes alternativas) ------------------
        • SINTAXE                           || A -> B
        • SINTAXE EM ORDEM NORMAL (A -> B)  || condicional -> logo -> só se -> somente se -> suficiente -> basta para
        • SINTAXE EM ORDEM INVERSA (B -> A) || segue de -> necessária;
    
    [ 108/109 ] [ item 4 ] -------------------------- Conectivo (bicondicional) (satisfação) --------------------------
        • Valores lógicos idênticos, tanto para (FF ou VV);
    
    [ 109 ] [ item 5 ] ------------------------------------- Fórmula bem formulada -------------------------------------
        • Fórmula que segue as regras de sintaxe (well-formed formula);
    
    [ 110 ] [ item 6 ] ------------------------- Cálculo proposicional (1. info) (2. exemplo) -------------------------
        1 • Os parênteses são delimitadores que indicam quais operações devem ser efetuadas primeiro
        2 • (2 + 3) * 5    • A adição é feita antes da multiplicação, devido ao parênteses    • página 109;
        
    [ 110 ] [ item 7 ] --------------------------- Conectores lógicos (ordem de procedência) ---------------------------
        • Se na operação há parênteses simples ou aninhados, são fetuados primeiro os aninhados, seguidos dos simples
        • Ordem de precedência: Negação [<-], Conjunção [^] e disjunção [v], condicional [->], bicondicional [<->]
        
    [ 111 ] [ item 8 ] ------------------------------- Fórmula bem formulada (valoração) -------------------------------
        • Deve ser feita em etapas, seguindo a ordem de precedência, assim como acontece em uma fórmula matemática;
     
    #i   
    [ 111 ] [ item 9 ] ------------------------------ Equivalência lógica (demonstração) ------------------------------
        • SÍMBOLO: <=>    • é diferente do bicondicional [ <-> ]
        • A <-> B    • (A -> B) ^ (B -> A)    
        • As duas fórmulas acima são equivalentes, pois o resultado da fórmula bicondicional é igual as combinações 
          condicionais dos itens, e isso é uma equivalência lógica;
    """.split(';')

u3_secao_3 = f"""
    [ 121 ] [ item 1 ] -------------------------------- Lógica (validação de argumento) --------------------------------
        •  Por regras de equivalência e inferência lógica (permitem avaliar a relação entre hipóteses e conclusão)
        •  Regras:    • Consequência lógica    • Dedução lógica    • Conclusão lógica    • Implicação lógica;
        
    [ 121 ] [ item 2 ] --------------------------- Proposição & Argumento (lógicas inversas) ---------------------------  
        • Uma PROPOSIÇÃO pode ser V ou F, mas não pode ser classificada como VÁLIDA ou INVÁLIDA    
        • Um ARGUMENTO segue a lógica inversa;
        
    [ 121/122 ] [ item 3 ] -------------------------------- Lógica formal (tautologia) --------------------------------
         • Tautologia é um resultado onde entradas possíveis de uma fórmula são todas V (regra de equivalência)
         • Devemos nos basear apenas nas regras p/ validar um argumento e não no conteúdo (se ele é ou não tautologia);
         
    [ 123 ] [ item 4 ] ------------------- Lógica Proposicional (regras de equivalência de dedução) -------------------
        • Comutatividade (com)               • [ Q v P               ]    [ Q ^ P       ]
        • Associatividade (ass)              • [ P v (Q v R)         ]    [ P ^ (Q ^ R) ]  
        • Leis de De Morgan (De Morgan)      • [ ¬ P ^ ¬ Q           ]    [ ¬ P v ¬ Q   ]
        • Condicional (cond)                 • [ ¬ P v Q             ]
        • Dupla negação (dn)                 • [ <- (<- P)           ]  
        • Definição de equivalência (que)    • [ (P -> Q) ^ (Q -> P) ];
        
    [ 124/125/126 ] [ item 5 ] ---------------- Lógica Proposicional (regras de inferência de dedução) ----------------         
        • Não é uma tautologia (resultados equivalentes VV ou FF)
        
        1 • Modus Ponens (MP)     • (P => Q) ^ P => Q               • Implicação & conjunção
        2 • Modus Tollens (MT)    • (P => Q) ^ ¬Q => ¬P             • Implicação, conjunção e negação
        3 • Silogismo hipotético  • (P => Q) ^ (Q => R) => (P -> R) • Implicação, conjunção, conclusão
          • Simplificação         • Inverso da conjunção, separando 2 proposições
          • Adição                • Adicina uma nova proposição por uma conjunção
        
        1 • Implicação prova que a consequência é V quando a premissa é V        
        2 • Implicação prova que a consequência é F quando a premissa é F
        3 • O resultado pode ser inferido do antecedente da 1a para a consequente da 2a proposição;        
    """.split(';')

# ----------------------------------------------------------------------------------------------------------------------

u4_secao_1 = f"""
    [ 138 ] [ item 1 ] -------------------------------------- Proposição (regra) --------------------------------------
        • Sempre é binária (V ou F) (1 ou 0);
        
    [ 139 ] [ item 2 ] ------------------------------ Proposição (cálculo de quantidade) ------------------------------
        • 2 elevado a n    • 2 = número de tipos de preposição (V ou F)    • n = quantidade de proposições
        • Lógica: duas proposições geram 4 linhas na Tabela Verdade
        • Quanto mais proposições, mais linhas, ou seja, 2 ** 3 = 8 linhas, 2 ** 4 = 16 linhas;
    
    [ 139 ] [ item 3 ] ---------------------------------- Tabela Verdade da conjunção ----------------------------------
        • Operação binária entre duas proposições    • Satisfação: todas as proposições V    • ^;
    
    [ 140 ] [ item 4 ] --------------------------- Lógica formal (construção de algoritmos) ---------------------------
        • O conector AND serve para tomada de decisões;
    
    [ 141 ] [ item 5 ] ---------------------------------- Tabela Verdade de disjunção ----------------------------------
        • Operação binária entre duas proposições    • Satisfação: uma proposição V    • v;
    
    [ 143 ] [ item 6 ] ---------------------------------- Tabela verdade para negação ----------------------------------
        • Operação de inversão de uma entrada ou do valor da operação    
        • ~ ou <--
        • Normalmente relacionado com parêntes
        • A = V    • B = F    C = <-- (A ^ B)    C = - (F)    C = V;
    """.split(';')

u4_secao_2 = f"""
    [ 150 ] [ item 1 ] ----------------------------------- Tabela Verdade (conceito) -----------------------------------
        • Método para extração de resultados
        • Produz fórmulas para testar todos os resultados de todas as combinações possíveis de entradas (V ou F)
        • As fórmulas compõem proposições e operadores lógicos (NOT, AND, OR)
        • Proposições mais comuns: conjunção, disjunção, negação;
        • Proposições menos comuns: condicional (implicação), bicondicional;
    
    [ 150/151 ] [ item 2 ] --------------------------------- Proposição (condicional) ---------------------------------
        • São 2 proposições, a da direita é a ANTECEDENTE e a da esquerda é a CONSEQUENTE, 
        • A interação entre elas gera uma conclusão, que é uma nova proposição
        • [A] há uma falha na rede elétrica (antecedente)    • [B] a chave central irá desligar (consequente)
        • A -> B    • A é condicão de B    • B está condicionado a A
        • Satisfação: todas as proposições devem ser V / proposição antecedente F;
    
    [ 153 ] [ item 3 ] ------------------------------------ Fórmulas (definições) ------------------------------------
        • Tautologia   (todas as proposições V)
        • Contradição  (todas as proposições F)
        • Contingência (algo que não é tautologia nem contradição);
    
    [ 155 ] [ item 4 ] ---------------------------------- Equivalências tautológicas ----------------------------------
        • Comutativa    • Associativa    • Distributiva;
    
    [ 157 ] [ item 5 ] ------------------------------------ Leis de Morgan (teoria) ------------------------------------
        • A negação de uma disjunção é equivalente à negação de cada uma das proposições em uma conjunção
        • A negação de uma conjunção é equivalente à negação de cada uma das proposições em uma disjunção;
    """.split(';')

u4_secao_3 = f"""
    [ 166 ] [ item 1 ] ---------------------------------- Tabela Verdade (aplicação) ----------------------------------
        • Em algoritmos, que são sequências de instruções que buscam resolver algum problema da vida real
        • A aplicação se dá por estruturas condicionais;
    
    [ 171 ] [ item 2 ] ------------------------------ Programação (estrutura condicional) ------------------------------
        • C      || se = if / então = chaves || conjunção = &&  || diferença = != || equivalência é ==
        • Java   || se = if / então = chaves || conjunção = &&  || diferença = != || equivalência é ==
        • Python || se = if / então = :      || conjunção = and || diferença = != || equivalência é ==;
    
    [ 171 ] [ item 1 ] --;
    """.split(';')

if __name__ == '__main__':

    from metodos_bdd.bdd import mtd_paint_random

    print(size(u1_secao_1))

    u1_s1 = 'Unidade 1 - SEÇÃO 1 = FUNDAMENTOS DE LÓGICA (página 9 a 16)'
    u1_s2 = 'Unidade 1 - SEÇÃO 2 = EVOLUÇÃO DA LÓGICA (página 20 a 27)'
    u1_s3 = 'Unidade 1 - SEÇÃO 3 = PRINCÍPIOS MATEMÁTICOS (página 32 a 42)'

    u2_s1 = 'Unidade 2 - SEÇÃO 1 = TEORIA DOS CONJUNTOS (página 50 a 57)'
    u2_s2 = 'Unidade 2 - SEÇÃO 2 = ÁLGEBRA DE CONJUNTOS (página 61 a 68)'
    u2_s3 = 'Unidade 2 - SEÇÃO 3 = APLICAÇÔES DE TEORIA DOS CONJUNTOS (página 73 a 81)'

    u3_s1 = 'Unidade 3 - SEÇÃO 1 = INTRODUÇÃO À LÓGICA PROPOSICIONAL (página 89 a 100)'
    u3_s2 = 'Unidade 3 - SEÇÃO 2 = CONECTIVOS E CLASSIFICAÇÂO TEXTUAL (página 104 a 113)'
    u3_s3 = 'Unidade 3 - SEÇÃO 3 = MÉTODOS DEDUTIVOS E INFERÊNCIA LÓGICA (página 119 a 127)'

    u4_s1 = 'Unidade 4 - SEÇÃO 1 = CONSTRUÇÃO DA TABELA VERDADE (página 135 a 144)'
    u4_s2 = 'Unidade 4 - SEÇÃO 2 = RESULTADOS NA TABELA VERDADE (página 149 a 157)'
    u4_s3 = 'Unidade 4 - SEÇÃO 3 = APLICAÇÕES TABELA VERDADE (página 162 a 171)'

    while True:

        print(u3_s3, mtd_paint_random(label=choice(u3_secao_3)))
        sleep(0.01)
        #
        # print(u1_s2, ink(choice(u1_secao_2)))
        # sleep(10)
        #
        # print(u1_s3, ink(choice(u1_secao_3)))
        # sleep(10)
        #
        # print(u2_s1, ink(choice(u2_secao_1)))
        # sleep(10)
        #
        # print(u2_s2, ink(choice(u2_secao_2)))
        # sleep(10)
        #
        # print(u2_s3, ink(choice(u2_secao_3)))
        # sleep(10)
        #
        # print(u3_s1, ink(choice(u3_secao_1)))
        # sleep(10)
        #
        # print(u3_s2, ink(choice(u3_secao_2)))
        # sleep(0.5)
