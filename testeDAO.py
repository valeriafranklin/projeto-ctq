from maquinarioBean import MaquinarioBean
from maquinarioDAO import MaquinarioDAO

r = MaquinarioBean()
r.setCodigo(1110)
r.setNome('Prensa')
r.setFuncao('Prensar e retirar o soro')
r.setEstado('Livre')

maq_dao = MaquinarioDAO()

#Inserção na tabela:
#maq_dao.inserir_maquinario(r)

#Remoção da tabela:
#maq_dao.remover_maquinario(r)

#Atualização de dados na tabela:
#maq_dao.atualizar_maquinario(r)

#Visualização da tabela:
#maq_dao.visualizar()
#print(maq_dao.visualizar())