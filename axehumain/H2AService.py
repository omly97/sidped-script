from axehumain.HDataService import HDataService
from gsheet.gsheet import GsheetService
from env import GSHEET_HUMAN


class H2AService:

    COLUMN_VALUES = 3

    def __init__(self) -> None:
        self.gsheet = GsheetService(GSHEET_HUMAN['H2A']['spreadsheet_key'])


    # Get Gsheet metadata
    def get_metadata(self):
        return self.gsheet.get_spreadsheet_metadata()


    # Get Gsheet data
    def get_data(self):
        return self.gsheet.get_col_values_from_worksheet(GSHEET_HUMAN['H2A']['worksheet_id'], self.COLUMN_VALUES)


    # Get data calculated
    def get_data_calculated(self):
        data_service = HDataService(data_list=self.get_data())

        Tr = data_service.calulate_Tr()
        Ns = data_service.calulate_Ns()
        Ps = data_service.calulate_Ps()
        As = data_service.calulate_As()
        Ts = data_service.calulate_Ts()
        stats = data_service.fornat_stats(Tr=Tr, Ns=Ns, Ps=Ps, As=As, Ts=Ts)

        round_number = lambda x: round(x, 2)

        score = ((Ts - Ns - Ps) / Tr )* 100

        results = {
            'score': round_number(score),
            'cible': "≥ 20",
            'ecart': round_number(20 - score),
            'success': score >= 20
        }

        return { 'stats': stats, 'results': results }
