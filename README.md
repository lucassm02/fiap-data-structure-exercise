# CAP 11 - CRIANDO NOVOS TIPOS DE DADOS - AGILIDADE PARA ATENDIMENTO A MORADORES DE RUA

O inverno no Brasil geralmente começa no final de junho e vai até o final de setembro. O inverno é o período em que os moradores de rua mais necessitam de ajuda. Atualmente, existem campanhas e ONGs que auxiliam pessoas nessa estação, assim como nas demais também.

Segundo pesquisa publicada em 2017, pelo Instituto de Pesquisa Econômica Aplicada (Ipea), o Brasil tem aproximadamente 100 mil pessoas vivendo nas ruas.

De acordo com o Ministério do Desenvolvimento Social, em  decreto nº 7.053 de 2009, Art. 1º, Parágrafo único: “considera-se população em situação de rua o grupo populacional heterogêneo que possui em comum a pobreza extrema, os vínculos familiares interrompidos ou fragilizados e a inexistência de moradia convencional regular, e que utiliza os logradouros públicos e as áreas degradadas como espaço de moradia e de sustento, de forma temporária ou permanente, bem como as unidades de acolhimento para pernoite temporário ou como moradia provisória”.

Pensando em auxiliar a Organização sem fins lucrativos de assistência humanitária “Aquece a alma e o coração” no processo de atendimento dessa população, ao distribuir sopas e pães, considerando a máxima agilidade e qualidade do atendimento, em função do frio,

 - A Van da ONG chega no local de distribuição às 20:00, quando é feita a entrega de um papel com o horário de entrada na fila de atendimento. Essa quantidade deve ser gerada de maneira aleatória, não ultrapassando o máximo de 15 moradores.

- Por questão de acomodação no local, a fila pode conter apenas 15 moradores de rua por vez.


- O próprio motorista da Van inicia a distribuição dos alimentos às 20h10 (1 estação de entrega), mas ele pode contar com a ajuda de mais um voluntário se necessário (2 estações de entrega).

- O tempo de servir a sopa em um recipiente e juntar o pão para a entrega é de X minutos (X=resto da divisão dos últimos 2 dígitos do seu RM por 3 somado a 1);

- Para agilizar o processo de entrega, são preparados 3 pratos simultaneamente (pode ser menos apenas no momento em que a fila tiver menos do que 3 pessoas);

- A cada 2 minutos, mais um morador de rua entra na fila;

- Quando o morador de rua recebe o alimento é calculado o tempo de espera usando a informação do papel que o motorista entregou com o horário de entrada.

Para simular uma situação real como esta, é preciso que o programa desenvolvido tenha uma repetição onde cada 10 iterações represente o avanço de 1 minuto no relógio ou utilize uma função que contabilize esse tempo de maneira real.   Conhecendo o tempo requerido para servir (X minutos) ou entrar na fila (2 minutos) o programa deve esperar o tempo correto para ocorrerem.

Supondo que a quantidade de alimentos é sempre maior do que a quantidade de moradores o programa deve ser encerrado apenas quando não houver mais nenhum morador na fila.