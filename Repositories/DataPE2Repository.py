from Models.DataPE2 import DataPE2
from Repositories.Repository import Repository


class DataPE2Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_PE2')


    def __dbrowToModel(self, item: dict):
        return DataPE2(annee=item['annee'], data_cp=item['data_CP'], data_ca=item['data_CA'], data_b=item['data_B'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

