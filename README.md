# SysMilk - Controle de Maquinário - CTq

O SysMilk é um projeto de software a ser desenvolvido por discentes do nível médio técnico integrado em Informática do IFRN, visando auxiliar a evolução do Centro de Tecnologia do Queijo por meio do controle de maquinário. O software será desenvolvido em Python e fará uso do PostgreSQL 15.1, sendo executado localmente.


## 01. Necessidades do Cliente

O Centro de Tecnologia do Queijo (CTq) do IFRN campus Currais Novos é um espaço destinado ao desenvolvimento de tarefas práticas que são tanto capazes de capacitar tecnicamente os discentes do curso integrado em Alimentos, quanto essencial no que diz respeito à comunidade do IFRN, tendo em vista que realiza a produção de alimentos lácteos (doce de leite, iogurte e queijo), fortificando a dieta de alunos e servidores que consomem esses produtos.

Após uma visita feita ao local, pôde-se observar a lacuna ainda existente em relação ao controle de maquinário. Sendo assim, o presente projeto tem como objetivo automatizar o gerenciamento das máquinas e equipamentos, dispondo os dados manipulados em um Banco de Dados e facilitando o serviço dos funcionários, permitindo que hajam consultas e o manuseio de informações.

O controle de maquinário será capaz de permitir com que os funcionários tenham domínio do que se passa no Centro de Tecnologia, mesmo que não estejam no ambiente. Desse modo, será possível ter ciência das máquinas existentes (por meio dos IDs e quantidade), os tipos de máquinas (por meio dos nome), a situação das máquinas (por meio do estado) e suas funcionalidades (por meio da função). Além disso, por consequência, é viável pressupor níveis de desgaste, necessidade de novas compras e a economia de acessórios para entrar no CTq, já que possibilita o acompanhamento externo do maquinário.

O usuário deverá selecionar a aba de acordo com o que deseja acessar. Para as funcionalidades de adicionar, atualizar e remover máquinas o usuário deve inserir o código, nome, função, quantidade da máquina e data da realização do processo, após isso o usuário deve confirmar a ação com o botão inferior. Enquanto isso, na aba destinada à visualização, será exibida uma tabela com todas as máquinas já cadastradas, permitindo, assim, a organização do sistema.


## 02. Requisitos

### [RF] Requisitos Funcionais

* [RF001] Cadastro de máquinas

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de cadastrar novas máquinas.

Prioridade: Essencial.


* [RF002] Visualização das máquinas

Descrição: O sistema deve permitir a consulta das máquinas existentes.

Prioridade: Essencial.


* [RF003] Atualização de máquinas

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de atualizar os dados das máquinas.

Prioridade: Essencial.


* [RF004] Deleção de máquinas

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de deletar máquinas.

Prioridade: Essencial.

* [RF005] Monitoramento do funcionamento das máquinas

Descrição: O sistema deve conceder ao cliente a capacidade de verificar se determinado equipamento se encontra em condições de uso ativo (apto) ou inativo (inapto).

Prioridade: Essencial.

* [RF006] Controle de entrada e saída das máquinas

Descrição: O sistema deve conceder ao cliente a capacidade de visualizar a data de chegada (uso) e de saída (desuso) das máquinas.

Prioridade: Essencial.


### [NF] Requisitos Não Funcionais

* [NF001] Controle do nível de desgaste das máquinas

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de acompanhar a vida útil da máquina a partir do seu nível de desgaste.

Prioridade: Desejável.

* [NF002] Necessidade de manutenção das máquinas

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de acompanhar a utilização das máquinas e, a partir disso, sinalizar a necessidade de manutenção delas.

Prioridade: Desejável.

* [NF003] Tempo de funcionamento

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de acompanhar o tempo de funcionamento das máquinas, assimilando-o à sua carga horária de serviço.

Prioridade: Opcional.


## Análise dos Requisítos e Projeto

### Diagramação (casos de uso)

Os requisitos que serão implementados consistem no cadastro, visualização, atualização, monitoramento do funcionamento e deleção de máquinas.

Por meio do diagrama de Caso de Uso, é possível analisar a conexão entre o administrador e as funções de cadastrar, monitorar, atualizar e deletar máquinas.

![Diagrama de casos de uso](https://i.imgur.com/Io0agfw.png)




