

from sys import getsizeof as _
# dot = 


def unidade1_secao1():
    """
    ----------------------------------------------- UNIDADE 1 / SEÇÃO 1 -----------------------------------------------
    INTRODUÇÃO À ENGENHARIA DE SOFTWARE - Roque Maitino Neto

    CONCEITO-CHAVE
    A Engenharia de Software é uma daquelas disciplinas que nos surpreendem o tempo todo_. Dinâmica por natureza, ela
    vem agregando elementos ao seu rol de temas, vem refinando e agilizando seus processos e, com efeito, contribuindo
    de forma inestimável para o desenvolvimento da Computação, entendida aqui como uma ciência. Encontrar um conceito
    definitivo para Engenharia de Software é, portanto, uma tarefa cujo resultado pode se apresentar ligeiramente
    obsoleto em um momento seguinte. Essa sua inclinação à constante mutação, no entanto, não a transforma em uma
    disciplina incompreensível e sem um nexo conceitual definido.

    DEFINIÇÃO DE ENGENHARIA DE SOFTWARE
    A literatura nos oferece diversas definições para a Engenharia de Software, desde as sucintas até as mais elaboradas
    . Porém, a grande maioria utiliza-se de termos como procedimentos, métodos e ferramentas para indicar uma natural
    convergência: a qualidade do produto a ser desenvolvido. Se o resultado da aplicação de procedimentos, métodos e
    ferramentas não for uma entrega de qualidade, de pouco terá valido todo_ o esforço em adotá-los. Como primeiro passo
    , convém conhecermos a definição para Engenharia de Software dada por um importante autor dessa área.

    A Engenharia de Software abrange um processo, um conjunto de métodos (práticas) e um leque de ferramentas que
    possibilitam aos profissionais desenvolverem software de altíssima qualidade. (PRESSMAN; MAXIM, 2016).

    Ao analisarmos uma definição, devemos considerar a natureza absolutamente dinâmica da Engenharia de Software,
    conforme já mencionamos. Com o passar dos anos, a importância que um programa de computador assumiu na vida das
    pessoas e em seus negócios foi sensivelmente alterada e a necessidade por qualidade e agilidade nas entregas cresceu
    na mesma proporção, o que acabou justificando o surgimento de novos meios de desenvolvimento de software. Dominar
    conceitos da Engenharia de Software é um caminho seguro para o estabelecimento de práticas consoantes com as
    necessidades da organização em que o profissional de TI está inserido.

    Via de regra, aquele que domina um conceito é capaz de adaptá-lo às suas necessidades ou as da organização em que
    atua, sem o risco de esvaziar sua essência. Por isso, uma melhor definição do conceito de Engenharia de Software
    pede o detalhamento dos termos que o compõem. O termo “Engenharia” está relacionado ao projeto e à manufatura de um
    artefato e, desde já, ressaltamos a importância dos requisitos e das especificações do artefato nesse contexto. Por
    não possuir uma forma física, um programa de computador não passa por processo de manufatura tradicional, conforme o
    conhecemos no meio industrial. Além disso, a produção de programas de computador possui situações bastante
    particulares, que requerem soluções especializadas e, portanto, diferentes daquelas adotadas em um processo fabril.

    Avançando para o próximo termo, temos uma definição satisfatória para software como:

    Instruções que, quando executadas, produzem a função desejada.
    Estruturas de dados que possibilitam os programas manipularem a informação;
    E documentação relativa ao sistema.

    Esses três elementos são, de fato, a matéria-prima para a Engenharia de Software, que é definida pelo IEEE Computer
    Society como a aplicação de uma abordagem sistemática, disciplinada e quantificável de desenvolvimento, operação e
    manutenção do software, além do estudo dessas abordagens (IEEE, 2004).

    PRINCÍPIOS DA ENGENHARIA DE SOFTWARE
    Formada a base conceitual da disciplina, avançamos agora para elementos que costumamos chamar de princípios da
    Engenharia de Software justamente por darem uma feição própria a ela e por suportarem suas práticas. São esses
    princípios que ajudam a estruturar os processos e a padronizar as soluções propostas por esse ramo da Computação.
    Eles foram propostos pelo SWEBOK (Software Engineering Body of Knowledge ou Conjunto de Conhecimentos de Engenharia
    de Software), que se trata de uma importante publicação do IEEE na área.

    O primeiro princípio proposto pelo IEEE (2004) foi o da organização hierárquica, o qual estabelece que os
    componentes de uma proposta de solução ou a organização de elementos de um problema devem ser apresentados em
    formato hierárquico, em uma estrutura do tipo árvore, com quantidade crescente de detalhamento nível após nível.

    A formalidade pode ser apontada como o próximo princípio e ela estabelece que a resolução de um problema deve seguir
    uma abordagem rigorosa, metódica e padronizada. Depois, como terceiro princípio, vale mencionar a completeza, que
    estabelece a necessidade de que se verifique cuidadosamente se todos os elementos de um problema foram levantados e
    se a solução proposta os contempla por completo.

    O IEEE (2004) sugere como próximo princípio aquele conhecido como dividir para conquistar e a justificativa para sua
    criação é simples: fica intelectualmente inviável encarar um problema complexo (e a construção de um sistema é um
    problema complexo!) sem que ele seja dividido em partes menores, independentes e, portanto, mais facilmente
    gerenciáveis. Essa é a lógica subjacente à criação de soluções modulares.

    O princípio da ocultação estabelece que, ao conceber uma solução modular, cada módulo tenha acesso às informações
    necessárias para seu funcionamento, o que significa ocultar informações não essenciais. Já o princípio da
    localização aponta para a necessidade de se colocar juntos os itens relacionados logicamente em um sistema e, pelo
    princípio da integridade conceitual, o engenheiro de software deve seguir uma filosofia e uma arquitetura de projeto
    coerentes (IEEE, 2004).

    A publicação SWEBOK (IEEE, 2004) ainda aborda alguns outros princípios, incluindo a abstração, a qual determina a
    atenção do engenheiro de software a elementos com afinidade a um problema particular, isolando-os de outros
    elementos relacionados a outros tipos de problemas. Difícil de entender? Então pense na abstração como a aplicação
    prática da capacidade de um profissional em concentrar-se em aspectos essenciais para a resolução de um determinado
    problema, deixando para outro momento os problemas relacionados ou de importância secundária.

    EXEMPLIFICANDO
    Certa equipe de desenvolvimento construiu um processador de texto. Ao planejar o menu da ferramenta, a
    funcionalidade de classificação por ordem alfabética acabou ficando no menu "Layout de página". Tempos depois, a
    mesma equipe foi chamada com o intuito de construir um sistema acadêmico. Para a fase de análise, a equipe escolheu
    a metodologia da análise estruturada e, para o projeto, a metodologia de projeto orientado a objeto.

    A Engenharia de Software guia-se por princípios que devem ser respeitados, a fim de que sua prática leve ao
    cumprimento de seus objetivos. No caso apresentado, dois desses princípios foram ignorados pela equipe de
    desenvolvimento.

    Ao pensar no menu, a equipe não considerou que a localização dos elementos no programa final é de suma importância
    para que o usuário o utilize com desenvoltura. Quando um menu de programa é identificado como “Layout de página”,
    não se espera que a funcionalidade de classificação por ordem alfabética lá esteja localizada.

    No segundo projeto, ao não considerar a adoção de uma metodologia do início ao fim do desenvolvimento, a equipe
    simplesmente ignorou o fato de que o projeto deve respeitar o princípio da integridade conceitual.

    O SOFTWARE
    Agora que você já teve contato os pilares da Engenharia de Software, vale focarmos naquele que é seu objeto
    principal: o software.

    De acordo com Pressmann e Maxim (2016), software de computador é o produto que profissionais de software desenvolvem
    e ao qual dão suporte no longo prazo. Abrange programas executáveis em um computador conteúdos e informações
    descritivas.

    Os conteúdos aos quais os autores se referem são dados e informações geradas conforme a execução do programa
    acontece. Já as informações descritivas referem-se à documentação do programa, necessária para referência e
    manutenção futura. Por meio dessa definição, é possível entender que o software não se resume ao programa
    executável.

    Um dos elementos que contribui para tornar o software uma criação de natureza única é o fato de que ele é um produto
    e, ao mesmo tempo, o veículo usado para a distribuição desse produto. Embora o papel do software tenha passado por
    mudanças significativas a partir da metade final do século XX, ele se consolidou como um elemento indispensável em
    nossos dias e se firmou como o responsável por fazer transitar mundo afora o bem mais precioso que possuímos, que é
    a informação (PRESSMAN, MAXIM, 2016).

    ASSIMILE
    Software consiste em: (1) instruções (programas de computador) que, quando executados, fornecem características,
    funções e desempenho desejados; (2) estruturas de dados que possibilitam aos programas manipular informações
    adequadamente; (3) informação descritiva, tanto na forma impressa quanto na virtual, descrevendo a operação e o uso
    do programa (PRESSMAN, MAXIM, 2016).

    Quando colocamos o conceito de software em palavras simples e objetivas e o abordamos como um produto comercialmente
    viável, a compreensão de suas funções pode soar bastante simples. Esse fato tem o potencial de nos dar a falsa
    impressão de que criá-los também seja uma atividade sem complexidade e que “sentar e programar” seja uma solução
    sempre viável. Mas, em sentido contrário, desenvolver produtos de software tem deixado de ser uma atividade
    artesanal e empírica e tem se tornado sistemática, organizada e baseada em métodos, muito por conta da evolução da
    Engenharia de Software. No entanto, logo em seus primeiros anos, a produção de software enfrentou tempos turbulentos
    , com tarefas em que a incerteza era fator preponderante e os resultados dos esforços de criação de um artefato
    poderiam ser empreendidos em vão.

    De acordo com Schach (2009), na década de 1960, alguns atores do processo de desenvolvimento de software cunharam a
    expressão “crise do software” na intenção de evidenciar o momento adverso que a atividade atravessava. Em seu
    sentido literal, crise indica estado de incerteza ou declínio e, de fato, esse era o retrato de um setor inapto a
    atender a demanda crescente por produção de software, a qual entregava programas que não funcionavam corretamente,
    construídos por meio de processos falhos e que não podiam passar por manutenção facilmente. Além disso, a incerteza
    causada pela imprecisão nas estimativas de custo e de prazo afetava a confiança das equipes e principalmente dos
    clientes.

    Era fato comum naquela época a precariedade na comunicação entre cliente e equipe de desenvolvimento, e essa
    realidade contribuía para que a qualidade do levantamento dos requisitos fosse perigosamente baixa, acarretando
    consequentes incorreções no produto final. Trataremos mais adiante do termo “requisito”, mas já convém defini-lo
    como uma condição para se alcançar certo fim (REQUISITO, 2001). O cenário era ainda agravado pela inexistência de
    métricas que retornassem avaliações seguras dos produtos entregues pelos desenvolvedores. Uma pergunta do tipo “o
    produto que entregamos está adequado às demandas do cliente?” poderia não ser respondida com segurança.

    Quando, apesar das adversidades, o programa era entregue, o processo de implantação tendia a ser turbulento, já que
    raramente eram considerados os impactos que o novo sistema causaria na organização. Treinamentos aos usuários após a
    implantação não era atividade prioritária e o fator humano era ignorado com frequência, gerando insatisfações nos
    funcionários impactados. Por fim, há que se considerar a dificuldade em se empreender manutenção nos produtos em
    funcionamento, normalmente ocasionados por projetos mal elaborados.

    MITOS SOBRE DESENVOLVIMENTO DE SOFTWARE
    Conforme nos ensinam Pressman e Maxim (2016), daquela época ficaram alguns mitos sobre o desenvolvimento de um
    software. Embora os profissionais atuais estejam mais capacitados a reconhecê-los e a evitarem seus efeitos, ainda é
    necessário dar atenção a eles. Trataremos de dois deles aqui.

    MITOS DE GERENCIAMENTO
    Sob pressão, gestores podem apoiar-se em crenças relacionadas ao gerenciamento de seus projetos de software. Um mito
    bastante comum é que um livro repleto de práticas e padrões vai ser instrumento suficiente para o sucesso da
    empreitada, bastando segui-lo à risca. O questionamento necessário à validade de tal livro é sua completude e
    adequação às modernas práticas da Engenharia de Software. Outro mito comum é que, mediante atraso em uma entrega, a
    inclusão de mais desenvolvedores no projeto ajudaria a evitar atraso maior. Por fim, é perigosa a crença de que, ao
    terceirizar o desenvolvimento de um produto, a empresa que o terceirizou pode deixar a cargo do terceiro todo_ o
    desenvolvimento, sem necessidade de gerenciá-lo (PRESSMAM, MAXIM, 2016).

    MITOS DOS CLIENTES
    Aqui, os autores destacam crenças relacionadas ao papel e ao comportamento dos clientes em um projeto. Segundo um
    dos mitos, basta ao cliente fornecer uma definição geral dos objetivos do software para que seja possível iniciar
    sua elaboração. Na verdade, a realidade é que a definição mais clara e mais completa possível dos requisitos é o
    caminho mais seguro para o bom início de um projeto (PRESSMAM, MAXIM, 2016).

    REFLITA
    Em 2002, uma empresa global de pesquisa em Tecnologia da Informação chamada Cutter Consortium constatou que 78% das
    empresas de TI pesquisadas fizeram parte de ações judiciais motivadas por desavenças relacionadas a seus produtos.
    Na maioria desses casos (67%), os clientes reclamavam que as funcionalidades entregues não correspondiam a suas
    demandas. Em outros tantos casos, a alegação era de que a data prometida para entrega havia sido desrespeitada
    várias vezes. E, por fim, em menor quantidade, a reclamação se originava do fato de o sistema ser tão ruim que
    simplesmente não se podia utilizá-lo (SCHACH, 2009).

    MODELO CASCATA
    Para o bem do futuro da Computação como uma atividade humana viável, uma metodologia estável e bem estruturada de
    desenvolvimento de software deveria ser criada. A resposta da comunidade ligada ao software, então, veio através do
    modelo em cascata, também conhecido como modelo tradicional, o qual ainda é utilizado para desenvolvimento de
    produtos de software. Ele descreve, por meio de etapas bem definidas, o ciclo que o software cumprirá durante o
    período compreendido entre sua concepção e sua descontinuidade.

    O ciclo de vida natural de um software, de acordo com Resende (2005), abrange as seguintes fases: concepção,
    construção, implantação, implementações, maturidade, declínio, manutenção e descontinuidade. Essas fases são mais
    comumente descritas como fase de requisitos, projeto, implementação, teste e manutenção. A Figura 1.1 mostra o
    esquema geral das fases do modelo cascata.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 1.1 | Representação das fases do modelo em cascata
    Fonte: adaptado de Schach (2009, p. 51).

    Observe que uma fase do processo depende do artefato gerado pela fase anterior. Um artefato nesse contexto não é
    exatamente um produto de software acabado. As setas de retroalimentação, dispostas no sentido contrário à cascata,
    indicam a possibilidade de retornos às fases anteriores, considerando a ocorrência de falhas. A volta a uma fase
    anterior serve, em tese, para sanar problemas que, se levados adiante, acarretariam mais prejuízo ao
    desenvolvimento.

    Antes de terminarmos esta seção, vale a apresentação introdutória de cada uma das etapas do modelo em cascata, de
    acordo com Schach (2009):

    -> Requisitos: a fase de requisitos de software preocupa-se com a descoberta, a análise, a especificação e a
       validação das propriedades que devem ser apresentadas para resolver tarefas relacionadas ao software a ser
       desenvolvido. Fazem parte dos requisitos de um software suas funções, suas características, suas restrições e
       todas as demais condições para que ele exista e cumpra seu objetivo. O projeto de um software fica comprometido
       quando o levantamento dos requisitos é executado de forma não apropriada. Eles expressam as necessidades e as
       restrições colocadas num produto de software, as quais contribuem para a solução de algum problema do mundo real
       (SCHACH, 2009).

    -> Projeto: uma vez tratados os requisitos, o modelo nos leva ao desenho do produto. Se os requisitos nos mostram o
       que o sistema deverá fazer, o projeto deverá refletir como ele o fará. Por meio do projeto, os requisitos são
       refinados de modo a se tornarem aptos a serem transformados em programa. O trabalho principal de um projetista é
       o de decompor o produto em módulos, que podem ser conceituados como blocos de código, que se comunicam com outros
       blocos por meio de interfaces (SCHACH, 2009).

    -> Implementação: nessa fase, o projeto é transformado em linguagem de programação para que, de fato, o produto
       passe a ser executável. Como estratégia de implementação, a equipe poderá dividir o trabalho de forma que cada
       programador (ou um pequeno grupo deles) fique responsável por um módulo do sistema. Idealmente, a documentação
       gerada pela fase de projeto deve servir como principal embasamento para a codificação, o que não afasta a
       necessidade de novas consultas ao cliente e à equipe de projetistas (SCHACH, 2009).

    -> Testes: testar significa executar um programa com o objetivo de revelar a presença de defeitos. Caso esse
       objetivo não possa ser cumprido, considera-se o aumento da confiança sobre o programa. As técnicas funcional e
       estrutural são duas das mais utilizadas a fim de se testar um software. A primeira baseia-se na especificação do
       software para derivar os requisitos de teste e a segunda no conhecimento da estrutura interna (implementação) do
       programa (SCHACH, 2009).

    -> Manutenção: os esforços de desenvolvimento de um software resultam na entrega de um produto que satisfaça os
       requisitos do usuário. Espera-se, contudo, que o software sofra alterações e evolua. Uma vez em operação,
       defeitos são descobertos, ambientes operacionais mudam e novos requisitos dos usuários vêm à tona. A manutenção
       de software é definida como modificações em um produto de software após a entrega ao cliente a fim de corrigir
       falhas, melhorar o desempenho ou adaptar o produto ao um ambiente diferente daquele em que o sistema foi
       construído (SCHACH, 2009).

    A seguir veja uma síntese sobre as atividades de um processo de software.

    Processo de software
    Um processo de software é um conjunto de atividades relacionadas, que levam à produção de um produto de software
    (SOMMERVILLE, 2011)
    -------------------------------------- IMAGEM: u1_s1_processo_de_software.png --------------------------------------

    SAIBA MAIS
    Entendemos que o modelo em cascata é um processo de software, pois se utiliza de uma sequência de etapas (ao invés
    de uma única ação) para o atingimento de seu objetivo. Os processos contêm divisões em sua estrutura e, a fim de
    entendermos melhor um processo de software, convém analisarmos duas delas.

    Fases: um conjunto de atividades afins e com objetivos bem definidos são realizados em uma fase do processo. O
    modelo em cascata, por exemplo, apresenta fases bem definidas, quais sejam a fase dos requisitos, a fase do projeto,
    a da implementação e assim por diante (WAZLAWICK, 2013).

    Atividades ou tarefas: comumente descritas com conceitos semelhantes, uma atividade ou uma tarefa constitui um
    projeto em pequena escala. Ela visa promover modificações nos artefatos do processo, que podem ser descritos como
    diagramas, documentos, programas e tudo o que puder ser desenvolvido no processo. As atividades devem possuir
    entradas, saídas, responsáveis, participantes e recursos bem definidos (WAZLAWICK, 2013).

    Em suas regras processuais, a organização pode determinar que seja adotado um documento que descreva a atividade.
    Por meio dele, a equipe tomará conhecimento da tarefa, de seus responsáveis, dos objetivos, dos recursos a serem
    utilizados e de tudo o que a caracteriza por completo.

    Sabemos até o momento que um processo é um conjunto disciplinado e articulado de tarefas que serve para sistematizar
    o desenvolvimento de um software.

    Há certos modelos de processos ditos prescritivos, que contêm descrições de como as atividades são realizadas. O
    modelo cascata, também conhecido como modelo tradicional, é o mais conhecido e ainda bastante utilizado para
    desenvolvimento de produtos de software. Ele descreve, por meio de etapas bem definidas, o ciclo que o software
    cumprirá durante o período compreendido entre sua concepção e sua descontinuidade.

    PESQUISE MAIS
    Ian Sommerville é um acadêmico britânico e autor de um livro que se tornou referência em Engenharia de Software.
    Nessa obra chamada simplesmente Engenharia de Software, ele coloca o modelo em cascata sob a perspectiva de um
    modelo de processo de software e apresenta uma visão interessante sobre aspectos da evolução do software e da
    relação dos requisitos com esse modelo. Sugere-se, portanto, a leitura das páginas 19, 20 e 21 dessa obra
    (SOMMERVILLE, 2011).

    SOMMERVILLE, I. Engenharia de Software. 9. ed. São Paulo: Pearson Prentice Hall, 2011.

    Esse foi o conteúdo que queríamos compartilhar nesta seção inicial. As informações compartilhadas aqui servirão como
    base para novos aprendizados e possibilitarão que comparações sejam feitas, sobretudo entre a metodologia em cascata
    (tida como tradicional) e a ágil, entendida como mais moderna. Execute com atenção as atividades propostas e fique
    com a gente!

    #ref Unidade 1 - Seção 1
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    IEEE Computer Society. Guide to the Software Engineering Body of Knowledge. Piscataway: The Institute of Electrical
    and Electronic Engineers, 2004.

    PRESSMAN, R. S., MAXIM, B, R.; Engenharia de Software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.
    Disponível em: https://bit.ly/3r4DQ1i. Acesso em: 23 nov. 2020.

    REQUISITO. In: HOUAISS, A, VILLAR, M. de S. Minidicionário Houaiss da Língua Portuguesa. Rio de Janeiro: Objetiva,
    2001.

    RESENDE, D. A. Engenharia de Software e Sistemas de Informação. 3. ed. Rio de Janeiro: Brasport, 2005.

    SCHACH, S. R. Engenharia de Software: os paradigmas clássicos e orientados a objetos. 7. ed. São Paulo: McGraw-Hill,
    2009.

    SOMMERVILLE, I. Engenharia de Software. 9. ed. São Paulo: Pearson Prentice Hall, 2011. Disponível em:
    https://bit.ly/34owzjb. Acesso em: 12 out. 2020.

    WAZLAWICK, R. S. Engenharia de software: conceitos e práticas. Rio de Janeiro: Elsiever, 2013.
    """


def unidade1_secao2():
    """
    ----------------------------------------------- UNIDADE 1 / SEÇÃO 2 -----------------------------------------------
    METODOLOGIAS ÁGEIS - Roque Maitino Neto

    CONCEITO-CHAVE
    Aquilo que não é bom não dura por muito tempo. Se a seleção natural é infalível na natureza, ela parece atuar com
    rigor semelhante no mundo do desenvolvimento de software ao permitir que apenas as metodologias mais aptas
    sobrevivam ao teste do tempo. Foi por isso que o Modelo em Cascata atravessou algumas décadas oferecendo aos
    engenheiros de software um modo razoavelmente seguro e efetivo de criar seus produtos, em substituição ao
    desenvolvimento especulativo e caótico praticado antes da estruturação de metodologias de desenvolvimento de
    software.

    Mas, se o Modelo em Cascata é realmente bom, talvez o termo “razoavelmente” tenha sido mal colocado na sentença, não
    é mesmo? Bem, nesta seção teremos oportunidade de entender alguns elementos desse modelo que justificaram a mudança
    de paradigma iniciada no ano de 2001 e vivenciada até hoje. O Ciclo de Vida Tradicional – outra forma como o Modelo
    em Cascata é conhecido – apresenta falhas de concepção que o acabaram tornando obsoleto diante das demandas de tempo
    e agilidade atuais de produção de software.

    Mas, afinal, quais são os problemas da metodologia tradicional? Qual o motivo da dificuldade dela em acompanhar as
    inevitáveis mudanças de requisitos de um produto durante seu ciclo de desenvolvimento? Por que o cliente tem
    dificuldade em reconhecer valor no que está sendo desenvolvido? Mais do que responder a essas questões, esta seção
    tem a intenção de apontar soluções. Antes de abordarmos diretamente as Metodologias Ágeis, convém tratarmos ainda de
    alguns aspectos do processo tradicional de desenvolvimento para que as comparações sejam feitas de forma adequada.

    Conforme estudamos na primeira seção, o processo tradicional de desenvolvimento baseia-se na construção linear do
    sistema, seguindo uma sequência definida de fases, com a particularidade de uma etapa do processo utilizar o
    resultado obtido pela etapa anterior para criar seu artefato (WAZLAWICK, 2013). Há também a possibilidade de que o
    fluxo retorne para etapas anteriores em havendo necessidade de ajustes. Essa construção linear da metodologia
    baseia-se na ideia de que todas as coisas podem ser construídas como se estivessem em uma linha de montagem: a
    matéria-prima é inserida na linha de produção e, após algumas etapas determinadas, o produto final está pronto.

    A Figura 1.2 ilustra a ideia de utilização dos princípios de uma linha de produção no processo de desenvolvimento de
    software. Observe que na primeira etapa os requisitos do produto de software representam as matérias-primas. Depois,
    como em uma linha de montagem tradicional, os especialistas em cada área do processo atuam na linha de montagem até
    que um produto de software acabado esteja disponível.


    Figura 1.2 | Representação da criação de um software em uma linha de montagem
    Fonte: elaborada pelo autor.
    ----------------------------------------------- IMAGEM: img_1-2.jpg -----------------------------------------------

    É essa fundamentação nas formas tradicionais de fabricação que nos permite atribuir ao Modelo em Cascata três
    características bem particulares segundo Teles (2006): o determinismo, a especialização e o foco na execução. Para
    explicar esses conceitos, usaremos a analogia com o processo de montagem de veículos. Vejamos:

    -> Determinismo: materiais alimentam um processo de fabricação e, ao final da linha de produção, temos um automóvel
       terminado. As alterações pelas quais os materiais passam são determinísticas e devem sempre gerar um resultado
       conhecido. Um processo assim estruturado tende a gerar segurança, redução de tempo e de custo.

    -> Especialização: o processo tradicional de manufatura divide a montagem desse carro em atividades especializadas,
       desenvolvidas por trabalhadores igualmente especializados. Assim, numa linha de montagem automotiva, haverá a
       etapa de soldagem do chassi, de colocação do motor, da montagem do interior e assim por diante, todas elas
       executadas por especialistas em cada função.

    -> Foco na execução: se as transformações na linha de montagem já estão determinadas e se cada etapa será executada
       por especialistas, então não há muito em que pensar. Basta executar.

    Não é difícil inferir, então, que o Modelo em Cascata tenha sido concebido com base nessas ideias de desenvolvimento
    industrial em linha. De acordo com essas ideias, a mera obediência a eventos consecutivos (de requisitos até
    implantação), à especialização (funções de analista, projetista, programador, testador) e ao foco na execução já
    seria capaz de criar um produto de qualidade, no tempo estipulado pelo cliente e nos limites do orçamento. Havia – e
    ainda há – a presunção de que a sequência de etapas do projeto seja transformada corretamente em software (TELES,
    2006).

    Outra presunção que o modelo tradicional de desenvolvimento assume é a de que o profissional do software cumpre
    trabalhos repetitivos, previamente determinados e que pouco dependem das suas habilidades intelectuais. No entanto,
    os desenvolvedores podem ser classificados como trabalhadores do conhecimento, pois cumprem suas tarefas com base em
    seu raciocínio e raramente seguem um processo linear em suas investidas criativas. A eles, portanto, deve ser dada a
    oportunidade de aplicar tantas revisões quantas forem necessárias em suas criações.

    Se as metodologias tradicionais de desenvolvimento se baseiam em modelos de construção que não se adequam
    especificamente ao produto que desejam entregar, as metodologias ágeis nasceram ajustadas para a criação de software
    . Os métodos ágeis enfatizam menos as definições de atividades e mais os fatores humanos inerentes ao
    desenvolvimento de programas de computador (WAZLAWICK, 2013). Eles são, portanto, claramente mais adequados à
    natureza do trabalho de profissionais de TI, já que preveem a necessidade de sucessivas revisões na obra. Atividades
    intelectuais não são executadas de forma linear e não são determinísticas.

    Durante o processo de criação de um software, é mais do que natural que os requisitos sejam revistos, decisões sejam
    alteradas e detalhes sejam resgatados. Afinal, ao explicar pela primeira vez as funcionalidades que deseja para o
    produto, o cliente ainda não as conhece por completo e a visão global do que necessita ainda não está formada. Que
    tal um procedimento que dê a ele oportunidade de aprender e de mudar de ideia ao longo do desenvolvimento? Você
    certamente não notou essa atenção com o cliente ao longo do conteúdo do Modelo em Cascata.

    Sobre o aprendizado do cliente em relação às suas próprias necessidades, Teles (2006) entende que ele está
    relacionado ao feedback que o software fornece ao cliente quando ele tem a oportunidade de utilizá-lo, mesmo na
    versão não completa. No desenvolvimento ágil, o conceito de feedback está presente ao longo de todo_ o
    desenvolvimento do software e exerce um papel fundamental.

    Como, então, podemos dar ao cliente a chance de aprender sobre suas reais necessidades e de mudar de opinião durante
    o processo de desenvolvimento?

    As práticas relacionadas aos métodos ágeis serão apresentadas nas próximas páginas e você conhecerá elementos do
    Extreme Programming e do Scrum, duas das mais utilizadas metodologias ágeis.

    Porém, antes de abordarmos diretamente as duas práticas, vale a menção ao ato que serviu como marco inicial do
    pensamento ágil de desenvolvimento. No ano de 2001, um documento contendo a declaração dos doze princípios que
    fundamentam o desenvolvimento ágil foi divulgado por um grupo de profissionais de TI. Através desse documento,
    chamado Manifesto Ágil, seus autores declaravam que indivíduos e interações importavam mais do que processos e
    ferramentas; que softwares em funcionamento importam mais do que documentação; que colaboração com o cliente
    importa mais do que negociação de contratos e que responder a mudanças é melhor do que seguir um plano (BECK et al.,
    2001). Você pode conferir a íntegra do manifesto e conhecer seus autores na página Agile Manifesto, na internet
    (BECK et al., 2001).

    VISÃO GERAL DO EXTREME PROGRAMMING (XP)
    O XP é uma metodologia adequada para empreitadas em que os requisitos mudam com certa constância, além de ser
    ajustado para equipes pequenas e para o desenvolvimento de programas orientados a objetos (TELES, 2006). Ao
    contrário das metodologias tradicionais, ele é indicado também para ocasiões em que se desejam partes executáveis do
    programa logo no início do desenvolvimento e que ganhem novas funcionalidades conforme o projeto avança.

    REFLITA
    O XP, assim como as outras metodologias ágeis, defende que a criação de um software segue a mesma dinâmica da
    criação de uma obra de arte. O trecho a seguir ilustra esse fato:

    CITAÇÃO
    Escrever uma redação, um artigo ou um livro é uma atividade puramente intelectual que se caracteriza pela
    necessidade de sucessivas revisões e correções até que a obra adquira sua forma final. [...] Quando um pintor cria
    um novo quadro, é comum começar com alguns esboços, evoluir para uma representação mais próxima do formato final,
    fazer acertos, retoques e afins até que a obra esteja concluída. (TELLES, 2004. p. 39)

    Embora a especialização não seja estimulada nas metodologias ágeis, ainda assim existe a necessidade de se
    estabelecer funções para os participantes do projeto. Uma típica equipe de trabalho no XP tem a seguinte
    configuração (TELLES, 2004):

    -> Gerente do projeto: trata-se do responsável pelos assuntos administrativos do projeto e do relacionamento com o
       cliente. Duas de suas funções mais importantes incluem o estabelecimento de contato entre a equipe e o cliente e
       o cuidado para que a equipe fique livre de pressões externas e se dedique integralmente ao desenvolvimento.

    -> Coach: este é o nome do responsável técnico pelo projeto, que deve ser tecnicamente bem preparado e experiente.
       Se, por exemplo, uma nova tecnologia fica disponível no mercado, é função dele sugerir seu uso no produto em
       desenvolvimento.

    -> Analista de teste: ajuda o cliente a escrever os testes de aceitação e fornece feedback para a equipe interna de
       modo que as correções no sistema possam ser feitas. Ao contrário do que é feito nas metodologias tradicionais, no
       desenvolvimento ágil em geral (e no XP em particular), o cliente participa ativamente dos testes no produto.

    -> Redator técnico: ajuda a equipe de desenvolvimento a documentar o sistema, permitindo que os desenvolvedores
       estejam plenamente focados na construção do programa propriamente dito. À propósito, a metodologia recomenda que
       o código deve ser claro o suficiente para permitir uma documentação mínima do sistema.

    -> Desenvolvedor: realiza análise, ajuda a criar o projeto e codifica o sistema. No XP, não há divisão entre as
       especialidades de engenheiro de requisitos, projetista e o desenvolvedor propriamente dito. No modelo tradicional
       , o desenvolvedor apenas programa, via de regra.

    Para atingir seus objetivos, o Extreme Programming apoia-se em quatro pilares, comumente chamados de valores.

    -> O primeiro deles é o feedback, cuja aplicação pretende alcançar a troca de informações entre cliente e equipe.
    Assim, quando o cliente aprende com o sistema que utiliza e reavalia suas necessidades, ele gera feedback para sua
    equipe de desenvolvimento.

    -> O segundo valor é chamado de comunicação e pretende estabelecer contato proveitoso entre equipe e cliente,
       evitando que os desenvolvedores realizem o trabalho de forma especulativa.

    ASSIMILE
    Uma das atitudes mais potencialmente nocivas que uma equipe de desenvolvimento pode adotar é o desenvolvimento
    especulativo. Isso significa, na prática, criar certa funcionalidade do sistema sem saber ao certo suas definições e
    seus requisitos, fato comumente associado à falha de comunicação com o cliente. Nesses casos, o desenvolvedor pode
    não ter entendido corretamente uma necessidade do cliente e, sem a devida segurança, acaba desenvolvendo um produto
    com base em suas próprias convicções praticamente. A proximidade com o cliente tende a reduzir bastante esse
    fenômeno.

    -> O terceiro valor é a simplicidade, cuja formulação serve para orientar a equipe a desenvolver apenas o que for
       suficiente para atender a necessidade do cliente, sem “sobrecarregar” o sistema com funções quase sempre inúteis.

    -> Por fim, o último valor estabelece a coragem como um dos pilares do XP, pois ela será necessária no
       impulsionamento da equipe para manter sempre o cliente presente, para propor melhorias no que já foi testado e
       colocado em funcionamento e, de modo geral, para sempre levar adiante as práticas da metodologia.

    Como não poderia deixar de ser, esses princípios refletem-se nas práticas e no processo proposto pelo XP. De forma a
    destacar suas atividades-chave, Pressman e Maxim (2016) assim dividem o processo do XP:

    Planejamento: essa atividade, comumente identificada como jogo do planejamento, tem início com o esclarecimento de
    requisitos do produto e é executada de modo bem diferente daquele proposto pelo modelo tradicional: aqui, o cliente
    escreve – de próprio punho – as funcionalidades do produto em uma ficha. A essa ficha dá-se o nome de Estória e cada
    uma delas é avaliada pela equipe em termos de custo e tempo de execução. A qualquer momento, o cliente pode escrever
    novas histórias.

    EXEMPLIFICANDO
    Uma estória escrita pelo cliente deve ser pautada na simplicidade e na objetividade, duas características que serão
    úteis em sua codificação. Ao descrever uma funcionalidade do sistema, o cliente poderá expressar-se em termos
    sucintos e usar a própria escrita para isso. Para entendermos como a criação de estórias funciona na prática, vamos
    considerar um cenário no qual um cliente deseja a criação de um programa que, com base nas informações armazenadas
    no sistema integrado de sua empresa, seja capaz de apresentar dados consolidados das suas vendas. Essa
    funcionalidade do novo sistema pode ser assim expressa em uma estória: “O sistema deverá consolidar as vendas por
    período, região e grupo de produtos, bem como permitir a exportação desses dados consolidados para uma planilha de
    dados. Além disso, a impressão de relatórios dessas consolidações deverá estar disponível”. Com a concordância do
    cliente, a equipe poderá fazer sugestões nessa estória e, por exemplo, dividi-la em outras tarefas para que sua
    implementação seja facilitada.

    -> Projeto: representações complexas da solução certamente não são características desta tarefa, muito menos a
       implementação de funcionalidades extras no produto não solicitadas pelo cliente. A intenção é que o projeto sirva
       como um guia de implementação de cada história e que seja compreendido também pelo cliente. Caso a equipe se
       depare com um problema cuja representação seja muito difícil, a metodologia recomenda que se construa um
       protótipo executável dessa parte do projeto, reduzindo, assim, o risco de se construir uma versão final
       equivocada daquela história.

    -> Codificação: mesmo depois de desenvolvidas as histórias e de ter sido feito o trabalho de projeto, a codificação
       ainda não é iniciada. Ao invés de procurarem codificar uma versão final do produto, os desenvolvedores criarão
       testes de unidade para cada uma das histórias e só então, após feita e validada essa atividade, o desenvolvimento
       será orientado a uma versão completa e final.

    -> Testes: os testes de unidade criados durante a codificação devem ser aptos à automatização, de modo a permitir
       que sejam feitos rapidamente e repetidos quando necessário. O conjunto de testes de unidade podem ser usados a
       qualquer momento para testes de integração e de validação do produto.

    Em linhas gerais, é assim que o Extreme Programming funciona. No entanto, ele não detém o monopólio das metodologias
    ágeis.

    VISÃO GERAL DO SCRUM
    Outro método, também bastante adaptado às demandas atuais de tempo e qualidade, tem sido alternativa para as
    organizações desenvolvedoras. Trata-se do Scrum, um modelo ágil para a gestão de projetos de software, o qual tem,
    na reunião regular dos seus desenvolvedores para criação de funcionalidades específicas, sua prática mais destacada.
    Suas práticas guardam semelhança com as próprias do XP, mas possuem nomes e graus de importância diferentes nos dois
    contextos. Iniciaremos nossa abordagem com o ciclo tradicional do Scrum, ilustrado na Figura 1.3.

    Figura 1.3 | O ciclo do Scrum
    Fonte: Sabbagh (2013, [s.p.]).
    ----------------------------------------------- IMAGEM: img_1-3.jpg -----------------------------------------------

    Cada um dos elementos do ciclo é abordado na sequência:

    Product Backlog: trata-se da lista que contém todas as funcionalidades desejadas para o produto. O Scrum defende que
                     tal lista não precisa estar completa logo na primeira vez em que é feita. “Pode-se iniciar com as
                     funcionalidades mais evidentes [...] para depois, à medida que o projeto avançar, tratar novas
                     funcionalidades que forem sendo descobertas” (WAZLAVICK, 2013, p.56).

    EXEMPLIFICANDO
    Para que possamos compreender a natureza de um Backlog, vamos considerar que está-se iniciando um novo projeto de
    software e que, antes do efetivo início da criação do produto, um ator do projeto, chamado Product Owner (a
    descrição desse ator será dada logo a seguir), deva criar uma lista do que será produzido ao longo dessa etapa. Tal
    documento, chamado Backlog, é uma lista ordenada, ainda não completa, e dinâmica dos itens que o Product Owner
    acredita que serão produzidos durante o projeto, em seu início (SABBAGH, 2013). Nesse nosso exemplo, o Backlog
    contém apenas os itens necessários para o começo do desenvolvimento.

    Quadro 1.1 | Exemplo de Backlog.lo
    Fonte: adaptado de SABBAGH (2013).
    ---------------------------------------------- IMAGEM: quadro_1-1.png ----------------------------------------------

    Sprint Backlog: lista de tarefas que a equipe deverá executar naquele Sprint. Tais tarefas são selecionadas do
    Product Backlog, com base nas prioridades definidas pelo Product Owner.

    Sprint: o Scrum divide o processo de efetiva construção do software em ciclos regulares, que variam de duas a quatro
    semanas (ou em períodos maiores, a depender da complexidade das tarefas). Trata-se do momento em que a equipe se
    compromete a desenvolver as funcionalidades previamente definidas e colocadas no Sprint Backlog. Se alguma
    funcionalidade nova for descoberta, ela deverá ser tratada na Sprint seguinte. Cabe ao Product Owner manter o Sprint
    Backlog atualizado, apontando as tarefas já concluídas e aquelas a serem concluídas.

    Embora o modelo Scrum defenda que as equipes sejam auto organizadas, ainda assim apresenta três perfis profissionais
    de relevância:

    -> Scrum Master: trata-se de um facilitador do projeto, um agente com amplo conhecimento do modelo e que preza pela
                     sua manutenção durante todas as etapas do projeto. Deve atuar como moderador ao evitar que a equipe
                     assuma tarefas além da sua capacidade de executá-las.

    -> Product Owner: é a pessoa responsável pelo projeto propriamente dito. Ele tem a missão de indicar os requisitos
                      mais importantes a serem tratados nos sprints.

    -> Scrum Team: é a equipe de desenvolvimento, composta normalmente por um grupo de seis a dez pessoas. A exemplo do
                   Extreme Programming, não há divisão entre programador, analista e projetista (WAZLAVICK, 2013)

    Bem, esse foi o conteúdo de natureza mais teórica que queríamos abordar sobre as metodologias ágeis. No entanto,
    ainda precisamos tratar do aspecto prático desses modelos e aproveitaremos esta oportunidade para fazê-lo. Conforme
    já tivemos a oportunidade de discutir, uma das forças que movem as metodologias ágeis é a boa comunicação que deve
    haver entre os elementos envolvidos em um projeto. É através de boas práticas de comunicação que o cliente poderá se
    sentir parte integrante (e essencial) do trabalho e poderá expor com segurança o que espera do futuro sistema. Além
    disso, o bom entrosamento – e a aplicação de técnicas que o aprimoram – é a liga que manterá os membros da equipe
    mutuamente informados sobre o andamento do projeto.

    Imaginemos, então, que você esteja começando seu trabalho em uma desenvolvedora de sistemas, a qual conduz seus
    projetos de acordo com o Scrum. Em dada ocasião, você acessa uma sala e se depara com um quadro branco afixado na
    parede, no qual observa um desenho em formato matricial e vários papéis coloridos colados. Um tanto encabulado,
    pergunta ao seu colega de trabalho do que se trata aquilo e ele diz ser o quadro por meio do qual a equipe mantém o
    controle das atividades desenvolvidas e a desenvolver do projeto em andamento. Para que você possa reconhecer esse
    quadro, no caso de essa situação se tornar real, vamos a algumas dicas sobre ele:

    -> De fato, o quadro Scrum é o meio pelo qual a equipe realiza a gestão visual das atividades do projeto. Uma
       análise mais detalhada do guia do framework Scrum revelará que o quadro não faz parte, oficialmente, da
       metodologia, porém sua adoção foi feita em larga escala pelas equipes e, aparentemente, esse fato não altera sua
       importância.

    -> As divisões do quadro (daí ele conter desenho com formato matricial) são bem simples: uma coluna identifica a
       estória e as três colunas seguintes representam as tarefas relacionadas a esta estória que estão: a fazer (to do)
       , em execução (doing) e feita (done).

    -> Com essa disposição, cada linha do quadro representa uma estória e suas respectivas tarefas, que são, na verdade,
       extraídas do backlog do produto e que foram selecionadas para uma determinada Sprint.

    -> Os papéis coloridos colados no quadro são post-its. Eles representam uma determinada característica ou estado
       daquela tarefa e contêm sua identificação resumida. O exemplo clássico é a do post-it vermelho, que pode
       representar uma tarefa de correção de defeitos em um código. A critério da equipe, uma determinada cor pode
       identificar um determinado membro da equipe. Entretanto, uma forma mais completa e racional de se usar o post-it
       é a que segue:

    Figura 1.4 | Exemplo de controle de atividades por meio de post-it
    Fonte: elaborada pelo autor.
    ------------------------------------------------ IMAGE: img_1-4.jpg ------------------------------------------------

    A dica final é que tanto o quadro quanto a própria metodologia são adaptáveis à cultura e às necessidades das
    equipes. Todavia, em sua essência, o quadro ajuda a comunicar a todos o que cada um está fazendo e em qual estágio
    da atividade ele está, de forma simples e intuitiva.

    Observe, na Figura 1.5, um exemplo de um quadro Scrum:

    Figura 1.5 | Exemplo de quadro Scrum
    Fonte: Sutherland (2014, p. 127).
    ----------------------------------------------- IMAGEM: img_1-5.jpg -----------------------------------------------

    Bem, mas será que podemos contar apenas com pedaços de papel autocolantes para registrar nossas tarefas no Scrum?
    Embora os post-its sejam úteis para a visualização, digamos, off-line do andamento do projeto, dispomos de
    ferramentas computacionais colaborativas que facilitam bastante o controle de um projeto, e a primeira que merece
    menção é o Trello, cujo acesso é gratuito. O início do cadastramento da sua conta acontece quando você fornece seu
    endereço de e-mail. Em seguida, você já pode dar um nome ao seu time, escolher o tipo do seu time e adicionar
    membros a ele, conforme exibido na Figura 1.6.

    Figura 1.6 | Ambiente de cadastramento de conta no Trello
    Fonte: captura de tela do Trello elaborada pelo autor.
    ----------------------------------------------- IMAGEM: img_1-6.jpg -----------------------------------------------

    Depois de fornecer essas informações, você será levado a um conjunto de opções e, dentre elas, poderá escolher um
    modelo de quadro em que as tarefas (e demais informações) serão exibidas. Se você escolher o Template Kanban, obterá
    um quadro semelhante ao exibido na Figura 1.7 De acordo com texto da autora do template, disponível na mesma página
    do modelo, ele deve ser usado para manter a equipe com o mesmo nível de informação, para que todos possam seguir o
    trabalho com fluidez.


    Figura 1.7 | Template Kanban no Trello
    Fonte: captura de tela do Trello de Alvernaz ([s.d.]).
    ----------------------------------------------- IMAGEM: img_1-7.jpg -----------------------------------------------

    Basta agora criar um quadro real com base nesse modelo e pronto! A partir daí é só inserir as tarefas e as
    informações relacionadas a elas para ter um controle eficiente do seu projeto Scrum. A fim de que você possa
    utilizar corretamente a ferramenta, vale um resumo de cada uma das colunas apresentadas no template:

    -> Backlog: aqui devem ser inseridas e descritas as tarefas do projeto, cada uma em seu cartão. A equipe deve ter a
       liberdade de inserir aqui tarefas que deverão ser, eventualmente, executadas no futuro, mas que ainda não devem
       ser movidas para a coluna “A Fazer”.

    -> Elaboração e pesquisa: nessa coluna a equipe deve colocar tarefas que precisam ser mais bem detalhadas e sobre as
       quais recai necessidade de pesquisa antes que sejam movidas para a próxima etapa. A ferramenta trata essa coluna
       como apropriada para atividades de projeto ou design, conforme assinalado no título da coluna.

    -> A Fazer: após a tarefa ser devidamente detalhada e um eventual aprofundamento ter sido feito, ela deve ser levada
       a essa coluna, como sinalização de que está pronta para ser executada. Nesse caso, um ou mais responsáveis devem
       ser atribuídos a ela e a data de entrega deve ser estipulada.

    -> Em andamento: quando as tarefas estão efetivamente em execução elas devem ocupar esta coluna. Dessa forma, todos
       os envolvidos poderão conferir o andamento das atividades executadas pelos pares e a ferramenta permite,
       inclusive, que mensagens sejam deixadas diretamente nas tarefas como forma de promover a comunicação.

    -> Revisão de código: no momento em que a tarefa estiver em vias de ser concluída, ela deve ser movida para esta
       coluna, a fim de que seja revisada por membro designado da equipe. Embora o título dela seja Revisão de Código,
       vale aqui qualquer tipo de conferência ou validação.

    -> Feito: assim que a tarefa é concluída, ela é movida para esta coluna, que não está completamente visível na
       Figura 1.7.

    A seguir veja uma síntese sobre o fluxo de um projeto Scrum.

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

    SAIBA MAIS
    Em meados dos anos 1980, Hirotaka Takeuchi e Ikujiro Nonaka definiram uma estratégia flexível e abrangente de
    criação de um produto, na qual a equipe de desenvolvimento trabalhava como uma unidade para atingir um objetivo
    comum. Eles descreveram uma abordagem inovadora para o desenvolvimento de artefatos, a qual eles chamaram de
    "abordagem rugby". A partir dela, uma equipe tenta percorrer a distância como uma unidade, passando a bola para
    frente e para trás. Os pesquisadores japoneses propuseram que o desenvolvimento do produto não deveria ser como uma
    corrida de revezamento sequencial, mas análogo ao jogo de rúgbi, no qual a equipe trabalha junto, passando a bola
    para frente e para trás enquanto se move como uma unidade pelo campo. O conceito de rugby de um "Scrum" (momento em
    que um grupo de jogadores se forma para reiniciar o jogo) foi introduzido para descrever a proposta feita pelos
    pesquisadores.

    Ken Schwaber e Jeff Sutherland desenvolveram o conceito Scrum e sua aplicabilidade no desenvolvimento de software em
    uma apresentação na conferência Programação Orientada a Objetos, Sistemas, Linguagens e Aplicações (OOPSLA)
    realizada em 1995, em Austin, Texas. Desde então, vários praticantes, especialistas e autores de Scrum continuaram a
    refinar seu conceito e sua estrutura. Nos últimos anos, o Scrum cresceu em popularidade e agora é a abordagem de
    desenvolvimento de projeto preferida para muitas organizações em todo_ o mundo (A GUIDE..., 2015).

    PESQUISE MAIS
    O Framework Scrum representa o conjunto de princípios e de práticas do Scrum voltado a promover o desenvolvimento de
    um produto de software de forma ágil e unitária. O Product Owner, o Scrum Master e os eventos do Scrum são exemplos
    de partes integrantes desse Framework. A Parte II da obra de Fábio Cruz (2018) detalha todos os elementos do Scrum.

    CRUZ, F. Scrum e Agile em Projetos. Guia Completo. 2. ed. Rio de Janeiro: Brasport, 2018.

    Outra abordagem importante do Framework Scrum pode ser encontrada no primeiro capítulo da obra de Edson Silva
    chamada Scrum e FTS: uma abordagem prática (SILVA, 2017).

    SILVA, E. C. Scrum e FTS: uma abordagem prática. Rio de Janeiro: Brasport Livros e Multimídia, 2017.

    Por fim, o capítulo 4 da obra Engenharia de Software: conceitos e práticas (WAZLAWICK, 2013), apresenta abordagem
    bastante sucinta sobre o Scrum, no contexto dos métodos ágeis.

    WAZLAWICK, R. S. Engenharia de software: conceitos e práticas. Rio de Janeiro: Elsiever, 2013.

    Essa foi, portanto, a exposição de conteúdo relacionado a metodologias ágeis. Tivemos a oportunidade de conhecer
    conceitos, práticas e, principalmente, de realizar comparações entre o novo e o tradicional. Em sua jornada
    profissional, você certamente encontrará organizações desenvolvedoras que um dia ousaram transformar seus processos
    e tornarem-se ágeis, outras que já foram concebidas como tais e, finalmente, outras tantas que preferiram continuar
    desenvolvendo programas seguindo padrões tradicionais. Em breve você será desafiado a decidir como a sua organização
    irá atuar e o embasamento aqui adquirido será fundamental. Continue focado nas leituras e nas atividades propostas!

    #ref Unidade 1 - Seção 2
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    A GUIDE to the Scrum Body of Knowledge (SBOK GUIDE). 3. ed. [S.l.]: SCRUMstudy, 2015. Disponível em https://apple.co/3nxZA3t. Acesso em: 18 out. 2020.

    ALVERNAZ, A. Template Kanban. Trello, [S.l., s.d.]. Disponível em: https://bit.ly/3gYRRZD. Acesso em: 12 dez. 2020.

    BECK, K. et al. Manifesto para Desenvolvimento Ágil de Software. Agile Manifesto, [S.l.], 2001. Disponível em:
    https://bit.ly/37tc1Ib. Acesso em: 29 out. 2020.

    CRUZ, F. Scrum e Agile em Projetos. Guia Completo. 2. ed. Rio de Janeiro: Brasport, 2018.

    PRESSMAN, R. S., MAXIM, B. R. Engenharia de Software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.

    SABBAGH, R. Gestão Ágil para Projetos de Sucesso. Edição Eletrônica: Casa do Código, 2013.

    SILVA, E. C. Scrum e FTS: uma abordagem prática. Rio de Janeiro: Brasport Livros e Multimídia, 2017. Disponível em:
    https://bit.ly/38d2kwO. Acesso em: 29 out. 2020.

    SUTHERLAND, J. A Arte de Fazer o Dobro do Trabalho na Metade do Tempo. São Paulo: LeYa, 2014.

    TELES, V. M. Extreme Programming: aprenda como encantar seus usuários desenvolvendo software com agilidade e alta
    qualidade. São Paulo: Novatec Editora, 2006.

    WAZLAWICK, R. S. Engenharia de software: conceitos e práticas. Rio de Janeiro: Elsiever, 2013.
    """


def unidade1_secao3():
    """
    ----------------------------------------------- UNIDADE 1 / SEÇÃO 3 -----------------------------------------------
    CONTROLE DE VERSÕES - Roque Maitino Neto

    CONCEITO-CHAVE
    Um software é um produto em constante evolução. Da sua concepção até a entrega (e além dela), ele nasce, cresce e
    carece de manutenção ao longo de um ciclo de vida bem definido e conhecido. Na condição de um produto dinâmico, seu
    processo de construção e sua manutenção requerem gerenciamento contínuo em todos os aspectos de sua construção e,
    mesmo em um estado considerado apto para entrega, um software passa por diversas modificações, e cada uma delas tem
    como resultado uma nova versão dele próprio. Por isso, um controle eficiente das revisões é necessário, o que é
    atingido por meio da utilização de uma ferramenta de controle de versões.

    GERENCIAMENTO DE CONFIGURAÇÃO DO SOFTWARE
    Embora o controle de versões seja o foco desta seção, será necessário contextualizá-lo em um tema mais abrangente,
    do qual ele faz parte como um elemento muito importante. Esse tema mais abrangente se chama Gerenciamento da
    Configuração do Software (GCS) que, de modo objetivo, é o meio pelo qual se proporciona controle a todo_ o processo
    de desenvolvimento de software (LEON, 2004). Esse controle se torna necessário, entre outros motivos, pela
    complexidade envolvida no processo de desenvolvimento e pela grande quantidade de componentes de um software.

    A motivação maior para a criação e para a estruturação de uma disciplina que cuida da Gerência de Configuração de
    Software foi a necessidade de controlar as modificações pelas quais inevitavelmente passa um programa, o que é feito
    com o uso de métodos e de ferramentas e com o intuito de maximizar a produtividade e minimizar os erros cometidos
    durante a evolução.

    A GCS é, portanto, um conjunto de práticas que controlam e notificam as inúmeras correções, extensões e adaptações
    aplicadas no software durante seu ciclo de vida, com o objetivo de assegurar um processo de desenvolvimento e de
    evolução organizado e passível de ser rastreado (DANTAS, 2009).

    Como o GCS não se resume a uma ação apenas, ele é composto por uma série de atividades bem definidas e estruturadas.
    De acordo com IEEE (2004), essas atividades incluem: gerenciamento e planejamento do processo de GCS, identificação
    de configuração do software, controle de configuração de software, controle de status de configuração de software,
    auditoria de configuração de software, gerenciamento da entrega e do lançamento de software e configuração das
    ferramentas de gerenciamento. A Figura 1.10 ilustra essas atividades em uma estrutura hierárquica.

    Figura 1.10 | Estrutura de tópicos do Gerenciamento da Configuração do Software
    Fonte: adaptada de IEEE (2004).
    ----------------------------------------------- IMAGEM: img_1-10.jpg -----------------------------------------------

    Na sequência serão discutidas as três primeiras grandes atividades do SCM, colocadas nos retângulos da Figura 1.10,
    de acordo com IEEE (2004).

    -> Gerenciamento do Processo de CGS: conforme temos mencionado, o GCS controla a evolução e a integridade de um
       produto e o faz por meio da identificação dos seus elementos, pelo gerenciamento e controle das mudanças
       aplicadas e pela verificação, registro e relato das informações de configuração. Da perspectiva do engenheiro de
       software, o SCM facilita o desenvolvimento e as atividades de implementação de mudanças. Uma implementação de SCM
       bem-sucedida requer planejamento e gerenciamento cuidadosos, o que, por sua vez, requer compreensão do contexto
       organizacional e das restrições impostas ao projeto e à implementação do processo de SCM.

    -> Identificação da configuração do software: essa atividade identifica os itens a serem controlados, estabelece
       esquemas de identificação para os itens e suas versões e, por fim, estabelece as ferramentas e técnicas a serem
       utilizadas na aquisição e no gerenciamento de itens controlados.

    -> Controle de configuração de software: essa atividade trata do gerenciamento de mudanças durante o ciclo de vida
       do software. Ela abrange o procedimento para determinar quais mudanças fazer, a autoridade para aprovar certas
       mudanças, o suporte para a implementação dessas mudanças e o conceito de desvios formais dos requisitos do
       projeto.

    ASSIMILE
    A Gerência de Configuração de Software é um processo aplicado a todas as fases que compõem o ciclo de vida de um
    software, estabelecendo regras formais para identificar e controlar mudanças por meio de um controle sistemático
    sobre modificações realizadas (CAETANO, 2004).

    Mesmo com a evidente necessidade de se gerenciar a configuração de um software, essa prática sofre com alguns mitos,
    muitos deles com potencial para desencorajar sua adoção nas organizações. Nas próximas linhas trataremos de três
    desses mitos e daremos bons motivos para que eles sejam desconstruídos, sempre com base na visão de Leon (2004).

    -> Mito 1 – Promover o gerenciamento da configuração de um software significa ter mais trabalho e adotar novos
       procedimentos: de fato a implantação e o gerenciamento adequados de uma sistemática de GCS não é uma tarefa
       simples. O período de transição entre um ambiente sem gerenciamento e um cenário de efetiva utilização de uma
       ferramenta para esse fim costuma ser difícil, já que novas habilidades devem ser desenvolvidas, novos
       procedimentos devem ser seguidos, entre outros desafios. No entanto, a transição será tão mais simples quanto
       mais eficiente for o trabalho das equipes de gerenciamento e de implementação do GCS. Ao utilizarem o sistema, os
       desenvolvedores e outros atores do processo de criação do software deverão compreender seus potenciais benefícios
       e o esforço que conseguirão evitar por meio da automação de tarefas e da eliminação de erros. Atualmente, as
       ferramentas de gerenciamento de configuração de um software automatizam todas as tarefas repetitivas, facilitando
       assim a atuação do pessoal envolvido com o produto.


    -> Mito 2 – O gerenciamento da configuração é de responsabilidade única do pessoal da administração do sistema: ao
       contrário do que sugere o mito, a implantação e a condução do GCS é responsabilidade de todas as pessoas
       envolvidas no processo de desenvolvimento de software embora a principal tarefa do pessoal da administração seja
       criar um ambiente organizacional no qual o GCS possa prosperar. Uma equipe de GCS precisa de todo_ o apoio do
       pessoal da administração para ter condições de implantar o sistema de gerenciamento da configuração aos poucos,
       pois é esse pessoal que deve monitorar a implementação e a operação do GCS, revisar periodicamente seu progresso
       e tomar as ações corretivas quando necessário.

    -> Mito 3 – O gerenciamento da configuração é apenas para os desenvolvedores: certamente as equipes de
       desenvolvedores constituem um dos mais frequentes usuários do GCS. Além disso, são os desenvolvedores que mais se
       beneficiam de um sistema de gerenciamento corretamente implementado. Problemas como perda de código-fonte,
       incapacidade de encontrar a última versão de um arquivo e reaparecimento de erros já corrigidos podem ser
       evitados com um sistema desses. Entretanto, há desenvolvedores que enxergam o GCS como perda de tempo e dele
       participam apenas por serem obrigados a isso. A potencial hostilidade voltada ao GCS pode ser eliminada se os
       desenvolvedores forem educados nos princípios da prática e esclarecidos sobre seus benefícios. As ferramentas
       atuais de GCS proporcionam um nível fenomenal de automação, o que acaba contribuindo para que outros atores do
       processo de desenvolvimento acabem se beneficiando delas, incluindo testadores e pessoal de qualidade, manutenção
       e suporte.

    REFLITA
    Com que frequência as equipes de desenvolvimento rejeitam ou boicotam um processo de gerenciamento de configuração
    de software? Bem, a resposta deverá variar conforme a familiaridade da equipe com as ferramentas de GCS, com a
    disposição a aceitar mudanças, entre outros fatores. Em certas equipes pode preponderar o sentimento de que tudo o
    que se refere ao software está bem registrado na memória de seus componentes ou que uma mera anotação em algum
    arquivo servirá como registro das mudanças efetivadas no produto. Com isso, a resistência a colocar em funcionamento
    um processo de GCS pode ser maior do que a eventual dificuldade técnica de implantá-lo?

    CONTROLE DE VERSÕES
    Feita a contextualização do Gerenciamento de Configuração do Software com o ambiente em que o controle de versões
    está inserido, avançamos para a abordagem desse tema. De acordo com Caetano (2004), o controle de versões é o meio
    pelo qual o GCS controla, de forma consistente, as modificações realizadas em um sistema. Isso ocorre por meio das
    seguintes funções:

    -> Recuperar versões anteriores do sistema.
    -> Auditar as modificações realizadas, levantando quem alterou, quando alterou e o que alterou.
    -> Automatizar o rastreamento de arquivos.
    -> Estabelecer meios para obter a situação de um projeto em determinado ponto do tempo.
    -> Prevenir conflitos entre desenvolvedores.
    -> Permitir o desenvolvimento paralelo do um ou mais sistemas.

    REPOSITÓRIO
    Todas essas funções parecem convergir para um elemento bem definido: a centralização dos dados. E se não tivéssemos
    essa centralização? Bem, o uso descentralizado de um arquivo de código-fonte, por exemplo, permitiria que vários
    programadores acessassem vários arquivos e cada alteração feita nele não seria refletida nos demais. Assim, o
    desenvolvimento paralelo seria inviável e o conflito entre desenvolvedores inevitável. O recurso que as ferramentas
    de controle de versão (abordadas a seguir) usam é o repositório, local em que programas em desenvolvimento, fotos,
    vídeos e demais arquivos ficam armazenados e podem ser acessados de forma controlada por todos os envolvidos no
    desenvolvimento do produto.

    BASELINES (LINHAS DE BASE)
    Um conceito importante no escopo do controle de versão é a baseline de software. As baselines representam conjuntos
    de itens de configuração formalmente aprovados, os quais servem de base para as etapas seguintes de desenvolvimento.
    Quando, no entanto, uma entrega formal é feita ao cliente no final de uma iteração, denominamos tal entrega de
    release. Baselines e releases são identificadas no repositório de programas, na grande maioria das vezes, pelo uso
    de etiquetas (tags) (DANTAS, 2009).

    O termo também é usado para se referir a uma versão específica de um item de configuração de software que foi
    acordado e, em qualquer caso, a baseline só pode ser alterada por meio de procedimentos formais de controle de
    mudanças. Uma baseline, junto com todas as alterações aprovadas na linha de base, representa a configuração aprovada
    atual.

    As comumente usadas são as linhas de base funcionais, alocadas, de desenvolvimento e de produto. A linha de base
    funcional corresponde aos requisitos de sistema revisados. A linha de base alocada corresponde à especificação de
    requisitos de software revisada e à especificação de requisitos de interface de software. A linha de base de
    desenvolvimento representa a configuração de um software em evolução, em momentos selecionados, durante o ciclo de
    vida do software. A autoridade de mudança para essa linha de base normalmente é da organização de desenvolvimento,
    mas pode ser compartilhada com outras organizações. A linha de base do produto corresponde ao produto de software
    completo e entregue para integração de sistema (IEEE, 2004).

    BRANCHES
    A Gerência de Configuração de Software também permite que a implementação de novas funcionalidades por uma equipe
    seja realizada em paralelo, mas de forma isolada e independente das modificações de outros desenvolvedores. O
    isolamento é obtido com uso de ramificações (branches). As linhas de desenvolvimento (codelines) são designadas para
    cada projeto e são compartilhadas por vários desenvolvedores. A primeira linha de desenvolvimento definida no
    projeto é, por convenção, nomeada mainline. O ramo é criado no repositório e representa uma linha secundária de
    desenvolvimento, a qual pode ser unida novamente à linha principal (mainline) por meio da operação de junção (merge)
    . Atualmente, a necessidade de atender, ao mesmo tempo, as múltiplas demandas do projeto tornam o uso de ramos um
    diferencial (DANTAS, 2009).

    FERRAMENTAS DE CONTROLE DE VERSÃO
    Como era de se esperar, as funções próprias do controle de versões podem (e devem) ser executadas por uma ferramenta
    computacional, fato que naturalmente apresenta indiscutíveis vantagens em relação a uma eventual execução manual. O
    mercado disponibiliza ótimas ferramentas de controle de versão e três delas serão abordadas na sequência. Os
    critérios para adoção da ferramenta mais adequada deverão variar entre organizações, mas vale o alerta de que
    nenhuma decisão deve ser tomada com base na convicção de que ela fará as vezes de um compilador, de que substituirá
    o gerente do projeto, ou de que ela pode se tornar um meio de automatizar testes. Passemos, então, à discussão de
    duas das mais importantes e utilizadas ferramentas de controle de versão.

    GIT E GITHUB
    Nossa primeira providência, ao tratarmos das ferramentas Git e GitHub, será a de diferenciá-las. Apesar de terem
    nomes bastante parecidos e de serem produtos do mesmo desenvolvedor, suas funções são distintas: o Git é uma
    ferramenta de controle de versão bastante popular entre desenvolvedores e apresenta recursos de colaboração bastante
    aprimorados, incluindo fóruns de discussão para os projetos em desenvolvimento e para abordagem das alterações em
    curso. Presente também em outras ferramentas de controle de versão, os branches implementados no Git viabilizam o
    trabalho em paralelo entre membros da equipe e o controle de subprojetos que um desenvolvedor pode manter para
    experimentos próprios, incluindo correção de bugs e aprimoramento de funções, sem que os arquivos do repositório
    central sejam alterados e com a possibilidade de que seus experimentos sejam compartilhados (MAILUND, 2017).

    O Git é um sistema de controle de versão gratuito e de código aberto, concebido para lidar com todos os projetos,
    desde os pequenos até aqueles bem grandes e que movimentam praticamente toda as equipes. Ele é bem fácil de ser
    aprendido e ocupará pouco espaço do servidor. Além disso, seu desempenho é bastante satisfatório. Mas e a segurança?
    Bem, o modelo de dados que o Git usa garantirá a integridade criptográfica de cada bit dos projetos. Cada arquivo e
    cada operação de commit passa por verificação de checksum, operação também aplicada em sua recuperação. Será
    impossível extrair qualquer coisa do Git além dos bits exatos que foram adicionados.

    O recurso do Git que realmente o diferencia de quase todos os outros sistemas de controle de versão existentes é seu
    modelo de branching (ou ramificação). Com o Git, é possível ter vários branches nas máquinas locais, os quais podem
    ser independentes uns dos outros. As operações de criação, merge e exclusão dos branches leva alguns poucos segundos
    apenas. Com esse diferencial, as equipes poderão trocar de contexto quase que imediatamente, além de criar branches
    para experimentar uma ideia e, mesmo aplicando a operação de commit, voltar ao ponto de onde começou. O mesmo cabe
    para a aplicação de um patch, por exemplo.

    O GitHub é equivalente ao repositório do Git, mas disponível em uma plataforma mundial e com acesso gratuito aos
    desenvolvedores que lá desejarem armazenar seus programas e compartilhá-los com outros desenvolvedores. Por meio da
    página de cadastro (GITHUB, c2020) é possível criar sua conta no GitHub e começar a fazer parte dessa grande
    comunidade. Bem, mas o que é possível obter com a criação de uma conta no GitHub além de um espaço para compartilhar
    código? A resposta mais simples vem com apenas uma palavra: visibilidade. Empresas de TI já consideram o repositório
    do candidato no GitHub como um dos critérios para sua contratação. Tamanha importância justifica nossa incursão por
    essa ferramenta, começando pelo passo a passo de cadastramento na plataforma.

    1. Acesse a página de cadastro (GITHUB, c2020) e preencha os espaços com os dados solicitados.

    2. Após a escolha de sua senha e da verificação da conta, a plataforma o levará para uma página em que você poderá
       escolher, nesta ordem:

    -> Seu tipo principal de trabalho.
    -> Seu nível de experiência em programação.
    -> Qual o uso que você pretende dar ao GitHub.
    -> Qual seu interesse (para que a ferramenta possa conectá-lo a comunidades com as mesmas afinidades que a sua).

    Para essas opções, nossas escolhas foram: estudante, pequena experiência em programação, interesse em aprender o Git
    e o GitHub e resposta em branco, respectivamente.

    3. Após a confirmação do seu endereço de e-mail, você será direcionado à tela em que poderá escolher o que deseja
       fazer primeiro: criar um novo repositório (ou um novo projeto), criar uma organização ou começar a aprender,
       conforme mostra a Figura 1.11.

    Figura 1.11 | Tela de escolha da ação inicial no GitHub
    Fonte: captura de tela do GitHub.
    ----------------------------------------------- IMAGEM: img_1-11.jpg -----------------------------------------------

    4. Ao criar um novo projeto, a primeira ação a ser tomada é a escolha de um nome para o repositório, que estará
       atrelado ao nome de usuário que você escolheu no passo inicial. O nome escolhido para o repositório foi engsoft e
       a visibilidade escolhida foi a pública. Nenhuma opção de inicialização foi escolhida.

    5. Neste ponto, uma tela com uma série de opções será oferecida, conforme ilustra a Figura 1.12.

    Figura 1.12 | Visão parcial da tela de opções do GitHub
    Fonte: captura de tela do GitHub elaborada pelo autor.
    ----------------------------------------------- IMAGEM: img_1-12.jpg -----------------------------------------------

    A partir deste ponto, você pode criar seus arquivos de código ou fazer upload de um já existente em sua máquina.

    Note o nome do usuário e o nome do repositório (roquemaitino/engsoft) na porção central e à esquerda da tela. Para
    que um arquivo estivesse disponível no repositório, foi feita a escolha de upload de um arquivo existente e, na
    sequência, acionado o botão de Commit. O arquivo escolhido foi Maior.java, uma aplicação simples em Java, que exibe
    o maior valor entre os oito informados pelo usuário via teclado.

    Pronto! Ao acessar a página inicial desse perfil (MAITINO, 2020), você poderá ter acesso também à aplicação Java que
    disponibilizamos e alterar seu código por meio da criação de um branch.

    A seguir veja uma síntese sobre as atividades de um processo de software.

    CVS (CONCURRENT VERSION SYSTEM OU SISTEMA DE VERSÕES CONCORRENTES)
    Trata-se de uma ferramenta open source que implementa as principais funções relacionadas ao processo de controle de
    versões. O CVS armazena em seu repositório as modificações realizadas num arquivo ao longo do tempo. Cada
    modificação é identificada por um número chamado revisão. Toda revisão armazena as modificações realizadas, quem
    realizou as modificações, quando foram realizadas, entre outras informações (CAETANO, 2004). A Figura 1.13 ilustra
    as principais funções realizadas pelo CVS.

    Figura 1.13 | Principais operações realizadas pelo CVS
    Fonte: adaptado de Caetano (2004, p. 15).
    ----------------------------------------------- IMAGEM: img_1-13.jpg -----------------------------------------------

    O repositório CVS – assim como o de outras ferramentas – armazena uma cópia completa de todos os arquivos e
    diretórios que estão sob controle de versão. Normalmente, o desenvolvedor nunca acessa nenhum dos arquivos no
    repositório diretamente. Em vez disso, usa comandos CVS para obter sua própria cópia dos arquivos em uma área de
    trabalho e, em seguida, trabalha nessa cópia. Quando termina um conjunto de alterações, realiza uma operação chamada
    commit (ou confirmação) de volta para o repositório. Por isso, o repositório guarda as mudanças feitas pelo
    desenvolvedor, além de registrar exatamente o que e quando foi alterado e outras informações semelhantes. Observe
    que o repositório não é um subdiretório da área de trabalho ou vice-versa e que eles devem estar em locais separados
    (GNU, [s.d.]).

    A estrutura geral do repositório é uma árvore de diretórios correspondente aos existentes no diretório de trabalho.
    Por exemplo, supondo que o repositório esteja em /usr/local/cvsroot, uma possível estrutura de diretório é mostrada
    na Figura 1.14.

    Figura 1.14 | Uma possível estrutura de diretórios do repositório CVS
    Fonte: GNU ([s.d.]).
    ----------------------------------------------- IMAGEM: img_1-14.jpg -----------------------------------------------

    Na estrutura de diretórios estão os arquivos de histórico de cada arquivo sob controle de versão. O nome do arquivo
    de histórico é o nome do arquivo correspondente com ‘, v’ anexado ao final. Os arquivos “index.php,v” e
    “frontend.c,v” são exemplos possíveis de arquivos de históricos. Eles guardam, entre outras coisas, informações
    suficientes para recriar qualquer revisão do arquivo, mais um log de todas as mensagens de commit e o nome do
    usuário que enviou a revisão. Os arquivos de histórico são conhecidos como arquivos RCS, porque o primeiro programa
    a armazenar arquivos nesse formato foi um sistema de controle de versão conhecido como RCS (GNU, [s.d.]).

    EXEMPLIFICANDO
    Conforme ilustrado na figura a seguir, vários desenvolvedores podem trabalhar de forma concorrente em um mesmo
    sistema. Como alternativa, é possível atuar isoladamente em sistemas diferentes. Este exemplo de operação do CVS
    inclui um repositório central e três usuários, cada um com sua cópia de trabalho. As transições de comandos update
    (ou check-out) e commit (ou check-in) também estão representadas na Figura 1.15.

    Figura 1.15 | Exemplo de funcionamento do CVS
    Fonte: elaborada do autor.
    ----------------------------------------------- IMAGEM: img_1-15.jpg -----------------------------------------------

    Cada alteração feita no programa gera um novo número de versão que o identifica. O CVS atribui automaticamente
    números como 1.1, 1.2 e assim por diante para as versões geradas. Um arquivo pode ter várias versões e, da mesma
    forma, um produto de software pode ter várias versões. Esse produto geralmente recebe um número de versão como
    “4.1.1”. Cada versão de um arquivo possui um número de revisão exclusivo. Os números de revisão são semelhantes a
    “1.1”, “1.2”, “1.3.2.2” ou mesmo “1.3.2.2.4.5”.

    Um número de revisão sempre tem um número par de inteiros decimais separados por ponto. Por padronização, a revisão
    1.1 é a primeira de um arquivo. Cada uma delas recebe sucessivamente um novo número, aumentando o número mais à
    direita em um. A Figura 1.16 exibe algumas revisões, com as mais recentes à direita. Também é possível terminar com
    números contendo mais de um ponto, por exemplo “1.3.2.2”.

    Figura 1.16 | Representação de revisões mais recentes no número à direita
    Fonte: GNU ([s.d.]).
    ----------------------------------------------- IMAGEM: img_1-16.jpg -----------------------------------------------

    Antes de encerrarmos o conteúdo do CVS, vale tratarmos de mais algumas terminologias relacionadas ao assunto (GNU,
    [s.d.]).

    -> Checkout: denominação dada à primeira recuperação (ou download) de um módulo do sistema vindo do repositório do CVS.

    -> Commit: trata-se do envio do artefato modificado ao repositório do CVS.

    -> Export (ou Exportação): trata-se da recuperação (ou download) de um módulo inteiro a partir de um repositório, sem
                               os arquivos administrativos CVS. Módulos exportados não ficam sob controle do CVS.

    -> Import (ou Importação): esse termo identifica a criação de um módulo completo no âmbito de um repositório CVS, feita
                               por meio de um upload de uma estrutura de diretórios.

    -> Module (ou módulo): é a representação de uma hierarquia de diretórios. Um projeto de determinado software
                           efetiva-se como um módulo dentro do repositório.

    -> Release: este termo equivale a um “lançamento”. Um número de release identifica a versão de um produto completo
                ou inteiro.

    ASSIMILE
    Release é o termo usado para descrever a denominação atribuída a um conjunto de arquivos para identificar
    determinado ponto no tempo, sobretudo quando se quer identificar um conjunto de novas características ou correções
    de um software (CAETANO, 2004).

    -> Merge: refere-se à fusão das diversas modificações feitas por diferentes usuários na cópia local de um mesmo
              arquivo. Sempre que alguém altera o código, é necessário realizar uma atualização antes da aplicação da
              operação de commit, a fim de que seja feita a fusão das mudanças.

    SAIBA MAIS
    Operações aplicadas nos branches

    A utilização dos branches não seria completa se não pudéssemos aplicar operações em suas instâncias por meio de
    comandos específicos. Vejamos alguns deles, segundo Vormittag (2016):

    1 - git branch <nome>: cria um novo branch com o nome escrito em <nome>.

    2 - git checkout <branch>: seleciona um branch específico, tornando-o o branch atual, com o qual o desenvolvedor
                               trabalhará.

    3 - git branch: este comando, sem argumentos, fornece a lista de todos os branches do projeto. A ferramenta indica o
                    atual com um asterico posicionado próximo a ele.

    4 - git mv: comando usado para mover ou renomear arquivos.

    5 - git rm: comando usado para remover arquivos a partir da linha de comando. Neste caso vale um registro: você
                também pode usar o Windows Explorer ou outro gerenciador de arquivos para mover, renomear ou remover
                arquivos de um projeto do GitHub.

    PESQUISE MAIS
    A indicação relacionada à utilização de branches no GitHub é a leitura do tutorial disponível no site Hostinger
    (LONGEN, 2019).

    LONGEN, A. S. Como Usar Um Git Branch. Hostinger, [S.l.], 23 abr. 2019.

    Este foi, portanto, o conteúdo que queríamos compartilhar com você. O entendimento de da importância do
    gerenciamento da configuração de um software e a familiaridade com os termos e o funcionamento de uma ferramenta de
    controle de versões são habilidades imprescindíveis para o desenvolvedor inserido em uma equipe de trabalho e ao
    gestor do software. Esperamos que este conteúdo seja útil a você em breve. Boa sorte e bons estudos!

    #ref Unidade 1 - Seção 3
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    CAETANO, C. CVS – Controle de Versões e Desenvolvimento Colaborativo de Software. São Paulo: Novatec Editora, 2004.

    DANTAS, C. Gerência de Configuração de Software. DevMedia, [S.l.], 2009. Disponível em: https://bit.ly/2LOcXP7.
    Acesso em: 26 out. 2020.

    GIT FOR WINDOWS. Git for Windows – Version 2.29.2.3. Git for Windows, [S.l.], 2020. Disponível em:
    https://gitforwindows.org/. Acesso em: 13 dez. 2020.

    GITHUB. Join. GitHub, [S.l.], c2020. Disponível em: https://github.com/join. Acesso em: 12 dez. 2020.

    GNU. The Repository. GNU, [S.l., s.d.]. Disponível em: https://bit.ly/38incTg. Acesso em: 27 out. 2020.

    IEEE Computer Society. Guide to the Software Engineering Body of Knowledge. Piscataway: The Institute of Electrical
    and Electronic Engineers, 2004.

    LEON, A. Software Configuration Management Handbook. 3. ed. Boston: Artech House, 2015.

    LONGEN, A. S. Como Usar Um Git Branch. Hostinger, [S.l.], 23 abr. 2019. Disponível em: https://bit.ly/3r8DGWC.
    Acesso em: 28 nov. 2020.

    MAILUND, T. The Beginner’s Guide to GitHub. [S.l.: s.n.], 2017. E-book.

    MAITINO, R. Roquemaitino/engsoft. GitHub, [S.l.], 2020. Disponível em: https://bit.ly/3nJHqfr. Acesso em: 12 dez.
    2020.

    VORMITTAG, R. A Practical Guide to Git and GitHub for Windows Users. 2. ed. [S.l.]: Reiter Consulting, 2016. E-book.
    """


def unidade2_secao1():
    """
    ----------------------------------------------- UNIDADE 2 / SEÇÃO 1 -----------------------------------------------
    INTRODUÇÃO A QUALIDADE DE SOFTWARE

    CONCEITO-CHAVE

    Caro aluno, certamente alguma vez na vida você já deve ter adquirido um produto ou serviço, o qual, no momento da
    compra, parecia perfeito, mas, ao utilizá-lo, as coisas acabaram saindo bem diferente do prometido. Como consumidor,
    isso traz muita frustração. E isso não é uma exclusividade da Tecnologia da Informação. Corriqueiramente, ocorre
    também na telefonia, na alimentação, no e-commerce, na entrega de encomendas, de roupas, etc.

    QUALIDADE DE SOFTWARE [#]
    No que se diz respeito à desenvolvimento de softwares, a qualidade visa basicamente atender as necessidades e
    expectativas do cliente, a fim de cumprir os requisitos acordados no início do projeto de desenvolvimento de
    software. O tema é bem mais abrangente do que essa simples definição e é isso que torna os assuntos relacionados à
    qualidade de software de extrema importância para os profissionais de T.I.

    Segundo Zanin et al. (2018) [#], a qualidade de software está ligada aos aspectos de conformidade com os requisitos
    funcionais e não funcionais encontrados nos desenvolvimentos de softwares. Para compreender melhor, observe a
    definição dos requisitos:


     Requisitos funcionais [#]: especificam uma função que o sistema ou que determinado componente do sistema deve
      realizar .Essa descrição é feita do ponto de vista do usuário e pode ser determinante para o comportamento do
      sistema, de  modo que precisa ficar bem claro o que deve ocorrer com uma entrada no software e qual a saída gerada

      . Para melhor exemplificar esse conceito, imagine que o seu cliente descreva que um software deve, após o usuário
      incluir os produtos no carrinho de compras, apresentar a opção de pagamento em crédito, débito ou boleto bancário.
      A nível de desenvolvimento, esse funcionamento é de extrema importância, pois determina quais são as
      funcionalidades que o software deve apresentar. Por exemplo: inserir, alterar, excluir, listar produtos, etc.

     Requisitos não funcionais [#]: esses requisitos podem estar relacionados a necessidades que devem ser atendidas,
      porém não utilizam funcionalidades. Esse conceito está diretamente ligado à qualidade de software, ou seja, trata
      das premissas técnicas que o software deve desempenhar. Um exemplo é a solicitação de um cliente para que
      determinada aplicação web seja responsiva, isto é, que permita ao usuário utilizá-la em um desktop e em um
      smartphone. Esses requisitos não funcionais podem ter um detalhamento técnico mais específico, como: o sistema
      deve se comunicar obrigatoriamente com o SGBD MySQL; a solução desenvolvida tem que ser voltada para o sistema
      operacional Linux; a consulta de novos clientes deve permitir que seja efetuada off-line, entre diversos outros
      requisitos não funcionais, os quais podem ocorrer nas atividades de desenvolvimento de software.

    Mas, enfim, o que é qualidade [#]?

    Diz respeito aos métodos, às ferramentas, às metodologias e aos processos os quais garantirão que determinada
    entrega seja feita dentro dos padrões de qualidade estabelecidos entre as partes. Todo_ esse processo se inicia no
    levantamento de requisitos, quando o cliente passa para a equipe de desenvolvimento todas as suas necessidades.

    ---------------------------------------------------- IMAGEM 2.1 ----------------------------------------------------
    Levantamento de requisitos [#]

     Requisitos funcionais: refletem a visão do usuário quanto ao funcionamento de determinada função dentro do
      software.
     Requisitos não funcionais: refletem a visão do desenvolvedor. A partir deles são determinados tanto o
      funcionamento técnico das funcionalidades quanto os mecanismos e os desempenhos esperados.

    Compreender os requisitos permite entender de que forma os aspectos relacionados à qualidade de software estão
    intimamente ligados com os processos de desenvolvimento. Para Pressman (2006), o ciclo de desenvolvimento de um
    software [#] é dividido em seis partes, conforme pode ser observado na Figura 2.1.

    Figura 2.1 | Ciclo de desenvolvimento de software

    Em todo_ o ciclo de vida do projeto, podem ser utilizadas as ferramentas de garantia da qualidade, ou seja, nos
    processos de desenvolvimento, teste, validações, correções, enfim, em qualquer parte que venha a compor um projeto
    de desenvolvimento. É importante lembrar também que essas metodologias de garantia da qualidade necessitam de
    parâmetros, de métricas, que podem variar conforme métodos, necessidades, recursos, etc.

    Ainda segundo o autor, o termo qualidade de software [#] pode ser definido como o atendimento das conformidades
    funcionais com um desempenho esperado pelo patrocinador. Porém, para Sommerville (2011), a qualidade nas atividades
    de desenvolvimento de software [#] deve ser mais abrangente, devendo ser gerenciada e compreendida em três níveis:

    Organizacional: a preocupação é de um nível mais amplo, no qual o objetivo é o estabelecimento de padrões de
    trabalho de desenvolvimento de software. Esses frameworks devem agrupar as melhores práticas para que os erros e
    falhas sejam minimizados.

    Projeto: envolve o desenvolvimento com base em padrões determinados por gestores de projetos. Isso pode variar
    conforme o projeto, a política da empresa, a utilização de frameworks, entre outras peculiaridades.

    Planejamento: deve haver um plano de qualidade, ou seja, parte da equipe deve ficar responsável pela verificação dos
    requisitos de qualidade acordados entre as partes. Tanto os processos quanto os produtos desenvolvidos devem ser
    revisitados afim de se evitar que algo passe despercebido.

    Caro aluno, para especificar de maneira mais clara alguns aspectos que podem impactar diretamente no quesito
    qualidade [#], observe de que formas eles podem se apresentar.

    FALHAS DE SOFTWARE
    Segundo Zanin et al. (2018) [#], a falha de software pode ser um comportamento inesperado do sistema e pode ser
    ocasionado por um ou mais erros. Para melhor compreensão de como a falha de software pode afetar um sistema, observe
    a Figura 2.2.

    ---------------------------------------------------- IMAGEM 2.2 ----------------------------------------------------

    Nesse exemplo, acima do aceite, o sistema retorna uma mensagem de erro, impedindo, assim, que um novo cliente seja
    cadastrado, pois a falta da confirmação do aceite que impede a finalização do processo. Isso, a nível de usuário, é
    bem impactante. Imagine que esse sistema seja de uma loja de departamentos, a qual depende desse sistema para gerar
    as vendas e as notas fiscais. Certamente o prejuízo seria muito grande e preocupante.

    Vale aqui ressaltar que o desenvolvedor [#] é o responsável pela implementação das rotinas que cuidam das tratativas
    para falhas e erros. Elas podem ser exibidas por meio de uma mensagem ao usuário, podem levar a uma página nova com
    alguma imagem que remeta a falhas e erros ou podem, ainda, utilizar um report para enviar os problemas a algum
    repositório, com o intuito de que os desenvolvedores ajustem o sistema.

    ERROS DE SOFTWARE
    Segundo Zanin et al. (2018), [#] grande parte dos erros de software estão relacionados a execuções incorretas, o que
    faz com que os resultados gerados não reflitam a verdade. Um exemplo pode ser observado na Figura 2.3.

    ---------------------------------------------------- IMAGEM 2.3 ----------------------------------------------------

    Observe, nesse exemplo, a data do sistema e a data marcada no relógio. O erro de data no sistema pode ter um impacto
    muito grande na integridade dos seus dados, fazendo com que os lançamentos não sejam confiáveis quanto a sua data.
    Isso para setores de venda, logísticos, contábeis e fiscais pode ser desastroso.

    DEFEITO DE SOFTWARE
    Segundo Zanin et al. (2018), [#] o defeito de software se refere a uma implementação incorreta, que ocasiona um erro
    , uma interrupção de serviço ou, ainda, um mal funcionamento. Um exemplo pode ser um sistema de cadastro que, após o
    preenchimento de todos os campos obrigatórios, executa o processo de inserção de dados, não retorna erros, porém não
    faz a inserção das informações no banco de dados.

    Quanto às atividades de desenvolvimento, os defeitos são mais difíceis de se encontrar, pois, em alguns casos, erros
    de lógica, de falha de escrita do código ou de qualquer outra referência não retornam para auxiliar o desenvolvedor
    a encontrar o problema.

    BUGS
    Esse termo se popularizou entre os jovens para fazer referência a comportamentos inesperados de softwares. Segundo
    Zanin et al. (2018), [#] um bug de sistema diz respeito a erros e falhas inesperados, que normalmente são de maiores
    complexidades e demandam mais tempo e conhecimento técnico para que sejam encontrados e solucionados.

    EXEMPLIFICANDO
    Um bug que tirou o sono de muitos administradores de sistemas foi o bug do milênio. Em 1999, os profissionais
    estavam preocupados com o comportamento dos sistemas na virada de ano, porque os sistemas antigos faziam a leitura
    apenas dos dois últimos dígitos do ano. Com isso, em vez de o sistema ir para o ano 2000, poderia voltar para o
    1900. Por isso o nome Bug do Milênio. Esse acontecimento foi veiculado em muitos meios de comunicação, como no site
    G1: SANDERS, N. Há 20 anos, o ‘bug do milênio’ e o fim do mundo que não aconteceu. G1, São Paulo, 31 dez. 2019.

    Caro aluno, agora que você compreendeu como a qualidade de software está profundamente relacionada com os processos
    de desenvolvimento computacionais, certamente virá aquela dúvida clássica: mas de que forma podemos garantir a
    qualidade de um software? Para que você possa compreender os aspectos relacionados à garantia da qualidade dos
    softwares, neste momento, procure ter uma visão além das funcionalidades, do desempenho, da escalabilidade, etc.
    Assim, pode-se incluir a qualidade dos processos para desenvolvê-los, testá-los e liberá-los para utilização.

    GARANTIA DA QUALIDADE

    Sommerville (2011) [#] mostra que a garantia da qualidade é conhecida como Software Quality Assurance (SQA). A sua
    abrangência se estende por todo_ o ciclo de vida do projeto de desenvolvimento de software e deve:

     Possuir ferramentas e/ou métodos que permitam a análise dos desenvolvimentos e dos testes.
     Efetuar revisões técnicas nos componentes e na funcionalidade, devendo ser feitas em cada uma das fases.
     Controlar a documentação por meio de versionamento.
     Atribuir métodos para se garantir padrões de desenvolvimento e das boas práticas, as quais atendem as necessidades
      das equipes de desenvolvimento.
     Obter mecanismos de aferição.

    Para Pressman (2006), a garantia da qualidade [#] diz respeito aos procedimentos, métodos e ferramentas utilizados
    por profissionais de Tecnologia da Informação para se garantir padrões acordados entre as partes durante todo_ o
    ciclo de vida do desenvolvimento de um software. É importante lembrar que os padrões de qualidade podem variar
    conforme o projeto e, por isso, a garantia da qualidade deve ser guiada pelo que foi acordado entre as partes.

    Com o intuito de que você possa compreender melhor como a garantia da qualidade é, de fato, operacionalizada em
    atividades de desenvolvimento em um meio profissional, vamos analisar um caso. Imagine que foi solicitado por um
    escritório de advocacia um programa para gerenciar os processos advocatícios. Em primeiro lugar, foi dito que tanto
    os advogados quanto os clientes deverão fazer login no sistema por um único local e de forma transparente. Tempos
    depois foi apresentada a tela de login ao cliente, conforme pode ser observado na Figura 2.4.

    ---------------------------------------------------- IMAGEM 2.4 ----------------------------------------------------

    Repare que o acordo entre as partes era o login transparente. Dessa forma, o menu dropdown para escolher o tipo do
    usuário não deveria ter sido utilizado na tela. A garantia da qualidade deve utilizar as ferramentas para detectar o
    problema, pois esse ajuste tem um impacto tanto no desenvolvimento do front-end quanto no do back-end, porque a
    lógica para se efetuar um login no sistema muda completamente.

    Caro aluno, certamente você deve estar pensando que, para determinar se algo está atendendo à qualidade, deve haver
    métricas. Pois bem, em qualidade de software também existem regras definidas, que fornecem formas de avaliar se os
    processos e produtos estão dentro da qualidade acordada entre as partes.

    Segundo Zanin et al. (2018), as diversas engenharias utilizam o processo de medição, para verificar se determinado
    desenvolvimento está em conformidade e segurança para ser utilizado. Porém, diferentemente das demais áreas de
    conhecimento, a engenharia de software não utiliza leis quantitativas ou medidas absolutas, mas um conjunto de
    medidas que dão um feedback quanto aos aspectos qualitativos do software.

    Boehn, Brown e Lipow (1977) determinam que, para efetuar a medição da qualidade de um software [#], deve-se
    determinar quais são as funcionalidades que devem/podem ser medidas e de que forma precisam ser medidas. A fim de
    orientar os desenvolvedores no alinhamento das métricas, os autores sugerem o esquema demonstrado na Figura 2.5.

    ---------------------------------------------------- IMAGEM 2.5 ----------------------------------------------------

    [#] Em sua estrutura mais alta, o software deve possuir elementos como usabilidade e manutenibilidade. E, em sua
    estrutura média, a portabilidade, a confiabilidade, a eficiência, a engenharia humana, a facilidade de teste, a
    facilidade de entendimento e a facilidade de modificação. Dessa estrutura média, derivam as primitivas (que dão as
    características dos elementos de nível médio). As primitivas podem ser verificadas por meio de checklists, ou seja,
    representam a atividade de desenvolvimento em si, que deve ser verificada quanto ao atendimento da garantia da
    qualidade. [#]

    Você deve ter percebido que essa ferramenta é bem complexa, mas observe como ela auxilia na atividade de encontrar
    problemas relacionados à qualidade de software. Para isso, observe a Figura 2.6.

    ---------------------------------------------------- IMAGEM 2.6 ----------------------------------------------------

    Nesse exemplo, o sistema de cadastro está com a funcionalidade de adicionar um novo usuário e exibir os cadastrados
    no sistema. Do lado esquerdo é apresentada a exibição desse sistema em navegador de desktop, já do lado direito está
    a apresentação em um smartphone. Com isso, vamos utilizar a árvore de qualidade de software apresentada na Figura
    2.5 para analisar esse cenário.

    No primeiro caminho: Utilidade geral -> Portabilidade -> Independente do dispositivo, já se observa que o software
    apresenta um problema de responsividade, o que demonstra que o sistema não é portável.

    Outro exemplo em que a qualidade é atendida pode ser verificado no caminho: Utilidade Geral -> Usabilidade ->
    Confiabilidade -> Precisão. Isso ocorre, pois, quando uma transação de inserção de dados é feita, a operação se
    completa corretamente.

    ASSIMILE
    Checklist [#] é uma ferramenta de grande importância para profissionais de desenvolvimento. Existem softwares que
    auxiliam o desenvolvedor nessas tarefas. Neles é possível detalhar as atividades do checklist, determinar a
    quantidade de tempo e ajustar as atividades predecessoras e sucessoras.

    Caro aluno, você percebeu como os processos de qualidade de software são de extrema importância para os
    desenvolvimentos? Com esses estudos, foi possível compreender que, ao se utilizar as técnicas e ferramentas de forma
    adequada, serão alcançados alguns benefícios. E quais são esses benefícios encontrados nos processos de qualidade de
    software?

    Segundo Sommerville (2011), as vantagens encontradas ao se operacionalizarem os processos de garantia da qualidade
    dependem de um esforço coletivo, que proporciona a economia de recursos durante todo_ o ciclo de vida do projeto de
    desenvolvimento de software. Ainda que de maneira bem específica, os processos de qualidade podem proporcionar
    algumas vantagens [#], listadas a seguir:

     Padronização: boas práticas passam a ser adotadas pelas equipes de desenvolvimento.

     Aumento de produtividade: ao se minimizar os retrabalhos por meio da verificação da qualidade, o tempo de
      produtividade é otimizado.

     Satisfação do cliente: com as ferramentas de verificação da qualidade, a equipe de desenvolvimento realiza as
      atividades de forma mais assertiva.

     Economia de recursos: redução nos custos operacionais como um todo_, sendo observados pontos como: tempo, custo
      com colaborador, custos gerais de operação.

     Retrabalho: evita que grandes correções e ajustes sejam necessários, fazendo com que muitas vezes as atividades
      com dependências funcionais necessitem ser paralisadas.

    Muitas vezes as vantagens obtidas com a aplicação dos recursos de qualidade nas atividades de desenvolvimento de
    software demoram a serem sentidas no dia a dia, uma vez que isso ocorre conforme a utilização das ferramentas
    aplicadas torna-se uma prática comum e corriqueira. A partir desse ponto é que, naturalmente, as vantagens começam a
    fazer parte de todo_ o ciclo de vida do desenvolvimento de um software.

    REFLITA
    Dentro das atividades de desenvolvimento de software existem diversos profissionais de diferentes áreas que devem
    conversar entre si, entre eles há: designers, programadores e DBA (Database Administrator). O bom diálogo entre eles
    é de extrema importância para que a integração ocorra de forma a atender as necessidades do sistema e com a
    qualidade desejada. Caso os diferentes integrantes não tivessem uma proximidade, quais das vantagens em se utilizar
    os processos de qualidade de software poderiam ser prejudicadas?

    SAIBA MAIS
    A Sociedade Brasileira de Computação é uma entidade que visa, por meio de eventos, promover o conhecimento através
    de debates e fóruns. Anualmente ocorre um simpósio totalmente voltado às discussões acerca de qualidade de software.

    Caro aluno, os conceitos de qualidade de software estão intrinsecamente ligados às ferramentas, aos métodos e às
    medições, que guiam a equipe de desenvolvimento de forma mais assertiva. Com isso, torna-se muito importante que o
    profissional de Tecnologia da Informação, o qual tem, em sua área de atuação, o desenvolvimento de software,
    compreenda as características técnicas ligadas à qualidade, a suas falhas e a como conseguir a garantia de qualidade
    nos processos de desenvolvimento durante o ciclo de vida do projeto. Dessa forma, podem-se proporcionar vantagens
    relevantes aos processos de desenvolvimento de software, que são convertidas em aumento de satisfação do cliente.

    PESQUISE MAIS
    A UNIVESP disponibiliza uma sequência de aulas sobre qualidade de software, sendo muito interessante como material
    complementar, uma vez que são discutidos novos exemplos, os quais abrangem os conhecimentos com os casos em que as
    ferramentas da qualidade de software podem ser aplicadas.

    Confira o vídeo Gerência e Qualidade de Software – Apresentação da Disciplina, disponível no YouTube.

    GERÊNCIA e Qualidade de Software – Apresentação da disciplina. [S.l.: s.n], 2018. 1 vídeo (2 min). Publicado pelo
    canal UNIVESP.

    Contribuição dos modelos de qualidade e maturidade na melhoria dos processos de software (TONINI; CARVALHO; SPINOLA,
    2008). O artigo intitulado traz uma interessante discussão sobre a implementação de modelos de qualidade e de
    maturidade com base em um estudo de casos múltiplos. Essa análise proposta no artigo engloba três níveis:
    desenvolvedores, grupos/equipes e organizacional. Vale a pena conferir!

    TONINI, A. C.; CARVALHO, M. M.; SPINOLA, M. M. Contribuição dos modelos de qualidade e maturidade na melhoria dos
    processos de software. Produção, v. 18, n. 2, p. 275-286, 2008.

    #ref Unidade 2 - Seção 1
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
     BOEHN, B. W.; BROWNN, J. R.; LIPOW, M. Characteristics of Software Quality. [S.l.: s.n.], 1977.

     GERÊNCIA e Qualidade de Software – Apresentação da disciplina. [S.l.: s.n], 2018. 1 vídeo (2 min). Publicado pelo
    canal UNIVESP. Disponível em: https://bit.ly/38hgONe. Acesso em: 25 set. 2020.

     PRESSMAN, R. S. Engenharia de Software. 6. ed. São Paulo: McGraw-Hill, 2006.

     SANDERS, N. Há 20 anos, o ‘bug do milênio’ e o fim do mundo que não aconteceu. G1, São Paulo, 31 dez. 2019.
    Disponível em: https://glo.bo/3bhqaum. Acesso em: 19 out. 2020.

     SOMMERVILLE, I. Engenharia de Software. 9. ed. São Paulo: Pearson Prentice Hall, 2011.

     TONINI, A. C.; CARVALHO, M. M.; SPINOLA, M. M. Contribuição dos modelos de qualidade e maturidade na melhoria dos
    processos de software. Produção, v. 18, n. 2, p. 275-286, 2008. Disponível em: https://bit.ly/2XdqC4L. Aceso em: 19
    out. 2020.

     ZANIN, A. et al. Qualidade de Software. Porto Alegre: Sagah, 2018.
    """


def unidade2_secao2():
    """
    ----------------------------------------------- UNIDADE 2 / SEÇÃO 2 -----------------------------------------------
    QUALIDADE DE PRODUTO - Sergio Eduardo Nunes

    CONCEITO-CHAVE
    Caro aluno, você já deve ter baixado algum aplicativo em seu smartphone que prometia fazer determinada função, porém
    ao utilizá-lo, sua operacionalização era tão complicada que o resultado gerado não chegava nem perto do prometido.
    Ou seja, o produto final do desenvolvedor do app estava longe da qualidade prometida na descrição disponível na loja
    de aplicativos. A área da Engenharia de Software que trata desses assuntos é conhecida por qualidade de produto de
    software.

    Certamente, quando nos referenciamos ao software como um produto, para alguns profissionais pode soar um pouco
    estranho. Porém, os assuntos relacionados à qualidade de produtos possuem uma grande abrangência, perpassando
    discussões como: os modelos de qualidade, as normas ISO de qualidade, a gestão da qualidade do produto, as medições,
    os requisitos e as avaliações da qualidade. Assim, devido à complexidade apresentada, tais conceitos serão
    exemplificados.

    Segundo Mello (2010), ao contrário dos produtos manufaturados, o desenvolvimento de softwares é projetado. Os
    processos de desenvolvimento são criativos e técnicos e exigem que os profissionais da área apresentem competências
    e habilidades para executar suas funções. Já a produção de produtos manufaturados, em sua grande maioria, possui
    processos produtivos mecanizados, que ocorrem conforme a automação projetada pelo engenheiro. A seguir, conforme
    Mello (2010), é exemplificada a diferença em termos práticos [#]:

     Setor de manufatura: são necessárias matérias-primas, processos de transformação para elas, embalagens,
      acondicionamento e transporte. E seu sistema produtivo pode ter diversos níveis de complexidade. Exemplo: uma
      padaria especializada em bolos possui determinadas matérias-primas envolvidas em seus processos produtivos e bolos
      com diferentes níveis de complexidade. Já uma empresa farmacêutica tem as características de seu setor produtivo
      construídas a partir de seus diversos insumos e níveis de processos.

     Setor de desenvolvimento: em grande parte dos desenvolvimentos, em termos de recursos computacionais, são
      necessários: computadores, acesso à internet e programas. Porém, para o bom aproveitamento dos recursos, grande
      parte do projeto vai depender das habilidades, competências e da criatividade dos profissionais que utilizam o
      desenvolvimento de software para a busca de soluções em diversas áreas do conhecimento.

    Você percebeu o quanto é complexo garantir a qualidade do produto de software? Pois bem, para tal existem algumas
    ferramentas, conhecidas como modelos de qualidade de produto [#], onde podem ser avaliado o produto de software.
    Normas foram padronizadas internacionalmente a fim de garantir que, independentemente do local onde se esteja
    desenvolvendo um software, algumas premissas sejam seguidas.

    ISO 9126 (NBR 13596)
    De acordo com Wazlawick (2013), a ISO 9126 (NBR 13596) é a norma que visa avaliar a qualidade, as características e
    os atributos da qualidade de software. Além disso, a norma tem como objetivo a padronização das atividades e da
    forma de se avaliar a qualidade do produto, a fim de se gerar feedbacks importantes para a equipe de desenvolvimento
    de software. A estrutura da norma ISO 9126 é feita em quatro partes, conforme pode ser observado a seguir: [#]

     ISO 9126-1 de 2001: trata das características, subcaracterísticas e métricas da qualidade de produto de software
      (tema desta seção).
     ISO 9126-2 de 2003: trata das métricas externas e do controle de falhas.
     ISO 9126-3 de 2003: o seu objetivo é verificar a quantidade de ocorrências de falhas e estimar o tempo de
      recuperação.
     ISO 9126-4 de 2004: faz as tratativas de User Experience, produtividade, eficácia e segurança.

    Embora o foco da seção seja a ISO 9126-1, é inevitável que processos de outras ISO não sejam mencionados,
    conceituados e exemplificados. Isso porque, em termos práticos, as normas são complementares dentro de um projeto de
    desenvolvimento de software.

    Ainda conforme Wazlawick (2013), define-se que a ISO 9126 faz parte da família de normas de qualidade 9000. O foco
    dela é a qualidade de produto de software. No Brasil a NBR 13596 é equivalente à ISO, porém houve uma substituição
    da NBR pela ISO/IEC 9126-1. A norma constante na ISO 9126 é composta por características, subcaracterísticas e
    métricas. As seis características podem ser observadas na Figura 2.7.

    CARACTERÍSTICAS E SUBCARACTERÍSTICAS DA ISO 9126 [#]
    Para melhor compreensão das características e subcaracterísticas da ISO 9126, a seguir vamos ver o detalhamento de
    cada uma delas segundo Wazlawick (2013).

    -> Funcionalidade: [#] Descreve os atributos das funções contidas nos softwares. Possui as subcaracterísticas:

     Adequação: diz respeito ao alinhamento do funcionamento correto da funcionalidade.
     Acurácia: preocupa-se com as saídas geradas pelo software, que têm de estar de acordo com as necessidades.
     Interoperabilidade: denota a capacidade do software de poder ser utilizado por tecnologias diferentes.
     Conformidade: deve estar de acordo com normas, regras e leis específicas.
     Segurança de acesso: capacidade de evitar intrusões e incidentes relacionados à segurança da informação.

    Para que você compreenda a forma de identificar as funcionalidades dentro de um projeto, analise a seguinte
    situação: uma empresa precisa de um chat para que os colaboradores se comuniquem dentro da rede local, porém existe
    a necessidade de se utilizar o protocolo IP nas duas versões: IPv4 e IPv6. Conforme pode ser observado, a
    funcionalidade de comunicação interna possui características de grande relevância quanto à adequação e à
    interoperabilidade. Ainda de acordo com Wazlawick (2013):

    -> Confiabilidade: [#] É a capacidade do software de se manter em funcionamento e com o desempenho esperado/
       estabelecido. Observe as subcaracterísticas:

     Maturidade: demonstra a frequência com que ocorrem as falhas de software.

     Tolerância a falhas: preocupa-se em verificar, na ocorrência de falhas ou em incidentes relacionados à segurança
      (falha provocada ou por violação), quais serviços permanecerão acessíveis e com a garantia da integridade.

     Recuperabilidade: trata-se do tempo em que, após a ocorrência de determinada falha, a funcionalidade ou sistema
      estará disponível novamente.

    Os aspectos relacionados à confiabilidade estão mais presentes em nossas atividades cotidianas, sendo, portanto,
    mais fácil de identificá-las. Por exemplo: quando os aplicativos de stream utilizados em smart TVs foram projetados,
    tornou-se necessário conhecer a sua confiabilidade, o que se deu a partir de questionamentos do tipo: em caso de
    falha, o filme, ou a série, será interrompido? Se caso ocorrerem, quais serão essas falhas? Qual o tempo para o
    sistema se reestabelecer?

    -> Usabilidade: [#] Trata-se de uma forma de aferir o nível de experiência do usuário (User Experience) quanto à
       facilidade de operacionalizar o software. As subcaracterísticas podem ser observadas a seguir:

     Inteligibilidade: está relacionada com a lógica de sua aplicabilidade ser intuitiva e de fácil operação.

     Apreensibilidade: afere o quanto o usuário se esforçou para aprender a utilizar uma funcionalidade ou o software
      como um todo_.

     Atratividade: observa o quanto as interfaces do software despertam a atenção do usuário.

    A usabilidade a nível de usuário é uma das características que requer mais atenção. É muito comum alguns usuários
    instalarem softwares de edição de vídeo e, devido à complexidade para fazer os tratamentos, acabarem por desistir e
    buscar uma solução para smartphone. Isso está totalmente relacionado às características de usabilidade do software.
    Continuando com o que explica Wazlawick (2013):

    -> Eficiência: [#] Refere-se à forma como o software irá se comportar dentro dos parâmetros estabelecidos no projeto
       . Suas subcaracterísticas são:

     Tempo: preocupa-se em medir o tempo de resposta de uma funcionalidade ou ainda a latência e/ou jitter.

     Recursos: trata-se de uma forma de aferir o quanto os recursos são utilizados ao se fazer uso de determinada
      funcionalidade ou do software como um todo_.

    -> Manutenibilidade: [#] A preocupação, nessa característica, está na capacidade de modificação, que é possível nos
       seguintes casos: excluir defeitos e falhas, adicionar novas funcionalidades, adaptar a novas plataformas ou a
       sistemas operacionais, etc. As subcaracterísticas estão apresentadas a seguir:

     Modificabilidade: trata da capacidade de modificar o software por algum motivo ou necessidade.

     Estabilidade: preocupa-se em verificar se algumas falhas ocorrerão após as modificações.

     Escalabilidade: faz a aferição da capacidade de crescimento do software a fim de se atender uma demanda maior.

    A manutenção dos softwares é algo que preocupa gerentes de projetos, pois a falha na projeção das subcaracterísticas
    impacta diretamente a qualidade dos serviços.

    Portabilidade
    Em 2020, o governo federal efetuou ajuda financeira à população por meio de um benefício (devido à alta taxa de
    desemprego causada pela pandemia do novo coronavírus). Porém, para ter acesso a esse benefício, era necessário fazer
    a instalação de um aplicativo no smartphone. Ocorre que o aplicativo não havia sido projetado para atender uma
    parcela tão grande da população e, dessa forma, seu funcionamento ficou muito comprometido. Segundo Wazlawick (2013)
    , a portabilidade torna-se um ponto de grande relevância, com a advento dos dispositivos móveis, e suas
    características podem ser observadas a seguir. A portabilidade [#] diz respeito a um conjunto de características que
    demonstra a capacidade do software ser utilizado em outros sistemas, dispositivos e plataformas.

     Adaptabilidade: capacidade de se adaptar a ambientes nos quais não foram projetados.

     Analisabilidade: deve-se analisar os impactos positivos e negativos que a utilização do software em outros meios
      pode ocasionar.

     Interoperabilidade: demonstra a capacidade de interação com outros sistemas, muitas vezes desenvolvidos com outras
      tecnologias e arquiteturas.

    Um exemplo clássico e muito atual da portabilidade ocorreu quando os dispositivos do tipo smartphone se
    popularizaram. Os sites, até então, estavam projetados para serem exibidos em monitores com um tamanho muito maior
    do que a tela de um smartphone. Isso fez com que os sites tivessem um comportamento muito estranho nesses
    dispositivos, ou seja, eles não estavam preparados para a portabilidade.

    ASSIMILE
    Com a popularização dos dispositivos móveis a característica portabilidade, existente na norma ISO 9126, tornou-se
    mais que uma necessidade, veio a ser uma obrigação. Para isso, algumas linguagens de programação/marcação possuem
    frameworks que fazem tratativas quanto à responsividade das aplicações. Um exemplo de linguagem de marcação que
    provê essa portabilidade é o Bootstrap. Como não existe um site oficial com versão em português para o Bootstrap,
    utilize o tradutor do navegador ao visitar o site W3Schools. BOOTSTRAP 3 Tutorial. W3Schools, [S.l., s.d.].

    CONJUNTO DE MÉTRICAS
    Caro aluno, caso você não se recorde, no início desta seção, foi dito que a ISO 9126 é composta por características,
    subcaracterísticas e métricas. De acordo com Wazlawick (2013), [#] a análise das características e das consequentes
    subcaracterísticas só é possível por meio das métricas, que equalizarão o desenvolvimento. A sua estrutura possui
    três fases [#] e pode, ainda, ser aplicada em qualquer momento no ciclo de vida do projeto. Observe o conjunto de
    métricas:

    Definição dos requisitos de qualidade [#]

    É a definição das características e subcaracterísticas por parte do cliente. Com isso, é possível definir quais
    serão as métricas utilizadas para a avaliação do produto. Para exemplificar, imagine que uma equipe seja contratada
    para organizar um campeonato de Counter Strike. O requisito é que a rede suporte vinte e cinco jogadores em cada
    time (cinquenta ao todo_) e uma latência abaixo de 0,350 ms. Ou seja, na contratação foi definido, segundo uma
    quantidade de jogadores, a latência esperada para se atender a qualidade, por meio da métrica de 0,350 ms.

    Preparação da avaliação [#]

    Nesse momento devem ser estabelecidos os critérios de avaliação, que podem ser numéricos (com escala de 0 a 10) ou,
    ainda, como orienta a norma: insatisfatório, razoável, bom e excelente. A avaliação pode ser aplicada nas
    funcionalidades desenvolvidas, mostrando-se como uma alternativa mais eficiente para aplicação no projeto como um
    todo_. Para exemplificar a preparação da avaliação, imagine que se tenha um sistema de venda em que o usuário
    adicione os produtos no carrinho de compras, escolha a forma de pagamento, o local de entrega e encerre o pedido.
    Quanto à experiência do usuário ao utilizar a funcionalidade de compra, foi elaborado o Quadro 2.1, como demonstrado
    a seguir.

    ---------------------------------------------------- QUADRO 2.1 ----------------------------------------------------

    A preparação permite a reflexão sobre os pontos necessários e importantes que devem ser medidos. Além disso, os
    feedbacks gerados possibilitam verificar se as métricas adotadas para a avaliação dos componentes e funcionalidades
    estão adequadas.

    Avaliação: [#] Trata-se do momento em que os sistemas de avaliação das funcionalidades serão aplicados para
    posterior análise e aplicação de medidas corretivas.

     Medida: são aquelas métricas definidas na preparação da avaliação. É possível, ainda nesse momento, verificar se
      as métricas estão adequadas (validação).

     Pontuação: verificar se o sistema de pontuação se adéqua a uma forma de avaliação justa.

    Percebeu como a aplicação da norma propriamente dita é simples? Ela ainda é tida pelos desenvolvedores como flexível
    e de simples adaptação para qualquer tipo de projeto de desenvolvimento. Sua metodologia é bem definida, fazendo com
    que os procedimentos sejam fáceis de serem implementados nos desenvolvimentos de software. Para melhor compreensão
    dos passos a serem seguidos no processo como um todo_, observe o diagrama representado na Figura 2.8.

    ---------------------------------------------------- IMAGEM 2.8 ----------------------------------------------------

    Vale lembrar que o modelo de processo de avaliação descrito, bem como as tratativas em relação às métricas aqui
    discutidas, refere-se à ISO 9126.

    EXEMPLIFICANDO
    Neste momento você deve estar apreensivo devido à quantidade de pontos que devem ser observados para se utilizar os
    modelos de qualidade de produto de software, não é? Então, imagine que você precise colocar em prática, na empresa
    em que você trabalha, a ISO 9126. Certamente virá a dúvida: por onde começar?

    A equipe deve elaborar um documento (o formato dele pode variar conforme a empresa, não existe um template), no qual
    o objeto a ser avaliado é pontuado dentro de todas as suas características e subcaracterísticas. Por exemplo: a
    equipe de desenvolvimento fez uma tela de Fale Conosco. Nesse tipo de página, normalmente há contatos, localização,
    textos informativos e uma área para se mandar uma mensagem. A equipe deve utilizar todos os pontos da ISO 9126 para
    avaliar cada uma das características e subcaracterísticas presentes. Isso pode ser organizado textualmente em
    quadros, tabelas, formulários, etc.

    ISO 9000
    Pois bem, você percebeu que os métodos aqui discutidos são todos apoiados em normas. Grande parte dos sistemas de
    gestão de qualidade são baseados nas normas ISO 9000:2015 (ABNT, 2015), que têm como função: [#]

     Descrever os fundamentos e princípios da gestão da qualidade.
     Compreender os processos de implementação da gestão da qualidade.
     Avaliar a conformidade dos produtos de software desenvolvido.

    Segundo Carpinetti e Gerolamo (2019), a ISO 9000 segue oito princípios de gestão da qualidade, [#] os quais têm como
    objetivo conduzir os gestores na melhoria de desempenho, principalmente em atividades relacionadas a desenvolvimento
    de software. Observe a seguir a descrição desses princípios:

     Foco no cliente: uma abordagem por meio da qual se buscam melhores práticas, a fim de entregar o melhor produto.
     Liderança: metodologia e abordagens como forma de liderar.
     Pessoas: utilizar formas de as pessoas se comprometerem com os processos e com a qualidade.
     Processos: verificar constantemente os processos e repensá-los.
     Inter-relacionamento: prover o inter-relacionamento de atividades concorrentes.
     Melhoria: buscar a melhoria contínua por meio de metodologias, normas e boas práticas.
     Decisão: utilizar os feedbacks gerados a favor da tomada de decisão.
     Benefícios: gerar vantagens administrativas e operacionais por meio da adoção de boas práticas.

    Para que você possa compreender como os princípios da ISO 9000 estão relacionados às atividades de desenvolvimento
    no mercado de trabalho, observe o exemplo descrito a seguir. Imagine que se tenham “ilhas” de desenvolvimento dentro
    de uma organização, o que faz com que os times sejam separados por conhecimento e habilidades. Porém, há um momento
    dentro do projeto em que as funcionalidades desenvolvidas precisam ser integradas para que o sistema de fato passe a
    existir. Como fazer isso?

    A ISO 9000 possui tratativas para esses fins. Observe o quanto a norma pode auxiliar nesse exemplo e o quanto trará
    impactos positivos aos profissionais. A norma apresenta guias quanto à abordagem a ser realizada com a equipe,
    quanto à liderança que orienta a forma de se garantir a integração das funcionalidades e, sob um aspecto diferente,
    quanto a um olhar que mapeia os processos a fim de propor melhorias e ajustes. Isso permite um planejamento mais
    adequado e gera benefícios a curto e longo prazo (conforme o aumento da maturidade).

    ISO 9001
    Para finalizar, vale a pena citar que a norma 9001:2015 faz uma abordagem com caráter de tarefas administrativas no
    tocante ao sistema de gestão da qualidade (SGQ). Segundo o catálogo da ISO 9001:2015 (ABNT, 2015), seus objetivos
    [#] são:

     Fazer o controle documental.
     Efetuar o controle de registro da qualidade.
     Normatizar a auditoria interna.
     Fazer o controle de produtos que não atendam às conformidades.
     Prover ações corretivas.
     Prover ações preventivas.

    EXEMPLIFICANDO
    O controle documental é uma preocupação tanto de gerentes de projetos quanto de desenvolvedores. Imagine que, após
    escrever uma funcionalidade de modos de pagamento para compra de passagens aéreas, um outro desenvolvedor subscreva
    a sua versão no sistema. Todo_ o seu trabalho estará perdido. Para isso, a ISO 9001:2015 possui algumas tratativas
    que podem ser facilmente alinhadas por meio de sistemas de versionamento de códigos. Uma das aplicações web para
    versionamento que mais se popularizou entre desenvolvedores foi o GitHub.

    A ISO da família 9000 é de grande importância para as atividades relacionadas ao desenvolvimento de softwares.
    Compreender a sua trajetória evolutiva é muito interessante para entender como as novas necessidades foram moldando
    a estrutura que utilizamos hoje em dia. No site da ABNT, é possível ir acessando os links para verificar essa
    evolução histórica. Observe a ISO 9000:2000 a seguir.

    Caro aluno, ao longo das discussões levantadas nesta seção, você pôde perceber como as normas são um ótimo guia para
    as atividades de desenvolvimento de software, não é mesmo? Para alguns profissionais, o uso dessas ferramentas
    parece ter o intuito de agregar mais uma atividade além daquelas que precisam ser executadas dentro de um projeto.
    Mas o objetivo é, na verdade, o oposto. A intenção é que, pela utilização das normas, as atividades sejam executadas
    de forma mais assertiva, fazendo com que menos processos e atividades de desenvolvimento precisem ser revisitadas.

    REFLITA
    Os projetos de desenvolvimento de software são compostos por atividades extremamente importantes, e as normas visam
    ser um balizador dos processos que devem ser seguidos para atingir determinados objetivos. Como observado, as normas
    ISO 9126, ISO 9000, ISO 9001, entre outras, são direcionadoras de qualidade para o produto de software. Porém,
    faz-se realmente necessário utilizar todos os seus apontamentos? Mesmo que eles engessem a sua operacionalização nos
    projetos.

    #ref Unidade 2 - Seção 2
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
     ABNT. NBR ISO 9000:2000: Sistemas de gestão da qualidade – Fundamentos e vocabulário. São Paulo: ABNT, 2000. 26p.
    Disponível em: https://bit.ly/3981W31. Acesso em: 3 out. 2020.

     ABNT. NBR ISO 9000:2000: Sistemas de gestão da qualidade – Fundamentos e vocabulário. São Paulo: ABNT, 2002. 26p.
    Disponível em: https://bit.ly/3nob6gS. Acesso em: 7 out. 2020.

     ABNT. NBR ISO 9000:2000: Sistemas de gestão da qualidade – Fundamentos e vocabulário. São Paulo: ABNT, 2005. 35p.
    Disponível em: https://bit.ly/3s2CuV8. Acesso em: 7 out. 2020.

     ABNT. NBR ISO 9000:2015: Sistemas de gestão da qualidade – Fundamentos e vocabulário. São Paulo: ABNT, 2015. 59p.
    Disponível em: https://bit.ly/2LrYbNT. Acesso em: 3 out. 2020.

     BOOTSTRAP 3 Tutorial. W3Schools, [S.l., s.d.]. Disponível em: https://bit.ly/2JVNBOM. Acesso em: 19 out. 2020.

     CARPINETTI, L. C. R.; GEROLAMO, M. C. Gestão da Qualidade ISO 9000:2015. São Paulo: Atlas, 2019.

     MELLO, C. H. P. Gestão da Qualidade. São Paulo: Pearson Education do Brasil, 2011.

     WAZLAWICK, R. S. Engenharia de software: conceitos e prática. Rio de Janeiro: Elsiever, 2013.
    """


def unidade2_secao3():
    """
    ----------------------------------------------- UNIDADE 2 / SEÇÃO 3 -----------------------------------------------
    QUALIDADE DE PROCESSO - Sergio Eduardo Nunes

    CONCEITO-CHAVE
    Caro aluno, quando você está utilizando o aplicativo para consultar sua área acadêmica, buscando informações como
    notas, dados pessoais, financeiros, entre outros, talvez não reflita sobre a quantidade de processos necessários
    para que se possa utilizar uma aplicação com confiabilidade, eficiência e segurança. Para isso, são utilizadas
    normas, métodos, ferramentas e metodologias que garantem a qualidade dos processos de software.

    Sommerville (2015) define que, nas atividades de desenvolvimento de software, são necessários processos como uma
    forma de se organizar, gerenciar e compreender a ordem em que as atividades são executadas. Com o intuito de que
    você compreenda melhor os processos, vamos tomar como exemplo um projeto de desenvolvimento da página Home de um
    site. Nesse exemplo poderiam ser observados os processos: design de layout, tratamento de imagens, responsividade,
    entre outros. Além disso, é possível notar que cada etapa do desenvolvimento pode ser orientada por uma norma a fim
    de que atinja os objetivos desejados.

    E por que a melhoria dos processos é importante para as atividades de desenvolvimento de software? Num primeiro
    momento pode parecer que a melhoria de processos só pode ser aplicada em atividades de linhas de produção, mas não é
    bem assim. Segundo Sommerville (2015), ao se utilizar ferramentas de qualidade de processo, a intenção é a de
    corrigir erros e falhas, padronizar atividades, alinhar o trabalho com a equipe de desenvolvimento, entre outros.
    Antes de se utilizar alguma metodologia de qualidade de processos, é necessário fazer o mapeamento deles.

    Sommerville (2015) [#] afirma que o mapeamento de processos é uma ferramenta gerencial que visa identificar a
    sequência na qual as atividades são executadas. Em termos práticos, o mapeamento pode gerar mais benefícios, como:

     Compreensão dos processos: permite entender todas as partes que os compõem.

     Análise dos processos: ao mapeá-los, é possível fazer uma reflexão sobre as atividades que os compõem.

     Melhoria dos processos: enxergando detalhadamente as atividades que os compõem, eles podem ser otimizados,
      ajustados ou substituídos, a fim de que sejam melhorados.

     Padronização dos processos: as atividades que possuem níveis de qualidade ajustados com as políticas da empresa
      dentro dos processos podem vir a se tornar padrão.

     Documentação dos processos: ao mapear as atividades que compõem os processos, é possível documentá-los, se assim a
      equipe não tiver feito nas atividades que precedem a fase de desenvolvimento do projeto. [#]

    Percebeu que antes de qualquer coisa, devem-se mapear os processos para que se compreendam detalhadamente todas as
    atividades de desenvolvimento? Até aqui tudo certo. Mas com que nível de detalhamento o mapeamento deve ser feito?
    Segundo Sommerville (2015), [#] existem três níveis de detalhamento dos processos, conforme pode ser observado:

     Nível 1 – Descritivo: por meio de uma descrição básica e abrangente dos processos, busca-se o alinhamento deles
      com as partes envolvidas no projeto de desenvolvimento.

     Nível 2 – Analítico: trata-se de uma fase técnica, na qual são detalhadas as atividades de desenvolvimentos,
      pontos de atenção e o tratamento de exceções.

     Nível 3 – Executável: é uma visão mais próxima aos dados, à aplicação em si. Aqui a intenção é detalhar as
      funcionalidades, os serviços e as saídas. [#]

    Com isso, após fazer o mapeamento dos processos, seja por meio de softwares, seja por meio de descrições (textos,
    tabelas ou quadros), pode-se utilizar ferramentas como: modelos, normas e metodologias, os quais compõem as formas
    que as equipes podem utilizar para garantir a qualidade de processos de desenvolvimento de software. Dentre essas
    ferramentas [#], abordaremos incialmente os Modelos de Maturidade CMM e CMMI.

    MODELOS DE MATURIDADE CMM E CMMI
    Caro aluno, as discussões acerca de qualidade de processos têm uma abrangência significativa, isso porque os
    processos de desenvolvimento podem ser vistos sob diversos aspectos. Para isso, inicialmente, você será conduzido às
    explanações acerca do grau de maturidade dos processos por meio de um modelo conhecido como CMM (Capability Maturity
    Model).

    ASSIMILE
    Os modelos de maturidade são ótimas ferramentas que permitem o conhecimento profundo dos processos, da equipe de
    desenvolvimento, das dificuldades, entre outros. Colocar tais metodologias em prática exige comprometimento e
    persistência, pois, em muitos casos, a resistência de colaboradores que nunca tiveram contato com as normas e
    diretrizes podem criar certo bloqueio em sua adoção.

    Segundo Couto (2007), o modelo CMM foi elaborado pelo Instituto de Engenharia de Software (conhecido por SEI –
    Software Engeneering Institute) da Universidade Carnegie Mellon, nos Estados Unidos da América. Para compreensão da
    linha do tempo do CMM, observe a Figura 2.13.

    --------------------------------------------------- IMAGEM 2.13 ---------------------------------------------------

    Antes de partirmos para a demonstração dos modelos de maturidade, vamos responder a uma indagação que você
    certamente está se fazendo: para que serve isso? Pois bem, imagine que um mesmo projeto é entregue para um grupo de
    programadores e para uma empresa de desenvolvimento de software. Ambos terão a mesma quantidade de profissionais,
    recursos computacionais e prazo. A partir disso, você pode imaginar que a entrega da empresa provavelmente será
    melhor. Por quê? Simplesmente porque os seus processos estão bem definidos, testados e possuem maturidade.

    Percebeu como os processos estão muito presentes na Engenharia de Software? Os improvisos, nas atividades de
    desenvolvimento, não podem ocorrer, pois os resultados seriam desastrosos. É por isso que existem os modelos de
    maturidade de processos.

    Segundo Couto (2007), os processos de melhoria se preocupam muito mais com a evolução dos processos que compõem as
    atividades de desenvolvimento do que com a agregação de novos processos ou inovações. O CMM utiliza [#], em sua
    estrutura, cinco níveis de maturidade, dentro de uma base hierárquica. Para melhor compreensão do modelo, observe a
    Figura 2.14.

    --------------------------------------------------- IMAGEM 2.14 ---------------------------------------------------

    Com base no modelo apresentado, observe o detalhamento de cada um dos níveis:

     Nível 1 (Inicial): não existe controle de processos, a equipe é guiada pelas atividades e entregas. O cliente faz
      a avaliação na entrega e, quando necessário, ocorrem os ajustes.

     Nível 2 (Repetitivo): nessa fase os controles de processos básicos já são utilizados nos desenvolvimentos. Porém,
      o mais relevante é que os processos bem-sucedidos passam a ser replicados em outros projetos.

     Nível 3 (Definido): após repetir boas práticas nos projetos, esses procedimentos são estabelecidos como padrão bem
      definido nas atividades de desenvolvimento. Com o tempo, passa a ser cultural entre os colaboradores.

     Nível 4 (Gerenciado): uma vez que se esteja no nível 3, momento em que já existe uma definição dos processos, é
      possível utilizar ferramentas de medição de estatística para efetuar o gerenciamento e o controle dos processos.

     Nível 5 (Otimização): conforme o conhecimento acerca dos processos vai aumentando e, consequentemente, o nível de
      maturidade, é possível repensar alguns processos, permitindo a otimização destes. [#]

    Ainda conforme define Couto (2007), os níveis de maturidade apresentam uma estrutura evolutiva, por meio da qual se
    busca atingir a qualidade esperada em determinado nível, para que, assim, seja possível passar ao próximo estágio e
    aumentar a capacidade dos processos dentro da organização.

    Ainda dentro do tópico sobre modelos relacionados ao processo de desenvolvimento, porém agora com o olhar voltado
    para a capacidade dos processos, abordaremos o framework CMMI (Capability Maturity Model Integration). Também
    desenvolvido pela SEI, em 2012 foi lançada a sua última versão (1.3). O principal objetivo dessa ferramenta é
    analisar a capacidade da maturidade do processo de software.

    Segundo Koscianski e Soares (2006) [#], o CMMI, quando inserido na área de desenvolvimento de software, utiliza a
    capacidade e a maturidade para atingir metas previamente estipuladas, com nível de qualidade acordado entre as
    partes. Seu maior objetivo é a produção de software com o maior nível de qualidade e a menor taxa de erros. [#]

    A estrutura do CCMI é dívida em cinco níveis, [#] os quais são utilizados para determinar a capacidade e a
    maturidade dos processos. Para melhor compreensão do modelo, observe a Figura 2.15.

    --------------------------------------------------- IMAGEM 2.15 ---------------------------------------------------

    Com base no modelo apresentado, observe o detalhamento de cada um dos níveis:

     Nível 0 (Incompleto): os processos não são executados em sua totalidade ou são parcialmente executados.

     Nível 1 (Executado): os processos conseguem satisfazer metas específicas, e a organização como um todo_ reconhece
      que existem processos definidos.

     Nível 2 (Gerenciado): nessa fase, além dos processos serem executados, existe também um monitoramento e um
      planejamento deles.

     Nível 3 (Definido): o processo serve como boa prática e se torna padrão dentro da organização.

     Nível 4 (Gerenciado): são utilizadas medições e técnicas de estatística para análise dos processos, o que gera,
      consequentemente, melhorias.

     Nível 5 (Otimizado): o foco é a melhoria contínua para a busca de melhores resultados. [#]

    Para que você compreenda o CMMI em uma situação profissional de desenvolvimento de software, observe o seguinte
    exemplo: o desenvolvimento do sistema web de determinada organização se dá em três partes: front end, back end e
    banco de dados. Ocorre que muitas vezes o tipo de dado tratado pela equipe de back end não está alinhado com o
    desenvolvedor de banco de dados. Ainda, ocorrem situações em que é necessária a validação dos campos tanto pelo
    front end (por meio do Bootstrap) quanto pelo desenvolvedor back end.

    Percebeu como nesse caso, os processos de software não estão definidos? Claramente a equipe está no nível 1 do CMMI.
    Por meio de técnicas específicas, de planejamento e da utilização das diretrizes do CMMI, a equipe poderá visar ao
    próximo nível, otimizando e profissionalizando os seus processos de desenvolvimento de software.

    NORMAS ISO DE QUALIDADE DE PROCESSOS
    Provavelmente você deve ter percebido, ao longo das discussões, que existem diversos modelos, normas e metodologias
    para todo_ o tipo de solução. Com a qualidade de processos não é diferente. Dito isso, você poderá compreender como
    a norma ISO 9001 pode auxiliar os desenvolvedores de software na busca da qualidade dos seus processos.

    Segundo Valls (2003), [#] a ISO 9001:2015 possui uma característica fundamental quanto à visão sistêmica que deve
    reger as atividades de desenvolvimento. Ou seja, os profissionais devem conhecer os processos, e esse conhecimento
    deve ser bem consistente entre os membros da organização como um todo_.

    Valls (2003) defende ainda que a ISO 9001 é um sistema de qualidade que visa à garantia de otimização dos processos.
    Essa norma também é conhecida nos meios profissionais como SQA (Sistema de Gestão da Qualidade) [#]. Para os
    gestores de projetos de desenvolvimento de software é um poderoso instrumento de correção e de melhoria de processos

    Conforme definido por Koscianski e Soares (2006), [#] a ISO 9001 é estruturada por meio de oito princípios da
    qualidade, conforme pode ser observado a seguir:

     Foco no cliente: o pilar principal de qualquer organização deve ser o cliente, de modo que a norma orienta a busca
      constante das necessidades e expectativas dele. Exemplo: o cliente deseja uma aplicação mobile, porém a empresa
      apresenta uma “opção” de aplicação web, que é acessada por meio do navegador. Embora tenha sido apresentada uma
      solução (que poderia até resolver o problema do cliente), o que foi solicitado foi para uma aplicação mobile.

     Liderança: na norma existem indicativos para uma liderança que busque, com disciplina, empenho, engajamento e
      dedicação, os melhores resultados para a organização. Exemplo: a equipe está envolvida em um projeto cujo cliente
      solicita novas funcionalidades e modificações (sendo que isso estava previsto no contrato). Retrabalho pode gerar
      desconforto na equipe. Por meio da norma, o gestor pode reverter esse quadro.

     Envolvimento das pessoas: os desenvolvedores devem ter ciência do seu papel no projeto. Além disso, devem ocorrer
      treinamentos, workshops e outras atividades que otimizem o seu desempenho. Exemplo: um projeto necessita consumir
      uma API cujo funcionamento é pouco conhecido. A organização pode promover cursos Hands on de forma que os
      desenvolvedores possam atender ao projeto sem que ocorram improvisos.

     Abordagem do processo: formalizar os processos que devem ser utilizados no desenvolvimento. Gerenciar a sua
      correta utilização, promovendo ajustes quando necessário. Exemplo: determinado desenvolvedor acha que a construção
      de uma função sairá melhor fazendo do jeito dele do que utilizando o processo estabelecido na organização. Nesse
      caso, são necessárias algumas intervenções para ajuste de conduta.

     Abordagem sistêmica para a gestão: os processos devem ser visualizados como partes que compõem um sistema. Dessa
      forma, as pessoas envolvidas nos processos conseguem entender melhor o seu papel no projeto. Exemplo: imagine que
      exista uma equipe desenvolvendo modos de pagamento para um e-commerce. Os desenvolvedores necessitam conhecer os
      processos que antecedem o pagamento (escolha do produto, cesta de compras, cadastro do cliente, etc) e, ainda, os
      que são posteriores (retorno de confirmação de pagamento, acompanhamento de envio, etc).

     Melhoria contínua: nesse princípio, os colaboradores compreendem o detalhamento dos processos e promovem melhorias
      . Exemplo: determinada API, que constrói gráficos com consulta a banco de dados relacional, apresenta um atraso.
      Por meio de testes, a equipe descobriu que, ao se utilizar banco de dados não relacional, existe uma diminuição no
      tempo de consulta.

     Abordagem para tomada de decisão: os indicadores de qualidade devem permitir uma análise e oportunizar melhorias.
      Exemplo: ao se utilizar um software apara contagem de linhas de códigos produzidas, percebeu-se que um intervalo
      de cinco minutos a cada meia hora gera um aumento de produtividade.

     Benefícios: deve haver uma relação de pareceria entre as partes, de forma que possam gerar benefícios nos
      processos de desenvolvimento. Exemplo: uma forma de estreitar laços e conhecer os processos do cliente é alocar,
      por um período, na empresa, colaboradores responsáveis por mapeamento de processos e levantamento de requisitos.

    Ainda de acordo com Valls (2003), ao se implantar o modelo ISO 9001:2015, deve-se [#]: estabelecer, manter e buscar
    melhorias para a gestão da qualidade com ênfase nos processos e nas interações entre os microprocessos. Dessa forma,
    fica evidente o objetivo de se conhecer a fundo cada parte dos processos e a interação entre eles, para que não
    ocorra a dissociação entre os processos.

    Você percebeu como a compreensão da ligação entre as partes facilita o entendimento dos processos? Além da
    compreensão desse aspecto, Valls (2003) afirma que, para a melhoria dos processos, as organizações devem compreender
    claramente os pontos a seguir: [#]

     Entradas e saídas: todo_ software possui entradas e saídas. Estas devem estar bem claras desde a fase de
      levantamento dos requisitos, pois isso possibilita o aumento da maturidade desse ponto.

     Sequência dos processos: os processos, quando muito bem claros e estabelecidos, permitem à equipe compreender como
      será a sequência de trabalho. Esta deve apresentar uma lógica bem estruturada.

     Interação dos processos: o conhecimento dos processos permite a compreensão da forma e do momento em que ocorrerão
      as interações entre eles, permitindo, assim, o estabelecimento de pontos de atenção dentro do projeto.

     Os recursos disponíveis: não se trata apenas de recursos computacionais. Os recursos mais escassos normalmente
      estão ligados a prazo e a mão de obra especializada.

     As responsabilidades: cada colaborador dentro da equipe deve ter em mente sua atribuição dentro do projeto, além
      de conhecer os pares de interação e reconhecer as lideranças.

     Os riscos: conhecer os processos mais a fundo permite aos gestores de projetos de desenvolvimento a identificação
      dos riscos e dos pontos de atenção, o que reflete em ações preventivas para o cumprimento da qualidade e dos
      prazos. [#]

    O processo de implantação da ISO 9001 é relativamente simples e pode ser feito nas empresas independentemente do seu
    porte. Porém, obter o reconhecimento da aplicação 100% correta por meio da certificação ISO 9001 exige que a empresa
    já possua um bom nível de maturidade em seus processos de desenvolvimento de software, além de um conhecimento
    profundo das partes que compõem as suas normas e diretrizes.

    MELHORIA DE PROCESSOS INDIVIDUAIS E DE EQUIPE (PSP)
    Em uma coisa a maioria de nós concorda: os softwares são desenvolvidos por pessoas. Indivíduos que, em algum momento
    da vida, dedicaram-se a aprender a desenvolver sistemas por meio de alguma tecnologia e hoje abstraem informações
    das pessoas e transformam essas ideias em códigos. É por esse motivo, justamente, que surge a ferramenta PSP, a qual
    visa às pessoas que desenvolvem os sistemas.

    Segundo Koscianski e Soares (2006), [#] a sigla PSP significa Personal Software Process, cujo objetivo é promover o
    desenvolvimento de software com enfoque na habilidade individual dos colaboradores [#]. Segundo o PSP, o
    conhecimento, a avaliação e a melhoria contínua no processo individual de desenvolvimento de software deve observar
    os erros e as falhas cometidas para que possam ser corrigidos e aprendidos pelo desenvolvedor.

    Para exemplificar uma das formas de se [#] operacionalizar o PSP em um projeto, pode-se utilizar a contagem de
    erros em código de desenvolvimento. Uma das maneiras clássicas utilizadas para esse fim é conhecida por Kloc, que
    tem como objetivo contar a quantidade de erros a cada mil linhas de código [#]. Ainda segundo Koscianski e Soares
    (2006), o PSP é composto por quatro níveis de competência conforme pode ser observado a seguir:

     PSP 0 – Processo atual: aqui deve ser estabelecida a base da competência, que inclui a determinação dos métodos de
      medição, o que medir e a que momento (desenvolvimento, compilação e teste), permitindo, assim, o desenvolvimento
      de relatórios para análise de falhas. Nessa fase ainda deve-se desenvolver o PIP (Process Improvement Proposal), o
      qual, por meio de um formulário, deve registrar os problemas dos processos e sugestões de melhorias.

     PSP 1 – Estimativa de tamanho: nessa fase existem apenas dois objetivos: o planejamento do tempo e das tarefas.
      Trata-se de uma fase de planejamento pessoal, na qual se deve ter uma estimativa de quantas tarefas estão
      atribuídas ao colaborador e o tempo de desenvolvimento delas. É claro que essas medidas variam conforme o nível de
      competências e habilidades do desenvolvedor.

     PSP 2 – Revisão de código: o enfoque dessa fase é o processo de administração da qualidade pessoal. Nela a visão
      técnica da tecnologia, por meio da qual está se desenvolvendo, deve observar a aplicação dos processos
      estabelecidos e os resultados positivos e negativos.

     PSP 3 – Desenvolvimento cíclico: trata-se de um processo pessoal cíclico, no qual a correta aplicação dos
      processos, que atendem as demandas e a qualidade, seja processada em cascata, a fim de se obterem os melhores
      resultados.

    Koscianski e Soares (2006) afirmam que as ferramentas de aferição, em conjunto com os tratamentos, fornecem curvas
    estatísticas que possibilitam uma análise mais profunda do desenvolvedor e ainda projeção de sua curva de evolução
    profissional. Porém, essa mesma técnica pode diagnosticar membros de equipe que, embora apliquem ações corretivas,
    insistem em não alinhar os processos de desenvolvimento.

    REFLITA
    As normas, referências, guias e metodologias fornecem um referencial para se atingir um objetivo e normalmente são
    documentos completos que permitem muitos olhares para um mesmo problema, fazendo com se tenha uma base técnica muito
    interessante. De fato, as atividades são desenvolvidas por pessoas, mas será que apenas uma metodologia pode ser
    capaz de promover mudanças?

    MELHORIA DE PROCESSOS DE SOFTWARE BRASILEIRO (MPS.BR) [#]
    No Brasil, nós possuímos uma ferramenta que possibilita a melhoria dos processos de softwares brasileiros. Porém,
    isso não significa que as suas normas sejam melhores ou piores que outras, pois estas seguem padrões internacionais
    de qualidade de processos. Aqui no País, a entidade que faz a gestão do MPS.BR é a Softex [#], responsável por
    apoiar a cultura da qualidade de software e por contribuir com a melhoria contínua dos processos/produto de software

    EXEMPLIFICANDO
    Uma dúvida muito comum no MPS.BR é referente aos processos de implementação. A Softex, gestora do MPS.BR,
    disponibiliza um tutorial com os [#] passos para uma empresa ser avaliada quanto ao nível de maturidade na
    utilização do modelo. Os passos necessários podem ser observados a seguir:

     Habilitar um representante da empresa na equipe de avaliação.
     Implementação do modelo MPS.BR.
     Contratação da instituição avaliadora.
     Avaliação oficial.
     Publicação do resultado oficial (SOFTEX, [s.d.]). [#]

    [#] Segundo Rocha (2005), a construção das técnicas constituintes ao MPS.BR é composta pelas NBR ISO/IEC, conforme
    pode ser observado no esquema representado na Figura 2.16.

    --------------------------------------------------- IMAGEM 2.16 ---------------------------------------------------

    Para a compreensão das siglas que compõem o MPS.BR, acompanhe os tópicos a seguir:

     Modelo de Referência (MR): contém informações a forma como a organização deve conduzir os seus processos para
      atingir os resultados. Ainda é possível, nesse mesmo documento, determinar o nível de maturidade e da capacidade
      dos processos descritos na NBR ISO/IEC 12207.

     Modelo de Avaliação (MA): trata-se do processo no qual são determinados os parâmetros e requisitos para se aferir
      a qualidade do desenvolvimento. É baseado na norma ISO/IEC 15504.

     Modelo de Negócio (MN): determina o nível de maturidade dos processos, que podem ser: (A) Otimizado, (B)
      Gerenciado, (C) Definido, (D) Largamente definido, (E) Parcialmente definido, (F) Gerenciado e (G) Parcialmente
      gerenciado.[#]

    Vale ressaltar que [#] cada modelo apresenta o seu formulário específico: MR (Guia Geral e Guia de Aquisição), MA
    (Guia de Avaliação) e MN (Documentos do projeto). Segundo Rocha (2005), a construção das técnicas constituintes ao
    MPS.BR é composta pelas NBR ISO/IEC:

     NBR ISO/IEC 12207 para processo de ciclo de vida de software.
     ISO/IEC 15504 para avaliação de processo.
     ISO/IEC 15504-5 para modelo de avaliação de processo de software.

    Na prática, como o MBS.BR deve ser iniciado no nível G, para o qual o manual determina 28 GPR, que são os objetivos
    que a equipe deve alcançar para atingir de maturidade. Observe a seguir as três primeiras GPR do nível G:

    ----------------------------------------------------- Citação -----------------------------------------------------
    GPR 1. O escopo do trabalho para o projeto é definido;
    GPR 2. As tarefas e os produtos de trabalho do projeto são dimensionados utilizando métodos apropriados;
    GPR 3. O modelo e as fases do ciclo de vida do projeto são definidos;
    (MPS.BR, 2012, p. )

    Os GPRs devem ser documentados, gerenciados e acompanhados. O modelo de documento é sugerido pelo manual, porém ele
    mesmo deixa flexível para que as empresas adicionem ou retirem quais campos desejar.

    Caro aluno, você percebeu ao longo do texto como os métodos, normas e modelos de qualidade de processo são
    importantes para a área de desenvolvimento de software? Por esse motivo, é importante que esses pontos abordados
    sejam compreendidos e aplicados em projetos de desenvolvimento. Fica evidente que, ao utilizar tais técnicas, os
    resultados gerados, conforme o nível de maturidade aumenta, e as melhorias tendem a ser constantes na maioria dos
    processos.

    SAIBA MAIS
    Normas como ISO 9000, 9001, etc. possuem certificações. São provas feitas em unidades certificadoras que comprovam,
    por meio de testes, que o profissional possui competências e habilidades para utilizar determinada tecnologia.

    PESQUISE MAIS
    Em diversas normas, métodos e metodologias, são utilizados níveis para classificar a maturidade de uma
    equipe/organização. Entre esses níveis, normalmente existe um em que o nível de maturidade é gerenciado e em que são
    utilizados medições e tratamentos estatísticos para uma análise dos processos.

    A UNIVESP disponibiliza, em seu canal do YouTube, uma aula que trata exatamente desse tema. Não deixe de conferir!

    CONTROLE Estatístico de Processo – Aula 01 – Introdução ao Controle de Qualidade. São Paulo: Univesp, 2017. 1 vídeo
    (21 min). Publicado pelo canal UNIVESP.

    #ref Unidade 2 - Seção 3
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
     CONTROLE Estatístico de Processo – Aula 01 – Introdução ao Controle de Qualidade. São Paulo: Univesp, 2017. 1
    vídeo (21 min). Publicado pelo canal UNIVESP. Disponível em: https://bit.ly/2Xg7WkH. Acesso em: 19 out. 2020.

     COUTO, A. B. CMMI: integração dos modelos de capacitação e maturidade de sistemas. Rio de Janeiro: Ciência Moderna
    , 2007.

     KOSCIANSKI, A.; SOARES, M. dos S. Qualidade de software: aprenda as metodologias e técnicas mais modernas para o
      desenvolvimento de software. São Paulo: Novatec, 2006.

     MPS.BR – Melhoria de Processo do Software Brasileiro. Guia Geral MPS de Software. Brasília: Softex, 2012.
      Disponível em: https://bit.ly/3oluRa5. Acesso em: 15 nov. 2020.

     SOFTEX. MPS BR. Softex, Brasília, [s.d.]. Disponível em: https://softex.br/mpsbr/. Acesso em: 16 out. 2020.

     SOMMERVILLE, Ian. Engenharia de Software. 9. ed. São Paulo: Pearson Prentice Hall, 2015.

     VALLS, V. M. A documentação na ISO 9001:2000. Banas qualidade, São Paulo, v. 12, n. 133, p. 100-105, jun. 2003.
    """


def unidade3_secao1():
    """
    ----------------------------------------------- UNIDADE 3 / SEÇÃO 1 -----------------------------------------------
    CONCEITOS DE TESTES DE SOFTWARE - Roque Maitino Neto

    CONCEITO-CHAVE
    Já vai longe o tempo em que um sistema computacional tinha sua execução restrita apenas a um computador de mesa e
    servia a propósitos típicos do meio corporativo, como controle de vendas e de estoques. Atualmente, há uma grande
    variedade de equipamentos que dependem de sistemas para executarem suas funções de modo muito mais flexível e
    confiável do que seria sem uma aplicação computacional. Exemplos não faltam e nossos carros e televisores são
    apenas dois deles. Há programas sendo executados em todos os lugares e controlando dispositivos indispensáveis em
    nosso cotidiano. Mas o que aconteceria se esses programas falhassem?

    Para que essa pergunta não precise ser respondida da pior forma, a Engenharia de Software desenvolveu mecanismos
    para que os produtos de software – tantos os comuns quanto os que dão “inteligência” aos nossos equipamentos –
    criados pelos desenvolvedores passassem por processos que atestassem sua aptidão para executar suas funções de
    forma adequada e com elevados níveis de qualidade. Esses processos incluem a verificação, a validação e os testes de
    software e, se por meio de uma análise menos atenta eles podem parecer idênticos, uma conceituação apropriada
    servirá para esclarecer seus conceitos e diferenciá-los.

    GERENCIAMENTO DA QUALIDADE DO SOFTWARE
    No entanto, antes de individualizarmos esses termos, vale a pena posicioná-los em um contexto mais amplo,
    relacionado à qualidade de um produto, e conhecido por Gerenciamento da Qualidade do Software (ou Software Quality
    Management). Nesse contexto, a verificação e a validação são colocadas como ações intimamente relacionadas,
    destinadas à averiguação da conformidade do produto com as necessidades do cliente e comumente referenciadas em
    conjunto, sob a sigla V&V.

    De acordo com uma importante publicação da área de Engenharia de Software (IEEE, 2014), o objetivo da V&V é ajudar
    a organização que desenvolve software a incorporar qualidade ao sistema durante o ciclo de vida, por meio de
    avaliações objetivas de produtos e de processos. Tais avaliações demonstram se os requisitos são corretos,
    completos, precisos, consistentes e testáveis. Os processos de V&V determinam se os produtos desenvolvidos em certa
    atividade estão em conformidade com os requisitos dela e se o produto satisfaz seu uso pretendido.

    As atividades de V&V, portanto, não são aplicadas unicamente a um programa ou função, mas a qualquer artefato que
    seja criado como resultado de determinada etapa do ciclo de vida de um produto. Os requisitos, o projeto e a
    implementação do produto são artefatos que podem (e devem) passar por verificações e validações.

    Nesse sentido, a IEEE (2014) estabelece que a verificação é uma tentativa de garantir a correta construção do
    produto, com vistas a atender as especificações impostas aos produtos de saída em atividades anteriores. Já a
    validação é uma tentativa de garantir que o produto certo seja construído, ou seja, que ele atenda a sua finalidade
    específica.

    Schach (2009) relaciona os conceitos de verificação e de validação a momentos específicos do ciclo de vida de um
    produto de software. Nesses termos a verificação se refere ao processo de determinar se um fluxo de trabalho foi
    executado corretamente ou não, e ela ocorre ao final de cada fluxo de trabalho. Já a validação é o processo
    intensivo de avaliação que ocorre imediatamente antes de o produto ser entregue ao cliente; seu propósito é o
    determinar se o produto como um todo_ satisfaz ou não às suas especificações.

    Embora sejam expressões parecidas e estejam inseridas em um contexto único, verificação e validação não são a mesma
    coisa. Santos e Oliveira (2017) resumem assim os termos: verificação refere-se à garantia das especificações do
    software em uma determinada fase do desenvolvimento, enquanto a validação se refere à garantia do produto de
    software como um todo_. A validação é uma fase mais geral, na qual o produto criado é confrontado com as
    expectativas do cliente.

    Observadas sob uma perspectiva teórica, expressões como “incorporar qualidade ao sistema” e “verificar se uma
    atividade está em conformidade com os requisitos” podem transmitir uma falsa sensação de simplicidade procedimental.
    Entretanto, a aplicação de procedimentos de verificação e validação requerem planejamento cuidadoso e precisão na
    execução. O objetivo do planejamento de V&V é garantir que cada recurso, função e responsabilidade sejam claramente
    atribuídos.

    Nessa fase de planejamento, devem ser especificados os recursos, suas funções e atividades, bem como as técnicas e
    ferramentas a serem usadas. A compreensão dos diferentes propósitos de cada atividade de V&V ajuda no planejamento
    cuidadoso das técnicas e dos recursos necessários para cumprir seus propósitos. O planejamento também deve abordar a
    gestão, a comunicação, as políticas e os procedimentos das atividades de V&V.

    ASSIMILE
    A verificação consiste em analisar o software para ver se ele está sendo construído de acordo com o que foi
    especificado. A validação consiste em analisar o software construído para ver se ele atende às verdadeiras
    necessidades dos interessados. Assim, a pergunta-chave para a validação é “Estamos fazendo a coisa certa?”,
    enquanto que a pergunta-chave para a verificação é “Estamos fazendo a coisa do jeito certo”? (WAZLAWICK, 2013).

    Conforme mencionamos, a verificação e a validação estão incluídas em um escopo mais abrangente e estão vinculadas à
    Garantia da Qualidade do Software (Software Quality Assurance ou SQA). Na visão de Pressman e Maxim (2016), a
    verificação e a validação incluem grande variedade de atividades de SQA, quais sejam as revisões técnicas,
    auditorias de qualidade, monitoramento do desempenho, simulação, estudo de viabilidade, teste de usabilidade e
    testes de aceitação e de instalação. Os autores complementam que, embora a aplicação de teste tenha um papel
    extremamente importante em V&V, muitas outras atividades são necessárias.

    À propósito, a menção aos testes vem a calhar. Como podemos posicioná-lo nesse contexto? O teste é a última frente
    de preservação da qualidade, mas não pode ser entendido como a garantia total de que a produção entregue pelas
    equipes está livre de defeitos. O teste proporciona o último elemento a partir do qual a qualidade pode ser estimada
    e, de forma mais pragmática, os defeitos podem ser encontrados. A qualidade é incorporada ao software por meio da
    correta aplicação das técnicas da Engenharia de Software e é confirmada durante o teste (PRESSMAN; MAXIM, 2016).

    TESTES DE SOFTWARE
    Um teste não é um procedimento isolado que pode ser concluído por um único membro da equipe. Embora seja comum
    tratá-lo por “teste”, sua execução depende de um conjunto de ações e procedimentos executados por vários elementos
    da equipe de desenvolvimento. Por isso, melhor seria chamá-lo de processo de teste, já que formalmente ele
    representa uma sequência de ações executadas com o objetivo de encontrar problemas no software, o que aumenta a
    percepção da qualidade geral dele e garante que o usuário final tenha um produto que atenda às suas necessidades
    (PINHEIRO, 2015).

    É necessário, no entanto, destacar que o objetivo do teste não é o de garantir que um programa seja absolutamente
    livre de defeitos, mas o de encontrar problemas no software. Por mais que essa premissa nos soe estranha (e um pouco
    frustrante) ela deriva do fato de que nenhum teste é capaz de assegurar 100% de ausência de defeitos em um sistema.
    Logo, se o processo de teste não revelar defeitos, há que se aprimorar o processo de forma geral. Não se pode
    considerar que o sistema não possui problemas se o teste não os revelar.

    TESTES DE SOFTWARE

    Que expressão você usa quando um programa simplesmente trava ou não produz o resultado que se espera dele? Tudo o
    que acontece de incomum em um programa pode ser chamado de erro?

    ERRO
    Ocorre quando o resultado obtido em um processamento e o que se esperava dele não são coincidentes. Um erro também
    está associado a uma violação nas próprias especificações do programa.
    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    resultado esperado -> um usuário não é admin
    resultado obtido   -> um usuário consegue acessar um módulo

    DEFEITO
    Trata-se de deficiência algorítmica que, se ativada, pode levar a uma falha.
    ----------------------------------------------------- EXEMPLO -----------------------------------------------------
    Um loop que não incrementa ou que incrementa de forma errada

    FALHA
    É tida como um não funcionamento do programa, provavelmente provocada por um defeito. No entanto, uma falha também
    pode ser atribuída a uma queda na comunicação ou a um erro na leitura do disco, por exemplo.

    Mas, afinal, o que é teste de software? Como ele se efetiva? Há um plano a ser executado?

    IEEE (2014) nos oferece o seguinte conceito: o teste de software consiste na verificação dinâmica de que um
    programa, de fato, fornece comportamentos esperados em um conjunto finito de casos de teste adequadamente
    selecionados do domínio de execução geralmente infinito.

    É natural que uma definição retirada de uma publicação de caráter estritamente técnico peça uma explicação que a
    aproxime da percepção comum que temos a respeito de teste.

    A expressão “verificação dinâmica” indica que aplicar um teste significa, necessariamente, executar o programa. Além
    disso, essa execução deve ser baseada em entradas previamente selecionadas. Conforme estudaremos em detalhes na
    sequência, casos de teste são entradas fornecidas ao programa e às respectivas saídas esperadas. Na teoria, as
    entradas possíveis para um programa são infinitas, daí a necessidade de restringi-las em um “conjunto finito de
    casos de teste” escolhidos criteriosamente.

    EXEMPLIFICANDO
    Antes de seguirmos em frente em nosso conteúdo, vale a pena fazermos um exercício de imaginação que colocará você
    diante da necessidade imperiosa de se testar um software (ou função dele) antes de exibi-lo a alguém ou de colocá-lo
    em funcionamento. Você assumiu a missão de criar uma nova funcionalidade para o sistema que já se encontrava em
    operação, com a promessa de facilitar o controle do estoque dos produtos controlados pela empresa em que atua.

    Na urgência de apresentar a nova funcionalidade, você reuniu os diretores e envolvidos com os estoques e, no
    primeiro acesso à função, um erro se manifestou no programa e sua execução foi interrompida. Feita a correção ali
    mesmo durante a demonstração, você resolveu confrontar a quantidade física de um certo item de estoque com a
    quantidade fornecida pelo sistema. Novamente uma falha se manifestou e uma resposta inesperada foi obtida. Dois
    tipos de problemas se tornaram visíveis na apresentação e a percepção de qualidade em relação à sua função sofreu
    abalo, para dizer o mínimo. Com os testes adequados, tal constrangimento teria sido facilmente evitado.

    Bem, mas como os testes são feitos? Há uma ferramenta computacional que os execute? Nas seções futuras desta
    unidade, teremos a oportunidade de abordar esses assuntos com mais riqueza de detalhes, mas convém termos agora uma
    rápida visão de um programa sendo testado. Para que isso seja possível, algumas premissas devem ser apresentadas:

    O programa em teste foi criado e está sendo executado no Eclipse, um importante ambiente integrado de
    desenvolvimento (ou IDE – Integrated Development Environment) utilizado principalmente para criação e para teste de
    aplicações Java.

    O tipo de teste em questão é o de unidade. Por meio dele, apenas uma unidade do programa (uma função ou uma classe,
    por exemplo) é testada e não o programa todo_.

    A ferramenta utilizada para a efetivação do teste é o JUnit, que já se encontra instalada nativamente no Eclipse.

    Na Figura 3.1, você vê uma classe – chamada CalculoTest –, que representa um caso de teste. Note que há variáveis
    com os valores 10 e 5 e uma terceira variável que contém o valor esperado para a execução da unidade que, no caso,
    realiza uma operação de soma.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.1 | Classe de teste escrita em Java
    Fonte: Medeiros (2009, [s.p.]).

    A classe a ser testada para este caso de teste está descrita na Figura 3.2 e se chama Calculo.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.2 | Classe de teste escrita em Java
    Fonte: Medeiros (2009, [s.p.]).

    A execução da classe CalculoTest através do JUnit retornará sucesso para o caso de teste em questão. Dessa forma,
    uma função pode ser testada por meio dessa ferramenta.

    PLANO DE TESTES
    Bem, como já compreendemos o conceito de teste, sua efetivação dependerá apenas da iniciativa do seu desenvolvedor
    em executar o programa com base em alguns casos de teste, não é mesmo? Responder “sim” a essa pergunta equivale a
    ignorar uma etapa absolutamente indispensável neste contexto: o planejamento.

    Pressman e Maxim (2016) ensinam que teste é um conjunto de atividades que precisam ser planejadas com antecedência e
    executadas com base em um procedimento padrão, fato que motiva a criação de um modelo para o teste. Tal modelo,
    segundo os autores, deverá prever o emprego de técnicas específicas no projeto de casos de teste e no método de
    teste.

    Uma definição que deve fazer parte do plano de testes é a de quem deve executá-los. Schach (2008) pondera que a
    realização dos testes equivale a um processo destrutivo e, como era de se esperar, um programador não desejará
    “destruir” seu próprio trabalho. Por isso, atribuir a atividade de teste ao mesmo time que desenvolveu o produto
    certamente não é uma boa ideia, já que é grande a chance de a equipe entender que deve proteger seu programa e não
    deve criar testes que possam revelar, de fato, problemas no código.

    Outra razão para evitar a designação dos criadores do programa como seus testadores é o fato de que um terceiro
    poderá detectar uma falha no entendimento dos requisitos que passou despercebida ao programador e que foi
    implementada incorretamente. Um teste feito por outras pessoas pode aumentar a chance de descoberta do problema
    antes que ele tenha reflexos na operação do cliente.

    REFLITA
    O programador que desenvolveu o produto deve ser sumariamente excluído do procedimento de teste? Não seria prudente
    afastar dos testes alguém que conhece como ninguém o produto e que precisou se aprofundar nos requisitos antes de
    começar a desenvolvê-lo. Além disso, em um procedimento de depuração – que será detalhado adiante – as causas
    suspeitas de um problema poderão ser mais facilmente levantadas pelo próprio desenvolvedor do sistema do que por
    outro testador.

    Isto posto, é necessário mencionar que um plano de teste é normalmente separado em quatro grandes etapas:

    Planejamento: nesta etapa deve ser definido quem executa os testes, em que período, com quais recursos (ferramentas
    e computadores, por exemplo) e qual será a técnica utilizada (técnica estrutural ou técnica funcional, por exemplo).

    Projeto de casos de teste: aqui são definidos os casos de teste que serão utilizados no processo. No próximo item,
    esse conceito será detalhado.

    Execução do programa com os casos de teste: nesta etapa, o teste é efetivamente realizado. Análise dos resultados:
    aqui se verifica se os testes retornaram resultados satisfatórios.

    A Figura 3.3 ilustra um modelo de plano de teste.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.3 | Modelo de processo de teste
    Fonte: Sommerville (2018, p. 207).

    Bem, aparentemente os casos de teste são, de fato, o elemento central no processo de teste.

    EXEMPLIFICANDO
    Porém, antes de iniciarmos essa abordagem, apresentamos uma experiência relacionada a planos de teste. Embora
    fictícia, ela ilustra bem como alguns detalhes de planejamento podem ser decisivos para o sucesso ou para o fracasso
    da missão de se testar um produto. Imagine uma empresa de desenvolvimento de software que, depois de passar muitos
    anos terceirizando a atividade de teste, resolveu realizá-la com sua própria equipe. Em sua primeira experiência de
    teste, a equipe criou um plano pautado no modelo ilustrado na Figura 3.3 e suas linhas gerais estão abaixo
    reproduzidas:

    1. Todos os desenvolvedores que atuaram na criação do software mais a recém-criada equipe de testadores deveriam
       atuar no processo de teste. Eles deveriam selecionar casos de teste que exercitassem todas as funções do
       programa, criar dados de entrada para testar o programa e executá-lo com os dados de teste.

    2. Outro membro da equipe, que até então não havia participado de nenhum procedimento, deveria analisar os
       resultados dos testes e produzir um relatório de como eles haviam sido feitos e quais os resultados obtidos.

    Conforme planejado, os desenvolvedores e os testadores puseram-se a criar os casos de teste, planejaram as entradas
    para o programa e, uma vez concluídas essas atividades, executaram-no. Terminadas as execuções, disponibilizaram ao
    outro membro da equipe o resultado do teste fornecido pela ferramenta que haviam utilizado e foi a partir daí que a
    primeira experiência de testes da empresa desenvolvedora começou a se distanciar do sucesso.

    Esse novo elemento havia tido apenas um rápido contato com os requisitos do sistema, além de não ter participado do
    projeto (design) e nem da implementação do produto. Embora sua primeira atitude ao receber a incumbência de analisar
    os resultados tenha sido a de buscar informações sobre o sistema, melhor seria se ele tivesse acompanhado todo_ o
    processo de criação do produto, incluindo a sua implementação. Outro fator que dificultou bastante a primeira
    experiência foi o fato de que a comparação dos resultados previstos com os resultados obtidos começou a ser feita
    manualmente e, portanto, sem a utilização dos relatórios que poderiam ser fornecidos pela ferramenta de teste
    utilizada. Uma vez sanada a falta de conhecimento sobre o sistema do novo membro da equipe e utilizados os dados
    comparativos fornecidos pela ferramenta de teste, o procedimento foi levado finalmente a bom termo.

    CASOS DE TESTE
    Um caso de teste é o par formado por uma entrada possível a ser dada no programa e a correspondente saída esperada,
    também dada pelo programa e de acordo com os requisitos previamente especificados. Nesse caso, devemos entender o
    conceito de entrada como o conjunto de dados necessários para uma execução do programa e o de saída esperada como o
    resultado daquela execução ou de função específica. Com um exemplo esses conceitos serão mais bem esclarecidos:
    imagine que você esteja testando um programa (ou função) que promove a validação de datas inseridas pelo usuário.
    Um caso de teste possível seria formado pelo par (31/12/2020; válida). Ao receber a entrada 31/12/2020, a função de
    validação deveria retornar “data válida”.

    A boa escolha dos casos de teste é fator crítico para o sucesso da atividade. Um conjunto de casos de teste de baixa
    qualidade pode não exercitar partes críticas do programa e, em consequência disso, acabar não revelando defeitos no
    código. O que aconteceria, por exemplo, se o responsável pelos testes usasse apenas datas válidas como entradas? No
    mínimo, a parte do programa que trata das datas inválidas não seria executada, o que prejudicaria a confiabilidade
    do processo de teste e do produto testado.

    EXEMPLIFICANDO
    Observe os casos de teste a seguir:

    t1= {(15/2/1946; data válida), (30/2/2022; data inválida); (15/13/2023; data inválida); (29/2/2016; data válida),
    (29/2/2015; data inválida), (##/1/1985; data inválida)}. Vamos analisar cada um dos casos de teste do conjunto t1:

    A entrada do primeiro caso de testes (15/2/1946) é formada por um dia válido (ou seja, contido no intervalo entre 1
    e 31), um mês válido (contido no intervalo entre 1 e 12) e um ano válido. Essa entrada, que deverá provocar o
    retorno da mensagem “data válida” irá, portanto, exercitar trechos do programa criados para tratamento de dia, mês e
    ano simultaneamente válidos.

    A entrada 30/2/2022 também é formada por dia, mês e anos situados em intervalos válidos. No entanto, para o mês 2, o
    dia 30 é considerado inválido, pois o mês de fevereiro possui 28 ou 29 dias apenas. Assim, embora uma análise
    isolada de cada unidade da data possa indicar sua validade, a combinação do dia com o mês a torna inválida. O trecho
    de programa a ser exercitado, portanto, será diferente daquele exercitado no caso de teste anterior.

    Já a entrada 15/13/2023 também deverá retornar a mensagem “data inválida”, pois o mês está fora do intervalo
    permitido, independentemente do ano e do dia escolhidos. Mais uma vez, o trecho do programa de validação de data a
    ser exercitado será distinto dos anteriores.

    Prosseguimos com as entradas 29/2/2016 e 29/2/2015. Elas retornam, respectivamente, “data válida” e “data inválida”.
    Embora os dias e meses dessas datas sejam idênticos, 2016 foi ano bissexto, o que torna válida a primeira das datas.
    Já no caso de 2015, o dia 29 de fevereiro não fez parte do calendário daquele ano, o que torna a data inválida.
    Novamente o fluxo do programa em questão seguirá trechos específicos para realizar as validações.

    Por fim, a última data de entrada deverá retornar a mensagem “data inválida” devido a um caractere não numérico na
    unidade do dia.

    Embora exista um conjunto muito maior de entradas possíveis, esse conjunto de casos de teste será capaz de exercitar
    grande parte do código, o que aumentará a chance de descoberta de defeitos.

    Será, entretanto, que os casos de teste apresentam apenas esse aspecto? Observe o desenvolvimento de outro exemplo:
    imagine que o cenário de teste agora seja a checagem da funcionalidade de login em um sistema de reserva de
    passagens feito por agentes de viagens. A verificação a ser feita se apoia na resposta do sistema a diversos padrões
    de entrada de nome de usuário e de senha. Selecionamos três deles para fins de exemplificação:

    1. Checagem da resposta do sistema no caso de o agente entrar com nome de usuário e senha válidos.
    2. Checagem de resposta do sistema no caso de o agente entrar com nome de usuário e/ou senha inválidos.
    3. Checagem de resposta do sistema no caso de o agente pressionar a tecla Enter com o campo de nome de usuário vazio

    Para que possamos tornar mais específico nosso cenário, trataremos apenas do primeiro item e, com base nele,
    apresentamos o Quadro 3.1, que descreve um caso de teste relacionado.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Quadro 3.1 | Cenário detalhado do teste e um caso de teste possível
    Fonte: adaptado de How... (2014).

    Dessa forma, o caso de teste estará mais bem detalhado e as condições para que seja verificado estarão especificadas
    por completo. Note que até os passos para a realização do teste – que nos parecem tão óbvios – estão descritos nele.
    Fica claro que o sucesso no procedimento de testes está diretamente relacionado à boa escolha e ao bom uso dos casos
    de teste. Idealmente, cada conjunto de casos de teste deverá estar associado a um grande requisito diferente a ser
    testado. Para que não se corra o risco de defini-los incorretamente, é necessário planejamento e bom conhecimento da
    aplicação. Uma boa forma de se abordar o problema é a que segue, segundo Pinheiro (2015): definir o ambiente no qual
    o teste será realizado, definir a entrada desse caso de teste, definir a saída esperada para cada entrada e definir
    os passos a serem realizados para executar os testes.

    Quando um caso de teste é executado, seu resultado deve ser coletado. Podemos assumir diferentes abordagens para
    definir o resultado da aplicação de um caso de teste específico. A mais comum define as seguintes opções
    (PINHEIRO, 2015):

    Passou: todos os passos do caso de teste foram executados com sucesso para todas as entradas.
    Falhou: nem todos os passos foram executados com sucesso para uma ou mais entradas.
    Bloqueado: o teste não pôde ser executado, pois o seu ambiente não pôde ser configurado.

    REFLITA
    O que é um teste bem-sucedido? Imagine que determinada equipe tenha planejado um procedimento de teste, feito a
    escolha dos casos de teste e, após a execução do procedimento, tenha encontrado 0 (zero) defeito no código. Podemos
    afirmar que tal teste tenha sido bem-sucedido? Pense melhor e considere se há (ou houve) algum sistema que tenha
    sido elaborado 100% livre de problemas. Será que o conjunto de casos de teste foi corretamente selecionado?

    DEPURAÇÃO
    Enquanto testar significa executar o software para encontrar defeitos desconhecidos, a depuração (ou debug) é a
    atividade que consiste em buscar a localização desses defeitos no código. O fato de saber que há um problema
    causador de erro no programa não significa, necessariamente, que o testador sabe também em qual ou em quais linhas o
    problema está. Os ambientes de programação atuais oferecem recursos para depuração do programa e, durante esse
    processo, o valor assumido pelas variáveis sob inspeção em cada passo do algoritmo pode ser observado. Além disso,
    alguns pontos de parada da execução do programa podem ser inseridos no código. Tudo para possibilitar que o testador
    identifique e isole o defeito no código.

    Na visão de Pressman e Maxim (2016), a depuração ocorre como consequência de um teste bem-sucedido, ou seja, quando
    um caso de teste descobre um defeito. Nesse caso, a depuração é o processo que encontra e remove o erro. Embora não
    seja um teste, ela ocorre como um desdobramento dele e começa com a execução de um caso de teste. O procedimento de
    depuração pode apresentar um entre dois resultados possíveis:

    -> A causa é encontrada e corrigida e a depuração daquele problema é bem-sucedida.
    -> A causa não é encontrada e, nesse caso, o profissional que está realizando o procedimento tenta outro caso de
       teste que lhe pareça mais adequado para aquela causa.

    A Figura 3.4 ilustra um procedimento de depuração:

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.4 | O processo de depuração
    Fonte: Pressman e Maxim (2016, p. 489).

    A figura anterior nos revela o passo a passo do processo de depuração:

    1. A depuração começa com a execução de um caso de teste.
    2. Os resultados são avaliados e o desempenho apurado é diferente do desempenho esperado para aquele caso de teste.
    3. Quando as causas do defeito são plenamente identificadas, o problema é corrigido. Não havendo a perfeita
       correspondência entre o problema e a causa, procuram-se causas suspeitas.

    Observe a natureza cíclica do procedimento e a colocação de “causas suspeitas” como um dos elementos do ciclo. Essa
    nomenclatura revela que, embora a depuração deva obedecer a um processo ordenado, ela depende bastante ainda da
    experiência e da sensibilidade do testador. Um engenheiro de software, ao avaliar os resultados do teste, pode
    perceber sintomas de um problema e não a sua manifestação inequívoca, o que usualmente indica que a manifestação
    externa do problema e a sua real causa interna podem não ter nenhuma relação aparente uma com a outra.

    Nesse ponto, vale a pena observarmos um caso em que a depuração é necessária e, para esse fim, utilizaremos uma
    aplicação simples em Java e o ambiente integrado de desenvolvimento Eclipse. Originalmente a aplicação deve permitir
    a digitação de cinco números inteiros e, ao final, informar o maior número digitado. No entanto, o comportamento do
    programa não é o esperado e alguns recursos de depuração do ambiente de desenvolvimento devem ser usados para que os
    defeitos sejam encontrados. O Código 3.1 exibe o código-fonte da aplicação.

    Código 3.1 | Aplicação de retorno do maior valor digitado, com dois defeitos inseridos
    Fonte: elaborado pelo autor.

    import java.util.Scanner;
    public class Maior {
        public static void main (String args[]) {
            Scanner entrada = new Scanner(System.in);
            int i, x=0, valor;
            for (i=1;i<7;i++) {
               System.out.printf("\nDigite o %d valor: ",i);
               valor = entrada.nextInt();
               if (valor < x) x = valor;
             }
             System.out.printf("\nO maior valor inserido eh: %d ",x);
        }
    }

    Há dois defeitos nesse código: o primeiro está situado na linha 6: ao invés de permitir a digitação de cinco números
    , a aplicação solicitará que seis números sejam digitados, dada a comparação feita com valor menor que 7 e não menor
    que 6. O segundo defeito está situado na linha 9, local em que o teste para apuração do maior valor a cada iteração
    está invertido. Assim, o valor que retornará a aplicação será o menor e não o maior, como se espera.

    A utilização dos recursos de depuração do Eclipse começa com a mudança da perspectiva de visualização. Na opção de
    menu Window, acesse Perspective > Open Perspective > Debug, conforme ilustra a Figura 3.5. Essa providência fornece
    um padrão de dados adequado para a execução da depuração.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.5 | Alteração da perspectiva para o modo depuração
    Fonte: captura de tela do IDE Eclipse elaborada pelo autor.

    O primeiro passo efetivo do processo se dá com a marcação da linha do programa em que se deseja iniciar, de fato, a
    depuração. Essa ação é realizada por meio do posicionamento do cursor na linha desejada e o acesso à opção Run >
    Toggle Breakpoint. Uma marca na parte esquerda da linha será criada e, nesse momento, você estará apto a executar a
    aplicação no modo Debug, conforme mostra a Figura 3.6. Posicione o mouse sobre a classe (cujo nome deve aparecer no
    lado esquerdo da tela), acione o botão direito do mouse sobre ela e acesse a opção Debug As.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.6 | Execução da aplicação no modo debug
    Fonte: captura de tela do IDE Eclipse elaborada pelo autor.

    Neste momento a aplicação será executada no modo de depuração e os valores das variáveis poderão ser verificados
    passo a passo. Dessa forma, será mais fácil identificar as anomalias inseridas no código e corrigi-las.

    SAIBA MAIS
    Os termos que definiremos na sequência podem ser tomados como sinônimos, mas não são:

    1. Erro (error): trata-se da diferença detectada entre o resultado de uma operação e o resultado correto que se
       pretendia obter com ela.
    2. Defeito (fault): trata-se de uma linha de código, bloco ou conjunto de dados incorretos que provocam um erro.
    3. Falha (failure): trata-se de um não funcionamento do software, possivelmente provocada por um defeito, embora
       possa haver outras causas.
    4. Engano (mistake): é a ação humana que produziu o defeito no código (WAZLAWICK, 2013).

    PESQUISE MAIS
    A obra de Raul Sidnei Wazlawick chamada Engenharia de Software: Conceitos e Práticas (WAZLAWICK, 2013) contém um
    capítulo todo_ dedicado aos testes de software e, logo na parte introdutória desse capítulo, é oferecida a
    diferenciação entre os termos erro, defeito e falha, além da conceituação de engano.

    WAZLAWICK, R. S. Engenharia de software: conceitos e práticas. Rio de Janeiro: Elsiever, 2013.

    O item 1 do capítulo 8 da obra de Pfleeger (2004) apresenta a diferença entre defeito e falha em um software. A
    falha é apresentada pelo autor como o resultado de um ou mais defeitos em algum aspecto do sistema.

    PFLEEGER, S. L. Engenharia de Software: Teoria e Prática. 2. ed. São Paulo: Prentice Hall, 2004.

    Essa foi a base introdutória de testes que queríamos compartilhar com você. Há muito ainda a tratar sobre esse
    procedimento, mas é com a correta compreensão dos conceitos fundamentais que teremos sucesso na continuidade do
    nosso estudo. Iniciamos a seção tratando da conceituação de verificação e de validação e, na sequência, abordamos o
    conceito de testes. Depois o situamos como um procedimento e demos a ele uma sequência de etapas. Nesse mesmo
    contexto, tratamos do plano de testes e demos relevância ao papel do desenvolvedor no processo de teste de seu
    próprio produto. Por fim, abordamos os casos de teste e a depuração como elementos que darão subsídio à continuidade
    dos nossos estudos sobre teste.

    #ref Unidade 3 - Seção 1
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    HOW to write a TEST CASE? Software Testing Tutorial. [S.l.: s.n.], 2014. 1 vídeo (3 min). Publicado pelo canal
    Guru99. Disponível em: https://bit.ly/3poU6ZV. Acesso em: 14 de dez. 2020.

    IEEE Computer Society. Guide to the Software Engineering Body of Knowledge. Piscataway: The Institute of Electrical
    and Electronic Engineers, 2014.

    MEDEIROS, M. P. JUnit Tutorial. DevMedia, [S.l.], 2009. Disponível em: https://bit.ly/3sY9ApL. Acesso em: 17 dez.
    2020.

    PFLEEGER, S. L. Engenharia de Software: Teoria e Prática. 2. ed. São Paulo: Prentice Hall, 2004.

    PINHEIRO, V. Um comparativo na execução de testes manuais e testes de aceitação automatizados em uma aplicação web.
    SIMPÓSIO BRASILEIRO DE QUALIDADE DE SOFTWARE (SBQS), 14., 2015, Manaus. Anais [...]. Manaus: Uninorte, 2015.

    PRESSMAN, R.; MAXIM, B. Engenharia de Software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.

    SANTOS, L. D. V., OLIVEIRA, C. V. S.; Introdução à Garantia de Qualidade de Software. Timburi: Cia do e-book, 2017.

    SCHACH, S. R. Engenharia de Software: os paradigmas clássicos e orientados a objetos. 7. ed. São Paulo: McGraw-Hill,
    2009.

    SOMMERVILLE, I. Engenharia de Software. 9. ed. São Paulo: Pearson Prentice Hall, 2018. E-book. Disponível em:
    https://bit.ly/3a6T5PN. Acesso em: 6 dez. 2020.

    WAZLAWICK, R. S. Engenharia de software: conceitos e práticas. Rio de Janeiro: Elsiever, 2013.
    """


def unidade3_secao2():
    """
    ----------------------------------------------- UNIDADE 3 / SEÇÃO 2 -----------------------------------------------
    TIPOS DE TESTE - Roque Maitino Neto

    CONCEITO-CHAVE
    Como já se sabe, um produto de software necessita de inúmeros elementos para oferecer ao seu usuário um
    funcionamento pleno. A adequação do hardware e da infraestrutura de rede são apenas dois desses elementos, e o
    dimensionamento incorreto de um deles terá o potencial de arruinar a experiência do usuário. Há, no entanto, um
    aspecto que sempre terá papel decisivo na percepção do usuário em relação ao sistema que utiliza: as suas funções.
    Afinal, será por meio delas que ele interagirá com o programa e será através delas que alcançará seus objetivos
    traçados lá na fase de requisitos. Funções mal projetadas ou defeituosas podem, inclusive, desestimular o uso do
    sistema. Com tamanha importância, a área de testes não poderia deixar de direcionar muita atenção às funções do
    sistema e o faz por meio da aplicação da Técnica de Teste Funcional e do Teste de Funcionalidades, assuntos que
    desenvolveremos na sequência.

    ESTRATÉGIAS DE TESTES
    Entretanto, antes de abordarmos especificamente técnicas de teste, vale a pena as situarmos no contexto da
    estratégia de teste, a qual equivale a uma prática cujo objetivo é estabelecer um roteiro que descreve os passos a
    serem executados no processo de teste ou, em outras palavras, um modelo para os testes. Pressman e Maxim (2016)
    descrevem genericamente alguns elementos presentes em todas as estratégias adotadas para os testes:

    -> Revisões de software: boas revisões eliminam problemas no código antes da efetiva aplicação dos testes.

    -> Progressão do teste: os testes devem começar em uma unidade do software e progredir em direção à integração do
       sistema como um todo_.

    -> Depuração: esta atividade deve estar associada ao teste embora sejam elementos distintos entre si.

    -> Técnicas: diferentes técnicas de teste são adequadas a diferentes sistemas e são aplicadas conforme os recursos
       disponíveis à equipe.

    O último item da estratégia de teste embasa nosso próximo assunto e, para entendermos as razões de uma técnica, vale
    uma breve digressão: os testes são realizados tendo em vista objetivos específicos e são projetados para verificar
    diferentes propriedades de um sistema. A depender da técnica escolhida, os casos de teste podem ser planejados, por
    exemplo, para verificar se as especificações funcionais estão implementadas corretamente. Em outros casos, eles são
    selecionados para averiguação da adequação do desempenho, da confiabilidade e a da usabilidade, por exemplo. Assim,
    abordagens diferentes de teste motivam a aplicação de técnicas também diferentes de testes (PRESSMAN; MAXIM, 2016).

    TIPOS DE TESTES
    Embora as técnicas de teste sejam de grande relevância, por remeterem mais diretamente a metodologias de aplicação
    de testes, esta é não a única dimensão que podemos identificar nesse contexto. Na verdade, podemos estabelecer
    outros tipos de relações entre um teste e seu objetivo e, para isso, basta fixarmos o momento, o objeto e, como já
    mencionado, a maneira (ou metodologia) da aplicação.

    Parece complicado? Observe a Figura 3.7: ela posiciona os vários tipos de teste nas três dimensões que acabamos de
    mencionar: o “quando”, o “que” e o “como”.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.7 | As três dimensões dos testes
    Fonte: Braga (2016, p. 24).

    Apesar de não termos tido contato com os testes apontados na figura, é possível destacar que o teste funcional está
    relacionado a uma maneira de se realizar um teste, daí ter sido posicionado na dimensão “Como testar”. Já o teste de
    funcionalidade – que também será abordado na sequência – guarda associação com “o que testar”. Feita essa
    contextualização, passamos à abordagem inicial da técnica de teste funcional e do teste de funcionalidade.

    TÉCNICA DE TESTE FUNCIONAL E TESTE DE FUNCIONALIDADE
    Essa técnica baseia-se nas especificações do software para derivar os requisitos de teste. O teste é realizado nas
    funções do programa, daí o nome funcional. Não é seu objetivo verificar como ocorrem internamente os processamentos,
    mas se o algoritmo inserido produz os resultados esperados (BARTIÉ, 2002).

    Uma das vantagens dessa estratégia de teste é o fato de ela não requerer conhecimento sobre detalhes da
    implementação do programa. Sequer o código-fonte é necessário. Observe uma representação dessa técnica na Figura
    3.8:

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.8 | Visão do teste de caixa preta
    Fonte: Bartié (2002, p. 105).

    A ideia ilustrada na figura nos faz entender que o testador não conhece os detalhes internos do sistema e baseia seu
    julgamento apenas nos resultados obtidos a cada entrada fornecida. A esse respeito, Pressman e Maxim (2016) afirmam
    que um produto de software pode ser testado caso o responsável conheça a função específica para a qual aquele
    software foi projetado e, com esse conhecimento, estará em condições de realizar testes que demonstrem que cada uma
    das funções é operacional, embora o objetivo final do teste seja o de encontrar defeitos no produto. Os autores
    concluem que essa abordagem de teste se vale de uma visão externa do produto e não se preocupa com a lógica interna
    do software, a qual é opaca ao testador. Por esse motivo, a técnica funcional também é conhecida como teste de caixa
    preta.

    O planejamento do teste funcional envolve dois passos principais: identificação das funções que o software deve
    realizar (por meio da especificação dos requisitos) e a criação de casos de teste capazes de checar se essas funções
    estão sendo executadas corretamente. Apesar da simplicidade da técnica e apesar de sua aplicação ser possível em
    todos os programas cujas funções são conhecidas, não podemos deixar de considerar uma dificuldade inerente: não se
    pode garantir que partes essenciais ou críticas do software serão executadas, mesmo com um bom conjunto de casos de
    teste.

    Um teste funcional não deve ser aplicado simultaneamente em todas as funções do sistema e nem em apenas uma única
    ocasião. Em vez disso, ele deve examinar elementos específicos em ocasiões previamente conhecidas, característica
    que levou esse tipo de teste a ser dividido em subtipos. Alguns exemplos ajudarão a esclarecer essa circunstância:
    quando aplicado para verificar funções de um módulo, função ou classe do sistema, ele recebe a denominação de teste
    de unidade. Já o teste de integração é executado quando se deseja avaliar como as unidades funcionam em conjunto ou
    integradas e o teste de regressão é um subtipo do teste funcional, que visa garantir que uma alteração feita em uma
    função não tenha introduzido outros problemas no código (PRESSMAN; MAXIM, 2016).

    A menção ao quarto subtipo de teste funcional nos dará a oportunidade para o desenvolvimento de um exemplo prático.
    Quando testamos um componente do sistema de modo independente para verificar sua saída esperada, chamamos tal
    procedimento de teste de componentes. Geralmente, ele é executado para verificar a funcionalidade e/ou usabilidade
    de componentes, mas não se restringe apenas a eles. Um componente pode ser qualquer coisa que receba entradas e
    forneça alguma saída, incluindo uma página web, telas e até mesmo um sistema dentro de um sistema maior.

    Como aplicação prática desse teste, imaginemos um sistema de vendas pela internet. Em uma análise mais minuciosa,
    seria possível identificar muitos componentes nessa aplicação, mas escolheremos apenas alguns, os quais estão
    representados na Figura 3.9.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.9 | Componentes de um sistema de vendas pela internet
    Fonte: elaborada pelo autor.

    O componente de login (identificado como componente 1) efetiva a validação de acesso do usuário ao sistema, usando,
    para isso, uma interface específica, que realiza a conexão com o banco de dados. Esse componente dá acesso à
    navegação pelos produtos, à inclusão de itens no carrinho, ao pagamento da compra e à sua confirmação. Para
    efetivação do pagamento, há uma interface que conecta o sistema em teste a um provedor de serviço de pagamentos.
    Considerando esse cenário, vejamos o que deve ser testado em específico no componente 1 (login):

    -> A interface de usuário nos itens de usabilidade e acessibilidade.
    -> O carregamento da página, como forma de garantir bom desempenho da aplicação.
    -> A suscetibilidade a ataques ao banco de dados por meio de elementos da interface de usuário.
    -> A resposta da funcionalidade de login por meio do uso de credenciais falsas e válidas.

    Se considerarmos o componente 3 (adição do produto ao carrinho), o testador deverá verificar o que ocorre, por
    exemplo, quando o usuário coloca um item, o qual supostamente deseja comprar, e fecha aplicação em seguida. Um
    cuidado especial também deverá ser tomado com a comunicação entre o componente 4 e o provedor de serviço de
    pagamento.

    Pelas suas características, o teste de componente nos prepara para o teste que vem a seguir. Se a técnica de teste
    funcional se preocupa com as funções do sistema, qual seria, então, sua diferença para o teste de funcionalidade?
    Os testes de funcionalidades priorizam interações com o usuário e a navegação no sistema e são executados para
    verificar se um aplicativo de software funciona corretamente, de acordo com as especificações do projeto, no que se
    refere à entrada de dados, validação de dados, funções de menu e tudo o que está relacionado à interação do usuário
    com as interfaces. Além das verificações mencionadas, um teste de funcionalidades deve se preocupar também em
    averiguar se funções de “copia e cola” funcionam corretamente e se os ajustes de padrões regionais estão de acordo
    com a localidade em que o software está sendo executado.

    EXEMPLIFICANDO
    Um sistema pode ter sido testado em todas as suas funcionalidades em um determinado país e, ao ser instalado e
    executado em outro, apresentar problemas nas mesmas funcionalidades já testadas. Isso ocorre devido às diferenças de
    formatos nos sistemas métricos e de data implementados em diferentes regiões do planeta. Um campo que exige a
    inclusão de uma data, por exemplo, será testado nos Estados Unidos considerando o formato “mm/dd/aaaa”. Na
    eventualidade de ser executado no Brasil, o programa deverá receber, no campo mencionado, uma data no formato
    “dd/mm/aaaa”, o que certamente causará inconsistência no processamento da informação recebida.

    No escopo da qualidade de software, não há apenas uma acepção relacionada à funcionalidade. Existem as
    funcionalidades do sistema, que são objetos de teste, e a funcionalidade entendida como um atributo fundamental da
    qualidade. Neste segundo caso, trata-se do grau com o que o software satisfaz as necessidades declaradas pelo
    cliente, conforme indicado pelos subatributos de adequabilidade, exatidão, interoperabilidade, conformidade e
    segurança (PRESSMAN; MAXIM, 2016). Em outras palavras, a funcionalidade oferecida pelo sistema não pode ser
    confundida com o grau com que um programa atende a requisitos de adequação ao seu propósito, à sua exatidão e à
    facilidade com que opera com outros sistemas.

    TÉCNICA DE TESTE ESTRUTURAL
    Se voltarmos um pouco no texto e observarmos novamente a Figura 3.7, encontraremos o teste estrutural posicionado na
    mesma dimensão do teste funcional. Essa dimensão, que chamamos de “Como testar”, agrupam técnicas (ou maneiras) de
    se realizar testes. Os testes estruturais (também chamados de caixa branca) são assim conhecidos por serem baseados
    na arquitetura interna do programa. Contando com o código-fonte e com a estrutura do banco de dados, o testador
    poderá submeter o programa a uma ferramenta automatizada de teste. Vale aqui a menção de que um teste funcional
    também pode (e deve) ser realizado de forma automática.

    Há várias ferramentas capazes de realizar testes estruturais, mas não usaremos nenhuma em especial para o nosso
    propósito de detalhar esse teste. Em vez disso, nós nos apoiaremos em uma possível forma de representação do código
    do programa para construir um método de teste. Vamos considerar que, ao analisar o código do programa, nossa
    ferramenta construa uma representação dele, conhecida como grafo. De acordo com Delamaro (2004), em um grafo, os nós
    equivalem a blocos indivisíveis de código, o que, em outras palavras, significa que não existe desvio de fluxo do
    programa para o meio do bloco e, uma vez que o primeiro comando dele é executado, os demais comandos são executados
    sequencialmente. Outro elemento que integra um grafo são as arestas (ou arcos), e eles representam o fluxo existente
    entre os nós. Se considerarmos o código da aplicação que calcula o fatorial de um valor, exibido no Código 3.3,
    teremos que o trecho entre a linha 1 e a linha 8 obedece aos requisitos para se transformar em um nó do grafo.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Código 3.3 | Programa que calcula o fatorial de um número fornecido
    Fonte: elaborado pelo autor.

    #include <stdio.h>
    main()
    {
        int i = 0;
        valor = 0;
        fatorial = 1;
        printf("Programa que calcula o fatorial de um valor informado pelo usuario\n");

        do {
            printf("\nInforme um valor entre 1 e 10: ");
            scanf("%d",&valor);
        } while ((valor<1) || (valor>10));
        for (i=1; i<=valor; i++)
            fatorial=fatorial*i;
        printf("\nO Fatorial de %d = %d", valor, fatorial);
        printf("\n");
    }

    O programa que usaremos para ilustrar um teste estrutural será aquele cujo código pode ser visto no Código 3.4. Sua
    função é a de verificar a validade de um nome de identificador fornecido com base nas seguintes regras:

    -> Tamanho t do identificador entre 1 e 6 (1 <= t <= 6): condição válida.
    -> Tamanho t do identificador maior que 6 (t>6): condição inválida.
    -> Primeiro caractere c é uma letra: condição válida.
    -> Primeiro caractere c não é uma letra: condição inválida.
    -> O identificador possui apenas caracteres válidos: condição válida.
    -> O identificador possui um ou mais caracteres inválidos: condição inválida.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Código 3.4 | Código em C que apura classes válidas e inválidas de identificadores
    Fonte: Delamaro (2004, p. 20).

    /* 01 */ {
    /* 01 */ char achar;
    /* 01 */ int length, valid_id;
    /* 01 */ lenght = 0;
    /* 01 */ printf ("Indentificador");
    /* 01 */ achar = fgetc(stdin);
    /* 01 */ valid_id = valid_s(achar);
    /* 01 */ if (valid_id)
    /* 02 */     lenght = 1;
    /* 03 */ achar = fgetc (stdin);
    /* 04 */ while (achar != '\n')
    /* 05 */ {
    /* 05 */     if (!(valid_f(achar)))
    /* 06 */          valid_id = 0;
    /* 07 */     lenght++;
    /* 07 */     achar = fgetc (stdin);
    /* 07 */ }
    /* 08 */ if (valid_id && (length >= 1) && (lenght < 6))
    /* 09 */     printf ("Valido\n");
    /* 10 */ else
    /* 10 */     printf ("Invalido\n");
    /* 11 */ }

    Quando analisado pela ferramenta de teste, o Código 3.4 será transformado no grafo da Figura 3.10. Note que cada
    trecho identificado com um número no código é representado em um nó no grafo gerado.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.10 | Grafo gerado pela ferramenta de teste estrutural
    Fonte: Delamaro (2004, p. 21).

    Ao testador cabe selecionar casos de teste capazes de percorrer os nós, os arcos e os caminhos representados no
    grafo do programa. Apenas para fins de exemplificação, um caminho que pode ser percorrido pelo fluxo do programa é o
    formado pela sequência de nós 2,3,4,5,6 e 7. Casos de testes diferentes tenderão a exercitar sequências diferentes
    do grafo e, se considerarmos a existência de um conjunto infinito desses casos, teremos que as escolhas incorretas
    podem arruinar o teste. Ainda, se consideramos que os casos de teste são potencialmente infinitos, alguns critérios
    de cobertura do código devem ser previamente definidos, o que nos leva a uma reflexão.

    REFLITA
    Se é certo que um teste, por melhor que seja sua execução e por melhor que tenham sido as escolhas para os casos de
    teste, não conseguirá assegurar que o programa é totalmente livre de defeitos, qual seria a indicação de que é
    chegado o momento de interrompê-lo? A resposta passa pelos critérios de parada da atividade, os quais foram
    estabelecidos previamente e que definiam taxa de cobertura de código e quantidade de casos de teste, por exemplo.

    Feitas essas abordagens, avançamos rumo aos testes de aplicações móveis e web.

    TESTES DE APLICAÇÕES WEB E MÓVEIS
    Houve um tempo em que códigos executáveis desempenhavam suas funções apenas em computadores de grande porte ou nos
    poucos computadores pessoais que existiam. Como os dispositivos móveis eram apenas um sonho, o planejamento e a
    execução dos testes eram atividades adequadas ao perfil dos programas da época e aos equipamentos que os executavam.
    Em nossos dias, no entanto, há dispositivos com uma ampla variedade de aplicações capazes de executar programas para
    as mais variadas finalidades e essa realidade exige algumas adequações nos procedimentos de testes aplicados nas
    plataformas mais comuns.

    A fim de delimitar nosso estudo, trataremos aqui dos testes voltados a aplicações feitas para dispositivos móveis e
    dos testes executados em aplicações para a internet, nessa mesma ordem. Pressman e Maxim (2016) destacam o que
    consideram abordagens de teste especializadas para aplicativos móveis:

    -> Teste de experiência do usuário: ninguém melhor do que um futuro usuário da aplicação móvel para expressar suas
       expectativas de usabilidade e acessibilidade, por exemplo. Se considerarmos uma aplicação móvel de vendas, os
       vendedores deverão ser incluídos no processo de desenvolvimento desde o seu início, para que o nível de
       experiência desejado por eles seja atingido.

    -> Teste de compatibilidade do dispositivo: este item sugere que os testadores devem verificar se o aplicativo móvel
       funciona corretamente com o hardware escolhido para executar o aplicativo.

    -> Teste de desempenho: neste quesito, os testadores devem verificar se indicadores de desempenho exclusivos dos
       dispositivos móveis correspondem à necessidade do cliente. Esses indicadores incluem tempo de download e
       autonomia de carga, por exemplo.

    -> Teste de conectividade: aqui são testados a capacidade da aplicação em realizar conexões em redes de diferentes
       modalidades (ad hoc ou com infraestrutura, por exemplo) e o comportamento da aplicação em caso de queda da
       conexão.

    Essas considerações nos permitem criar um panorama dos testes de aplicações móveis, começando com sua definição: são
    atividades organizadas de teste, executadas com o objetivo de descobrir erros em aspectos fundamentais de seu
    funcionamento em um dispositivo móvel. Esses testes são realizados pelos profissionais técnicos, além dos usuários,
    do cliente e do gerente do projeto. Um teste típico começa por verificar as funções visíveis da aplicação para,
    então, voltar sua atenção para aspectos de infraestrutura e tecnologia. Normalmente, as etapas desse teste incluem
    testes de conteúdo, de interface, de navegação, de componente, de configuração, de desempenho e de segurança.

    ASSIMILE
    O teste de aplicativos móveis é um conjunto de atividades relacionadas com um único objetivo: descobrir erros no
    conteúdo, na função, na usabilidade, na navegabilidade, no desempenho, na capacidade e na segurança do aplicativo
    móvel. Para tanto, deve ser executada uma estratégia de teste que abrange as revisões e o teste executável
    (PRESSMAN; MAXIM, 2016).

    Como qualquer teste, temos aqui também a necessidade de apurar se o processo foi corretamente desempenhado. Como não
    é possível aplicar absolutamente todas as possibilidades existentes de entradas, nem apurar todas as situações que
    podem ocorrer durante o uso da aplicação, novamente os critérios de parada serão o parâmetro para o fim dos testes.

    Outro elemento que demanda providências específicas durante o processo de teste são as aplicações web. Da mesma
    forma que em qualquer outro teste, aqui também estamos diante da missão de executar um sistema para encontrar e
    corrigir defeitos. No entanto, as aplicações web podem operar em conjunto com diferentes sistemas operacionais,
    navegadores, protocolos de comunicação e plataformas de hardware, o que pode representar dificuldades adicionais na
    busca por defeitos. Com essas especificidades, os seguintes elementos de qualidade devem ser testados (PRESSMAN;
    MAXIM, 2016):

    -> Conteúdo da aplicação: deve ser avaliado em dois níveis:
        Sintático: neste nível devem ser avaliadas a ortografia, a pontuação e a gramática do conteúdo textual da
                   aplicação web.

        Semântico: aqui devem ser avaliadas a exatidão, a consistência e a ausência de ambiguidade da informação.

    -> Funcionalidades da aplicação: são testadas para fins de descoberta de problemas que colocam a ferramenta em
       situação de não conformidade com os requisitos do cliente.

    -> Estrutura da aplicação: a facilidade com que a estrutura da aplicação pode crescer e, ainda assim, passar por
       manutenções é testada neste elemento.

    -> Usabilidade: testes são feitos para que vários perfis de usuários possam se adaptar às características da
       interface da aplicação.

    -> Navegabilidade: atenção especial é dedicada a links inativos e incorretos neste elemento

    Adicionalmente, desempenho, interoperabilidade e segurança também recebem atenção especial em um teste de aplicação
    web.

    TESTES DE APLICAÇÕES ORIENTADAS A OBJETOS
    Seguindo nosso caminho pelos testes feitos em aplicações ou paradigmas específicos, chegamos até as aplicações
    Orientadas a Objetos (OO). Por causa das características próprias dos programas OO, os testes aqui aplicados devem
    considerar a existência de subsistemas em camadas que encapsulam outras classes. De acordo com Pressman e Maxim
    (2016), é preciso testar um sistema OO em vários níveis diferentes, de modo que erros eventualmente ocorridos
    durante as interações entre as classes sejam descobertos. Ainda de acordo com os autores, três providências básicas
    são necessárias para se testar adequadamente um sistema OO:

    -> A definição do teste deve ser ampliada para incluir as técnicas da descoberta de erros aplicadas à análise
       orientada a objetos e aos modelos do projeto.

    -> A estratégia para teste de unidade e de integração deve ser alterada significativamente.

    -> O conjunto de casos de teste devem levar em conta as características especiais do paradigma de Orientação a
       Objetos.

    Uma análise mais minuciosa da primeira providência pode nos levar a uma aparente inconsistência: como é possível que
    aspectos da análise orientada a objetos e modelos do projeto sejam testados? De fato, no sentido convencional, não
    podem. Ocorre que a criação de uma aplicação OO começa com a criação de modelos de análise e de projeto, os quais
    começam com representações quase informais dos requisitos e se tornam modelos detalhados de classes e de suas
    relações conforme o desenvolvimento avança. Por isso, em cada estágio da sua evolução, esses modelos devem ser
    revisados para que erros sejam descobertos logo em fases iniciais do desenvolvimento (PRESSMAN; MAXIM, 2016).

    Entre os vários benefícios trazidos pela adoção da Orientação a Objetos para o desenvolvimento de software, está o
    fato de que esse paradigma reduz a necessidade de testes, segundo Schach (2009). O autor complementa que a
    reutilização de código via herança é um dos fatores que torna essa característica ainda mais forte: em tese, uma vez
    que a classe mãe tenha sido testada, as classes provenientes dela não precisam ser novamente testadas. Quando os
    desenvolvedores inserem novos métodos na subclasse de uma classe já testada, é natural que eles precisem ser
    testados. No entanto, métodos herdados não precisam de teste adicional.

    Por mais lógicas e confiáveis que nos pareçam, essas afirmações precisam ser analisadas com um certo cuidado. Para
    começar, a classe é um tipo de dado abstrato e o objeto é a instância de uma classe. Esse fato nos induz ao
    raciocínio de que uma classe não tem uma realização concreta e que, portanto, não é possível aplicar testes baseados
    em execução (ou seja, aqueles que temos abordado nesta unidade) diretamente nela. Outra característica da Orientação
    a Objetos que tem efeitos em um teste é quantidade normalmente elevada de métodos em um objeto que, ao invés de
    retornarem um valor para o chamador, simplesmente alteram o estado do objeto ao modificarem seus atributos. Segundo
    Schach (2009), a dificuldade, nesse caso, é a de testar se a alteração de estado foi realizada corretamente.

    Tomemos a seguinte situação como exemplo: uma aplicação bancária possui um método chamado deposito, cujo efeito é o
    de aumentar o valor da variável de estado chamada saldoDaConta. No entanto, como consequência do ocultamento de
    informações, a única maneira viável de se testar se o método deposito tem uma execução correta é pela invocação de
    um outro método, chamado determinarSaldo, tanto antes como depois da chamada do método deposito, a fim de verificar
    como a mudança do saldo se dá.

    Outro aspecto a ser analisado é a necessidade de aplicação de um novo teste em métodos herdados. Observe a
    hierarquia de classes ilustrada no trecho de código contido no Código 3.5. Na primeira classe (ClasseArvoreComRaiz),
    são definidos dois métodos: o que exibe o conteúdo de um nó e a rotina de impressão, utilizada pelo método
    exibeConteudoNo.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Código 3.5 | Ilustração de uma hierarquia de classes em Java
    Fonte: adaptado de Schach (2009).

    class ClasseArvoreComRaiz {
        void exibeConteudoNo (No a);
        void rotinaImpressao (No b);
        // o método exibeConteudoNo usa o método rotinaImpressao
    }

    class ClasseArvoreBinaria extends ClasseArvoreComRaiz {
        void exibeConteudoNo (No a);
        // o método exibeConteudoNo definido aqui usa
        // o método rotinaImpressao herdado de ClasseArvoreComRaiz
    }

    class ClasseArvoreBinariaBalanceada extends ClasseArvoreBinaria {
        void rotinaImpressao (No b);
        // o método exibeConteudoNo (herdado de ClasseArvoreBinaria)
        // usa essa versão local de rotinaImpressao dentro da classe
        // ClasseArvoreBinariaBalanceada
    }

    Observe que a subclasse ClasseArvoreBinaria herda o método rotinaImpressao da classe mãe chamada
    ClasseArvoreComRaiz. Além disso, o método exibeConteudoNo é novamente definido nessa subclasse, o que anula o mesmo
    método definido na classe ClasseArvoreBinaria. Já a subclasse ClasseArvoreBinariaBalanceada herda o método
    exibeConteudoNo da superclasse ClasseArvoreBinaria. No entanto, nela é definido um novo método, o rotinaImpressao,
    que anula aquele definido em ClasseArvoreComRaiz. Quando o método exibeConteudoNo usa o método rotinaImpressao no
    contexto de ClasseArvoreBinariaBalanceada, as regras do Java especificam que a versão local de rotinaImpressao deve
    ser usada e, em consequência disso, o código real do método rotinaImpressao, executado quando exibeConteudoNo é
    chamado no contexto da instanciação da classe ClasseArvoreBinaria, é diferente daquele executado quando esse mesmo
    método é executado na instanciação de ClasseArvoreBinariaBalanceada. Esse fenômeno ocorre normalmente apesar de o
    método exibeConteudoNo ser herdado sem modificação, o que acarreta a necessidade do novo teste (SCHACH, 2009).

    Também considerando características próprias de sistemas Orientados a Objetos, Masiero et al. (2015) dividem o
    procedimento de testes em três fases:

    -> Teste de unidade: Os autores consideram que as menores unidades a serem testadas em um programa OO são os métodos
                         . Por isso, indicam que o teste de unidade consiste no teste de cada método de forma isolada,
                         o que também é chamado de teste intra-método.

    -> Teste de módulo: Trata-se do teste de um conjunto de unidades que interagem entre si por meio de chamadas. Essa
                        fase pode ainda ser assim dividida:

        Inter-método: aplicação de teste nos métodos públicos de uma classe, em conjunto com os outros métodos da mesma
                      classe.

        Intra-classe: consiste em testar as interações entre os métodos públicos de uma classe quando chamados em
                      diferentes sequências.

        Inter-classe: consiste em testar as interações entre classes diferentes.

    -> Teste de sistema: consiste em testar a integração entre todos os módulos, o que equivale a um sistema completo.
                         Para esta fase geralmente é usado o teste funcional.

    SAIBA MAIS
    Os testes de sistema e de usuário são executados nas etapas finais de seus respectivos níveis e são considerados de
    elevada importância na apuração consolidada de qualidade.

    Teste de sistema

    -> O teste de sistema deve ser apresentado como uma etapa em que o sistema, já completamente integrado, passa pelo
        procedimento do teste.

    -> Para que a equipe consiga chegar ao teste de sistema, todas as unidades e as integrações entre elas devem ter
       sido testadas previamente. Os erros encontrados devem ter sido também sanados.

    -> Mesmo depois de testada cada unidade isoladamente e a comunicação entre as unidades, é necessário ainda testar o
       funcionamento do sistema de modo global, adotando o ponto de vista de quem usará o sistema. O objetivo do teste
       de sistema é o de apurar se o programa é capaz de executar processos completos, como se estivesse em uso pleno.

    Teste de usuário

    -> Aplicado o teste de sistema, o produto final deve ser aceito pelo usuário. Como o nome sugere, esse teste é
       executado pelo usuário e não pela equipe de testadores ou desenvolvedores. Em relação ao planejamento e à
       execução, o teste de usuário se equipara ao teste de sistema, com a diferença de que ele será executado pelo
       usuário. Se considerarmos que o teste de sistema ainda é parte da verificação do produto, o teste de aceitação
       serve para sua validação.

    -> O teste de usuário tem objetivo e metodologia de aplicação semelhantes ao teste de sistema, com a diferença de
       que ele é executado pelo usuário, como se estivesse operando-o em situação normal de uso. A elaboração de um
       roteiro de funções a serem testadas é aconselhada.

    PESQUISE MAIS
    A obra de Roger Pressman e Bruce Maxim (PRESSMAN; MAXIM, 2016) oferece um bom conteúdo com relação a teste de
    usuário e de sistema e, quanto a este último, posiciona-o como o último nível de teste em relação à estratégia de
    teste. Essa contextualização é feita em figura da página 470.

    PRESSMAN, R.; MAXIM, B. Engenharia de Software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.

    O vídeo chamado Como são feitos os testes de usuário fornece dicas sobre como aplicar testes de usuários, incluindo
    o direcionamento do usuário para o teste.

    COMO são feitos os testes de usuário? [S.l.: s.n.], 2018. 1 vídeo (4 min). Canal Alura Cursos Online

    O vídeo chamado Teste de Integração e Teste de Sistema detalha como eles são feitos e como se relacionam. Para
    cumprir com a finaliade deste quadro, deve-se dar maior atenção ao teste de sistema.

    TESTES de Integração e Teste de Sistema. [S.l.: s.n.], 2018. 1 vídeo (12 min). Canal Eduardo Engelharia de Software.

    Este foi, portanto, o conteúdo preparado para esta seção. Durante seu desenvolvimento, você teve contato com as
    técnicas de teste funcional e estrutural e com outros tipos de testes específicos para determinadas aplicações e
    paradigmas de desenvolvimento. Tivemos a oportunidade de desenvolvermos juntos um exemplo de teste estrutural
    baseado na criação de um grafo, que representava o código apresentado. Embora simples, o exemplo nos mostrou como a
    técnica funciona e quão importante é a correta escolha dos casos de teste. Não deixe de se aprofundar neste assunto
    e torne-o logo uma boa referência em testes de software. Até a próxima!

    #ref Unidade 3 - Seção 2
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    BARTIÉ, A. Garantia da Qualidade de Software: As melhores práticas de Engenharia de Software aplicadas à sua
    empresa. Rio de Janeiro: Elsevier, 2002.

    BRAGA, P. H. Testes de Software. São Paulo: Pearson Educational do Brasil, 2016.

    COMO são feitos os testes de usuário? [S.l.: s.n.], 2018. 1 vídeo (4 min). Canal Alura Cursos Online. Disponível em:
    https://bit.ly/3sYiSlD. Acesso em: 24 dez. 2020.

    DELAMARO, M. E. Introdução ao teste de software. Rio de Janeiro: Elsevier, 2004.

    MASIERO, P. C., LEMOS, O. A. L, FERRARI, F. C., MALDONADO, J. C. Teste de software orientado a objetos: teoria e
    prática. ResearchGate, [S.l.], 2015. Disponível em: https://bit.ly/3iRA1ZR. Acesso em: 24 dez. 2020.

    PRESSMAN, R.; MAXIM, B. Engenharia de Software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.

    SCHACH, S. R. Engenharia de Software: os Paradigmas Clássico e Orientado a Objetos. 7. ed. São Paulo: McGraw-Hill,
    2009.

    TESTES de Integração e Teste de Sistema. [S.l.: s.n.], 2018. 1 vídeo (12 min). Canal Eduardo Engelharia de Software.
    Disponível em: https://bit.ly/39knSsX. Acesso em: 24 dez. 2020.
    """


def unidade3_secao3():
    """
    ----------------------------------------------- UNIDADE 3 / SEÇÃO 3 -----------------------------------------------
    DESENVOLVIMENTO ORIENTADO A TESTES E FERRAMENTAS - Roque Maitino Neto

    CONCEITO-CHAVE
    Tivemos a oportunidade de conhecer técnicas e metodologias de teste que se baseavam em uma sequência bem
    estabelecida de procedimentos e que eram capazes de acomodar as particularidades de alguns tipos específicos de
    aplicações. Essa sequência foi assim apresentada:

    -> Implementar código.
    -> Selecionar casos de teste.
    -> Executar o código com os casos de teste selecionados.
    -> Depurar o código para encontrar defeitos.
    -> Corrigir defeitos.
    -> Avaliar resultados.

    Considerando o momento da aplicação dos testes, a fase em que ela ocorre é, tradicionalmente, uma das últimas do
    processo de software, logo após o completo desenvolvimento do produto e antes da entrega ao cliente. Via de regra,
    qualquer atraso ocorrido durante o projeto impactará no tempo disponível para os testes. Haveria então outro momento
    mais adequado para aplicá-los? Será que a prática do teste também não teria experimentado uma evolução, impulsionada
    pelo aprimoramento das metodologias de desenvolvimento? Felizmente a resposta é sim para ambas as questões.

    DESENVOLVIMENTO ORIENTADO A TESTES (TDD)
    O advento das metodologias ágeis, especificamente o Extreme Programming (XP), ofereceu-nos inovações também no modo
    como fazemos nossos testes, sendo a mais importante delas o TDD. De acordo com Aniche (2014), a ideia central do TDD
    é a de fazer com que o desenvolvedor escreva testes automatizados de maneira constante ao longo do processo de
    desenvolvimento e antes mesmo da implementação do código. Ainda segundo o autor, essa inversão no ciclo compele o
    desenvolvedor a escrever um código de melhor qualidade, já que a escrita de bons testes de unidade requer o bom uso
    dos recursos da orientação a objetos.

    Antes de continuarmos a exploração deste conteúdo, será necessário resgatarmos alguns termos já citados para
    fazermos uma delimitação do nosso tema. O Desenvolvimento Orientado a Testes será abordado aqui como uma das
    práticas do XP e, nessa condição, usaremos o teste de unidade como nosso objeto de análise. O fato de o TDD estar
    situado no contexto do XP explica nossa menção ao paradigma de Orientação a Objetos feita há pouco. Por fim, vale
    relembrarmos que o teste de unidade é aquele realizado sobre cada classe do sistema e que os testes de aceitação
    são efetuados sobre cada estória (ou funcionalidade) do sistema (TELES, 2004).

    EXEMPLIFICANDO
    A ilustração de um teste de unidade será oferecida por meio do exemplo de uma loja virtual qualquer na web. Quando o
    usuário seleciona um produto para comprá-lo, o sistema se incumbe de colocá-lo no carrinho de compras, de fazer
    contato com a operadora do cartão de crédito, de retirar o produto do estoque, de informar o pessoal da logística
    para preparar a entrega e de enviar ao usuário um e-mail de confirmação de compra. É natural imaginarmos que o
    sistema que gerencia todas essas operações (mais aquelas que não mencionamos) seja bastante complexo e que,
    portanto, esteja implementado em diversas classes, cada qual com uma função específica.

    Ao invés de focar o sistema todo_, o teste de unidade se preocupará com cada uma dessas classes, que geralmente é a
    unidade de um sistema Orientado a Objetos. Em nosso sistema de exemplo, muito provavelmente existem classes como
    CarrinhoDeCompras, Pedido e assim por diante. A ideia é termos baterias de testes de unidade separadas para cada uma
    dessas classes, com cada bateria preocupada apenas com a sua classe (ANICHE, 2014).

    Bem, e como o Desenvolvimento Orientado a Testes funciona? Descobriremos isso ao longo desta primeira etapa da seção
    e a iniciaremos pela apresentação de uma figura que se tornou referência universal quando se trata desse assunto. A
    aplicação do Desenvolvimento Orientado a Testes é ilustrada pelo ciclo Vermelho-Verde-Refatorar, mostrado na Figura
    3.11.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.11 | Ciclo Vermelho-Verde-Refatorar
    Fonte: adaptada de Qiu (2018).

    Essa representação pode ser traduzida de modo textual da seguinte forma:

    1. Na primeira fase do ciclo, o desenvolvedor escreve um teste que intencionalmente falhará. O código em que ele
       está inserido provavelmente sequer compilará.

    2. Na sequência, o desenvolvedor escreve um código – referente a uma nova funcionalidade do sistema – que fará o
       teste escrito na etapa anterior passar.

    3. Como última dessas três etapas, o desenvolvedor aplicará a refatoração no código, eliminando eventuais
       duplicidades, estruturando melhor o código, mudando o nome de variáveis, entre outras providências.

    Embora essa ilustração nos dê ideia de um ciclo, ela não deixa claro como ele se efetiva, principalmente para quem
    se propõe a usar o TDD pela primeira vez. A Figura 3.12 nos oferece visão detalhada do procedimento. Na verdade, o
    TDD contém duas partes: implementação rápida e refatoração e, na prática, o teste para implementação rápida não se
    limita ao teste de unidade. Pode ser um teste de aceitação também.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.12 | O procedimento de TDD em detalhes
    Fonte: adaptada de Qiu (2018).

    Observe que, na parte de implementação rápida, o procedimento executado pelo desenvolvedor é visualmente descrito da
    mesma forma que o fizemos textualmente, ou seja, (1) o desenvolvedor escreve um teste que deverá falhar e (2)
    verifica se, de fato, o teste falha. Caso não falhe, o teste deverá ser reescrito. Caso falhe, (3) o desenvolvedor
    deverá escrever o código para que ele passe. Neste ponto um registro deve ser feito: a expressão “código suficiente”
    indica que o desenvolvedor só deverá codificar o suficiente para que o teste passe, nem mais, nem menos. Quando o
    teste passa, a parte da refatoração começa e, como primeira providência dessa etapa, (4) o desenvolvedor deve
    verificar se todos os testes passam e (5) aplicar a refatoração no código. Caso um ou mais testes falhem, (5’) eles
    devem ser atualizados e eventuais correções devem ser feitas. A seta com a legenda de “Iterações” indica que esse
    procedimento deve ser executado até o fim do procedimento.

    REFLITA
    No início do desenvolvimento desse tema, foi mencionado que o teste de unidade seria utilizado como o meio de
    aplicar o TDD. Em relação a essa colocação, vale a reflexão: essa forma de aplicar testes estaria limitada ao teste
    de unidade apenas? Na verdade, a aplicação do teste de aceitação pode ser uma ideia melhor, pois garante que o
    desenvolvedor está fazendo a coisa certa já na primeira vez. Devemos nos lembrar de que os testes de aceitação
    representam a perspectiva do usuário final e, por isso, um teste de aceitação que passa é a garantia de que o
    código atende aos requisitos de negócios. Em consequência, esse fato pode ajudar o desenvolvedor a não perder seu
    tempo de forma desnecessária.

    Neste ponto cabe um exemplo da aplicação do TDD e novamente usaremos a loja de comércio eletrônico para
    desenvolvê-lo, segundo Aniche (2014). A classe exibida no código do Código 3.7 aponta o produto de maior valor e o
    produto de menor valor no carrinho e o faz percorrendo a lista de compras e comparando valores.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Código 3.7 | Classe que retorna o produto de maior valor e de menor valor
    Fonte: Aniche (2014, [s.p.]).

    public class MaiorEMenor {
        private Produto menor;
        private Produto maior;
        public void encontra (CarrinhoDeCompras carrinho) {
            for (Produto produto : carrinho.getProdutos()) {
                if (menor == null || produto.getValor() < menor.getValor()) {
                    menor = produto
                }
                else if (maior == null || produto.getValor() > maior.getValor()) {
                    maior = produto;
                }

                }
            }
        }
        public Produto getMenor() {
            return menor;
        }
        public Produto getMaior() {
            return maior;
        }
    }

    O método encontra() recebe um CarrinhoDeCompras e percorre a lista de produtos desse carrinho, comparando sempre o
    produto atual com o menor e maior já encontrados. Ao final da execução, temos nos atributos maior e menor os
    produtos desejados. O Código 3.8 exemplifica o uso da classe MaiorEMenor. Observe que o carrinho contém três itens:
    o que tem preço menor é o jogo de pratos e o que tem preço maior é a geladeira. Ao executar essa aplicação, a saída
    será:

    O menor produto: jogo de pratos
    O maior produto: geladeira.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Código 3.8 | Classe que utiliza a classe MaiorEMenor
    Fonte: Aniche (2014, [s.p.]).

    public class TestaMaiorEMenor {
    public static void main(String[] args) {

    CarrinhoDeCompras carrinho = new CarrinhoDeCompras();
    carrinho.adiciona(new Produto("Geladeira", 450.0));
    carrinho.adiciona(new Produto("Liquidificador", 250.0));
    carrinho.adiciona(new Produto("Jogo de pratos", 70.0));

    MaiorEMenor algoritmo = new MaiorEMenor();
    algoritmo.encontra(carrinho);

    System.out.println("O menor produto: " + algoritmo.getMenor().getNome());
    System.out.println("O maior produto: " + algoritmo.getMaior().getNome());
        }
     }
    }

    Sendo assim, podemos concluir que a aplicação funciona, certo? Ainda não. Precisamos verificar se ela funciona
    também em outro cenário. Se o código do desenvolvedor fizesse a inserção dos mesmos produtos em ordem diferente
    (geladeira, liquidificador e jogo de pratos), a saída gerada seria a seguinte:

    menor produto: jogo de pratos.

    Exception in thread "main" java.lang.NullPointerException at TestaMaiorEMenor.main(TestaMaiorEMenor.java:5).

    É fato que, se os produtos forem adicionados em ordem decrescente, a classe não retorna a saída esperada e o cliente
    não conseguirá efetuar sua compra. Essa situação nos leva a duas conclusões:

    1.Testar constantemente, considerar vários cenários e repetir o procedimento a cada mínima alteração feita são
    providências indispensáveis em um procedimento de teste.

    2. Proceder manualmente (ou seja, sem uma ferramenta de teste), conforme determina o item anterior, é impraticável.

    Ainda nesta seção trataremos de testes automatizados de software como forma de apresentarmos uma solução possível
    para este caso. Antes, porém, colocaremos como tema algumas questões sobre o teste de unidade e seu gerenciamento,
    sempre no âmbito do Desenvolvimento Orientado a Testes, e, na sequência, será apresentada uma solução viável para a
    situação que acabamos de tratar.

    GERENCIAMENTO DE TESTES
    Na maioria dos casos, criar testes antes para codificar depois não é exatamente o modelo de desenvolvimento com o
    qual um profissional de TI está acostumado. Como se a falta de familiaridade com esse estilo não fosse obstáculo
    importante o suficiente, há questões relacionadas ao teste de unidade que demandarão o devido gerenciamento por
    parte de quem estiver à frente deles. É bom lembrarmos que o teste de unidade é o elemento central do TDD, embora
    ele possa ter como objeto também o teste de aceitação. Na visão de Teles (2004), as situações a seguir requerem bom
    gerenciamento para que a condução do TDD seja satisfatória.

    Como escrever testes quando o sistema faz acesso a um banco de dados?
    Nesta questão, o desempenho é um aspecto a ser seriamente considerado no procedimento de teste. É necessário que os
    testes de unidade sejam executados muito rapidamente, de modo que o ciclo “testar-codificar-refatorar” seja
    completado também rapidamente. O desempenho do teste será tanto mais significativo quanto mais numerosas forem as
    classes que acessam um banco de dados. O gerenciamento da situação inclui fazer com que uma boa quantidade de testes
    que usam dados do banco passe a acessar arquivos na memória volátil, em vez de o fazerem no registro em disco. Uma
    boa alternativa seria escrever uma classe “falsa”, que atuasse como um banco de dados, interceptando os comandos SQL
    enviados pela aplicação. Embora essa solução seja viável, em algum momento o acesso ao banco real deverá ser testado
    , mas o bom gerenciamento da situação deverá providenciar que tais acessos sejam feitos com a menor frequência
    possível.

    O que o desenvolvedor deve fazer quando não tiver ideia de como testar uma classe?

    Embora a condução dessa situação esteja diretamente relacionada à classe específica, ainda assim é natural imaginar
    que estamos diante de uma classe problemática. Se a instanciação da classe é feita de forma complexa, é provável que
    um padrão viável de codificação não foi seguido, o que torna aconselhável a revisão do código. Se a classe sob teste
    colabora com diversas outras classes de complexidade elevada, a providência deverá passar pela criação de mock
    objects, definidos como objetos falsos, os quais simulam o comportamento de objetos reais e mais complexos.

    ASSIMILE
    O termo mock objects (ou objeto de simulação, em língua portuguesa) é utilizado para descrever um caso especial de
    objetos que imitam objetos reais para teste. Eles podem ser criados através de frameworks que facilitam bastante o
    processo de criação. Praticamente todas as principais linguagens possuem frameworks disponíveis para a criação de
    mock objects (MEDEIROS, 2014).

    O gerenciamento dessa situação passa por reuniões com a equipe de desenvolvedores sobre o que tem sido difícil
    submeter ao TDD.

    Como saber se foi testado tudo o que poderia dar errado?

    As características de bom senso e de experiência são componentes desta questão. Quando o sistema manifesta um erro
    no teste de aceitação, há boa chance de estar faltando um teste de unidade. Ao escrever esse teste, o desenvolvedor
    deve ser orientado a lembrar-se de outros testes que pode não ter escrito e essa providência tenderá a torná-lo mais
    desenvolto na questão da completude dos testes.

    Os desafios que envolvem o TDD não se resumem a esses que abordamos. Será normal nos depararmos com quem presume ser
    esta uma metodologia que aumenta o trabalho da equipe de desenvolvimento. No entanto, como o TDD prevê que os testes
    devem ser escritos antes da efetiva codificação, a simplificação da implementação das classes deverá ser um dos bons
    efeitos desse estilo de desenvolvimento. Como não podemos nos esquecer de que estamos tratando de uma prática do XP,
    é necessário mencionar que a programação em par constitui um ponto altamente positivo quanto à celeridade da
    construção dos testes, justamente pela forte interação que se estabelece entre o par.

    Embora a condução dessas questões deva estar sempre na ordem do dia dos gestores envolvidos em testes, o
    gerenciamento do processo de teste envolve outros elementos procedimentais e outras ações, já introduzidas em
    conteúdos anteriores, quando tratamos de planos de testes. Cabe-nos, portanto, fazer alguns resgates de conceitos
    pontuados naquela seção e apresentar uma ferramenta de gerenciamento de teste bastante utilizada: a TestLink. Antes
    de tratarmos especificamente dela, vale a observação de que não apenas o procedimento de teste deve ser
    automatizado, como teremos oportunidade de constatar na sequência. O gerenciamento desse procedimento, por meio de
    uma ferramenta, implica facilidades que vão desde o cadastramento de projetos de teste até a designação dos
    testadores responsáveis por um conjunto de testes.

    A apresentação da TestLink tem início pela menção de que se trata de uma ferramenta open source automatizada escrita
    em PHP e com interface web, cujo principal objetivo é dar suporte às atividades de gestão de testes, permitindo a
    criação de planos de testes e a geração de relatórios com diversas métricas para o acompanhamento da execução deles.
    Por meio dessa ferramenta, é possível associar casos de teste a requisitos específicos do produto (CAETANO, [s.d.])

    O download da ferramenta deve ser feito no site TestLink (TESTLINK, [s.d.]) e, em vez de apresentarmos aqui os
    procedimentos de instalação, apresentaremos algumas telas da versão 1.9.13, que reproduzem a criação de um plano de
    testes, segundo Reis (2018). A Figura 3.13 exibe a tela de login da ferramenta.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.13 | Tela de login da TestLink
    Fonte: Reis (2018, [s.p.]).

    Após obter acesso à ferramenta, seu usuário poderá criar um Projeto de Teste clicando no link Gerenciar Projeto de
    Teste, conforme exibido na Figura 3.14.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.14 | Criação de um Projeto de Teste
    Fonte: Reis (2018, [s.p.]).

    A partir dessa escolha, o usuário terá acesso ao formulário de criação do Projeto de Teste, por meio do qual poderá
    informar um nome, a descrição do projeto e habilitar algumas funcionalidades, incluindo a possibilidade de
    automatizar o teste. A ferramenta deverá, então, habilitar o gerenciamento do plano de teste e, nesse contexto, uma
    baseline/release do projeto poderá criada. A Figura 3.15 exibe o resultado dessa criação e as orientações fornecidas
    pela ferramenta.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.15 | Criação da baseline/release do projeto
    Fonte: Reis (2018, [s.p.]).

    Seguindo esse mesmo padrão procedimental e visual, a ferramenta também permite o registro de requisitos e de casos
    de teste, sempre associados ao projeto atual. Na Figura 3.16, é possível visualizar o contexto de especificação de
    requisitos do software.

    Figura 3.16 | Criação da especificação de requisitos
    Fonte: Reis (2018, [s.p.]).

    Embora a TestLink ofereça inúmeras outras funcionalidades, fica claro que se trata de um recurso extremamente
    valioso nos casos em que vários processos de teste estão sendo executados simultaneamente. À propósito, já que
    mencionamos algo valioso, que tal estudarmos os procedimentos e os benefícios de um teste automático? Siga conosco.

    TESTES AUTOMATIZADOS DE SOFTWARE
    Em momentos anteriores desta seção, esclarecemos, por meio de um exemplo, que testar uma unidade considerando vários
    cenários e por diversas vezes é uma ação fundamental para a obtenção da desejada qualidade do produto. Embora esta
    seja uma necessidade, não se pode atendê-la apenas contando com o empenho humano. É preciso automatizar o teste.
    Teles (2004) ensina que os testes de unidade são automatizados na forma de classes do sistema, as quais têm como
    objetivo testar outras classes. O autor complementa que, de modo geral, para cada classe do sistema deverá existir
    uma outra com o único objetivo de testá-la e que esse é o passo inicial para que seja possível automatizar os testes
    de unidade.

    De fato, automatizar o processo reduz o custo e o tempo do teste, se é que podemos separar esses dois fatores.
    Aniche (2014) afirma que escrever um teste automatizado não é tarefa complexa, pois se assemelha a um teste manual.
    Para validarmos essa afirmação, voltemos à aplicação de comércio eletrônico. Dessa vez, o desenvolvedor precisa
    testar o carrinho da loja virtual e, para este exemplo, consideraremos que há dois produtos cadastrados na loja. Ao
    simular o comportamento de um cliente, ele seleciona os dois produtos, segue para o carrinho de compras e finalmente
    verifica a quantidade de itens existentes nele. Essa quantidade deve ser dois e o valor da compra deve ser a soma
    dos valores dos dois produtos.

    O que esse desenvolvedor fez foi imaginar um cenário (a compra de dois produtos), executar uma ação (colocá-los no
    carrinho) e verificar o resultado (checar a quantidade e o valor dos itens comprados). Em um teste automatizado de
    software, a sequência a ser cumprida deverá ser exatamente essa e a intervenção humana fica restrita, neste caso
    específico, à conferência do valor obtido com o valor esperado. Com um breve retorno ao Código 3.8 , veremos que
    aquela classe monta um cenário (um carrinho de compras com três produtos), executa uma ação (chama o método
    encontra()), e valida a saída, que significa imprimir o maior e o menor produto. A simples execução da classe monta
    o cenário e executa a ação, sem intervenção do desenvolvedor (ANICHE, 2014).

    Embora já tenhamos automatizado duas das três etapas da sequência, ainda será necessário tornar a conferência da
    saída independente da intervenção humana. A plena automatização do teste virá com a utilização do JUnit, o framework
    de testes de unidade do Java, que funciona em conjunto com o IDE Eclipse. A adaptação do nosso código ao JUnit será
    simples e atingirá a parte da validação, na qual os métodos do framework serão invocados para que comparem o
    resultado esperado com o obtido. O método Assert.assertEquals() fará esse trabalho. O Código, 3.9, mostra a classe
    TestaMaiorEMenor ajustada para funcionamento do JUnit. Como sabemos, esse teste falhará, pois há um defeito na
    classe MaiorEMenor, instanciada pela TestaMaiorEMenor. A presença do else naquele código não permite que o segundo
    if seja executado e, portanto, o maior elemento nunca é verificado. Com esse defeito corrigido, o teste passará.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Código 3.9 | Código adequado para teste no JUnit
    Fonte: Aniche (2014, [s.p.]).

    import org.junit.Assert;
    import org.junit.Test;
    public class TestaMaiorEMenor {
       @Test
       public void ordemDecrescente() {
        CarrinhoDeCompras carrinho = new CarrinhoDeCompras();
           carrinho.adiciona(new Produto("Geladeira", 450.0));
           carrinho.adiciona(new Produto("Liquidificador", 250.0));
           carrinho.adiciona(new Produto("Jogo de pratos", 70.0));

            MaiorEMenor algoritmo = new MaiorEMenor();
            algoritmo.encontra(carrinho);
            Assert.assertEquals("Jogo de pratos", algoritmo.getMenor().getNome());
            Assert.assertEquals("Geladeira", algoritmo.getMaior().getNome());
        }
    }

    Dessa forma é que um teste automatizado se efetiva. Naturalmente que a complexidade, a quantidade e o tamanho das
    classes tornarão os testes mais ou menos complexos, mas a forma geral não se altera significativamente. A agilidade
    no procedimento, a redução de custos e a capacidade de o teste ser repetido quantas vezes forem necessárias são
    apenas algumas poucas vantagens da automação.

    SAIBA MAIS
    Neste quadro trataremos de algumas anotações do JUnit úteis para a organização e para a execução dos procedimentos
    de teste em classes Java.

    @Test: usada para sinalizar que o método anotado é um método de teste.

    @AfterAll: usada para sinalizar que o método anotado deve ser executado após todos os testes na classe de teste
               atual.

    @AfterEach: usada para sinalizar que o método anotado deve ser executado após cada método @Test, @RepeatedTest,
    @ParameterizedTest, @TestFactory e @TestTemplate na classe de teste atual.

    @BeforeAll: usada para sinalizar que o método anotado deve ser executado antes de todos os testes na classe de teste
    atual.

    @BeforeEach: usada para sinalizar que o método anotado deve ser executado antes de cada método @Test, @RepeatedTest,
    @ParameterizedTest, @TestFactory e @TestTemplate na classe de teste atual.

    @RepeatedTest: usada para sinalizar que o método anotado é um método de modelo de teste que deve ser repetido um
    número específico de vezes com um nome de exibição configurável.

    Antes de terminarmos esta seção, cabe ainda uma questão: com tantas vantagens e recursos interessantes, só temos uma
    ferramenta de automação de testes disponível?

    FERRAMENTA PARA TESTES DE SOFTWARE
    Por meio do exemplo de teste automatizado que acabamos de desenvolver, você teve contato com uma das mais conhecidas
    e utilizadas ferramentas de teste que existem: a JUnit. No entanto, ela está longe de ser a única e, dada a
    importante função técnica exercida por essas ferramentas, dedicaremos as próximas linhas à explanação de uma delas.

    SELENIUM
    Trata-se de uma ferramenta de testes open source, multiplataforma e com várias frentes de utilização, especialmente
    em testes de aplicações web. O site oficial da ferramenta (SELENIUM, [s.d.]) apresenta três projetos e indica o mais
    apropriado para cada aplicação.

    Selenium WebDriver: indicado para quem deseja criar testes automatizados em aplicações baseadas em navegador. O
    Selenium WebDriver é capaz de automatizar interações com a maioria dos navegadores, tanto local quanto remotamente e
    realizar a simulação da operação de um usuário real é o seu objetivo.

    Observe a Figura 3.17. Por meio dela é possível observar que o WebDriver se comunica com um navegador através de um
    driver de modo bidirecional: o WebDriver passa os comandos para o navegador pelo driver e recebe as informações
    pela mesma rota. O driver é específico para o navegador, como o ChromeDriver é para o Chrome, como o GeckoDriver é
    para o Mozilla Firefox, entre outros. O driver é executado no mesmo sistema do navegador.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 3.17 | Comunicação entre componentes do WebDriver
    Fonte: adaptada de Selenium ([s.d.]).

    Por meio do WebDriver, o Selenium oferece suporte a todos os principais navegadores do mercado, como o Chrome, o
    Firefox, o Internet Explorer, o Opera e o Safari. Sempre que possível, o WebDriver dirige o navegador usando o
    suporte integrado dele para a automação, mesmo que nem todos os navegadores tenham suporte oficial para controle
    remoto. Embora todos os drivers compartilhem uma única interface voltada ao usuário para controlar o navegador, eles
    têm maneiras ligeiramente diferentes de configurar suas sessões. Como muitas das implementações de driver são
    fornecidas por terceiros, eles não estão incluídos na distribuição padrão do Selenium (SELENIUM, [s.d.]).

    Selenium IDE: trata-se de uma extensão para os navegadores Chrome e Firefox que permite a gravação e a reprodução
                  dos testes neles.

    Selenium Grid: esta modalidade do Selenium é capaz de executar testes em várias máquinas ao mesmo tempo, reduzindo,
                   assim, o tempo necessário para realizar testes em vários navegadores ou Sistemas Operacionais.

    PESQUISE MAIS
    Para saber mais sobre o conceito e a utilização de anotações em Java, leia o artigo Entendendo anotações em Java, de
    Carlos Araújo (ARAÚJO, 2012).

    ARAÚJO, C. Entendendo anotações em Java. DevMedia, [S.l.], 2012.

    Este foi, portanto, o conteúdo que queríamos compartilhar com você nesta seção. Longe de ser uma mera opção,
    automatizar testes é uma providência absolutamente necessária em ambientes profissionais de Engenharia de Software.
    Como tivemos oportunidade de discutir, as reduções nos custos e no tempo de execução excedem qualquer tempo que se
    leve para que se possa conseguir familiaridade com as ferramentas de teste. A respeito do custo, inclusive, tivemos
    a oportunidade de conhecer duas ferramentas com custo zero de aquisição e implantação. Continue focado em seus
    estudos e boa sorte!

    #ref Unidade 3 - Seção 3
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    ANICHE, M. Test-Driven Development. [S.l.]: Casa do Código, 2014. E-book.

    ANICHE, M. Testes automatizados de software: Um guia prático. [S.l.]: Casa do Código, 2015. E-book.

    ARAÚJO, C. Entendendo anotações em Java. DevMedia, [S.l.], 2012. Disponível em: https://bit.ly/3iPtMp8. Acesso em:
    31 dez. 2020.

    CAETANO, C. Gestão de Testes Ferramentas Open Source e melhores práticas na gestão de testes. Engenharia de Software
    Magazine, [S.l.], ed. 3, p. 58-66, [s.d.]. Disponível em: https://bit.ly/3t2sA6r. Acesso em: 6 jan. 2021.

    MEDEIROS, H. Mocks: Introdução a Automatização de Testes com Mock Object. DevMedia, [S.l.], 2014. Disponível em:
    https://bit.ly/3qX8XLi. Acesso em: 29 dez. 2020.

    QIU, J. Acceptance Test Driven Development with React. [S.l.: s.n.], 2018. E-book.

    REIS, L. Testlink – uma ferramenta de gerenciamento de testes de software. Medium, [S.l.], 24 ago. 2018. Disponível
    em: https://bit.ly/2MrAJRp. Acesso em: 7 jan. 2021.

    SELENIUM. Selenium Projects. [S.l., s.d.]. Disponível em: https://www.selenium.dev/projects/. Acesso em: 30 dez.
    2020.

    TELES, V. M. Extreme Programming: aprenda como encantar seus usuários desenvolvendo software com agilidade e alta
    qualidade. São Paulo: Novatec, 2004.

    TESTLINK. TestLink Open Source Test Management. [S.l., s.d.]. Disponível em: https://testlink.org/. Acesso em: 13
    jan. 2021.
    """


def unidade4_secao1():
    """
    ----------------------------------------------- UNIDADE 4 / SEÇÃO 1 -----------------------------------------------
    FUNDAMENTOS DE AUDITORIA DE SISTEMAS - Sergio Eduardo Nunes

    CONCEITO-CHAVE
    Normalmente, quando as pessoas comentam sobre passar por auditorias, os relatos são sempre carregados de momentos
    tensos, pressão no trabalho, ajustes de condutas e processos, entre outras situações que causam uma sensação de
    verificação minuciosa das atividades profissionais desenvolvidas.

    Assim como em outras áreas do conhecimento (fiscal, contábil, administrativa, etc.), a Engenharia de Software também
    conta com processos de auditoria para verificação dos desenvolvimentos de software, pois, como se trata de
    atividades que necessitam do emprego de habilidades técnicas de programação, criatividade e aplicação correta dos
    processos, são passíveis de auditoria.

    AUDITORIA
    Mas, de fato, o que é uma auditoria?

    Segundo Cardoso (2015), as atividades de auditoria têm como principal função analisar parcial ou globalmente os
    processos, resultados e, em alguns casos, sugerir ações corretivas ou melhorias. Elas podem ser aplicadas por
    diversos métodos (questionário, teste de uso prático, análise documental, entre outras formas), porém os resultados
    obtidos não devem gerar dúvidas.

    Para que você possa compreender em que casos isso será encontrado, vamos tomar como exemplo uma empresa que precise
    auditar o desenvolvimento de determinada funcionalidade no aplicativo de uma operadora de convênio odontológico, a
    qual permite agendamento de consultas. A auditoria foi necessária, pois houve um atraso significativo na entrega do
    aplicativo. Esse processo serve para compreender em que momento ocorreu o atraso e o porquê ele foi gerado,
    informações que podem ajudar a corrigir falhas no processo, por exemplo. Nesse caso, a equipe de auditoria poderia
    analisar os documentos ou fazer entrevistas com os envolvidos, de modo a ter dados o suficiente para gerar
    informações úteis para a compreensão do problema.

    É claro que, embora existam processos de auditoria para verificar as atividades em diversas áreas, a tecnologia da
    informação possui métodos e normas específicas para si. Segundo Cardoso (2015), as atividades de auditoria em
    Engenharia de Software são conhecidas por auditoria em sistemas da informação. As atividades de auditoria de
    sistemas não têm apenas a função de verificar códigos, instruções e outras formas de se codificar uma aplicação
    computacional, mas também a de aplicar os seus esforços conforme demonstrado a seguir:

    -> Processos: diz respeito à forma como são orientados os meios de execução das atividades de desenvolvimento. Em
       termos operacionais, imagine que a empresa utilize o SCRUM com o objetivo específico de priorizar as atividades.
       A auditoria de processo poderia analisar especificamente se o SCRUM foi seguido durante o ciclo de vida do
       desenvolvimento do software.

    ASSIMILE
    Assim como em diversas áreas, a urgência nas entregas, os picos de alta demanda e a exigência de maior produtividade
    certas vezes acabam por comprometer alguns atributos importantes da garantia de qualidade do produto. Uma das
    soluções para esse problema, na área de tecnologia da informação, é a metodologia conhecida como SCRUM.

    Ela se trata de uma metodologia agile que visa segmentar um projeto de desenvolvimento em pequenos ciclos, reuniões
    de alinhamentos frequentes para acompanhamento dos desenvolvimentos de softwares.

    -> Desenvolvimento: compreende a análise dos scripts em si, ou seja, trata-se de uma forma de efetuar a verificação
       de erros de escrita da linguagem de programação/marcação utilizada. Um exemplo muito atual se refere à auditoria
       de responsividade de desenvolvimentos Web, na qual é analisada a correta utilização dos frameworks, que têm como
       objetivo deixar a aplicação responsiva. Nesse caso, os processos de auditoria mostrarão em quais dispositivos
       existem erros, desconforto de navegação, entre outras avaliações muito úteis a nível de qualidade dos
       desenvolvimentos.

    -> Testes: a auditoria visa à verificação da eficácia dos testes efetuados nos desenvolvimentos de software. Em
       termos profissionais, significa que as atividades desenvolvidas pelos testers de software receberão uma auditoria
       para verificar se de fato as funcionalidades desenvolvidas estão sendo testadas ou se existem falhas, vícios ou
       qualquer outra inconformidade.

    -> Segurança e proteção dos dados: são aquelas tratativas realizadas quanto à proteção e à segurança dos dados para
       que não ocorram incidentes indesejados. Um exemplo é quando o processo de auditoria utiliza pentest (profissional
       de segurança da informação que busca vulnerabilidades) para comprovar, na prática, que um sistema é seguro.

    -> Estrutura de desenvolvimento: está voltada às atividades administrativas e de recursos humanos, ambiente de
       trabalho e recursos disponíveis para o desenvolvimento profissional. Exemplo: o auditor, dentro de suas análises,
       poderia voltar a suas atividades profissionais para que seja efetuada a avaliação do ambiente de trabalho
       favorece o bom desempenho do profissional de desenvolvimento de software.

    VOCABULÁRIO
    Os profissionais de tecnologia da informação que efetuam testes de intrusão são conhecidos como pentest, uma
    abreviação da palavra Penetration Test. Esses especialistas são altamente requisitados para o processo de auditoria
    de software voltado à análise de desenvolvimento de software. Isso porque, normalmente, esses profissionais possuem
    competências e habilidades para efetuar teste de intrusão em: serviços de rede, aplicações web, teste ao lado do
    cliente (client side) e teste de serviços de aplicações web.

    O AUDITOR
    Certamente você percebeu que existe a possibilidade de efetuar auditorias em muitas áreas que envolvem o
    desenvolvimento de software. Entretanto, existe um agente dentro dos processos de auditoria de software cujas
    atribuições e responsabilidades é essencial compreender. Estamos falando aqui do auditor.

    Segundo Gallotti (2016), o auditor é o profissional que tem conhecimentos técnicos, gerenciais, operacionais e
    analíticos para conduzir as atividades relacionadas ao desenvolvimento de auditorias em sistemas da informação.

    Para compreender o papel do auditor, observe o Quadro 4.1.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Quadro 4.1 | Atribuições e responsabilidades do auditor de tecnologia da informação
    Fonte: adaptado de Gallotti (2016).

    TIPOS       ATRIBUIÇÃO
    --------------------------------------------------------------------------------------------------------------------
    Inspeção    Efetuar inspeção dos processos e dos desenvolvimentos.
                Verificar onde ocorrem inconformidades e apresentar provas convincentes.
    --------------------------------------------------------------------------------------------------------------------
    Controle    Efetuar a análise de controle dos processos, podendo ser operacionais, de desenvolvimento ou gerenciais.
    --------------------------------------------------------------------------------------------------------------------
    Risco       Verificar quais riscos podem afetar o projeto, a fim de se indicar a equipe na qual existe um risco.
                Isso permite que o gerente de projetos possa tomar medidas corretivas/preventivas.

                Analisar de forma mais abrangente os riscos, apresentando consequências externas que possam ocorrer.
    --------------------------------------------------------------------------------------------------------------------
    Contínua    Elaborar relatórios das análises em espaços curtos de tempo.
                Utilizar sistemas de verificação constantes para que se faça uma análise de diversos momentos.
                Contratar especialistas da área em que é necessária uma análise mais profunda, a fim de se permitir o
                aumento do detalhamento dos processos.
    --------------------------------------------------------------------------------------------------------------------

    Acerca das responsabilidades e atribuições de um auditor de desenvolvimento de software, vamos a um exemplo: imagine
    que uma desenvolvedora de games para mobile tenha decidido fazer um jogo exclusivo para um público específico. Um
    processo de auditoria poderia responder quais são os impactos positivos e negativos de um jogo cujo tema exclui
    outros jogadores, porém cabe aos níveis administrativos e gerenciais da empresa, após os resultados das auditorias,
    tomar uma decisão quanto ao produto elaborado. Uma auditoria aponta falhas, erros, pontos de atenção, no entanto não
    obriga a empresa a tomar outros rumos. Essa decisão fica a cargo dela.

    Vale ressaltar, ainda, que as atividades de auditoria de software são pautadas por testes, análises, avaliações e
    outras formas que possam provar que algo de inconformidade está ocorrendo ou sendo executado, conforme define
    Gallotti (2016).

    CICLO DE VIDA DA AUDITORIA
    Caro aluno, percebeu a importância da auditoria na Engenharia de Software? As auditorias não devem ser enxergadas
    como um processo doloroso e negativo, como descrito no início de nossas discussões, mas devem ser encaradas como uma
    ferramenta de apontamento de falhas, que permite agregar qualidade ao projeto, à equipe, à organização, o que
    reflete positivamente para o cliente. Mas, em termos práticos, em que momento a auditoria deve ser utilizada durante
    o projeto de desenvolvimento de software?

    Conforme defendem Weill e Ross (2006), os processos de auditoria em sistemas da informação podem ser
    operacionalizados durante todo_ o ciclo de vida do projeto de desenvolvimento. O ciclo de vida da auditoria é
    dividido em quatro processos, que compreendem desde as atividades precedentes à autoria em si (preparação) até o
    acompanhamento dela. Os processos de auditoria durante seu ciclo de vida são sequenciais. Para compreender a
    organização dessas atividades, observe a Figura 4.1.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 4.1 | Ciclos de vida da auditoria
    Fonte: adaptada de Gallotti (2016).

    De acordo com o observado no ciclo de vida da auditoria, as atividades de auditoria começam antes mesmo de seu
    início em sistemas da informação. Vale ressaltar, aqui, que neste momento não estamos discutindo o ciclo de vida do
    projeto, mas o ciclo de vida da auditoria. Em termos de aplicação profissional, estamos agora com foco em todos os
    processos que compõem uma auditoria em atividades de desenvolvimento de software.

    PLANEJAMENTO DO CRONOGRAMA
    Segundo Vetorazzo (2018), as atividades de elaboração do cronograma mostram o nível de organização da equipe que
    aplicará a auditoria. Além disso, é possível compreender como o ciclo todo_ será organizado. Ao divulgar o
    cronograma da auditoria, a empresa/equipe que será auditada pode ajustar alguns pontos de melhorias. Para que você
    compreenda como um cronograma de auditoria pode ser organizado, observe o Quadro 4.2.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Quadro 4.2 | Exemplo de cronograma de auditoria
    Fonte: elaborado pelo autor.

    Esse cronograma pode ter diversas atividades descritas dependendo do nível de detalhamento de que o projeto
    necessite. Quanto às informações das colunas, ser minimalista é o suficiente para demonstrar a atividade, as datas
    inicial e final e o responsável. Mas nada impede que ele apresente outras informações.

    Vetorazzo (2018) defende ainda que o planejamento do cronograma de auditoria, em muitos casos, deve ser aprovado
    pela contratante. Para entender como isso ocorre em termos práticos, imagine que uma empresa desenvolveu um
    aplicativo para a população votar on-line e com garantia de autenticidade. Porém, antes que ele seja liberado para
    a população utilizar, é necessário que seja feita uma auditoria. A empresa de auditoria, então, divulga as datas de
    seu cronograma. Entretanto, há um problema: a data final do reporte está para depois do dia em que deveria ocorrer
    a votação. Percebeu a importância da aprovação do cronograma da auditoria?

    PLANEJAMENTO DA AUDITORIA
    Para Rainer e Cegielsky (2016), o planejamento da auditoria como primeira atividade está no mapeamento dos
    processos, o qual identifica individualmente os agentes responsáveis por eles. Ainda é possível que o auditor
    consulte documentos de auditorias anteriores para que possa voltar suas atividades a apontamentos já feitos. Entre
    as atividades do planejamento da auditoria, deve-se estar claro qual o objetivo de determinada auditoria, de forma
    que a empresa de desenvolvimento de software que receberá os auditores possa se adequar às necessidades do cliente.

    Por que o objetivo da auditoria deve ser divulgado? Imagine que uma empresa de desenvolvimento tenha quatro equipes:
    front end, back end, banco de dados e infraestrutura de redes. Mas, devido às muitas reclamações a respeito da
    performance do tempo de resposta do sistema, será agendada uma auditoria nos setores de desenvolvimento. Em todas as
    equipes? Não, somente naquelas que podem impactar diretamente no desempenho da aplicação, ou seja, back end, banco
    de dados e infraestrutura de redes.

    Rainer (2016) defende ainda que o planejamento é um documento que deve ser elaborado pelos auditores de forma que
    três pontos fiquem claros para equipe de auditores e para a organização/equipe a ser auditada:

    -> Quem será auditado?
    -> O que será auditado?
    -> Quando ocorrerá a auditoria?

    REFLITA
    A auditoria deve demonstrar claramente qual o seu objetivo. Além disso, é indicado que a organização/equipe que a
    receberá saiba previamente quando e como isso vai ocorrer.

    Porém, não existe apenas essa forma de execução de processos de auditoria nem somente uma necessidade a ser atendida
    por ela. Em muitos casos, auditorias são aplicadas de surpresa e o intuito é realmente este: que o auditado não se
    prepare previamente; assim, poderá ser refletido o que de fato ocorre no dia a dia. Será que esse modo de aplicar
    auditoria não gera respostas mais fiéis ao que realmente ocorre?

    CONDUÇÃO DA AUDITORIA
    Conforme defende Vetorazzo (2018), quando o planejamento da auditoria está pronto e aprovado, dá-se seu início, no
    qual são aplicadas as atividades de coleta de informações, tais como: revisão documental, conversas e entrevistas,
    análise de dados de processos, observações, entre outras técnicas. Normalmente, a equipe de auditoria possui um
    checklist com escopo expandido para permitir diversas análises.

    Em termos práticos e profissionais, o checklist, para o auditor, é um guia com os pontos a serem auditados. Para que
    você possa compreender como é estruturado esse documento, observe o Quadro 4.3.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Quadro 4.3 | Exemplo de checklist de auditoria
    Fonte: elaborado pelo autor.

    Esse cronograma pode ter diversas atividades descritas dependendo do nível de detalhamento de que o projeto
    necessite. Quanto às informações das colunas, ser minimalista é o suficiente para demonstrar a atividade, as datas
    inicial e final, o horário, o local e os responsáveis. Mas nada impede que nele sejam apresentadas outras
    informações.

    REPORTE DA AUDITORIA
    Segundo Vetorazzo (2018), trata-se da parte de encerramento da auditoria, na qual podem ser feitas reuniões,
    relatórios, apresentações, entre diversos outros recursos que fornecem a devolutiva do que foi auditado. Dependendo
    do acordado na contratação desse serviço, podem-se propor melhorias e ajustes. Porém, não cabe à empresa/equipe de
    auditoria promover as mudanças descritas no reporte.

    Em termos práticos, após longos dias de auditoria, é chegada a hora de conhecer os resultados para saber os acertos,
    os erros e, assim, poder projetar e alcançar novos objetivos e melhorias. Normalmente nesse dia a equipe auditada,
    com gerentes e demais cargos administrativos, é chamada para uma reunião em que os resultados são apresentados e as
    sugestões são discutidas.

    EXEMPLIFICANDO
    No dia em que são apresentados os resultados de uma auditoria, a empresa marca uma reunião com os auditados e cargos
    gerenciais/administrativos a fim de expor as conclusões do processo e de discutir as sugestões.

    Um objeto interessante para a demonstração dos resultados é o relatório de auditoria, pois podem ser feitas cópias
    dele, as quais são entregues para cada membro presente na reunião. Abusar dos gráficos e tabelas é uma forma muito
    eficiente de se demonstrar os resultados, além de ajudar os auditados a compreenderem melhor as análises.

    Como você pôde ver ao longo das discussões e dos exemplos apresentados, a auditoria em atividades de desenvolvimento
    de software pode levar uma equipe à melhoria de seus processos e produtos. A forma como deve ser feita a abordagem
    da auditoria em sistema da informação visa contribuir com a qualidade dos processos, do produto de software e nos
    membros da equipe de desenvolvimento. Por fim, as discussões acerca do ciclo de vida da auditoria guiarão o
    profissional na construção de documentações como cronogramas, checklists e ambientes auditáveis.

    PESQUISE MAIS
    No capítulo 4 do livro Introdução a sistemas de informação (RAINER; CEGIELSKY, 2016), disponível na biblioteca
    virtual, são tratados os assuntos relacionados à auditoria de software, sendo este um referencial bibliográfico
    muito interessante para o assunto. Vale a pena conferir!

    RAINER Jr. R. K.; CEGIELSKY, C. G. Introdução a sistemas de informação. 5. ed. Rio de Janeiro: Elsevier, 2016.

    #ref Unidade 4 - Seção 1
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    CARDOSO, A. Auditoria de sistema de gestão integrada. São Paulo: Pearson Education do Brasil, 2015.

    GALLOTTI, G. M. A. Qualidade de software. São Paulo: Pearson Education do Brasil, 2016.

    RAINER Jr. R. K.; CEGIELSKY, C. G. Introdução a sistemas de informação. 5. ed. Rio de Janeiro: Elsevier, 2016.
    Disponível em: https://cutt.ly/wjOtJCU. Acesso em: 16 nov. 2020.

    VETORAZZO, A. de S. Engenharia de software. Porto Alegre: SAGAH, 2018.

    WAMPSERVER. WampServer, [S.l., 2020]. Disponível em: https://www.wampserver.com/en/. Acesso em: 5 nov. 2020.

    WEILL, P.; ROSS, J. W. Governança de TI: como as empresas com melhor desempenho administram os direitos decisórios
    de TI na busca por resultados superiores. São Paulo: M. Books do Brasil Editora Ltda., 2006.
    """


def unidade4_secao2():
    """
    ----------------------------------------------- UNIDADE 4 / SEÇÃO 2 -----------------------------------------------
    AUDITORIA DE SISTEMAS DA INFORMAÇÃO - Sergio Eduardo Nunes

    CONCEITO-CHAVE
    Caro aluno, cada organização apresenta algumas características, como costumes, clima organizacional, políticas
    internas, que fazem com que os colaboradores tenham determinado comportamento e que são parte do DNA de cada uma
    delas. Na área de desenvolvimento de software, esse ambiente de trabalho, também está presente. Muitas vezes,
    orientado por métodos, normas ou metodologias de desenvolvimento.

    Para que os controles gerais de auditoria possam ser compreendidos, Braz (2017) define-os como as estruturas
    internas das organizações, as políticas administrativas operacionalizadas e os procedimentos utilizados nas
    atividades como um todo_.

    Na prática os controles gerais não são aplicáveis somente à tecnologia da informação. O controle geral é
    operacionalizado da portaria à direção da empresa, ou seja, todos os colaboradores criam o ambiente, o que ajuda a
    moldar o controle geral. Mas por que o controle geral interfere nos processos de auditoria?

    Para responder ao questionamento, Braz (2017) afirma que, durante um processo de auditoria em que se tenha como
    objetivo a avaliação de um sistema na empresa (financeiro, contábil, fiscal, etc.), é necessário compreender como o
    controle geral atua sobre a aplicação. Por exemplo, se o processo de auditoria ocorrerá sobre o sistema de vendas de
    uma loja de departamento, precisamos compreender alguns pontos, tais como:

    -> Um vendedor pode conceder desconto para o cliente?
    -> O gerente pode conceder desconto para o cliente?
    -> É possível alterar o prazo de pagamento?
    -> O número de parcelas no crediário pode ser aumentado pelos colaboradores?

    Percebeu como o controle geral das atividades, as regras e os procedimentos estão diretamente ligados aos processos
    de auditoria? Por exemplo, imagine que somente o gerente tenha uma senha que permita aumentar o percentual de
    desconto no sistema de vendas do caixa. Mas, ao fazer o processo de auditoria, é feito um apontamento de
    vulnerabilidade, pois o sistema permite que qualquer colaborador possa inserir o desconto. Isso seria muito negativo
    para um processo de auditoria, pois seria apontada como vulnerabilidade uma funcionalidade do sistema.

    ASSIMILE
    Falhas e erros de software ocorrem em algumas situações e podem ter consequências negativas, sobretudo para empresas
    que utilizam a aplicação. O maior prejuízo é a visibilidade perante os clientes. Imagine que um aplicativo bancário,
    devido a uma falha, comece a fazer transferências aleatoriamente e deixe o saldo dos usuários zerados. Mesmo que o
    dinheiro retorne para conta posteriormente, haverá um impacto negativo quanto à visão do cliente.

    Segundo Braz (2017), quando os controles gerais apresentam deficiência, ocorre a diminuição da confiabilidade nos
    controles individuais. Por esse motivo, o primeiro passo de um processo de auditoria é a avaliação dos controles
    gerais para então promover as análises por meio de processos de auditoria a fim de avaliar as aplicações
    computacionais. No processo de auditoria em desenvolvimento de software, no que tange à avaliação do controle geral,
    ela é organizada em seis categorias, conforme pode ser observado no Quadro 4.4.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Quadro 4.4 | Categorias de controles gerais para processo de auditoria
    Fonte: adaptado de Braz (2017, p. 52).

    Controle organizacional
        São as políticas internas, os procedimentos e a organização estrutural utilizada na empresa. Isso determina
        quais são as atribuições e as responsabilidades dos colaboradores envolvidos nas atividades de desenvolvimento
        de software. Um exemplo prático é compreender como são organizados os times de desenvolvimento dentro da empresa
        . Existe um gerente de projetos responsável por cada time de desenvolvimento? Existe um gerente geral que faz as
        tratativas com cada gerente de projetos? Existem diversas possibilidades dentro das organizações e é necessário
        compreender essa estrutura no processo de auditoria.

    Controle geral de segurança
        Este deve verificar se os controles gerais determinam que o sistema possua gerência de riscos e incidentes,
        quais são as políticas de segurança da empresa, se as funções relacionadas à segurança possuem um setor ou
        responsável pelo gerenciamento na empresa e se existe supervisão relacionada à segurança da informação. Como
        exemplo, imagine que uma empresa de móveis planejados possua um sistema para desenvolver um layout para o
        cliente. Esse sistema permite importar para o layout imagens baixadas pelo cliente. Porém, a política de
        segurança da empresa não permite que sejam utilizados pendrives de clientes no computador. Ou seja, uma política
        interna moldará como o sistema deve operar.

    Continuidade de serviço
        No processo de auditoria deve ser analisado se o controle geral possui tratativas e se, em caso de falhas, erros
        , bugs ou incidentes de segurança, existe alguma tratativa relacionada à recuperação parcial ou total do sistema
        . Por exemplo, um sistema de pagamento permite diversos meios, tais como: boleto, cartão de crédito, cartão de
        débito e PIX. Caso umas das formas falhe, o sistema vai continuar disponibilizando os outros meios de pagamento?

    Controle de software
        O controle geral, neste ponto, tem um olhar de limitação e supervisão de acessos aos arquivos, diretórios e
        pontos críticos do sistema. Por exemplo, o sistema possui senha de acesso ao driver C:, onde os arquivos e
        diretórios estão instalados? Caso o sistema permita acesso aos arquivos, o usuário terá permissão de editar
        algum?

    Controle de acesso
        No processo de auditoria, deve haver a verificação de existência de recursos ou politicas administrativas que
        detectam acessos não autorizados para evitar incidentes de segurança e intrusões. Exemplo: o sistema deve emitir
        um alerta ao administrador se houver um alarme de intrusão no sistema. Dessa forma, no processo de auditoria, é
        preciso ocorrer uma verificação dessa funcionalidade.

    Controle de versionamento
        Verifica se existe um controle de modificações e implementações no sistema. Um exemplo é a verificação de
        utilização de algum software para gerenciamento e controle das versões desenvolvidas.

    Conforme se pode observar, as categorias de controles gerais para processo de auditoria apresentam diversas
    tratativas, as quais visam observar todas as características que possam, de alguma forma, interferir na auditoria.

    Segundo Lyra (2008), o controle de software de sistema se trata de um conjunto de programas desenvolvidos para
    gerenciar, controlar e executar atividades de processamento de dados. Observe, no Quadro 4.5, exemplos de software
    de sistemas.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Quadro 4.5 | Softwares de sistemas
    Fonte: elaborado pelo autor.

    Software de sistema    Definição    Exemplo

    Sistema operacional
        DEFINIÇÃO
        Sistema responsável pelo funcionamento do computador e que faz a conexão do sistema com o hardware.

        EXEMPLO
        Windows, Linux, Android, IOS, entre outros.

    Utilitários do sistema
        DEFINIÇÃO
        Sistema responsável por fazer o gerenciamento dos recursos.

        EXEMPLO
        Gerenciador de dispositivos, gerenciador do sistema, sistema de gerenciamento de compartilhamento.

    Sistemas de bibliotecas
        DEFINIÇÃO
        São partes de programas que realizam determinadas funcionalidades.

        EXEMPLO
        Bootstrap (para desenvolver sites responsivos), PyGame (para desenvolver jogos em Python), Google Charts (para
        gerar gráficos em PHP).

    Software de segurança
        DEFINIÇÃO
        São sistemas que visam evitar incidentes de segurança.

        EXEMPLO
        Firewall, Proxy, sistemas de senhas e autenticação de usuário.

    Sistema de comunicação de dados
        DEFINIÇÃO
        Sistemas que permitem a comunicação da aplicação com o usuário.

        EXEMPLO
        WAMP, XAMMP, LAMP, entre outros.

    Sistema de gerenciamento de banco de dados
        DEFINIÇÃO
        Trata-se de sistemas de banco de dados, podendo ser do tipo relacional e não relacional.

        EXEMPLO
        MySQL, Oracle, MongoDB, CouchDB, etc.

    Como se pode observar no quadro, os sistemas estão muito presentes em muitas organizações, e boa parte deles é
    necessária para que a empresa faça suas operações.

    Com isso, neste momento temos um olhar de aplicação profissional para os processos de auditoria no controle de
    software de sistema. Assim, vamos tomar como exemplo um sistema de vendas para caixa de supermercado, no qual,
    incialmente, temos que listar quais sistemas estão, de alguma forma, relacionados ao sistema do caixa, logo
    passíveis de análise nos processos de auditoria. A fim de entender o que contexto apresentado compreende, observe
    quais sistemas são elegíveis para a auditoria:

    -> Sistema operacional: obrigatoriamente estará instalado nos computadores dos caixas e nos servidores.

    -> Utilitários de segurança: como ocorrem transações que envolvem quantidades, pagamentos e contabilizações, é
                                 necessária auditoria sobre esses serviços.

    -> Sistema de comunicação: a auditoria é necessária, pois, para que os caixas possam efetuar as transações,
                               obrigatoriamente são necessários sistemas de gerenciamento de comunicação de dados.

    -> Sistema de gerenciamento de banco de dados: a auditoria deve dar especial atenção a este ponto pois, em um
                                                   sistema de supermercado, as transações são feitas em cima de banco de
                                                   dados

    Segundo Lyra (2008), nos processos de auditoria, existe uma preocupação voltada ao controle de software de sistema,
    que é relacionado:

    -> Ao acesso ao software de sistema.
    -> À supervisão do software de sistema.
    -> Ao controle de alteração do software de sistema.

    Ainda de acordo com Lyra (2008), considera-se que esses três pontos discutidos sejam elementos críticos dentro do
    controle de software de sistema. Em termos práticos, os processos de auditoria devem ser orientadores (onde são
    necessários), como a verificação de documentação de desenvolvimento, os checklists de funcionalidades que garantam
    os pontos críticos, as observações e comprovações de funcionamento e eficácia, entre ouras ferramentas de auditoria.

    SAIBA MAIS
    Nos controles gerais para processo de auditoria em desenvolvimento de sistema, existe uma divisão em seis categorias
    . Entre elas, há uma que trata exclusivamente de versionamento de desenvolvimento de software, a qual é uma parte
    extremamente importante do processo, principalmente quando as atividades de desenvolvimento são feitas em equipe.
    Uma ferramenta muito eficiente para gerenciamento de versão são os conhecidos GITs, entre eles o mais utilizado é o
    GitHub (c2020).

    CONTROLE DE APLICATIVOS
    Caro aluno, grande parte dos softwares executam três funções: entrada, processamento e saída. Por exemplo, em um
    sistema de consulta bancária, no caixa eletrônico, o usuário escolhe a função de saque (entrada), o sistema consulta
    o saldo, faz as verificações, autoriza o saque do valor desejado (processamento) e, finalmente, o dinheiro é
    liberado no caixa (saída). Quanto aos processos de auditoria, isso é conhecido por Controle de Aplicativos.

    Segundo Imoniana (2016), o controle de aplicativos pode ser definido como as funcionalidades que são executadas
    diretamente nos softwares, os quais têm as três funções básicas de qualquer aplicação, sendo elas: entrada,
    processamento e saída. A auditoria deve atestar que as três sejam confiáveis e que garantam a integridade dos dados.
    Para tal, vamos observar os processos de auditoria devem se comportar em cada uma das funções.

    CONTROLE DE ENTRADA DE DADOS
    Segundo Imoniana (2016), são desenvolvidos para garantir que os dados sejam inseridos na aplicação do tipo e da
    forma correta. Cabe aos controles de entradas terem mecanismos de entrada de dados correta, bem como evitarem que as
    transações ocorram de forma incompleta, duplicadas, com falhas e com outras anomalias.

    Para você compreender melhor como um processo de auditoria pode atuar sobre o controle de aplicativos, vamos tomar
    como exemplo uma auditoria feita sobre a validação de campos de determinado formulário. Isso pode ser feito a nível
    de script ou ainda por meio de teste de uso, sendo mais comum que ocorra a nível de script. Para isso, observe um
    trecho de um script na Figura 4.7.

    <div class="form-group">
    <label class="col-sm-2 control-label">E-mail</label>
      <div class="col-sm-5">
        <input type="email" class="form-control" name="email" required="">
      </div>

      <label class="col-sm-1 control-label">RG</label>
      <div class="col-sm-4">
        <input type="text" class="form-control" name="rg" maxlength="12"
        pattern="[0-9]{2}.[0-9]{3}.[0-9]{3}-[0-9]{1}$" OnKeyPress="formatar('##.###.###-#', this)" required>
      </div>
    </div>

    <div class="form-group">
      <label class="col-sm-2 control-label">Celular</label>
      Vdiv class="col-sm-5">
        <input type="phone" class="form-control" name="celular" maxlength="13" placeholder="com whatsapp"
        pattern="\([0-9](\d{2}\))\[0-9]d{5}-\[0-9]d{4}$" OnKeyPress="formatar('## #####-####', this)" required>
      </div>

      <label class="col-sm-1 control-label">Telefone</label>
      <div class="col-sm-4">
        Vinput type="phone" class="form-control" name="telefone" maxlength="12" placeholder="não obrigatório"
        pattern="\([0-9](\d{2}\))\[0-9]d{4}-\[0-9]d{4}$" OnKeyPress="formatar('## ####-####', this)">
      </div>
    </div>

    Nesse exemplo, nas linhas 4, 9/10, 17/18 e 23/24 ocorre o controle de entrada de dados, sendo este um ponto de
    verificação do controle de aplicativos, para o qual é utilizada uma técnica disponível na linguagem de marcação a
    fim de se validar a entrada do CPF, do RG, do celular e do telefone. Para isso foram aplicadas máscaras nas entradas
    . Por exemplo: se o usuário entrar com o CPF 123.456.789-01, o campo apresentará e fará a entrada do dado, conforme
    demostrado na Figura 4.8.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 4.8 | Validação de entrada de dados
    Fonte: captura de tela do sistema em auditoria elaborada pelo autor.

    Reparou que, para efetuar a auditoria em software de sistemas, deve-se conhecer a tecnologia na qual determinada
    funcionalidade foi desenvolvida? Isso ocorre por se tratar de uma área de desenvolvimento de software, na qual são
    utilizadas linguagens de programação/marcação.

    EXEMPLIFICANDO
    A validação de dados é algo muito importante na programação, pois garante que as entradas dos dados estejam no tipo
    e no formato corretos, o que garante uma execução exitosa da transação entre aplicação e banco de dados. Para isso,
    as linguagens de programação, como JavaScript, ou de marcação, como o HTML 5, possuem ferramentas que auxiliam o
    desenvolvedor nessa tarefa.

    Já quanto às tratativas de processamento de dados em controles de aplicativos, Imoniana (2016) define que o controle
    de processamento deve garantir que os dados de entrada sejam executados dentro do sistema, gerando, assim, saídas
    coerentes. Na prática, para que a análise de processamento ocorra, são necessários recursos auxiliares dentro do
    sistema.

    Um exemplo de recursos auxiliares em sistemas de software são os logs. Segundo Imoniana (2016), os logs são
    históricos que ficam registrados em um repositório dentro do sistema. Para uma análise a nível de auditoria de
    sistemas, eles são grandes aliados não somente para verificação de processamento, mas também para diversas outras
    transações.

    A nível de código, a auditoria de sistema de software, quanto ao processamento (segunda fase do controle de
    aplicativos), normalmente necessita do auxílio de um especialista, o qual deve conhecer bem a sintaxe de linguagem
    de programação, os seus métodos, funções, objetos e compatibilidade com outras tecnologias. Em termos práticos, as
    empresas de auditoria fazem a contratação do especialista para auditar os scripts.

    Finalmente, o controle de saída de dados é definido por Imoniana (2016) como ferramenta de garantia de integridade
    de forma consistente a absoluta. No processo de auditoria, é preciso gerar relatórios de saídas de dados para que
    seja possível uma análise com relação à sua integridade e exatidão.

    Em aplicações profissionais, essas análises são mais fáceis de serem executadas nos processos de auditoria. Por
    exemplo, imagine que um software de controle de vendas de móveis deva aplicar 5% de desconto nos pagamentos à vista.
    Os testes são de execução fácil, uma vez que basta escolher um produto qualquer e aplicar a opção pagamento à vista.
    Por meio da verificação do valor gerado, é possível fazer uma análise. Porém, para uma análise consistente, é
    necessário efetuar muitos testes com produtos e situações possíveis de serem executadas.

    REFLITA
    Os históricos de registros em sistemas, por meio de logs de uso de sistemas, podem fornecer detalhes importantes
    para permitir diversas análises de entrada, processamento e saída de um sistema. Porém, ao mesmo tempo, ficam
    monitorando as atividades que o usuário faz dentro do sistema. Até que ponto os logs podem ser utilizados para
    monitoramento do sistema, sem que ocorra a invasão da privacidade dos usuários? Vale a pena essa reflexão.

    Caro aluno, percebeu como a auditoria pode estar presente em muitos momentos do ciclo de vida do desenvolvimento de
    um software? Ao longo das discussões, percebemos que desde o momento do levantamento de requisitos, no início do
    projeto, até o encerramento/entrega do produto de software, os processos de auditoria podem estar presentes. Isso
    com o intuito de contribuir positivamente para que o software seja confiável e eficiente.

    Em termos profissionais, as discussões desta seção, contribuirão para que você compreenda os períodos de auditoria
    durante o ciclo de vida de desenvolvimento e de que forma os controles de auditoria, software de sistemas e
    aplicativos são executados em sistemas da informação. Ainda, por meio dos exemplos práticos, você conseguiu um
    excelente referencial para realizar suas próprias aplicações em outras situações dentro das organizações e nas
    atividades de desenvolvimento de software.

    PESQUISE MAIS
    No capítulo 4 do livro intitulado Introdução a sistemas de informação (RAINER Jr.; CEGIELSKY, 2016), disponível na
    Biblioteca Virtual, são tratados os assuntos relacionados à auditoria de software. Este é um referencial
    bibliográfico muito interessante para a compreensão dos processos relacionados à auditoria de software, por isso
    aproveite a leitura!

    RAINER Jr. R. K.; CEGIELSKY, C. G. Introdução a sistemas de informação. 5. ed. Rio de Janeiro: Elsevier, 2016.

    #ref Unidade 4 - Seção 2
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    BRAZ, M. R. Auditoria de TI: o guia da sobrevivência. Brasília: Asè Editorial, 2017.

    GITHUB. GitHub, [S.l.], c2020. Disponível em: https://github.com/. Acesso em: 21 nov. 2020.

    IMONIANA, J. O. Auditoria de Sistemas de Informação. 3. ed. São Paulo: Atlas, 2016.

    LYRA, M. R. Segurança e Auditoria em Sistemas de Informação. Rio de Janeiro: Editora Ciência Moderna, 2008.

    RAINER Jr. R. K.; CEGIELSKY, C. G. Introdução a sistemas de informação. 5. ed. Rio de Janeiro: Elsevier, 2016.
    Disponível em: https://cutt.ly/SjOoalH. Acesso em: 16 nov. 2020.
    """


def unidade4_secao3():
    """
    ----------------------------------------------- UNIDADE 4 / SEÇÃO 3 -----------------------------------------------
    MANUTENÇÃO E EVOLUÇÃO DE SOFTWARE - Sergio Eduardo Nunes

    CONCEITO-CHAVE
    Após certo tempo de uso, os sistemas operacionais deixam de receber suporte das empresas e isso significa que não
    serão mais disponibilizadas correções e atualizações para eles. Já os sistemas operacionais livres e de código
    aberto não são descontinuados, pois anualmente a comunidade evolui o sistema, efetua correções e insere novas
    funcionalidades.

    Percebeu como existem tratativas diferentes para o envelhecimento do software? Os processos evolutivos e de
    manutenção acompanham o ciclo de vida do sistema, e, em alguns casos, ao atingir o seu limite, ele é descontinuado.
    Com base no exposto, nesta seção de aprendizagem, você conhecerá a necessidade de evolução e de manutenção de um
    software, a classificação e os tipos de atividades de manutenção normalmente executadas. Ainda será possível
    entender como são utilizadas as ferramentas dentro dos processos de manutenção, e ao final como a engenharia reversa
    e a reengenharia podem contribuir com a manutenção e os processos evolutivos dos softwares.

    Antes de iniciarmos tais discussões, compreendamos qual a motivação para estudar esses tópicos. Imagine que seja
    desenvolvido um aplicativo para rastreamento de PETs com chip de localização. No seu lançamento, existiam poucos
    clientes, somente método de pagamento via cartão (crédito e débito). Com o passar do tempo, o número de clientes
    aumentou consideravelmente, surgiram novos métodos de pagamento, como o PIX, e novas tecnologias de rastreamentos.

    Percebeu como a evolução de outras tecnologias impactou diretamente na aplicação? Para compreender melhor os
    processos de evolução e de manutenção, entendamos, inicialmente, como ocorre o processo de envelhecimento de um
    software.

    Segundo Vetorazzo (2018), os softwares são sequências lógicas de algoritmos cujo intuito é atender aos objetivos
    estabelecidos, os quais estão suscetíveis a mudanças de requisitos e ao ambiente que está sendo operacionalizado.
    Esse processo de envelhecimento é inevitável e exige uma análise de causas, de forma a fazer sua evolução e/ou
    manutenção, garantindo, assim, sua continuidade.

    Vetorazzo (2018) define ainda que existem dois tipos de envelhecimento de software, conforme pode ser observado a
    seguir:

    1. Falha de adequação: ocorre quando a equipe responsável pela evolução do software comete erros e falhas na
       adequação ou na implementação dos requisitos, ocasionando muitas vezes a perda da integridade e da confiabilidade
       da aplicação. Um exemplo prático: um software para conversão de formatos de vídeo, que funcionava em uma versão
       do sistema operacional, não tem compatibilidade com a versão mais recente desse mesmo sistema operacional. Caso o
       software seja utilizado por um usuário comum, certamente ele procurará outra solução. Mas, se uma empresa utiliza
       esse software em suas operações e em determinado momento os computadores são trocados e vêm com um sistema
       operacional não compatível com o software de conversão de vídeo, isso será um grande problema.

    2. Falha na mudança: é quando existe alguma atualização, manutenção ou implementação que impacta negativamente
       outras funcionalidades que já estavam em pleno funcionamento. Um exemplo prático: um e-commerce possui apenas um
       gerador de boleto em funcionamento, mas, devido a solicitações dos usuários, precisará apresentar outras formas
       de pagamento. Para isso, foi implementado (de forma incorreta) uma API de módulo de pagamentos. O impacto desse
       erro foi o sistema gerador de boletos e o módulo de pagamentos diversos não funcionarem. Isso ocorreu devido ao
       desconhecimento da estrutura do gerador de boletos.

    Caro aluno, percebeu a necessidade de evolução e manutenção dos softwares? São muitas variáveis a serem observadas:
    evolução dos sistemas operacionais, modos de consumo, novos meios e métodos de pagamento, segurança e diversos
    outros pontos. Mas, como prever a expectativa de envelhecimento do software? Isso só ocorreria se tivéssemos
    informações de todas as empresas de tecnologia da informação, as quais poderiam, por meio de uma alteração, impactar
    no funcionamento do sistema de alguma forma, o que é impossível.

    Porém, a compreensão da classificação e dos tipos de atividades de manutenção de softwares trará uma vantagem de
    recuperabilidade nas atividades de ajustes, manutenções, evoluções e adequações do sistema em casos de
    inconformidades.

    Com isso, Pressman e Maxim (2016) defendem que há diferentes intenções para evoluir um sistema que não apenas
    correção de falhas, bugs, erros e inconformidades. Para compreender como são classificadas as atividades de
    manutenção, observe o Quadro 4.6.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Quadro 4.6 | Classificação e tipos de manutenção de software
    Fonte: adaptado de Pressman e Maxim (2016, p. 798)

    Classificação

    Adaptativa
        São modificações necessárias para estar de acordo com novos requisitos, os quais podem ser provenientes de leis,
        regras, ameaças, meios ou métodos novos.

        APLICAÇÃO
            Recentemente (no ano de 2020) o Banco Central autorizou as instituições financeiras a utilizarem o PIX como
            método de pagamento. Isso exigiu uma adaptação do sistema de internet banking para que essa nova
            funcionalidade estivesse disponível aos clientes.

    Corretiva
        Sua função é corrigir falhas ou qualquer outro aspecto que seja motivo de degradação dos serviços do software.
        Além disso, a manutenção corretiva pode ocorrer antes, nas fases de desenvolvimento, ou depois, com o software
        já em funcionamento.

        APLICAÇÃO
            Nas eleições municipais de 2020, para que as pessoas que não foram votar pudessem justificar o voto, o
            governo federal disponibilizou um aplicativo para mobile conhecido como e-título. No primeiro turno, ele
            apresentou problemas desde a sua instalação até o processo de realizar a justificativa. A única
            funcionalidade em conformidade era a consulta da situação do eleitor quanto à Justiça Eleitoral. No segundo
            turno, o aplicativo teve de passar por uma manutenção corretiva para que fossem efetuados os ajustes
            necessários.

    Evolutiva
        A manutenção evolutiva tem o objetivo de inserir novas funcionalidades no sistema.

        APLICAÇÃO
            Os chats eram um recurso bastante presente no e-commerce para atendimento aos clientes. Uma evolução desse
            tipo de atendimento é, em vez de ter um colaborador de plantão para atendimento no chat, utilizar
            atendimento virtual. Para isso, foram desenvolvidos algoritmos que utilizam inteligência artificial, os
            quais, com a evolução tecnológica, conseguem responder grande parte das dúvidas dos clientes.

    O conhecimento da classificação dos tipos de manutenção, em termos profissionais, permite que tanto um desenvolvedor
    quanto um gestor se posicione quanto às reais necessidades dentro da estrutura do sistema, facilitando o
    direcionamento de recursos dentro do ciclo de vida de desenvolvimento de software. Para tal, é necessário conhecer
    os processos e as ferramentas utilizados na manutenção de software, os quais são recursos de extrema importância
    para que, de fato, os processos sejam otimizados.

    TÉCNICAS E FERRAMENTAS UTILIZADAS NA MANUTENÇÃO DE SOFTWARES
    Segundo Pressman e Maxim (2016), os processos e ferramentas utilizados na manutenção de softwares têm como objetivo
    obter métodos que sejam utilizados como boas práticas e garantir conformidade aos requisitos. Para entender melhor
    esse tópico, observe algumas das técnicas e ferramentas mais utilizadas a seguir.

    CODIFICAÇÃO
    É tida como uma parte muito importante na manutenção. A qualidade do código de programação deve possuir legibilidade
    , ou seja, deve ser fácil e legível. Ainda que as técnicas de indentação e os comentários de código devam estar
    presentes nas principais linhas da escrita do sistema e as suas funcionalidades. Observe na figura a seguir uma
    forma de utilizar a codificação com boas práticas.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 4.11 | Exemplo de codificação
    Fonte: captura de tela do Sublime elaborada pelo autor.

    O trecho de código foi escrito em JavaScript (não sendo necessário saber programar nessa linguagem). Mas repare em
    algumas boas práticas, que podem ser observadas:

    Nomes: os nomes de variáveis devem sempre remeter ao que será usado, exemplo: rua, bairro, cidade e estado (em
           amarelo nas linhas 197, 198, 199 e 200); outra boa prática é nomear as funções a serem realizadas. Por
           exemplo: na linha 195 existe uma função (function) para deixar os campos sem nenhum valor dentro, a qual é
           chamada de limpa_formulario_cep.

    Comentário: essa é uma técnica muito importante, mas deixada de lado por alguns desenvolvedores quando as práticas
                do desenvolvimento não impõem mais dificuldades, o que acaba complicando a execução da manutenção
                efetuada por outros desenvolvedores. Um exemplo pode ser observado na Figura 4.11, pois, na linha 196,
                é explicado o que a função irá executar naquele trecho de código.

    Indentação: são espaços utilizados para demonstrar o nível hierárquico das funcionalidades dentro do algoritmo.
                Ainda utilizando como base a Figura 4.11, repare que na linha 195 existe uma estrutura de função em que
                se abre uma chave, a qual é fechada na linha 201. Para a indentação, as linhas de 169 a 200 sofreram um
                recuo por meio de um TAB no teclado. Isso organiza o código-fonte e facilita o processo de manutenção.

    VERSIONAMENTO
    São documentações que determinam as modificações e as atualizações dos softwares. Elas podem ser feitas por dois
    meios:

    Numeração: trata-se de um sistema que por meio de uma numeração demonstra a sua versão. O objetivo é especificar as
               suas características por meio desse sistema numérico. Para um exemplo vamos supor que um determinado
               software esteja na versão 10.2.4.3 e que cada um desses números tenha um significado, conforme o que se
               explica adiante:

    10: indica que houve dez mudanças significativas no sistema. Essa numeração muda cada vez que o software faz uma
        evolução que promova mudanças de grande escala.

    2: esse número indica que foram adicionadas novas funcionalidades no sistema. Por exemplo, um software possui, na
       nova versão, a funcionalidade de impressão.

    4: esse número indica a quantidade de correções de bugs e falhas. Por exemplo, existia uma falha de envio de
       confirmação de inserção de produtos no carrinho de compras em um e-commerce na versão 10.2.3.3, que foi corrigido
       na versão 10.2.4.3.

    3: são correções graves relacionadas a incidentes de segurança. Por exemplo, determinado aplicativo expunha os dados
       dos usuários na versão 10.2.4.2, e a falha foi corrigida na versão 10.4.2.3. Comentário: uma prática muito comum
       é adicionar, nas primeiras linhas do arquivo no qual foram feitas as manutenções, informações como: data,
       objetivo da manutenção, modificações efetuadas e demais comentários úteis para manutenções futuras.

    SAIBA MAIS
    Os versionamentos em atividades de desenvolvimento de sistemas são essenciais para que se possa gerenciar as
    mudanças que ocorrem no ciclo de vida do desenvolvimento do software. Para isso, existem softwares que auxilia os
    profissionais de desenvolvimento. Entre eles, está o GitHub que faz uma tratativa para o versionamento de forma
    simples e muito eficiente.

    Para isso, a página do Git disponibiliza um informativo de como deve ser tratada as versões do GitHub.

    GITHUB. 1.1 Começando - Sobre Controle de Versão, [S.l.] c2021.

    ESTRUTURAR O CÓDIGO PARA EVOLUÇÃO
    A atividade de planejamento requer uma reflexão dos limites do software. Dessa forma, permite projetar o código para
    permitir sua evolução, seja ela por meio de adaptações, mudanças, ou por qualquer outro meio, o importante é que sua
    estrutura permita a evolução.

    ASSIMILE
    O processo de manutenção é muito delicado e requer muita atenção, pois, em alguns casos, existe uma alteração nos
    algoritmos que impacta toda a lógica pensada para o desenvolvimento. Um código-fonte com severas falhas de
    indentação pode atrapalhar, e muito, a manutenção do sistema.

    Na linguagem de programação Python, a indentação é obrigatória para que os programas funcionem, pois, do contrário,
    ao serem compilados, será gerada uma mensagem de erro de indentação. Aprender Python faz com que o desenvolvedor
    leve para outras linguagens a boa prática de indentar os scripts corretamente.

    Caro aluno, as discussões e os exemplos acerca dos processos e das ferramentas de manutenção de software em
    aplicações profissionais estão no cotidiano das práticas de desenvolvimento de sistemas e são essenciais para que se
    possam fazer manutenções corretamente e para que seja realizado um trabalho a ser continuado por outros
    profissionais com habilidades técnicas.

    Além disso, em termos profissionais, as discussões acerca da classificação e dos tipos de atividades de manutenção
    podem levá-lo a compreender os momentos nos quais as manutenções adaptativas (ajustar a novos requisitos),
    corretivas (correções de bugs e falhas) e evolutivas (adicionar novas funcionalidades) são operacionalizadas, em
    ambiente de desenvolvimento de sistemas, bem como as suas finalidades.

    REENGENHARIA DE SOFTWARE
    Segundo Pádua (2019), o processo de reengenharia de software é uma forma de reorganizar e/ou modificar o sistema a
    fim de fazê-lo apresentar um desempenho aceitável. Alguns fatores como falta de evolução de software ou excesso de
    contínuas mudanças (pior ainda quando promovidas por equipes diferentes) acabam degradando os serviços do sistema.

    Nesse momento, tentar encontrar novas soluções em um sistema comprometido pode não gerar o resultado desejado e
    ainda comprometer muitos recursos. Dessa forma, fazer uma reconstrução com a correção de erros e falhas, além de
    adequar as evoluções necessárias é uma ótima saída em busca de soluções.

    Ainda de acordo com Pádua (2019), a reengenharia de software tem o objetivo de reimplementar sistemas legados, em
    que se busca:

    Melhorar a manutenção: ao se reestruturar o sistema, as futuras manutenções serão mais fáceis para efetuar a
                           manutenção, visto que os antigos erros devem ser corrigidos na nova versão.

    Redocumentar o software: quando o software é reestruturado, a documentação é refeita, permitindo, assim, que novas
                             informações sejam colocadas nos scripts.

    Reestruturar o sistema: as estruturas que funcionavam à base de reparos e correções podem ser repensadas, o que
                            permitirá a construção de um sistema com otimizações e atendimento aos requisitos.

    Quando o software é produzido, existem funcionalidades e módulos que requerem grandes esforços para serem
    desenvolvidos, e, embora o sistema passe por testes, ao longo do tempo ele pode apresentar falhas. Porém, no
    processo de reengenharia de software, se o entendermos como uma releitura dos algoritmos, podemos dizer que a chance
    de erro será menor. Com base nisso, Pádua (2019) defende que os processos de reengenharia possuem riscos reduzidos,
    pois alguns problemas já haviam sido tratados.

    Esses processos são apoiados em metodologias de operacionalização. Para tal, Pressman e Maxim (2016) defende o
    modelo apresentado na Figura 4.12.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 4.12 | Modelo de reengenharia
    Fonte: adaptada de Pressman e Maxim (2016, p. 802).

    Observe que, ao longo dessa discussão, esses processos foram explorados e exemplificados. Porém, um novo termo muito
    importante quanto à manutenção e à evolução dos softwares foi citado no modelo representado na Figura 4.12:
    engenharia reversa.

    EXEMPLIFICANDO
    A área de desenvolvimento de software é muito colaborativa, permitindo, às vezes, encontrar funcionalidades inteiras
    já em funcionamento. No entanto, para ser utilizada em um sistema em funcionamento, sempre são necessárias algumas
    adequações.

    Para isso, é preciso fazer uma engenharia reversa, de modo que, após a compreensão de sua estrutura, seja possível
    promover as adequações necessárias.

    Conforme defende Pádua (2019), a engenharia reversa é o processo de reconstrução do software que parte do princípio
    de recuperação do código para tornar compreensíveis suas funcionalidades. Assim, elas podem ser reescritas com
    vistas a serem otimizadas e corrigidas.

    Claramente, quando a engenharia reversa é utilizada em hardware, a técnica fica visualmente mais fácil de ser
    compreendida, pois imaginamos os componentes sendo desmontados, o que nos permite compreender a ordem de montagem e,
    ainda, analisar cada componente em separado a fim de entender o seu objetivo e funcionamento.

    Mas como a engenharia reversa é tratada a nível de software? Antes de responder esse questionamento, observe a
    Figura 4.13.

    ------------------------------------------------------ IMAGEM ------------------------------------------------------
    Figura 4.13 | Processo de engenharia reversa
    Fonte: adaptada de Pressman e Maxim (2016, p. 803).

    Observe que gradativamente os métodos de engenharia reversa tratam de reestruturar o código, permitindo, assim, a
    compreensão das funcionalidades (entradas e saídas, interface e funcionalidades).

    Segundo Pádua (2019), ao se utilizar os processos e técnicas de engenharia reversa, é possível visualizar o software
    de diferentes maneiras, tais como:

    Nível de implementação: permite a compreensão das características e especifidades da linguagem de programação
                            utilizada no processo de implementação.

    Nível estrutural: permite a compreensão dos diferentes módulos e funcionalidades e das suas respectivas dependências
                      funcionais. Essa abstração se dá por meio da análise da estrutura da linguagem de programação
                      utilizada.

    Nível funcional: permite que as partes que compõem os sistemas sejam compreendidas; com ênfase na lógica utilizada
                     no desenvolvimento.

    Nível de domínio: permite compreender onde o software é utilizado.

    Com isso, em termos profissionais, tanto a reengenharia quanto a engenharia reversa possuem técnicas relativamente
    simples, mas que não são tão fáceis de operacionalizar. As técnicas são comumente utilizadas em práticas cotidianas
    para gerar diminuição no tempo de desenvolvimento. Dessa maneira, os resultados tendem a ser melhores visto que boa
    parte das funcionalidades já foram desenvolvidas.

    REFLITA
    A reengenharia permite, além de reescrever o sistema, compreender os erros e falhas e promover os devidos ajustes na
    nova construção do software. Na engenharia reversa também é possível encontrar erros, falhas, bugs e demais
    inconformidades?

    Caro aluno, ao longo das discussões, exemplos e conceituações desta seção, o objetivo foi mostrar a você, a partir
    de um olhar profissional, as formas encontradas na engenharia de software para promover os processos de manutenção e
    evolução do software. Os assuntos discutidos aqui são largamente utilizados nas atividades diárias de
    desenvolvimento de software, por isso esse conhecimento é tão importante para a sua carreira profissional.

    PESQUISE MAIS
    Na unidade 6 do livro intitulado Engenharia de Software (PERINI; HISATOMI; BERTO, 2009), disponível na Biblioteca
    Virtual, são tratados os assuntos relacionados à manutenção de software. Este é um referencial bibliográfico muito
    interessante para a compreensão dos processos de manutenção e evolução de software, por isso aproveite a leitura!

    PERINI L. C.; HISATOMI I. H.; BERTO, W. L. Engenharia de software. Pearson Prentice Hall, São Paulo, 2009.

    #ref Unidade 4 - Seção 3
    --------------------------------------------------- REFERÊNCIAS ---------------------------------------------------
    GITHUB. 1.1 Começando - Sobre Controle de Versão, [S.l.] c2021. Disponível em: https://cutt.ly/ujOsgiq. Acesso em:
    07 jan. 2021.

    PÁDUA, Wilson. Engenharia de Software. 1ª Ed. Rio de Janeiro: LTC, 2019.

    PRESSMAN, R.; MAXIM, B. Engenharia de Software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.

    PERINI L. C.; HISATOMI I. H.; BERTO, W. L. Engenharia de software. São Paulo: Pearson Prentice Hall, 2009.
    Disponível em: https://cutt.ly/pjOssev. Acesso em: 12 de jan. 2021.

    VETORAZZO, A. de S. Engenharia de software. Porto Alegre: SAGAH, 2018.
    """
