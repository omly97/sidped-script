class DataPE1:

    def __init__(self, annee, data_tr, data_ta) -> None:
        self.__annee = annee
        self.__data_tr = data_tr
        self.__data_ta = data_ta

    
    def get_code(self):
        return "PE1"


    def get_cible_str(self):
        return "80%"

    
    def get_cible_numeric(self):
        return 80


    def calculate_score(self):
        return (self.__data_tr * 100) / (self.__data_tr + self.__data_ta)


    def get_stats(self):
        return {
            'annee': self.__annee,
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

