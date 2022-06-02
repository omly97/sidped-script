class DataH3:

    def __init__(self, annee, data_ts, data_ns, data_ps, data_tr) -> None:
        self.__annee = annee
        self.__data_ts = data_ts
        self.__data_ns = data_ns
        self.__data_ps = data_ps
        self.__data_tr = data_tr


    def get_intitule(self):
        return "Comportement individuel des PPD"


    def get_code(self):
        return "H3"


    def get_cible_str(self):
        return "≥ 20"

    
    def get_cible_numeric(self):
        return 20


    def calculate_score(self):
        score = ((self.__data_ts - self.__data_ns - self.__data_ps) * 100) / self.__data_tr
        return round(score, 2)


    def get_stats(self):
        return {
            'annee': self.__annee,
            'intitule': self.get_intitule(),
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

