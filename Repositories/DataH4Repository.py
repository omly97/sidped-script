from Models.DataH4 import DataH4
from Repositories.Repository import Repository


class DataH4Repository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_H4')


    def __dbrowToModel(self, item: dict):
        return DataH4(annee=item['annee'], data_ts=item['data_TS'], data_ns=item['data_NS'], data_ps=item['data_PS'], data_tr=item['data_TR'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

