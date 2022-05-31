from Models.DataF1 import DataF1
from Repositories.Repository import Repository


class DataF1Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_F1')


    def __dbrowToModel(self, item: dict):
        return DataF1(annee=item['annee'], data_tr=item['data_TR'], data_ta=item['data_TA'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

