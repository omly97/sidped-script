from Models.DataH1 import DataH1
from Repositories.Repository import Repository


class DataH1Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_H1')


    def __dbrowToModel(self, item: dict):
        return DataH1(annee=item['annee'], data_dt=item['data_DT'], data_dr=item['data_DR'], data_at=item['data_AT'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

