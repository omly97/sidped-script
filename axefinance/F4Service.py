from gsheet.gsheet import GsheetService
from env import GSHEET_FINANCE

class F4Service:

    def __init__(self) -> None:
        self.gsheet = GsheetService(GSHEET_FINANCE['F4']['spreadsheet_key'])


    # Get Gsheet metadata
    def get_metadata(self):
        return self.gsheet.get_spreadsheet_metadata()


    # Get Gsheet data
    def get_data(self):
        return self.gsheet.get_data_from_worksheet(GSHEET_FINANCE['F4']['worksheet_id'])


    # Get data calculated
    def get_data_calculated(self):
        data = self.get_data()

        calcul_score = lambda SUM,PIB: (SUM / (10*PIB))
        get_value = lambda data_dict,i: int(str(data_dict[list(data_dict.keys())[i]]).replace(" ", ""))
        round_number = lambda x: round(x, 2)

        for item in data:
            somme = sum([get_value(item, 1), get_value(item, 2), get_value(item, 3), get_value(item, 4), get_value(item, 5)])
            somme = sum([get_value(item, 6), get_value(item, 7), get_value(item, 8), get_value(item, 9), get_value(item, 10)], somme)
            score = calcul_score(somme, get_value(item, 11))
            item.update({
                'score': round_number(score),
                # 'cible': "≥ 20%",
                # 'ecart': round_number(20 - score),
                # 'success': score == 20
            })
        return data
