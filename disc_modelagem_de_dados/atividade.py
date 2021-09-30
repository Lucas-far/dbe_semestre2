

def notas():
    """
    Seção 3.1 - Modelagem de dados através do modelo entidade-relacionamento usando DER - página 7

    --------------------------------------------------- [ Página 8 ] ---------------------------------------------------
    No desenvolvimento de qualquer software devemos sempre considerar o seu ciclo de vida, que nada mais é do que o
    início do software através do estudo e do planejamento de sua viabilidade até o seu término na fase da manutenção ou
    do abandono do software. Em um projeto de banco de dados também há um ciclo de vida que determinará o começo do
    projeto até o seu final (que neste caso é a manutenção ou a evolução do banco de dados). Coronel e Rob (2011)
    destacam as seis fases e suas respectivas ações do ciclo de vida de um banco de dados:

    • Estudo inicial do banco de dados: estudo dos requisitos do problema e suas restrições e definição dos objetivos,
      escopo e fronteiras do banco de dados.

    • Projeto do banco de dados: criação do projeto conceitual, escolha do sistema de gerenciamento do banco de dados
      (SGBD) que deverá ser usado e criação do projeto lógico e físico do banco de dados.

    • Implementação e carga: instalação do SGBD, criação do banco de dados e carregamento ou conversão dos dados
      que serão armazenados no banco.

    • Teste e avaliação: realização de testes na base de dados para encontrar possíveis erros.

    --------------------------------------------------- [ Página 9 ] ---------------------------------------------------
    • Operação: o banco entra em funcionamento nos aplicativos desenvolvidos em paralelo.

    • Manutenção e evolução: assim que entra em operação, o banco de dados deve sempre receber manutenção para ficar o
      máximo possível em plena operação e a evolução do banco de dados acontece assim que novas necessidades do
      usuário surgem.

    EXEMPLIFICANDO
    As manutenções que acontecem em um banco de dados podem ser:
    • Preventiva: por causa do backup.
    • Corretiva: se houver necessidade de recuperação de informação.
    • Adaptativa: para melhor o desempenho, para acrescentar tabelas ou campos ou para dar permissões de acessos.

    Conforme afirmam Coronel e Rob (2011), há duas abordagens clássicas tradicionais que podem ser adotadas como
    estratégia de modelagem em um diagrama de entidade-relacionamentos:

    • Estratégia top-down: inicializa-se identificando os conjuntos de dados e, em seguida, são definidos os elementos
      de cada um desses conjuntos. O processo envolve a identificação de diferentes tipos de entidades e a definição de
      cada atributo. Esta técnica é utilizada em banco de dados maiores.

    • Estratégia bottom-up: primeiramente são identificados os elementos de dados, ou seja, os itens, e então eles são
      agrupados em conjuntos de dados. Neste caso, os atributos são identificados primeiro e, ao agrupá-los, teremos as
      tabelas. Geralmente, esta técnica é utilizada em banco de dados pequenos.

    As abordagens top-down e bottom-up acabam se complementando, pois muitas vezes um analista ou projetista aplica as
    duas técnicas no mesmo banco de dados a ser modelado, surgindo então uma abordagem mista, denominada middle-up-down.

    -------------------------------------------------- [ Página 10 ] --------------------------------------------------
    A modelagem conceitual em um projeto de banco de dados é considerada de alto nível, pois possui como finalidade a
    fácil compreensão entre os usuários envolvidos na modelagem, como ressaltam Korth, Silberschatz e Sudarshan (2012).
    O foco da modelagem conceitual (Quadro 3.1) é detalhar e discutir o funcionamento do negócio do cliente e não o uso
    de determinada tecnologia, descartando dados de como as informações serão armazenadas e depois recuperadas em banco
    de dados.

    ---------------------------------------------------- Quadro 3.1 ----------------------------------------------------
    Assim que o modelo lógico começar a ser implementado, o modelo conceitual servirá de apoio à construção do esquema
    do banco de dados. Navathe e Ramez (2005) afirmam que durante ou mesmo ao término do esquema conceitual, as
    operações básicas do modelo de dados podem ser usadas para especificar as operações de alto nível do usuário e
    servem para verificar se o modelo possui todos os requisitos listados pelo cliente.

    Para criar um modelo lógico e mais coeso do banco de dados, são necessárias várias revisões na descrição do modelo
    conceitual (de alto nível) e, desta forma, encontrar:

    • Tabelas: em substantivos, objetos reais e objetos que podem armazenar informações.

    -------------------------------------------------- [ Página 11 ] --------------------------------------------------
    • Campos: em características específicas de algum objeto ou adjetivos.
    • Relacionamentos: em verbos que “ligam” uma tabela a outra.
    • Cardinalidades: a quantidade de vezes que cada tabela pode estar relacionada com outra.

    Algumas normas precisam ser adotadas durante a criação do modelo lógico do banco de dados, na criação do diagrama de
    entidade-relacionamentos. Estão elencadas abaixo as principais regras que norteiam os fundamentos da modelagem de
    dados, conforme adaptado de Heuser (2011):

    • Em casos de relacionamento 1 para N: a chave primária do lado 1 sempre deverá estar na tabela do lado N como uma
      chave estrangeira.

    • Em casos de relacionamento N para N: o relacionamento passa a ser implementado como tabela própria que possui
      campos específicos relacionados entre as duas tabelas que deram origem a esta nova tabela, chamada tabela
      associativa.

    • As tabelas devem ter o número reduzido de chaves primárias ao mínimo possível, ou seja, sempre que possível, uma
      tabela deverá ter somente um identificador único, evitando chaves alternativas.

    ASSIMILE
    Os modelos de dados podem estar classificados como: modelo de alto nível, modelo intermediário e modelo de baixo
    nível. O de alto nível é o modelo conceitual, que fornece uma visão mais próxima de como os usuários realmente
    enxergam os dados. O modelo físico fornece uma visão mais detalhada de como realmente o dado será armazenado dentro
    do SGBD. O modelo intermediário está entre os dois tipos (alto nível e baixo nível) e faz uma espécie de ligação.
    Usa-se o modelo conceitual para a construção de um esquema lógico de banco de dados e que será depois implementado
    no SGBD (pelo modelo físico).

    Na maioria dos projetos existe uma grande quantidade de tabelas e campos envolvidos. É necessário criar padrões de
    desenvolvimento para evitar problemas de conflito de nomes de

    -------------------------------------------------- [ Página 12 ] --------------------------------------------------
    atributos, por exemplo. Em uma modelagem em que dois ou três analistas ou programadores estejam trabalhando, caso
    não haja um padrão, o mesmo campo pode ser criado e referenciado com nomes diferentes, dificultando uma consulta ou
    alguma manutenção realizada posteriormente. É necessário criar o dicionário de dados para estabelecer uma
    padronização e uma documentação sobre cada tabela criada. Korth, Silberschatz e Sudarshan (2012) mencionam um
    dicionário como uma descrição de dados, ou seja, contém metadados que são detalhes dos dados armazenados na tabela.
    Observe no Quadro 3.2 um exemplo simplificado de dicionário de dados.

    ---------------------------------------------------- Quadro 3.2 ----------------------------------------------------
    Cada empresa de desenvolvimento de software possui o seu próprio padrão de dicionário de dados, porém, Korth,
    Silberschatz e Sudarshan (2012) afirmam que um dicionário de dados deve ter várias informações, como as seguintes:

    • Descrição dos nomes das tabelas, relações e atributos.
    • Tipos dos dados (domínio) e seus respectivos tamanhos.
    • Descrição detalhada das chaves utilizadas.
    • Nomes dos usuários com suas permissões sobre a tabela.

    -------------------------------------------------- [ Página 13 ] --------------------------------------------------
    O nível de detalhamento do dicionário de dados é opcional, mas ele acaba se tornando um documento fundamental, sendo
    muito requisitado quando o banco de dados apresenta problemas e precisa sofrer manutenção. É comum que a pessoa que
    realizará a manutenção não seja a mesma que criou o banco de dados, por isso a documentação dos campos é fundamental
    para acelerar o processo de manutenção. O Quadro 3.3 mostra outra forma de dicionário de dados, mais robusta e com
    mais informações.

    ---------------------------------------------------- Quadro 3.3 ----------------------------------------------------

    -------------------------------------------------- [ Página 14 ] --------------------------------------------------
    PESQUISE MAIS
    Saiba mais sobre o uso de metadados como forma de padronização, sendo utilizados em bibliotecas digitais como
    ambiente propício para a recuperação da informação.

    PESQUISE MAIS
    CASTRO, F. F.; SANTOS, P. L. V. A. C. Os metadados como instrumentos tecnológicos na padronização e potencialização
    dos recursos informacionais no âmbito das bibliotecas digitais na era da web semântica. Inf. & Soc.: Est., João
    Pessoa, v. 17, n. 2, p.13-19, maio/ago. 2007. Disponível em: <https://bit.ly/2Awx2Dw>. Acesso em: 1 ago. 2018.

    Para exemplificar um modelo lógico de entidaderelacionamento, vamos modelar um estudo de caso. Uma imobiliária
    especializada em aluguel de casas e apartamentos do litoral de Santa Catarina necessita de um software para ajudar
    no gerenciamento dos aluguéis e oferecer melhores ofertas para seus clientes. Após diversos contatos com a
    imobiliária, ficou estabelecido que os seguintes requisitos deveriam ser atendidos pelo banco de dados:

    • Para cada imóvel deverá ter registrado: seu tipo (casa ou apartamento), quantidade de quartos e banheiros, se
      possui vista para o mar e preço da diária.

    • As informações dos proprietários e dos inquilinos deverão ser armazenadas separadamente. Os proprietários podem
      ter vários imóveis que podem ser alugados para vários inquilinos.

    • Além das informações sobre o munícipio ao qual o imóvel pertence, deverá também ser informado o nome da praia mais
      próxima a ele.

    • Os imóveis são todos os itens que compõem a mobília, e os mais verificados são: cama, geladeira, freezer,
      televisor, ar-condicionado, entre outros. Neste caso, é importante que seja informada a quantidade de cada item.

    • Deverá ser realizado e registrado um contrato exclusivo para os aluguéis com os inquilinos e os imóveis
      respectivamente alugados por eles.

    -------------------------------------------------- [ Página 15 ] --------------------------------------------------
    Com os requisitos listados, podemos identificar primeiramente as entidades que se destacam: imóvel, tipo de imóvel,
    cidade, praia, proprietário, inquilino, contrato de aluguel e mobília.

    Para expressar graficamente o diagrama de entidade-relacionamentos, utilizamos a notação “Pé de Galinha” de James
    Martin, de acordo com Coronel e Rob (2011). Para entender o diagrama da Figura 3.1, observe as entidades e seus
    atributos.

    ---------------------------------------------------- Figura 3.1 ----------------------------------------------------
    Para melhor entendimento do diagrama da imobiliária, considere os seguintes itens:
    • Observe as setas que ligam as tabelas, o lado que tem três pontas está representando o lado N, o que possui uma
      ponta é o lado 1.

    • Observe que há as siglas PK e FK em alguns campos.
    • PK significa Primary Key ou a chave primária da tabela.
    • FK significa Foreign Key ou a chave estrangeira da tabela.

    O dicionário de dados da tabela imóvel pode ser observado no Quadro 3.4. Para fins didáticos, estamos criando o
    dicionário de somente uma tabela e com poucos campos. Vale ressaltar que os acentos das palavras foram preservados,
    mas na criação do modelo físico no SGBD, os acentos deverão ser evitados.

    -------------------------------------------------- [ Página 16 ] --------------------------------------------------

    ---------------------------------------------------- Quadro 3.4 ----------------------------------------------------

    REFLITA
    Na Figura 3.1 é demonstrado o diagrama de entidade-relacionamentos como sendo uma solução inicial para a modelagem
    do banco de dados da imobiliária. Em um DER sempre podemos agregar mais tabelas, além das que aparecem
    explicitamente no enunciado. Uma situação que o cliente não levantou foi a questão do contrato que o proprietário
    deve ter em relação ao seu imóvel. O que você faria para criar um contrato para o proprietário? Outra situação é que
    a imobiliária pode expandir suas atividades para outros estados. Como você poderia criar uma relação entre cidade,
    estado e praias?

    Nesta seção você pôde conhecer mais alguns aspectos do processo de modelagem de dados, como as estratégias de
    modelagem top-down e bottom-down e a documentação do desenvolvimento de um diagrama de entidade-relacionamentos.

    -------------------------------------------------- [ Página 17 ] --------------------------------------------------
    Em sua vida profissional você conhecerá e usará modelos diferentes, adaptados pelas empresas de acordo com suas
    necessidades de desenvolvimentos. A necessidade de apartação das novas tecnologias determinará o seu sucesso
    profissional. Na próxima seção, abordaremos os padrões de modelagem com UML, uma linguagem de modelagem unificada e
    muito utilizada na programação orientada a objetos.
    """
