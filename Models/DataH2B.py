class DataH2B:

    def __init__(self, annee, data_as, data_ts, data_tr) -> None:
        self.__annee = annee
        self.__data_as = data_as
        self.__data_ts = data_ts
        self.__data_tr = data_tr


    def get_intitule(self):
        return "Conformité du caractère avec le poste occupé"


    def get_code(self):
        return "H2B"


    def get_cible_str(self):
        return "≥ 80%"

    
    def get_cible_numeric(self):
        return 80


    def calculate_score(self):
        score = ((self.__data_ts + self.__data_as) * 100) / self.__data_tr
        return round(score, 2)


    def get_stats(self):
        return {
            'annee': self.__annee,
            'intitule': self.get_intitule(),
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

