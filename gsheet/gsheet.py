import gspread
from google.oauth2.service_account import Credentials


class GsheetService:

    def __init__(self, spreadsheet_key):
        self.spreadsheet_key = spreadsheet_key


    def __gspread_connection(self):
        # define the scope
        scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        # add credentials to the account
        credentials = Credentials.from_service_account_file('gsheet/auth.json', scopes=scopes)

        # authorize the clientsheet 
        gspread_client = gspread.authorize(credentials)

        return gspread_client


    def get_spreadsheet_metadata(self):
        # connection
        gspread_client = self.__gspread_connection()

        # open Google Sheet file
        spreadsheet = gspread_client.open_by_key(self.spreadsheet_key)

        # return infos
        return {
            'id': spreadsheet.id,
            'creationTime': spreadsheet.creationTime,
            'lastUpdateTime': spreadsheet.lastUpdateTime,
            'timezone': spreadsheet.timezone,
            'title': spreadsheet.title,
            'url': spreadsheet.url,
        }


    def get_data_from_worksheet(self, worksheet_id, data_dict=True):
        # connection
        gspread_client = self.__gspread_connection()

        # open Google Sheet file
        spreadsheet = gspread_client.open_by_key(self.spreadsheet_key)

        # get sheet of the Spreadsheet
        sheet = spreadsheet.get_worksheet_by_id(worksheet_id)

        # retrieve all records
        return sheet.get_all_records() if data_dict == True else sheet.get_all_values()


    def get_col_values_from_worksheet(self, worksheet_id, col_index):
        # connection
        gspread_client = self.__gspread_connection()

        # open Google Sheet file
        spreadsheet = gspread_client.open_by_key(self.spreadsheet_key)

        # get sheet of the Spreadsheet
        sheet = spreadsheet.get_worksheet_by_id(worksheet_id)

        # retrieve all records
        return sheet.col_values(col_index)[1::]

