from models.DataPE1 import DataPE1
from repositories.Repository import Repository


class DataPE1Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_PE1')


    def __dbrowToModel(self, item: dict):
        return DataPE1(annee=item['annee'], data_tr=item['data_TR'], data_ta=item['data_TA'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

