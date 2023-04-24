import os.path
import requests

from conftest import PROJECT_TMP_PATH


def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    downloaded_file = os.path.join(PROJECT_TMP_PATH, 'selenium_logo.png')
    r = requests.get(url)
    with open(downloaded_file, 'wb') as file:
        file.write(r.content)

    size = os.path.getsize(downloaded_file)
    assert size == 30803
