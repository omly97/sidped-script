from Models.DataH2B import DataH2B
from Repositories.Repository import Repository


class DataH2BRepository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_H2B')


    def __dbrowToModel(self, item: dict):
        return DataH2B(annee=item['annee'], data_as=item['data_AS'], data_ts=item['data_TS'], data_tr=item['data_TR'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

