from models.DataPE3 import DataPE3
from repositories.Repository import Repository


class DataPE3Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_PE3')


    def __dbrowToModel(self, item: dict):
        return DataPE3(annee=item['annee'], data_di=item['data_DI'], data_sa=item['data_SA'], data_cp=item['data_CP'], data_ca=item['data_CA'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

