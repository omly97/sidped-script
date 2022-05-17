class DataPE2:

    def __init__(self, annee, data_cp, data_ca, data_b) -> None:
        self.__annee = annee
        self.__data_cp = data_cp
        self.__data_ca = data_ca
        self.__data_b = data_b

    
    def get_intitule(self):
        return "Organisation du module « Méthodologie de préparation de thèse »"


    def get_code(self):
        return "PE2"


    def get_cible_str(self):
        return "≥ 20%"

    
    def get_cible_numeric(self):
        return 20


    def calculate_score(self):
        score = ((self.__data_cp + self.__data_ca) * 100) / self.__data_b
        return round(score, 2)


    def get_stats(self):
        return {
            'annee': self.__annee,
            'intitule': self.get_intitule(),
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

