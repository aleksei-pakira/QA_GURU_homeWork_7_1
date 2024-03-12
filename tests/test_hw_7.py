import zipfile
import csv
from pypdf import PdfReader
from io import BytesIO
from xlrd import open_workbook
from tests.conftest import archive


def test_csv():
    with zipfile.ZipFile(archive) as zip_file:
        with zip_file.open('sample_1.csv') as csv_file:
            content = csv_file.read().decode('ISO-8859-1')
            csvreader = list(csv.reader(content.splitlines()))
            second_row = csvreader[1]

            assert second_row[0] == '2'
            assert second_row[1] == '1.7 Cubic Foot Compact "Cube" Office Refrigerators'
            assert second_row[2] == 'Barry French'

def test_xls():
    with zipfile.ZipFile(archive) as zip_file:
        with zip_file.open('file_example_1000.xls') as xls_file:
            content = xls_file.read()
            buffer = BytesIO(content)
            workbook = open_workbook(file_contents=buffer.read())
            count_sheets_xls = workbook.nsheets
            check_name_xls = workbook.sheet_names()
            first_sheet_xls = workbook.sheet_by_index(0)
            count_rows_xls = first_sheet_xls.nrows

            assert count_sheets_xls == 1
            assert check_name_xls == ['Sheet1']
            assert count_rows_xls == 1001

def test_pdf():
    with zipfile.ZipFile(archive) as zip_file:
        with zip_file.open('file_example_1.pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            page_count = len(reader.pages)
            page = reader.pages[0]
            text = page.extract_text()

            assert page_count == 1
            assert text.__contains__("PDF Test File")











