from Models.DataF3 import DataF3
from Repositories.Repository import Repository


class DataF3Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_F3')


    def __dbrowToModel(self, item: dict):
        return DataF3(annee=item['annee'], data_di=item['data_DI'], data_sa=item['data_SA'], data_cp=item['data_CP'], data_ca=item['data_CA'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

