import sqlite3

# registro


class reg:
    # conexao com banco de dados
    def __init__(self):
        self.conn = sqlite3.connect("dados.db")
        self.c = self.conn.cursor()
        self.create_table()
        # criacao de tabela

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS registros
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        genero TEXT NOT NULL,
                        nascimento TEXT NOT NULL,
                        endereco TEXT NOT NULL,
                        curso TEXT NOT NULL,
                        imagem TEXT NOT NULL)''')
        # funcao registrar

    def registrar(self, registros):
        self.c.execute(
            "INSERT INTO registros (nome, email, telefone, genero, nascimento, endereco, curso, imagem) VALUES (?,?,?,?,?,?,?,?)", (registros))
        self.conn.commit()
        # visualizar usuario

    def visualizar_dados(self):
        self.c.execute("SELECT * FROM registros")
        dados = self.c.fetchall()
        for i in dados:
            print(f"ID: {i[0]} | Nome: {i[1]} | Email: {i[2]} | Telefone: {i[3]} | Genero: {i[4]} | Data de Nascimento: {i[5]} | Endereço: {i[6]} | Curso: {i[7]} | Imagem:{i[8]} ")
        # buscar usuario

    def buscar_dados(self, id):
        self.c.execute("SELECT * FROM registros WHERE id = ?", (id,))
        dados = self.c.fetchone()
        print(f"ID: {dados[0]} | Nome: {dados[1]} | Email: {dados[2]} | Telefone: {dados[3]} | Genero: {dados[4]} | Data de Nascimento: {dados[5]} | Endereço: {dados[6]} | Curso: {dados[7]} | Imagem:{dados[8]} ")
        # atualizar usuario

    def atualizar_dados(self, valores):
        query = "UPDATE registros SET nome=?, email=?, telefone=?, genero=?, nascimento=?, endereco=?, curso=?, imagem=? WHERE id=?"
        self.c.execute(query, valores)
        self.conn.commit()
        # deletar usuario

    def deletar_dados(self, id):
        self.c.execute("DELET FROM registros WHERE id=?", (id,))
        self.conn.commit
