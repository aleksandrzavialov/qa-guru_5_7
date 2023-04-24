import os
import time
from selenium import webdriver
from selene import browser
from zipfile import ZipFile

from conftest import PROJECT_TMP_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
def test_file_downloading_via_browser():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": PROJECT_TMP_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(10)
    browser.quit()

    downloaded_file = os.path.join(PROJECT_TMP_PATH, 'pytest-main.zip')
    size = os.path.getsize(downloaded_file)
    assert size > 1000000
    with ZipFile(downloaded_file) as hello_zip:
        archived_folder_files = [archive_element.filename for archive_element in hello_zip.infolist()]
        assert archived_folder_files[0] == 'pytest-main/'
        for archive_element in archived_folder_files:
            assert archive_element.startswith('pytest-main/')
