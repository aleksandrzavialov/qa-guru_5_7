import datetime
import os
from zipfile import ZipFile, ZIP_DEFLATED


def archive_directory(path, archive_name, target_directory):
    file_dir = os.listdir(path)
    with ZipFile(os.path.join(target_directory, archive_name), mode='w', compression=ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.abspath(os.path.join(path, file))
            zf.write(add_file, file)


def check_file_in_archive(archive_file, checked_file):
    with ZipFile(archive_file, mode='a') as zf:
        for file in zf.infolist():
            if str(datetime.datetime(*file.date_time))[0:16] == \
                    datetime.datetime.fromtimestamp(os.path.getmtime(checked_file)).strftime('%Y-%m-%d %H:%M:%S.%f')[
                    :-3][0:16] \
                    and os.path.basename(file.filename) == os.path.basename(checked_file) \
                    and os.path.getsize(checked_file) == file.file_size:
                return True
