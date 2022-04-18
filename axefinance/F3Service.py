from gsheet.gsheet import GsheetService
from env import GSHEET_FINANCE

class F3Service:

    def __init__(self) -> None:
        self.gsheet = GsheetService(GSHEET_FINANCE['F3']['spreadsheet_key'])


    # Get Gsheet metadata
    def get_metadata(self):
        return self.gsheet.get_spreadsheet_metadata()


    # Get Gsheet data
    def get_data(self):
        return self.gsheet.get_data_from_worksheet(GSHEET_FINANCE['F3']['worksheet_id'])


    # Get data calculated
    def get_data_calculated(self):
        data = self.get_data()

        calcul_score = lambda NI,SA,CP,CA: ((NI*SA) / (CP+CA)) * 100
        get_value = lambda data_dict,i: int(data_dict[list(data_dict.keys())[i]].replace(" ", ""))
        round_number = lambda x: round(x, 2)

        for item in data:
            score = calcul_score(get_value(item, 1), get_value(item, 2), get_value(item, 3))
            item.update({
                'score': round_number(score),
                'cible': "≥ 20%",
                'ecart': round_number(20 - score),
                'success': score == 20
            })
        return data
