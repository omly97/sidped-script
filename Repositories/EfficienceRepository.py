from Models.Efficience import Efficience
from Repositories.Repository import Repository


class EfficienceRepository(Repository):

    def __init__(self) -> None:
        super().__init__()


    def create_efficience(self, eff: Efficience):
        conn = super().create_connection()
        sql = """
            INSERT INTO efficience(annee, pe1_tr, pe1_ta, pe2_cp, pe2_ca, pe2_b, pe3_d1, pe3_sa, pe3_cp, pe3_ca)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        data = (eff.get_annee(), eff.get_pe1_tr(), eff.get_pe1_ta(), eff.get_pe2_cp(), eff.get_pe2_ca(), eff.get_pe2_b(), eff.get_pe3_d1(), eff.get_pe3_sa, eff.get_pe3_cp(), eff.get_pe3_ca())
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        return cur.lastrowid


    def select_all__efficience(conn):
        conn = super().create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM efficience")

        rows = cur.fetchall()
        # cur.close()
        # conn.close()
        return rows
