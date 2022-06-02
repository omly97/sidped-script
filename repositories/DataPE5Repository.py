from models.DataPE5 import DataPE5
from repositories.Repository import Repository


class DataPE5Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_PE5')


    def __dbrowToModel(self, item: dict):
        return DataPE5(annee=item['annee'], data_a1=item['data_A1'], data_a2=item['data_A2'], data_dd=item['data_DD'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

