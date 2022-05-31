from Models.DataF2 import DataF2
from Repositories.Repository import Repository


class DataF2Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_F2')


    def __dbrowToModel(self, item: dict):
        return DataF2(annee=item['annee'], data_cp=item['data_CP'], data_ca=item['data_CA'], data_b=item['data_B'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

