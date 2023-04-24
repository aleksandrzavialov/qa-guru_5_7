import os
from conftest import PROJECT_TMP_PATH
from helper_functions import file_helpers

archived_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources'))


def test_pdf_archiving():
    file_helpers.archive_directory(archived_dir, 'resources.zip', PROJECT_TMP_PATH)
    tested_pdf_file = os.path.join(archived_dir, 'docs-pytest-org-en-latest.pdf')
    assert file_helpers.check_file_in_archive(os.path.join(PROJECT_TMP_PATH, 'resources.zip'), tested_pdf_file)


def test_xls_archiving():
    file_helpers.archive_directory(archived_dir, 'resources.zip', PROJECT_TMP_PATH)
    tested_xls_file = os.path.join(archived_dir, 'file_example_XLS_10.xls')
    assert file_helpers.check_file_in_archive(os.path.join(PROJECT_TMP_PATH, 'resources.zip'), tested_xls_file)


def test_xlsx_archiving():
    file_helpers.archive_directory(archived_dir, 'resources.zip', PROJECT_TMP_PATH)
    tested_xlsx_file = os.path.join(archived_dir, 'file_example_XLS_10.xls')
    assert file_helpers.check_file_in_archive(os.path.join(PROJECT_TMP_PATH, 'resources.zip'), tested_xlsx_file)


def test_zip_archiving():
    file_helpers.archive_directory(archived_dir, 'resources.zip', PROJECT_TMP_PATH)
    tested_zip_file = os.path.join(archived_dir, 'hello.zip')
    assert file_helpers.check_file_in_archive(os.path.join(PROJECT_TMP_PATH, 'resources.zip'), tested_zip_file)
