import gspread
from openpyxl.utils import column_index_from_string
from gspread_dataframe import set_with_dataframe
import os.path
import json
from oauth2client.service_account import ServiceAccountCredentials


def google_sheets_export(dataframe, sheet, column):

    api, key = _api_key_get()

    gc = gspread.service_account(filename=api)
    sh = gc.open_by_key(key)

    worksheet = sh.worksheet(sheet)
    column = column_index_from_string(column)

    first_empty_row = _find_first_empty_cell(worksheet)

    if first_empty_row + len(dataframe) > worksheet.row_count:
        worksheet.add_rows(first_empty_row + len(dataframe) - worksheet.row_count)

    set_with_dataframe(worksheet, dataframe, row=first_empty_row, col=column, include_column_header=False)


def _find_first_empty_cell(worksheet):

    values = worksheet.get_all_values()
    return len(values)+1


def validate_api_key():

    api, key = _api_key_get()

    if not os.path.isfile(api):
        return "Error: API file not found"

    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(api, ["https://spreadsheets.google.com/feeds"])
        gc = gspread.authorize(credentials)
    except Exception as e:
        return "Error: Failed to authenticate with Google Sheets API:", e

    try:
        sh = gc.open_by_key(key)
    except Exception as e:
        return "Error: Failed to access Google Sheet:", e

    return "Api and key info valid"


def _api_key_get():
    with open("api_key.json", 'r') as f:
        info = json.load(f)

    return info[0], info[1]
