import os
from pypdf import PdfReader
from conftest import PROJECT_RESOURCE_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_pdf_processing():
    pdf_file = os.path.join(PROJECT_RESOURCE_PATH, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_file)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)
    assert number_of_pages == 412
    assert text == 'pytest Documentation\nRelease 0.1\nholger krekel, ' \
                   'trainer and consultant, https://merlinux.eu/\nJul 14, 2022'
