class DataH1:

    def __init__(self, annee, data_dt, data_dr, data_at) -> None:
        self.__annee = annee
        self.__data_dt = data_dt
        self.__data_dr = data_dr
        self.__data_at = data_at

    
    def get_intitule(self):
        return "Diligence des PPD dans le travail"


    def get_code(self):
        return "H1"


    def get_cible_str(self):
        return "≥ 80%"

    
    def get_cible_numeric(self):
        return 80


    def calculate_score(self):
        score = ((self.__data_dt - self.__data_dr) * 100) / self.__data_at
        return round(score, 2)


    def get_stats(self):
        return {
            'annee': self.__annee,
            'intitule': self.get_intitule(),
            'code': self.get_code(),
            'cible': self.get_cible_str(),
            'score': self.calculate_score(),
        }

