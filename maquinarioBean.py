class MaquinarioBean:

    def __init__(self):
        self.__codigo = None
        self.__nome = None
        self.__funcao = None
        self.__estado = None

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getFuncao(self):
        return self.__funcao
        
    def getEstado(self):
        return self.__estado

    def setCodigo(self, cod):
        self.__codigo = cod

    def setNome(self, n):
        self.__nome = n

    def setFuncao(self, fun):
        self.__funcao = fun

    def setEstado(self, est):
        self.__estado = est