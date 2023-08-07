import sqlite3

class RegisterSystem:
    # Database
    def __init__(self):
        self.conn = sqlite3.connect("StudentSystem.db")
        self.c = self.conn.cursor()
        self.create_table()

        # Creating Table

    def create_table(self):
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS students
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        genero TEXT NOT NULL,
                        nascimento TEXT NOT NULL,
                        endereco TEXT NOT NULL,
                        curso TEXT NOT NULL,
                        imagem TEXT NOT NULL)"""
        )

        # Create Function

    def create(self, students):
        self.c.execute(
            "INSERT INTO students (nome, email, telefone, genero, nascimento, endereco, curso, imagem) VALUES (?,?,?,?,?,?,?,?)",
            (students),
        )
        self.conn.commit()

        # Read Function

    def read(self):
        self.c.execute("SELECT * FROM students")
        data = self.c.fetchall()

        return data

        # Search Function

    def search(self, id):
        self.c.execute("SELECT * FROM students WHERE id = ?", (id,))
        data = self.c.fetchone()

        return data

        # Update Function

    def update(self, valores):
        query = "UPDATE students SET nome=?, email=?, telefone=?, genero=?, nascimento=?, endereco=?, curso=?, imagem=? WHERE id=?"
        self.c.execute(query, valores)
        self.conn.commit()

        # Delete Function

    def delete(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()
        
    # Close the database
    def __del__(self):
        self.conn.close()
registersystem = RegisterSystem()
