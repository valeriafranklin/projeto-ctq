from maquinarioBean import MaquinarioBean
from maquinarioDAO import MaquinarioDAO

class MaquinarioController:

    def __init__(self):
        self.__maquinario_dao = MaquinarioDAO()

    def inserir(self, cod, n, func, est):
        maquinario = MaquinarioBean()
        maquinario.setCodigo(cod)
        maquinario.setNome(n)
        maquinario.setFuncao(func)
        maquinario.setEstado(est)

        self.__maquinario_dao.inserir_maquinario(maquinario)

    def remover(self, cod):
        maquinario = MaquinarioBean()
        maquinario.setCodigo(cod)
        self.__maquinario_dao.remover_maquinario(maquinario)

    def visualizar(self):
        return self.__maquinario_dao.visualizar()

    def atualizar(self, cod, n, func, est):
        maquinario = MaquinarioBean()
        maquinario.setCodigo(cod)
        maquinario.setNome(n)
        maquinario.setFuncao(func)
        maquinario.setEstado(est)

        self.__maquinario_dao.atualizar_maquinario(maquinario)