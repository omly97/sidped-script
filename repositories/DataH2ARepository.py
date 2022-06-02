from models.DataH2A import DataH2A
from repositories.Repository import Repository


class DataH2ARepository(Repository):

    def __init__(self) -> None:
        super().__init__(tablename='data_H2A')


    def __dbrowToModel(self, item: dict):
        return DataH2A(annee=item['annee'], data_ts=item['data_TS'], data_ns=item['data_NS'], data_ps=item['data_PS'], data_tr=item['data_TR'])


    def all(self):
        return [self.__dbrowToModel(item) for item in super().all()]


    def find(self, annee: int):
        return self.__dbrowToModel(super().find(annee))

