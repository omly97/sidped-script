from Models.DataPE6 import DataPE6
from Repositories.Repository import Repository


class DataPE6Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_PE6')


    def __dbrowToModel(self, item: dict):
        return DataPE6(annee=item['annee'], data_pats=item['data_PATS'], data_n=item['data_N'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

