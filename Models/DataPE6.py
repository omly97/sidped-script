class DataPE6:

    def __init__(self, annee, data_pats, data_n) -> None:
        self.__annee = annee
        self.__data_pats = data_pats
        self.__data_n = data_n

    
    def get_code(self):
        return "PE6"


    def get_cible_str(self):
        return "≥ 80%"

    
    def get_cible_numeric(self):
        return 80


    def calculate_score(self):
        return (self.__data_pats * 100) / self.__data_n


    def get_stats(self):
        return {
            'annee': self.__annee,
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

