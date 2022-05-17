class DataPE1:

    def __init__(self, annee, data_tr, data_ta) -> None:
        self.__annee = annee
        self.__data_tr = data_tr
        self.__data_ta = data_ta

    
    def get_intitule(self):
        return "Fréquence de mise à jour di site web"


    def get_code(self):
        return "PE1"


    def get_cible_str(self):
        return "80%"

    
    def get_cible_numeric(self):
        return 80


    def calculate_score(self):
        score = (self.__data_tr * 100) / (self.__data_tr + self.__data_ta)
        return round(score, 2)


    def get_stats(self):
        return {
            'annee': self.__annee,
            'intitule': self.get_intitule(),
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

