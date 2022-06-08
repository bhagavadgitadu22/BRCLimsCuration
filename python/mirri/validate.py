#!C:\Users\mboutrou\AppData\Local\Programs\Python\Python310\python.exe
import sys
from pathlib import Path
from mirri.validation.excel_validator import validate_mirri_excel
import warnings
warnings.simplefilter("ignore")

def main(way):
    count_pubmed = 0
    count_first_page = 0
    count_nagoya = 0

    path = Path(way)
    error_log = validate_mirri_excel(path.open("rb"))

    for errors in error_log.get_errors().values():
        for error in errors:
            if 'If the those values are Pubmed ids or DOIs, please ignore this messsage' in error.message:
                count_pubmed += 1
            elif "The 'First page' for literature with ID" in error.message:
                count_first_page += 1
            elif 'The value is missing or not associated with a country for strain' in error.message:
                count_nagoya += 1
            else:
                print(error.pk, error.message, error.code)

    print(count_pubmed)
    print(count_first_page)
    print(count_nagoya)

if __name__ == "__main__":
    main('C:/Users/mboutrou/Documents/mirri/brclims_excel.xlsx')
