class DataPE5:

    def __init__(self, annee, data_a1, data_a2, data_dd) -> None:
        self.__annee = annee
        self.__data_a1 = data_a1
        self.__data_a2 = data_a2
        self.__data_dd = data_dd

    
    def get_code(self):
        return "PE5"


    def get_cible_str(self):
        return "≤ 1/10"

    
    def get_cible_numeric(self):
        return 1/10


    def calculate_score(self):
        return ((self.__data_a1 + self.__data_a2) * 100) / self.__data_dd


    def get_stats(self):
        return {
            'annee': self.__annee,
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

