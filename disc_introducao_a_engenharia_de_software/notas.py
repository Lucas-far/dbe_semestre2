

from random import choice
from time import sleep

# ...•
# pressman = 'Pressman (2006)'
# sommerville = 'Sommerville (2011)'
# zanin = 'Zanin et al. (2018)'

u1_secao_1 = f"""
    [ item 1 ] ----------------------------------- Engenharia de software (conceito) -----------------------------------
        • (Pressman, MAXIM, 2016) Conjunto de métodos ou práticas, com ferramentas que possibilitam o desenvolvimento de
           softwares;
    
    [ item 2 ] ------------------------------- Engenharia de software (características) -------------------------------  
        • Dinâmica    • Agregadora    • Processos refinados e ágeis    • Contribuinte ao desenvolvimento da Computação
        • Interpretada como ciência    • Mutabilidade constante;
        
    [ item 3 ] --------------------------------- Engenharia vs Engenharia de software ---------------------------------
        • Engenharia             = desenvolvimento de um projeto e à manufatura de um artefato        
        • Engenharia de software = não passa por uma manufatura tradicional, mas possui situações particulares que
          necessitam de soluções especializadas; 
          
    [ item 4 ] ----------------------------------------- Software (conceitos) -----------------------------------------
        • Instruções          || programas de computador, que, quando executadas, produzem a função desejada
        • Estruturas de dados || possibilitam que os programas manipularem a informação de forma adequada
        • Documentação        || informação descritiva relativa ao sistema (física/virtual);
        
    [ item 5 ] -------------------------------- Engenharia de software (matéria-prima) --------------------------------
        • Instruções    • Estruturas de dados    • Documentação;   
        
    [ item 6 ] ------------------------------------------- Termo mencionado ------------------------------------------- 
        • IEEE computer society    • Propositor dos princípios relacionados a Engenharia de Software; 
         
    [ item 7 ] --------------------------- Princípios da Engenharia de Software (objetivos) ---------------------------
        • Ajudar na estruturação dos processos    • Padronização de soluções (SWEBOK 
                                                                              Software Engineering Body of Knowledge);
                                                                              
    [ item 8 ] ---------------------------------- Engenharia de software (princípios) ---------------------------------- 
        1 • Organização hierárquica    2 • Formalidade    3 • Completeza    4 • Dividir para conquistar
        5 • Ocultação                  6 • Localização    7 • Integridade conceitual    8 • Abstração 
        
        1 • Uma proposta de solução/organização para tratar um problema deve estar disposto em formato hierárquico, como
            em uma estrutura de árvore, crescente em detalahamento
                                    
        2 • A abordagem na solução de um problema deve ser rigorosa, metódica e padronizada
        
        3 • Verificação rigorosa se a solução contempla todos os elementos de um problema
        
        4 • Necessidade da divisão de um problema complexo em partes menores, afim de facilitar seu gerenciamento
                                    
        5 • Módulos devem manter ocultas informações não essenciais, deixando apenas as informações necessárias para o
            funcionamento
                      
        6 • Itens logicamente relacionaos em um sistema, devem compartilhar o mesmo espaço
        
        7 • Deve haver coerência ao seguir uma filosofia e arquitetura de um projeto
        
        8 • Profissional que consegue aplicar foco em aspectos essenciais, para resolver problemas de maior grandeza,
            ignorando temporariamente os menos relevantes;
            
    [ item 9 ] ----------------------------------------- Software (conceito 2) -----------------------------------------
        • Pressmann e Maxim (2016)    • Produto que profissionais de software desenvolvem e dão suporte a longo prazo,
                                        sendo programas executáveis com conteúdos (dados e informações geradas conforme
                                        a execução do programa acontece) e informações descritivas (documentação);
                                        
    [ item 10 ] ----------------------------------------- Software (conquista) -----------------------------------------
        • Tornou-se um produto relevante no mercado e um veículo para a distribuição de informação;
        
    [ item 11 ] -------------------------- Desenvolvimento de software (detalhes históricos) --------------------------
        • Década de 1960 (crise do software)    
        • Inaptidão em atender demandas, processos falhos, manutenção difícil
        • Falta de confiança pelo imprecisão nas estimativas de custo e de prazo    
        • Precariedade de comunicação entre clientes e equipes de desenvolvimento 
        • Pobre levantamento de requisitos
        • Métricas sem avaliações seguras;
        
    [ item 12 ] --------------------------------- Desenvolvimento de software (mitos) ---------------------------------
        • Mito do gerenciamento = conteúdos teóricos bem organizados serão suficientes para o sucesso de um software
                                  um atraso na entrega de um software será minimizado pelo aumento da equipe
                                  terceirizar o desenvolvimento de um software, sem a necessidade de gerenciamento    
        
        • Mito do cliente = um cliente oferecendo uma definição geral dos objetivos de um software já tornam possível 
                            o início de sua elaboração, quando é preciso uma definição clara e completa dos requisitos;
                            
    [ item 13 ] --------------- Pesquisa (Cutter Consortium) (problemas recorrentes com empresas de TI) ---------------  
        • Funcionalidades entregues não condizentes com o esperado    • Desrespeito a data prometida de entrega
        • Sistemas considerados ruins, com impossibilidade de uso (razão não está clara);
        
    [ item 14 ] ----------------------------- Desenvolvimento de software (modelo cascata) -----------------------------
        • Modelo tradicional, possuindo ciclo possui etapas bem definidas, sendo (requisitos, projeto, implementação,
          teste e manutenção) onde a conclusão de cada fase é requisito para o início da próxima, podendo haver retornos
          para sanar problemas que venha a prejudicar o produto final; 
        
    [ item 15 ] ------------------ Desenvolvimento de software (ciclo de vida natural de um software) ------------------
        • Concepção, construção, implantação, implementações, maturidade, declínio, manutenção e descontinuidade;
         
    [ item 16 ] ------------------------- Desenvolvimento de software (modelo cascata) (fases) ------------------------- 
        • Fase de requisitos = descoberta, análise, especificação, validação das propriedades do software, sendo estas
                               funções, características, restrições, condições, o que representa um levantamento de
                               requisitos para expressar as necessidades e restrições esperadas num software
                               
        • Fase de projeto = desenho do produto, para refletir o que este fará, usando a fase de requisitos como base,
                            e ajudando-a a ser refinada, desmembrando o produto em módulos ou blocos de código que
                            se comunicam entre outros por interfaces
                            
        • Fase de implementação = conversão do projeto em linguagem de programação para torná-lo executável, delegando
                                  a divisão de equipes de programadores para a construção de um módulo do sistema
                                  tomando por base a documentação da fase do projeto, ou fases anteriores
                                  
        • Fase de testes = códigos que executam partes do programa afim de revelar anomalias, com uso das técnicas
                           funcional (especificação do software) e estrutural (conhecimento da implementação interna do
                           programa)
                         
        • Fase de manutenção = fase de observação para possíveis alterações e evoluções no software, como consequências
                               de bugs descobertos e novos requisitos sejam necessários, afim de melhorar o desempenho 
                               ou adaptá-lo a um ambiente diferente para qual foi construído;
    
    [ item 17 ] ------------------------------- Desenvolvimento de software (atividades) -------------------------------
        • Um software é: 1. especificado           (requisitos validados)    
                         2. projetado e implantado (projeto de arquitetura)    
                         3. validado               (testes unitários)   
                         4. evoluído               (projeto de manutenção)
        
        • Um software é resultado de: 1. Produtos (atividade do processo)
                                      2. Papéis (trabalho dos envolvidos em etapas do processo)
                                      3. Condições preliminares e posteriores (lista de funcionalidades e apuração dos 
                                                                             resultados);
                                                                             
    [ item 18 ] ----------------------------------- Processo de software (conceito) -----------------------------------
        • Conjunto disciplinado e articulado de tarefas que serve para sistematizar o desenvolvimento de um software;
        
    [ item 19 ] - Leitura (recomendação) - 
        • Ian Sommerville    • SOMMERVILLE, I. Engenharia de Software. 9. ed. São Paulo: Pearson Prentice Hall, 2011
        • Páginas 19 a 21;
    """.split(';')

u1_secao_2 = f"""
    [ item 1 ] ------------------------------ Modelo cascata / Ciclo de vida tradicional ------------------------------
        • Desde 2001, tornou-se obsoleto devido as demandas de tempo e agilidade atuais;
        
    [ item 2 ] --------------------------------- Modelo cascata (conceito prescritivo) ---------------------------------  
        • Não é uma citação direta
        • Construção linear do sistema com uma sequência de fases, com a particularidade de uma etapa do processo
          utilizar o resultado obtido pela etapa anterior para criar seu artefato, com possibilidade de retorno
          para etapas anteriores, para ajustes (WAZLAWICK, 2013);
          
    [ item 3 ] ----------------------------------- Modelo cascata (características) ----------------------------------- 
        • Determinismo = há um processo de fabricação, uma linha de produção, onde alterações são determinísticas,
                         conhecidas, esperadas, gerando mais segurança, redução de tempo e custo
        
        • Especialização = atividades especializadas na criação, por pessoas especializadas 
        
        • Foco na execução = se muito já foi planejado e as etapas serão feitas por especialistas, então deve haver
                             fooo na execução, pois o pensar já foi feito;
                             
    [ item 4 ] --------------------------------- Metodologias ágeis (características) ---------------------------------
        • (WAZLAWICK, 2013)
        • Enfatizam em fatores humanos inerentes ao desenvolvimento de programas, mais do que definições de atividades 
        • Mais adequados à natureza do trabalho de profissionais de TI
        • Revisões são mais suscetíveis
        • Atividades intelectuais não lineares ou determinísticas
        • Abertura maior para que o cliente possa mudar de ideia durante o desenvolvimento (feedback);
        
    [ item 5 ] ------------------------------- Software (etapas do processo de criação) -------------------------------
        • Revisão de requisitos (rever)    • Alteração de decisões    • Resgate de detalhes;
        
    [ item 6 ] --------------------------------------- Metodologias ágeis comuns ---------------------------------------
        • Extreme programming (XP)    • Scrum
        • Surgiram a partir de 2001, após a criação do Manifesto ágil;
         
    [ item 7 ] -------------------------------------- Manifesto ágil (princípios) --------------------------------------
        • Indivíduos e interações importavam mais do que processos e ferramentas
        • Softwares em funcionamento importam mais do que documentação
        • Colaboração com o cliente importa mais do que negociação de contratos
        • Responder a mudanças é melhor do que seguir um plano
        
        FONTE: Agile Manifesto, na internet (BECK et al., 2001);
        
    [ item 8 ] ----------------------------------------- Metodologia ágil (XP) -----------------------------------------
        • Adequada para projetos cujos requisitos são voláteis, com equipes reduzidas, paradigma OO, com o projeto
          desmembrado em partes a serem entregues para teste desde o princípio, e que sejam submetidos à escalabilidade
          em funcionalidades
          
        FONTE: TELES, 2006;
        
    [ item 9 ] ----------------------------- Metodologia ágil (XP) (equipe) (configuração) -----------------------------
        • Gerente do projeto || estabelecimento de contato entre a equipe e o cliente, gerencimento de assuntos
                             || administrativos, relacionamento com o cliente, cuidados com a equipe com pressões 
                             ||  externas
                             ||                     
        • Coach              || responsável técnico pelo projeto, com preparado e experiência técnica, sabendo usar 
                             || ferramentas específicas ou analisar novas tecnologias para designar ou não seu uso em
                             || algum produto
                             ||
        • Analista de teste  || ajuda o cliente a escrever os testes de aceitação e fornece feedback para a equipe
                             || interna sobre como correções no sistema possam ser feitas, trazendo a participação do
                             || cliente como ativa nos testes do produto (oposto das metodologias tradicionais)
                             ||
        • Redator técnico    || ajuda a equipe de desenvolvimento a documentar o sistema, com a intenção de que seja
                             || mínima e dar oportunidade aos desenvolvedores mais foco na construção do programa
                             || 
        • Desenvolvedor      || realiza análise, ajuda a criar o projeto e codifica o sistema, podendo este ser além de
                             || desenvolvedor, um engenheiro de requisitos ou projetista; 
                             
    [ item 10 ] ----------------------------------- Metodologia ágil (XP) (pilares) -----------------------------------
        • Feedback     = troca de informações entre cliente e equipe, reavaliação de necessidades 
        • Comunicação  = contato proveitoso entre equipe e cliente, evitando ao máximo trabalho especulativo
        • Simplicidade = desenvolvimento baseado na necessidade do cliente, sem sobrecarregar o sistema com adicionais  
        • Coragem      = equipe buscar manter o cliente incluso, para propor melhorias e levar adiante a metodologia
        
        DETALHE = Trabalho especulativo faz referência a quando o desenvolvedor, por falha na comunicação, desenvolve um
                  produto com base em suas convicções;
        
    [ item 11 ] ---------------------------------- Metodologia ágil (XP) (processos) ----------------------------------
        • Planejamento = esclarecimento de requisitos do produto, onde o cliente é convidado a redigir as 
                         funcionalidades em uma ficha denominada 'Estória', sendo passível de edição e validação
    
        • Projeto = Guia de implementação de cada história da ficha de 'Estória', no intuito de criar um protótipo
                    executável para redução de riscos caso um problema seja de difícil representação dessas histórias
              
        • Codificação = Etapa posterior à criação de histórias e do trabalho de projeto, com a criação de testes de 
                        unidades para cada história, que precisam de uma validação para o desenvolvimento de uma versão
                        mais completa
    
        • Testes = Automatização do conjunto de testes de unidade, afim de integrar e validar o produto em andamento;
        
    [ item 12 ] --------------------------------------- Metodologia ágil (Scrum) ---------------------------------------
        • Gestão de projetos de software com a prática de criação de funcionalidades específicas
        • Se comparada a metodologia XP, suas práticas se assemelham, mas possuem nomes e graus de importância !=;
        
    [ item 13 ] --------------------------------------- Metodologia ágil (SCRUM) ---------------------------------------
        • Product backlog = lista de funcionalidades almejadas para o produto, passível de alteração
        
        • Product Owner = ator do projeto que cria listas de requsitos denominadas 'Backlog', que são ordenadas, 
                          incompletas e dinâmicas que contenha itens a serem produzidos durante o projeto, na etapa 
                          inicial (requisitos de menor importância vão ao final da lista)
        
        • Sprint = divisão do processo em ciclos regulares de 15 a 30 dias, ou mais dependendo da complexidade, para
                   desenvolver funcionalidades previamente definidas para inserção na etapa de 'Sprint backlog', e caso
                   algo novo surja, será tratado no próximo 'Sprint'
                   
        • Sprint backlog = lista de tarefas que são executas em uma etapa de 'Sprint', vindas da etapa de 
                           'Product backlog' e priorizadas pelo 'Product owner';
                           
    [ item 14 ] --------------------------- Metodologia ágil (Scrum) (perfis profissionais) ---------------------------
        • Scrum master = facilitador do projeto, que oferece manutenção em todas as etapas do projeto, e atua como 
                         moderador para evitar que a equipe faça coisas além do que conhecem 
                          
        • Scrum team = equipe de desenvolvimento, compondo entre 6 para 10 membros, sem divisões entre programador,
                       analista e projetista
        
        • Product owner = pessoa responsável pelo projeto, indicando requisitos mais importantes a serem tratados nos
                          sprints; 
                          
    [ item 15 ] --------------------------------- Metodologias ágeis (características) ---------------------------------
        • Boa comunicação entre os elementos envolvidos em um projeto
        • Boas prátcias de comunicação para que o cliente se sinta parte integrante;
        
    [ item 16 ] ------------------------------ Metodologias ágeis (Scrum) (quadro Scrum) ------------------------------
        • Meio de gestão visual das atividades do projeto, não sendo parte oficial da metodologia 
        • Seu desenho possui um formato matricial
        • Tabela com 4 colunas: 1 coluna reservada p/ a 'Estória' e 3 colunas relacionadas a ela (To do) (Doing) (Done)
        • Cada linha representa uma estória e suas tarefas, selecionado de uma 'Sprint' e extraídas do 'Product Backlog'
        • No quadro, temos 'Post-its' que servem para determinar uma característica ou estado, e identificação resumida
          de uma tarefa;
          
    [ item 17 ] ------------------------- Metodologias ágeis (Scrum) (quadro Scrum) (exemplo) -------------------------
        • Meio de informar a todos da equipe sobre o que cada um está fazendo e em qual estágio
        • Os dados estão dispersos, devido a posição das informações no 'Post-it' (imaginar um cartão envolto ao texto)
        
        Prioridade da tarefa                                                             Esforço para executar a tarefa
        MA = muito alta                                                                  1 = algumas horas
        A = alta                                                                         3 = 12 horas
        M = média                                                                        5 = 1 dia
        B = baixa                                                                        8 = 1,5 p/ 2 dias
        MB = muito baixa                     
        
                                         Estória onde a tarefa pertence
                             
                                     Descrição da tarefa reduzida e objetiva
        
        Nome do responsável                                                                              Tempo estimado;                                                                                              
    
    [ item 18 ] --------------------------------- Metodologias ágeis (Scrum) (Trello) ---------------------------------
        • Software colaborativo para visualização online do andamento de projetos (gratuito);
        
    [ item 19 ] ------------------------------- Metodologias ágeis (Scrum) (visão geral) -------------------------------
        1. Início do ciclo -> compreensão do caso que envolve o projeto -> reunião entre interessados -> criação do 
           desenho do projeto
        
        2. Desenvolvimento de um 'Backlog' pelo 'Product Owner' -> lista priorizada de requisitos -> projeto escrito em
           forma de Estória
        
        3. Reunião de planejamento -> iniciação de uma 'Sprint' -> inclusão de Estórias principais -> 1 a 6 semanas ->
           Desenvolvimento de artefatos ou incrementos do produto
          
        4. 'Sprint' em andamento -> reuniões diárias curtas para discussão do progresso -> assuntos sobre o que foi
           realizado, se houve dificuldades, o que será feito antes do próxima reunião
          
        5 • 'Sprint' em encerramento -> reunião de revisão -> demonstração do produto para o 'Product Owner' e clientes
            -> avaliação dos critérios e aceitação do 'Product Owner' 
          
        6 • 'Sprint' encerramento -> reunião de retrospetiva -> discussão de melhoramentos: processos, desempenho ->
            Avanço ao 'Sprint' subsequente;
            
    [ item 20 ] -------------------------------------------- Fontes extras --------------------------------------------
        CRUZ, F.            Scrum e Agile em Projetos. Guia Completo.        2. ed. RJ: Brasport, 2018.
        SILVA, E. C.        Scrum e FTS: uma abordagem prática.              RJ: Brasport Livros e Multimídia, 2017.
        WAZLAWICK, R. S.    Engenharia de software: conceitos e práticas.    RJ: Elsiever, 2013.;
    """.split(';')

u1_secao_3 = f"""
    [ item 1 ] ------------------------------------------ Controle de versões ------------------------------------------
        • Controlar as diversas modificações que um software pode ter
        • Meio pelo qual o GCS (gerenciamento de configuração de software) controla modificações em um sistema;  
    
    [ item 2 ] ----------------- Gerencimaneto de configuração do software (GCS) (conceito) (detalhes) -----------------
        • Meio pelo qual se proporciona controle a todo o processo de desenvolvimento de software
        • Conjunto de práticas que controlam e notificam as inúmeras correções, extensões e adaptações aplicadas ao 
          software enquanto seu ciclo de vida durar
        
        • Sua necessidade se dá principalmente pela complexidade envolvida no desenvolvimento de um software
        • Sua motivação se dá na necessidade de controlar as modificações que um software pode e deve passar
        • Não é incomum esse tipo de recurso ser rejeitado por desenvolvedores, que usam muito mais por obrigatoriedade;
    
    [ item 3 ] ------------------ Gerencimaneto de configuração do software (GCS) (atividades) (IEEE) ------------------
        • Auditoria de configuração de software
        • Controle de configuração de software (relevante 3)
        • Controle de status de configuração de software
        • Gerencimento da entrega e do lançamento de software e configuração das ferramentas de gerenciamento
        • Gerenciamento e planejamento do processo de GCS (relevante 1)
        • Identificação de configuração do software (relevante 2);
        
    [ item 4 ] ------------- Gerencimaneto de configuração do software (GCS) (atividades mais relevantes) -------------
        • Gerenciamento e planejamento do processo de GCS
        -> controle de evolução e integridade do produto, identifica seus elementos, criando registro e relato das 
           informações de configuração
        
        • Identificação de configuração do software
        -> esquemas de identificação para os itens e versões de um produto que devem ser controlados, para estabelecer
           ferramentas e técnicas capazes de fazer essa identificação
           
        • Controle de configuração de software
        -> gerenciamento de mudanças durante o ciclo de vida do software, determinando quais mudanças, autoridade 
           de aprovação, suporte de implementação, desvios formais dos requisitos;
    
    [ item 5 ] ------------------------ Gerenciamento de configuração de software (CGS) (mitos) ------------------------
        • Promover o GCS significa ter mais trabalho e adotar novos procedimentos
         -> A dificuldade de transição de um ambiente que não tenha, que passe a adotar um GCS, pode ser difícil, mas
            isso é relativo, dependendo da equipe que vai lidar com isso, mas se deve levar em conta os potenciais 
            benefícios, como automação de tarefas e eliminação de erros
            
        • GCS é de responsabilidade única do pessoal da administração do sistema
        ->  Os responsáveis pela administração têm maior contribuição em criar um ambiente organizacional no qual o GCS
            possa prosperar, porém a implantação e a condução do GCS é de todos os envolvidos no projeto
            
        • GCS é apenas para os desenvolvedores
        -> Os desenvolvedores são usuários mais frequentes no uso do GCS, sendo os maiores beneficiados, mas devido
           os GCS terem um bom nível de automação, acaba por atrair públicos além de desenvolvedores;
    
    [ item 6 ] ------------------------------------- Controle de versões (funções) -------------------------------------
        • Auditar as modificações realizadas (quem, quando, o que)
        • Automatizar o rastreamento de arquivos
        • Estabelecer meios para obter a situação de um projeto em determinado ponto do tempo
        • Permitir o desenvolvimento paralelo do um ou mais sistemas
        • Prevenir conflitos entre desenvolvedores
        • Recuperar versões anteriores do sistema;
        
    [ item 7 ] ----------------------------------- Controle de versões (repositório) -----------------------------------
        • ambiente virtual que abriga módulos em geral, relacionados ao programa em desenvolvimento, para acesso
          de forma controlada pela equipe de desenvolvimento;
    
    [ item 8 ] ------------------------- Controle de versões (baselines) (conceito) (detalhes) -------------------------
        • Conjuntos de itens de configuração formalmente aprovados, que servem de base para as etapas seguintes de 
          desenvolvimento, e que pode evoluir para um 'Release' quando há uma entrega formal ao fim de uma iteração
          
        • 'Baselines' também pode ser entendida como uma versão específica de um item de configuração de software que
           foi acordado, alterado somente via procedimentos formais
        
        • Tanto 'Baselines' quanto 'Releases' podem ser encontradas em repositórios, em formato de tags 
        
        FONTES MENCIONADAS: (DANTAS, 2009);   
        
    [ item 9 ] -------------------------------- Controle de versões (baselines) (tipos) --------------------------------
        1 • Linha de base funcional  
        2 • Linha de base alocada   
        3 • Linha de base de desenvolvimento 
        4 • Linha de base do produto          
        
        1 • Revisão de requisitos de um sistema  
        2 • Revisão e especificação de requisitos de software e especificação de requisitos de interface de um software
        3 • Configuração de um software em evolução em momentos específicos durante o ciclo de vida de um software
        4 • Software completo e entregue para integração de sistema;
          
    [ item 10 ] ------------------------------------ Controle de versões (branches) ------------------------------------
        • Implementação em paralelo de novas funcionalidades, feita de forma isolada por cada desenvolvedor
        • 'Mainline' é a primeira linha de desenvolvimento
        • 'Branches' é a segunda linha de desenvolvimento, que pode ser unida a 1a linha de desenvolvimento (merge)
        • São um diferencial para múltiplas demandas de um projeto;
    
    [ item 11 ] ------------------------------------- Controle de versões (tipos) -------------------------------------
        • Git    • Github;    

    [ item 12 ] --------------------------------------- Controle de versão (Git) ---------------------------------------
        • Git = sistema de controle de versão gratuito aberto, de bom desempenho, com criptografia, operações de 
                'Commit' e verificação de 'Checksum', modelo de 'Branching' diferenciado (vários branches que podem ser 
                independentes), operações de criação, merge, exclusão dos 'Branches' com rapidez
        
                viabiliza o trabalho em paralelo, controle e compartilhamento de subprojetos de desenvolvedores com seus
                experimentos, como correção de bugs, aprimoramento de funções, sem afetar arquivos do repositório 
                central
                
        FONTE: MAILUND, 2017;
    
    [ item 13 ] ------------------------------------- Controle de versão (Github) -------------------------------------
        • Github = sistema de controle de versão gratuito aberto e mundial, possuindo as mesmas características do
                   controlador Git;
    
    [ item 14 ] ------------------------------------------- Github (branch) -------------------------------------------
        • Linha independente de desenvolvimento em um projeto com um histórico de commits particular;   
        
    [ item 15 ] ------------------------------ Git (versões de um arquivo em um projeto) ------------------------------
        • Diretório de trabalho   (versão para edição)  
        • Stage (versão alterada não incluída no repositório, que aguarda uma operação de commit)  
        • Permanente (versão alteradas permanentemente, pós operação de commit);
        
    [ item 16 ] ----------------------------------- CVS (concurrent version system) -----------------------------------
        • Ferramenta open source que implementa as principais funções relacionadas ao processo de controle de versões
        
        • Atua armazenando as modificações realizadas em um repositório, conforme elas vão acontecendo, através de um 
          número 
          
        • Seu repositório armazena cópias dos arquivos que estão sob o controle de versão, onde o acesso se dá via
          comandos CVS, que são alteradas e passam por uma operação de commit;
    
    [ item 17 ] ----------------------- CVS (concurrent version system) (arquivos de histórico) -----------------------
        • São conhecidos como arquivos RCS, que guardam informações suficientes para recriar qualquer revisão do 
          arquivo, log das mensagens de commit, nome do usuário; 
    
    [ item 18 ] ------------------------------------- Controle de versão (termos) -------------------------------------
        • Checkout = primeira recuperação/download de um módulo do sistema vindo do repositório do CVS
        • Commit = envio do artefato alterado para o repositório CVS
        • Export = recuperação/download de um módulo exportado a partir de um repositório sem arquivos CVS admin
        • Import = criação de um módulo no escopo de um repositório CVS, via upload de uma estrutura de diretórios
        • Module = representação de uma hierarquia de diretórios
        • Release = número de versão de lançamento de um produto
        • Merge = fusão de diversas modificações feitas por usuários diferentes  na cópia local de um mesmo arquivo;
    
    [ item 19 ] ---------------------------------------- Git (comandos comuns) ----------------------------------------
        • git branch = retorna a(s) 'Branch(es)' existente(s) no repositório, dando ênfase em * para a logada
        • git branch nome = criar um 'Branch' e loga nela
        • git checkout nome = logar em um 'Branch' especificado;
   
    [ item 20 ] ------------------------------------------------ FONTE ------------------------------------------------
        • LONGEN, A. S. Como Usar Um Git Branch. Hostinger, [S.l.], 23 abr. 2019.;
    """.split(';')

# todo parada
u2_secao_1 = f"""
    [ item 1 ] ------------------------------- Software (meios que determinam qualidade) -------------------------------
        •  Métodos    • Ferramentas    • Processos    • Medições    • Modelos    • Normas
        • Oferecem a garantia p/ que a entrega seja feita dentro dos padrões de qualidade estabelecidos entre as partes
        • O início desse procedimento começa com o 'levantamento de requisitos' (cliente -> equipe -> necessidades);
        
    [ item 2 ] ----------------------------------- Qualidade de software (conceito) -----------------------------------
        • Conexão de aspectos de conformidade com os requisitos funcionais e não funcionais encontrados nos 
          desenvolvimentos de softwares [ FONTE: Zanin et al. (2018) ]
          
        • Requisitos funcionais = Reflexo da visão do usuário quanto ao funcionamento de determinada função dentro do
                                  software
                                  
        • Requisitos não funcionais = Reflexo da visão do desenvolvedor, para determinar tanto o funcionamento técnico 
                                      das funcionalidades quanto os mecanismos e o desempenho;
    
    [ item 3 ] --------------------------------- Ciclo de desenvolvimento de software ---------------------------------
        • FONTE: [ Pressman (2006) ]
        • Avaliação    • Análise    • Projeto    • Implementação    • Teste    • Manutenção    •    
    
    [ item 4 ] -------------------------- Atividades de desenvolvimento de software (níveis) --------------------------
        • FONTE: [ Sommerville (2011) ]
        • Organizacional || padrões de trabalho de desenvolvimento (frameworks) com as melhores práticas
                         ||
        • Projeto        || padrões variáveis determinados por gestores de projetos, dependendo do projeto, política da
                         || empresa, framework utilizado, etc
                         ||
        • Planejamento   || plano de qualidade, com verificação e revisitação dos requisitos de qualidade dos processos 
                         || e produtos desenvolvidos;
    
    [ item 5 ] ------------------------------------- Falha de software (conceito) -------------------------------------
        • FONTE: [ Zanin et al. (2018) ] comportamento inesperado que é reflexo de um erro, relacionados a execuções
          incorretas que não reflete a realidade (ex: erro na data do SO)
    
    [ item 6 ] ------------------------------------ Defeito de software (conceito) ------------------------------------
        • FONTE: [ Zanin et al. (2018) ] Serviço apresenta erro, interrupção ou mal funcionamento devido uma 
          implementação incorreta (ex: formulário que funciona em receber dados, mas não há registro em um bdd)
    
    [ item 7 ] - Bugs (conceito) -
        • FONTE: [ Zanin et al. (2018) ] Erros e falhas inesperadas de maior complexidade em um software, criando maior
          demanda para sua descoberta e resolução
        
    [ item 8 ] - Garantia de Qualidade -
        • FONTE: [ Sommerville (2011) ]
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')

u2_secao_2 = f"""
    [ item 1 ] -  -
        •  
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')

u2_secao_3 = f"""
    [ item 1 ] -  -
        •  
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')

u3_secao_1 = f"""
    [ item 1 ] -  -
        •  
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')

u3_secao_2 = f"""
    [ item 1 ] -  -
        •  
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')

u3_secao_3 = f"""
    [ item 1 ] -  -
        •  
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')

u4_secao_1 = f"""
    [ item 1 ] -  -
        •  
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')

u4_secao_2 = f"""
    [ item 1 ] -  -
        •  
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')

u4_secao_3 = f"""
    [ item 1 ] -  -
        •  
    [ item 2 ] -  -
        •
    [ item 3 ] -  -
        •
    [ item 4 ] -  -
        •
    [ item 5 ] -  -
        •
    [ item 6 ] -  -
        •
    [ item 7 ] -  -
        •
    [ item 8 ] -  -
        •
    [ item 9 ] -  -
        •
    [ item 10 ] -  -
        •
    [ item 11 ] -  -
        •
    [ item 12 ] -  -
        •
    [ item 13 ] -  -
        •
    [ item 14 ] -  -
        •
    [ item 15 ] -  -
        •
    [ item 16 ] -  -
        •
    [ item 17 ] -  -
        •
    [ item 18 ] -  -
        •
    [ item 19 ] -  -
        •
    [ item 20 ] -  -
        •  
    """.split(';')


if __name__ == '__main__':

    from metodos_bdd.bdd import mtd_paint_random

    autor = 'Roque Maitino Neto'
    u1_s1 = 'Unidade 1 - SEÇÃO 1 = INTRODUÇÃO A ENGENHARIA DE SOFTWARE'
    u1_s2 = 'Unidade 1 - SEÇÃO 2 = METODOLOGIAS ÁGEIS'
    u1_s3 = 'Unidade 1 - SEÇÃO 3 = CONTROLE DE VERSÕES'

    u2_s1 = 'Unidade 2 - Seção 1 = INTRODUÇÃO À QUALIDADE DE SOFTWARE'

    parada = """
    Segundo Zanin et al. (2018), a falha de software pode ser um comportamento inesperado do sistema
    """

    while True:
        print(u1_s3, mtd_paint_random(label=choice(u1_secao_3)))
        sleep(0.1)

    # print(len(u1_secao_2))
