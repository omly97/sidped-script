import sqlite3

class Repository:

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]

        return d


    def create_connection(self, db_file="~/Documents/Workspace/Python/Doctorat/databases/database.db"):
        conn = None
        try:
            conn = sqlite3.connect("databases/database.db")
            # conn.row_factory = self.dict_factory
        except sqlite3.Error as e:
            print(e)

        return conn
