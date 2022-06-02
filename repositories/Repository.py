import sqlite3

class Repository:

    def __init__(self, tablename) -> None:
        self.__tablename = tablename


    def __dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]

        return d


    def __create_connection(self, db_file="~/Documents/Workspace/Python/Doctorat/databases/database.db"):
        conn = None
        try:
            conn = sqlite3.connect("databases/database.db")
            conn.row_factory = self.__dict_factory
        except sqlite3.Error as e:
            print(e)

        return conn


    def all(self):
        try:
            conn = self.__create_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM {}" . format(self.__tablename))
            return cur.fetchall()

        except:
            return "Error"

        finally:
            cur.close()
            conn.close()


    def find(self, annee: int):
        try:
            conn = self.__create_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM {} WHERE annee = {}" . format(self.__tablename, str(annee)))
            return cur.fetchone()

        except:
            return "Error"

        finally:
            cur.close()
            conn.close()
