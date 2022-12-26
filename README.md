# SysMilk - Controle de Maquinário - CTq

O SysMilk é um projeto de software a ser desenvolvido por discentes do nível médio técnico integrado em Informática do IFRN, visando auxiliar a evolução do Centro de Tecnologia do Queijo por meio do controle de maquinário. O software será desenvolvido em Python e fará uso do PostgreSQL 15.1, sendo executado localmente.


## 01. Necessidades do Cliente

O Centro de Tecnologia do Queijo (CTq) do IFCN é um espaço destinado ao desenvolvimento de tarefas práticas que são tanto capazes de capacitar tecnicamente os discentes do curso integrado em Alimentos, quanto essencial no que diz respeito à comunidade do IFRN, tendo em vista que realiza a produção de alimentos lácteos (doce de leite, iogurte e queijo), fortificando a dieta de alunos e servidores que consomem esses produtos.

Após uma visita feita ao local, pôde-se observar a lacuna ainda existente em relação ao controle de maquinário. Sendo assim, o presente projeto tem como objetivo automatizar o gerenciamento das máquinas e equipamentos, dispondo os dados manipulados em um Banco de Dados e facilitando o serviço dos funcionários, permitindo que hajam consultas e o manuseio de informações.

O controle de maquinário será capaz de permitir com que os funcionários tenham domínio do que se passa no Centro de Tecnologia, mesmo que não estejam no ambiente. Desse modo, será possível ter ciência das máquinas existentes - por meio dos IDs -, os tipos de máquinas - por meio dos nomes -, a situação das máquinas - por meio do estado - e suas funcionalidades - por meio da função -. Além disso, por consequência, é viável pressupor níveis de desgaste, necessidade de novas compras e a economia de acessórios para entrar no CTq, já que possibilita o acompanhamento externo do maquinário.


## 02. Requisitos

### [RF] Requisitos Funcionais

* [RF001] Monitoramento do funcionamento das máquinas

Descrição: O sistema deve conceder ao cliente a capacidade de verificar se determinado equipamento se encontra em condições de uso ativo (apto) ou inativo (inapto).

Prioridade: Essencial.


* [RF002] Cadastro de máquinas

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de cadastrar novas máquinas.

Prioridade: Essencial.


* [RF003] Atualização de máquinas

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de atualizar os dados das máquinas.

Prioridade: Essencial.


* [RF004] Deleção de máquinas

Descrição: O sistema deve conceder aos coordenadores, professores, técnicos e bolsistas a capacidade de deletar máquinas.

Prioridade: Essencial.
