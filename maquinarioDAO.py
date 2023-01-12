import psycopg2

class MaquinarioDAO:

    def __init__(self):
        self.conexao = psycopg2.connect(database="sysmilk", user="adm_sysmilk", password="admsysmilk", host="sysmilk.cnbkkiavari1.us-east-1.rds.amazonaws.com", port="5432")

        self.cursor = self.conexao.cursor()

    def inserir_maquinario(self, maquinario):
        sql = f"insert into maquinario values ({maquinario.getCodigo()}, '{maquinario.getNome()}', '{maquinario.getFuncao()}', '{maquinario.getEstado()}')"

        self.cursor.execute(sql)
        self.conexao.commit()

    def remover_maquinario(self, maquinario):
        sql = f"delete from maquinario where codigo = {maquinario.getCodigo()}"

        self.cursor.execute(sql)
        self.conexao.commit()

    def atualizar_maquinario(self, maquinario):
        sql = f"update maquinario set nome = '{maquinario.getNome()}', funcao = '{maquinario.getFuncao()}', estado = '{maquinario.getEstado()}' where codigo = {maquinario.getCodigo()}"

        self.cursor.execute(sql)
        self.conexao.commit()

    def visualizar(self):
        sql = "select * from maquinario"
        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()
        texto = ""

        for linha in resultado:
            texto = texto + f"Código: {str(linha[0])} \nNome: {str(linha[1])} \nFunção: {str(linha[2])} \nEstado: {str(linha[3])} \n \n"
 
        return texto