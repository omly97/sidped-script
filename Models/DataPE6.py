class DataPE6:

    def __init__(self, annee, data_pats, data_n) -> None:
        self.__annee = annee
        self.__data_pats = data_pats
        self.__data_n = data_n

    
    def get_intitule(self):
        return "Existance de d’accords"

    
    def get_code(self):
        return "PE6"


    def get_cible_str(self):
        return "≥ 80%"

    
    def get_cible_numeric(self):
        return 80


    def calculate_score(self):
        score = (self.__data_pats * 100) / self.__data_n
        return round(score, 2)


    def get_stats(self):
        return {
            'annee': self.__annee,
            'intitule': self.get_intitule(),
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

