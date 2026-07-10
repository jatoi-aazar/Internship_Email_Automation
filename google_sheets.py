from gspread import Worksheet
from typing import Dict
import gspread
from config import CREDENTIALS_PATH , SPREADSHEET , WORKSHEET_INDEX , PROCESSED_COLUMN

def get_client(credentials_path) -> gspread.Client:

    sheets_client = gspread.service_account(credentials_path)

    return sheets_client
    
client = get_client(CREDENTIALS_PATH)

def get_worksheet(client: gspread.Client , spreadsheet_name: str , worksheet_index: int) -> gspread.Worksheet:
    
    spreadsheet = client.open(spreadsheet_name)
    worksheet = spreadsheet.get_worksheet(worksheet_index)

    return worksheet

worksheet = get_worksheet(client , SPREADSHEET , WORKSHEET_INDEX)


def get_unprocessed_applicants(worksheet: gspread.Worksheet):

    records = worksheet.get_all_records()
    applicants = []

    for row_number , record in enumerate(records, start=2):
        processed = str(record["Processed"]).strip().upper()

        if processed != "TRUE": 
            applicant = {
            "row_number" : row_number,
            "timestamp" : record["Timestamp"],
            "name": record["Enter Your Name"],
            "email": record["\nEnter Your Email"],
            "department": record["Choose Your Department"],
            "experience": record["Any Internship Experience?"],
            "processed": record["Processed"]
    }
            applicants.append(applicant)

    return applicants

def mark_applicant_processed(worksheet: gspread.Worksheet , row_number: int):
    
    cell = worksheet.find(PROCESSED_COLUMN)

    processed_col = cell.col

    worksheet.update_cell(row_number , processed_col , True)




