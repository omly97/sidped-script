class DataF3:

    def __init__(self, annee, data_di, data_sa, data_cp, data_ca) -> None:
        self.__annee = annee
        self.__data_di = data_di
        self.__data_sa = data_sa
        self.__data_cp = data_cp
        self.__data_ca = data_ca

    
    def get_intitule(self):
        return "Ratio du budget alloué aux subventions des doctorants"


    def get_code(self):
        return "F3"


    def get_cible_str(self):
        return "250 000 / Ni"

    
    def get_cible_numeric(self):
        return 250000


    def calculate_score(self):
        score = (self.__data_di * self.__data_sa * 100) / (self.__data_cp + self.__data_ca)
        return round(score, 2)


    def get_stats(self):
        return {
            'annee': self.__annee,
            'intitule': self.get_intitule(),
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

